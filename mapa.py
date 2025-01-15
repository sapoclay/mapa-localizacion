"""
Script para mostrar y buscar ubicaciones en un mapa utilizando Tkinter y TkinterMapView.

Características:
- Muestra una ubicación inicial (Madrid) en el mapa.
- Permite buscar una ubicación basada en coordenadas ingresadas por el usuario.
- Dirección (texto de una ubicación)
- Obtiene y muestra la ubicación real del usuario basada en su dirección IP.

Correcciones realizadas respecto al primer código:
1. **Error en las funciones `buscar_ubicacion` y `mostrar_ubicacion`:**
   - Se corrigió el uso de `map_widget.set_position` y `map_widget.set_marker`, que faltaban en el código original.
   - Ahora se actualiza correctamente la posición y el marcador en el mapa.

2. **Manejo de excepciones en `buscar_ubicacion`:**
   - Se agregó un bloque `try-except` para capturar errores al procesar coordenadas ingresadas por el usuario.
   - Esto previene que el programa se detenga si las coordenadas no tienen el formato esperado.

3. **Implementación de la función `mostrar_ubicacion_real`:**
   - Se agregó esta función para obtener la ubicación actual del usuario utilizando la biblioteca `geocoder`.
   - Muestra un marcador en el mapa con las coordenadas obtenidas y un mensaje informativo.


Dependencias:
- `tkinter`: Librería estándar para crear interfaces gráficas en Python.
- `tkintermapview`: Widget de mapas interactivos basado en Leaflet. Instalable con `pip install tkintermapview`.
- `geocoder`: Biblioteca para obtener datos de geolocalización. Instalable con `pip install geocoder`.

Cómo usar:
1. Ejecuta el script.
2. Usa el botón "Los Madriles" para mostrar la ubicación inicial (Madrid).
3. Escribe coordenadas en el formato latitud,longitud en el cuadro de texto y presiona "Buscar ubicación por coordenadas".
4. Pulsa "Ubicación de mi IP" para mostrar la ubicación actual basada en la dirección IP del dispositivo.

Notas:
- La ubicación obtenida por `geocoder.ip("me")` depende de la IP pública y no es nada precisa.
- Se deben escribir coordenadas válidas en el formato latitud,longitud para evitar errores.
"""

# Importar tkinter
import tkinter as tk
from tkintermapview import TkinterMapView  
from tkinter import messagebox
import geocoder  

# Función para mostrar la ubicación inicial con un marcador
def mostrar_ubicacion():
    """Muestra la ubicación inicial (Madrid) en el mapa con un marcador."""
    latitud, longitud = 40.4168, -3.7038  # Coordenadas iniciales (Madrid)
    map_widget.set_position(latitud, longitud)
    map_widget.set_zoom(15)
    map_widget.set_marker(latitud, longitud, text="Ubicación Actual")
    messagebox.showinfo("Ubicación", "Estás en la calle principal")

# Función para buscar ubicación por coordenadas
def buscar_ubicacion():
    """
    Busca y muestra en el mapa una ubicación basada en coordenadas ingresadas por el usuario.
    
    Formato esperado: latitud,longitud
    Ejemplo: 40.4168,-3.7038
    """
    entrada = entrada_busqueda.get()
    try:
        # Separar latitud y longitud ingresadas por el usuario
        # map() se utiliza para aplicar una función específica a cada elemento de un iterable tuplas, listas...
        # split divide la cadena entrada en una lista de valores utilizando la coma (,) como delimitador.
        latitud, longitud = map(float, entrada.split(",")) 
        map_widget.set_position(latitud, longitud) # Faltaba el set_position
        map_widget.set_marker(latitud, longitud, text="Ubicación Especificada") # Faltaba el set_marker
        messagebox.showinfo("Ubicación encontrada", f"Ubicación encontrada: {latitud}, {longitud}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce coordenadas válidas en el formato: latitud,longitud")

# Función para mostrar la ubicación real del usuario
def mostrar_ubicacion_real():
    """Obtiene la ubicación actual del usuario y la muestra en el mapa."""
    try:
        # Obtener la ubicación actual utilizando geocoder
        ubicacion = geocoder.ip("me")  # Obtiene la ubicación basada en la IP local
        if ubicacion.ok:
            latitud, longitud = ubicacion.latlng
            map_widget.set_position(latitud, longitud)
            map_widget.set_zoom(15)
            map_widget.set_marker(latitud, longitud, text="Mi IP está en....")
            messagebox.showinfo("Ubicación", f"Tu IP se sitúa en: {latitud}, {longitud}")
        else:
            messagebox.showerror("Error", "No se pudo obtener la ubicación real")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener la ubicación: {e}")

# Crear la ventana principal
mapa_ventana = tk.Tk()
mapa_ventana.title("Mapa Genérico de Búsqueda")
mapa_ventana.geometry("800x600")

# Entrada de búsqueda de coordenadas
entrada_busqueda = tk.Entry(mapa_ventana, width=50, font=("Arial", 12))
entrada_busqueda.pack(pady=10)

# Botón para buscar coordenadas
boton_buscar = tk.Button(
    mapa_ventana, 
    text="Buscar ubicación por coordenadas", 
    font=("Arial", 12), 
    command=buscar_ubicacion
)
boton_buscar.pack(pady=10)

# Mapa de Leaflet widget
map_widget = TkinterMapView(mapa_ventana, width=780, height=450, corner_radius=0)
map_widget.pack(pady=10)

# Configurar punto inicial del mapa con coordenadas de Madrid
map_widget.set_position(40.4168, -3.7038)
map_widget.set_zoom(10)

# Botón para mostrar ubicación inicial
boton_ubicacion = tk.Button(
    mapa_ventana, 
    text="Los Madriles", 
    font=("Arial", 12), 
    command=mostrar_ubicacion
)
boton_ubicacion.pack(side="left", padx=5, pady=5)

# Botón para mostrar la ubicación real
boton_ubicacion_real = tk.Button(
    mapa_ventana, 
    text="Ubicación de mi IP", 
    font=("Arial", 12), 
    command=mostrar_ubicacion_real
)
boton_ubicacion_real.pack(side="left", padx=5, pady=5)

# Iniciar el bucle principal
mapa_ventana.mainloop()
