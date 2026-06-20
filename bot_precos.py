import requests
import schedule
import time
import smtplib
from email.mime.text import MIMEText


class BotPrecos:
    """Bot para monitorar cotação de moedas e enviar alertas por email."""
    
    def __init__(self, moeda="USD", preco_alvo=5.00, seu_email="teu_email@gmail.com", 
                 senha_email="tua_senha", email_destino="teu_email@gmail.com"):
        """
        Inicializa o bot com as configurações.
        
        Args:
            moeda: Moeda a monitorar (padrão: USD)
            preco_alvo: Preço alvo para alerta (padrão: 5.00)
            seu_email: Email de origem para enviar alertas
            senha_email: Senha do email
            email_destino: Email de destino para alertas
        """
        self.moeda = moeda
        self.preco_alvo = preco_alvo
        self.seu_email = seu_email
        self.senha_email = senha_email
        self.email_destino = email_destino

    def verificar_cambio(self):
        """Verifica a cotação atual da moeda."""
        try:
            url = f"https://economia.awesomeapi.com.br/json/last/{self.moeda}-BRL"
            response = requests.get(url, timeout=5)
            data = response.json()

            chave = f"{self.moeda}BRL"
            cotacao = float(data[chave]["bid"])
            nome_moeda = data[chave]["name"]

            print(f" {nome_moeda}")
            print(f" Cotação atual: R$ {cotacao:.2f}")
            print(f" Teu alvo: R$ {self.preco_alvo:.2f}")
            print("-" * 40)

            if cotacao <= self.preco_alvo:
                print(" Alvo atingido! Enviando email...")
                self.enviar_email(nome_moeda, cotacao)

        except Exception as e:
            print(f" Erro: {e}")

    def enviar_email(self, moeda, cotacao):
        """Envia email de alerta."""
        try:
            mensagem = MIMEText(
                f" A moeda atingiu o teu preço alvo!\n\n"
                f" Moeda: {moeda}\n"
                f" Cotação atual: R$ {cotacao:.2f}\n"
                f" Teu alvo: R$ {self.preco_alvo:.2f}\n"
            )
            mensagem["Subject"] = " Alerta de Câmbio!"
            mensagem["From"] = self.seu_email
            mensagem["To"] = self.email_destino

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
                servidor.login(self.seu_email, self.senha_email)
                servidor.sendmail(self.seu_email, self.email_destino, mensagem.as_string())
                print(" Email enviado com sucesso!")

        except Exception as e:
            print(f" Erro ao enviar email: {e}")

    def iniciar_monitoramento(self):
        """Inicia o monitoramento contínuo da moeda."""
        print(" Bot iniciado! Monitorando câmbio...")
        print(f" Moeda: {self.moeda}")
        print(f" Preço alvo: R$ {self.preco_alvo:.2f}")
        print("-" * 40)

        self.verificar_cambio()
        schedule.every(1).hours.do(self.verificar_cambio)

        while True:
            schedule.run_pending()
            time.sleep(60)


if __name__ == "__main__":
    # ============================================
    # CONFIGURAÇÕES
    # ============================================
    SEU_EMAIL = "teu_email@gmail.com"
    SENHA_EMAIL = "tua_senha"
    EMAIL_DESTINO = "teu_email@gmail.com"
    MOEDA = "USD"        # Moeda que queres monitorar
    PRECO_ALVO = 5.00   # Te avisa quando dólar chegar a R$ 5,00

    bot = BotPrecos(moeda=MOEDA, preco_alvo=PRECO_ALVO, seu_email=SEU_EMAIL,
                    senha_email=SENHA_EMAIL, email_destino=EMAIL_DESTINO)
    bot.iniciar_monitoramento()
