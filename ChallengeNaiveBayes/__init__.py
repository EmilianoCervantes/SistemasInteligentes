import tensorflow as tf
import pandas as pd
import numpy as np

# Columna v1 - clasificacion ham/spam
# v2 - palabras a clasificar
data = pd.read_csv("spam.csv", encoding="utf-8")
print(data.head())

distribucion = None

'''def generarModelo(self, clasificaciones, palabras):
	# numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)
	# Find the unique elements of an array. Returns the sorted unique elements of an array
	palabras_unicas = np.unique(palabras)
	# zip(*iterables)
	# Make an iterator that aggregates elements from each of the iterables.
	palabras_por_clasificacion = np.array([
		[pal for pal, palabra in zip(clasificaciones, palabras) if palabra == clasificacion] \
		for clasificacion in palabras_unicas
	])
	media, desviacion_estandar = tf.nn.moments(tf.placeholder(tf.string, palabras_por_clasificacion), tf.sqrt(axes=[1]))
	# media, varianza = tf.nn.moments(tf.constant(palabras_por_clasificacion))
	
	self.distribucion = tf.distributions.Normal(loc=media, scale=desviacion_estandar)
	
def predecir(self, palabra):
	# Tomar datos de prueba
	# arr = [1,2,3,4,5]
	# arr[:] = [1,2,3,4,5]
'''

'''
Sklearn
This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 150x4 numpy.ndarray
The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features. - entiendo van siendo las caracteristicas/clasificaciones
y = iris.target - las cosas a categorizar
'''

# Como esta la columna v1 ahorita:
# TypeError: Expected binary or unicode string, got ['ham']
# Cambiar ham por 0 y spam por 1
data['v1'] = data['v1'].replace('ham', 0)
data['v1'] = data['v1'].replace('spam', 1)
print(data['v1'])
print(data['v2'])
# numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)
# Find the unique elements of an array. Returns the sorted unique elements of an array
palabras_unicas = np.unique(data['v2'])
# zip(*iterables)
# Make an iterator that aggregates elements from each of the iterables.
palabras_por_clasificacion = np.array([
	[x for x, clasif in zip(data['v2'], data['v1']) if clasif == clasificacion]\
	for clasificacion in palabras_unicas
])
# media, desviacion_estandar = tf.nn.moments(tf.placeholder(tf.string, palabras_por_clasificacion), tf.sqrt(axes=[1]))
# media, desviacion_estandar = tf.nn.moments(tf.constant(palabras_por_clasificacion, dtype=tf.as_dtype), tf.sqrt(axes=[1]))
media, varianza = tf.nn.moments(tf.constant(palabras_por_clasificacion), axes=[1])
# media, varianza = tf.nn.moments(palabras_por_clasificacion, axes=[1])
desviacion_estandar = tf.sqrt(varianza)
distribucion = tf.distributions.Normal(loc=media, scale=desviacion_estandar)
print(distribucion)
