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
    return Portfolio(portfolioName) # Returns portfolio object 

# Function that returns a stock object
def createStock():
    stockName = input('Enter Stock Name: ').strip().upper()
    stockPrice = float(input('Enter Stock Price: '))
    return Stock(stockName, stockPrice) # Returns stock object

# Function to add a stock to the portfolio
def addStockToPortfolio(portfolio):
    stock = createStock() # Create a stock object
    quantity = int(input('Enter Quantity: '))
    portfolio.addStock(stock, quantity) # Add the stock to the portfolio

# Get number of days to simulate stock price changes
def getDays():
    days = int(input('Enter number of days to simulate: '))
    return days # Returns the number of days

# Function to simulate stock price changes over a number of days
def simulateStockPriceChanges(portfolio, getDays):
    days = getDays() 
    for day in range(days):
        print(f'Day {day + 1}:')
        for stockName, data in portfolio.stocks.items(): # Prints the current price of each stock in the portfolio
            stock = data["stock"]
            quantity = data["quantity"]
            stock.update_price()
            print(f'{stock.name}: {stock.getValue():.2f} (Quantity: {quantity})')
        print('')

# Prints Average price of each stock in the portfolio
def printAveragePrice(portfolio):
    for stockName, data in portfolio.stocks.items():
        stock = data["stock"]
        averagePrice = sum(stock.getHistory()) / len(stock.getHistory())
        print(f'{stock.name}: {averagePrice:.2f}')

# Prints the maximum price of each stock in the portfolio and the day it occurred on
def printMaxPrice(portfolio):
    for stockName, data in portfolio.stocks.items():
        stock = data["stock"]
        maxPrice = max(stock.getHistory())
        print(f'{stock.name}: {maxPrice:.2f}, Day: {stock.getHistory().index(maxPrice) + 1}')

# Prints the minimum price of each stock in the portfolio and the day it occurred on
def printMinPrice(portfolio):
    for stockName, data in portfolio.stocks.items():
        stock = data["stock"]
        minPrice = min(stock.getHistory())
        print(f'{stock.name}: {minPrice:.2f}, Day: {stock.getHistory().index(minPrice) + 1}')

# Function to print the analytics options for the user to choose from
def printAnalyticsOptions():
    print('Analytics Options:')
    print('1. Average Price')
    print('2. Maximum Price')
    print('3. Minimum Price')
    print('0. Back to Main Menu')

# Function to run the stock portfolio tracker simulation
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


budgetHistory = [] 

# Function to get the user's monthly income with input validation
def getIncome():
    while True:
        try:
            income = float(input("Enter this month income: "))
            if income <= 0:
                print("Income must be more than 0")
                continue
            return income
        except ValueError:
            print("Invalid input, try again.")

# Function to get an expense with its name and amount
def getExpense():
    expense_name = input("Enter your expense name: ").strip()
    while True:
        try:
            expense_amt = float(input(f"Enter the amount for '{expense_name}': "))
            if expense_amt < 0:
                print("Amount cannot be negative.")
                continue
            return {"Name": expense_name, "Amount": expense_amt}
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to add expenses
def addExpense():
    expenses = []
    while True:
        try:
            count = int(input("Enter the number of expenses to be added: "))
            if count <= 0:
                print("Number must be greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input.")
    for i in range(count):
        expenses.append(getExpense())

    return expenses

# Function to calculate totals
def calculateTotals(income, expenses):
    totalExpenses = sum(item["Amount"] for item in expenses)
    netIncome = income - totalExpenses
    return totalExpenses, netIncome

# Function to calculate statistics
def calculateStats(amounts):
    if len(amounts) == 0:
        return None
    stats = {}  
    stats["mean"] = sum(amounts) / len(amounts)
    stats["max"] = max(amounts)
    stats["min"] = min(amounts)
    stats["count"] = len(amounts)
    return stats

# Financial analysis
def analysis(income, totalExpenses, netIncome):
    print("\nFinancial Analysis")
    if totalExpenses > income:  
        print("You are spending more than your income!")
    elif netIncome > 0:
        savingsRate = (netIncome / income) * 100
        print(f"You saved {savingsRate:.2f}% of your income.")
    else:
        print("You broke even this month.")

# Display summary
def displaySummary(income, expenses, total, balance, stats):
    print("\nMonthly Budget Summary")
    print(f"Income: {income:.2f}")
    print("\nExpenses:")
    for item in expenses:
        print(f" {item['Name']}: {item['Amount']:.2f}")
    print(f"\nTotal Expenses: {total:.2f}")
    print(f"Remaining Balance: {balance:.2f}")
# stats
    print("\nStatistics")
    print(f"Average Expense: {stats['mean']:.2f}")
    print(f"Highest Expense: {stats['max']:.2f}")
    print(f"Lowest Expense: {stats['min']:.2f}")
    print(f"Number of Expenses: {stats['count']}")

# Main budget planner
def budgetPlanner():
    print("\nBudget Planner & Expense Analyzer")
    income = getIncome()
    expenses = addExpense()

    totalExpenses, netIncome = calculateTotals(income, expenses)

    amounts = [item["Amount"] for item in expenses]
    stats = calculateStats(amounts)

    displaySummary(income, expenses, totalExpenses, netIncome, stats)
    analysis(income, totalExpenses, netIncome)

# Main function to run the program
def main():
    while True:
        simMenu()
        choice = input('Enter your choice: ')
        if choice == '1':
            stockPortfolioTracker()
        elif choice == '2':
            budgetPlanner()
            break
        elif choice == '0':
            print('Exiting the program...')
            break
        else:
            print('Invalid choice.')
            print('')
main()