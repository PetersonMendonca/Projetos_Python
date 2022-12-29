import socket

# Retorno do ip no qual o python esta rodando
print('IP rodando pelo Python: {}'.format(socket.gethostbyname(socket.gethostname())))

print('*'*50)

# Retorna o IP da maquina e a Porta de Acesso
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
print('IP Maquina: {} - Porta Acesso: {}'.format(s.getsockname()[0],s.getsockname()[1]))

print('*'*50)

# Retorna o IP da maquina e a Porta de Acesso mesmo sem acesso a internet
def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP
print(extract_ip())