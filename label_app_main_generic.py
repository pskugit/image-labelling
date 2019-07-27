import os
import configparser
import specify_folders
import main_gui_generic
import instructions
import time
import random

from PyQt5 import QtCore, QtGui,QtPrintSupport, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,  QVBoxLayout, QLabel, QMainWindow, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPainter, QPixmap, QIcon, QImage
import sys
from PIL import Image
from pathlib import Path
import numpy as np

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

####
#THIS IS THE CURRENT VERSION
#.ui files are used as .py files
#changes from the designer are to be followed by:
#pyuic5 file.ui -o file.py
#
#to build the exe run in powershell:
#pyinstaller -w -F -i favicon.ico --add-data "favicon.ico;files" --add-data "files\colors.png;files" --add-data "files\colors_gray.png;files" --add-data "files\left.png;files" --add-data "files\right.png;files" --add-data "files\down.png;files" --add-data "files\undo2.png;files" --add-data "files\note.png;files" label_app_main_generic.py
# ###

#when in dev
#SOURCE_PATH = u"d:\\programming\\tinder_scraper\\images_women"
#POSITIVE_PATH = u"d:\\programming\\tinder_scraper\\images_women_positive"
#NEGATIVE_PATH = u"d:\\programming\\tinder_scraper\\images_women_negative"
#OTHER_PATH = u"d:\\programming\\tinder_scraper\\images_not_human"

SOURCE_PATH = "--chose folder--"
POSITIVE_PATH = "--chose folder--"
NEGATIVE_PATH = "--chose folder--"
OTHER_PATH = "--chose folder--"

REMEMBER_FILE = u"lm_memory.txt"
CONFIG_FILE = u"lm.ini"
IMAGE_SIZE = 600

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
if __name__ == "__main__":
    sys.excepthook = except_hook

# def get_image_dir():
#     files = {}
#     # r=root, d=directories, f = files
#     filenames = os.listdir(SOURCE_PATH)
#     for index,filename in enumerate(filenames):
#         if ".jpg" not in filename:
#             return []
#         filepath = os.path.join(SOURCE_PATH, filename)
#         filepath.encode(encoding='UTF-8')
#         files[index] = Path(filepath)
#     return files

def get_image_list():
    files = []
    filenames = os.listdir(SOURCE_PATH)
    for filename in filenames:
        #if ".jpg" not in filename:
        #    return []
        #filepath = os.path.join(SOURCE_PATH, filename)
        filepath = SOURCE_PATH / filename
        #filepath.encode(encoding='UTF-8')
        files.append(filepath)
    print("file list loaded")
    return files


def move_file(window, file, folder):
    #print(file)
    #print(folder)
    to = folder / file.parts[-1]
    exists = os.path.isfile(to)
    if exists:
        QtWidgets.QMessageBox.about(window, "Warning", "File with the same name already exists in target folder! \nPlease rename "+str(file.parts[-1])+"\n\nProgramm will close.")
        sys.exit(0)
    to = folder / file.parts[-1]
    file.rename(to)
    #to =  folder+"\\"+file.rsplit('\\', 1)[-1]
    #os.rename(file, to)
    print("Moving", file, "to",folder)

def remember(name):
    with open(REMEMBER_FILE, 'a') as file:
        file.write(name+'\n')
    print("Remembers", name)

def rescale(image, size):
    img = image
    #print("before rescale:",img.size)
    if img.size[0] < img.size[1]:
        basewidth = size
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    else:
        baseheight = size
        hpercent = (baseheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, baseheight), Image.ANTIALIAS)
    #print("after rescale:",img.size)
    return img


def top_center_crop(image, new_width, new_height):
    img = image
    # print("before crop:",img.size)
    width, height = img.size  # Get dimensions

    wdiff = (width - new_width) / 2
    hdiff = (height - new_height) / 2

    x1 = wdiff
    y1 = 0

    x2 = width - wdiff
    y2 = new_height

    img = img.crop((x1, y1, x2, y2))
    # print("after crop:",img.size)
    return img

def uniform_aspect_ratio(image, size):
    img = image
    img = rescale(img,size)
    img = top_center_crop(img,size,size)
    return img

def piltoqimg(pilimg):
    cvImg = np.array(pilimg)
    height, width, channel = cvImg.shape
    bytesPerLine = channel * width
    qImg = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888)
    return qImg

