#ifndef GRID_FIELD_H
#define GRID_FIELD_H

#include <vector>
#include <unordered_map>
#include <utility>

template <typename Point>
class GridField {
protected:
  unsigned int axis0_size;
  unsigned int axis1_size;
  unsigned int total_size;
  typedef typename std::unordered_map<long int, Point*>::iterator Iterator;
  std::unordered_map<long int, Point*> m_points;
  
public:
  GridField(unsigned int size0, unsigned int size1) {
    axis0_size = size0;
    axis1_size = size1;
    total_size = axis0_size * axis1_size;
  }
  
  GridField() { }
  ~GridField() { }
  
  long int GetLinearIndex(long int x, long int y) {
    NormalizeInputCoords(x, y);
    return x + axis0_size * y;
  }
  
  Point* FetchCreate(long int x, long int y) {
    long int linidx = GetLinearIndex(x, y);
    auto it = m_points.find(linidx);
    if (it == m_points.end()) {
      it = m_points.emplace(linidx, new Point()).first;
    }
    return it->second;
  }
  
  void ErasePoint(long int x, long int y) {
    NormalizeInputCoords(x, y);
    long int linidx = GetLinearIndex(x, y);
    auto it = m_points.find(linidx);
    if (it == m_points.end()) {
      return;
    }
    else {
      m_points.erase(it);
    }
  }
  
  Point* GetPoint(unsigned int idx) {
    Iterator node_idx = m_points.begin();
    unsigned int i;
    for (i = 0; i < idx; ++i, ++node_idx) { }
    return node_idx->second;
  }
  
  Point& GetPoint(long int x, long int y) {
    NormalizeInputCoords(x, y);
    return *FetchCreate(x, y);
  }
  
  Point& operator()(long int x, long int y) {
    NormalizeInputCoords(x, y);
    return *FetchCreate(x, y);
  }
  
  void SetPoint(long int x, long int y, Point p) {
    NormalizeInputCoords(x, y);
    *FetchCreate(x, y) = p;
  }
  
  bool IsOccupied(long int x, long int y) {
    NormalizeInputCoords(x, y);
    long int linidx = GetLinearIndex(x, y);
    auto it = m_points.find(linidx);
    if (it == m_points.end()) {
      return false;
    }
    else {
      return true;
    }
  }
  
  unsigned int Axis0Size() const {
    return axis0_size;
  }
  
  unsigned int Axis1Size() const {
    return axis1_size;
  }
  
  unsigned int TotalSize() const {
    return total_size;
  }
  
  unsigned int MapSize() const {
    return m_points.size();
  }
  
  void NormalizeInputCoords(long int& x, long int& y) {
    if (x < 0) {
      x = 0;
    }
    if (x >= axis0_size) {
      x = axis0_size;
    }
    
    if (y < 0) {
      y = 0;
    }
    if (x >= axis1_size) {
      y = axis1_size;
    }
  }
};

#endif
