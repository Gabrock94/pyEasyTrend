#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This python package is used to perform Trends analysis using a single line


Created on Tue Dec 15 15:26:05 2020

@author: giulio gabrock gabrieli
"""

import numpy as np
from scipy import stats
from scipy.stats import norm
import pandas as pd

__version__ = '0.0.0.5'

MODEL_NAMES = ['Constant', # y = mean
               'Linear', # y = mx+1
               'Quadratic', # y = ax2 + bx + q
               'Cubic', # y = ax3 + bx2 + cx + q
               'Quartic', # ...
               'Quintic']
    
def analyzeTrend(x, y, maxDegree = 2,
                 visualize=False, title='Trend Analysis', 
                 xlabel='x', ylabel='y', plotci=True, ci=95):
    """ This is a simple entrypoint to perform a trend analysis
    
        :param x: x
        :type x: list
        :param y: y
        :type y: list
        :param maxDegree: highest order of the model to test
        :type maxDegree: int
        :param visualize: renders a visual representation of the model(s)
        :type visualize: bool
        :param title: Title of the visual representation. Only used if visualize is True
        :type title: string
        :param xlabe;: Label of the X axis of the visual representation. Only used if visualize is True
        :type xlabe;: string
        :param ylabel: Label of the Y axis of the visual representation. Only used if visualize is True
        :type ylabel: string
        :param plotci: renders the confidence interval on the plot
        :type plotci: boolean
        :param ci: confidence interval
        :type ci: int
        :return: a dictionary containing the results of the ECG analysis 
        :rtype: list
    """
    
    #check input type
    if(type(maxDegree) != int):
        raise TypeError("maxDegree must be an interger value")
    if(maxDegree < 1):
        raise TypeError("maxDegree must be 1 (Linear model) or higher")
    
    #TODO
    # Check type of x and y
    
    if(visualize):
        import matplotlib.pyplot as plt
        plt.scatter(x,y)
    
    results = {}
    
    #Reduced model yp = mean    
    mean_y = np.mean(y)
    SSE0 = sum([(value - mean_y)**2 for value in y])
    
    if(visualize):
        plt.hlines(mean_y, xmin=min(x), xmax=max(x), label=MODEL_NAMES[0],
                   color='black', linestyles='--', alpha=0.4)
    
    #linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    yp = [value*slope + intercept for value in x]

    SSE1 = sum([(value[0] - value[1])**2 for value in np.transpose([yp, y])])
    results[1] = {'r2':r_value**2,
                   'pvalue':p_value}
    
    alpha = 1 - (ci/100)
    t  = stats.t.ppf(1 - alpha, len(x) -1)
    civ = t*(np.std(y)/np.sqrt(len(x)))
    if(visualize):
        plt.plot(x, yp, label=MODEL_NAMES[1])
        
        if(plotci):
            morex = np.linspace(min(x), max(x), 200)
            morey = [value *slope + intercept for value in morex]
            plt.fill_between(morex, [value - civ for value in morey], [value + civ for value in morey], alpha=0.4)
    
    #if the order is equal or greater than 2, we fit the polynomial
    if(maxDegree>= 2):
        SSER = SSE1 #for the first comparison, the linear model is the reduced model
            
        for order in range(2, maxDegree+1):
            p, residuals, rank, singular_values, rcond = np.polyfit(x,y, order, full=True)
            p = np.poly1d(p)
            SSEF = residuals[0]
            F = ((SSER - SSEF) / ( (len(x)- order) - (len(x) - (order+1)) )) / (SSEF / (len(x) - (order+1)))
            p_value = 1- stats.f.cdf(F, 1, len(x) - (order+1))
            r2 = 1 - (SSEF / SSE0)
            if(order < len(MODEL_NAMES)):
                modelname = MODEL_NAMES[order]
            else:
                modelname = str(order) + ' order model'

            results[order] = {'r2':r2,'pvalue': p_value}
            if(visualize):
                morex = np.linspace(min(x), max(x), 200)
                plt.plot(morex, p(morex), label=modelname)
                if(plotci):
                    morex = np.linspace(min(x), max(x), 200)
                    morey = p(morex)
                    plt.fill_between(morex, [value - civ for value in morey], [value + civ for value in morey], alpha=0.4)
            

    if(visualize):
        plt.title(title, fontweight='bold',fontsize='x-large')
        plt.xlabel(xlabel,fontsize='x-large')
        plt.ylabel(ylabel, fontsize='x-large')
        plt.legend()
        plt.show()
        
    return (results)

def tablifyResults(results):
    orders = list(results.keys())
    modelnames = [MODEL_NAMES[order] for order in results.keys()]
    r2s = [results[order]['r2'] for order in results.keys()]
    pvalues = [results[order]['pvalue'] for order in results.keys()]
    data = {'Order':orders,'Model':modelnames, 'R2':r2s,'p-value':pvalues}
    return(pd.DataFrame(data))
###############################################################################


###############################################################################
#                                                                             #
#                                  DEBUG                                      #
#                                                                             #
###############################################################################
""" For debug purposes."""

if(__name__=='__main__'):
    x = [0,1,2,3,4,5]
    y = [0,27,8,-27,-64,125]
    results = analyzeTrend(x,y, visualize=True, maxDegree=3,plotci=False)
    print(tablifyResults(results))
    