class MainWindow(QMainWindow):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, files):
        super().__init__()

        self.files = files
        if not self.files:
            QtWidgets.QMessageBox.about(self, "Error", "Directory must only contain .jpg files.")
            sys.exit()

        parser = configparser.ConfigParser()
        parser.read(CONFIG_FILE)
        self.image_size = parser['options'].getint('image_size')
        self.resize_img = parser['options'].getboolean('resize_img')

        self.previous = []
        self.current_path = ""          #stores the full path including the name of the actual file
        self.current_picture = ""       #stores only the name of the actual file
        self.remembered = False
        self.progress_count = 0
        self.initial_count = len(files)

        self.setWindowTitle("Image label app")

        self.layout = main_gui_generic.Ui_MainWindow()
        self.layout.setupUi(self)


        #self.central_widget = QWidget()
        #self.setCentralWidget(self.central_widget)
        #lay = QVBoxLayout(self.central_widget)
        #self.name_label = QLabel(self)
        #lay.addWidget(self.name_label)
        #self.img_label = QLabel(self)
        #lay.addWidget(self.img_label)
        #self.pos_count_label = QLabel(self)
        #lay.addWidget(self.pos_count_label)
        #self.neg_count_label = QLabel(self)
        #lay.addWidget(self.neg_count_label)
        #self.other_count_label = QLabel(self)
        #lay.addWidget(self.other_count_label)
        #verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        #lay.addItem(verticalSpacer)


        self.setup_connections()
        self.setup_button_icons()
        self.show()

        self.positive_count = 0
        self.negative_count = 0
        self.other_count = 0

    def setup_button_icons(self):
        #print('QToolButton{qproperty-icon: url("'+resource_path("files/nope.png").replace('\\','/')+'")')
        self.layout.pos_button.setStyleSheet(
            'QToolButton{qproperty-icon: url("'+resource_path("files/right.png").replace('\\','/')+'")}')
        self.layout.neg_button.setStyleSheet(
            'QToolButton{qproperty-icon: url("' + resource_path("files/left.png").replace('\\', '/') + '")}')
        self.layout.other_button.setStyleSheet(
            'QToolButton{qproperty-icon: url("' + resource_path("files/down.png").replace('\\', '/') + '")}')
        self.layout.remember_button.setStyleSheet(
            'QToolButton{qproperty-icon: url("' + resource_path("files/note.png").replace('\\', '/') + '")}')
        self.layout.undo_button.setStyleSheet(
            'QToolButton{qproperty-icon: url("' + resource_path("files/undo2.png").replace('\\', '/') + '")}')
        #checkbox_stylesheet = 'QCheckBox::indicator: unchecked{image: url("'+resource_path("files/flame.png").replace('\\', '/')+'");border: 1px solid gray;}QCheckBox::indicator: checked{image: url("'+resource_path("files/flame_gray.png").replace('\\', '/')+'");}'
        checkbox_stylesheet = 'QCheckBox::indicator:unchecked{image:url('+resource_path("files/colors.png").replace('\\', '/')+');}\nQCheckBox::indicator:checked{image:url('+resource_path("files/colors_gray.png").replace('\\', '/')+');}'
        self.layout.grayscale_checkbox.setStyleSheet(checkbox_stylesheet)
        #print(checkbox_stylesheet)
    def setup_connections(self):
        self.layout.pos_button.clicked.connect(self.right_pressed)
        self.layout.neg_button.clicked.connect(self.left_pressed)
        self.layout.other_button.clicked.connect(self.down_pressed)
        self.layout.remember_button.clicked.connect(self.up_pressed)
        self.layout.undo_button.clicked.connect(self.space_pressed)
        self.layout.grayscale_checkbox.clicked.connect(self.grayscale_toggle)

    def right_pressed(self):
        self.progress_count += 1
        move_file(self, self.current_path, POSITIVE_PATH)
        self.current_path = POSITIVE_PATH / self.current_picture
        self.update_counts(1, 0, 0)
        self.get_next()

    def left_pressed(self):
        self.progress_count += 1
        move_file(self, self.current_path, NEGATIVE_PATH)
        self.current_path = NEGATIVE_PATH / self.current_picture
        self.update_counts(0, 1, 0)
        self.get_next()

    def down_pressed(self):
        self.progress_count += 1
        move_file(self, self.current_path, OTHER_PATH)
        self.current_path = OTHER_PATH / self.current_picture
        self.update_counts(0, 0, 1)
        self.get_next()

    def up_pressed(self):
        if not self.remembered:
            remember(self.current_picture)

            self.remembered = True

    def space_pressed(self):
        if self.previous:
            self.progress_count -= 1
            self.get_previous()
            move_file(self, self.current_path, SOURCE_PATH)
            if POSITIVE_PATH == self.current_path.parent:
                self.update_counts(-1, 0, 0)
            if NEGATIVE_PATH == self.current_path.parent:
                self.update_counts(0, -1, 0)
            if OTHER_PATH == self.current_path.parent:
                self.update_counts(0, 0, -1)
            self.current_path = SOURCE_PATH / self.current_picture
            #print("current after space", self.current_path)


    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Right:
            self.right_pressed()
        elif key == QtCore.Qt.Key_Left:
            self.left_pressed()
        elif key == QtCore.Qt.Key_Down:
            self.down_pressed()
        elif key == QtCore.Qt.Key_Up:
            self.up_pressed()
        elif key == QtCore.Qt.Key_Space:
            self.space_pressed()

    def get_next(self, is_first=False):
        if not is_first:
            self.previous.append(self.current_path)
        len(self.files)
        if self.files:
            next = self.files.pop()
            self.update_image(next)
        else:
            self.update_final()

    def get_previous(self):
        if self.current_path is not None:                   #it is None if there were no frames left
            self.files.append(self.current_path)
        next = self.previous.pop()
        print("Ignoring current and retrieving previous from",next)
        self.update_image(next)

    def grayscale_toggle(self):
        self.update_image(self.current_path)

    def adjust_progress_bar(self):
        print("Progress:", self.progress_count,",",str(round(100*(self.progress_count / self.initial_count),3))+"%")
        self.layout.progressBar.setValue(100*(self.progress_count / self.initial_count))

    def update_final(self):
        self.adjust_progress_bar()
        self.remembered = False
        self.update_name("Finished!")
        self.layout.img_label.setText("\tAll images are labelled.\t\n\n\tGreat :)")

        self.layout.img_label.setMinimumWidth(self.image_size)
        self.current_path = None                                    #set current path to None as there is nothing more to come

    def update_image(self, path):
        if path is None:
            return
        self.adjust_progress_bar()
        self.remembered = False
        self.current_path = path
        self.current_picture = str(path).rsplit('\\', 1)[-1]
        self.update_name(self.current_picture)

        if self.resize_img:
            img = Image.open(str(path))
            img = uniform_aspect_ratio(img, self.image_size)
            qimg = piltoqimg(img)
            if self.layout.grayscale_checkbox.isChecked():
                qimg = qimg.convertToFormat(QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qimg)
        else:
            pixmap = QPixmap(str(path))                #in case there are issues with the conversion, ppixmap can be loaded directly

        self.layout.img_label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        print("\n"+self.current_picture,"Dimensions:",(pixmap.width(), pixmap.height()))
        print("path:",self.current_path)

    def update_name(self, name):
        self.layout.name_label.setText(name)


    def update_counts(self, pos, neg, other):
        self.positive_count += pos
        self.negative_count += neg
        self.other_count += other
        self.layout.pos_count_label.setText("Positive: "+str(self.positive_count))
        self.layout.neg_count_label.setText("Negative: "+str(self.negative_count))
        self.layout.other_count_label.setText("Other: "+str(self.other_count))


