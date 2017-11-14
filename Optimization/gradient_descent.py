#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:58:59 2017

@author: davi
"""
import numpy as np
import matplotlib.pyplot as plt

class MathFunction():
   
   def sphere(self,X):
      """
      In: numpy.array([x1,x2,...,xn])
      Out: float(f(x1,x2,...,xn))
      """
      return np.sum(X**2)
   
   def venkataraman(self,X):
      """
      In: numpy.array([x1,x2,...,xn])
      Out: float(f(x1,x2,...,xn))
      
      Source: Venkataraman, P. (2009). Applied optimization with MATLAB programming.
      """
      return 3*(np.sin(0.5+0.25*X[0]*X[1]))*np.cos(X[0])
   
   def branin(self,X):
      """
      In: numpy.array([x1,x2,...,xn])
      Out: float(f(x1,x2,...,xn))
      
      Source: https://www.sfu.ca/~ssurjano/branin.html
      """
      a=1.
      b=5.1/(4.*np.pi**2.)
      c=5./np.pi
      r=6.
      s=10.
      t=1./(8.*np.pi)
      return a*(X[1]-b*X[0]**2+c*X[0]-r)**2+s*(1-t)*np.cos(X[0])+s

class GradientDescent():
   
   def __init__(self,function):
      self.function = function
   
   def gradient(self,X):
      """
      In: numpy.array([x1,x2,...,xn])
      Out: numpy.array([dx1,dx2,...,dxn])
      """
      h = 1e-5
      derivative_array = np.empty(X.shape[0])
      for i in range(X.shape[0]):
         X_upper = np.copy(X).astype(np.float)
         X_lower = np.copy(X).astype(np.float)
         X_upper[i]+=h
         X_lower[i]-=h
         derivative_array[i] = (self.function(X_upper)-self.function(X_lower))/(2*h)
      return derivative_array
   
   def search(self,X,a,N):
      """
      In: numpy.array([x1_0,x2_0,...,xn_0]), float(learning_rate), int(iterations)
      Out: {'solution': [X_0,X_1,...,X_n], 'output': [f(X_0),f(X_1),...,f(X_n)]}
      """
      optimization_process = {'solution': [], 'output': []}
      for i in range(N):
         optimization_process['solution'].append(X)
         optimization_process['output'].append(self.function(X))
         X1 = X - a*self.gradient(X)
         X = np.copy(X1)
      return optimization_process

if __name__ == "__main__":
   
   function = MathFunction()
   optimizer = GradientDescent(function.venkataraman)
   X0 = np.array([.5,.5]) #initial guess
   optimizer_results = optimizer.search(X0,.33,10)
   
   #PLOTTING
   x1 = np.linspace(-6, 6, 100)
   x2 = np.linspace(-6, 6, 100)
   X = np.array(np.meshgrid(x1, x2))
   z = function.venkataraman(X)
   
   plt.contour(x1,x2,z,np.arange(-3.3, 3.5, .25).tolist(),cmap='jet')
   
   for i,solution in enumerate(optimizer_results['solution']):
      plt.scatter(solution[0],solution[1],c=[0,0,0],zorder=1e+3)
      plt.text(solution[0],solution[1],i,va='bottom',fontsize=8)
   
   plt.xlim([-6,6])
   plt.ylim([-6,6])
   
   plt.savefig('gradient_descent.png')