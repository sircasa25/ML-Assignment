import tensorflow_hub
from dataprovider import data 
import tensorflow.compat.v1 as tf

tf.disable_eager_execution()
ses = tf.Session()

elmo = tensorflow_hub.Module("https://tfhub.dev/google/elmo/3", trainable=False)

embeddings = elmo(data, signature = 'default', as_dict = True)["elmo"]

ses.run(tf.initialize_all_variables())
print("working")

print(ses.run(embeddings[1][4]))