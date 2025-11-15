import random

# CLASE: LoteriaShuffleEuroSueños
# OBJETIVO: Implementar un algoritmo de mezcla aleatoria (Fisher-Yates) utilizando POO.
class LoteriaShuffleEuroSueños:
    
    # Declaración de Constantes (atributos de clase)
    MAX_NUMEROS = 50        # Total de números posibles en el bombo
    TOTAL_A_EXTRAER = 5     # Cantidad de números principales ganadores
    
    # Constructor: Inicializa el estado del objeto
    def __init__(self):
        """
        Inicializa la lista base de números (1 a 50) y la lista de ganadores.
        """
        # Atributos de instancia que almacenan el estado
        self.lista_base = list(range(1, self.MAX_NUMEROS + 1))
        self.ganadores_finales = []
        print(f"Lotería 'Euro Sueños' inicializada. Lista de {len(self.lista_base)} números cargada.")

    # ----------------------------------------------------------------------
    # MÉTODOS PRIVADOS (Simulan funciones locales/auxiliares)
    # ----------------------------------------------------------------------
    
    def __intercambiar(self, indice_a: int, indice_b: int):
        """
        Función auxiliar privada para intercambiar dos elementos en la lista.
        Es la función local de nuestro algoritmo de mezcla (modularidad).
        """
        temp = self.lista_base[indice_a]
        self.lista_base[indice_a] = self.lista_base[indice_b]
        self.lista_base[indice_b] = temp

    def __mezcla_fisher_yates(self):
        """
        Algoritmo de Mezcla Fisher-Yates. Garantiza una permutación aleatoria uniforme.
        """
        n = len(self.lista_base)
        
        # Recorre la lista desde el último elemento hasta el segundo (índice 1)
        for i in range(n - 1, 0, -1):
            # Genera un índice aleatorio 'j' entre 0 y el índice actual 'i'
            j = random.randint(0, i)
            
            # Llama a la función auxiliar para realizar el intercambio
            self.__intercambiar(i, j)
            
        print("Mezcla de números completada con éxito.")

    def __extraer_resultados(self, cantidad: int):
        """
        Extrae los primeros 'cantidad' números de la lista ya mezclada.
        """
        # Los números ya están mezclados, simplemente tomamos los primeros 'cantidad'
        self.ganadores_finales = self.lista_base[:cantidad]
        print(f"Extracción de {len(self.ganadores_finales)} números completada.")
        
    # ----------------------------------------------------------------------
    # MÉTODOS PÚBLICOS (Mecanismos de Abstracción y Salida)
    # ----------------------------------------------------------------------

    def ejecutar_sorteo(self):
        """
        MÉTODO PÚBLICO. Punto de entrada principal (Abstracción). 
        Ejecuta todo el proceso del sorteo en una única llamada.
        """
        # Paso 1: Ejecutar el algoritmo de mezcla
        self.__mezcla_fisher_yates()
        
        # Paso 2: Extraer los ganadores
        self.__extraer_resultados(self.TOTAL_A_EXTRAER)

        # Paso 3: Mostrar el resultado
        self.mostrar_numeros_ganadores()

    def mostrar_numeros_ganadores(self):
        """
        Muestra el resultado final (Salida de Información).
        """
        print("\n-----------------------------------")
        print("NÚMEROS GANADORES OFICIALES:")
        print(self.ganadores_finales)
        print("-----------------------------------")
        
# ----------------------------------------------------------------------
# CÓDIGO DE INICIO Y EJECUCIÓN DEL PROGRAMA
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Instanciación del objeto (Diseño Orientado a Objetos)
    sorteo_hoy = LoteriaShuffleEuroSueños()

    # Ejecución de la lógica del programa
    sorteo_hoy.ejecutar_sorteo()
