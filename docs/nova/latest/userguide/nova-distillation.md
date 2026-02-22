# Amazon Nova distillation

This quick start guide helps you get started with Amazon Nova model distillation using
supervised fine-tuning (SFT) on SageMaker AI.

Model distillation is a SageMaker AI method that transfers knowledge from large, advanced
models to smaller, efficient ones. With Amazon Nova models, a larger "teacher" model
(like Amazon Nova Pro or ) passes its capabilities to a smaller "student" model
(like Amazon Nova Lite or Amazon Nova Micro). This creates a customized model that maintains
high performance while using fewer resources.

## Key

components

The distillation process primarily involves two types of models:

**Teacher models** serve as the knowledge source
and include:

- Amazon Nova Pro (amazon.nova-pro-v1:0)
- (amazon.nova-premier-v1:0)

**Student models** receive and implement the
knowledge:

- Amazon Nova Lite (amazon.nova-lite-v1:0:300k)
- Amazon Nova Micro (amazon.nova-micro-v1:0:128k)
- Amazon Nova Pro (amazon.nova-pro-v1:0:300k) - Available only when using
  as teacher

## Use cases

Mode distillation is particularly beneficial when:

- Your application has strict latency, cost, and accuracy
  requirements.
- You need a custom model for specific tasks but lack sufficient
  high-quality labeled training data.
- You want to match the performance of advanced models while maintaining
  the efficiency of smaller models.

## Prerequisites

- AWS account with access to Amazon Nova models and appropriate service
  quotas (min. 6 P5 and 1 R5 instances).
- IAM role with permissions for SageMaker Training Jobs.
- Amazon S3 bucket to store training data and outputs.

## Setting up data

augmentation

The data augmentation phase uses SageMaker Training Jobs to generate high-quality
training data using the teacher model. This section details the setup process
and requirements.

### IAM

role

