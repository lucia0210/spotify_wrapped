def puntos_tops(valor_real: list[bool], cantidad) -> int:
    '''
    Función que dada la lista con los booleanos que indican, en orden 
    respectivo, si se ha acertado el orden en un top, y la cantidad de 
    elementos predicha que sí están presentes en el top, devuelve la cantidad 
    de puntos obtenidos.
    
    Parameters
    ----------
    valor_real: la lista con los valores. Será del tipo
                [True, False, False, True, True]
    
    Precondition
    ------------
    len(valor_real) == 5
    valores_reales.count(True) <= cantidad
    
    Returns
    -------
    La puntuación
    
    Example
    -------
    >>> puntos_tops([True, True, False, True, False], 4)
    53
    '''
    x = 0
    
    x+= 10*cantidad
    
    x+= valor_real[0]*5
    x+= valor_real[1]*5
    x+= valor_real[2]*3
    x+= valor_real[3]*3
    x+= valor_real[4]*3
    
    return x
