import pytest
from bot_precos import BotPrecos


def test_verificar_cambio():
    """Teste para verificar a função de cotação."""
    bot = BotPrecos()
    # Verifica se o bot foi inicializado corretamente
    assert bot is not None
    assert bot.moeda == "USD"
    assert bot.preco_alvo == 5.00
    # Executa a função sem lançar exceção
    bot.verificar_cambio()


def test_enviar_email():
    """Teste para verificar a função de envio de email."""
    bot = BotPrecos()
    assert bot is not None
    # Testa o envio de email com dados válidos
    bot.enviar_email("Teste Moeda", 123.45)


def test_bot_precos_initialization():
    """Teste para verificar a inicialização do bot com parâmetros customizados."""
    bot = BotPrecos(moeda="EUR", preco_alvo=6.50, seu_email="test@gmail.com")
    assert bot.moeda == "EUR"
    assert bot.preco_alvo == 6.50
    assert bot.seu_email == "test@gmail.com"         