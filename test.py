from bot_precos import BotPrecos


def test_verificar_cambio():
    """Teste para verificar a função de cotação."""
    bot = BotPrecos()
    try:
        bot.verificar_cambio()
        print("Teste de verificação de câmbio: SUCESSO")
    except Exception as e:
        print(f"Teste de verificação de câmbio: FALHA - {e}")


def test_enviar_email():
    """Teste para verificar a função de envio de email."""
    bot = BotPrecos()
    try:
        bot.enviar_email("Teste Moeda", 123.45)
        print("Teste de envio de email: SUCESSO")
    except Exception as e:
        print(f"Teste de envio de email: FALHA - {e}")


def test_run_tests():
    """Executa todos os testes."""
    test_verificar_cambio()
    test_enviar_email()


if __name__ == "__main__":
    test_run_tests()         