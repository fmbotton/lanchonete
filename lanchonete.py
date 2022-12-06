print("Bem Vindo a Lanchonete")
valortotal = float(0) #Cria variável para valor total
continuamenu = str('1') #Cria variável para busca dos itens no menu
print("********************Cardápio********************")
print("| Código | Descrição | Valor |\n| 100 |Cachorro Quente | 9,00 |\n| 101 | Cachorro Quente Duplo | 11,00 |\n| 102 | X-Egg | 12,00 |\n| 103 | X-Salada | 12,00 |\n| 104 | X-Bacon | 14,00 |\n| 105 | X-Tudo | 17,00 |\n| 200 | Refrigerante Lata | 5,00 |\n| 201 | CháGelado | 4,00 |")
while (continuamenu == '1'): #Cria laço de repetição para que o menu nunca se encerre
    escolhamenu = float(input("Entre com o código desejado: ")) #Cria variável e pede entrada do código de produto desejado
    if escolhamenu == 100: #Insere que o cliente escolheu um cachorro-quente
        print("Você pediu um Cachorro-Quente no valor de 9,00")
        valortotal = valortotal+9.00 #Adiciona preço de R$9,00 ao valor total
    elif escolhamenu == 101: #Insere que o cliente escolheu um cachorro-quente duplo
        print("Você pediu um Cachorro-Quente Duplo no valor de 11,00")
        valortotal = valortotal+11 #Adiciona preço de R$11,00 ao valor total
    elif escolhamenu == 102: #Insere que o cliente escolheu um x-egg
        print("Você pediu um X-Egg no valor de 12,00")
        valortotal = valortotal+12 #Adiciona preço de R$12,00 ao valor total
    elif escolhamenu == 103: #Insere que o cliente escolheu um x-salada
        print("Você pediu um X-Salada no valor de 12,00")
        valortotal = valortotal+12 #Adiciona preço de R$12,00 ao valor total
    elif escolhamenu == 104: #Insere que o cliente escolheu um x-bacon
        print("Você pediu um X-Bacon no valor de 14,00")
        valortotal = valortotal+14 #Adiciona preço de R$14,00 ao valor total
    elif escolhamenu == 105: #Insere que o cliente escolheu um x-tudo
        print("Você pediu um X-Tudo no valor de 17,00")
        valortotal = valortotal+17 #Adiciona preço de R$17,00 ao valor total
    elif escolhamenu == 200: #Insere que o cliente escolheu um refrigerante lata
        print("Você pediu um Refrigerante Lata no valor de 5,00")
        valortotal = valortotal+5 #Adiciona preço de R$5,00 ao valor total
    elif escolhamenu == 201: #Insere que o cliente escolheu um chá gelado
        print("Você pediu um Chá Gelado no valor de 4,00")
        valortotal = valortotal+4 #Adiciona preço de R$4,00 ao valor total
    else:
        print("Opção inválida")
        continue
    continuamenu = str(input("Deseja continuar?\n1- Sim\n0 - Nao\n")) #Pergunta se a execução do menu deve continuar
    if continuamenu == '1': #Continua o loop, assim voltando ao inicio do menu
        continue
    elif continuamenu == '0': #Termina o loop do menu, assim encerrando o programa
        break
print("O valor total a ser pago é: {:.2f}" .format(valortotal)) #Printa o valor total do pedido do cliente.
