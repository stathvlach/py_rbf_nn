# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:00:22 2022

@author: stathvlach
"""
import numpy as np

def create_sample_data(shape):
    
    sample_data = np.zeros(shape)
    
    return sample_data

def main():
    d = create_sample_data((3,3))
    print(d)
    return

if __name__ == "__main__":
    main()
    