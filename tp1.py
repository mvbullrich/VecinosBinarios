from distancia_binaria import distancia_binaria, son_aledaños, \
                   aledaños_menores, cant_aledaños, densidad_intervalo

def elegir_funcion() -> str:
    '''
    Despliega el menú de funciones disponibles en la pantalla y devuelve
    la opción elegida por el usuario según la siguiente codificación:
        A -> Distancia binaria;
        B -> Son vecinos binarios aledaños;
        C -> Lista vecinos binarios aledaños menores;
        D -> Cantidad de aledaños en intervalo;
        E -> Densidad binaria;
        F -> Finalizar;
    Requiere: Nada.
    Devuelve: La opción elegida por el usuario, en mayúscula y sin espacios adelante y atrás.
    '''
    print()
    print('Funciones disponibles')
    print('---------------------')
    print('A. Distancia binaria [n,m]')
    print('B. Son vecinos binarios aledaños [n,m]')
    print('C. Lista vecinos binarios aledaños menores [n]')
    print('D. Cantidad de aledaños en intervalo [n,a,b]')
    print('E. Densidad binaria [n,a,b]')
    print('F. Finalizar')
    opción_elegida:str = input('Seleccione una opción: ').upper().strip()
    return opción_elegida


# Cuerpo principal del programa
finalizar:bool = False
while not finalizar:
    opcion_seleccionada:str = elegir_funcion()

    # Se analiza la opción elegida
    if opcion_seleccionada == 'A':
        n_str:str = input('Ingrese n: ')
        m_str:str = input('Ingrese m: ')
        print(f'La distancia binaria entre {n_str} y {m_str} es {distancia_binaria(int(n_str), int(m_str))}')

    elif opcion_seleccionada == 'B':
        n_str:str = input('Ingrese n: ')
        m_str:str = input('Ingrese m: ')
        if son_aledaños(int(n_str), int(m_str)):
            print(f'Los números {n_str} y {m_str} son vecinos binarios aledaños')
        else:
            print(f'Los números {n_str} y {m_str} no son vecinos binarios aledaños')

    elif opcion_seleccionada == 'C':
        n_str: str = input('Ingrese n: ')
        lista_aledaños_menores:list[int] = aledaños_menores(int(n_str))
        if not lista_aledaños_menores:
            print(f'El número {n_str} no tiene vecinos aledaños menores.')
        else:
            i: int = 0
            mensaje: str = 'Los números '
            while i < len(lista_aledaños_menores):
                if i == len(lista_aledaños_menores) - 1:
                    mensaje += f' y {lista_aledaños_menores[i]}'
                elif i == len(lista_aledaños_menores) - 2:
                    mensaje += f' {lista_aledaños_menores[i]}'
                else:
                    mensaje += f' {lista_aledaños_menores[i]},'
                i += 1
            mensaje += f' son los vecinos aledaños a {n_str} menores a {n_str}'
            print(mensaje)

    elif opcion_seleccionada == 'D':
        n_str:str = input('Ingrese n: ')
        a_str:str = input('Ingrese a: ')
        b_str:str = input('Ingrese b: ')
        print(f'{cant_aledaños(int(n_str), int(a_str), int(b_str))} números en [{a_str}, {b_str}] son aledaños a {n_str}')

    elif opcion_seleccionada == 'E':
        n_str:str = input('Ingrese n: ')
        a_str:str = input('Ingrese a: ')
        b_str:str = input('Ingrese b: ')
        print(f'La densidad binaria de {n_str} en [{a_str}, {b_str}] es aproximadamente {densidad_intervalo(int(n_str), int(a_str), int(b_str))}')
    
    elif opcion_seleccionada == 'F':
        finalizar = True

    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'F':
        input('Presione ENTER para continuar.')
