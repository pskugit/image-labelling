# Image labelling application
> a stand alone program to sort images from a source folder into one of three specified destination folders.

This program was made to ease the labelling process for several ML projects.
The sorted image folders can then for example easily be loaded by PyTorch's ImageFolder class. 
[https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder]

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
![](/screenshots/la3.png?raw=true "Optional Title")

At first start, the program will create an lm.ini file where the user settings can be stored and few additional parameters may be set.

## .EXE

The program is also available as ready compiled executable. 
(Built with pyinstaller)


## Meta

Philipp Skudlik 

[https://github.com/pskugit](https://github.com/pskugit/)
