import tkinter

def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Erreur: Division par zéro"

def calculer_resultat(operation, num1, num2):
    if operation == '+':
        return addition(num1, num2)
    elif operation == '-':
        return soustraction(num1, num2)
    elif operation == '*':
        return multiplication(num1, num2)
    elif operation == '/':
        return division(num1, num2)
    else:
        return "Opération non valide"

while True:
    expression = input("Entrez une expression (ex: 3 + 4 * 2 / 5), 'exit' pour quitter : ")

    if expression.lower() == 'exit':
        print("Au revoir !")
        break

    try:
        # Utilisation de la fonction eval pour évaluer l'expression
        resultat = eval(expression)
        print("Résultat :", resultat)
    except Exception as e:
        print("Erreur :", e)
