from math import floor

def puntos_minutos(valor_real: int, valor_predicho: int) -> int:
    '''
    Función que dada la cantidad de minutos escuchados 
    predicha y la cantidad real, devuelve la cantidad de puntos obtenidos por
    el usuario.
    
    Parameters
    ----------
    valor_real: el valor real
    
    valor_predicho: el valor predicho
    
    Precondition
    ------------
    -
    
    Returns
    -------
    La puntuación
    
    Example
    -------
    '''
    x = 10 - (abs(valor_real - valor_predicho)/valor_real)*10
    if x!=0:
        x = floor(x) + 1
        
    if valor_real == valor_predicho:
        x+=2
        
    return int(x)
