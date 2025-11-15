import networkx as nx

# --- VARIABLES/CONSTANTES (Simulación de Datos Cuantitativos y Cualitativos) ---
UMBRAL_RETRASO_ALARMA = 15  # Minutos (Dato Cuantitativo: Umbral de alerta)
RENDIMIENTO_ANTERIOR_PORCENTAJE = 70 # % (Tasa de puntualidad histórica simulada)
RENDIMIENTO_ESPERADO_PORCENTAJE = 95 # % (Tasa de puntualidad objetivo simulada)

# Simula la entrada de datos de retrasos para cada tren
DICT_RETRASOS = {
    "TR001": 5,
    "TR002": 0,    # Este tren está configurado para generar una excepción
    "TR003": 20,
    "TP101": 10
}

# Datos Cualitativos (obtenidos de entrevistas simuladas)
DESAFIO_PERCIBIDO = "Coordinar horarios de manera efectiva y gestionar la congestión."
BENEFICIO_PERCIBIDO = "Monitoreo en tiempo real y ajuste dinámico de horarios."


# --- CLASE GRAFO (Diseño Orientado a Objetos - Anexo) ---
class Grafo:
    """Clase base para representar un grafo dirigido de la red ferroviaria,
    utilizando networkx para modelar rutas y distancias entre estaciones.
    """

    def __init__(self):
        self.grafo = nx.DiGraph()
        self.nodos_tren = {} # Almacena la ubicación actual de los trenes

    def agregar_arista(self, nodo1, nodo2, peso):
        """Añade una arista (ruta) entre dos nodos (estaciones) con un peso (distancia/tiempo).
        
        Args:
            nodo1 (str): Estación de origen.
            nodo2 (str): Estación de destino.
            peso (int): Peso de la arista.
        """
        self.grafo.add_edge(nodo1, nodo2, weight=peso)


# --- CLASE TREN (Diseño Orientado a Objetos - Clase Base) ---
class Tren:
    """Clase base para representar un tren de la flota (OOD)."""

    def __init__(self, id_tren, ruta_actual, prioridad=False):
        self.id = id_tren
        self.ruta_actual = ruta_actual
        self.estado = "En Estación"
        self.retraso_min = 0
        self.prioridad = prioridad

    def actualizar_estado(self, nuevo_estado):
        """Método para cambiar el estado del tren."""
        self.estado = nuevo_estado
        print(f"Tren {self.id} -> Estado actualizado a: {self.estado}")

    def aplicar_retraso(self, minutos):
        """
        Registra un retraso y usa Sentencia Condicional para la toma de decisiones (Pregunta 1).
        """
        self.retraso_min += minutos
        
        if self.retraso_min > UMBRAL_RETRASO_ALARMA:
            # Lógica para notificar a la siguiente estación o rerutear
            print(f"!!! ALERTA: Tren {self.id} ha superado el umbral de retraso ({self.retraso_min} min).")
        else:
            print(f"Tren {self.id} tiene un retraso de {self.retraso_min} minutos.")

# --- CLASE TRENDEPASAJEROS (Diseño Orientado a Objetos - Herencia) ---
class TrenDePasajeros(Tren):
    """Subclase que hereda de Tren, demostrando la escalabilidad del OOD (Pregunta 3)."""
    
    def __init__(self, id_tren, ruta_actual, capacidad, prioridad=False):
        # Llama al constructor de la clase base (Tren)
        super().__init__(id_tren, ruta_actual, prioridad)
        self.capacidad = capacidad
        self.reservas = [] # Estructura de datos: Lista para reservas

    def generar_lista_embarque(self):
        """Usa bucles para automatizar la revisión de pasajeros (Pregunta 2)."""
        print(f"\n--- Detalle Tren de Pasajeros {self.id} ---")
        if not self.reservas:
            print("No hay reservas cargadas para simular.")
            return

        # Bucle For
        for i, pasajero in enumerate(self.reservas, 1):
            print(f"  {i}. {pasajero} - Verificado.")
        print(f"Lista de embarque generada para {len(self.reservas)} pasajeros.")


