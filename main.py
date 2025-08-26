import threading
import time
import random
from strategies import pullback_signal

# Histórico de preços e último sinal
price_history = []
last_signal = None

def simulate_ticks():
    """Simula ticks de preço e gera sinais CALL/PUT"""
    global last_signal
    price = 1.1300  # Preço inicial
    while True:
        price += random.uniform(-0.0005, 0.0005)  # Pequena variação
        price_history.append(price)
        if len(price_history) > 20:
            price_history.pop(0)
        signal = pullback_signal(price_history)
        if signal:
            last_signal = signal
            print(f"[Simulação] Sinal {signal} detectado em {price:.5f}")
        time.sleep(1)

# Inicia simulação em thread
threading.Thread(target=simulate_ticks).start()
