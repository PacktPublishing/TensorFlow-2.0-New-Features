import tensorflow as tf
import keras as k
sess = tf.Session()

outputs = sess.run(f(placeholder), feed_dict={placeholder: input})
outputs = f(input)

def my_func(x):
     return np.sinh(x)

outputs = sess.run(my_func(90))
outputs = my_func(90)