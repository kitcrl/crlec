################################################################################
#                                                                              #
#                                                                              #
#                             OPTIONAL INFORMATION                             #
#                                                                              #
################################################################################
SRC  = .
SRC += src

INC  = -I.
INC += -Iinc

xLIB += -Xlinker --start-group
xLIB += -L$(TOOLCHAIN_LIB) -ldl -lm -lgcc_s -lpthread
xLIB += -Xlinker --end-group
