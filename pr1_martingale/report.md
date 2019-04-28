# Project 1: Martingale
## Plots produced by code:
![fig1](https://raw.githubusercontent.com/zhexuanz/ML4T/master/pr1_martingale/exp1.png)

Figure 1. plot of 10 paths of the gabling simulation assuming no limit on bank roll

![fig2](https://raw.githubusercontent.com/zhexuanz/ML4T/master/pr1_martingale/exp2.png)

Figure 2. plot of mean, mean +/- std of 1000 paths assuming no limit on bank roll

![fig3](https://raw.githubusercontent.com/zhexuanz/ML4T/master/pr1_martingale/exp3.png)

Figure 3. plot of median, median +/- std of 1000 paths assuming no limit on bank roll

![fig4](https://raw.githubusercontent.com/zhexuanz/ML4T/master/pr1_martingale/exp4.png)

Figure 4. plot of mean, mean +/- std of 1000 paths assuming $256 bank roll limit

![fig5](https://raw.githubusercontent.com/zhexuanz/ML4T/master/pr1_martingale/exp5.png)

Figure 5. plot of median, median +/- std of 1000 paths assuming $256 bank roll limit

## Q&A:
1. In Experiment 1, what is the estimated expected value of our winnings after 1000 sequential bets? Explain your reasoning

Expected value is 80. Every win will add 1 dollar to the current episode regardless how many prior losses before the win spin. Thus, if the expected number winning spin is more than 80 in the 1000 spins, the solution will be 80. Given the binomial distrubition, the number of spins required to reach 80 as expected winnings is 80/(18/38) = 169

2. In Experiment 1, does the standard deviation reach a maximum value then stabilize as the number of sequential bets increases? Explain why it does (or does not).

Yes, as shown by the plot below of standard deviation v.s. number of sequenty bets. Standard deviation is high when number of sequential draws is small because any consecutive loss spin will drive up the standard deviation. As number of sequential draws increases, probability of having less than 80 win spin becomes less and less, thus standard deviation becoming really small
![fig6](https://raw.githubusercontent.com/zhexuanz/ML4T/master/pr1_martingale/support1.png)

Figure 6. plot of standard deviation of 1000 paths assuming no bank roll

3. In Experiment 2, estimate the probability of winning $80 within 1000 sequential bets. Explain your reasoning.

The numerical estimate from 1000 simulations is 0.638. This is basically the probability of not having consecutive 8 loss spins in the 1000 bets

4. In Experiment 2, what is the estimated expected value of our winnings after 1000 sequential bets? Explain your reasoning.

The numerical estimate from 1000 simulations is -41.6 = 0.638*80-ги1-0.638)*256

5. In Experiment 2, does the standard deviation reach a maximum value then stabilize as the number of sequential bets increases? Explain why it does (or does not).

No, as shown by the plot below of standard deviation v.s. number of sequenty bets. Standard deviation will increase as we increase the number of sequential bets. When increasing number of sequential bets, there are higher probabilities of having 8 consecutive loss spin which will triger the 256 episode loss, thus higher probability of bigger deviation from the mean.

![fig7](https://raw.githubusercontent.com/zhexuanz/ML4T/master/pr1_martingale/support2.png)

Figure 7. plot of standard deviation of 1000 paths assuming $256 bank roll limit
