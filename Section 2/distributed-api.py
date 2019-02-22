# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:42:41 2019

@author: Radhika
"""

import tensorflow as tf
import numpy as np
import pandas as pd
k = 5
n = 100
variables = 2
points = np.random.uniform(0, 1000, [n, variables])
input_fn=lambda: tf.train.limit_epochs(tf.convert_to_tensor(points, dtype=tf.float32), num_epochs=1)
kmeans=tf.contrib.factorization.KMeansClustering(num_clusters=k, use_mini_batch=False,model_dir="my_hdfs_path")

train_spec = tf.estimator.TrainSpec(input_fn=input_fn, max_steps=100)
eval_spec = tf.estimator.EvalSpec(input_fn=input_fn)

tf.estimator.train_and_evaluate(kmeans, train_spec, eval_spec)
print(kmeans.predict(input_fn=input_fn))