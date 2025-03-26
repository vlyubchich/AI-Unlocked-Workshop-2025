### Example based on  https://www.tensorflow.org/guide/keras/functional
### slurm_resolver call sets 4 GPUs per node (for Expanse)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

batch_size=64
slurm_resolver = tf.distribute.cluster_resolver.SlurmClusterResolver(port_base=15000,gpus_per_node=4, gpus_per_task=4, tasks_per_node=1, auto_set_gpu=False, rpc_layer='grpc')
mirrored_strategy = tf.distribute.MultiWorkerMirroredStrategy(cluster_resolver=slurm_resolver)

print('Number of replicas:', mirrored_strategy.num_replicas_in_sync)
with mirrored_strategy.scope():
     inputs = keras.Input(shape=(784,), name='img')
     x = layers.Dense(64, activation='relu')(inputs)
     x = layers.Dense(64, activation='relu')(x)
     outputs = layers.Dense(10)(x)

     model = keras.Model(inputs=inputs, outputs=outputs, name='mnist_model')

     model.compile(loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True), optimizer=keras.optimizers.RMSprop(), metrics=['accuracy'])

x_train = tf.random.normal((60000, 784), dtype='float32')
x_test = tf.random.normal((10000, 784), dtype='float32')
y_train = tf.random.uniform((60000,), minval=0, maxval=10, dtype='int32')
y_test = tf.random.uniform((10000,), minval=0, maxval=10, dtype='int32')


history = model.fit(x_train, y_train,
                        batch_size=batch_size,
                        epochs=5,
                        validation_split=0.2)
test_scores = model.evaluate(x_test, y_test, verbose=2)

print('Test loss:', test_scores[0])
print('Test accuracy:', test_scores[1])
