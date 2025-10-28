# Train and deploy models with HyperPod CLI and SDK

Amazon SageMaker HyperPod helps you train and deploy machine learning models at scale. The AWS HyperPod CLI is a unified command-line interface
that simplifies machine learning (ML) workflows on AWS. It abstracts infrastructure complexities and provides a streamlined experience for submitting,
monitoring, and managing ML training jobs. The CLI is designed specifically for data scientists and ML engineers who want to focus on
model development rather than infrastructure management. This topic walks you through three key scenarios:
training a PyTorch model, deploying a custom model using trained artifacts, and deploying a JumpStart model.
Designed for first-time users, this concise tutorial ensures you can set up, train, and deploy models effortlessly using either the HyperPod CLI or the SDK.
The handshake process between training and inference helps you manage model artifacts effectively.

## Prerequisites

Before you begin using Amazon SageMaker HyperPod, make sure you have:

- An AWS account with access to Amazon SageMaker HyperPod
- Python 3.9, 3.10, or 3.11 installed
- AWS CLI configured with appropriate credentials.

## Install the HyperPod CLI and SDK

Install the required package to access the CLI and SDK:

```
pip install sagemaker-hyperpod
```

This command sets up the tools needed to interact with HyperPod clusters.

## Configure your cluster context

HyperPod operates on clusters optimized for machine learning. Start by listing available clusters to select one for your tasks.

1. List all available clusters:

```
hyp list-cluster
```

2. Choose and set your active cluster:

```
hyp set-cluster-context your-eks-cluster-name

```

3. Verify the configuration:

```
hyp get-cluster-context
```

###### Note

All subsequent commands target the cluster you've set as your context.

## Choose your scenario

For detailed instructions on each scenario, click on the topics below:

###### Topics

- [Train a PyTorch model](train-models-with-hyperpod.md "train-models-with-hyperpod.md")
- [Deploy a custom model](deploy-trained-model.md "deploy-trained-model.md")
- [Deploy a JumpStart model](deploy-jumpstart-model.md "deploy-jumpstart-model.md")
