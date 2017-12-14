#!/usr/bin/python

from footgen import *

f = Footgen("ATWINC1500-MR210", output_format='geda')

# Left side 20-28
f.add_pad("20", x=-10.86, y=-5.465, xsize=1.9, ysize=0.8)
f.add_pad("21", x=-10.86, y=-2.417, xsize=1.9, ysize=0.8)
f.add_pad("22", x=-10.86, y=-1.401, xsize=1.9, ysize=0.8)
f.add_pad("23", x=-10.86, y=-0.385, xsize=1.9, ysize=0.8)
f.add_pad("24", x=-10.86, y=0.631, xsize=1.9, ysize=0.8)
f.add_pad("25", x=-10.86, y=1.647, xsize=1.9, ysize=0.8)
f.add_pad("26", x=-10.86, y=2.663, xsize=1.9, ysize=0.8)
f.add_pad("27", x=-10.86, y=3.679, xsize=1.9, ysize=0.8)
f.add_pad("28", x=-10.86, y=4.695, xsize=1.9, ysize=0.8)

# Bottom side 1-9
f.add_pad("1", x=-8.19, y=7.365, xsize=0.8, ysize=1.9)
f.add_pad("2", x=-7.174, y=7.365, xsize=0.8, ysize=1.9)
f.add_pad("3", x=-6.158, y=7.365, xsize=0.8, ysize=1.9)
f.add_pad("4", x=-5.142, y=7.365, xsize=0.8, ysize=1.9)
f.add_pad("5", x=-1.078, y=7.365, xsize=0.8, ysize=1.9)
f.add_pad("6", x=0.954, y=7.365, xsize=0.8, ysize=1.9)
f.add_pad("7", x=1.97, y=7.365, xsize=0.8, ysize=1.9)
f.add_pad("8", x=2.986, y=7.365, xsize=0.8, ysize=1.9)
f.add_pad("9", x=4.002, y=7.365, xsize=0.8, ysize=1.9)

# Top side 19-10
f.add_pad("19", x=-7.18, y=-7.365, xsize=0.8, ysize=1.9)
f.add_pad("18", x=-6.164, y=-7.365, xsize=0.8, ysize=1.9)
f.add_pad("17", x=-5.148, y=-7.365, xsize=0.8, ysize=1.9)
f.add_pad("16", x=-4.132, y=-7.365, xsize=0.8, ysize=1.9)
f.add_pad("15", x=-3.116, y=-7.365, xsize=0.8, ysize=1.9)
f.add_pad("14", x=-2.1, y=-7.365, xsize=0.8, ysize=1.9)
f.add_pad("13", x=-1.084, y=-7.365, xsize=0.8, ysize=1.9)
f.add_pad("12", x=-0.068, y=-7.365, xsize=0.8, ysize=1.9)
f.add_pad("11", x=0.948, y=-7.365, xsize=0.8, ysize=1.9)
f.add_pad("10", x=1.964, y=-7.365, xsize=0.8, ysize=1.9)

#f.qfn(pitch = 0.5, pins = 48, width = 7.5, padheight = 0.25, padwidth = 0.9, silk_xsize = 7.0)
#f.generator.silk_circle(0, 0, 9.27)
f.silkbox(h=14.73, w=21.72)
f.finish()
