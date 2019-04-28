"""Assess a betting strategy. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
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
 			  		 			     			  	   		   	  			  	
import numpy as np 	
from matplotlib import pyplot as plt 
 			  		 			     			  	   		   	  			  	
def author(): 			  		 			     			  	   		   	  			  	
        return 'tb34' # replace tb34 with your Georgia Tech username. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def gtid(): 			  		 			     			  	   		   	  			  	
	return 900897987 # replace with your GT ID number 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def get_spin_result(win_prob): 			  		 			     			  	   		   	  			  	
	result = False 			  		 			     			  	   		   	  			  	
	if np.random.random() <= win_prob: 			  		 			     			  	   		   	  			  	
		result = True 			  		 			     			  	   		   	  			  	
	return result 			 

def gambling_simulator(win_prob,n,stop_amount,winnings,sim_count,total):
    bet_amount = 1
    for i in xrange(1,n+1):        
        won = get_spin_result(win_prob)
        if won:
            winnings[sim_count][i] = winnings[sim_count][i-1] + bet_amount            
            if winnings[sim_count][i] >= 80:
                winnings[sim_count][i+1:] = winnings[sim_count][i]
                break
            bet_amount = 1
        else:
            winnings[sim_count][i] = winnings[sim_count][i-1] - bet_amount
            if total > 0 and winnings[sim_count][i] + total == 0:
                winnings[sim_count][i+1:] = winnings[sim_count][i]
                break                        
            if total > 0 and winnings[sim_count][i] - bet_amount + total < 0:
                bet_amount = total + winnings[sim_count][i]
            else:    
                bet_amount *= 2 
 			  		 			     			  	   		   	  			  	
def test_code(): 			  		 			     			  	   		   	  			  	        
    win_prob = 18./38.
    np.random.seed(gtid()) # do this only once 			  		 			     			  	   		   	  			  	     
    print get_spin_result(win_prob) # test the roulette spin 			  		 			     			  	   		   	  			  		      
 			  		 			     			  	   		   	  			  	
 	 # add your code here to implement the experiments
    n = 1000 # max number of spins in one game
    stop_amount = 80 # quit game if winning more than this amount
    x = np.linspace(0,n,n+1)  
    plt.cla()    

    # figure 1: plot 10 paths     
    winnings = np.zeros((10,n+1))
    for i in xrange(10):        
        gambling_simulator(win_prob,n,stop_amount,winnings,i,-1)
        plt.plot(x,winnings[i])
    plt.xlim(0, 300)
    plt.ylim(-256, 100) 
    plt.xlabel("# of spins")
    plt.ylabel("Episode Winning")
    plt.savefig('exp1.png', bbox_inches='tight')
    plt.cla()
	
    # figure 2: plot mean, mean \pm std of 1000 paths
    winnings = np.zeros((1000,n+1))
    for i in xrange(1000):        
        gambling_simulator(win_prob,n,stop_amount,winnings,i,-1)   
    avg = np.mean(winnings,axis=0)    
    std = np.std(winnings,axis=0)    
    mdn = np.median(winnings,axis=0)    
    print avg[-1]
    plt.plot(x,avg,x,avg-std,'--',x,avg+std,'--')    
    plt.xlim(0, 300)
    plt.ylim(-256, 100) 
    plt.xlabel("# of spins")
    plt.ylabel("Winning")
    plt.title(r'Mean and Mean $\pm$ Std')
    plt.savefig('exp2.png', bbox_inches='tight')     
    plt.cla()
    
    # figure 3: plot median, median \pm std of 1000 paths
    plt.plot(x,mdn,x,mdn-std,'--',x,mdn+std,'--')    
    plt.xlim(0, 300)
    plt.ylim(-256, 100) 
    plt.xlabel("# of spins")
    plt.ylabel("Winning")
    plt.title(r'Median and Median $\pm$ Std')
    plt.savefig('exp3.png', bbox_inches='tight')     
    plt.cla()         

    # figure 4: plot mean, mean \pm std of 1000 paths for realistic scenario
    winnings = np.zeros((1000,n+1))
    for i in xrange(1000):        
        gambling_simulator(win_prob,n,stop_amount,winnings,i,256)        
    avg = np.mean(winnings,axis=0)    
    std = np.std(winnings,axis=0)    
    mdn = np.median(winnings,axis=0)    
    plt.plot(x,avg,x,avg-std,'--',x,avg+std,'--')    
    plt.xlim(0, 300)
    plt.ylim(-256, 100) 
    plt.xlabel("# of spins")
    plt.ylabel("Winning")
    plt.title(r'Mean and Mean $\pm$ Std with $\$256$ bank roll')
    plt.savefig('exp4.png', bbox_inches='tight')     
    plt.cla()

    # figure 5: plot median, median \pm std of 1000 paths for realistic scenario    
    plt.plot(x,mdn,x,mdn-std,'--',x,mdn+std,'--')    
    plt.xlim(0, 300)
    plt.ylim(-256, 100) 
    plt.xlabel("# of spins")
    plt.ylabel("Winning")
    plt.title(r'Median and Median $\pm$ Std with $\$256$ bank roll')
    plt.savefig('exp5.png', bbox_inches='tight')     
    plt.cla()         
    
if __name__ == "__main__": 			  		 			     			  	   		   	  			  	
    test_code()