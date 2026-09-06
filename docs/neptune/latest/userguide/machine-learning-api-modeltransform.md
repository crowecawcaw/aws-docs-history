

# Model transform using the `modeltransform` command
<a name="machine-learning-api-modeltransform"></a>

You use the Neptune ML `modeltransform` command to create a model transform job, check its status, stop it, or list all active model-transform jobs.

## Creating a model-transform job using the Neptune ML `modeltransform` command
<a name="machine-learning-api-modeltransform-create-job"></a>

A Neptune ML `modeltransform` command for creating an incremental transform job, without model retraining, looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata start-ml-model-transform-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique model-transform job ID)}}" \
  --data-processing-job-id "{{(the job-id of a completed data-processing job)}}" \
  --ml-model-training-job-id "{{(the job-id of a completed model-training job)}}" \
  --model-transform-output-s3-location "s3://{{(your S3 bucket)}}/neptune-model-transform"
```

For more information, see [start-ml-model-transform-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/start-ml-model-transform-job.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.start_ml_model_transform_job(
    id='{{(a unique model-transform job ID)}}',
    dataProcessingJobId='{{(the job-id of a completed data-processing job)}}',
    mlModelTrainingJobId='{{(the job-id of a completed model-training job)}}',
    modelTransformOutputS3Location='s3://{{(your S3 bucket)}}/neptune-model-transform'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-transform job ID)}}",
        "dataProcessingJobId" : "{{(the job-id of a completed data-processing job)}}",
        "mlModelTrainingJobId" : "{{(the job-id of a completed model-training job)}}",
        "modelTransformOutputS3Location" : "s3://{{(your S3 bucket)}}/neptune-model-transform"
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl \
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-transform job ID)}}",
        "dataProcessingJobId" : "{{(the job-id of a completed data-processing job)}}",
        "mlModelTrainingJobId" : "{{(the job-id of a completed model-training job)}}",
        "modelTransformOutputS3Location" : "s3://{{(your S3 bucket)}}/neptune-model-transform"
      }'
```

------

A Neptune ML `modeltransform` command for creating a job from a completed SageMaker AI training job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata start-ml-model-transform-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique model-transform job ID)}}" \
  --training-job-name "{{(name of a completed SageMaker training job)}}" \
  --model-transform-output-s3-location "s3://{{(your S3 bucket)}}/neptune-model-transform"
```

For more information, see [start-ml-model-transform-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/start-ml-model-transform-job.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.start_ml_model_transform_job(
    id='{{(a unique model-transform job ID)}}',
    trainingJobName='{{(name of a completed SageMaker training job)}}',
    modelTransformOutputS3Location='s3://{{(your S3 bucket)}}/neptune-model-transform'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-transform job ID)}}",
        "trainingJobName" : "{{(name of a completed SageMaker training job)}}",
        "modelTransformOutputS3Location" : "s3://{{(your S3 bucket)}}/neptune-model-transform"
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl \
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-transform job ID)}}",
        "trainingJobName" : "{{(name of a completed SageMaker training job)}}",
        "modelTransformOutputS3Location" : "s3://{{(your S3 bucket)}}/neptune-model-transform"
      }'
```

------

A Neptune ML `modeltransform` command for creating a job that uses a custom model implementation looks like:

------
#### [ AWS CLI ]

```
aws neptunedata start-ml-model-transform-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique model-transform job ID)}}" \
  --training-job-name "{{(name of a completed SageMaker training job)}}" \
  --model-transform-output-s3-location "s3://{{(your Amazon S3 bucket)}}/neptune-model-transform/" \
  --custom-model-transform-parameters '{
    "sourceS3DirectoryPath": "s3://{{(your Amazon S3 bucket)}}/{{(path to your Python module)}}",
    "transformEntryPointScript": "{{(your transform script entry-point name in the Python module)}}"
  }'
```

