#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:18:09 2020

@author: wayky
"""

import TSP_rep

inst = TSP_rep.TSP_Instance( "./samples/Huelva/cities.csv", [2,3,4], [1,0] )
                
print( inst.matrix )