def arithmetic_arranger(problems, show_answers=False):
    # Verifica que no haya más de 5 problemas
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Listas para almacenar las diferentes partes de los problemas
    first_line = []
    second_line = []
    botton_lines = []
    answers = []

    # Procesa cada problema individualmente
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'
        
        num1, operator, num2 = parts

        # Verifica que el operador sea + o -
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Verifica que ambos operandos sean numéricos
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        # Verifica que los operandos no tengan más de 4 dígitos
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calcula el ancho necesario para alinear el problema
        width = max(len(num1), len(num2)) + 2

        # Alinea y guarda cada parte del problema
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        botton_lines.append('-' * width)

        # Si se solicita mostrar las respuestas, calcula y guarda el resultado
        if show_answers: 
            if operator == '+':
                answer = str(int(num1) + int(num2))
            elif operator == '-':
                answer = str(int(num1) - int(num2))
            answers.append(answer.rjust(width))
    
    # Une todas las líneas con 4 espacios de separación
    problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(botton_lines)

    # Si show_answers es True, añade la línea de respuestas
    if show_answers:
        problems += '\n' + '    '.join(answers)

    return problems

# Ejemplo de uso de la función
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
