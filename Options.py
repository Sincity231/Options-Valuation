import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import minimize

class BlackScholes:
    #Class to calculate (European) call and put option prices through
    #the Black-Scholes formula without dividends
    #:param S: Price of underlying stock
    #:param K: Strike price
    #:param T: Time until expiration (Years)
    #:param R: Risk-free interest rate (0.05 indicates 5%)
    #:param sigma: Volatility (Standard deviation) of stock (0.15 = 15%)

    @staticmethod
    def d1(S,K,T,r,sigma):
        return (1 / (sigma * np.sqrt(T))) * (np.log(S/K) + (r + sigma**2 / 2) *T)

    def d2(self, S, K, T, r, sigma):
        return self.d1(S, K, T, r, simga) - sigma * np.sqrt(T)

    def call_price(self, S, K, T, r, sigma):
        #Main method for clacualting price of a call option
        _d1 = self.d1(S, K, T, r, simga)
        _d2 = self.d2(S, K, T, r, simga)
        return norm.cdf(_d1) * S - norm.cdf(_d2) * K * np.exp(-r*T)

    def put_price(self, S, K, T, r, sigma):
        #Main method for calculating price of a put option
        _d1 = self.d1(S, K, T, r, sigma)
        _d2 = self.d2(S, K, T, r, sigma)
        return norm.cdf(-_d2) * K * np.exp(-r*T) - norm.cdf(-_d1) * S

    def call_in_the_money(self, S, K, T, r, sigma):
        #Calculate the probability of the call option being in the money by
        #expiration according to Black-Scholes.
        _d2 = self.d2(S, K, T, r, sigma)
        return norm.cdf(_d2)

    def put_in_the_money(self, S, K, T, r, sigma):
        #Calculate the probability of the put option being in the money by
        #expiration according to Black-Scholes.
        _d2 = self.d2(S, K, T, r, sigma)
        return 1 - norm.cdf(_d2)

print (BlackScholes.d1(192, 190, 0.0136986, 0.05, 0.15)) #Test1
