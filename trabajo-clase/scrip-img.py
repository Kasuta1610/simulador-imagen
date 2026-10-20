import argparse  # Librería para leer argumentos desde la línea de comandos (terminal)
import os  # Librería para manejar carpetas y rutas del sistema operativo


def crear_archivos(cantidad, prefijo, ruta):
  # os.makedirs crea la carpeta de destino.
  # exist_ok=True evita que dé error si la carpeta ya existe.
  os.makedirs(ruta, exist_ok=True)

  print(f"Creando {cantidad} archivos en: {ruta}...")

  # Bucle que se repite desde 1 hasta la cantidad indicada (1000 por defecto)
  for i in range(1, cantidad + 1):
    # f"{prefijo}{i:04d}.txt" da formato al nombre:
    # - {prefijo}: toma "img"
    # - {i:04d}: rellena el número con ceros a la izquierda hasta 4 dígitos (0001, 0002...)
    # - .txt: la extensión del archivo
    nombre = f"{prefijo}{i:04d}.txt"

    # os.path.join une de forma segura la ruta de la carpeta con el nombre del archivo
    ruta_completa = os.path.join(ruta, nombre)

    # Abre (o crea) el archivo en modo escritura ("w" de write) con codificación UTF-8
    with open(ruta_completa, "w", encoding="utf-8") as f:
      # Escribe un texto básico dentro de cada archivo
      f.write(f"Hola {i}")

  print("¡Proceso terminado con éxito!")


# Este bloque asegura que el script solo se ejecute si lo llamamos directamente
if __name__ == "__main__":
  # Configurar el analizador de argumentos de la terminal
  parser = argparse.ArgumentParser(
      description="Crear archivos en secuencia de forma automatizada."
  )

  # Argumento para definir cuántos archivos queremos crear (por defecto 1000)
  parser.add_argument(
      "--cantidad", type=int, default=1000, help="Número de archivos a crear"
  )

  # Argumento para definir el nombre inicial de los archivos (por defecto "img")
  parser.add_argument(
      "--prefijo", type=str, default="img", help="Prefijo para los nombres"
  )

  # Argumento para definir la carpeta donde se guardarán
  parser.add_argument(
      "--ruta",
      type=str,
      default=r"C:\Users\Zack\Documents\visual\clase1310\fotos",
      help="Carpeta de destino",
  )

  # Lee los argumentos que le pasemos (o usa los valores por defecto si no ponemos nada)
  args = parser.parse_args()

  # Llama a la función principal pasándole los valores obtenidos
  crear_archivos(args.cantidad, args.prefijo, args.ruta)

      