# --- CLASE GESTOR HORARIOS (Estructura Común: Listas y Bucles) ---
class GestorHorarios:
    """Clase para gestionar el conjunto de trenes y horarios."""

    def __init__(self, red_ferroviaria, flota_trenes):
        self.red = red_ferroviaria 
        self.flota = flota_trenes    # Estructura de datos: Lista de objetos Tren/Subclases

    def simular_operacion(self):
        """
        Simula la operación diaria. Usa un Bucle for para el monitoreo masivo (Pregunta 2).
        """
        print("\n--- SIMULACIÓN DE OPERACIÓN DIARIA ---")
        
        for tren in self.flota:
            
            if tren.estado == "En Ruta":
                retraso_simulado = DICT_RETRASOS.get(tren.id, 0)
                
                # Manejo de Errores (Pregunta 4)
                try:
                    self._verificar_incidente(tren, retraso_simulado)
                except Exception as e:
                    # Captura el error y ejecuta una rutina de contingencia
                    print(f"ERROR CRÍTICO manejado en Tren {tren.id}: {e}")
                    print("--> Ejecutando protocolo de seguridad: Detención inmediata.")
                    tren.actualizar_estado("Detenido por Falla")
            else:
                print(f"Tren {tren.id} está en {tren.estado}. No requiere acción inmediata.")

    def _verificar_incidente(self, tren, retraso):
        """Lógica para aplicar retrasos y verificar incidentes."""
        
        # Simulación de Incidente de Vía para demostrar el try/except
        if tren.id == "TR002":
            raise ValueError("Incidente de vía en la ruta del Tren TR002. Fallo en el sensor de tramo.")
        
        if retraso > 0:
            tren.aplicar_retraso(retraso)

    def mostrar_rendimiento_global(self):
        """Muestra datos cuantitativos y cualitativos simulados (Pregunta 3)."""
        print("\n--- RENDIMIENTO Y ANÁLISIS GLOBAL ---")
        trenes_con_retraso = sum(1 for t in self.flota if t.retraso_min > 0)
        
        # Datos Cuantitativos
        print(f"Trenes analizados: {len(self.flota)}")
        print(f"Trenes con algún retraso: {trenes_con_retraso}")
        print(f"Rendimiento anterior (simulado): {RENDIMIENTO_ANTERIOR_PORCENTAJE}%")
        print(f"Rendimiento esperado (simulado): {RENDIMIENTO_ESPERADO_PORCENTAJE}%")

        # Datos Cualitativos
        print(f"\nFeedback de Desarrolladores (Dato Cualitativo):")
        print(f"Desafío Percibido: {DESAFIO_PERCIBIDO}")
        print(f"Beneficio Percibido: {BENEFICIO_PERCIBIDO}")
        print("El diseño de Clases (OOD) mejoró la mantenibilidad y escalabilidad del código.")


# --- FUNCIÓN PRINCIPAL DE EJECUCIÓN (main) ---
if __name__ == "__main__":
    
    # 1. Inicialización de la Red Ferroviaria (Grafo)
    print(">>> INICIALIZANDO RED FERROVIARIA")
    red_ferroviaria = Grafo()
    red_ferroviaria.agregar_arista("A", "B", 1) # Arista A-B
    red_ferroviaria.agregar_arista("B", "C", 2) # Arista B-C
    red_ferroviaria.agregar_arista("A", "C", 4) # Arista A-C

    # 2. Inicialización de la Flota de Trenes (Objetos y Subclase)
    print("\n>>> CREANDO FLOTA DE TRENES")
    trenes = [
        Tren("TR001", "A-B", prioridad=True),
        Tren("TR002", "B-C", prioridad=False),
        Tren("TR003", "A-C", prioridad=False),
        TrenDePasajeros("TP101", "C-A", capacidad=500, prioridad=True) # Uso de la subclase
    ]
    
    # Agregar datos simulados para el Tren de Pasajeros
    trenes[3].reservas = ["Juan Perez", "Maria Gomez", "Carlos Ruiz"]

    # 3. Simulación de Operación y Actualización de Estados
    print("\n>>> ACTUALIZANDO ESTADOS INICIALES")
    for t in trenes:
        t.actualizar_estado("En Ruta")

    # 4. Uso del Gestor de Horarios
    gestor = GestorHorarios(red_ferroviaria, trenes)
    gestor.simular_operacion()
    
    # Lógica específica de la subclase
    trenes[3].generar_lista_embarque()
    
    gestor.mostrar_rendimiento_global()
