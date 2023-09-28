DIR_ROOT  = ../

CC 				= gcc
CX 				= g++
CCFLAGS		= -Wall -c
CXFLAGS 	= -Wall -c
CP     		= cp
CP_ALL  	= cp -r
RM        = rm
RM_ALL    = rm -f
SRCS			= lds_driver.cpp
OBJS			= lds_driver.o
INC_DIRS  = -I/usr/include
TARGET 	  = lds_driver

all : $(TARGET)
	$(CXX) -o $(TARGET) $(OBJS) $(INC_DIRS)
 
$(TARGET) :
	$(CXX) -c $(SRCS) $(INC_DIRS)

clean:
	$(RM_ALL) $(OBJS) $(TARGET)
