

# TensorFlow 2
<a name="tutorial-tensorflow-2"></a>

This tutorial shows how to activate TensorFlow 2 on an instance running the Deep Learning AMI with Conda (DLAMI on Conda) and run a TensorFlow 2 program.

When a stable Conda package of a framework is released, it's tested and pre-installed on the DLAMI. 

## Activating TensorFlow 2
<a name="tutorial-tensorflow-2-overview"></a>

**To run TensorFlow on the DLAMI with Conda**

1. To activate TensorFlow 2, open an Amazon Elastic Compute Cloud (Amazon EC2) instance of the DLAMI with Conda.

1. For TensorFlow 2 and Keras 2 on Python 3 with CUDA 10.1 and MKL-DNN, run this command:

   ```
   $ source activate tensorflow2_p310
   ```

1. Start the iPython terminal:

   ```
   (tensorflow2_p310)$ ipython
   ```

1. Run a TensorFlow 2 program to verify that it is working properly:

   ```
   import tensorflow as tf
   hello = tf.constant('Hello, TensorFlow!')
   tf.print(hello)
   ```

   `Hello, TensorFlow!` should appear on your screen.

## More Tutorials
<a name="tutorial-tensorflow-2-more"></a>

For more tutorials and examples, see the TensorFlow documentation for the [TensorFlow Python API](https://www.tensorflow.org/api_docs/python/) or see the [TensorFlow](https://www.tensorflow.org) website.