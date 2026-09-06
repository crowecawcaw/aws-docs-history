

# Model training using the `modeltraining` command
<a name="machine-learning-api-modeltraining"></a>

You use the Neptune ML `modeltraining` command to create a model training job, check its status, stop it, or list all active model-training jobs.

## Creating a model-training job using the Neptune ML `modeltraining` command
<a name="machine-learning-api-modeltraining-create-job"></a>

A Neptune ML `modeltraining` command for creating a completely new job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata start-ml-model-training-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique model-training job ID)}}" \
  --data-processing-job-id "{{(the data-processing job-id of a completed job)}}" \
  --train-model-s3-location "s3://{{(your S3 bucket)}}/neptune-model-graph-autotrainer"
```

For more information, see [start-ml-model-training-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/start-ml-model-training-job.html) in the AWS CLI Command Reference.

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

response = client.start_ml_model_training_job(
    id='{{(a unique model-training job ID)}}',
    dataProcessingJobId='{{(the data-processing job-id of a completed job)}}',
    trainModelS3Location='s3://{{(your S3 bucket)}}/neptune-model-graph-autotrainer'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-training job ID)}}",
        "dataProcessingJobId" : "{{(the data-processing job-id of a completed job)}}",
        "trainModelS3Location" : "s3://{{(your S3 bucket)}}/neptune-model-graph-autotrainer"
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl \
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-training job ID)}}",
        "dataProcessingJobId" : "{{(the data-processing job-id of a completed job)}}",
        "trainModelS3Location" : "s3://{{(your S3 bucket)}}/neptune-model-graph-autotrainer"
      }'
```

------

A Neptune ML `modeltraining` command for creating an update job for incremental model training looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata start-ml-model-training-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique model-training job ID)}}" \
  --data-processing-job-id "{{(the data-processing job-id of a completed job)}}" \
  --train-model-s3-location "s3://{{(your S3 bucket)}}/neptune-model-graph-autotrainer" \
  --previous-model-training-job-id "{{(the job ID of a completed model-training job to update)}}"
```

For more information, see [start-ml-model-training-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/start-ml-model-training-job.html) in the AWS CLI Command Reference.

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

response = client.start_ml_model_training_job(
    id='{{(a unique model-training job ID)}}',
    dataProcessingJobId='{{(the data-processing job-id of a completed job)}}',
    trainModelS3Location='s3://{{(your S3 bucket)}}/neptune-model-graph-autotrainer',
    previousModelTrainingJobId='{{(the job ID of a completed model-training job to update)}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-training job ID)}}",
        "dataProcessingJobId" : "{{(the data-processing job-id of a completed job)}}",
        "trainModelS3Location" : "s3://{{(your S3 bucket)}}/neptune-model-graph-autotrainer",
        "previousModelTrainingJobId" : "{{(the job ID of a completed model-training job to update)}}"
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl \
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-training job ID)}}",
        "dataProcessingJobId" : "{{(the data-processing job-id of a completed job)}}",
        "trainModelS3Location" : "s3://{{(your S3 bucket)}}/neptune-model-graph-autotrainer",
        "previousModelTrainingJobId" : "{{(the job ID of a completed model-training job to update)}}"
      }'
```

------

A Neptune ML `modeltraining` command for creating a new job with user provided custom model implementation looks like: 

------
#### [ AWS CLI ]

```
aws neptunedata start-ml-model-training-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique model-training job ID)}}" \
  --data-processing-job-id "{{(the data-processing job-id of a completed job)}}" \
  --train-model-s3-location "s3://{{(your Amazon S3 bucket)}}/neptune-model-graph-autotrainer" \
  --model-name "custom" \
  --custom-model-training-parameters '{
    "sourceS3DirectoryPath": "s3://{{(your Amazon S3 bucket)}}/{{(path to your Python module)}}",
    "trainingEntryPointScript": "{{(your training script entry-point name in the Python module)}}",
    "transformEntryPointScript": "{{(your transform script entry-point name in the Python module)}}"
  }'
```

For more information, see [start-ml-model-training-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/start-ml-model-training-job.html) in the AWS CLI Command Reference.

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

