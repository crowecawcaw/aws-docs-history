# Amazon SageMaker Debugger references

Find more information and references about using Amazon SageMaker Debugger in the following topics.

###### Topics

- [Amazon SageMaker Debugger APIs](#debugger-apis "#debugger-apis")
- [Docker images for Debugger rules](#debugger-docker-images-rules "#debugger-docker-images-rules")
- [Amazon SageMaker Debugger exceptions](#debugger-exceptions "#debugger-exceptions")
- [Distributed training supported by
  Amazon SageMaker Debugger](#debugger-considerations "#debugger-considerations")

## Amazon SageMaker Debugger APIs

Amazon SageMaker Debugger has API operations in several locations that are used to implement its
monitoring and analysis of model training.

Amazon SageMaker Debugger also provides the open source [`sagemaker-debugger` Python SDK](https://github.com/awslabs/sagemaker-debugger/tree/master/smdebug "https://github.com/awslabs/sagemaker-debugger/tree/master/smdebug") that is used to configure
built-in rules, define custom rules, and register hooks to collect output tensor data
from training jobs.

The [Amazon SageMaker AI Python
SDK](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/") is a high-level SDK focused on machine learning experimentation. The SDK
can be used to deploy built-in or custom rules defined with the `SMDebug`
Python library to monitor and analyze these tensors using SageMaker AI estimators.

Debugger has added operations and types to the Amazon SageMaker API that enable the platform to use
Debugger when training a model and to manage the configuration of inputs and outputs.

- [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") and [`UpdateTrainingJob`](../APIReference/API_UpdateTrainingJob.md "../APIReference/API_UpdateTrainingJob.md") use the following Debugger APIs to
  configure tensor collections, rules, rule images, and profiling options:
  - [`CollectionConfiguration`](../APIReference/API_CollectionConfiguration.md "../APIReference/API_CollectionConfiguration.md")
  - [`DebugHookConfig`](../APIReference/API_DebugHookConfig.md "../APIReference/API_DebugHookConfig.md")
  - [`DebugRuleConfiguration`](../APIReference/API_DebugRuleConfiguration.md "../APIReference/API_DebugRuleConfiguration.md")
  - [`TensorBoardOutputConfig`](../APIReference/API_TensorBoardOutputConfig.md "../APIReference/API_TensorBoardOutputConfig.md")
  - [`ProfilerConfig`](../APIReference/API_ProfilerConfig.md "../APIReference/API_ProfilerConfig.md")
  - [`ProfilerRuleConfiguration`](../APIReference/API_ProfilerRuleConfiguration.md "../APIReference/API_ProfilerRuleConfiguration.md")

- [`DescribeTrainingJob`](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md") provides a full description of
  a training job, including the following Debugger configurations and rule
  evaluation statuses:
  - [`DebugHookConfig`](../APIReference/API_DebugHookConfig.md "../APIReference/API_DebugHookConfig.md")
  - [`DebugRuleConfiguration`](../APIReference/API_DebugRuleConfiguration.md "../APIReference/API_DebugRuleConfiguration.md")
  - [`DebugRuleEvaluationStatus`](../APIReference/API_DebugRuleEvaluationStatus.md "../APIReference/API_DebugRuleEvaluationStatus.md")
  - [`ProfilerConfig`](../APIReference/API_ProfilerConfig.md "../APIReference/API_ProfilerConfig.md")
  - [`ProfilerRuleConfiguration`](../APIReference/API_ProfilerRuleConfiguration.md "../APIReference/API_ProfilerRuleConfiguration.md")
  - [`ProfilerRuleEvaluationStatus`](../APIReference/API_ProfilerRuleEvaluationStatus.md "../APIReference/API_ProfilerRuleEvaluationStatus.md")

The rule configuration API operations use the SageMaker Processing functionality when
analyzing a model training. For more information about SageMaker Processing, see [Data transformation
workloads with SageMaker Processing](processing-job.md "processing-job.md").

## Docker images for Debugger rules

Amazon SageMaker AI provides two sets of Docker images for rules: one set for evaluating rules provided
by SageMaker AI (built-in rules) and one set for evaluating custom rules provided in Python source
files.

If you use the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"), you can simply use SageMaker AI high-level Debugger API
operations with SageMaker AI Estimator API operations, without having to manually retrieve the
Debugger Docker images and configure the `ConfigureTrainingJob`API.

If you are not using the SageMaker Python SDK, you have to retrieve a relevant pre-built
container base image for the Debugger rules. Amazon SageMaker Debugger provides pre-built Docker images for
built-in and custom rules, and the images are stored in Amazon Elastic Container Registry (Amazon ECR). To pull an image
from an Amazon ECR repository (or to push an image to one), use the full name registry URL of the
image using the `CreateTrainingJob` API. SageMaker AI uses the following URL patterns for
the Debugger rule container image registry address.

```
<account_id>.dkr.ecr.<Region>.amazonaws.com/<ECR repository name>:<tag>
```

For the account ID in each AWS Region, the Amazon ECR repository name, and the tag value, see the
following topics.

###### Topics

- [Amazon SageMaker Debugger image URIs for built-in rule
  evaluators](#debuger-built-in-registry-ids "#debuger-built-in-registry-ids")
- [Amazon SageMaker Debugger image URIs for custom rule
  evaluators](#debuger-custom-rule-registry-ids "#debuger-custom-rule-registry-ids")

### Amazon SageMaker Debugger image URIs for built-in rule

evaluators

Use the following values for the components of the registry URLs for the images that
provide built-in rules for Amazon SageMaker Debugger. For account IDs, see the following table.

**ECR Repository Name**: sagemaker-debugger-rules

**Tag**: latest

**Example of a full registry URL**:

`904829902805.dkr.ecr.ap-south-1.amazonaws.com/sagemaker-debugger-rules:latest`

Account IDs for Built-in Rules Container Images by AWS Region

| Region           | account_id   |
| ---------------- | ------------ |
| `af-south-1`     | 314341159256 |
| `ap-east-1`      | 199566480951 |
| `ap-northeast-1` | 430734990657 |
| `ap-northeast-2` | 578805364391 |
| `ap-south-1`     | 904829902805 |
| `ap-southeast-1` | 972752614525 |
| `ap-southeast-2` | 184798709955 |
| `ca-central-1`   | 519511493484 |
| `cn-north-1`     | 618459771430 |
| `cn-northwest-1` | 658757709296 |
| `eu-central-1`   | 482524230118 |
| `eu-north-1`     | 314864569078 |
| `eu-south-1`     | 563282790590 |
| `eu-west-1`      | 929884845733 |
| `eu-west-2`      | 250201462417 |
| `eu-west-3`      | 447278800020 |
| `me-south-1`     | 986000313247 |
| `sa-east-1`      | 818342061345 |
| `us-east-1`      | 503895931360 |
| `us-east-2`      | 915447279597 |
| `us-west-1`      | 685455198987 |
| `us-west-2`      | 895741380848 |
| `us-gov-west-1`  | 515509971035 |

### Amazon SageMaker Debugger image URIs for custom rule

evaluators

Use the following values for the components of the registry URL for the images that
provide custom rule evaluators for Amazon SageMaker Debugger. For account IDs, see the following
table.

**ECR Repository Name**:
sagemaker-debugger-rule-evaluator

**Tag**: latest

**Example of a full registry URL**:

`552407032007.dkr.ecr.ap-south-1.amazonaws.com/sagemaker-debugger-rule-evaluator:latest`

Account IDs for Custom Rules Container Images by AWS Region

| Region           | account_id   |
| ---------------- | ------------ |
| `af-south-1`     | 515950693465 |
| `ap-east-1`      | 645844755771 |
| `ap-northeast-1` | 670969264625 |
| `ap-northeast-2` | 326368420253 |
| `ap-south-1`     | 552407032007 |
| `ap-southeast-1` | 631532610101 |
| `ap-southeast-2` | 445670767460 |
| `ca-central-1`   | 105842248657 |
| `cn-north-1`     | 617202126805 |
| `cn-northwest-1` | 658559488188 |
| `eu-central-1`   | 691764027602 |
| `eu-north-1`     | 091235270104 |
| `eu-south-1`     | 335033873580 |
| `eu-west-1`      | 606966180310 |
| `eu-west-2`      | 074613877050 |
| `eu-west-3`      | 224335253976 |
| `me-south-1`     | 050406412588 |
| `sa-east-1`      | 466516958431 |
| `us-east-1`      | 864354269164 |
| `us-east-2`      | 840043622174 |
| `us-west-1`      | 952348334681 |
| `us-west-2`      | 759209512951 |
| `us-gov-west-1`  | 515361955729 |

## Amazon SageMaker Debugger exceptions

Amazon SageMaker Debugger is designed to be aware of that tensors required to execute a rule might not be
available at every step. As a result, it raises a few exceptions, which enable you to
control what happens when a tensor is missing. These exceptions are available in the
[smdebug.exceptions module](https://github.com/awslabs/sagemaker-debugger/blob/master/smdebug/exceptions.py "https://github.com/awslabs/sagemaker-debugger/blob/master/smdebug/exceptions.py"). You can import them as follows:

```
from smdebug.exceptions import *
```

The following exceptions are available:

- `TensorUnavailableForStep` – The tensor requested is not
  available for the step. This might mean that this step might not be saved at all
  by the hook, or that this step might have saved some tensors but the requested
  tensor is not part of them. Note that when you see this exception, it means that
  this tensor can never become available for this step in the future. If the
  tensor has reductions saved for the step, it notifies you they can be
  queried.
- `TensorUnavailable` – This tensor is not being saved or has
  not been saved by the `smdebug` API. This means that this tensor is
  never seen for any step in `smdebug`.
- `StepUnavailable` – The step was not saved and Debugger has no
  data from the step.
- `StepNotYetAvailable` – The step has not yet been seen by
  `smdebug`. It might be available in the future if the training is
  still going on. Debugger automatically loads new data as it becomes
  available.
- `NoMoreData` – Raised when the training ends. Once you see
  this, you know that there are no more steps and no more tensors to be
  saved.
- `IndexReaderException` – The index reader is not
  valid.
- `InvalidWorker` – A worker was invoked that was not
  valid.
- `RuleEvaluationConditionMet` – Evaluation of the rule at the
  step resulted in the condition being met.
- `InsufficientInformationForRuleInvocation` – Insufficient
  information was provided to invoke the rule.

## Distributed training supported by

Amazon SageMaker Debugger

The following list shows the scope of validity and considerations for using Debugger on
training jobs with deep learning frameworks and various distributed training
options.

- **Horovod**

Scope of validity of using Debugger for training jobs with Horovod

| Deep Learning Framework        | Apache MXNet | TensorFlow 1.x | TensorFlow 2.x | TensorFlow 2.x with Keras | PyTorch |
| ------------------------------ | ------------ | -------------- | -------------- | ------------------------- | ------- |
| Monitoring system bottlenecks  | Yes          | Yes            | Yes            | Yes                       | Yes     |
| Profiling framework operations | No           | No             | No             | Yes                       | Yes     |
| Debugging model output tensors | Yes          | Yes            | Yes            | Yes                       | Yes     |

- **SageMaker AI distributed data parallel**

Scope of validity of using Debugger for training jobs with SageMaker AI distributed data
parallel

| Deep Learning Framework        | TensorFlow 2.x | TensorFlow 2.x with Keras | PyTorch |
| ------------------------------ | -------------- | ------------------------- | ------- |
| Monitoring system bottlenecks  | Yes            | Yes                       | Yes     |
| Profiling framework operations | No\*           | No\*\*                    | Yes     |
| Debugging model output tensors | Yes            | Yes                       | Yes     |

\* Debugger does not support framework profiling for TensorFlow 2.x.

\*\* SageMaker AI distributed data parallel does not support TensorFlow 2.x with Keras
implementation.

- **SageMaker AI distributed model parallel** – Debugger does not
  support SageMaker AI distributed model parallel training.
- **Distributed training with SageMaker AI checkpoints** –
  Debugger is not available for training jobs when both the distributed training
  option and SageMaker AI checkpoints are enabled. You might see an error that looks like
  the following:

```
SMDebug Does Not Currently Support Distributed Training Jobs With Checkpointing Enabled
```

To use Debugger for training jobs with distributed training options, you need to
disable SageMaker AI checkpointing and add manual checkpointing functions to your
training script. For more information about using Debugger with distributed
training options and checkpoints, see [Using SageMaker AI distributed data
parallel with Amazon SageMaker Debugger and checkpoints](distributed-troubleshooting-data-parallel.md#distributed-ts-data-parallel-debugger "distributed-troubleshooting-data-parallel.md#distributed-ts-data-parallel-debugger") and [Saving Checkpoints](distributed-troubleshooting-model-parallel.md#distributed-ts-model-parallel-checkpoints "distributed-troubleshooting-model-parallel.md#distributed-ts-model-parallel-checkpoints").

- **Parameter Server** – Debugger does not support
  parameter server-based distributed training.
- Profiling distributed training framework operations, such as the
  `AllReduced` operation of SageMaker AI distributed data parallel and
  [Horovod operations](https://horovod.readthedocs.io/en/stable/timeline_include.html "https://horovod.readthedocs.io/en/stable/timeline_include.html"), is not available.
