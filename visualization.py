#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import basemap

"""
 Shows the solution circuit
"""
def geo_visualization( instance, solution ):
    fig = plt.figure( figsize=(12,12) )
    
    min_coord = ( min(instance.cities_coordinates[:][0]), )
    
    back_map = basemap( projection='merc', resolution=None, wid )