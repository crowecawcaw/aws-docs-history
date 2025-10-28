# Debugger tutorial videos

The following videos provide a tour of Amazon SageMaker Debugger capabilities using SageMaker Studio and SageMaker AI
notebook instances.

###### Topics

- [Debugging models with Amazon SageMaker Debugger in
  Studio Classic](#debugger-video-get-started "#debugger-video-get-started")
- [Deep dive on Amazon SageMaker Debugger and SageMaker AI model
  monitor](#debugger-video-dive-deep "#debugger-video-dive-deep")

## Debugging models with Amazon SageMaker Debugger in

Studio Classic

_Julien Simon, AWS Technical Evangelist | Length: 14
minutes 17 seconds_

This tutorial video demonstrates how to use Amazon SageMaker Debugger to capture and inspect
debugging information from a training model. The example training model used in this
video is a simple convolutional neural network (CNN) based on Keras with the
TensorFlow backend. SageMaker AI in a TensorFlow framework and Debugger enable you to build an
estimator directly using the training script and debug the training job.

You can find the example notebook in the video in [this
Studio Demo repository](https://gitlab.com/juliensimon/amazon-studio-demos/-/tree/master "https://gitlab.com/juliensimon/amazon-studio-demos/-/tree/master") provided by the author. You need to clone the
`debugger.ipynb` notebook file and the
`mnist_keras_tf.py` training script to your SageMaker Studio or a
SageMaker notebook instance. After you clone the two files, specify the path
`keras_script_path` to the `mnist_keras_tf.py`
file inside the `debugger.ipynb` notebook. For example, if you
cloned the two files in the same directory, set it as `keras_script_path =
 "mnist_keras_tf.py"`.

## Deep dive on Amazon SageMaker Debugger and SageMaker AI model

monitor

_Julien Simon, AWS Technical Evangelist | Length: 44
minutes 34 seconds_

This video session explores advanced features of Debugger and SageMaker Model Monitor
that help boost productivity and the quality of your models. First, this video shows
how to detect and fix training issues, visualize tensors, and improve models with
Debugger. Next, at 22:41, the video shows how to monitor models in production and
identify prediction issues such as missing features or data drift using SageMaker AI Model
Monitor. Finally, it offers cost optimization tips to help you make the most of your
machine learning budget.

You can find the example notebook in the video in [this AWS
Dev Days 2020 repository](https://gitlab.com/juliensimon/awsdevdays2020/-/tree/master/mls1 "https://gitlab.com/juliensimon/awsdevdays2020/-/tree/master/mls1") offered by the author.
