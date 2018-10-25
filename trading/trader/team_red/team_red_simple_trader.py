"""
Created on 08.11.2017

@author: jtymoszuk
"""
from model.Portfolio import Portfolio
from model.StockMarketData import StockMarketData
from model.CompanyEnum import CompanyEnum
from model.ITrader import ITrader
from model.Order import OrderList
from model.IPredictor import IPredictor

from logger import logger

class TeamRedSimpleTrader(ITrader):
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

        orders = OrderList()

        cheapest_company = min(list(CompanyEnum), key=lambda c: stock_market_data.get_most_recent_price(c))

        cash_per_comp = portfolio.cash / stock_market_data.get_number_of_companies()

        price = stock_market_data.get_most_recent_price(cheapest_company)
        num_shares_to_buy = cash_per_comp // price
        if num_shares_to_buy > 0:
            orders.buy(cheapest_company, num_shares_to_buy)
            logger.info("Bought {0} shares.".format(num_shares_to_buy))

        return orders