To create IAM roles and attach policies, see [Creating roles and attaching policies (console)](../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md "../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md"). If you use
AWS CLI, follow instructions in [create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") and
[attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md"). For more information, see [How
to use SageMaker AI execution roles](../../../sagemaker/latest/dg/sagemaker-roles.md "../../../sagemaker/latest/dg/sagemaker-roles.md") from the _SageMaker AI Developer Guide_.

The following are example commands for your reference.

**Create a SageMaker AI execution role**

The role is created with a trust relationship allowing SageMaker AI, Amazon Bedrock, to
assume this role. This enables these services to act on your behalf when
executing batch inference jobs.

```
aws iam create-role \
 --role-name NovaCustomizationRole \
 --assume-role-policy-document '{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": ["sagemaker.amazonaws.com",
            "bedrock.amazonaws.com"]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}'
```

**Attach necessary policies**

```
# Attach AmazonSageMakerFullAccess
 aws iam attach-role-policy \
 --role-name NovaCustomizationRole \
 --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess

# Attach AmazonBedrockFullAccess
 aws iam attach-role-policy \
 --role-name NovaCustomizationRole \
 --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess

 # Attach S3 access policy
 aws iam attach-role-policy \
 --role-name NovaCustomizationRole \
 --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

# Attach AmazonEC2FullAccess
 aws iam attach-role-policy \
 --role-name NovaCustomizationRole \
 --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess

# Attach AmazonEC2ContainerRegistryFullAccess
 aws iam attach-role-policy \
 --role-name NovaCustomizationRole \
 --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess

# Attach AmazonEC2ContainerRegistryFullAccess
 aws iam attach-role-policy \
 --role-name NovaCustomizationRole \
 --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsFullAccess
```

Attach the following inline policy to customer execution role needed for
Distillation Container.

- AWS KMS permissions: Allows the role to interact with AWS Key
  Management Service, necessary for accessing encrypted resources or
  managing encryption keys.
- `IAM:PassRole`: This permission is often required when
  one service needs to pass this role to another service, a common
  pattern in AWS service integrations.

```
aws iam put-role-policy \
 --role-name NovaCustomizationRole \
 --policy-name Distillation-Additional-Permissions\
 --policy-document '{
 "Version": "2012-10-17",
 "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "*"
        }
    ]
}
```

### Amazon VPC

configuration

To create Amazon VPC configuration for SageMaker Training Jobs using the AWS Management Console,
follow instructions in [Configure Your private VPC for
SageMaker AI training (console)](../../../sagemaker/latest/dg/train-vpc.md "../../../sagemaker/latest/dg/train-vpc.md").

**Create a new Amazon VPC**

```
Name: Distillation-VPC
IPv4 CIDR: 10.0.0.0/16 (or your preferred range)
Availability Zones: 2
Public Subnets: 2
Private Subnets: 2
NAT Gateways: 1 (in one AZ)
```

**Create a security group**

```
Name: Distillation-SG
Description: Security group for data distillation jobs
Inbound Rules: Allow all traffic from self
Outbound Rules: Allow all traffic (0.0.0.0/0)
```

**Create VPC endpoints for the following
services**

```
com.amazonaws.[region].s3
com.amazonaws.[region].sagemaker.api
com.amazonaws.[region].sagemaker.runtime
com.amazonaws.[region].bedrock.api
com.amazonaws.[region].bedrock.runtime
com.amazonaws.[region].sts
com.amazonaws.[region].logs
com.amazonaws.[region].ecr.api
com.amazonaws.[region].ecr.dkr
```

For each endpoint:

- Select your Distillation-VPC
- Choose the private subnets
- Select the Distillation-SG security group

### AWS KMS

keys

When working with Amazon Bedrock batch inference, a AWS KMS key is required for data
security and compliance. Amazon Bedrock batch inference jobs require input and output
Amazon S3 buckets to be encrypted with AWS KMS keys to ensure data protection at
rest.

Create a KMS key using AWS CLI with this command:

```
# Create KMS key
aws kms create-key \
  --description "KMS key for Nova distillation"
```

The command will output the key information including the ARN. Example
output:

```
{
    "KeyMetadata": {
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "Arn": "arn:aws:kms:`us-east-1`:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }
}
```

###### Note

Save the KMS key ARN from the output as you'll need it for the Amazon S3
bucket creation in the next section.

### Amazon S3

bucket

You need two types of Amazon S3 storage. Customer-managed Amazon S3 bucket stores
your input data and output `manifest.json` files. You create and
manage this bucket and can use a single bucket for both input and output.
This bucket must be configured with KMS encryption since it will store
sensitive output data and will be used by Amazon Bedrock batch inference jobs - Amazon Bedrock
requires KMS-encrypted buckets for processing batch inference tasks.

Service-managed Amazon S3 bucket stores model weights. A service-managed Amazon S3
bucket is created automatically during your first training job. It has
restricted access controls with specific paths accessible via manifest files
only.

To create a bucket in a specific AWS Region, use the [create-bucket](../../../cli/latest/reference/s3api/create-bucket.md "../../../cli/latest/reference/s3api/create-bucket.md") CLI command.

Example command to create an Amazon S3 bucket with AWS KMS encryption. Replace
`{kms_key_arn}` with your AWS KMS key ARN. You'll need to
create a AWS KMS key first if you haven't already done so.

```
aws s3api create-bucket \
    "Rules": [
        {
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "aws:kms",
                "KMSMasterKeyID": "{kms_key_arn}"
            },
            "BucketKeyEnabled": true
        }
    ]
}'
```

## Starting a SageMaker training

job

Before you start a training job, prepare your data.

**Data format requirement -** Your input dataset
must be in JSONL format with each line containing a sample in converse format
for more information follow [Preparing data for
distilling understanding models](custom-distill-prepare.md "custom-distill-prepare.md").

**Dataset constraints**

- Minimum prompts: 100
- Maximum file size: 2GB
- Maximum line length: 180KB
- File format: JSONL only

To upload input data, run the following command.

```
aws s3 cp /path/to/input-data/ s3://customer-input-data-bucket/ —recursive
```

**Data augmentation recipe**

You can get the distillation recipe from the [recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes") repository. The distillation recipe is under
the directory: `recipes-collection/recipes/fine-tuning/nova`. The
data augmentation process is controlled by a YAML configuration file. Below is a
detailed explanation of each parameter. All are required fields.

| Parameter                                      | Description                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                                           | A descriptive name for your training job. This helps<br>identify your job in the AWS Management Console.                                                                                                                                                                                             |
| distillation_data                              | Enables data distillation job, do not modify this<br>field.                                                                                                                                                                                                                                          |
| maxNumberOfPrompts                             | The Maximum number of prompts in the dataset.                                                                                                                                                                                                                                                        |
| maxResponseLength                              | The Maximum response length per prompt (tokens).                                                                                                                                                                                                                                                     |
| maxInputFileSizeInGB                           | The Maximum size of the input file (in GB).                                                                                                                                                                                                                                                          |
| maxLineLengthInKB                              | The Maximum size of a single line in the input file (in<br>KB).                                                                                                                                                                                                                                      |
| maxStudentModelFineTuningContextLengthInTokens | The Maximum context window size (tokens) for student<br>model. The is value must not exceed student model capacity.<br>You can set this value to 32k or 64k based on student model<br>capacity.                                                                                                      |
| teacherModelId                                 | When you set Teacher Model Id, select from two:<br>• For Amazon Nova Premier: "us.amazon.nova-premier-v1:0"<br>for IAD region. Note: This is only available in IAD<br>region.<br>• For Amazon Nova Pro: "us.amazon.nova-pro-v1:0" for IAD<br>region and "eu.amazon.nova-pro-v1:0" for ARN<br>region. |
| temperature                                    | Controls response randomness (0.7 recommended for<br>balance).                                                                                                                                                                                                                                       |
| top_p                                          | Cumulative probability threshold for token sampling (0.9<br>is recommended).                                                                                                                                                                                                                         |
| customer_bucket                                | Amazon S3 bucket for input/output data.                                                                                                                                                                                                                                                              |
| kms_key                                        | AWS KMS key to encrypt output in S3, This needed by Bedrock<br>batch inference to store output returned by inference<br>job.                                                                                                                                                                         |

**Limitation**

For Teacher Model as Nova Premier - Only supported in IAD region
(`us-east-1`) due to Amazon Bedrock batch inference is not available in ARN
(`eu-north-1`) region.

**Best Practices**

Data preparation

- Include 100 high-quality labeled examples to guide the teacher
  model
- Remove poor quality labels before submission
- Follow text understanding prompting best practices
- Test prompts with the teacher model before starting
  distillation

Model selection

- Use Nova Pro as teacher for general use cases
- Consider Nova Premier for specialized domain knowledge
- Choose student model based on latency and cost requirements

Performance optimization

- Start with recommended temperature (0.7) and top_p (0.9)
- Validate augmented data quality before fine-tuning
- Follow the guidelines in [Selecting hyperparameters](customize-fine-tune-hyperparameters.md "customize-fine-tune-hyperparameters.md") to adjust the
  hyperparameters

**Starting a job with PySDK**

The following sample notebook demonstrates how to run a SageMaker training job for
distillation. For more information, see [Use a SageMaker AI estimator to run a training job](../../../sagemaker/latest/dg/docker-containers-adapt-your-own-private-registry-estimator.md "../../../sagemaker/latest/dg/docker-containers-adapt-your-own-private-registry-estimator.md").

```
import os
import sagemaker,boto3
from sagemaker.pytorch import PyTorch
from sagemaker.inputs import TrainingInput

sagemaker_session = sagemaker.Session()
role = sagemaker.get_execution_role()

# SETUP
job_name = <Your_job_name> # Must be unique for every run

input_s3_uri = <S3 URI to your input dataset> # Must end in .jsonl file
output_s3_uri = <S3 URI to your output bucket> + job_name

image_uri = "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-distillation-repo:SM-TJ-DISTILL-LATEST" # Do not change
instance_type = "ml.r5.4xlarge" # Recommedation is to use cpu instances
instance_count = 1 # Must be 1, do not change
role_arn = <IAM role to execute the job with>
recipe_path = <Local path to your recipe>

# Execution

estimator = PyTorch(
    output_path=output_s3_uri,
    base_job_name=job_name,
    role=role_arn,
    instance_count=instance_count,
    instance_type=instance_type,
    training_recipe=recipe_path,
    max_run=432000,
    sagemaker_session=sagemaker_session,
    image_uri=image_uri,
    subnets= ['subnet-xxxxxxxxxxxxxxxxx','subnet-xxxxxxxxxxxxxxxxx'], # Add subnet groups created in previous steps
    security_group_ids= ['sg-xxxxxxxxxxxxxxxxx'], # Add security group created in previous steps
    disable_profiler=True,
    debugger_hook_config=False
)

trainingInput = TrainingInput(
    s3_data=input_s3_uri,
    distribution='FullyReplicated',
    s3_data_type='Converse'
)

# The keys must be "train".
estimator.fit(inputs={"train": trainingInput})
```

## CloudWatch logs

Logs are available in Amazon CloudWatch under the
`/aws/sagemaker/TrainingJobs` log group in your AWS account.
You will see one log file per host used for your training job.

## Successful

training

For a successful training job, you will see the log message "Training is
complete" at the end of the log.

The output bucket contains the following files:

- `distillation_data/manifest.json`: Contains the location of
  augmented data. You can use this dataset to start an Amazon Nova fine-tuning
  job. Only SFT training is supported with this dataset.

```
{
  "distillation_data": "s3://`customer_escrow_bucket`/`job_id`/distillation_data/"
}
```

- `distillation_data/sample_training_data.jsonl`: This JSONL
  file contains 50 samples of augmented data for preview to help you
  determine data quality.
- `distillation_data/training_config.json`: This file
  contains recommended hyperparameters for Amazon Nova fine-tuning jobs. The
  following is an example file:

```
{
    "epochCount": 5,
    "learningRate": 1e-05,
    "batchSize": 1,
    "learningRateWarmupSteps": 1
}
```

## Validating augmented

data quality

Before proceeding to fine-tuning, it's crucial to validate the quality of the
augmented data:

1. Review the `sample_training_data.jsonl` file in your output
   bucket. This file contains 50 random samples from the augmented
   dataset.
2. Manually inspect these samples for relevance, coherence, and alignment
   with your use case.
3. If the quality doesn't meet your expectations, you may need to adjust
   your input data or distillation parameters and rerun the data
   augmentation process.

After data augmentation completes, the second phase involves fine-tuning the
student model using . For more information, see [Supervised fine-tuning (SFT)](nova-fine-tune.md "nova-fine-tune.md").

In SFT training recipe you can pass the dataset path returned form previous
job.

```
data_s3_path: "s3://[escrow-bucket]/[job-name]/distillation_data/training_data.jsonl"
```

Also override the training config recommended generated from previous step.

**Limitations**

- Only supports SFT Nova fine-tuning technique on this augmented
  data.
- No support for multi-modal distillation.
- No support for custom teacher models.
