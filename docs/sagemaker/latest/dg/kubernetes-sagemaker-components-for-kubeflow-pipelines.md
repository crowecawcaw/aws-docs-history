# SageMaker AI Components for

Kubeflow Pipelines

With SageMaker AI components for Kubeflow Pipelines, you can create and monitor native SageMaker AI
training, tuning, endpoint deployment, and batch transform jobs from your Kubeflow Pipelines. By
running Kubeflow Pipeline jobs on SageMaker AI, you move data processing and training jobs from the
Kubernetes cluster to SageMaker AI's machine learning-optimized managed service. This document assumes
prior knowledge of Kubernetes and Kubeflow.

###### Contents

- [What are Kubeflow Pipelines?](#what-is-kubeflow-pipelines "#what-is-kubeflow-pipelines")
- [What are Kubeflow Pipeline components?](#kubeflow-pipeline-components "#kubeflow-pipeline-components")
- [Why use SageMaker AI Components for Kubeflow
  Pipelines?](#why-use-sagemaker-components "#why-use-sagemaker-components")
- [SageMaker AI Components for Kubeflow
  Pipelines versions](#sagemaker-components-versions "#sagemaker-components-versions")
- [List of SageMaker AI Components for Kubeflow
  Pipelines](#sagemaker-components-list "#sagemaker-components-list")
- [IAM permissions](#iam-permissions "#iam-permissions")
- [Converting pipelines to use
  SageMaker AI](#converting-pipelines-to-use-amazon-sagemaker "#converting-pipelines-to-use-amazon-sagemaker")
- [Install Kubeflow Pipelines](kubernetes-sagemaker-components-install.md "kubernetes-sagemaker-components-install.md")
- [Use SageMaker AI components](kubernetes-sagemaker-components-tutorials.md "kubernetes-sagemaker-components-tutorials.md")

## What are Kubeflow Pipelines?

Kubeflow Pipelines (KFP) is a platform for building and deploying portable, scalable
machine learning (ML) workflows based on Docker containers. The Kubeflow Pipelines platform
consists of the following:

- A user interface (UI) for managing and tracking experiments, jobs, and runs.
- An engine (Argo) for scheduling multi-step ML workflows.
- An SDK for defining and manipulating pipelines and components.
- Notebooks for interacting with the system using the SDK.

A pipeline is a description of an ML workflow expressed as a [directed acyclic
graph](https://www.kubeflow.org/docs/pipelines/concepts/graph/ "https://www.kubeflow.org/docs/pipelines/concepts/graph/"). Every step in the workflow is expressed as a Kubeflow Pipeline [component](https://www.kubeflow.org/docs/pipelines/overview/concepts/component/ "https://www.kubeflow.org/docs/pipelines/overview/concepts/component/"), which is a AWS SDK for Python (Boto3) module.

For more information on Kubeflow Pipelines, see the [Kubeflow Pipelines documentation](https://www.kubeflow.org/docs/pipelines/ "https://www.kubeflow.org/docs/pipelines/").

## What are Kubeflow Pipeline components?

A Kubeflow Pipeline component is a set of code used to execute one step of a Kubeflow
pipeline. Components are represented by a Python module built into a Docker image. When the
pipeline runs, the component's container is instantiated on one of the worker nodes on the
Kubernetes cluster running Kubeflow, and your logic is executed. Pipeline components can read
outputs from the previous components and create outputs that the next component in the
pipeline can consume. These components make it fast and easy to write pipelines for
experimentation and production environments without having to interact with the underlying
Kubernetes infrastructure.

You can use SageMaker AI Components in your Kubeflow pipeline. Rather than encapsulating your
logic in a custom container, you simply load the components and describe your pipeline using
the Kubeflow Pipelines SDK. When the pipeline runs, your instructions are translated into a
SageMaker AI job or deployment. The workload then runs on the fully managed infrastructure of SageMaker AI.

## Why use SageMaker AI Components for Kubeflow

Pipelines?

SageMaker AI Components for Kubeflow Pipelines offer an alternative to launching your
compute-intensive jobs from SageMaker AI. The components integrate SageMaker AI with the portability and
orchestration of Kubeflow Pipelines. Using the SageMaker AI Components for Kubeflow Pipelines, you can
create and monitor your SageMaker AI resources as part of a Kubeflow Pipelines workflow. Each of the
jobs in your pipelines runs on SageMaker AI instead of the local Kubernetes cluster allowing you to
take advantage of key SageMaker AI features such as data labeling, large-scale hyperparameter tuning
and distributed training jobs, or one-click secure and scalable model deployment. The job
parameters, status, logs, and outputs from SageMaker AI are still accessible from the Kubeflow
Pipelines UI.

The SageMaker AI components integrate key SageMaker AI features into your ML workflows from preparing
data, to building, training, and deploying ML models. You can create a Kubeflow Pipeline built
entirely using these components, or integrate individual components into your workflow as
needed. The components are available in one or two versions. Each version of a component
leverages a different backend. For more information on those versions, see [SageMaker AI Components for Kubeflow
Pipelines versions](#sagemaker-components-versions "#sagemaker-components-versions").

There is no additional charge for using SageMaker AI Components for Kubeflow Pipelines. You incur
charges for any SageMaker AI resources you use through these components.

## SageMaker AI Components for Kubeflow

Pipelines versions

SageMaker AI Components for Kubeflow Pipelines come in two versions. Each version leverages a
different backend to create and manage resources on SageMaker AI.

- The SageMaker AI Components for Kubeflow Pipelines version 1 (v1.x or below) use **[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html")** (AWS SDK for Python (Boto3)) as backend.
- The version 2 (v2.0.0-alpha2 and above) of SageMaker AI Components for Kubeflow Pipelines use
  [SageMaker AI Operator
  for Kubernetes (ACK)](https://github.com/aws-controllers-k8s/sagemaker-controller "https://github.com/aws-controllers-k8s/sagemaker-controller").

AWS introduced [ACK](https://aws-controllers-k8s.github.io/community/ "https://aws-controllers-k8s.github.io/community/") to facilitate a Kubernetes-native way of managing AWS Cloud resources.
ACK includes a set of AWS service-specific controllers, one of which is the SageMaker AI
controller. The SageMaker AI controller makes it easier for machine learning developers and data
scientists using Kubernetes as their control plane to train, tune, and deploy machine
learning (ML) models in SageMaker AI. For more information, see [SageMaker AI Operators for Kubernetes](https://aws-controllers-k8s.github.io/community/docs/tutorials/sagemaker-example/ "https://aws-controllers-k8s.github.io/community/docs/tutorials/sagemaker-example/")

Both versions of the SageMaker AI Components for Kubeflow Pipelines are supported. However, the
version 2 provides some additional advantages. In particular, it offers:

1. A consistent experience to manage your SageMaker AI resources from any application; whether
   you are using Kubeflow pipelines, or Kubernetes CLI (`kubectl`) or other
   Kubeflow applications such as Notebooks.
2. The flexibility to manage and monitor your SageMaker AI resources outside of the Kubeflow
   pipeline workflow.
3. Zero setup time to use the SageMaker AI components if you deployed the full [Kubeflow on AWS](https://awslabs.github.io/kubeflow-manifests/docs/about/ "https://awslabs.github.io/kubeflow-manifests/docs/about/")
   release since the SageMaker AI Operator is part of its deployment.

## List of SageMaker AI Components for Kubeflow

Pipelines

The following is a list of all SageMaker AI Components for Kubeflow Pipelines and their available
versions. Alternatively, you can find all [SageMaker AI Components for Kubeflow Pipelines in GitHub](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker#versioning "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker#versioning").

###### Note

We encourage users to utilize Version 2 of a SageMaker AI component wherever it is
available.

- **Ground Truth**

The Ground Truth component enables you to submit SageMaker AI Ground Truth labeling jobs directly from a
Kubeflow Pipelines workflow.

| Version 1 of the component                                                                                                                                                                                                                            | Version 2 of the component |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [SageMaker AI Ground Truth Kubeflow Pipelines component version 1](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/ground_truth "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/ground_truth") | X                          |

- **Workteam**

The Workteam component enables you to create SageMaker AI private workteam jobs directly
from a Kubeflow Pipelines workflow.

| Version 1 of the component                                                                                                                                                                                                                                  | Version 2 of the component |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [SageMaker AI create private workteam Kubeflow Pipelines component version<br>1](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/workteam "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/workteam") | X                          |

- **Processing**

The Processing component enables you to submit processing jobs to SageMaker AI directly
from a Kubeflow Pipelines workflow.

| Version 1 of the component                                                                                                                                                                                                            | Version 2 of the component |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [SageMaker Processing Kubeflow Pipeline component version 1](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/process "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/process") | X                          |

- **Training**

The Training component allows you to submit SageMaker Training jobs directly from a
Kubeflow Pipelines workflow.

| Version 1 of the component                                                                                                                                                                                                       | Version 2 of the component                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SageMaker Training Kubeflow Pipelines component version 1](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/train "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/train") | [SageMaker Training Kubeflow Pipelines component version 2](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/TrainingJob "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/TrainingJob") |

- **Hyperparameter Optimization**

The Hyperparameter Optimization component enables you to submit hyperparameter
tuning jobs to SageMaker AI directly from a Kubeflow Pipelines workflow.

| Version 1 of the component                                                                                                                                                                                                                                                               | Version 2 of the component |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [SageMaker AI hyperparameter optimization Kubeflow Pipeline component version<br>1](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/hyperparameter_tuning "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/hyperparameter_tuning") | X                          |

- **Hosting Deploy**

The Hosting components allow you to deploy a model using SageMaker AI hosting services
from a Kubeflow Pipelines workflow.

| Version 1 of the component                                                                                                                                                                                                                                            | Version 2 of the component                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SageMaker AI Hosting Services<br>• Create Endpoint Kubeflow Pipeline component<br>version 1](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/deploy "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/deploy"). | Version 2 of the Hosting components consists of the three sub-components<br>needed to create a hosting deployment on SageMaker AI.<br>+ A [SageMaker AI Model Kubeflow Pipelines component version 2](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/Modelv2 "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/Modelv2") responsible<br>for the model artifacts and the model image registry path that contains<br>the inference code.<br>+ A [SageMaker AI Endpoint Configuration Kubeflow Pipelines component version<br>2](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/EndpointConfig "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/EndpointConfig") responsible for defining the configuration of the endpoint<br>such as the instance type, models, number of instances, and serverless<br>inference option.<br>+ A [SageMaker AI Endpoint Kubeflow Pipelines component version 2](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/Endpoint "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/Endpoint")<br>responsible for creating or updating the endpoint on SageMaker AI as specified<br>in the endpoint configuration. |

- **Batch Transform**

The Batch Transform component allows you to run inference jobs for an entire
dataset in SageMaker AI from a Kubeflow Pipelines workflow.

| Version 1 of the component                                                                                                                                                                                                                                    | Version 2 of the component |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [SageMaker AI Batch Transform Kubeflow Pipeline component version 1](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/batch_transform "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/batch_transform") | X                          |

- **Model Monitor**

The Model Monitor components allow you to monitor the quality of SageMaker AI machine
learning models in production from a Kubeflow Pipelines workflow.

| Version 1 of the component | Version 2 of the component                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X                          | The Model Monitor components consist of four sub-components for<br>monitoring drift in a model.<br>+ A [SageMaker AI Data Quality Job Definition Kubeflow Pipelines component version<br>2](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/DataQualityJobDefinition "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/DataQualityJobDefinition") responsible for monitoring drift in data quality.<br>+ A [SageMaker AI Model Quality Job Definition Kubeflow Pipelines component<br>version 2](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/ModelQualityJobDefinition "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/ModelQualityJobDefinition") responsible for monitoring drift in model quality<br>metrics.<br>+ A [SageMaker AI Model Bias Job Definition Kubeflow Pipelines component version<br>2](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/ModelBiasJobDefinition "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/ModelBiasJobDefinition") responsible for monitoring bias in a model's<br>predictions.<br>+ A [SageMaker AI Model Explainability Job Definition Kubeflow Pipelines component<br>version 2](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/ModelExplainabilityJobDefinition "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/ModelExplainabilityJobDefinition") responsible for monitoring drift in feature<br>attribution.<br>Additionally, for on-schedule monitoring at a specified frequency, a<br>fifth component, [SageMaker AI Monitoring Schedule Kubeflow Pipelines component version 2](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/MonitoringSchedule "https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/MonitoringSchedule"),<br>is responsible for monitoring the data collected from a real-time endpoint<br>on a schedule.<br>For more information on Amazon SageMaker Model Monitor, see [Data and model quality monitoring with Amazon SageMaker Model Monitor](model-monitor.md "model-monitor.md"). |

## IAM permissions

Deploying Kubeflow Pipelines with SageMaker AI components requires the following three layers of
authentication:

- An IAM role granting your gateway node (which can be your local machine or a remote
  instance) access to the Amazon Elastic Kubernetes Service (Amazon EKS) cluster.

The user accessing the gateway node assumes this role to:

    + Create an Amazon EKS cluster and install KFP
    + Create IAM roles
    + Create Amazon S3 buckets for your sample input data

The role requires the following permissions:

    + CloudWatchLogsFullAccess
    + [AWSCloudFormationFullAccess](https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAWSCloudFormationFullAccess "https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAWSCloudFormationFullAccess")
    + IAMFullAccess
    + AmazonS3FullAccess
    + AmazonEC2FullAccess
    + AmazonEKSAdminPolicy (Create this policy using the schema from [Amazon EKS Identity-Based Policy Examples](../../../eks/latest/userguide/security_iam_id-based-policy-examples.md "../../../eks/latest/userguide/security_iam_id-based-policy-examples.md"))

- A Kubernetes IAM execution role assumed by Kubernetes pipeline pods (**kfp-example-pod-role**) or the SageMaker AI Operator for Kubernetes
  controller pod to access SageMaker AI. This role is used to create and monitor SageMaker AI jobs from
  Kubernetes.

The role requires the following permission:

    + AmazonSageMakerFullAccess

You can limit permissions to the KFP and controller pods by creating and attaching
your own custom policy.

- A SageMaker AI IAM execution role assumed by SageMaker AI jobs to access AWS resources such as
  Amazon S3 or Amazon ECR (**kfp-example-sagemaker-execution-role**).

SageMaker AI jobs use this role to:

    + Access SageMaker AI resources
    + Input Data from Amazon S3
    + Store your output model to Amazon S3

The role requires the following permissions:

    + AmazonSageMakerFullAccess
    + AmazonS3FullAccess

## Converting pipelines to use

SageMaker AI

You can convert an existing pipeline to use SageMaker AI by porting your generic Python [processing
containers](amazon-sagemaker-containers.md "amazon-sagemaker-containers.md") and [training containers](your-algorithms-training-algo.md "your-algorithms-training-algo.md"). If
you are using SageMaker AI for inference, you also need to attach IAM permissions to your cluster
and convert an artifact to a model.
