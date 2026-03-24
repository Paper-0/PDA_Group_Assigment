# SimulationMenu

def simMenu():
    print('Please Select a Simulation')
    print('1. Stock portfolio tracker with simulated daily price changes')
    print('2. Budget planner and monthly expense analyser')
    print('0. Exit')

def stockPortfolioTracker():
    print("__STOCK PORTFOLIO TRACKER__")

    
def budgetPlanner():
    print("__BUDGET PLANNER__")

def main():
    while True:
        simMenu()
        choice = input('Enter your choice: ')
        if choice == '1':
            stockPortfolioTracker()
        elif choice == '2':
            budgetPlanner()
        elif choice == '0':
            print('Exiting the program...')
            break
        else:
            print('Invalid choice.')
            print('')
