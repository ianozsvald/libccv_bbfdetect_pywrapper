libccv_bbfdetect_pywrapper
==========================

Python wrapper around command line call to libccv's bbfdetect face detector. Assumes you have installed:

https://github.com/liuliu/ccv


Example usage:

python bbfdetect_wrapper.py --image ./faces.jpg

[{'y': 159, 'width': 33, 'confidence': 2.56699, 'height': 33, 'x': 237}, {'y': 158, 'width': 44, 'confidence': 6.200849, 'height': 44, 'x': 447}, {'y': 219, 'width': 53, 'confidence': 5.060024, 'height': 53, 'x': 365}, {'y': 231, 'width': 54, 'confidence': 0.210586, 'height': 54, 'x': 495}, {'y': 192, 'width': 46, 'confidence': 2.897291, 'height': 46, 'x': 159}, {'y': 190, 'width': 51, 'confidence': 4.579619, 'height': 51, 'x': 286}, {'y': 145, 'width': 81, 'confidence': -3.323252, 'height': 81, 'x': 295}]

It returns a list of dictionary elements for x, y, width, height, confidence values per detected face.
