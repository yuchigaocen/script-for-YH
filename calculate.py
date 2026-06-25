import numpy as np

def center(loc,template):
    h,w = template.shape[:2]
    center = (loc[0]+w/2,loc[1]+h/2)
    return center

