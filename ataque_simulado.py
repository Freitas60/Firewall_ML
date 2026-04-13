import socket
import time

# Substitui pelo IP do computador do teu colega
IP_DESTINO = "192.168.x.x" 
PORTO = 5000

def enviar_mensagem(texto):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP_DESTINO, PORTO))
        s.send(texto.encode())
        resposta = s.recv(1024)
        print(f"Resposta do Servidor: {resposta.decode()}")
        s.close()
    except:
        print("Erro: Servidor não alcançável ou conexão recusada.")

# 1. Teste de Tráfego Normal
print("--- Enviando tráfego legítimo ---")
enviar_mensagem("Olá, sou um utilizador normal.")

# 2. Simulação de Ataque (Inundação)
print("\n--- A iniciar simulação de ataque DoS ---")
for i in range(15):
    print(f"Tentativa {i+1}...")
    enviar_mensagem("ATAQUE!!!")
    time.sleep(0.1)
