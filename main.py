from datetime import datetime
from AlgorithmImports import *


class Sergiobot(QCAlgorithm):
    # Initialize: Time period, Cash, Security + Time frame, &
    # Data
    def Initialize(self):
        self.SetStartDate(2013, 10, 7)  # Set Start Date
        self.SetEndDate(2013, 10, 11)  # Set End Date
        self.SetCash(100000)  # Set  Cash
        self.AddEquity("NAS100", Resolution.Minute)


     # OnData event is where our algorithm lives. New data points are pumped into this f(x).
    def OnData(self, data):

          # define strategy here:
        # The MACD, RSI, STOCH will be used as TA indicators that must be satisfied before a trade can be place. 
        # The ATR is used to dynamically set stoploss and take profit. 

        # Pattern Recognition?

        # Eventually: Implement some form of sentiment analysis via Tensor flow or some ML package. Sergio will use this SA as a flag to determine if a trade is good or not. 

        # - MACD
        # initialize the macd(12,26) w/ 9 day signal
        self.macd = self.MACD("NAS100", 12, 26, 9, MovingAverageType.Exponential, Resolution.Daily)
        # store datetime in var
        self.previous = datetime.min
        # Plot MACD Indicator + Signal 
        self.PlotIndicator("MACD" , True, self.macd, self.macd.Signal )
        # Plot NAS100, fast period, slow period
        self.PlotIndicator("NAS100", self.macd.Fast, self.macd.Slow)
        # - RSI
        # - Stoch
        # - ATR 



        
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)
            self.Debug("Purchased Stock")
