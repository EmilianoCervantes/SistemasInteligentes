import tensorflow as tf

ss = tf.Session()
print(ss)

c = tf.constant(4.7)
ss = tf.Session()
print(ss.run(c))

# Declarando constante
x = tf.constant(45, name='x')
y = tf.Variable(x + 10, name='y')

# Inicializar variables
modelo = tf.global_variables_initializer()

print(type(x))
print(type(y))
print(x)
print(y)

# Crear operacion
a_mas_b = tf.add(x,y)

with tf.Session() as ss:
	ss.run(modelo)
	salida = ss.run(a_mas_b)
	print(salida)
	# print(ss.run(y))

# Placeholder
ph = tf.placeholder("float", None)
ph2 = tf.placeholder("float", None)
# Operaciones pueden ponerse explicitas o declararse
cuadrado = ph ** 2
with tf.Session() as ss:
	res = ss.run(cuadrado, feed_dict={ph: [5, 8, 9], ph2: [6, 6, 6]})
	print(res)

tf.reset_default_graph()
a = tf.constant(2)
b = tf.constant(3)
c = tf.add(a, b)

# PROBLEMA INTERNET TELEFONO
''' p(A|B) = P(B|A)*P(A) / P(B) '''
A = 0.63


# with tf.Session() as ss:
	# Codigo faltante