response = client.start_ml_model_training_job(
    id='{{(a unique model-training job ID)}}',
    dataProcessingJobId='{{(the data-processing job-id of a completed job)}}',
    trainModelS3Location='s3://{{(your Amazon S3 bucket)}}/neptune-model-graph-autotrainer',
    modelName='custom',
    customModelTrainingParameters={
        'sourceS3DirectoryPath': 's3://{{(your Amazon S3 bucket)}}/{{(path to your Python module)}}',
        'trainingEntryPointScript': '{{(your training script entry-point name in the Python module)}}',
        'transformEntryPointScript': '{{(your transform script entry-point name in the Python module)}}'
    }
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-training job ID)}}",
        "dataProcessingJobId" : "{{(the data-processing job-id of a completed job)}}",
        "trainModelS3Location" : "s3://{{(your Amazon S3 bucket)}}/neptune-model-graph-autotrainer",
        "modelName": "custom",
        "customModelTrainingParameters" : {
          "sourceS3DirectoryPath": "s3://{{(your Amazon S3 bucket)}}/{{(path to your Python module)}}",
          "trainingEntryPointScript": "{{(your training script entry-point name in the Python module)}}",
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
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique model-training job ID)}}",
        "dataProcessingJobId" : "{{(the data-processing job-id of a completed job)}}",
        "trainModelS3Location" : "s3://{{(your Amazon S3 bucket)}}/neptune-model-graph-autotrainer",
        "modelName": "custom",
        "customModelTrainingParameters" : {
          "sourceS3DirectoryPath": "s3://{{(your Amazon S3 bucket)}}/{{(path to your Python module)}}",
          "trainingEntryPointScript": "{{(your training script entry-point name in the Python module)}}",
          "transformEntryPointScript": "{{(your transform script entry-point name in the Python module)}}"
        }
      }'
```

------

**Parameters for `modeltraining` job creation**
+ **`id`**   –   (*Optional*) A unique identifier for the new job.

  *Type*: string. *Default*: An autogenerated UUID.
+ **`dataProcessingJobId`**   –   (*Required*) The job Id of the completed data-processing job that has created the data that the training will work with.

  *Type*: string.
+ **`trainModelS3Location`**   –   (*Required*) The location in Amazon S3 where the model artifacts are to be stored.

  *Type*: string.
+ **`previousModelTrainingJobId`**   –   (*Optional*) The job ID of a completed model-training job that you want to update incrementally based on updated data.

  *Type*: string. *Default*: *none*.
+ **`sagemakerIamRoleArn`**   –   (*Optional*) The ARN of an IAM role for SageMaker AI execution.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role that provides Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.
+ **`modelName`**   –   (*Optional*) The model type for training. By default the ML model is automatically based on the `modelType` used in data processing, but you can specify a different model type here.

  *Type*: string. *Default*: `rgcn` for heterogeneous graphs and `kge` for knowledge graphs. *Valid values*: For heterogeneous graphs: `rgcn`. For `kge` graphs: `transe`, `distmult`, or `rotate`. For a custom model implementation: `custom`.
+ **`baseProcessingInstanceType`**   –   (*Optional*) The type of ML instance used in preparing and managing training of ML models.

  *Type*: string. *Note*: This is a CPU instance chosen based on memory requirements for processing the training data and model. See [Selecting an instance for model training and model transform](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-training-transform-instance-size).
+ **`trainingInstanceType`**   –   (*Optional*) The type of ML instance used for model training. All Neptune ML models support CPU, GPU, and multiGPU training.

  *Type*: string. *Default*: `ml.p3.2xlarge`.

  *Note*: Choosing the right instance type for training depends on the task type, graph size, and your budget. See [Selecting an instance for model training and model transform](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-training-transform-instance-size).
+ **`trainingInstanceVolumeSizeInGB`**   –   (*Optional*) The disk volume size of the training instance. Both input data and the output model are stored on disk, so the volume size must be large enough to hold both data sets.

  *Type*: integer. *Default*: `0`.

  *Note*: If not specified or 0, Neptune ML selects a disk volume size based on the recommendation generated in the data processing step. See [Selecting an instance for model training and model transform](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-training-transform-instance-size).
+ **`trainingTimeOutInSeconds`**   –   (*Optional*) Timeout in seconds for the training job.

  *Type*: integer. *Default*: `86,400` (1 day).
+ **`maxHPONumberOfTrainingJobs`**   –   Maximum total number of training jobs to start for the hyperparameter tuning job.

  *Type*: integer. *Default*: `2`.

  *Note*: Neptune ML automatically tunes the hyper-parameters of the machine learning model. To obtain a model that performs well, use at least 10 jobs (in other words, set `maxHPONumberOfTrainingJobs` to 10). In general, the more tuning runs, the better the results.
+ **`maxHPOParallelTrainingJobs`**   –   Maximum number of parallel training jobs to start for the hyperparameter tuning job.

  *Type*: integer. *Default*: `2`.

  *Note*: The number of parallel jobs you can run is limited by the available resources on your training instance.
+ **`subnets`**   –   (*Optional*) The IDs of the subnets in the Neptune VPC.

  *Type*: list of strings. *Default*: *none*.
+ **`securityGroupIds`**   –   (*Optional*) The VPC security group IDs.

  *Type*: list of strings. *Default*: *none*.
+ **`volumeEncryptionKMSKey`**   –   (*Optional*) The AWS Key Management Service (AWS KMS) key that SageMaker AI uses to encrypt data on the storage volume attached to the ML compute instances that run the training job.

  *Type*: string. *Default*: *none*.
+ **`s3OutputEncryptionKMSKey`**   –   (*Optional*) The AWS Key Management Service (AWS KMS) key that SageMaker AI uses to encrypt the output of the processing job.

  *Type*: string. *Default*: *none*.
+ **`enableInterContainerTrafficEncryption`**   –   (*Optional*) Enable or disable inter-container traffic encryption in training or hyper-parameter tuning jobs.

  *Type*: boolean. *Default*: *True*.
**Note**  
The `enableInterContainerTrafficEncryption` parameter is only available in [engine release 1.2.0.2.R3](engine-releases-1.2.0.2.R3.md).
+ **`enableManagedSpotTraining`**   –   (*Optional*) Optimizes the cost of training machine learning models by using Amazon Elastic Compute Cloud spot instances. For more information, see [Managed Spot Training in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html).

  *Type*: Boolean. *Default*: *False*.
+ **`customModelTrainingParameters`**  –   (*Optional*) The configuration for custom model training. This is a JSON object with the following fields:
  + **`sourceS3DirectoryPath`**   –   (*Required*) The path to the Amazon S3 location where the Python module implementing your model is located. This must point to a valid existing Amazon S3 location that contains, at a minimum, a training script, a transform script, and a `model-hpo-configuration.json` file.
  + **`trainingEntryPointScript`**   –   (*Optional*) The name of the entry point in your module of a script that performs model training and takes hyperparameters as command-line arguments, including fixed hyperparameters.

    *Default*: `training.py`.
  + **`transformEntryPointScript`**   –   (*Optional*) The name of the entry point in your module of a script that should be run after the best model from the hyperparameter search has been identified, to compute the model artifacts necessary for model deployment. It should be able to run with no command-line arguments.

    *Default*: `transform.py`.
+ **`maxWaitTime`**   –   (*Optional*) The maximum time to wait, in seconds, when performing model training using spot instances. Should be greater than `trainingTimeOutInSeconds`.

  *Type*: integer.

## Getting the status of a model-training job using the Neptune ML `modeltraining` command
<a name="machine-learning-api-modeltraining-get-job-status"></a>

A sample Neptune ML `modeltraining` command for the status of a job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata get-ml-model-training-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(the job ID)}}"
```

