def distancia_binaria(n:int, m:int) -> int:
    '''
    Requiere: n>0, m>0
    Devuelve: la distancia binaria entre n y m como un entero
    '''
    n_bin:str = bin(n).replace('0b','')
    m_bin:str = bin(m).replace('0b', '')
    while len(m_bin) < len(n_bin):
        m_bin = '0' + m_bin
    while len(n_bin) < len(m_bin):
        n_bin = '0' + n_bin
    distancia:int = 0
    i:int = 0
    while i < len(n_bin):
        if n_bin[i] != m_bin[i]:
            distancia += 1
        i += 1
    return distancia


def son_aledaños(n:int, m:int) -> bool:
    '''
    Requiere: n>0, m>0
    Devuelve: True si n y m son vecinos binarios aledaños, False si no lo son
    '''
    return distancia_binaria(n, m) == 1
    

def aledaños_menores(n:int) -> list[int]:
    '''
    Requiere: n>0
    Devuelve: una lista de enteros de los vecinos binarios aledaños a n que son menores que n, ordenados de menor a mayor
    '''
    lista_aledaños_menores:list[int] = list()
    i:int = 1
    while i < n:
        if son_aledaños(n, i):
            lista_aledaños_menores.append(i)
        i += 1
    return lista_aledaños_menores


def cant_aledaños(n:int, a:int, b:int) -> int:
    '''
    Requiere: n>0, a>0, b>0, a<b
    Devuelve: un entero con la cantidad de números en el intervalo [a,b] que son vecinos aledaños a n
    '''
    res:int = 0
    i:int = a
    while i <= b:
        if son_aledaños(n, i):
            res +=1
        i += 1
    return res


def densidad_intervalo(n:int, a:int, b:int) -> float:
    '''
    Requiere: n>0, a>0, b>0, a<b
    Devuelve: la densidad binaria de n en el intervalo [a, b], como un punto flotante, con un error menor a 10^(-5)
    '''
    cant_naturales:int = b - a + 1
    aledaños:int = 0
    i:int = a
    while i <= b:
        if son_aledaños(i, n):
            aledaños += 1
        i += 1
    res:float = aledaños/cant_naturales
    #Nota: Como el intervalo incluye los extremos, no habrá división por cero, ya que la variable cant_naturales siempre será mayor o igual a 1.
    return round(res, 5)