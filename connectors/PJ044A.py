#!/usr/bin/python

from footgen import *

f = Footgen("PJ044A", output_format='geda')
f.add_pad("1", x=0, y=-3.7, diameter=4.125, shape='circle', drill=3.5)
f.add_pad("2", x=0, y=2.5, diameter=3.625, shape='circle', drill=3.0)
f.add_pad("3", x=3.5, y=1.5, diameter=3.125, shape='circle', drill=2.5)
f.silkbox(h=11.5, w=10.0) 
f.finish()
