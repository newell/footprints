#!/usr/bin/python

from footgen import *

f = Footgen("B82479A", output_format='geda')
f.add_pad("1", x=-7.685, y=0.0, xsize=2.92, ysize=2.79)
f.add_pad("2", x=7.685, y=0.0, xsize=2.92, ysize=2.79)
f.generator.silk_circle(0, 0, 9.27)
f.finish()
