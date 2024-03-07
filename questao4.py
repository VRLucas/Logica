import time

def descobrir_interruptores():
    # Ligar o primeiro interruptor
    print("Ligando o primeiro interruptor...")
    time.sleep(2)  # Simula o tempo que deixamos o interruptor ligado
    print("Desligando o primeiro interruptor...")

    # Ligar o segundo interruptor e entrar na sala
    print("Ligando o segundo interruptor e entrando na sala...")
    time.sleep(1)  # Simula o tempo de entrar na sala

    # Verificar o estado das lâmpadas
    lâmpada_1 = "acesa"
    lâmpada_2 = "quente"
    lâmpada_3 = "apagada e fria"

    # Determinar qual interruptor controla cada lâmpada
    if lâmpada_1 == "acesa":
        print("O primeiro interruptor controla a lâmpada 1.")
    if lâmpada_2 == "quente":
        print("O segundo interruptor controla a lâmpada 2.")
    if lâmpada_3 == "apagada e fria":
        print("O terceiro interruptor controla a lâmpada 3.")

descobrir_interruptores()
