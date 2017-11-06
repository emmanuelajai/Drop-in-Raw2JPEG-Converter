# Drop-in-Raw2JPEG-Converter
Drop the python file in same folder with .NEF raw images, it will create a new folder to save the converted files

On a Mac computer, make nef2jpg.py file executable and ensure python exists in the path specified on the first line

Requirements: python,  rawpy and imageio
run this command from your terminal to get rawpy and imageio

if you do not have pip on your Mac, run this command

    easy_install pip
    
next run

    pip install rawpy

then 

    pip install imageio


Note: nef2jpg will not convert files in subdirectories.
if you need to do this, you may need to move the file to the subdirectory and run it from there.


contact: ajayi@oluwaseun.com