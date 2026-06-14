import requests
import schedule
import time
import smtplib
from email.mime.text import MIMEText

# ============================================
# CONFIGURAÇÕES
# ============================================
SEU_EMAIL = "teu_email@gmail.com"
SENHA_EMAIL = "tua_senha"
EMAIL_DESTINO = "teu_email@gmail.com"
MOEDA = "USD"        # Moeda que queres monitorar
PRECO_ALVO = 5.00   # Te avisa quando dólar chegar a R$ 5,00


# ============================================
# FUNÇÕES
# ============================================
def verificar_cambio():
    """Verifica a cotação atual da moeda."""
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{MOEDA}-BRL"
        response = requests.get(url)
        data = response.json()

        chave = f"{MOEDA}BRL"
        cotacao = float(data[chave]["bid"])
        nome_moeda = data[chave]["name"]

        print(f" {nome_moeda}")
        print(f" Cotação atual: R$ {cotacao:.2f}")
        print(f" Teu alvo: R$ {PRECO_ALVO:.2f}")
        print("-" * 40)

        if cotacao <= PRECO_ALVO:
            print(" Alvo atingido! Enviando email...")
            enviar_email(nome_moeda, cotacao)

    except Exception as e:
        print(f" Erro: {e}")


def enviar_email(moeda, cotacao):
    """Envia email de alerta."""
    try:
        mensagem = MIMEText(
            f" A moeda atingiu o teu preço alvo!\n\n"
            f" Moeda: {moeda}\n"
            f" Cotação atual: R$ {cotacao:.2f}\n"
            f" Teu alvo: R$ {PRECO_ALVO:.2f}\n"
        )
        mensagem["Subject"] = " Alerta de Câmbio!"
        mensagem["From"] = SEU_EMAIL
        mensagem["To"] = EMAIL_DESTINO

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login(SEU_EMAIL, SENHA_EMAIL)
            servidor.sendmail(SEU_EMAIL, EMAIL_DESTINO, mensagem.as_string())
            print(" Email enviado com sucesso!")

    except Exception as e:
        print(f" Erro ao enviar email: {e}")


# ============================================
# AGENDAMENTO
# ============================================
print(" Bot iniciado! Monitorando câmbio...")
print(f" Moeda: {MOEDA}")
print(f" Preço alvo: R$ {PRECO_ALVO:.2f}")
print("-" * 40)

verificar_cambio()

schedule.every(1).hours.do(verificar_cambio)

while True:
    schedule.run_pending()
    time.sleep(60)
