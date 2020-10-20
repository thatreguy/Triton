#!/usr/bin/env python2
## -*- coding: utf-8 -*-

from pintool import *
from triton  import CALLBACK, ARCH


def mycb(inst):
    print('Processing instruction at', inst, '\n')
    return

def reg_hit(ctxt, reg):
    print('Need concrete register value:', reg)
    return

def mem_hit(ctxt, mem):
    print('Need concrete memory value:', mem)
    return

if __name__ == '__main__':
    # Start JIT at the entry point
    startAnalysisFromEntry()

    getTritonContext().addCallback(CALLBACK.GET_CONCRETE_MEMORY_VALUE, mem_hit)
    getTritonContext().addCallback(CALLBACK.GET_CONCRETE_REGISTER_VALUE, reg_hit)

    # Add callback
    insertCall(mycb, INSERT_POINT.BEFORE)

    # Run Program
    runProgram()
