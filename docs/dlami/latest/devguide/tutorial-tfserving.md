# TensorFlow Serving

[TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving "https://www.tensorflow.org/tfx/guide/serving") is a flexible, high-performance serving system for machine learning models.

The `tensorflow-serving-api` is pre-installed with single framwork DLAMI.
To use tensorflow serving, first activate the TensorFlow environment.

```
`$` source /opt/tensorflow/bin/activate
```

Then use your preferred text editor to
create a script that has the following content. Name it `test_train_mnist.py`.
This script is referenced from [TensorFlow Tutorial](https://github.com/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb "https://github.com/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb") which will train and evaluate a neural network machine learning model that classifies images.

```

import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)

```

Now run the script passing the server location and port and the husky photo's filename as the parameters.

```
`$` /opt/tensorflow/bin/python3 test_train_mnist.py
```

Be patient, as this script may take a while before providing any output.
When the training is complete you should see the following:

```
I0000 00:00:1739482012.389276    4284 device_compiler.h:188] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.
1875/1875 [==============================] - 24s 2ms/step - loss: 0.2973 - accuracy: 0.9134
Epoch 2/5
1875/1875 [==============================] - 3s 2ms/step - loss: 0.1422 - accuracy: 0.9582
Epoch 3/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.1076 - accuracy: 0.9687
Epoch 4/5
1875/1875 [==============================] - 3s 2ms/step - loss: 0.0872 - accuracy: 0.9731
Epoch 5/5
1875/1875 [==============================] - 3s 1ms/step - loss: 0.0731 - accuracy: 0.9771
313/313 [==============================] - 0s 1ms/step - loss: 0.0749 - accuracy: 0.9780

```

## More Features and Examples

If you are interested in learning more about TensorFlow Serving, check out the
[TensorFlow website](https://www.tensorflow.org/serving/ "https://www.tensorflow.org/serving/").
