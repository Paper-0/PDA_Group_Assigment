# SimulationMenu

import random


def simMenu():
    print('Please Select a Simulation')
    print('1. Stock portfolio tracker with simulated daily price changes')
    print('2. Budget planner and monthly expense analyser')
    print('0. Exit')

# Stock class to hold stocks with their name and price
class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def update_price(self):
        change_percent = random.uniform(-0.05, 0.05) # Simulate price change between -5% and +5%
        self.price *= (1 + change_percent)

        if self.price < 0:
            self.price = 0 # Ensure price doesn't go negative

    def getValue(self):
        return self.price

# Portfolio class to hold multiple stocks and their quantities
class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = {} # Dictionary to hold stock names and their quantities

    def addStock(self, stock, quantity):
        if stock.name in self.stocks:
            self.stocks[stock.name] += quantity
        else:
            self.stocks[stock.name] = quantity

def createStock():
    stockName = input('Enter Stock Name: ').strip().upper()
    stockPrice = float(input('Enter Stock Price: '))
    return Stock(stockName, stockPrice)

def createPortfolio():
    portfolioName = input('Enter Portfolio Name: ').strip().upper()
    return Portfolio(portfolioName)

def addStockToPortfolio(portfolio):
    stock = createStock()
    quantity = int(input('Enter Quantity: '))
    portfolio.addStock(stock, quantity)

def simulateStockPriceChanges(portfolio, getDays):
    days = getDays()
    for day in range(days):
        print(f'Day {day + 1}:')
        for (stockName, quantity) in portfolio.stocks.items():
            stock = Stock(stockName, 0) # Create a stock object with the name and a dummy price
            stock.update_price() # Simulate price change
            print(f'{stock.name}: {stock.getValue():.2f} (Quantity: {quantity})')
        print('')
def getDays():
    days = int(input('Enter number of days to simulate: '))
    return days

def stockPortfolioTracker():
    portfolio = createPortfolio()
    while True:
        addStockToPortfolio(portfolio)
        cont = input('Add another stock? (y/n): ').strip().lower()
        if cont != 'y':
            break
    simulateStockPriceChanges(portfolio, getDays)




def main():
    while True:
        simMenu()
        choice = input('Enter your choice: ')
        if choice == '1':
            stockPortfolioTracker()
        elif choice == '2':
            break
        elif choice == '0':
            print('Exiting the program...')
            break
        else:
            print('Invalid choice.')
            print('')
main()