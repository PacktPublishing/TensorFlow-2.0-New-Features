# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:53:50 2019

@author: Radhika
"""

from __future__ import absolute_import, division, print_function

import tensorflow as tf

tf.enable_eager_execution()

tf.executing_eagerly()

x = [[2.]]
m = tf.matmul(x, x)
print("hello, {}".format(m))

a = tf.constant([[1, 2],
                 [3, 4]])

# Broadcasting support
b = tf.add(a, 1)
print(b)

# Operator overloading is supported
print(a * b)

# Use NumPy values
import numpy as np

c = np.multiply(a, b)
print(c)


# Obtain numpy value from a tensor:
print(a.numpy())
# => [[1 2]
#     [3 4]]

tfe = tf.contrib.eager

def fizzbuzz(max_num):
  counter = tf.constant(0)
  max_num = tf.convert_to_tensor(max_num)
  for num in range(1, max_num.numpy()+1):
    num = tf.constant(num)
    if int(num % 3) == 0 and int(num % 5) == 0:
      print('FizzBuzz')
    elif int(num % 3) == 0:
      print('Fizz')
    elif int(num % 5) == 0:
      print('Buzz')
    else:
      print(num.numpy())
    counter += 1
    
fizzbuzz(15)