"""
Created on 08.11.2017

@author: jtymoszuk
"""
from model.Portfolio import Portfolio
from model.StockMarketData import StockMarketData
from model.ITrader import ITrader
from model.Order import OrderList
from model.IPredictor import IPredictor
from model.CompanyEnum import CompanyEnum


class TeamBlackSimpleTrader(ITrader):
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

        order_list = OrderList()

        pred_a_value = self.stock_a_predictor.doPredict(stock_market_data[CompanyEnum.COMPANY_A])
        pred_b_value = self.stock_b_predictor.doPredict(stock_market_data[CompanyEnum.COMPANY_B])

        stock_a = portfolio.get_amount(CompanyEnum.COMPANY_A)
        stock_a_value = stock_market_data.get_most_recent_price(CompanyEnum.COMPANY_A)
        stock_b = portfolio.get_amount(CompanyEnum.COMPANY_B)
        stock_b_value = stock_market_data.get_most_recent_price(CompanyEnum.COMPANY_B)

        increase_a = pred_a_value - stock_a_value
        increase_b = pred_b_value - stock_b_value

        new_cash = 0.0

        if stock_a > 0 and increase_a < 0.0:
            order_list.sell(CompanyEnum.COMPANY_A, stock_a)

        if stock_b > 0 and increase_b < 0.0:
            order_list.sell(CompanyEnum.COMPANY_B, stock_b)

        if increase_a > increase_b and increase_a > 0.0:
            count_a = portfolio.cash / stock_a_value
            if count_a > 0:
                order_list.buy(CompanyEnum.COMPANY_A, int(count_a))
        elif increase_b > increase_a and increase_b > 0.0:
            count_b = portfolio.cash / stock_b_value
            if count_b > 0:
                order_list.buy(CompanyEnum.COMPANY_B, int(count_b))




        # TODO: implement trading logic

        return order_list
