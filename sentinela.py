import socket

# Configuração do servidor
IP_LOCAL = "0.0.0.0" # Ouve em todas as interfaces
PORTO = 5000         # Porto alto (não precisa de root)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP_LOCAL, PORTO))
server.listen(5)

print(f"[*] Sentinela ativa no porto {PORTO}. À espera de conexões...")

contagem_mensagens = {}

while True:
    client, addr = server.accept()
    ip_cliente = addr[0]
    
    # Simulação de Lógica de IA:
    # No dataset, 'count' (frequência) era uma feature crucial.
    contagem_mensagens[ip_cliente] = contagem_mensagens.get(ip_cliente, 0) + 1
    
    if contagem_mensagens[ip_cliente] > 10:
        print(f"[ALERTA IA] Bloqueio Simulado: {ip_cliente} excedeu o limite de segurança!")
        client.send(b"ACESSO BLOQUEADO PELA IA\n")
        client.close()
    else:
        mensagem = client.recv(1024).decode()
        print(f"[LOG] Mensagem de {ip_cliente}: {mensagem}")
        client.send(b"Mensagem recebida com sucesso.\n")
        client.close()
