import argparse
from datetime import datetime
import os

def main():
  # Crear el objeto parser que se encargará de leer los comandos que escribas en la terminal
  parser = argparse.ArgumentParser(
      description=(
          "Generador de archivos secuenciales con código de tiempo para CMD."
      )
  )
  # Argumento obligatorio: Nombre de la carpeta (-n o --nombre_carpeta)
  parser.add_argument(
      "-n",
      "--nombre_carpeta",
      type=str,
      required=True,  # Es obligatorio pasarlo en la terminal
      help="Nombre de la nueva carpeta que se creará.",
  )
  # Argumento opcional: Cantidad de archivos a crear (-c o --cantidad)
  parser.add_argument(
      "-c",
      "--cantidad",
      type=int,
      default=10,  # Si no pones nada, por defecto creará 10
      choices=[
          1,
          5,
          10,
          100,
          1000,
      ],  # Restringe los valores permitidos únicamente a estos
      help="Cantidad de archivos a generar (1, 5, 10, 100 o 1000).",
  )
  # Argumento opcional: Ruta base donde se guardará todo
  parser.add_argument(
      "--ruta_base",
      type=str,
      default=r"C:\Users\Zack\Documents\visual\clase1310",
      help="Ruta base del directorio de trabajo.",
  )

  # Lee y captura todos los argumentos que el usuario escribió en la terminal
  args = parser.parse_args()

  # 1. GESTIÓN DE LA CARPETA DE DESTINO
  # Une de forma segura la ruta base con el nombre de la carpeta que introdujiste
  ruta_destino = os.path.join(args.ruta_base, args.nombre_carpeta)

  # Comprobador: verifica si la carpeta ya existe físicamente en el ordenador
  if os.path.exists(ruta_destino):
    print(f" La carpeta '{args.nombre_carpeta}' ya existe. Se usará la existente.")
  else:
    os.makedirs(ruta_destino)
    print(f"Carpeta '{args.nombre_carpeta}' creada con éxito.")

  # 2. GENERACIÓN DEL CÓDIGO TEMPORAL ÚNICO
  # Obtiene la fecha y hora exacta del momento en que se ejecuta el script
  ahora = datetime.now()
  anio = ahora.strftime("%Y") 
  mes = ahora.strftime("%m") 
  dia = ahora.strftime("%d") 
  hora = ahora.strftime("%H")  
  minuto = ahora.strftime("%M")  
  segundo = ahora.strftime("%S")  
  milisegundo = str(ahora.microsecond)[
      :3
  ]  # Microsegundos recortados a 3 dígitos (milisegundos)

  # Construye el código base único combinando todos los valores temporales
  codigo_base = f"IMG_{anio}{mes}{dia}_{hora}{minuto}{segundo}_{milisegundo}"

  print(f"Generando {args.cantidad} archivos en: {ruta_destino}...")

  # 3. BUCLE DE CREACIÓN DE ARCHIVOS
  # Se repite tantas veces como indique la cantidad elegida (desde 1 hasta N)
  for i in range(1, args.cantidad + 1):
    # Formatea el nombre combinando el código de tiempo y el número secuencial (ej. _0001.txt)
    nombre_archivo = f"{codigo_base}_{i:04d}.txt"
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)

    # Comprobador individual: por si un archivo con ese nombre exacto ya existiera
    if os.path.exists(ruta_completa):
      print(f" El archivo {nombre_archivo} ya existe, omitiendo...")
      continue  # Salta a la siguiente iteración sin sobrescribir

    # Abre el archivo en modo escritura ("w") con codificación UTF-8 y escribe dentro
    with open(ruta_completa, "w", encoding="utf-8") as f:
      f.write(f"Hola {i} - Generado desde el script")

  print(
      f"¡Proceso completado! Se han creado {args.cantidad} archivos en"
      f" '{args.nombre_carpeta}'."
  )

# Punto de entrada principal del script cuando se ejecuta desde la terminal
if __name__ == "__main__":
  main() 
  
  # python simulador.py --help
  # python simular-imagen/simulador.py -n imgs -c 100