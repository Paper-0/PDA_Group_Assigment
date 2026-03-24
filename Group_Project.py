# Group Project Simulation for PDA
# Group Members: Jordan Rerrie(2509926), 

import random
import statistics

# Menu to select between stock portfolio tracker and budget planner 
def simMenu():
    print('\n=================================')
    print('PDA GROUP PROJECT SIMULATION ')
    print('Please Select a Simulation')
    print('1. Stock portfolio tracker with simulated daily price changes')
    print('2. Budget planner and monthly expense analyser')
    print('0. Exit')
    print('=================================\n')

# Class to represent a stock in the portfolio
class Stock:
    def __init__(self, name, price, shares):
        self.name = name
        self.price = price
        self.shares = shares

    def update_price(self):
        change_percent = random.uniform(-0.05, 0.05)  # Simulate daily price change between -5% and +5%
        self.price *= (1 + change_percent)

        if self.price < 0:
            self.price = 0

    def get_value(self):
        return self.price * self.shares

class Portfolio:
    def __init__(self, username):
        self.username = username
        self.stocks = []

    def addStock(self, stock):
        self.stocks.append(stock)

# Function to create a stock
def createStock():
    name = input('Enter stock name: ').strip().upper()
    price = float(input('Enter stock price: '))
    shares = int(input('Enter number of shares: '))
    return Stock(name, price, shares)

def createPortfolio():
    username = input('Enter your Name: ').strip().upper()
    return Portfolio(username)

# Function to get the number of days to simulate
def getDays():
    while True:
        days = int(input('Enter number of days to simulate: '))
        if days > 0:
            return days
        else:
            print('Please enter a positive integer for days.')

# Function to simulate stock price changes over a number of days
def simulateStock(stock, days):
    dailyPrices = []
    dailyValues = []
    
    for day in range(days):
        stock.update_price()

        dailyPrices.append(stock.price)
        dailyValues.append(stock.get_value())

        print(f'Day {day + 1}: Price = ${stock.price:.2f}, Portfolio Value = ${stock.get_value():.2f}')

        return dailyPrices, dailyValues

# Main function to run the program
def main():
    while True:
        simMenu()
        choice = input('Enter your choice: ')
        if choice == '1':
            simulateStock(createStock(), getDays())
            break
        elif choice == '2':
            break
        elif choice == '0':
            print('Exiting the program...')
            break
        else:
            print('Invalid choice.')
            print('')
main()
