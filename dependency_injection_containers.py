'''
Created on 09.11.2017

@author: jtymoszuk
'''
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from model.CompanyEnum import CompanyEnum
from predicting.predictor.reference.random_predictor import RandomPredictor
from predicting.predictor.reference.perfect_predictor import PerfectPredictor
from trading.trader.reference.buy_and_hold_trader import BuyAndHoldTrader
from predicting.predictor.team_blue.team_blue_predictor import TeamBlueStockAPredictor, \
    TeamBlueStockBPredictor
from predicting.predictor.team_green.team_green_predictor import TeamGreenStockAPredictor, \
    TeamGreenStockBPredictor
from predicting.predictor.team_pink.team_pink_predictor import TeamPinkStockBPredictor, \
    TeamPinkStockAPredictor
from predicting.predictor.team_red.team_red_predictor import TeamRedStockBPredictor, \
    TeamRedStockAPredictor
from trading.trader.team_blue.team_blue_simple_trader import TeamBlueSimpleTrader
from trading.trader.team_green.team_green_simple_trader import TeamGreenSimpleTrader
from trading.trader.team_pink.team_pink_simple_trader import TeamPinkSimpleTrader
from trading.trader.team_red.team_red_simple_trader import TeamRedSimpleTrader


class Predictors(containers.DeclarativeContainer):
    """IoC container of predictor providers."""
 
    """ Random predictor delivering value of last share +- Random[0,1]"""
    RandomPredictor = providers.Factory(RandomPredictor)
    
    """ Perfect predictors knowing future"""
    # Task 0 and Task 2
    PerfectPredictor_stock_a = providers.Factory(PerfectPredictor, CompanyEnum.COMPANY_A)    
    PerfectPredictor_stock_b = providers.Factory(PerfectPredictor, CompanyEnum.COMPANY_B)
    
    """Initial empty Predictors for training purposes"""
    """Team Blue Predictors"""
    # Task 1
    TeamBlueStockAPredictor = providers.Factory(TeamBlueStockAPredictor)
    TeamBlueStockBPredictor = providers.Factory(TeamBlueStockBPredictor)
    
    """Team Green Predictors"""
    # Task 1
    TeamGreenStockAPredictor = providers.Factory(TeamGreenStockAPredictor)
    TeamGreenStockBPredictor = providers.Factory(TeamGreenStockBPredictor)
        
    """Team Pink Predictors"""
    # Task 1
    TeamPinkStockAPredictor = providers.Factory(TeamPinkStockAPredictor)
    TeamPinkStockBPredictor = providers.Factory(TeamPinkStockBPredictor)
            
    """Team Red Predictors"""
    # Task 1
    TeamRedStockAPredictor = providers.Factory(TeamRedStockAPredictor)
    TeamRedStockBPredictor = providers.Factory(TeamRedStockBPredictor)

 
class Traders(containers.DeclarativeContainer):
    """IoC container of trader providers."""

    """Buy and Hold Trader"""
    BuyAndHoldTrader = providers.Factory(
        BuyAndHoldTrader
        )
   
    """Traders for training purposes"""
    """Team Blue Traders"""
    # Task 0
    TeamBlueSimpleTrader_with_perfect_prediction = providers.Factory(
        TeamBlueSimpleTrader,
        stock_a_predictor=Predictors.PerfectPredictor_stock_a,
        stock_b_predictor=Predictors.PerfectPredictor_stock_b
        )
    
    """Team Green Traders"""
    # Task 0
    TeamGreenSimpleTrader_with_perfect_prediction = providers.Factory(
        TeamGreenSimpleTrader,
        stock_a_predictor=Predictors.PerfectPredictor_stock_a,
        stock_b_predictor=Predictors.PerfectPredictor_stock_b
        )
       
    """Team Pink Traders"""
    # Task 0
    TeamPinkSimpleTrader_with_perfect_prediction = providers.Factory(
        TeamPinkSimpleTrader,
        stock_a_predictor=Predictors.PerfectPredictor_stock_a,
        stock_b_predictor=Predictors.PerfectPredictor_stock_b
        )
           
    """Team Red Traders"""
    # Task 0
    TeamRedSimpleTrader_with_perfect_prediction = providers.Factory(
        TeamRedSimpleTrader,
        stock_a_predictor=Predictors.PerfectPredictor_stock_a,
        stock_b_predictor=Predictors.PerfectPredictor_stock_b
        )
    
