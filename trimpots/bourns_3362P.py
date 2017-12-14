#!/usr/bin/python

from footgen import *

f = Footgen("bourns_3362P", output_format='geda')
f.add_pad("1", x=-2.54, y=-0.035, diameter=2.0, shape = "circle", drill=1.0)
f.add_pad("2", x=2.54, y=-0.035, diameter=2.0, shape = "circle", drill=1.0)
f.add_pad("3", x=0, y=2.505, diameter=2.0, shape = "circle", drill=1.0)
f.silkbox(h=7.0, w=6.60)
f.finish()
