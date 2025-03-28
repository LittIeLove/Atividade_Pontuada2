import os
os.system ("clear || cls")
from time import sleep
valor = 0
valorf = 0
pratos = []
while True:

    print("""
        Codigo |            Prato                |Valor
        1      | Lasanha                         | 40,00                        
        2      | Strogonoff                      | 35,00
        3      | Churrasco                       | 30,00
        4      | Feijoada                        | 30,00
        5      | Aimpim frito                    | 15,00
        6      | Batata frita                    | 15,00
        7      | Macarrão ao molho branco        | 35,00
                Digite (0) Para finalizar.
        """)
    codigo = str(input("Digite o codigo do prato: "))
    match codigo:
        case "1":
            prato = "1-Lasanha"
            valor = 40
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
            break
        case "2":
            prato = "2-Strogonoff"
            valor = 35
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
            break
        case "3":
            prato = "3-Churrasco"
            valor = 30
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
            break
        case "4":
            prato = "4-Feijoada"
            valor = 30
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
            break
        case "5":
            prato = "5-Aimpim_frito"
            valor = 15
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
            break
        case "6":
            prato = "6-Batata_frita"
            valor = 15
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
            break
        case "7":
            prato = "7-Macarrão_ao_molho_branco"
            valor = 35
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
            break
        case "0":
            print("Não existe pedidos.")
            sleep(1)
            os.system ("clear || cls")
            exit()
        case _:
            print("Codigo invalido.\nDigite o código novamente.")
            sleep(1)
            os.system ("clear || cls")
            
novamente = str(input("Deseja adicionar mais pratos? (s/n)")).lower()



while novamente == "s":
    os.system ("clear || cls")
    print("""
    Codigo |            Prato                |Valor
    1      | Lasanha                         | 40,00                        
    2      | Strogonoff                      | 35,00
    3      | Churrasco                       | 30,00
    4      | Feijoada                        | 30,00
    5      | Aimpim frito                    | 15,00
    6      | Batata frita                    | 15,00
    7      | Macarrão ao molho branco        | 35,00
               Digite (0) Para finalizar.
    """)

    codigo = str(input("Digite o codigo do prato: "))
    match codigo:
        case "1":
            prato = "1-Lasanha"
            valor = 40
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
        case "2":
            prato = "2-Strogonoff"
            valor = 35
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
        case "3":
            prato = "3-Churrasco"
            valor = 30
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)   
        case "4":
            prato = "4-Feijoada"
            valor = 30
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
        case "5":
            prato = "5-Aimpim_frito"
            valor = 15
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
        case "6":
            prato = "6-Batata_frita"
            valor = 15
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
        case "7":
            prato = "7-Macarrão_ao_molho_branco"
            valor = 35
            valorf += valor
            pratos.append(prato)
            print("Adicionado")
            sleep (1)
        case "0":
            print("Escolher forma de pagamento.")
            sleep(1)
            os.system ("clear || cls")
            break
        case _:
            print("Codigo invalido.\nDigite o código novamente.")
            sleep(1)


while True:
    os.system ("clear || cls")
    print("""
Codigo| Método  | info
1     | À vista | Desconto de 10%
2     | Crédito | Acréscimo
""")
    metodo = str(input("Digite o codigo de pagamento."))
    match metodo:
        case "1":
            desconto = valorf * 0.1
            valorfinal = valorf - desconto
            forma = "Á vista"
            print("Obrigado por fazer o pedido conosco!\nIndo para o resultado.")
            sleep(1)
            os.system ("clear || cls")
            print("Pedidos:")
            print (pratos)
            print(f"\nValor bruto = {valorf}\nMetódo ({forma})\nDesconto ({desconto})\nValor final ({valorfinal})")
            break
    
        case "2":
            desconto = valorf * 0.1
            valorfinal = valorf + desconto
            forma = "Crédito"
            print("Obrigado por fazer o pedido conosco!\nIndo para o resultado.")
            sleep(1)
            os.system ("clear || cls")
            print("Pedidos:")
            print (pratos)
            print(f"\nValor bruto = {valorf}\nMetódo ({forma})\nAcrescimo ({desconto})\nValor final ({valorfinal})")
            break
        case _:
            print("Opcão invalida.\nDigite novamente")
            sleep(1)


    


    


