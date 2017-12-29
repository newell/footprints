#!/usr/bin/python

from footgen import *

f = Footgen("PJ044A", output_format='geda')
f.add_pad("1", x=0, y=-3.7, xsize=3.5,  ysize=1.0)
f.add_pad("2", x=0, y=2.5, xsize=3.0, ysize=1.0)
f.add_pad("3", x=3.5, y=1.5, xsize=2.50, ysize=1.0)
f.silkbox(h=11.5, w=10.0) 
f.finish()
