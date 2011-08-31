#!/usr/bin/python

import random
import time

log = 0

def print_tile(map, width, height):
  for iy in xrange(height):
    for ix in xrange(width):
      print "%(num)2d " % {'num': map[iy][ix]},
    print 
  return
  
# get available size
def avail_size(map, width, height, uwidth, uheight, sx, sy):
  if (sx >= width) or (sy >= height):
    return

  xmax =  min(width - sx, uwidth)
  ymax =  min(height - sy, uheight)
  for y in xrange(1, min(height - sy, uheight) + 1):
    for x in xrange(1, min(width - sx, uwidth) + 1):
      if (map[sy + y - 1][sx + x - 1] != 0) and (x - 1 < xmax):
        xmax = x - 1
      if (map[sy + y - 1][sx + x - 1] != 0) and (y - 1 < ymax):
        ymax = y - 1

  #print "xmax = ", xmax, "ymax = ", ymax
  return xmax, ymax 

# make tile
def make_tile(width, height, uwidth, uheight):
  map = [[0]*width for x in xrange(height)]

  x = random.randint(0, width - 1)
  y = random.randint(0, height - 1)
  w = random.randint(1, uwidth)
  h = random.randint(1, uheight)

  area_list = []
  area_count = 1

  for iy in xrange(height):
    for ix in xrange(width):
      if (map[iy][ix] != 0):
        continue

      area = avail_size(map, width, height, uwidth, uheight, ix, iy)
      factor = 1.6
      area_width = max(min(int(area[0] * random.random() * factor), area[0]), 1)
      area_height = max(min(int(area[1] * random.random() * factor), area[1]), 1)
      area_size = area_width * area_height

      if (log == 1):
        print "Block ", area_count, ": x=", ix, "y=", iy, "avail_width=", area[0], "avail_height=", area[1], "--> area_width=", area_width, "area_height=", area_height

      # paint
      for ay in xrange(area_height):
        for ax in xrange(area_width):
          map[iy + ay][ix + ax] = area_count

      area_list.append([area_count, area_width, area_height, ix, iy, area_size])
      area_count += 1

  if (log == 1):
    print_tile(map, width, height) 
    print area_list
  return area_list

def make_html_tile(width, height, unitx, unity):
  area_list = make_tile(unitx, unity, 4, 3)
  width1 = int(width / unitx)
  height1 = int(height / unity)

  font_max = 64
  font_min = 18
  padding = 5
  border = 1
  background_color = [ "#9c1f1f", "#9c891f", "#449c1f", "#1f9c66", "#1f689c", "#421f9c", "#9c1f8b" ]
  
  for area in area_list:
    print "<div class=box style='",
    print "left:"+str(width1*area[3])+"px;",
    print "top:"+str(height1*area[4])+"px;",
    print "width:"+str(width1*area[1]-padding*2-border*2)+"px;",
    print "height:"+str(height1*area[2]-padding*2-border*2)+"px;",
    color = background_color[random.randint(0, len(background_color) - 1)]
    print "background-color:"+color+";",
    font_size = (float((font_max - font_min)) / (4 * 3)) * area[5] + font_min
    print "font-size:"+str(font_size)+"px;",
    print "'>All work and no play makes Jack a dull boy</div>"


make_html_tile(1280, 720, 10, 8)

