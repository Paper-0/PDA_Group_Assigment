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
    try:
        stockName = input('Enter Stock Name: ').strip().upper()
        stockPrice = float(input('Enter Stock Price: '))
    except ValueError:
        print('Invalid input. Please enter a valid stock price.')
        return createStock()
    return Stock(stockName, stockPrice) # Returns stock object

# Function to add a stock to the portfolio
def addStockToPortfolio(portfolio):
    try:
        stock = createStock() # Create a stock object
        quantity = int(input('Enter Quantity: '))
        portfolio.addStock(stock, quantity) # Add the stock to the portfolio
    except ValueError:
        print('Invalid input. Please enter a valid quantity.')
        addStockToPortfolio(portfolio)

# Get number of days to simulate stock price changes
def getDays():
    try:
        days = int(input('Enter number of days to simulate: '))
    except ValueError:
        print('Invalid input. Please enter a valid number of days.')
        return getDays()
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
        while True:
            cont = input('Add another stock? (y/n): ').strip().lower()
            if cont == 'y':
                break
            elif cont == 'n':
                simulateStockPriceChanges(portfolio, getDays)
                while True:
                    printAnalyticsOptions()
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
                return
            else:
                print('Invalid input. Please enter "y" or "n".')

# Function to input values for the income and expenses 
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Try again.")
            else:
                return value
        except ValueError: 
             print("Invalid input. Please enter a number.")

# Function to input income 
def add_income():
    income = get_float_input("Enter your monthly income: $")
    print("Income was recorded ")
    return income

# Function to input expenses
def add_expense(expenses):
    category = input("Enter expense category (e.g. Food, Rent, Transport): ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    amount = get_float_input("Enter amount: $")
    expenses[category] = expenses.get(category, 0) + amount
    print("Expense was added")

# Function to view expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return 
    print("Expense List")
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
    print()

# Function to calculate monthly summary 
def monthly_summary(income, expenses):
    if income == 0:
        print("Please add income first")
        return
    total_expenses = sum(expenses.values())
    balance = income - total_expenses
    print("Monthly Summary")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")
    if balance < 0:
        print("Warning: You are overspending")
    else:
        print()

# Function to analyse expenses 
def expense_analysis(expenses):
    if not expenses:
        print("No expenses to analyze.")
        return
    print("Expense Analysis")
    total = sum(expenses.values())
    for category, amount in expenses.items():
        percentage = (amount / total) * 100
        print(f"{category}: {percentage:.2f}%")
    print()

# Calling functions 
def budgetPlanner():
    expenses = {}
    income = 0
    while True:
        print("Budget Planner")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Monthly Summary")
        print("5. Expense Analysis")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            income = add_income()
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            view_expenses(expenses)
        elif choice == "4":
            monthly_summary(income, expenses)
        elif choice == "5":
            expense_analysis(expenses)
        elif choice == "6":
            print("Exiting program... Goodbye")
            break
        else:
            print("Invalid choice. Try again.")

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