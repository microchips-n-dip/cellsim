%module swig_cellsimcpp

%include "cpointer.i"

%{
#include "cpp_export.h"
#include "cellsim/grid_cell.h"
#include "cellsim/grid_field.h"
%}

namespace cellsim {}

class Cell {
public:
  Cell();
  ~Cell();
  void Run();
  long int GetPosX();
  long int GetPosY();
  void SetPosX(long int nxt_x);
  void SetPosY(long int nxt_y);
  void SetColour(const char* colour);
  const char* GetColour();
  unsigned int GetNumFreeDNA();
  void PopDNA();
  unsigned int GetNFlagella();
  void AddRsrc();
};

class IntGrid {
public:
  IntGrid(unsigned int x, unsigned int y);
  void ErasePoint(unsigned int x, unsigned int y);
  int* GetPoint(unsigned int idx);
  int& GetPoint(unsigned int x, unsigned int y);
  int& operator()(unsigned int x, unsigned int y);
  void SetPoint(unsigned int x, unsigned int y, int p);
  bool IsOccupied(unsigned int x, unsigned int y);
  unsigned int MapSize();
};

%pointer_class(int, intp);

class CellGrid {
public:
  CellGrid(unsigned int x, unsigned int y);
  long int GetLinearIndex(long int x, long int y);
  void ErasePoint(unsigned int x, unsigned int y);
  Cell* GetPoint(unsigned int idx);
  Cell& GetPoint(long int x, long int y);
  Cell& operator()(long int x, long int y);
  void SetPoint(long int x, long int y, Cell p);
  bool IsOccupied(long int x, long int y);
  unsigned int MapSize();
};

%pointer_class(Cell, Cellp);

%include "grid_field.h"
%include "grid_cell.h"
%include "cpp_export.h"
