from swig_cellsimcpp.swig_cellsimcpp import *
import graphics as gr
import random
import time

import sys
import os

def bound(x, b):
  x0 = max(0, x)
  x1 = min(b - 1, x0)
  return x1

def create_rect(x, y, s, c):
  tl_x = x * s
  tl_y = y * s
  pt = gr.Point(tl_x, tl_y)
  rect = gr.Rectangle(pt, pt)
  rect.setWidth(s)
  rect.setFill(c)
  rect.setOutline(c)
  return rect

class PyGridOutputter:
  def __init__(self):
    self.grid_dim = 100
    self.grid_space = 7
    self.grid_px = self.grid_dim * self.grid_space
    
    self.cell_grid = CellGrid(self.grid_dim, self.grid_dim)
    self.food_grid = IntGrid(self.grid_dim, self.grid_dim)
    
    self.win = gr.GraphWin('Cell Grid', self.grid_px, self.grid_px)
    
    self.rects = {}
    self.frects = {}
  
  def IsOccupied(self, x, y):
    s = self.cell_grid.IsOccupied(x, y)
    return s
  
  def CreateCell(self, x, y, c):
    if (self.IsOccupied(x, y)):
      return
    else:
      cell = self.cell_grid.GetPoint(x, y)
      cell.SetPosX(x)
      cell.SetPosY(y)
      cell.SetColour(c)
      self.rects[(x, y)] = create_rect(x, y, self.grid_space, c)
  
  def EraseCell(self, x, y):
    self.cell_grid.ErasePoint(x, y)
    del self.rects[(x, y)]
      
  def DestroyCell(self, x, y):
    self.cell_grid.ErasePoint(x, y)
    self.rects[(x, y)].undraw()
    del self.rects[(x, y)]
    
  def MoveCell(self, x0, y0, x1, y1):
    if (x0 == x1 and y0 == y1):
      return
    if (self.IsOccupied(x1, y1)):
      self.DestroyCell(x0, y0)
      self.DestroyCell(x1, y1)
      return
    else:
      cell = self.cell_grid.GetPoint(x0, y0)
      self.cell_grid.SetPoint(x1, y1, cell)
      cell = self.cell_grid.GetPoint(x1, y1)
      cell.SetPosX(x1)
      cell.SetPosY(y1)
      dx = (x1 - x0) * self.grid_space
      dy = (y1 - y0) * self.grid_space
      self.rects[(x1, y1)] = self.rects[(x0, y0)]
      self.rects[(x1, y1)].move(dx, dy)
      print "Cell rect moved ({}, {}) pixels".format(dx, dy)
      self.EraseCell(x0, y0)
      
    if (self.food_grid.IsOccupied(x1, y1)):
      self.frects[(x1, y1)].undraw()
      del self.frects[(x1, y1)]
      self.food_grid.ErasePoint(x1, y1)
      cell = self.cell_grid.GetPoint(x1, y1)
      cell.AddRsrc()
      
  def DisplayCell(self, x, y):
    try:
      self.rects[(x, y)].draw(self.win)
    except:
      pass
    
  def DisplayCells(self):
    m = self.cell_grid.MapSize()
    for i in range(0, m):
      cell = self.cell_grid.GetPoint(i)
      x = cell.GetPosX()
      y = cell.GetPosY()
      self.DisplayCell(x, y)
      
  def RunCells(self):
    i = 0
    while i < self.cell_grid.MapSize():
      print "Running cell", i, "of", self.cell_grid.MapSize()
      cell = self.cell_grid.GetPoint(i)
      cell.Run()
      n_flagella = cell.GetNFlagella()
      x0 = cell.GetPosX()
      y0 = cell.GetPosY()
      x1 = bound(random.randint(x0 - n_flagella, x0 + n_flagella), self.grid_dim)
      y1 = bound(random.randint(y0 - n_flagella, y0 + n_flagella), self.grid_dim)
      self.MoveCell(x0, y0, x1, y1)
      if (cell.GetNumFreeDNA() > 0):
        self.CreateCell(x0, y0, cell.GetColour())
        self.DisplayCell(x0, y0)
        cell.PopDNA()
      i += 1
      
  def AddFood(self, x, y):
    self.food_grid.SetPoint(x, y, 1)
    self.frects[(x, y)] = create_rect(x, y, self.grid_space, "orange")
    self.frects[(x, y)].draw(self.win)

cellsim = PyGridOutputter()
pop0_x = 20
pop0_y = 20
for i in range(0, 20):
  for j in range(0, 20):
    x = i + j % 2 + pop0_x
    y = j + i % 2 + pop0_y
    cellsim.CreateCell(x, y, "green")
pop1_x = 60
pop1_y = 60
for i in range(0, 20):
  for j in range(0, 20):
    x = i + j % 2 + pop1_x
    y = j + i % 2 + pop1_y
    cellsim.CreateCell(x, y, "blue")
pop2_x = 10
pop2_y = 50
for i in range(0, 20):
  for j in range(0, 20):
    x = i + j % 2 + pop2_x
    y = j + i % 2 + pop2_y
    cellsim.CreateCell(x, y, "aqua")
pop3_x = 30
pop3_y = 30
for i in range(0, 20):
  for j in range(0, 20):
    x = i + j % 2 + pop3_x
    y = j + i % 2 + pop3_y
    cellsim.CreateCell(x, y, "black")
pop4_x = 45
pop4_y = 25
for i in range(0, 20):
  for j in range(0, 20):
    x = i + j % 2 + pop4_x
    y = j + i % 2 + pop4_y
    cellsim.CreateCell(x, y, "red")
    
for i in range (0, 100):
  for j in range (0, 100):
    cellsim.AddFood(i, j)

cellsim.DisplayCells()

while True:
  cellsim.RunCells()
  time.sleep(0.05)
