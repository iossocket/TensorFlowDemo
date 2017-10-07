import tensorflow as tf
import os  
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
print(tf.__version__)

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b

print(result)

with tf.Session() as sess:
  print(result.eval())
