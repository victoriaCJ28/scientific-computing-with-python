def add_expense(expenses, amount, category):
    # Agrega un nuevo gasto a la lista de gastos
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    # Imprime todos los gastos registrados
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    # Calcula e imprime el total de todos los gastos
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    # Filtra y devuelve los gastos que pertenecen a una categoría específica
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    # Función principal que maneja la lógica del programa
    expenses = []  # Lista para almacenar los gastos
    while True:
        # Menú de opciones para el usuario
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            # Agregar un nuevo gasto
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # Mostrar todos los gastos registrados
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            # Mostrar el total de los gastos
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            # Filtrar y mostrar los gastos por categoría
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            # Salir del programa
            print('Exiting the program.')
            break

# Ejecutar la función principal
main()
