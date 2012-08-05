libccv_bbfdetect_pywrapper
==========================

Python wrapper around command line call to libccv's bbfdetect face detector. Assumes you have installed:

https://github.com/liuliu/ccv


Example usage:

python bbfdetect_wrapper.py --image /home/ian/workspace/libccv/liuliu-ccv-43ec190/faces/faces1.jpg

It returns a list of dictionary elements for x, y, width, height, confidence values per detected face.
