def puntos_porcentaje(valor_real: int, valor_predicho: int, p_suma: int = 0.8, p_resta: int = 0.2) -> float:
    '''
    Función que dado el valor real del porcentaje y el valor predicho calcula
    la puntuación final.
    p_suma y p_resta serán los pesos de ,respectivamente, acercarse al valor 
    real (esto solo suma puntos) y de pasarse del valor real (esto puede
    restar puntos). Quedarse por debajo del valor real nunca resta puntos.
    La puntuación máxima obtenible son 50 puntos.
    La puntuación mínima obtenible son -infinito puntos.
    
    Parameters
    ----------
    valor_real: el valor del porcentaje real
    
    valor_predicho: el valor del porcentaje predicho
    
    p_suma: el peso de acercarse al valor real. Por defecto será 0.8
    
    p_resta: el peso de pasarse o no del valor real. Por defecto será 0.2
    
    Precondition
    ------------
    p_suma + p_resta == 1
    0 <= p_suma <= 1
    0 <= p_resta <= 1
    0 <= valor_real <= 100
    0 <= valor_predicho <= 100
    
    Returns
    -------
    La puntuación
    
    Example
    -------
    >>> puntos_porcentaje(40, 60)
    53
    '''
    
    parte_positiva = (abs(valor_real - valor_predicho)/valor_real) * p_suma
    parte_negativa = ((valor_real - valor_predicho)/valor_real) * p_resta
    
    return 50*(1 - parte_positiva + parte_negativa)
