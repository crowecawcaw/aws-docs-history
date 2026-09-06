

# Submit a service job in AWS Batch
<a name="service-job-submit"></a>

To submit service jobs to AWS Batch, you use the [SubmitServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitServiceJob.html) API. You can submit jobs using the AWS CLI or SDK.

If you don't already have an execution role then you must create one before you can submit your service job. To create the SageMaker AI execution role, see [How to use SageMaker AI execution roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) in the *[SageMaker AI Developer guide](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)*.

## Service job submission workflow
<a name="service-job-submit-workflow"></a>

When you submit a service job, AWS Batch follows this workflow:

1. AWS Batch receives your `[SubmitServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitServiceJob.html)` request and validates the AWS Batch-specific parameters. The `serviceRequestPayload` is passed through without validation.

1. The job enters the `SUBMITTED` state and is placed in the specified job queue

1. AWS Batch evaluates if there is available capacity in the service environment for `RUNNABLE` jobs at the front of the queue

1. If capacity is available, the job moves to `SCHEDULED` and the job has been passed to SageMaker AI

1. When capacity has been acquired and SageMaker AI has downloaded the service job data, the service job will start initialization and the job is changed to `STARTING`. 

1. When SageMaker AI starts to execute the job its status is changed to `RUNNING`.

1. While SageMaker AI executes the job, AWS Batch monitors its progress and maps service states to AWS Batch job states. For details about how service job states are mapped, see [Mapping AWS Batch service job status to SageMaker AI status](service-job-status.md)

1. When the service job is completed it moves to `SUCCEEDED` and any output is ready to be downloaded.

## Prerequisites
<a name="service-job-submit-prerequisites"></a>

Before submitting a service job, ensure you have:
+ **Service environment** – A service environment that defines capacity limits. For more information, see [Create a service environment in AWS Batch](create-service-environments.md).
+ **SageMaker job queue** – A SageMaker job queue to provide job scheduling. For more information, see [Create a SageMaker Training job queue in AWS Batch](create-sagemaker-job-queue.md).
+ **IAM permissions** – Permissions to create and manage AWS Batch job queues and service environments. For more information, see [AWS Batch IAM policies, roles, and permissions](IAM_policies.md).

## Submit a service job
<a name="service-job-submit-example"></a>

The table below shows how to submit a service job using either the SageMaker Python SDK or the AWS CLI:

------
#### [ Submit using the SageMaker Python SDK ]

The [SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/v3-examples/training-examples/aws_batch/sm-training-queues_getting_started_with_model_trainer.html) has built-in support for submitting jobs to AWS Batch. The following examples show how to create a model trainer, create a training queue, and submit a job. For a complete example, see the [full sample notebook](https://github.com/aws/sagemaker-python-sdk/blob/master/v3-examples/training-examples/aws_batch/sm-training-queues_getting_started_with_model_trainer.ipynb) on GitHub.

Create a `ModelTrainer` that defines the training job configuration.

```
from sagemaker.train.model_trainer import ModelTrainer
from sagemaker.train.configs import SourceCode, Compute, StoppingCondition

source_code = SourceCode(command="echo 'Hello World'")

model_trainer = ModelTrainer(
    training_image={{"123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:2.5-gpu-py311"}},
    source_code=source_code,
    base_job_name={{"my-training-job"}},
    compute=Compute(instance_type={{"ml.g5.xlarge"}}, instance_count={{1}}),
    stopping_condition=StoppingCondition(max_runtime_in_seconds={{300}}),
)
```

Create a `TrainingQueue` object that references your job queue by name.

```
from sagemaker.train.aws_batch.training_queue import TrainingQueue

queue = TrainingQueue({{"my-sagemaker-job-queue"}})
```

Submit a job by calling `queue.submit`.

```
job = queue.submit(
    training_job=model_trainer,
    inputs=None,
)
```

------
#### [ Submit using the AWS CLI ]

The following shows how to submit a service job using the AWS CLI:

```
aws batch submit-service-job \
    --job-name "my-sagemaker-training-job" \
    --job-queue "my-sagemaker-job-queue" \
    --service-job-type "SAGEMAKER_TRAINING" \
    --service-request-payload '{\"TrainingJobName\": \"sagemaker-training-job-example\", \"AlgorithmSpecification\": {\"TrainingImage\": \"123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.8.0-cpu-py3\", \"TrainingInputMode\": \"File\", \"ContainerEntrypoint\":  [\"sleep\", \"1\"]}, \"RoleArn\":\"arn:aws:iam::123456789012:role/SageMakerExecutionRole\", \"OutputDataConfig\": {\"S3OutputPath\": \"s3://example-bucket/model-output/\"}, \"ResourceConfig\": {\"InstanceType\": \"ml.m5.large\", \"InstanceCount\": 1, \"VolumeSizeInGB\": 1}}'
    --client-token "unique-token-12345"
```

For more information about the `serviceRequestPayload` parameters, see [Service job payloads in AWS Batch](service-job-payload.md).

------