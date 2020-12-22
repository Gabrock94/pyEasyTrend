#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This python package is used to perform Trends analysis using a single line

Created on Tue Dec 15 15:26:05 2020
Last edited on Mon Dec 21 18:45:00 2020

@author: Giulio gabrock Gabrieli
"""

import numpy as np
from scipy import stats
from scipy.stats import norm
import pandas as pd

__version__ = '0.0.0.6'

MODEL_NAMES = ['Constant (mean y)', # y = mean
               'Linear', # y = mx+1
               'Quadratic', # y = ax2 + bx + q
               'Cubic', # y = ax3 + bx2 + cx + q
               'Quartic', # ...
               'Quintic']

def analyzeTrend(x, y, maxDegree = 2,
                  visualize=False, title='Trend Analysis', 
                  xlabel='x', ylabel='y', plotci=True, ci=95):
    """ This is a simple entrypoint to perform a trend analysis. This functions
        performs the analysis of the trend (SSE, R2, F, AIC, BIC) up to the maxDegree order.
        
    
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
        :param xlabel: Label of the X axis of the visual representation. Only used if visualize is True
        :type xlabel: string
        :param ylabel: Label of the Y axis of the visual representation. Only used if visualize is True
        :type ylabel: string
        :param plotci: renders the confidence interval on the plot
        :type plotci: boolean
        :param ci: confidence interval. Only used if plotci is True
        :type ci: int
        :return: a dictionary containing the results of the trend analysis 
        :rtype: dict
    """
    
    #check input type and values
    if(type(maxDegree) != int):
        raise TypeError("maxDegree must be an interger value")
    if(maxDegree < 1):
        raise TypeError("maxDegree must be 1 (Linear model) or higher")
    if(type(x) in [list, 'pandas.core.series.Series']):
        raise TypeError("x must be a list")
    if(type(y) in [list, 'pandas.core.series.Series']):
        raise TypeError("y must be a list")
    if(type(visualize) != bool):
        raise TypeError("visualize must be a boolean")
    if(type(title) != str):
        raise TypeError("title must be a string")
    if(type(xlabel) != str):
        raise TypeError("xlabel must be a string")
    if(type(ylabel) != str):
        raise TypeError("ylabel must be a string")
    if(type(plotci) != bool):
        raise TypeError("plotci must be a boolean")
    if(type(ci) != int):
        raise TypeError("ci must be an integer")
    if(ci <= 0 or ci > 100):
        raise TypeError('ci must be an integer between 1 and 99')
    
        
    # if visualzie is true, produces a scatterplot    
    if(visualize):
        import matplotlib.pyplot as plt
        plt.scatter(x,y)
    
    #initialize the results' dict           
    results = {}
    
    #Reduced model yp = mean    
    mean_y = np.mean(y) #quite dumb
    SSE0 = sum([(value - mean_y)**2 for value in y]) #Get the Sum of Squared Error for the model y = mean(y)
    
    #if visualize is true, plot th model
    if(visualize):
        plt.hlines(mean_y, xmin=min(x), xmax=max(x), label=MODEL_NAMES[0],
                    color='black', linestyles='--', alpha=0.4)
    
    #get the confidence interval
    alpha = 1 - (ci/100)
    t  = stats.t.ppf(1 - alpha, len(x) -1)
    civ = t*(np.std(y)/np.sqrt(len(x)))


    #fit the polynomial up to the n-th order, where n is maxDegree
    if(maxDegree>= 1):
        SSER = SSE0 #for the first comparison, the constant model is the reduced model
            
        #for each order
        for order in range(1, maxDegree+1):
            #fit the model, get parameters and residuals
            p, residuals, rank, singular_values, rcond = np.polyfit(x,y, order, full=True)
            p = np.poly1d(p) #black magic
            SSEF = residuals[0] #get the Sum of Squared Error
            F = ((SSER - SSEF) / ( (len(x)- order) - (len(x) - (order+1)) )) / (SSEF / (len(x) - (order+1))) #get F
            p_value = 1- stats.f.cdf(F, 1, len(x) - (order+1)) #and from F get p
            r2 = 1 - (SSEF / SSE0) #r2
            #black magic to get log-likelihood
            ll = -(len(x)/2)*np.log(2*np.pi) - (len(x)/2)*np.log(SSEF / len(x))  - (len(x)/2)
            AIC = 2*order - 2*ll #Evaluate AIC
            BIC = order*np.log(len(x)) - 2*ll #and BIC
            
            #give the model a name?
            if(order < len(MODEL_NAMES)):
                modelname = MODEL_NAMES[order]
            else:
                modelname = str(order) + ' order model'

            #put everything in the results
            results[order] = {'R2':r2,
                  'SSE':SSEF,
                  'F':F,
                  'pvalue':p_value,
                  'AIC':AIC,
                  'BIC':BIC}
            
            #render something if visualzie is true
            if(visualize):
                morex = np.linspace(min(x), max(x), 200)
                line = plt.plot(morex, p(morex), label=modelname)
                color = line[0].get_color()
                if(plotci):
                    morex = np.linspace(min(x), max(x), 200)
                    morey = p(morex)
                    plt.fill_between(morex, [value - civ for value in morey], [value + civ for value in morey], alpha=0.4, color=color)
            SSER = SSEF #update the SSER for the next model
           
    #Final touch to the plot        
    if(visualize):
        plt.title(title, fontweight='bold',fontsize='x-large')
        plt.xlabel(xlabel,fontsize='x-large')
        plt.ylabel(ylabel, fontsize='x-large')
        plt.legend()
        plt.show()
        
    return (results)

def tablifyResults(results):
    ''' This function create a pandas DataFrame containing the results of the 
    linear trend analysis obtained using the analyzeTrend function.
    
        :param results: results dictionary obtained using the analyzeTrend function
        :type resu;ts: dict
        :return: pandas Dataframe of length = len(maxOrder).
        :rtype: pandas DataFrame
    '''
    
    data = {}
    data['Order'] = results.keys()
    for key in results[1].keys():
        data[key] = [results[order][key] for order in results.keys()]
    return(pd.DataFrame(data))
###############################################################################


###############################################################################
#                                                                             #
#                                  DEBUG                                      #
#                                                                             #
###############################################################################
""" For debug purposes."""

if(__name__=='__main__'):
    data = {'StudyTime':[24, 44, 21, 45, 54, 26, 57, 34, 33, 12, 17, 21, 58, 41, 29, 55, 42, 40, 21, 9, 39, 30, 17, 31, 51, 42, 30, 3, 20, 21, 4, 16, 26, 6, 18, 50, 60, 13, 23, 13, 3, 35, 38, 51, 12, 35, 7, 42, 20, 41, 37, 56, 19, 57, 12, 49, 15, 6, 43, 7, 40, 12, 35, 4, 46, 29, 6, 38, 36, 33, 21, 33, 50, 54, 25, 38, 48, 17, 28, 48, 16, 50, 24, 15, 40, 54, 40, 42, 2, 20, 24, 21, 37, 15, 52, 36, 5, 7, 29, 21],
            'Score':[18, 47, 21, 60, 80, 18, 100, 28, 41, 7, 12, 17, 82, 45, 33, 94, 41, 55, 9, 6, 53, 24, 13, 35, 62, 43, 33, 2, 17, 10, 0, 7, 14, 0, 14, 72, 94, 7, 14, 3, 0, 43, 39, 80, 5, 39, 4, 43, 14, 37, 39, 80, 16, 94, 7, 55, 13, 2, 45, 6, 55, 7, 35, 0, 69, 18, 0, 45, 43, 27, 11, 37, 67, 82, 16, 41, 74, 10, 19, 55, 14, 60, 18, 7, 55, 64, 37, 60, 2, 10, 17, 14, 30, 6, 69, 32, 2, 1, 32, 10]}
    df = pd.DataFrame(data)
    df.head()
        
    #run the analysis
    results = analyzeTrend(df.StudyTime, df.Score, maxDegree=3, visualize=True)
    table = tablifyResults(results)
    print(table)
    
