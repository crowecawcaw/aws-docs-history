

# Prebuilt SageMaker AI Docker images for deep learning
<a name="pre-built-containers-frameworks-deep-learning"></a>

Amazon SageMaker AI provides prebuilt Docker images that include deep learning frameworks and other dependencies needed for training and inference. For a complete list of the prebuilt Docker images managed by SageMaker AI, see [Docker Registry Paths and Example Code](https://docs.aws.amazon.com/sagemaker/latest/dg-ecr-paths/sagemaker-algo-docker-registry-paths.html).

## Using the SageMaker AI Python SDK
<a name="pre-built-containers-frameworks-deep-learning-sdk"></a>

With the [SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk#installing-the-sagemaker-python-sdk), you can train and deploy models using these popular deep learning frameworks. For instructions on installing and using the SDK, see [[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable)](https://github.com/aws/sagemaker-python-sdk#installing-the-sagemaker-python-sdk). The following table lists the available frameworks and instructions on how to use them with the [SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk#installing-the-sagemaker-python-sdk):


| Framework | Instructions | 
| --- | --- | 
| TensorFlow | [Using TensorFlow with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) | 
| MXNet | [Using MXNet with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) | 
| PyTorch | [Using PyTorch with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) | 
| Chainer | [Using Chainer with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) | 
| Hugging Face | [Using Hugging Face with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) | 

## Extending Prebuilt SageMaker AI Docker Images
<a name="pre-built-containers-frameworks-deep-learning-adapt"></a>

You can customize these prebuilt containers or extend them as needed. With this customization, you can handle any additional functional requirements for your algorithm or model that the prebuilt SageMaker AI Docker image doesn't support. For an example of this, see [Fine-tuning and deploying a BERTopic model on SageMaker AI with your own scripts and dataset, by extending existing PyTorch containers](https://sagemaker-examples.readthedocs.io/en/latest/advanced_functionality/pytorch_extend_container_train_deploy_bertopic/BERTtopic_extending_container.html).

You can also use prebuilt containers to deploy your custom models or models that have been trained in a framework other than SageMaker AI. For an overview of the process, see [Bring Your Own Pretrained MXNet or TensorFlow Models into Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/bring-your-own-pre-trained-mxnet-or-tensorflow-models-into-amazon-sagemaker/). This tutorial covers bringing the trained model artifacts into SageMaker AI and hosting them at an endpoint.