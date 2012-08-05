libccv_bbfdetect_pywrapper
==========================

Python wrapper around command line call to libccv's bbfdetect face detector. Assumes you have installed:

https://github.com/liuliu/ccv


Example usage:

python bbfdetect_wrapper.py --image /home/ian/workspace/libccv/liuliu-ccv-43ec190/faces/faces1.jpg

[{'y': 80, 'width': 46, 'confidence': 7.184594, 'height': 46, 'x': 371}, {'y': 278, 'width': 36, 'confidence': -1.564904, 'height': 36, 'x': 503}, {'y': 53, 'width': 47, 'confidence': 3.803873, 'height': 47, 'x': 289}, {'y': 88, 'width': 47, 'confidence': 4.719907, 'height': 47, 'x': 445}, {'y': 55, 'width': 53, 'confidence': -0.12583, 'height': 53, 'x': 177}, {'y': 93, 'width': 56, 'confidence': -1.443526, 'height': 56, 'x': 78}]


It returns a list of dictionary elements for x, y, width, height, confidence values per detected face.
