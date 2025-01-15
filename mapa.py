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

def mostrar_ubicacion():
    """Muestra la ubicación inicial (Madrid) en el mapa con un marcador."""
    latitud, longitud = 40.4168, -3.7038  # Coordenadas iniciales (Madrid)
    map_widget.set_position(latitud, longitud)  # Establece la posición inicial del mapa con las coordenadas de Madrid.
    map_widget.set_zoom(15)  # Configura el zoom del mapa a nivel 15 (detallado).
    map_widget.set_marker(latitud, longitud, text="Ubicación Actual")  # Coloca un marcador en Madrid con un texto explicativo.
    messagebox.showinfo("Ubicación", "Estás en la calle principal")  # Muestra un cuadro de mensaje con información sobre la ubicación.


# Función para buscar ubicación por coordenadas
def buscar_ubicacion():
    """
    Busca y muestra en el mapa una ubicación basada en coordenadas ingresadas por el usuario.
    
    Formato esperado: latitud,longitud
    Ejemplo: 40.4168,-3.7038
    """
    entrada = entrada_busqueda.get()  # Obtiene el valor que el usuario introduce en el campo de entrada de búsqueda.
    try:
        # Separar latitud y longitud ingresadas por el usuario
        latitud, longitud = map(float, entrada.split(","))  # Divide la cadena de entrada por la coma y convierte las partes a flotantes.
        map_widget.set_position(latitud, longitud)  # Ajusta la posición del mapa a las coordenadas ingresadas.
        map_widget.set_marker(latitud, longitud, text="Ubicación Especificada")  # Coloca un marcador en las coordenadas especificadas.
        messagebox.showinfo("Ubicación encontrada", f"Ubicación encontrada: {latitud}, {longitud}")  # Muestra un mensaje con las coordenadas encontradas.
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce coordenadas válidas en el formato: latitud,longitud")  # Si hay un error al convertir las coordenadas, muestra un mensaje de error.

def mostrar_ubicacion_real():
    """Obtiene la ubicación actual del usuario y la muestra en el mapa."""
    try:
        # Obtener la ubicación actual utilizando geocoder
        ubicacion = geocoder.ip("me")  # Obtiene la ubicación basada en la IP local del usuario.
        if ubicacion.ok:  # Si la ubicación se obtiene correctamente:
            latitud, longitud = ubicacion.latlng  # Asigna las coordenadas obtenidas de la ubicación de la IP.
            map_widget.set_position(latitud, longitud)  # Ajusta el mapa a la ubicación obtenida.
            map_widget.set_zoom(15)  # Ajusta el zoom para hacer más detallada la vista.
            map_widget.set_marker(latitud, longitud, text="Mi IP está en....")  # Coloca un marcador en la ubicación obtenida.
            messagebox.showinfo("Ubicación", f"Tu IP se sitúa en: {latitud}, {longitud}")  # Muestra un mensaje con la ubicación de la IP.
        else:
            messagebox.showerror("Error", "No se pudo obtener la ubicación real")  # Si no se puede obtener la ubicación, muestra un mensaje de error.
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener la ubicación: {e}")  # Si ocurre algún error en el proceso, muestra un mensaje de error.

mapa_ventana = tk.Tk()  # Crea la ventana principal de la aplicación utilizando tkinter.
mapa_ventana.title("Mapa Genérico de Búsqueda")  # Establece el título de la ventana como "Mapa Genérico de Búsqueda".
mapa_ventana.geometry("800x600")  # Define el tamaño de la ventana en píxeles (ancho x alto).


entrada_busqueda = tk.Entry(mapa_ventana, width=50, font=("Arial", 12))  # Crea un campo de entrada de texto para que el usuario ingrese las coordenadas.
entrada_busqueda.pack(pady=10)  # Añade el campo de entrada a la ventana y le da un margen vertical de 10 píxeles.


boton_buscar = tk.Button(
    mapa_ventana,  # Botón que se crea dentro de la ventana principal.
    text="Buscar ubicación por coordenadas",  # Texto que aparecerá en el botón.
    font=("Arial", 12),  # Define el tipo de fuente y tamaño del texto del botón.
    command=buscar_ubicacion  # Define la función que se ejecutará cuando el usuario presione el botón.
)
boton_buscar.pack(pady=10)  # Añade el botón a la ventana y le da un margen vertical de 10 píxeles.


map_widget = TkinterMapView(mapa_ventana, width=780, height=450, corner_radius=0)  # Crea el widget de mapa con un tamaño específico.
map_widget.pack(pady=10)  # Añade el mapa a la ventana con un margen vertical de 10 píxeles.


# Configurar punto inicial del mapa con coordenadas de Madrid
map_widget.set_position(40.4168, -3.7038)
map_widget.set_zoom(10)

boton_ubicacion = tk.Button(
    mapa_ventana,  # Botón que se crea dentro de la ventana principal.
    text="Los Madriles",  # Texto que aparecerá en el botón.
    font=("Arial", 12),  # Define el tipo de fuente y tamaño del texto del botón.
    command=mostrar_ubicacion  # Define la función que se ejecutará cuando el usuario presione el botón.
)
boton_ubicacion.pack(side="left", padx=5, pady=5)  # Añade el botón a la ventana, alineado a la izquierda y con márgenes laterales.


boton_ubicacion_real = tk.Button(
    mapa_ventana,  # Botón que se crea dentro de la ventana principal.
    text="Ubicación de mi IP",  # Texto que aparecerá en el botón.
    font=("Arial", 12),  # Define el tipo de fuente y tamaño del texto del botón.
    command=mostrar_ubicacion_real  # Define la función que se ejecutará cuando el usuario presione el botón.
)
boton_ubicacion_real.pack(side="left", padx=5, pady=5)  # Añade el botón a la ventana, alineado a la izquierda y con márgenes laterales.


mapa_ventana.mainloop()  # Inicia el bucle principal de la aplicación, que mantiene la ventana abierta y en funcionamiento hasta que el usuario la cierre.