For more information, see [start-ml-model-transform-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/start-ml-model-transform-job.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.start_ml_model_transform_job(
    id='{{(a unique model-transform job ID)}}',
    trainingJobName='{{(name of a completed SageMaker training job)}}',
    modelTransformOutputS3Location='s3://{{(your Amazon S3 bucket)}}/neptune-model-transform/',
    customModelTransformParameters={
        'sourceS3DirectoryPath': 's3://{{(your Amazon S3 bucket)}}/{{(path to your Python module)}}',
        'transformEntryPointScript': '{{(your transform script entry-point name in the Python module)}}'
    }
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-transform job ID)}}",
        "trainingJobName" : "{{(name of a completed SageMaker training job)}}",
        "modelTransformOutputS3Location" : "s3://{{(your Amazon S3 bucket)}}/neptune-model-transform/",
        "customModelTransformParameters" : {
          "sourceS3DirectoryPath": "s3://{{(your Amazon S3 bucket)}}/{{(path to your Python module)}}",
          "transformEntryPointScript": "{{(your transform script entry-point name in the Python module)}}"
        }
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl \
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-transform job ID)}}",
        "trainingJobName" : "{{(name of a completed SageMaker training job)}}",
        "modelTransformOutputS3Location" : "s3://{{(your Amazon S3 bucket)}}/neptune-model-transform/",
        "customModelTransformParameters" : {
          "sourceS3DirectoryPath": "s3://{{(your Amazon S3 bucket)}}/{{(path to your Python module)}}",
          "transformEntryPointScript": "{{(your transform script entry-point name in the Python module)}}"
        }
      }'
```

------

**Parameters for `modeltransform` job creation**
+ **`id`**   –   (*Optional*) A unique identifier for the new job.

  *Type*: string. *Default*: An autogenerated UUID.
+ **`dataProcessingJobId`**   –   The job Id of a completed data-processing job.

  *Type*: string.

  *Note*: You must include either both `dataProcessingJobId` and `mlModelTrainingJobId`, or `trainingJobName`.
+ **`mlModelTrainingJobId`**   –   The job Id of a completed model-training job.

  *Type*: string.

  *Note*: You must include either both `dataProcessingJobId` and `mlModelTrainingJobId`, or `trainingJobName`.
+ **`trainingJobName`**   –   The name of a completed SageMaker AI training job.

  *Type*: string.

  *Note*: You must include either both the `dataProcessingJobId` and the `mlModelTrainingJobId` parameters, or the `trainingJobName` parameter.
+ **`sagemakerIamRoleArn`**   –   (*Optional*) The ARN of an IAM role for SageMaker AI execution.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role that provides Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.
+ **`customModelTransformParameters `**   –   (*Optional*) Configuration information for a model transform using a custom model. The `customModelTransformParameters` object contains the following fields, which must have values compatible with the saved model parameters from the training job:
  + **`sourceS3DirectoryPath`**   –   (*Required*) The path to the Amazon S3 location where the Python module implementing your model is located. This must point to a valid existing Amazon S3 location that contains, at a minimum, a training script, a transform script, and a `model-hpo-configuration.json` file.
  + **`transformEntryPointScript`**   –   (*Optional*) The name of the entry point in your module of a script that should be run after the best model from the hyperparameter search has been identified, to compute the model artifacts necessary for model deployment. It should be able to run with no command-line arguments.

    *Default*: `transform.py`.
+ **`baseProcessingInstanceType`**   –   (*Optional*) The type of ML instance used in preparing and managing training of ML models.

  *Type*: string. *Note*: This is a CPU instance chosen based on memory requirements for processing the transform data and model. See [Selecting an instance for model training and model transform](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-training-transform-instance-size).
+ **`baseProcessingInstanceVolumeSizeInGB`**   –   (*Optional*) The disk volume size of the training instance. Both input data and the output model are stored on disk, so the volume size must be large enough to hold both data sets.

  *Type*: integer. *Default*: `0`.

  *Note*: If not specified or 0, Neptune ML selects a disk volume size based on the recommendation generated in the data processing step. See [Selecting an instance for model training and model transform](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-training-transform-instance-size).
+ **`subnets`**   –   (*Optional*) The IDs of the subnets in the Neptune VPC.

  *Type*: list of strings. *Default*: *none*.
+ **`securityGroupIds`**   –   (*Optional*) The VPC security group IDs.

  *Type*: list of strings. *Default*: *none*.
+ **`volumeEncryptionKMSKey`**   –   (*Optional*) The AWS Key Management Service (AWS KMS) key that SageMaker AI uses to encrypt data on the storage volume attached to the ML compute instances that run the transform job.

  *Type*: string. *Default*: *none*.
+ **`enableInterContainerTrafficEncryption`**   –   (*Optional*) Enable or disable inter-container traffic encryption in training or hyper-parameter tuning jobs.

  *Type*: boolean. *Default*: *True*.
**Note**  
The `enableInterContainerTrafficEncryption` parameter is only available in [engine release 1.2.0.2.R3](engine-releases-1.2.0.2.R3.md).
+ **`s3OutputEncryptionKMSKey`**   –   (*Optional*) The AWS Key Management Service (AWS KMS) key that SageMaker AI uses to encrypt the output of the processing job.

  *Type*: string. *Default*: *none*.

## Getting the status of a model-transform job using the Neptune ML `modeltransform` command
<a name="machine-learning-api-modeltransform-get-job-status"></a>

A sample Neptune ML `modeltransform` command for the status of a job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata get-ml-model-transform-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(the job ID)}}"
```

