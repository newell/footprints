#!/usr/bin/python

from footgen import *

f = Footgen("B3F-1022", output_format='geda')
f.add_pad("1", x=-3.25, y=2.25, diameter = 2.0, shape = "circle", drill = 1.0)
f.add_pad("2", x=3.25, y=2.25, diameter = 2.0, shape = "circle", drill = 1.0)
f.add_pad("3", x=-3.25, y=-2.25, diameter = 2.0, shape = "circle", drill = 1.0)
f.add_pad("4", x=3.25, y=-2.25, diameter = 2.0, shape = "circle", drill = 1.0)
f.silkbox(h=7.0, w=9.0) 
f.finish()
