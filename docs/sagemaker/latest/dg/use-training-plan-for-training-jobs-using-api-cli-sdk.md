# Create a training job using the API, AWS CLI, SageMaker SDK

To use SageMaker training plans for your SageMaker training job, specify the
`TrainingPlanArn` parameter of the desired plan in the
`ResourceConfig` when calling the [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") API operation. You can use exactly one plan per
job.

###### Important

The `InstanceType` field set in the `ResourceConfig` section of
the `CreateTrainingJob` request must match the`InstanceType` of your
training plan.

## Run a training job on a plan using the CLI

The following example demonstrates how to create a SageMaker training job and associate it
with a provided training plan using the `TrainingPlanArn` attribute in the
`create-training-job` AWS CLI command.

For more information about how to create a training job using the AWS CLI [CreateTrainingJob](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") command, see [`create-training-job`](../../../cli/latest/reference/sagemaker/create-training-job.md "../../../cli/latest/reference/sagemaker/create-training-job.md").

```
# Create a training job
aws sagemaker create-training-job \
  --training-job-name `training-job-name` \
  ...

  --resource-config '{
        "InstanceType": "`ml.p5.48xlarge`",
        "InstanceCount": `8`,
        "VolumeSizeInGB": `10`,
        "TrainingPlanArn": "`training-plan-arn`"
        }
    }' \
    ...

```

This AWS CLI example command creates a new training job in SageMaker AI passing a training plan in
the `--resource-config` argument.

```
aws sagemaker create-training-job \
  --training-job-name `job-name` \
  --role-arn `arn:aws:iam::111122223333:role/DataAndAPIAccessRole` \
  --algorithm-specification '{"TrainingInputMode": "`File`","TrainingImage": "`111122223333.dkr.ecr.us-east-1.amazonaws.com/algo-image:tag`", "ContainerArguments": [" "]}' \
  --input-data-config '[{"ChannelName":"`training`","DataSource":{"S3DataSource":{"S3DataType":"`S3Prefix`","S3Uri":"`s3://bucketname/input`","S3DataDistributionType":"`ShardedByS3Key`"}}}]' \
  --output-data-config '{"S3OutputPath": "`s3://bucketname/output`"}' \
  --resource-config '{"VolumeSizeInGB":`10`,"InstanceCount":`4`,"InstanceType":"`ml.p5.48xlarge`", "TrainingPlanArn" : "`arn:aws:sagemaker:us-east-1:111122223333:training-plan/plan-name`"}' \
  --stopping-condition '{"MaxRuntimeInSeconds": `1800`}' \
  --region `us-east-1`

```

After creating the training job, you can verify that it was properly assigned to the
training plan by calling the `DescribeTrainingJob` API.

```
aws sagemaker describe-training-job --training-job-name `training-job-name`
```

## Run a training job on a plan using the SageMaker AI Python SDK

Alternatively, you can create a training job associated with a training plan using the
[SageMaker Python
SDK](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/").

If you are using the SageMaker Python SDK from JupyterLab in Studio to create a
training job, ensure that the execution role used by the space running your JupyterLab
application has the required permissions to use SageMaker training plans. To learn about the
required permissions to use SageMaker training plans, see [IAM for SageMaker training plans](training-plan-iam-permissions.md "training-plan-iam-permissions.md").

The following example demonstrates how to create a SageMaker training job and associate it
with a provided training plan using the `training_plan` attribute in the
`ModelTrainer` object when using the SageMaker Python SDK.

For more information on the SageMaker ModelTrainer, see [Use a SageMaker ModelTrainer to run a training job](docker-containers-adapt-your-own-private-registry-estimator.md "docker-containers-adapt-your-own-private-registry-estimator.md").

```
import boto3
from sagemaker.core.helper.session_helper import get_execution_role
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import InputData
from sagemaker.train.configs import Compute, SourceCode
from sagemaker.core.shapes import OutputDataConfig

# Set up the session and SageMaker client
session = boto3.Session()
region = session.region_name
sagemaker_session = session.client('sagemaker')

# Get the execution role for the training job
role = get_execution_role()

# Define the input data configuration
trainingInput = InputData(
    channel_name='`training`',
    data_source='`s3://input-path`'
)

model_trainer = ModelTrainer(
    training_image="`123456789123.dkr.ecr.{}.amazonaws.com/image:tag`",
    source_code=SourceCode(entry_script='train.py'),
    role=role,
    compute=Compute(
        instance_type='`ml.p5.48xlarge`',
        instance_count=`4`,
        volume_size_in_gb=`20`,
        training_plan_arn="`training-plan-arn`"
    ),
    output_data_config=OutputDataConfig(s3_output_path="`s3://output-path`")
)

# Create the training job
model_trainer.train(input_data_config=[trainingInput])

```

After creating the training job, you can verify that it was properly assigned to the
training plan by calling the `DescribeTrainingJob` API.

```
# Check job details
sagemaker_session.describe_training_job(TrainingJobName=job_name)
```
