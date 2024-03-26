COPT = -g -ggdb -W -Wall -no-integrated-cpp -static-libgcc

CC     = gcc
AR     = ar
RANLIB = ranlib
AR_OPT = rcs

C_SUFFIX = .c
O_SUFFIX = .o
OUT_SUFFIX = .out

LIBS = -lnsl -lrt

OUT = ./out

OUTPUT_NAME = $(notdir $(shell pwd))

_NAME = $(OUTPUT_NAME)
TARGET_OBJ = $(OUT)/$(_NAME).$(OBJ).$(XTARGET)
TARGET_NAME = $(OUTPUT_NAME).$(XTARGET)

SRC  = . src

INC  = -I. -Iinc

xLIB += -Xlinker --start-group
xLIB += -ldl -lm -lgcc_s -lpthread
xLIB += -Xlinker --end-group

C_SRCS  = $(foreach dir, $(SRC), $(wildcard $(dir)/*$(C_SUFFIX)))
CXX_SRCS = $(foreach dir, $(SRC), $(wildcard $(dir)/*$(CXX_SUFFIX)))
OBJS = $(foreach dir, . $(TARGET_OBJ), $(wildcard $(dir)/*$(O_SUFFIX)))
OXXS = $(foreach dir, . $(TARGET_OBJ), $(wildcard $(dir)/*$(OXX_SUFFIX)))

%$(O_SUFFIX) :
	@echo "################################################################################"
	@echo "#                                                                              #"
	@echo "#  compile "$@
	@echo "#                                                                              #"
	@echo "################################################################################"
	$(RM) $(TARGET_OBJ)/$@;
	$(CC) $(INC) $(COPT) -static -o $(addprefix $(TARGET_OBJ)/, $(notdir $@)) \
	-fPIC -c $(subst $(O_SUFFIX),$(C_SUFFIX), $@) -lm $(xLIB);
	@echo "################################################################################"
	@echo "#                                                                              #"
	@echo "#                                                                              #"
	@echo "#                                                                              #"
	@echo "################################################################################"

%$(OXX_SUFFIX) :
	@echo "################################################################################"
	@echo "#                                                                              #"
	@echo "#  compile CXX "$@
	@echo "#                                                                              #"
	@echo "################################################################################"
	$(CXX) $(INC) $(COPT) -static -o $(addprefix $(TARGET_OBJ)/, $(notdir $@)) \
	-fpermissive -fPIC -c $(subst $(OXX_SUFFIX),$(CXX_SUFFIX), $@) -lm $(xLIB);
	@echo "################################################################################"
	@echo "#                                                                              #"
	@echo "#                                                                              #"
	@echo "#                                                                              #"
	@echo "################################################################################"

% :
	@echo "################################################################################"
	@echo "#                                                                              #"
	@echo "#  binary "$@$(OUT_SUFFIX)
	@echo "#                                                                              #"
	@echo "################################################################################"
	$(CC) -o $(OUT)/$@$(OUT_SUFFIX) $(OBJS) $(INC) $(COPT) $(xLIB);
	@echo "################################################################################"
	@echo "#                                                                              #"
	@echo "#                                                                              #"
	@echo "#                                                                              #"
	@echo "################################################################################"

all:
	make $(addsuffix $(O_SUFFIX),$(basename $(C_SRCS)));
	make $(TARGET_NAME);
