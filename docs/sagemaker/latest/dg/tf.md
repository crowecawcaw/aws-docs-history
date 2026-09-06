

# Resources for using TensorFlow with Amazon SageMaker AI
<a name="tf"></a>

You can use Amazon SageMaker AI to train and deploy a model using custom TensorFlow code. The SageMaker AI Python SDK TensorFlow ModelTrainers and models and the SageMaker AI open-source TensorFlow containers can help. Use the following list of resources to find more information, based on which version of TensorFlow you're using and what you want to do.

## TensorFlow Version 1.11 and Later
<a name="tf-script-mode"></a>

For TensorFlow versions 1.11 and later, the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable) supports script mode training scripts.

### What do you want to do?
<a name="tf-intent"></a>

I want to train a custom TensorFlow model in SageMaker AI.  
For a sample Jupyter notebook, see [TensorFlow script mode training and serving](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-python-sdk/tensorflow_script_mode_training_and_serving/tensorflow_script_mode_training_and_serving.html).  
For documentation, see [Train a Model with TensorFlow](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html).

I have a TensorFlow model that I trained in SageMaker AI, and I want to deploy it to a hosted endpoint.  
For more information, see [Deploy TensorFlow Serving models](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html).

I have a TensorFlow model that I trained outside of SageMaker AI, and I want to deploy it to a SageMaker AI endpoint.  
For more information, see [Deploying directly from model artifacts](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html).

I want to see the API documentation for [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable) TensorFlow classes.  
For more information, see [TensorFlow ModelTrainer](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html).

I want to find the SageMaker AI TensorFlow container repository.  
For more information, see [SageMaker TensorFlow Container GitHub repository](https://github.com/aws/sagemaker-tensorflow-container).

I want to find information about TensorFlow versions supported by AWS Deep Learning Containers.  
For more information, see [Available Deep Learning Container Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md).

 For general information about writing TensorFlow script mode training scripts and using TensorFlow script mode ModelTrainers and models with SageMaker AI, see [Using TensorFlow with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html).

## TensorFlow Legacy Mode for Versions 1.11 and Earlier
<a name="tf-legacy-mode"></a>

The [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable) provides a legacy mode that supports TensorFlow versions 1.11 and earlier. Use legacy mode TensorFlow training scripts to run TensorFlow jobs in SageMaker AI if:
+ You have existing legacy mode scripts that you do not want to convert to script mode.
+ You want to use a TensorFlow version earlier than 1.11.

For information about writing legacy mode TensorFlow scripts to use with the SageMaker AI Python SDK, see [TensorFlow SageMaker ModelTrainers and Models](https://github.com/aws/sagemaker-python-sdk/tree/v1.12.0/src/sagemaker/tensorflow#tensorflow-sagemaker-estimators-and-models).