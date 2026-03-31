import random

# Main menu for application 
def simMenu():
    print('Please Select a Simulation')
    print('1. Stock portfolio tracker with simulated daily price changes')
    print('2. Budget planner and monthly expense analyser')
    print('0. Exit')

# Portfolio class to hold multiple stocks and their quantities
class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = {} # Dictionary to hold stock objects and quantities

    def addStock(self, stock, quantity):
        # If the stock already exists the quantity is updated
        if stock.name in self.stocks:
            self.stocks[stock.name]["quantity"] += quantity
        # New stock is added to the portfolio
        else:
            self.stocks[stock.name] = {"stock": stock, "quantity": quantity}

# Stock class to hold stocks with their name and price
class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.history = [price] # To keep track of price history
    
    def update_price(self):
        change_percent = random.uniform(-0.065, 0.065) # Simulate price change between -6.5% and +6.5%
        self.price *= (1 + change_percent)

        if self.price < 0:
            self.price = 0 # Ensure price doesn't go negative
        
        self.history.append(self.price)

    # Function to return the current price of the stock
    def getValue(self):
        return self.price
    
    # Function to return the price history of the stock
    def getHistory(self):
        return self.history

# Function that returns a portfolio object
def createPortfolio():
    portfolioName = input('Enter Portfolio Name: ').strip().upper()
    return Portfolio(portfolioName)

# Function that returns a stock object
def createStock():
    stockName = input('Enter Stock Name: ').strip().upper()
    stockPrice = float(input('Enter Stock Price: '))
    return Stock(stockName, stockPrice)

def addStockToPortfolio(portfolio):
    stock = createStock()
    quantity = int(input('Enter Quantity: '))
    portfolio.addStock(stock, quantity)

def getDays():
    days = int(input('Enter number of days to simulate: '))
    return days

def simulateStockPriceChanges(portfolio, getDays):
    days = getDays()
    for day in range(days):
        print(f'Day {day + 1}:')
        for stockName, data in portfolio.stocks.items():
            stock = data["stock"]
            quantity = data["quantity"]
            stock.update_price()
            print(f'{stock.name}: {stock.getValue():.2f} (Quantity: {quantity})')
        print('')

def printAveragePrice(portfolio):
    for stockName, data in portfolio.stocks.items():
        stock = data["stock"]
        averagePrice = sum(stock.getHistory()) / len(stock.getHistory())
        print(f'{stock.name}: {averagePrice:.2f}')

def printMaxPrice(portfolio):
    for stockName, data in portfolio.stocks.items():
        stock = data["stock"]
        maxPrice = max(stock.getHistory())
        print(f'{stock.name}: {maxPrice:.2f}, Day: {stock.getHistory().index(maxPrice) + 1}')
    
def printMinPrice(portfolio):
    for stockName, data in portfolio.stocks.items():
        stock = data["stock"]
        minPrice = min(stock.getHistory())
        print(f'{stock.name}: {minPrice:.2f}, Day: {stock.getHistory().index(minPrice) + 1}')

def printAnalyticsOptions():
    print('Analytics Options:')
    print('1. Average Price')
    print('2. Maximum Price')
    print('3. Minimum Price')
    print('0. Back to Main Menu')

def stockPortfolioTracker():
    portfolio = createPortfolio()
    while True:
        addStockToPortfolio(portfolio)
        cont = input('Add another stock? (y/n): ').strip().lower()
        if cont != 'y' and cont != 'n':
            print('Invalid input. Please enter "y" or "n".')
        elif cont == 'n':
            break
    simulateStockPriceChanges(portfolio, getDays)

    printAnalyticsOptions()
    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            printAveragePrice(portfolio)
        elif choice == '2':
            printMaxPrice(portfolio)
        elif choice == '3':
            printMinPrice(portfolio)
        elif choice == '0':
            break
        else:
            print('Invalid choice.')
            print('')

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