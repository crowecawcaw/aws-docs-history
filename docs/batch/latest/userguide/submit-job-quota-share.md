

# Submitting jobs to a quota share
<a name="submit-job-quota-share"></a>

Quota management job queues require that all jobs specify a quota share at job submission. To submit jobs to a quota share, specify the `quotaShareName` in [SubmitServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitServiceJob.html). A `preemptionConfiguration` can optionally be supplied to limit the number of preemption attempts before a job attempt enters `FAILED`. To limit the number of preemptions a job experiences, set `preemptionRetriesBeforeTermination` within [ServiceJobPreemptionConfiguration](https://docs.aws.amazon.com/batch/latest/APIReference/API_ServiceJobPreemptionConfiguration.html) on job submission.

## Prerequisites
<a name="submit-job-quota-share-prerequisites"></a>

Before submitting jobs to a quota share, ensure you have:
+ **Quota management resources** – A scheduling policy, service environment, and job queue configured for quota management. For more information, see [Create quota management resources](create-quota-management-resources.md).
+ **Quota share** – At least one quota share created on the job queue. For more information, see [Creating quota shares](create-quota-shares.md).
+ **IAM permissions** – Permissions to submit jobs to AWS Batch. For more information, see [AWS Batch IAM policies, roles, and permissions](IAM_policies.md).

## Submit a service job to a quota share
<a name="submit-job-quota-share-example"></a>

The table below shows how to submit a service job to a quota share using either the SageMaker Python SDK or the AWS CLI: 

------
#### [ Submit using the SageMaker Python SDK ]

The [SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/v3-examples/training-examples/aws_batch/sm-training-queues_quota-management.html) has built-in support for submitting jobs to a quota management enabled job queue. The following examples show how to create a model trainer, create a training queue, and submit jobs to a quota share. For a complete example, see the [full sample notebook](https://github.com/aws/sagemaker-python-sdk/blob/master/v3-examples/training-examples/aws_batch/sm-training-queues_quota-management.ipynb) on GitHub.

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

Create a `TrainingQueue` object that references your quota management enabled job queue by name.

```
from sagemaker.train.aws_batch.training_queue import TrainingQueue

queue = TrainingQueue({{"my-sagemaker-job-queue"}})
```

Submit jobs to a quota share by calling `queue.submit` and specifying the `quota_share_name`. You should set a `priority` to influence job ordering within the quota share. A real-world `ModelTrainer` will require `inputs` so that it has data to train on.

```
job = queue.submit(
    job_name={{"my-training-job"}},
    training_job=model_trainer,
    quota_share_name={{"my_quota_share"}},
    priority={{3}},
    inputs=None,
)
```

------
#### [ Submit using the AWS CLI ]

The following example uses the **submit-service-job** command to submit a job to a quota share.

```
aws batch submit-service-job \
    --job-name {{"my-sagemaker-training-job"}} \
    --job-queue {{"my-sagemaker-job-queue"}} \
    --service-job-type "SAGEMAKER_TRAINING" \
    --quota-share-name {{"my_quota_share"}} \
    --timeout-config '{"attemptDurationSeconds":{{3600}}}' \
    --scheduling-priority {{5}} \
    --service-request-payload {{'{\"TrainingJobName\": \"sagemaker-training-job-example\", \"AlgorithmSpecification\": {\"TrainingImage\": \"123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.8.0-cpu-py3\", \"TrainingInputMode\": \"File\", \"ContainerEntrypoint\":  [\"sleep\", \"1\"]}, \"RoleArn\":\"arn:aws:iam::123456789012:role/SageMakerExecutionRole\", \"OutputDataConfig\": {\"S3OutputPath\": \"s3://example-bucket/model-output/\"}, \"ResourceConfig\": {\"InstanceType\": \"ml.m5.large\", \"InstanceCount\": 1, \"VolumeSizeInGB\": 1}}'}}"
```

------