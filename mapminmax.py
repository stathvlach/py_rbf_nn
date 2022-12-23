# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:52:17 2022

@author: stathvlach
"""
import numpy as np


def manpminmax(mode, data, a = -1, b = 1, ps = ()):

    if len(data.shape) == 1:
        data = np.reshape(data, (1, data.size))
    
    out = np.zeros(data.shape)
    if mode == "apply":
    
        if len(ps) == 0:
            ps = (data.min(1), data.max(1))
        
        for i in range(0, data.shape[1]):
            out[:, i] = a + ((b - a)/(ps[1] - ps[0]))*(data[:, i] - ps[0])
        
        return (out, ps)
    
    if mode == "reverse":
        
        if len(ps) == 0:
            # throw error
            return -1
 
        for i in range(0, data.shape[1]):
            out[:, i] = (a*ps[1] - b*ps[0])/(a-b) + ((ps[0] - ps[1])/(a - b))*data[:, i]

        return (out, None)
    
    # throw error
    return -1