def pullback_signal(prices, threshold=0.0005):
    """Detecta pullback simples"""
    if len(prices) < 3:
        return None
    if prices[-2] < prices[-3] and prices[-1] > prices[-2] and (prices[-1] - prices[-2]) > threshold:
        return 'CALL'
    elif prices[-2] > prices[-3] and prices[-1] < prices[-2] and (prices[-2] - prices[-1]) > threshold:
        return 'PUT'
    else:
        return None
