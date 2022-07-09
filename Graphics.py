#-----------------------------------------------------------------------------------------------------------
#Algunas librerias
import numpy as np
import matplotlib.pyplot as plt

#Creando el gráfico de barras para la información solicitada en el primer ejercicio

# Definir los Arreglos de Datos.
Lenguajes = np.array(["Burj Khalifa", "Torre Shanghai", "Torre Royal Clock", "Torre Ping An", "Torre Lotte World", "Torre One World", "Torre Tianjin", "Torre Guangzhou", "Torre CITIC", "Taipei 101"])
Porcentaje = np.array([829.8, 632, 601, 599.1, 555.7, 546.2, 530.4, 530, 527.7, 508])
# Crear Arreglo para las Posiciones de las Barras.
Posicion = np.arange(len(Lenguajes)) # Posicion = [0, 1, 2, 3, 4, 5, 6. 7, 8, 9]
# Generar el Gráfico de Barras.
plt.figure(figsize=(18,6))
plt.bar(Posicion, Porcentaje, align="center", alpha=0.7, color="g")
# Agregando los Nombres de cada Barra.
plt.xticks(Posicion, Lenguajes, rotation=45)
# Agregando Títulos para los Ejes y para el Gráfico.
plt.xlabel("Edificios")
plt.ylabel("Altura (M)")
plt.title("Los edificios más altos del mundo en el 2022")
# Ajustando Margen Inferior del Gráfico.
plt.subplots_adjust(bottom=0.2)
# Mostrando Gráfico en Pantalla.
plt.show()

#Creando el gráfico de porciones para la información solicitada en el segundo ejercicio

# Crear los Arreglos para Almacenar los Datos.
Gen = np.array(["Europeo", "Indígenas", "Africanos", "Asiáticos"])
Porcentaje = np.array([45.6, 33.5, 11.7, 9.2])
# Crear Tupla de Selección de una Porción.
Seleccion = (0, 0, 0, 0)
# Generar el Gráfico de Pastel.
plt.figure(figsize=(10,10))
plt.pie(Porcentaje, labels=Gen, autopct="%.1f%%", explode=Seleccion)
plt.title("Orígenes de los genes de la población Costarrricense")
# Mostrando Gráfico en Pantalla.
plt.show()