# pdfMerger
A little python script (a wrapper in fact) using ghostScript to merge pdf files

## What is this?
This programm deals with an issue I frequently had:
Many pdf files that I would like to merge, but I don't want to use a third party web service and I don't have an Adobe license
for a reliable merging software.

This script allows you to merge every pdf files stored in a folder (don't worry for non pdf files, they won't be broken) or to merge a given
list of pdf files.

## What is needed?

You will need __ghostScript__ installed (it's free!!) and added to your PATH.
Here is a [link](https://www.ghostscript.com/download/gsdnld.html)

Of course, you need a working python 3.x installation.

Nothing more! It only uses the python standard library!

## How to use it?

Start by downloading or cloning this project

In order to clone, 
Open a terminal, then type:
```
$ cd /path/where/you/want/to/install
$ git clone https://github.com/spineki/pdfMerger.git
$ cd pdfMerger
```

here you are! There is two ways to use it

### Simplest mode (if you are not familiar with command line interface and options)

1) Type the following and press enter 
```
python pdfMerger.py
```

2) You will be prompted to enter the path of the directory containing the pdf files that need to be merged. Type it and press enter:
```
    :warning
    Files will be merged following an alphabetical order.
    It means that the following repository:
    |-> file3.pdf
    |-> file1.pdf
    |-> file2.pdf

    becomes
    |-> merged_document.pdf containing file1.pdf-file2.pdf-file3.pdf in this order, it's the same with letters.
```

3) You will be prompted to enter the _ouput path of your merged file_:
 The default name is __merged_document.pdf__.
 
    You can keep it just by pressing enter. Or you can choose your own output name, it's hope to you!

4) Wait until it's done (usually less than one second)
    The merged file is now __stored in the folder that previously held your pdf files.__ (there are still there too, no worries!)

### Command line mode

You will be a LOT more precise with this mode:

1) If you need to merge some precise files that are not in the same folder, use the following :

    Example: I want to merge cat.pdf, dog.pdf and frog.pdf that are in three different folder in this precise order.

    (the paths here are linux-like, but it works perfectly on windows)

    ```
    $ python pdfMerger.py -f /pathfoo/cat.pdf /path/dog.pdf /last/path/frog.pdf -o   my_special_output_name.pdf
    ```
    -f stands for file  
    -o stands for output name (optional -> 'merged_document.pdf' by default)

    The merged file will be __stored in the very folder you started this programm from__. (In an incoming update, -o will make a difference between relative and absolute paths)


2) If you need to merge all the files in a folder, use the following:
    
    Example: I want to merge cat.pdf, dog.pdf and frog.pdf that are in folder myAnimalFolder

    ```
    $ python pdfMerger -d /path/to/MyAnimalFolder -o a_fancy_output_name.pdf
    ```
    -d stands for directory  
    -o stands for output name (optional -> 'merged_document.pdf' by default)

    The merged file is now __stored in the folder that previously held your pdf files (myAnimalFolder).__ (there are still there too, no worries!)
3) You can precise the verbosity with __-v True (verbose) or -v False (quiet)__

4) If you need __some help, type__ 
    ```
    $ python pdfMerger.py -h  
    ```
    as usual!

## Want to contribute?

Fork this project and make a pull request.

This project is designed to stay very simple, as a toy example for a simple wrapper with argarse for example. So I won't add too much complexity in it. 

Stay simple!