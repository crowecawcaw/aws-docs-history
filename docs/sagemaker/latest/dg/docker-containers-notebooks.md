# Examples and More Information: Use Your Own

Algorithm or Model

The following Jupyter notebooks and added information show how to use your own algorithms
or pretrained models from an Amazon SageMaker notebook instance. For links to the GitHub
repositories with the prebuilt Dockerfiles for the TensorFlow, MXNet, Chainer, and PyTorch
frameworks and instructions on using the AWS SDK for Python (Boto3) estimators to run your own training
algorithms on SageMaker AI Learner and your own models on SageMaker AI hosting, see [Prebuilt SageMaker AI Docker images
for deep learning](pre-built-containers-frameworks-deep-learning.md "pre-built-containers-frameworks-deep-learning.md")

## Setup

1. Create a SageMaker notebook instance. For instructions on how to create and access
   Jupyter notebook instances, see [Amazon SageMaker notebook instances](nbi.md "nbi.md").
2. Open the notebook instance you created.
3. Choose the **SageMaker AI Examples** tab for a list of all SageMaker AI
   example notebooks.
4. Open the sample notebooks from the **Advanced Functionality**
   section in your notebook instance or from GitHub using the provided links. To
   open a notebook, choose its **Use** tab, then
   choose **Create copy**.

## Host models trained in

Scikit-learn

To learn how to host models trained in Scikit-learn for making predictions in SageMaker AI by
injecting them into first-party k-means and XGBoost containers, see the following sample
notebooks.

- [kmeans_bring_your_own_model](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/kmeans_bring_your_own_model "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/kmeans_bring_your_own_model")
- [xgboost_bring_your_own_model](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/xgboost_bring_your_own_model "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/xgboost_bring_your_own_model")

## Package TensorFlow and

Scikit-learn models for use in SageMaker AI

To learn how to package algorithms that you have developed in TensorFlow and
scikit-learn frameworks for training and deployment in the SageMaker AI environment, see the
following notebooks. They show you how to build, register, and deploy your own Docker
containers using Dockerfiles.

- [tensorflow_bring_your_own](https://github.com/aws/amazon-sagemaker-examples/blob/main/advanced_functionality/tensorflow_iris_byom/tensorflow_BYOM_iris.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/advanced_functionality/tensorflow_iris_byom/tensorflow_BYOM_iris.ipynb")
- [scikit_bring_your_own](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/scikit_bring_your_own "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/scikit_bring_your_own")

## Train and deploy a neural network

on SageMaker AI

To learn how to train a neural network locally using MXNet or TensorFlow, and then
create an endpoint from the trained model and deploy it on SageMaker AI, see the following
notebooks. The MXNet model is trained to recognize handwritten numbers from the MNIST
dataset. The TensorFlow model is trained to classify irises.

- [mxnet_mnist_byom](https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/using_mxnet.html "https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/using_mxnet.html")
- [tensorflow_BYOM_iris](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/tensorflow_iris_byom/tensorflow_BYOM_iris.ipynb "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/tensorflow_iris_byom/tensorflow_BYOM_iris.ipynb")

## Training using pipe mode

To learn how to use a Dockerfile to build a container that calls the
`train.py script` and uses pipe mode to custom train an
algorithm, see the following notebook. In pipe mode, the input data is transferred to
the algorithm while it is training. This can decrease training time compared to using
file mode.

- [pipe_bring_your_own](https://github.com/aws/amazon-sagemaker-examples/blob/0efd885ef2a5c04929d10c5272681f4ca17dac17/advanced_functionality/pipe_bring_your_own/pipe_bring_your_own.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/0efd885ef2a5c04929d10c5272681f4ca17dac17/advanced_functionality/pipe_bring_your_own/pipe_bring_your_own.ipynb")

## Bring your own R model

To learn how to use add a custom R image to build and train a model in a AWS SMS
notebook, see the following blog post. This blog post uses a sample R Dockerfile from a
library of [SageMaker AI
Studio Classic Custom Image Samples](https://github.com/aws-samples/sagemaker-studio-custom-image-samples "https://github.com/aws-samples/sagemaker-studio-custom-image-samples").

- [Bringing your own R environment to Amazon SageMaker Studio Classic](https://aws.amazon.com/blogs/machine-learning/bringing-your-own-r-environment-to-amazon-sagemaker-studio/ "https://aws.amazon.com/blogs/machine-learning/bringing-your-own-r-environment-to-amazon-sagemaker-studio/")

## Extend a pre-built PyTorch container

Image

To learn how to extend a prebuilt SageMaker AI PyTorch container image when you have
additional functional requirements for your algorithm or model that the prebuilt Docker
image doesn't support, see the following notebook.

- [BERTtopic_extending_container](https://github.com/aws/amazon-sagemaker-examples/blob/0efd885ef2a5c04929d10c5272681f4ca17dac17/advanced_functionality/pytorch_extend_container_train_deploy_bertopic/BERTtopic_extending_container.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/0efd885ef2a5c04929d10c5272681f4ca17dac17/advanced_functionality/pytorch_extend_container_train_deploy_bertopic/BERTtopic_extending_container.ipynb")

For more information about extending a container, see [Extend a Pre-built
Container](prebuilt-containers-extend.md "prebuilt-containers-extend.md").

## Train and debug training jobs on

a custom container

To learn how to train and debug training jobs using SageMaker Debugger, see the following
notebook. A training script provided through this example uses the TensorFlow Keras
ResNet 50 model and the CIFAR10 dataset. A Docker custom container is built with the
training script and pushed to Amazon ECR. While the training job is running, Debugger collects
tensor outputs and identifies debugging problems. With `smdebug` client
library tools, you can set a `smdebug` trial object that calls the training
job and debugging information, check the training and Debugger rule status, and retrieve
tensors saved in an Amazon S3 bucket to analyze training issues.

- [build_your_own_container_with_debugger](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/build_your_own_container_with_debugger/debugger_byoc.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/build_your_own_container_with_debugger/debugger_byoc.html")
