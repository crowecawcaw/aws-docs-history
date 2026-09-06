

# Debugger tutorial videos
<a name="debugger-videos"></a>

**Note**  
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md). 

The following videos provide a tour of Amazon SageMaker Debugger capabilities using SageMaker Studio and SageMaker AI notebook instances. 

**Topics**
+ [Debugging models with Amazon SageMaker Debugger in Studio Classic](#debugger-video-get-started)
+ [Deep dive on Amazon SageMaker Debugger and SageMaker AI model monitor](#debugger-video-dive-deep)

## Debugging models with Amazon SageMaker Debugger in Studio Classic
<a name="debugger-video-get-started"></a>

*Julien Simon, AWS Technical Evangelist \| Length: 14 minutes 17 seconds*

This tutorial video demonstrates how to use Amazon SageMaker Debugger to capture and inspect debugging information from a training model. The example training model used in this video is a simple convolutional neural network (CNN) based on Keras with the TensorFlow backend. SageMaker AI in a TensorFlow framework and Debugger enable you to build an ModelTrainer directly using the training script and debug the training job.

[![AWS Videos](http://img.youtube.com/vi/MqPdTj0Znwg/0.jpg)](http://www.youtube.com/watch?v=MqPdTj0Znwg)


You can find the example notebook in the video in [ this Studio Demo repository](https://gitlab.com/juliensimon/amazon-studio-demos/-/tree/master) provided by the author. You need to clone the `debugger.ipynb` notebook file and the `mnist_keras_tf.py` training script to your SageMaker Studio or a SageMaker notebook instance. After you clone the two files, specify the path `keras_script_path` to the `mnist_keras_tf.py` file inside the `debugger.ipynb` notebook. For example, if you cloned the two files in the same directory, set it as `keras_script_path = "mnist_keras_tf.py"`.

## Deep dive on Amazon SageMaker Debugger and SageMaker AI model monitor
<a name="debugger-video-dive-deep"></a>

*Julien Simon, AWS Technical Evangelist \| Length: 44 minutes 34 seconds*

This video session explores advanced features of Debugger and SageMaker Model Monitor that help boost productivity and the quality of your models. First, this video shows how to detect and fix training issues, visualize tensors, and improve models with Debugger. Next, at 22:41, the video shows how to monitor models in production and identify prediction issues such as missing features or data drift using SageMaker AI Model Monitor. Finally, it offers cost optimization tips to help you make the most of your machine learning budget.

[![AWS Videos](http://img.youtube.com/vi/0zqoeZxakOI/0.jpg)](http://www.youtube.com/watch?v=0zqoeZxakOI)


You can find the example notebook in the video in [ this AWS Dev Days 2020 repository](https://gitlab.com/juliensimon/awsdevdays2020/-/tree/master/mls1) offered by the author.