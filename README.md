# Mapa Genérico de Búsqueda

![mapa-generico](https://github.com/user-attachments/assets/00a9c6d9-1cf0-446f-ad7f-644274895682)

Este proyecto permite mostrar y buscar ubicaciones en un mapa interactivo utilizando **Tkinter** y **TkinterMapView**. Los usuarios pueden buscar ubicaciones por coordenadas geográficas, por dirección (texto de una ubicación) o visualizar la ubicación actual basada en su dirección IP.

## Características

- Muestra una ubicación inicial (Madrid) en el mapa.
- Permite buscar una ubicación basada en coordenadas ingresadas por el usuario.
- Permite buscar una ubicación basada en una dirección escrita.
- Muestra la ubicación real del usuario basada en su dirección IP.
- Interfaz gráfica sencilla construida con **Tkinter**.

## Funcionalidades

1. **Mostrar Ubicación Inicial (Madrid):**
   - Al hacer clic en el botón "Los Madriles", se muestra la ubicación de Madrid en el mapa con un marcador.
   
2. **Buscar Ubicación por Coordenadas:**
   - Al escribir las coordenadas en el formato `latitud,longitud` y hacer clic en "Buscar ubicación por coordenadas", se muestra la ubicación especificada en el mapa.

3. **Obtener Ubicación Real:**
   - Al hacer clic en "Ubicación de mi IP", el programa obtiene la ubicación del usuario utilizando la biblioteca `geocoder`, mostrando la posición en el mapa basada en su dirección IP.

## Instalación

Para ejecutar este proyecto, asegúrate de tener Python 3.x instalado y luego instala las dependencias necesarias.

### Dependencias

1. **Tkinter**: Esta biblioteca está incluida en la mayoría de las distribuciones de Python. Si no la tienes, instálala con:
2. **TkinterMapView**: Este es el widget de mapas basado en Leaflet.
3. **Geocoder**: Esta biblioteca se usa para obtener la ubicación basada en la dirección IP.

## Uso

1. **Ejecutar el script**: Abre una terminal, navega a la carpeta del proyecto y ejecuta el script:

    ```bash
    python run_app.py
    ```
    - Las dependecias del requirements.txt deberían instalarse de forma automátican antes de abrir el mapa.

2. **Interactuar con el mapa**:
   - **Los Madriles**: Muestra la ubicación inicial (Madrid).
   - **Buscar ubicación por coordenadas**: Escribe las coordenadas en el formato `latitud,longitud` (por ejemplo, `40.4168,-3.7038`) y presiona el botón.
   - **Ubicación de mi IP**: Muestra la ubicación basada en la IP pública del dispositivo.

## Notas

- **Precisión de la ubicación IP**: La ubicación obtenida por `geocoder.ip("me")` depende de la IP pública, por lo que no siempre es precisa.
- **Formato de coordenadas**: Asegúrate de ingresar las coordenadas en el formato correcto `latitud,longitud`, separadas por una coma.
