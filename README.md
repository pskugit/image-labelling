# Image labelling application
> a stand alone program to sort images from a source folder into one of three specified destinatin folder.

This program was made to ease the labelling process for several ML projects.
The sorted image folders can then for example easily be loaded by PyTorch's ImageFOlder class. [https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder]

## Prerequisites

Written in Python3, the program has a few external libraries
They are all accessible through pip.

```
$ pip install PyQt5 
$ pip install Pillow
$ pip install numpy
```

## Usage

At start time, the program shows the instructions and then asks the user to specify three paths which will be mapped to the terms
'positive', 'negative' and 'other'.
![](/screenshots/la1.png?raw=true "Optional Title")

One can then quickly label all the source images.
![](/screenshots/la2.jpg?raw=true "Optional Title")


## .EXE

The program is also available as ready compiled executable. 
(Build with pyinstaller)


## Meta

Philipp Skudlik 

[https://github.com/pskugit](https://github.com/pskugit/)
