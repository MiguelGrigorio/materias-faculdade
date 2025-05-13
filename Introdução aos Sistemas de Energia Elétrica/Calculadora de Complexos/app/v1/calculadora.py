from typeNumbers import Graus, Radianos, Polar, Complexo
import time
import os

ang = None
def inicio():
    global ang
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal
    print("---- Calculadora de números complexos ----")
    ang = input("Deseja utilizar radianos ou graus? (R/G): ").upper()
    
    if ang not in ["R", "G"]:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
        inicio()

    print("Caso queira um número polar, digite P(r, theta)")
    print("Caso queira um número retangular, digite X + Yj")
    menu()

ans = None
values = []
index = 0
exp = ""

def menu():
    global index, exp, ans
    text = [f"- Digite o primeiro número complexo{"" if not ans else f" ou ans ({ans.print(ang)})"}:" , "- Digite a operação: ", "- Digite o segundo número complexo: "]
    
    while index != len(text):
        if values:
            print(exp)
        value = input(text[index])
        if value == "ans":
            if not ans:
                print("Nenhum valor armazenado.")
                time.sleep(1)
                menu()
            values.append(ans)
            index += 1
            exp += ans.print(ang) + " "
        elif index != 1:
            try:
                if value[0] == "P":
                    num = value[2:-1].split(",")
                    num = Polar(float(num[0]), Graus(float(num[1])) if ang == "G" else Radianos(float(num[1])))
                else:
                    num = complex(value.replace(" ", "").replace("i", "j"))
                v = Complexo(num)
                values.append(v)
                index += 1
                exp += v.print(ang) + " "
            except:
                print("Entrada inválida.")
                time.sleep(1)
                menu()
        elif value in ["+", "-", "*", "/"] and index == 1:
            values.append(value)
            index += 1
            exp += value + " "
        else:
            print("Entrada inválida.")
            time.sleep(1)
            menu()
    
    V1 = values[0]
    V2 = values[2]
    match values[1]:
        case "+":
            ans = V1 + V2
        case "-":
            ans = V1 - V2
        case "*":
            ans = V1 * V2
        case "/":
            ans = V1 / V2
    
    print(f"{exp + "= " + ans.print(ang)}")
    index = 0
    exp = ""
    values.clear()
    reset = input("Reiniciar ou continuar? (R/C): ").upper()
    if reset == "R":
        ans = None
        inicio()
    else:
        os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal
        menu()

try:
    inicio()
except KeyboardInterrupt:
    print("\nPrograma encerrado.")