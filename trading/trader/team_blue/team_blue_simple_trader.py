"""
Created on 08.11.2017

@author: jtymoszuk
"""
import math

from model.CompanyEnum import CompanyEnum
from model.Portfolio import Portfolio
from model.StockMarketData import StockMarketData
from model.ITrader import ITrader
from model.Order import OrderList
from model.IPredictor import IPredictor


class TeamBlueSimpleTrader(ITrader):
    """
    Simple Trader generates Order based on simple logic, input data and prediction from NN-Engine
    """

    def __init__(self, stock_a_predictor: IPredictor, stock_b_predictor: IPredictor):
        """
        Constructor
        """
        self.stock_a_predictor = stock_a_predictor
        self.stock_b_predictor = stock_b_predictor

    def doTrade(self, portfolio: Portfolio, current_portfolio_value: float,
                stock_market_data: StockMarketData) -> OrderList:
        """
        Generate action to be taken on the "stock market"
    
        Args:
          portfolio : current Portfolio of this trader
          current_portfolio_value : value of Portfolio at given Momemnt
          stock_market_data : StockMarketData for evaluation

        Returns:
          A OrderList instance, may be empty never None
        """

        y_a = stock_market_data.get_most_recent_price(CompanyEnum.COMPANY_A)
        y_b = stock_market_data.get_most_recent_price(CompanyEnum.COMPANY_B)

        p_a = self.stock_a_predictor.doPredict(stock_market_data[CompanyEnum.COMPANY_A]);
        p_b = self.stock_b_predictor.doPredict(stock_market_data[CompanyEnum.COMPANY_B]);

        r_a = (p_a - y_a) / y_a * 100;
        r_b = (p_b - y_b) / y_b * 100;

        result = OrderList()

        if (r_a < 0 and portfolio.get_amount(CompanyEnum.COMPANY_A) > 0):
            result.sell(CompanyEnum.COMPANY_A, portfolio.get_amount(CompanyEnum.COMPANY_A))

        if (r_b < 0 and portfolio.get_amount(CompanyEnum.COMPANY_B) > 0):
            result.sell(CompanyEnum.COMPANY_B, portfolio.get_amount(CompanyEnum.COMPANY_B))


        if (r_a <= 0 and r_b <= 0):
            return result


        company = CompanyEnum.COMPANY_A

        if (r_b > r_a):
            company = CompanyEnum.COMPANY_B

        buy_amount = math.floor(portfolio.cash / stock_market_data.get_most_recent_price(company))

        if (portfolio.cash > 0 and buy_amount > 0):
            result.buy(company, buy_amount)


        print("Portfolio: " + str(portfolio.total_value(stock_market_data.get_most_recent_trade_day(), stock_market_data)));



        # TODO: implement trading logic

        return result
