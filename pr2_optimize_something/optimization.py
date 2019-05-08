"""MC1-P2: Optimize a portfolio. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Copyright 2018, Georgia Institute of Technology (Georgia Tech) 			  		 			     			  	   		   	  			  	
Atlanta, Georgia 30332 			  		 			     			  	   		   	  			  	
All Rights Reserved 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Template code for CS 4646/7646 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Georgia Tech asserts copyright ownership of this template and all derivative 			  		 			     			  	   		   	  			  	
works, including solutions to the projects assigned in this course. Students 			  		 			     			  	   		   	  			  	
and other users of this template code are advised not to share it with others 			  		 			     			  	   		   	  			  	
or to make it available on publicly viewable websites including repositories 			  		 			     			  	   		   	  			  	
such as github and gitlab.  This copyright statement should not be removed 			  		 			     			  	   		   	  			  	
or edited. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
We do grant permission to share solutions privately with non-students such 			  		 			     			  	   		   	  			  	
as potential employers. However, sharing with other current or future 			  		 			     			  	   		   	  			  	
students of CS 7646 is prohibited and subject to being investigated as a 			  		 			     			  	   		   	  			  	
GT honor code violation. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
-----do not edit anything above this line--- 			  		 			     			  	   		   	  			  	
""" 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
import pandas as pd 			  		 			     			  	   		   	  			  	
import matplotlib.pyplot as plt 			  		 			     			  	   		   	  			  	
import numpy as np 			  		 			     			  	   		   	  			  	
import datetime as dt 			  		 			     			  	   		   	  			  	
from util import get_data, plot_data 		
import scipy.optimize as spo
 			  		 			     			  	   		   	  			  	
# This is the function that will be tested by the autograder 			  		 			     			  	   		   	  			  	
# The student must update this code to properly implement the functionality 			  		 			     			  	   		   	  			  	

def sharpe(allocs,prices_nml):
    port_prices = prices_nml * allocs
    port_prices = port_prices.sum(axis=1)
    port_daily_returns = port_prices.iloc[1:] / port_prices.shift().iloc[1:] - 1
    return -port_daily_returns.mean()/port_daily_returns.std()

def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
    syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False): 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
    # Read in adjusted closing prices for given symbols, date range 			  		 			     			  	   		   	  			  	
    dates = pd.date_range(sd, ed) 			  		 			     			  	   		   	  			  	
    prices_all = get_data(syms, dates)  # automatically adds SPY 			  		 			     			  	   		   	  			  	
    prices = prices_all[syms]  # only portfolio symbols 			  	
    prices_nml = prices/prices.iloc[0] # normalized prices

    prices_SPY = prices_all['SPY']  # only SPY, for comparison later 
    prices_SPY = prices_SPY / prices_SPY.iloc[0]
    
 			  		 			     			  	   		   	  			  	      
    # find the allocations for the optimal portfolio 			  		 			     			  	   		   	  			  	    
    allocs = np.ones(len(syms))/len(syms)
    bnds = [(0,1) for _ in range(len(syms))]
    cons = ({ 'type': 'eq', 'fun': lambda x: 1.0 - np.sum(x) })    
    min_result = spo.minimize(sharpe,allocs,args=prices_nml,method='SLSQP',options={'disp':True},bounds=bnds,constraints=cons)    

    # find other necessary output values    
    allocs = min_result.x # allocatiion
    sr = -min_result.fun # sharpe ratio
    port_prices = prices_nml * allocs 
    port_prices = port_prices.sum(axis=1)
    cr = port_prices[-1] / port_prices[0]-1 #cumulatiive return
    port_daily_returns = port_prices.iloc[1:] / port_prices.shift().iloc[1:] - 1
    adr = port_daily_returns.mean() # average daily return
    sddr = port_daily_returns.std() # standard deviation 			  		 			     			  	   		   	  			  	 
 			  		 			     			  	   		   	  			  	
    # Compare daily portfolio value with SPY using a normalized plot 			  		 			     			  	   		   	  			  	
    if gen_plot: 			  		 			     			  	   		   	  			  	
        # add code to plot here 			  		 			     			  	   		   	  			  	
        df_temp = pd.concat([port_prices, prices_SPY], keys=['Portfolio', 'SPY'], axis=1) 			  		 			     			  	   		   	  			  	
        df_temp.plot(title='Daily Portfolio Value and SPY',legend=True,grid=True)
        plt.grid(linestyle='dotted')        
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.savefig('plot.png', bbox_inches='tight')     
                   	   		   	  			  	
    return allocs, cr, adr, sddr, sr 			  		 			     			  	   		   	  			  	

def test_code(): 			  		 			     			  	   		   	  			  	
    # This function WILL NOT be called by the auto grader 			  		 			     			  	   		   	  			  	
    # Do not assume that any variables defined here are available to your function/code 			  		 			     			  	   		   	  			  	
    # It is only here to help you set up and test your code 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
    # Define input parameters 			  		 			     			  	   		   	  			  	
    # Note that ALL of these values will be set to different values by 			  		 			     			  	   		   	  			  	
    # the autograder! 			  		 			     			  	   		   	  			  	
    	  		 			     			  	   		   	  			  	
    start_date = dt.datetime(2009,1,1) 			  		 			     			  	   		   	  			  	
    end_date = dt.datetime(2010,1,1) 			  		 			     			  	   		   	  			  	
    symbols = ['GOOG', 'AAPL', 'GLD', 'XOM', 'IBM'] 			  		 			     			  	   		   	  			  	
		 
    # Assess the portfolio 			  		 			     			  	   		   	  			  	
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        gen_plot = False) 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
    # Print statistics 			  		 			     			  	   		   	  			  	
    print "Start Date:", start_date 			  		 			     			  	   		   	  			  	
    print "End Date:", end_date 			  		 			     			  	   		   	  			  	
    print "Symbols:", symbols 			  		 			     			  	   		   	  			  	
    print "Allocations:", allocations 			  		 			     			  	   		   	  			  	
    print "Sharpe Ratio:", sr 			  		 			     			  	   		   	  			  	
    print "Volatility (stdev of daily returns):", sddr 			  		 			     			  	   		   	  			  	
    print "Average Daily Return:", adr 			  		 			     			  	   		   	  			  	
    print "Cumulative Return:", cr 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
if __name__ == "__main__": 			  		 			     			  	   		   	  			  	
    # This code WILL NOT be called by the auto grader 			  		 			     			  	   		   	  			  	
    # Do not assume that it will be called 			  		 			     			  	   		   	  			  	
    test_code() 			  		 			     			  	   		   	  			  	
