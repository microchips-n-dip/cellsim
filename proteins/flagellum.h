#ifndef CELLSIM_FLAGELLUM_H
#define CELLSIM_FLAGELLUM_H

#include "cellsim/proteins/protein_base.h"

namespace cellsim {

struct Flagellum : public Protein
{
  bool self_eaten;
  void EatYourself()
  {
    self_eaten = true;
  }
  
  void FetchKernelRunner(KernelRunHelper** kernel_runner);
};

}

#endif
