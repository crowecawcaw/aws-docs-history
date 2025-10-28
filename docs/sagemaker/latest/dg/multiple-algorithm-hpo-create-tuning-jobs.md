# Create a Hyperparameter

Optimization Tuning Job for One or More Algorithms (Console)

This guide shows you how to create a new hyperparameter optimization (HPO) tuning job for
one or more algorithms. To create an HPO job, define the settings for the tuning job, and
create training job definitions for each algorithm being tuned. Next, configure the resources
for and create the tuning job. The following sections provide details about how to complete
each step. We provide an example of how to tune multiple algorithms using the SageMaker AI
SDK for Python client at the end of this guide.

## Components of a

tuning job

An HPO tuning job contains the following three components:

- Tuning job settings
- Training job definitions
- Tuning job configuration

The way that these components are included in your HPO tuning job depends on whether
your tuning job contains one or multiple training algorithms. The following guide describes
each of the components and gives an example of both types of tuning jobs.

Your tuning job settings are applied across all of the algorithms in the HPO tuning
job. Warm start and early stopping are available only when you're tuning a single
algorithm. After you define the job settings, you can create individual training
definitions for each algorithm or variation that you want to tune.

###### Warm start

If you cloned this job, you can use the results from a previous tuning job to
improve the performance of this new tuning job. This is the warm start feature, and
it's only available when tuning a single algorithm. With the warm start option, you
can choose up to five previous hyperparameter tuning jobs to use. Alternatively, you
can use transfer learning to add additional data to the parent tuning job. When you
select this option, you choose one previous tuning job as the parent.

###### Note

Warm start is compatible only with tuning jobs that were created after October 1, 2018. For more information, see [Run a warm start
job](automatic-model-tuning-considerations.md "automatic-model-tuning-considerations.md").

###### Early stopping

To reduce compute time and avoid overfitting your model, you can stop training
jobs early. Early stopping is helpful when the training job is unlikely to improve the
current best objective metric of the hyperparameter tuning job. Like warm start, this
feature is only available when tuning a single algorithm. This is an automatic feature
without configuration options, and it’s disabled by default. For more information
about how early stopping works, the algorithms that support it, and how to use it with
your own algorithms, see [Stop
Training Jobs Early](automatic-model-tuning-early-stopping.md "automatic-model-tuning-early-stopping.md").

###### Tuning strategy

Tuning strategy can be either random, Bayesian, or Hyperband. These
selections specify how automatic tuning algorithms search specified hyperparameter
ranges that are selected in a later step. Random search chooses random combinations of
values from the specified ranges and can be run sequentially or in parallel. Bayesian
optimization chooses values based on what is likely to get the best result according
to the known history of previous selections. Hyperband uses a
multi-fidelity strategy that dynamically allocates resources toward well-utilized jobs
and automatically stops those that underperform. The new configuration that starts
after stopping other configurations is chosen randomly.

Hyperband can only be used with iterative algorithms, or algorithms
that run steps in iterations, such as [XGBoost](xgboost.md "xgboost.md") or [Random Cut
Forest](randomcutforest.md "randomcutforest.md"). Hyperband can't be used with non-iterative
algorithms, such as decision trees or [k-Nearest Neighbors](k-nearest-neighbors.md "k-nearest-neighbors.md"). For
more information about search strategies, see [How Hyperparameter Tuning
Works](automatic-model-tuning-how-it-works.md "automatic-model-tuning-how-it-works.md").

###### Note

Hyperband uses an advanced internal mechanism to apply early
stopping. Therefore, when you use the Hyperband internal early stopping
feature, the parameter `TrainingJobEarlyStoppingType` in the
`HyperParameterTuningJobConfig` API must be set to
`OFF`.

###### Tags

To help you manage tuning jobs, you can enter tags as key-value pairs to assign
metadata to tuning jobs. Values in the key-value pair are not required. You can use
the key without values. To see the keys associated with a job, choose
the **Tags** tab on the details page for tuning job. For more
information about using tags for tuning jobs, see [Manage Hyperparameter Tuning and
Training Jobs](multiple-algorithm-hpo-manage-tuning-jobs.md "multiple-algorithm-hpo-manage-tuning-jobs.md").

