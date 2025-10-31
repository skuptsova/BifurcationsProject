from vpython import *
# Web VPython 3.2
X = float(input("starting X, between 0 and 1"))
N = int(input("N of iterations"))

def logistic(r,X):
    return r*X*(1-X)
    
popvIterate = graph(title="Population fraction vs Iterate number", ytitle="Population fraction", xtitle="Iterate number")
bifurcations = graph(title="Bifurcation", ytitle="X", xtitle="r", fast=True)
gc1 = gdots(graph = popvIterate, color = color.red, size=1)
gc2 = gdots(graph=bifurcations, color = color.black, size=1)

for r in range(2.8,4,0.0001):
    for i in range(1, N, 1):
        X = logistic(r, X)
        gc1.plot(i,X)
    gc2.plot(r,X)
        
