# Resources for using Hugging Face with Amazon SageMaker AI

Amazon SageMaker AI lets customers train, fine-tune, and run inference using Hugging Face models for
Natural Language Processing (NLP) on SageMaker AI. You can use Hugging Face for both training and
inference. The following section provides information on Hugging Face models and includes
reference material you can use to learn how to use Hugging Face with SageMaker AI.

This functionality is available through the development of Hugging Face [AWS Deep Learning Containers](../../../deep-learning-containers/latest/devguide/what-is-dlc.md "../../../deep-learning-containers/latest/devguide/what-is-dlc.md"). These containers include Hugging Face Transformers, Tokenizers and the
Datasets library, which allows you to use these resources for your training and inference jobs.
For a list of the available Deep Learning Containers images, see [Available Deep Learning Containers Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md"). These Deep Learning Containers images are maintained and regularly updated
with security patches.

To use the Hugging Face Deep Learning Containers with the SageMaker Python SDK for training, see the [Hugging
Face SageMaker AI Estimator](https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/index.html "https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/index.html"). With the Hugging Face Estimator, you can use the Hugging Face
models as you would any other SageMaker AI Estimator. However, using the SageMaker Python SDK is optional.
You can also orchestrate your use of the Hugging Face Deep Learning Containers with the AWS CLI and
AWS SDK for Python (Boto3).

For more information on Hugging Face and the models available in it, see the [Hugging Face documentation](https://huggingface.co/ "https://huggingface.co/").

## Training

To run training, use any of the thousands of models available in Hugging Face and
fine-tune them for your use case with additional training. With SageMaker AI, you can use standard
training or take advantage of [SageMaker AI Distributed Data and Model Parallel
training](distributed-training.md "distributed-training.md").

Like other SageMaker training jobs using custom code, you can capture your own metrics by
passing a metrics definition to the SageMaker Python SDK. For an example, see [Defining Training
Metrics (SageMaker Python SDK)](training-metrics.md#define-train-metrics-sdk "training-metrics.md#define-train-metrics-sdk") . You can access the captured metrics using [CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
and as a Pandas `DataFrame` using the [TrainingJobAnalytics](https://sagemaker.readthedocs.io/en/stable/api/training/analytics.html#sagemaker.analytics.TrainingJobAnalytics "https://sagemaker.readthedocs.io/en/stable/api/training/analytics.html#sagemaker.analytics.TrainingJobAnalytics") method. After your model is trained and fine-tuned, you can
use it like any other model to run inference jobs.

### How to run training with the Hugging Face

estimator

You can implement the Hugging Face Estimator for training jobs using the SageMaker AI Python
SDK. The SageMaker Python SDK is an open source library for training and deploying machine
learning models on SageMaker AI. For more information on the Hugging Face Estimator, see the [SageMaker AI
Python SDK documentation.](https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/index.html "https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/index.html")

With the SageMaker Python SDK, you can run training jobs using the Hugging Face Estimator in
the following environments:

- [Amazon SageMaker Studio Classic](studio.md "studio.md"): Studio Classic is the first fully integrated development
  environment (IDE) for machine learning (ML). Studio Classic provides a single, web-based
  visual interface where you can perform all ML development steps required to:

      + prepare
      + build
      + train and tune
      + deploy and manage models

  For information on using Jupyter Notebooks in Studio Classic, see [Use Amazon SageMaker Studio Classic Notebooks](notebooks.md "notebooks.md").

- [SageMaker
  Notebook Instances](nbi.md "nbi.md"): An Amazon SageMaker notebook instance is a machine learning (ML)
  compute instance running the Jupyter Notebook App. This app lets you run Jupyter
  Notebooks in your notebook instance to:
  - prepare and process data
  - write code to train models
  - deploy models to SageMaker AI hosting
  - test or validate your models without SageMaker Studio features like Debugger, Model
    Monitoring, and a web-based IDE

- Locally: If you have connectivity to AWS and have appropriate SageMaker AI permissions,
  you can use the SageMaker Python SDK locally. With local use, you can launch remote training
  and inference jobs for Hugging Face in SageMaker AI on AWS. This works on your local machine,
  as well as other AWS services with a connected SageMaker Python SDK and appropriate
  permissions.

## Inference

For inference, you can use your trained Hugging Face model or one of the pretrained
Hugging Face models to deploy an inference job with SageMaker AI. With this collaboration, you only
need one line of code to deploy both your trained models and pre-trained models with SageMaker AI. You
can also run inference jobs without having to write any custom inference code. With custom
inference code, you can customize the inference logic by providing your own Python
script.

### How to deploy an inference job using the

Hugging Face Deep Learning Containers

You have two options for running inference with SageMaker AI. You can run inference using a
model that you trained, or deploy a pre-trained Hugging Face model.

- **Run inference with your trained model:** You have two
  options for running inference with your own trained model:

      + Run inference with a model that you trained using an existing Hugging Face model
       with the SageMaker AI Hugging Face Deep Learning Containers.
      + Bring your own existing Hugging Face model and deploy it using SageMaker AI.

  When you run inference with a model that you trained with the SageMaker AI Hugging Face
  Estimator, you can deploy the model immediately after training completes. You can also
  upload the trained model to an Amazon S3 bucket and ingest it when running inference later.

If you bring your own existing Hugging Face model, you must upload the trained model
to an Amazon S3 bucket. You then ingest that bucket when running inference as shown in [Deploy your Hugging Face Transformers for inference example](https://github.com/huggingface/notebooks/blob/main/sagemaker/10_deploy_model_from_s3/deploy_transformer_model_from_s3.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/10_deploy_model_from_s3/deploy_transformer_model_from_s3.ipynb").

- **Run inference with a pre-trained HuggingFace model:** You can use one of the thousands of pre-trained Hugging Face models to run
  your inference jobs with no additional training needed. To run inference, select the
  pre-trained model from the list of [Hugging
  Face models](https://huggingface.co/models "https://huggingface.co/models"), as outlined in [Deploy pre-trained Hugging Face Transformers for inference example](https://github.com/huggingface/notebooks/blob/main/sagemaker/11_deploy_model_from_hf_hub/deploy_transformer_model_from_hf_hub.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/11_deploy_model_from_hf_hub/deploy_transformer_model_from_hf_hub.ipynb").

## What do you want to do?

The following notebooks in the Hugging Face notebooks repository show how to use the
Hugging Face Deep Learning Containers with SageMaker AI in various use cases.

I want to train and deploy a text classification model using Hugging Face in SageMaker AI with
PyTorch.

For a sample Jupyter Notebook, see the [PyTorch Getting Started Demo](https://github.com/huggingface/notebooks/blob/main/sagemaker/01_getting_started_pytorch/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/01_getting_started_pytorch/sagemaker-notebook.ipynb").

I want to train and deploy a text classification model using Hugging Face in SageMaker AI with
TensorFlow.

For a sample Jupyter Notebook, see the [TensorFlow Getting Started example](https://github.com/huggingface/notebooks/blob/main/sagemaker/02_getting_started_tensorflow/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/02_getting_started_tensorflow/sagemaker-notebook.ipynb").

I want to run distributed training with data parallelism using Hugging Face and SageMaker AI
Distributed.

For a sample Jupyter Notebook, see the [Distributed Training example](https://github.com/huggingface/notebooks/blob/main/sagemaker/03_distributed_training_data_parallelism/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/03_distributed_training_data_parallelism/sagemaker-notebook.ipynb").

I want to run distributed training with model parallelism using Hugging Face and SageMaker AI
Distributed.

For a sample Jupyter Notebook, see the [Model Parallelism example](https://github.com/huggingface/notebooks/blob/main/sagemaker/04_distributed_training_model_parallelism/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/04_distributed_training_model_parallelism/sagemaker-notebook.ipynb").

I want to use a spot instance to train and deploy a model using Hugging Face in
SageMaker AI.

For a sample Jupyter Notebook, see the [Spot Instances example](https://github.com/huggingface/notebooks/blob/main/sagemaker/05_spot_instances/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/05_spot_instances/sagemaker-notebook.ipynb").

I want to capture custom metrics and use SageMaker AI Checkpointing when training a text
classification model using Hugging Face in SageMaker AI.

For a sample Jupyter Notebook, see the [Training with Custom Metrics example](https://github.com/huggingface/notebooks/blob/main/sagemaker/06_sagemaker_metrics/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/06_sagemaker_metrics/sagemaker-notebook.ipynb").

I want to train a distributed question-answering TensorFlow model using Hugging Face
in SageMaker AI.

For a sample Jupyter Notebook, see the [Distributed TensorFlow Training example](https://github.com/huggingface/notebooks/blob/main/sagemaker/07_tensorflow_distributed_training_data_parallelism/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/07_tensorflow_distributed_training_data_parallelism/sagemaker-notebook.ipynb").

I want to train a distributed summarization model using Hugging Face in SageMaker AI.

For a sample Jupyter Notebook, see the [Distributed Summarization Training example](https://github.com/huggingface/notebooks/blob/main/sagemaker/08_distributed_summarization_bart_t5/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/08_distributed_summarization_bart_t5/sagemaker-notebook.ipynb").

I want to train an image classification model using Hugging Face in SageMaker AI.

For a sample Jupyter Notebook, see the [Vision Transformer Training example](https://github.com/huggingface/notebooks/blob/main/sagemaker/09_image_classification_vision_transformer/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/09_image_classification_vision_transformer/sagemaker-notebook.ipynb").

I want to deploy my trained Hugging Face model in SageMaker AI.

For a sample Jupyter Notebook, see the [Deploy your Hugging Face Transformers for inference example](https://github.com/huggingface/notebooks/blob/main/sagemaker/10_deploy_model_from_s3/deploy_transformer_model_from_s3.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/10_deploy_model_from_s3/deploy_transformer_model_from_s3.ipynb").

I want to deploy a pre-trained Hugging Face model in SageMaker AI.

For a sample Jupyter Notebook, see the [Deploy pre-trained Hugging Face Transformers for inference example](https://github.com/huggingface/notebooks/blob/main/sagemaker/11_deploy_model_from_hf_hub/deploy_transformer_model_from_hf_hub.ipynb "https://github.com/huggingface/notebooks/blob/main/sagemaker/11_deploy_model_from_hf_hub/deploy_transformer_model_from_hf_hub.ipynb").
