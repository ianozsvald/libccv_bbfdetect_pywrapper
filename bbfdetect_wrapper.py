"""Trivial libccv bbfdetect face detection wrapper - uses Popen for shell calls and returns the results in a dict"""

# Wraps:
# http://libccv.org/
# https://github.com/liuliu/ccv
#
# Designed around version:
# liuliu-ccv-43ec190
# from July 2012

# Example call:
# python bbfdetect_wrapper.py --image /home/ian/workspace/libccv/liuliu-ccv-43ec190/faces/faces1.jpg

import sys
import os
import subprocess
import argparse

# Confirm we have LIBCCV env variable pointing at bbfdetect face detector
LIBCCV_ROOT = os.environ.get('LIBCCV')
if not LIBCCV_ROOT:
    print "Expected to find the path to libccv's directory in system environment LIBCCV"
    print "E.g. $LIBCCV == /home/ian/workspace/libccv/liuliu-ccv-43ec190"
    print "We need $LIBCCV/bin/bbfdetect and $LIBCCV/samples/faces/*"
    sys.exit(1)

BBFDETECT = os.path.join(LIBCCV_ROOT, 'bin', 'bbfdetect')
FACES_DIR = os.path.join(LIBCCV_ROOT, 'samples', 'face')

assert os.path.exists(BBFDETECT) # confirm bin/bbfdetect binary exists
assert os.path.exists(FACES_DIR) # confirm that samples/faces/* directory exists

# example command line call:
# ./bbfdetect faces1.jpg ../samples/face/


def find_faces(image_path):
    """Find all the faces in the given image, return as list of dictionaries of coords and confidences"""
    cmd_parts = [BBFDETECT, image_path, FACES_DIR]
    output = subprocess.check_output(cmd_parts)

    output_lines = output.strip().split('\n')
    # the last line should look something like:
    # 'total : 6 in time 174ms'
    assert output_lines[-1].startswith('total :')

    faces = []
    for nbr, line in enumerate(output_lines[:-1]):
        x, y, width, height, confidence = line.split()
        faces.append(dict(x=int(x), y=int(y), width=int(width), height=int(height), confidence=float(confidence)))
    return faces

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', help="Image file with path, e.g. '/home/ian/workspace/libccv/liuliu-ccv-43ec190/faces/faces1.jpg'")
    args = parser.parse_args()
    #print args
    if not os.path.exists(args.image):
        print "You must supply a valid image file, %s does not exist" % (args.image)
        sys.exit(1)
    faces = find_faces(args.image)
    print faces
