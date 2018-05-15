CC = g++
CPPFLAGS = -std=c++11 -g -Wall -iquote"/home/microchips-n-dip/Desktop/" -I"/usr/include/python2.7" -fpic

VPATH = core:	 	 \
	dna: 		 \
	kernel: 	 \
	proteins: 	 \
	rna:		 \
	swig_cellsimcpp

vpath %.c core
vpath %.c dna
vpath %.c kernel
vpath %.c proteins
vpath %.c rna
vpath %.c swig_cellsimcpp

SRCS = $(wildcard **/*.cpp)
VPATH_SPACES = $(subst :, , $(VPATH))
OBJS = $(patsubst %.cpp, build/%.o, $(notdir $(SRCS)))

cellsimcpp.so: $(OBJS)
	$(CC) -fpic -shared $^ -o swig_cellsimcpp/_swig_cellsimcpp.so

build/%.o: %.cpp
	$(CC) $(CPPFLAGS) -c $< -o build/$(@F)

swig:
	swig -c++ -python \
	-o swig_cellsimcpp/_swig_cellsimcpp.cpp \
	swig_cellsimcpp/swig_cellsimcpp.i

clean:
	rm build/*.o
	rm *.exe

verb:
	@echo $(SRCS)
	@echo $(OBJS)
