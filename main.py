import os
import webbrowser
import urllib.request

print('Olá senhor. Sou o Jarvis. Estou aqui. Controlo tudo o que o senhor precisa')
entrada = input("O que posso fazer pelo senhor?  ")

if(entrada == "desligar"):
    print('Desligando seu computador...')
    os.system("shutdown /s /t 1")
elif(entrada == "reiniciar"):
    print('Reiniciando seu computador...')
    os.system("shutdown /r /t 1")
elif(entrada == "verificar site de arquitetura"):
    print('Verificando site da Agá Empreendimentos...')
    if(urllib.request.urlopen("https://agaempreendimentos.com.br").getcode() == 200):
        print('Site funcionando perfeitamente, senhor')
elif(entrada == "deixe comigo"):
    print('Estarei aqui se precisar...')
    exit()
elif(entrada == "calculadora"):
    operacao = input('Soma, multiplicação, subtração ou divisão? ')

    numero1 = input('Digite o primeiro número  ')
    numero2 = input('Digite o segundo número   ')

    if(operacao == "soma"):
        resultado = int(numero1) + int(numero2)
    elif (operacao == "subtração"):
        resultado = int(numero1) - int(numero2)
    elif (operacao == "multiplicação"):
        resultado = int(numero1) * int(numero2)
    elif (operacao == "divisão"):
        resultado = int(numero1) / int(numero2)
    else:
        resultado = "Operação não suportada"

    print('O resultado da operação é ', str(resultado))
elif(entrada == "baixar vídeos do youtube"):
    url = input('Perfeito, qual é a url do vídeo? ')
    url = url[:12] + "ss" + url[12:]
    webbrowser.open(url)
    print('Pronto, senhor.')
else:
    print('Não entendi esse comando senhor...')

input()



