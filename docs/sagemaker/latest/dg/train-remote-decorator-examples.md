# Example notebooks

You can transform a training code in an existing workspace environment and any
associated data processing code and datasets into a SageMaker training job. The following
notebooks show you how to customize your environment, job settings, and more for an
image classification problem, using the XGBoost algorithm and Hugging Face.

The [quick_start notebook](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-remote-function/quick_start/quick_start.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-remote-function/quick_start/quick_start.ipynb") contains the following code examples:

- How to customize your job settings with a configuration file.
- How to invoke Python functions as jobs, asynchronously.
- How to customize the job runtime environment by bringing in additional
  dependencies.
- How to use local dependencies with the @remote function method.
  The following notebooks provide additional code examples for different ML problems
  types and implementations.

- To see code examples to use the @remote decorator for an image classification
  problem, open the [pytorch_mnist.ipynb](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-remote-function/pytorch_mnist_sample_notebook "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-remote-function/pytorch_mnist_sample_notebook") notebook. This classification problem
  recognizes handwritten digits using the Modified National Institute of Standards
  and Technology (MNIST) sample dataset.
- To see code examples for using the @remote decorator for the previous image
  classification problem with a script, see the Pytorch MNIST sample script,
  [train.py](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-remote-function/pytorch_mnist_sample_script "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-remote-function/pytorch_mnist_sample_script").
- To see how the XGBoost algorithm implemented with an @remote decorator: Open
  the [xgboost_abalone.ipynb](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-remote-function/xgboost_abalone "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-remote-function/xgboost_abalone") notebook.
- To see how Hugging Face is integrated with an @remote decorator: Open the
  [huggingface.ipynb](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-remote-function/huggingface_text_classification "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-remote-function/huggingface_text_classification") notebook.