To create a training job definition, you must configure the algorithm and
parameters, define the data input and output, and configure resources. Provide at least
one [`TrainingJobDefinition`](../APIReference/API_TrainingJobDefinition.md "../APIReference/API_TrainingJobDefinition.md") for each HPO tuning job. Each training
definition specifies the configuration for an algorithm.

To create several definitions for your training job, you can clone a job definition.
Cloning a job can save time because it copies all of the job settings, including data
channels and Amazon S3 storage locations for output artifacts. You can edit a cloned job to
change what you need for your use case.

###### Topics

- [Configure algorithm
  and parameters](#multiple-algorithm-hpo-algorithm-configuration "#multiple-algorithm-hpo-algorithm-configuration")
- [Define data input and output](#multiple-algorithm-hpo-data "#multiple-algorithm-hpo-data")
- [Configure
  training job resources](#multiple-algorithm-hpo-training-job-definition-resources "#multiple-algorithm-hpo-training-job-definition-resources")
- [Add or clone a training
  job](#multiple-algorithm-hpo-add-training-job "#multiple-algorithm-hpo-add-training-job")

#### Configure algorithm

and parameters

The following list describes what you need to configure the set of hyperparameter
values for each training job.

- A name for your tuning job
- Permission to access services
- Parameters for any algorithm options
- An objective metric
- The range of hyperparameter values, when required

###### Name

Provide a unique name for the training definition.

###### Permissions

Amazon SageMaker AI requires permissions to call other services on your behalf. Choose an
AWS Identity and Access Management (IAM) role, or let AWS create a role with the
`AmazonSageMakerFullAccess` IAM policy attached.

###### Optional security settings

The network isolation setting prevents the container from making any outbound
network calls. This is required for AWS Marketplace machine learning offerings.

You can also choose to use a virtual private cloud (VPC).

###### Note

Inter-container encryption is only available when you create a job definition
from the API.

###### Algorithm options

You can choose built-in algorithms, your own algorithm, your own container with
an algorithm, or you can subscribe to an algorithm from AWS Marketplace.

- If you choose a built-in algorithm, it has the Amazon Elastic Container Registry (Amazon ECR) image
  information pre-populated.
- If you choose your own container, you must specify the (Amazon ECR) image
  information. You can select the input mode for the algorithm as file or
  pipe.
- If you plan to supply your data using a CSV file from Amazon S3, you should select
  the file.

###### Metrics

When you choose a built-in algorithm, metrics are provided for you. If you
choose your own algorithm, you must define your metrics. You can define up to 20
metrics for your tuning job to monitor. You must choose one metric as the objective
metric. For more information about how to define a metric for a tuning job, see
[Define metrics](automatic-model-tuning-define-metrics-variables.md#automatic-model-tuning-define-metrics "automatic-model-tuning-define-metrics-variables.md#automatic-model-tuning-define-metrics").

###### Objective metric

To find the best training job, set an objective metric and whether to maximize
or minimize it. After the training job is complete, you can view the tuning job
detail page. The detail page provides a summary of the best training job that is
found using this objective metric.

###### Hyperparameter configuration

When you choose a built-in algorithm, the default values for its hyperparameters
are set for you, using ranges that are optimized for the algorithm that's being
tuned. You can change these values as you see fit. For example, instead of a range,
you can set a fixed value for a hyperparameter by setting the parameter’s type
to **static**. Each algorithm has different
required and optional parameters. For more information, see [Best Practices for Hyperparameter
Tuning](automatic-model-tuning-considerations.md "automatic-model-tuning-considerations.md") and [Define
Hyperparameter Ranges](automatic-model-tuning-define-ranges.md "automatic-model-tuning-define-ranges.md").

#### Define data input and output

Each training job definition for a tuning job must configure the channels for data
inputs, data output locations, and optionally, any checkpoint storage locations for
each training job.

###### Input data configuration

Input data is defined by channels. Each channel its own source location (Amazon S3
or Amazon Elastic File System), compression, and format options. You can define up to 20 channels of
input sources. If the algorithm that you choose supports multiple input channels,
you can specify those, too. For example, when you use the [XGBoost churn prediction notebook](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/xgboost_customer_churn/xgboost_customer_churn.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/xgboost_customer_churn/xgboost_customer_churn.html"), you can add two
channels: train and validation.

###### Checkpoint configuration

Checkpoints are periodically generated during training. For the checkpoints to
be saved, you must choose an Amazon S3 location. Checkpoints are used in metrics
reporting, and are also used to resume managed spot training jobs. For more
information, see [Checkpoints in Amazon SageMaker AI](model-checkpoints.md "model-checkpoints.md").

###### Output data configuration

Define an Amazon S3 location for the artifacts of the training job to be stored. You
have the option of adding encryption to the output using an AWS Key Management Service (AWS KMS) key.

#### Configure

training job resources

Each training job definition for a tuning job must configure the resources to
deploy, including instance types and counts, managed spot training, and stopping
conditions.

###### Resource configuration

Each training definition can have a different resource configuration. You choose
the instance type and number of nodes.

###### Managed spot training

You can save computer costs for jobs if you have flexibility in start and end
times by allowing SageMaker AI to use spare capacity to run jobs. For more information, see
[Managed Spot Training in Amazon SageMaker AI](model-managed-spot-training.md "model-managed-spot-training.md").

###### Stopping condition

The stopping condition specifies the maximum duration that's allowed for each
training job.

#### Add or clone a training

job

After you create a training job definition for a tuning job, you will return to
the **Training Job Definition(s)** panel. This panel is where you can
create additional training job definitions to train additional algorithms. You can
select the **Add training job definition** and work through the steps
to define a training job again.

Alternatively, to replicate an existing training job definition and edit it for
the new algorithm, choose **Clone** from the
**Action** menu. The clone option can save time because it copies
all of the job’s settings, including the data channels and Amazon S3 storage locations. For
more information about cloning, see [Manage Hyperparameter Tuning and
Training Jobs](multiple-algorithm-hpo-manage-tuning-jobs.md "multiple-algorithm-hpo-manage-tuning-jobs.md").

###### Resource Limits

You can specify the maximum number of concurrent training jobs that a
hyperparameter tuning job can run concurrently (10 at most). You can also specify the
maximum number of training jobs that the hyperparameter tuning job can run (500 at
most). The number of parallel jobs should not exceed the number of nodes that you
have requested across all of your training definitions. The total number of jobs can’t
exceed the number of jobs that your definitions are expected to run.

Review the job settings, the training job definitions, and the resource limits. Then
select **Create hyperparameter tuning job**.

## HPO tuning job

example

To run a hyperparameter optimization (HPO) training job, first create a training job
definition for each algorithm that's being tuned. Next, define the tuning job settings and
configure the resources for the tuning job. Finally, run the tuning job.

If your HPO tuning job contains a single training algorithm, the SageMaker AI tuning function
will call the `HyperparameterTuner` API directly and pass in your parameters. If
your HPO tuning job contains multiple training algorithms, your tuning function will call
the `create` function of the `HyperparameterTuner` API. The
`create` function tells the API to expect a dictionary containing one or more
estimators.

In the following section, code examples show how to tune a job containing either a
single training algorithm or multiple algorithms using the SageMaker AI Python
SDK.

### Create

training job definitions

When you create a tuning job that includes multiple training algorithms, your tuning
job configuration will include the estimators and metrics and other parameters for your
training jobs. Therefore, you need to create the training job definition first, and then
configure your tuning job.

The following code example shows how to retrieve two SageMaker AI containers containing the
built-in algorithms [XGBoost](xgboost.md "xgboost.md") and [Linear Learner](linear-learner.md "linear-learner.md"). If
your tuning job contains only one training algorithm, omit one of the containers and one
of the estimators.

```
import sagemaker
from sagemaker import image_uris

from sagemaker.estimator import Estimator

sess = sagemaker.Session()
region = sess.boto_region_name
role = sagemaker.get_execution_role()

bucket = sess.default_bucket()
prefix = "sagemaker/multi-algo-hpo"

# Define the training containers and intialize the estimators
xgb_container = image_uris.retrieve("xgboost", region, "latest")
ll_container = image_uris.retrieve("linear-learner", region, "latest")

xgb_estimator = Estimator(
    xgb_container,
    role=role,
    instance_count=1,
    instance_type="ml.m4.xlarge",
    output_path='s3://{}/{}/xgb_output".format(bucket, prefix)',
    sagemaker_session=sess,
)

ll_estimator = Estimator(
    ll_container,
    role,
    instance_count=1,
    instance_type="ml.c4.xlarge",
    output_path="s3://{}/{}/ll_output".format(bucket, prefix),
    sagemaker_session=sess,
)

# Set static hyperparameters
ll_estimator.set_hyperparameters(predictor_type="binary_classifier")
xgb_estimator.set_hyperparameters(
    eval_metric="auc",
    objective="binary:logistic",
    num_round=100,
    rate_drop=0.3,
    tweedie_variance_power=1.4,
)
```

Next, define your input data by specifying the training, validation, and testing
datasets, as shown in the following code example. This example shows how to tune multiple
training algorithms.

```
training_data = sagemaker.inputs.TrainingInput(
    s3_data="s3://{}/{}/train".format(bucket, prefix), content_type="csv"
)
validation_data = sagemaker.inputs.TrainingInput(
    s3_data="s3://{}/{}/validate".format(bucket, prefix), content_type="csv"
)
test_data = sagemaker.inputs.TrainingInput(
    s3_data="s3://{}/{}/test".format(bucket, prefix), content_type="csv"
)

train_inputs = {
    "estimator-1": {
        "train": training_data,
        "validation": validation_data,
        "test": test_data,
    },
    "estimator-2": {
        "train": training_data,
        "validation": validation_data,
        "test": test_data,
    },
}
```

If your tuning algorithm contains only one training algorithm, your
`train_inputs` should contain only one estimator.

You must upload the inputs for the training, validation, and training datasets to your
Amazon S3 bucket before you use those in an HPO tuning job.

### Define resources and settings for your tuning job

This section shows how to initialize a tuner, define resources, and specify job
settings for your tuning job. If your tuning job contains multiple training algorithms,
these settings are applied to all of the algorithms that are contained inside your tuning
job. This section provides two code examples to define a tuner. The code examples show you
how to optimize a single training algorithm followed by an example of how to tune multiple
training algorithms.

####

Tune a single training algorithm

The following code example shows how to initialize a tuner and set hyperparameter
ranges for one SageMaker AI built-in algorithm, XGBoost.

```
from sagemaker.tuner import HyperparameterTuner
from sagemaker.parameter import ContinuousParameter, IntegerParameter

hyperparameter_ranges = {
    "max_depth": IntegerParameter(1, 10),
    "eta": ContinuousParameter(0.1, 0.3),
}

objective_metric_name = "validation:accuracy"

tuner = HyperparameterTuner(
    xgb_estimator,
    objective_metric_name,
    hyperparameter_ranges,
    objective_type="Maximize",
    max_jobs=5,
    max_parallel_jobs=2,
)
```

#### Tune multiple training algorithms

Each training job requires different configurations, and these are specified using a
dictionary. The following code example shows how to initialize a tuner with
configurations for two SageMaker AI built-in algorithms, XGBoost and
Linear Learner. The code example also shows how to set a tuning
strategy and other job settings, such as the compute resources for the tuning job. The
following code example uses `metric_definitions_dict`, which is
optional.

```
from sagemaker.tuner import HyperparameterTuner
from sagemaker.parameter import ContinuousParameter, IntegerParameter

# Initialize your tuner
tuner = HyperparameterTuner.create(
    estimator_dict={
        "estimator-1": xgb_estimator,
        "estimator-2": ll_estimator,
    },
    objective_metric_name_dict={
        "estimator-1": "validation:auc",
        "estimator-2": "test:binary_classification_accuracy",
    },
    hyperparameter_ranges_dict={
        "estimator-1": {"eta": ContinuousParameter(0.1, 0.3)},
        "estimator-2": {"learning_rate": ContinuousParameter(0.1, 0.3)},
    },
    metric_definitions_dict={
        "estimator-1": [
            {"Name": "validation:auc", "Regex": "Overall test accuracy: (.*?);"}
        ],
        "estimator-2": [
            {
                "Name": "test:binary_classification_accuracy",
                "Regex": "Overall test accuracy: (.*?);",
            }
        ],
    },
    strategy="Bayesian",
    max_jobs=10,
    max_parallel_jobs=3,
)
```

### Run your

HPO tuning job

Now you can run your tuning job by passing your training inputs to the
`fit` function of the `HyperparameterTuner` class. The following
code example shows how to pass the `train_inputs` parameter, that is defined in
a previous code example, to your tuner.

```
tuner.fit(inputs=train_inputs, include_cls_metadata ={}, estimator_kwargs ={})
```
