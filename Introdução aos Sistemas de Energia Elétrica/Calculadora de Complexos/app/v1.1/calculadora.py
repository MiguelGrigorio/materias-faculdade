from typeNumbers import Graus, Radianos, Polar, Complexo
import sympy
import time
import os
import re

ang = None
def inicio():
    global ang
    clear()
    print("---- Calculadora de números complexos ----")
    ang = input("Deseja utilizar radianos ou graus? (R/G): ").upper()
    
    if ang not in ["R", "G"]:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
        inicio()

    print("Caso queira um número polar, digite P(r, theta)")
    print("Caso queira um número retangular, digite X + Yj")
    menu()

values = []

def clear():
    global values
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal
    if values:
        print(f"Resultados anteriores: {', '.join([val for val in values])}")
        print(f"{'-'*os.get_terminal_size().columns}")
    
                 
def obter_valores(expressao, variaveis):
    global ang
    exp = expressao
    valores = {}
    for var in variaveis:
        while True:
            sympy.pprint(sympy.sympify(exp, evaluate=False))
            try:
                number = input(f"Digite o valor de {var}: ")
                if number[0] == "P":
                    num = number[2:-1].split(",")
                    num = Polar(float(num[0]), Graus(float(num[1])) if ang == "G" else Radianos(float(num[1])))
                else:
                    num = complex(number.replace(" ", "").replace("i", "j"))
                valores[var] = Complexo(num)
                exp = exp.replace(var, f"({valores[var].sympy()})")
                clear()
                break
            except Exception as e:
                print("Entrada inválida.", e)
                time.sleep(1)
    sympy.pprint(sympy.sympify(exp, evaluate=False))
    return valores

def calcular_expressao(expressao, valores):
    contexto = {var: val for var, val in valores.items()}
    try:
        resultado = eval(expressao, {"__builtins__": {}}, contexto)
        return resultado
    except Exception as e:
        return f"Erro ao calcular a expressão: {e}"

def menu():
    expressao = input("Digite a expressão matemática usando variáveis (ex: (N1+N2)/N3): ")
    variaveis = sorted(set(re.findall(r'\b[A-Za-z]\w*\b', expressao)))
    if not variaveis:
        print("Nenhuma variável encontrada na expressão. Tente novamente.")
        return
    
    valores = obter_valores(expressao, variaveis)
    resultado = calcular_expressao(expressao, valores)

    print(f"Resultado: {resultado.print(ang)}")
    reset = input("Reiniciar ou continuar? (R/C): ").upper()
    if reset == "R":
        values.clear()
        inicio()
    else:
        values.append(resultado.print(ang))
        if len(values) > 5:
            values.pop(0)
        clear()
        menu()

try:
    inicio()
except KeyboardInterrupt:
    print("\nPrograma encerrado.")