class Instructions(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()
    save_config = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Label App - Instructions')
        self.layout = instructions.Ui_Instructions()
        self.layout.setupUi(self)
        self.setup_connections()


    def setup_connections(self):
        self.layout.continue_button.clicked.connect(self.next_window)

    def next_window(self):
        if self.layout.noshow_checkBox.isChecked():
            self.save_config.emit()
        self.switch_window.emit()


class FolderChoice(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()
    save_config = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Specify Folders')

        self.layout = specify_folders.Ui_Folders()
        self.layout.setupUi(self)

        self.setup_connections()

    def set_default_paths(self):
        self.layout.line_edit_source.setText(str(SOURCE_PATH))
        self.layout.line_edit_pos.setText(str(POSITIVE_PATH))
        self.layout.line_edit_neg.setText(str(NEGATIVE_PATH))
        self.layout.line_edit_other.setText(str(OTHER_PATH))

    def set_folder(self, line_edit):
        folder = self.choose_folder_path()
        path = Path(folder.toString()[8:])
        print(folder)
        line_edit.setText(str(path))

    def choose_folder_path(self):
        dir_browser = QtWidgets.QFileDialog()
        dir_browser.setFileMode(QtWidgets.QFileDialog.Directory)
        folder = dir_browser.getExistingDirectoryUrl()
        return folder

    def setup_connections(self):
        self.layout.start_button.clicked.connect(self.next_window)
        self.layout.source_fc_button.clicked.connect(lambda x: self.set_folder(self.layout.line_edit_source))
        self.layout.pos_fc_button.clicked.connect(lambda x: self.set_folder(self.layout.line_edit_pos))
        self.layout.neg_fc_button.clicked.connect(lambda x: self.set_folder(self.layout.line_edit_neg))
        self.layout.other_fc_button.clicked.connect(lambda x: self.set_folder(self.layout.line_edit_other))

    def set_paths(self):
        global SOURCE_PATH, POSITIVE_PATH, NEGATIVE_PATH, OTHER_PATH

        SOURCE_PATH = Path(self.layout.line_edit_source.text())
        POSITIVE_PATH = Path(self.layout.line_edit_pos.text())
        NEGATIVE_PATH = Path(self.layout.line_edit_neg.text())
        OTHER_PATH = Path(self.layout.line_edit_other.text())


    def next_window(self):
        self.set_paths()

        if self.layout.remember_checkBox.isChecked():
            self.save_config.emit()

        if SOURCE_PATH.is_dir() and POSITIVE_PATH.is_dir() and NEGATIVE_PATH.is_dir() and OTHER_PATH.is_dir():
            self.switch_window.emit()
        else:
            QtWidgets.QMessageBox.about(self, "Warning", "Directory does not exist!")




class Controller(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.files = []

    def get_files(self):
        self.files = get_image_list()
        print(len(self.files),"files in source folder")

    def get_counts(self):
        self.positive_count = len(list(os.listdir(POSITIVE_PATH)))
        self.negative_count = len(list(os.listdir(NEGATIVE_PATH)))
        self.other_count = len(list(os.listdir(OTHER_PATH)))
        print(self.positive_count, "files in positive folder")
        print(self.negative_count, "files in negative folder")
        print(self.other_count, "files in other folder")

    def change_dontshow_config(self):
        parser = configparser.ConfigParser()
        parser.read(CONFIG_FILE)
        parser.set('options', 'show_instructions', 'False')

        with open(CONFIG_FILE, "w") as config:
            parser.write(config)

    def change_path_config(self):
        parser = configparser.ConfigParser()
        parser.read(CONFIG_FILE)

        parser.set('paths', 'source', str(SOURCE_PATH))
        parser.set('paths', 'positive',  str(POSITIVE_PATH))
        parser.set('paths', 'negative',  str(NEGATIVE_PATH))
        parser.set('paths', 'other', str(OTHER_PATH))

        with open(CONFIG_FILE, "w") as config:
            parser.write(config)

    def show_instructions(self):
        self.instructions = Instructions()
        self.instructions.setWindowTitle("Image label app")
        self.instructions.switch_window.connect(self.show_folderchoice)
        self.instructions.save_config.connect(self.change_dontshow_config)
        self.instructions.show()

    def show_folderchoice(self, show_instructions=True):
        if show_instructions:
            self.instructions.close()
        self.folder_choice = FolderChoice()
        self.folder_choice.setWindowTitle("Image label app")
        self.folder_choice.set_default_paths()
        self.folder_choice.switch_window.connect(self.show_main)
        self.folder_choice.save_config.connect(self.change_path_config)
        self.folder_choice.show()

    def show_main(self):
        self.folder_choice.close()
        self.get_files()
        self.get_counts()
        self.main_window = MainWindow(self.files)
        self.main_window.get_next(is_first=True)
        self.main_window.update_counts(self.positive_count, self.negative_count, self.other_count)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    print("resource path",str(os.path.join(base_path, relative_path)))
    return os.path.join(base_path, relative_path)



def main():
    global SOURCE_PATH, POSITIVE_PATH, NEGATIVE_PATH, OTHER_PATH

    parser = configparser.ConfigParser()
    app = QtWidgets.QApplication(sys.argv)
    iconpath=resource_path("files/favicon.ico")
    app.setWindowIcon(QtGui.QIcon(iconpath))
    controller = Controller()

    cofig_exists = os.path.isfile(CONFIG_FILE)
    if not cofig_exists:
        config = open(CONFIG_FILE, "a+")
        parser.add_section('paths')
        parser.set('paths', 'source', "--chose folder--")
        parser.set('paths', 'positive',  "--chose folder--")
        parser.set('paths', 'negative',  "--chose folder--")
        parser.set('paths', 'other', "--chose folder--")
        parser.add_section('options')
        parser.set('options', 'show_instructions', 'True')
        parser.set('options', 'image_size', '600')
        parser.set('options', 'resize_img', 'True')
        parser.write(config)
        config.close()
        show_instructions = True
    else:
        parser.read(CONFIG_FILE)
        SOURCE_PATH = Path(parser['paths']['source'])
        POSITIVE_PATH = Path(parser['paths']['positive'])
        NEGATIVE_PATH = Path(parser['paths']['negative'])
        OTHER_PATH = Path(parser['paths']['other'])
        print(OTHER_PATH)

        show_instructions = parser['options'].getboolean('show_instructions')
        print("show_instr",show_instructions)

    if show_instructions:
        controller.show_instructions()
    else:
        controller.show_folderchoice(show_instructions=False)

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()





