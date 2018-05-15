#ifndef GRID_CELL_H
#define GRID_CELL_H

#include <string>

#include "cellsim/core/worldstate.h"

class Cell {
protected:
  cellsim::WorldState* cell;
  
  long int x;
  long int y;
  
  std::string m_colour;
  
public:
  Cell() {
    x = 0;
    y = 0;
    
    using namespace cellsim;
    cell = new WorldState();
    std::vector<DNAStrand*> strands;
    strands.push_back(new DNAStrand(FLAGELLUM_GENE, {}));
    strands.push_back(new DNAStrand(DNA_POLYMERASE_GENE, {}));
    strands.push_back(new DNAStrand(RNA_POLYMERASE_GENE, {}));
    strands.push_back(new DNAStrand(RIBOSOME_COMPLEX_GENE, {}));
    cell->AddProtein(new RibosomeComplex());
    cell->AddProtein(new RNAPolymerase());
    cell->AddProtein(new DNAPolymerase());
    cell->AddProtein(new RibosomeComplex());
    cell->AddProtein(new RibosomeComplex());
    cell->AddProtein(new Flagellum());
    cell->AddProtein(new Flagellum());
    cell->AddProtein(new Flagellum());
    cell->AddProtein(new Flagellum());
    cell->AddDNA(new DNA(strands));
    cell->reset();
  }
  ~Cell() { }
  
  void Run() {
    cell->Run();
    std::cout << "Cell has " << cell->GetRNASize() << " floating RNA strands\n";
    std::cout << "Cell has " << cell->GetProteinsSize() << " proteins\n";
  }
  
  long int GetPosX() const {
    return x;
  }
  
  long int GetPosY() const {
    return y;
  }
  
  void SetPosX(long int nxt_x) {
    x = nxt_x;
  }
  
  void SetPosY(long int nxt_y) {
    y = nxt_y;
  }
  
  void SetColour(const char* colour) {
    m_colour = std::string(colour);
  }
  
  const char* GetColour() {
    return m_colour.c_str();
  }
  
  unsigned int GetNumFreeDNA() const {
    return cell->GetDNASize() - 1;
  }
  
  void PopDNA() {
    cell->dna_.pop_back();
  }
  
  unsigned int GetNFlagella() const {
    std::cout << "Cell has " << cell->n_flagella << " flagella\n";
    return cell->n_flagella;
  }
  
  void AddRsrc() {
    cell->n_rsrc += 1;
  }
};

#endif
