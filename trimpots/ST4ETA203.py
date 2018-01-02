#!/usr/bin/python

from footgen import *

f = Footgen("ST4ETA203", output_format='geda')
f.add_pad("1", x=1.175, y=2.0, xsize=1.6, ysize=2.0)
f.add_pad("3", x=-1.175, y=2.0, xsize=1.6, ysize=2.0)
f.add_pad("2", x=0, y=-2.0, xsize=2.0, ysize=2.0)
f.silkbox(h=4.5, w=5.0)
f.finish()