For more information, see [get-ml-model-transform-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-ml-model-transform-job.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.get_ml_model_transform_job(
    id='{{(the job ID)}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform/{{(the job ID)}} \
  --region {{us-east-1}} \
  --service neptune-db \
  -X GET
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -s \
  "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform/{{(the job ID)}}" \
  | python -m json.tool
```

------

**Parameters for `modeltransform` job status**
+ **`id`**   –   (*Required*) The unique identifier of the model-transform job.

  *Type*: string.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role that provides Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.

## Stopping a model-transform job using the Neptune ML `modeltransform` command
<a name="machine-learning-api-modeltransform-stop-job"></a>

A sample Neptune ML `modeltransform` command for stopping a job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata cancel-ml-model-transform-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(the job ID)}}"
```

To also clean up Amazon S3 artifacts:

```
aws neptunedata cancel-ml-model-transform-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(the job ID)}}" \
  --clean
```

For more information, see [cancel-ml-model-transform-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/cancel-ml-model-transform-job.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.cancel_ml_model_transform_job(
    id='{{(the job ID)}}',
    clean=True
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform/{{(the job ID)}} \
  --region {{us-east-1}} \
  --service neptune-db \
  -X DELETE
```

To also clean up Amazon S3 artifacts:

```
awscurl "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform/{{(the job ID)}}?clean=true" \
  --region {{us-east-1}} \
  --service neptune-db \
  -X DELETE
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -s \
  -X DELETE "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform/{{(the job ID)}}"
```

Or this:

```
curl -s \
  -X DELETE "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform/{{(the job ID)}}?clean=true"
```

------

**Parameters for `modeltransform` stop job**
+ **`id`**   –   (*Required*) The unique identifier of the model-transform job.

  *Type*: string.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role that provides Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.
+ **`clean`**   –   (*Optional*) This flag specifies that all Amazon S3 artifacts should be deleted when the job is stopped.

  *Type*: Boolean. *Default*: `FALSE`.

## Listing active model-transform jobs using the Neptune ML `modeltransform` command
<a name="machine-learning-api-modeltransform-list-jobs"></a>

A sample Neptune ML `modeltransform` command for listing active jobs looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata list-ml-model-transform-jobs \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}}
```

To limit the number of results:

```
aws neptunedata list-ml-model-transform-jobs \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --max-items 3
```

For more information, see [list-ml-model-transform-jobs](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/list-ml-model-transform-jobs.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.list_ml_model_transform_jobs(
    maxItems=3
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform \
  --region {{us-east-1}} \
  --service neptune-db \
  -X GET
```

To limit the number of results:

```
awscurl "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform?maxItems=3" \
  --region {{us-east-1}} \
  --service neptune-db \
  -X GET
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -s "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform" | python -m json.tool
```

Or this:

```
curl -s "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltransform?maxItems=3" | python -m json.tool
```

------

**Parameters for `modeltransform` list jobs**
+ **`maxItems`**   –   (*Optional*) The maximum number of items to return.

  *Type*: integer. *Default*: `10`. *Maximum allowed value*: `1024`.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role that provides Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.