# Develop Algorithms and Models in

Amazon SageMaker AI

Before you can create algorithm and model package resources to use in Amazon SageMaker AI or list
on AWS Marketplace, you have to develop them and package them in Docker containers.

###### Note

When algorithms and model packages are created for listing on AWS Marketplace, SageMaker AI
scans the containers for security vulnerabilities on supported operating systems.

Only the following operating system versions are supported:

- Debian: 6.0, 7, 8, 9, 10
- Ubuntu: 12.04, 12.10, 13.04, 14.04, 14.10, 15.04, 15.10, 16.04, 16.10, 17.04, 17.10, 18.04, 18.10
- CentOS: 5, 6, 7
- Oracle Linux: 5, 6, 7
- Alpine: 3.3, 3.4, 3.5
- Amazon Linux

###### Topics

- [Develop
  Algorithms in SageMaker AI](#sagmeaker-mkt-develop-algo "#sagmeaker-mkt-develop-algo")
- [Develop Models in SageMaker AI](#sagemaker-mkt-develop-model "#sagemaker-mkt-develop-model")

## Develop

Algorithms in SageMaker AI

An algorithm should be packaged as a docker container and stored in Amazon ECR to
use it in SageMaker AI. The Docker container contains the training code used to run training jobs and, optionally, the
inference code used to get inferences from models trained by using the
algorithm.

For information about developing algorithms in SageMaker AI and packaging them as
containers, see [Docker containers for training and deploying models](docker-containers.md "docker-containers.md"). For a complete example of how to create
an algorithm container, see the sample notebook at [https://sagemaker-examples.readthedocs.io/en/latest/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.html](https://sagemaker-examples.readthedocs.io/en/latest/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.html "https://sagemaker-examples.readthedocs.io/en/latest/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.html").
You can also find the sample notebook in a SageMaker notebook instance. The notebook
is in the **Advanced Functionality** section, and is named
`scikit_bring_your_own.ipynb`.

Always thoroughly test your algorithms before you create algorithm resources
to publish on AWS Marketplace.

###### Note

When a buyer subscribes to your containerized product, the Docker
containers run in an isolated (internet-free) environment. When you create
your containers, do not rely on making outgoing calls over the internet.
Calls to AWS services are also not allowed.

## Develop Models in SageMaker AI

A deployable model in SageMaker AI consists of inference code, model artifacts, an
IAM role that is used to access resources, and other information required to
deploy the model in SageMaker AI. Model artifacts are the results of training a model by
using a machine learning algorithm. The inference code must be packaged in a
Docker container and stored in Amazon ECR. You can either package the model artifacts
in the same container as the inference code, or store them in Amazon S3.

You create a model by running a training job in SageMaker AI, or by training a machine
learning algorithm outside of SageMaker AI. If you run a training job in SageMaker AI, the
resulting model artifacts are available in the `ModelArtifacts` field
in the response to a call to the [DescribeTrainingJob](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md") operation. For information about how to develop
a SageMaker AI model container, see [Containers with custom inference code](your-algorithms-inference-main.md "your-algorithms-inference-main.md"). For a complete example of
how to create a model container from a model trained outside of SageMaker AI, see the
sample notebook at [https://sagemaker-examples.readthedocs.io/en/latest/advanced_functionality/xgboost_bring_your_own_model/xgboost_bring_your_own_model.html](https://sagemaker-examples.readthedocs.io/en/latest/advanced_functionality/xgboost_bring_your_own_model/xgboost_bring_your_own_model.html "https://sagemaker-examples.readthedocs.io/en/latest/advanced_functionality/xgboost_bring_your_own_model/xgboost_bring_your_own_model.html").

Always thoroughly test your models before you create model packages to publish
on AWS Marketplace.

###### Note

When a buyer subscribes to your containerized product, the Docker
containers run in an isolated (internet-free) environment. When you create
your containers, do not rely on making outgoing calls over the internet.
Calls to AWS services are also not allowed.
