

# Training a model using Neptune ML
<a name="machine-learning-on-graphs-model-training"></a>

After you have processed the data that you exported from Neptune for model training, you can start a model-training job using a command like the following:

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

The details of how to use this command are explained in [The modeltraining command](machine-learning-api-modeltraining.md), along with information about how to get the status of a running job, how to stop a running job, and how to list all running jobs.

You can also supply a `previousModelTrainingJobId` to use information from a completed Neptune ML model training job to accelerate the hyperparameter search in a new training job. This is useful during [model retraining on new graph data](machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-model-retraining), as well as [incremental training on the same graph data](machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-incremental). Use a command like this one:

------
#### [ AWS CLI ]

```
aws neptunedata start-ml-model-training-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique model-training job ID)}}" \
  --data-processing-job-id "{{(the data-processing job-id of a completed job)}}" \
  --train-model-s3-location "s3://{{(your S3 bucket)}}/neptune-model-graph-autotrainer" \
  --previous-model-training-job-id "{{(the model-training job-id of a completed job)}}"
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
    previousModelTrainingJobId='{{(the model-training job-id of a completed job)}}'
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
        "previousModelTrainingJobId" : "{{(the model-training job-id of a completed job)}}"
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
        "previousModelTrainingJobId" : "{{(the model-training job-id of a completed job)}}"
      }'
```

------

You can train your own model implementation on the Neptune ML training infrastructure by supplying a `customModelTrainingParameters` object, like this:

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



See [The modeltraining command](machine-learning-api-modeltraining.md) for more information, such as about how to get the status of a running job, how to stop a running job, and how to list all running jobs. See [Custom models in Neptune ML](machine-learning-custom-models.md) for information about how to implement and use a custom model.

**Topics**
+ [Models and model training in Amazon Neptune ML](machine-learning-models-and-training.md)
+ [Customizing model hyperparameter configurations in Neptune ML](machine-learning-customizing-hyperparams.md)
+ [Model training best practices](machine-learning-improve-model-performance.md)