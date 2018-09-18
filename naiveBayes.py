import pandas as pd
import numpy as np

# un frame vacio creado con pandas
data = pd.DataFrame()

# Crearemos un clasificador donde nuestra variable meta es predecir el sexo en base a otras variables independientes
data['sexo'] = ['hombre', 'hombre', 'hombre', 'hombre', 'mujer', 'mujer', 'mujer', 'mujer']

# Variables
data['altura'] = [6, 5.92, 5.58, 5.92, 5, 5.5, 5.42, 5.75]
data['peso'] = [180, 190, 170, 165, 100, 150, 130, 150]
data['tamanio_pies'] = [12, 11, 12, 10, 6, 8, 7, 9]
# View the data
print(data)

# dataFrame vacio
persona = pd.DataFrame()

# datos para predecir
persona['altura'] = [6]
persona['peso'] = [130]
persona['tamanio_pies'] = [8]

# View the data
print(persona)

# número de hombres
numHombres = data['sexo'][data['sexo'] == 'hombre'].count()
print(numHombres)

# número de mujeres
numMujeres = data['sexo'][data['sexo'] == 'mujer'].count()
print(numMujeres)

# total de registros
total = data['sexo'].count()
print(total)

# probabilidad de hombres
probHom = numHombres/total
print(probHom)

# probabilidad de mujeres
probMuj = numMujeres/total
print(probMuj)

# media de cada variable por sexo
dataMedia = data.groupby('sexo').mean()
print(dataMedia)

# Varianza de cada variable por sexo
dataVarianza = data.groupby('sexo').var()
print(dataVarianza)

# Media para hombre
mediaAlturaHom = dataMedia['altura']['hombre']
print(mediaAlturaHom)
mediaPesoHom = dataMedia['peso']['hombre']
print(mediaPesoHom)
mediaPiesHom = dataMedia['tamanio_pies']['hombre']
print(mediaPiesHom)

# Varianza para hombre
varAlturaHom = dataVarianza['altura']['hombre']
print(varAlturaHom)
varPesoHom = dataVarianza['peso']['hombre']
print(varPesoHom)
varPiesHom = dataVarianza['tamanio_pies']['hombre']
print(varPiesHom)

# media para mujer
mediaAlturaMuj = dataMedia['altura']['mujer']
print(mediaAlturaMuj)
mediaPesoMuj = dataMedia['peso']['mujer']
print(mediaPesoMuj)
mediaPiesMuj = dataMedia['tamanio_pies']['mujer']
print(mediaPiesMuj)

# varianza para mujer
varAlturaMuj = dataVarianza['altura']['mujer']
print(varAlturaMuj)
varPesoMuj = dataVarianza['peso']['mujer']
print(varPesoMuj)
varPiesMuj = dataVarianza['tamanio_pies']['mujer']
print(varPiesMuj)


# función para calcular p(x | y)
def p_x_dado_y(x, media_y, var_y):
	divisor = var_y * np.sqrt((2 * np.pi))
	parteUno = 1/divisor
	exponencialPower = np.power(np.e, -(np.power((x - media_y), 2))/2 * np.power(var_y, 2))
	return parteUno * exponencialPower


probHom * p_x_dado_y(persona['altura'][0], mediaAlturaHom, varAlturaHom) * \
	p_x_dado_y(persona['peso'][0], mediaPesoHom, varPesoHom) * \
	p_x_dado_y(persona['tamanio_pies'][0], mediaPiesHom, varPiesHom)