For more information, see [get-ml-model-training-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-ml-model-training-job.html) in the AWS CLI Command Reference.

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

response = client.get_ml_model_training_job(
    id='{{(the job ID)}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining/{{(the job ID)}} \
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
  "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining/{{(the job ID)}}" \
  | python -m json.tool
```

------

**Parameters for `modeltraining` job status**
+ **`id`**   –   (*Required*) The unique identifier of the model-training job.

  *Type*: string.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role that provides Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.

## Stopping a model-training job using the Neptune ML `modeltraining` command
<a name="machine-learning-api-modeltraining-stop-job"></a>

A sample Neptune ML `modeltraining` command for stopping a job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata cancel-ml-model-training-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(the job ID)}}"
```

To also clean up Amazon S3 artifacts:

```
aws neptunedata cancel-ml-model-training-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(the job ID)}}" \
  --clean
```

For more information, see [cancel-ml-model-training-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/cancel-ml-model-training-job.html) in the AWS CLI Command Reference.

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

response = client.cancel_ml_model_training_job(
    id='{{(the job ID)}}',
    clean=True
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining/{{(the job ID)}} \
  --region {{us-east-1}} \
  --service neptune-db \
  -X DELETE
```

To also clean up Amazon S3 artifacts:

```
awscurl "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining/{{(the job ID)}}?clean=true" \
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
  -X DELETE "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining/{{(the job ID)}}"
```

Or this:

```
curl -s \
  -X DELETE "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining/{{(the job ID)}}?clean=true"
```

------

**Parameters for `modeltraining` stop job**
+ **`id`**   –   (*Required*) The unique identifier of the model-training job.

  *Type*: string.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role that provides Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.
+ **`clean`**   –   (*Optional*) This flag specifies that all Amazon S3 artifacts should be deleted when the job is stopped.

  *Type*: Boolean. *Default*: `FALSE`.

## Listing active model-training jobs using the Neptune ML `modeltraining` command
<a name="machine-learning-api-modeltraining-list-jobs"></a>

A sample Neptune ML `modeltraining` command for listing active jobs looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata list-ml-model-training-jobs \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}}
```

To limit the number of results:

```
aws neptunedata list-ml-model-training-jobs \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --max-items 3
```

For more information, see [list-ml-model-training-jobs](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/list-ml-model-training-jobs.html) in the AWS CLI Command Reference.

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

response = client.list_ml_model_training_jobs(
    maxItems=3
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining \
  --region {{us-east-1}} \
  --service neptune-db \
  -X GET
```

To limit the number of results:

```
awscurl "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining?maxItems=3" \
  --region {{us-east-1}} \
  --service neptune-db \
  -X GET
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -s "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining" | python -m json.tool
```

Or this:

```
curl -s "https://{{your-neptune-endpoint}}:{{port}}/ml/modeltraining?maxItems=3" | python -m json.tool
```

------

**Parameters for `modeltraining` list jobs**
+ **`maxItems`**   –   (*Optional*) The maximum number of items to return.

  *Type*: integer. *Default*: `10`. *Maximum allowed value*: `1024`.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role that provides Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will occur.