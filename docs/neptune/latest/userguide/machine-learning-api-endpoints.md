

# Managing inference endpoints using the `endpoints` command
<a name="machine-learning-api-endpoints"></a>

You use the Neptune ML `endpoints` command to create an inference endpoint, check its status, delete it, or list existing inference endpoints.

## Creating an inference endpoint using the Neptune ML `endpoints` command
<a name="machine-learning-api-endpoints-create-job"></a>

A Neptune ML `endpoints` command for creating an inference endpoint from a model created by a training job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata create-ml-endpoint \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique ID for the new endpoint)}}" \
  --ml-model-training-job-id "{{(the model-training job-id of a completed job)}}"
```

For more information, see [create-ml-endpoint](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/create-ml-endpoint.html) in the AWS CLI Command Reference.

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

response = client.create_ml_endpoint(
    id='{{(a unique ID for the new endpoint)}}',
    mlModelTrainingJobId='{{(the model-training job-id of a completed job)}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique ID for the new endpoint)}}",
        "mlModelTrainingJobId": "{{(the model-training job-id of a completed job)}}"
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl \
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique ID for the new endpoint)}}",
        "mlModelTrainingJobId": "{{(the model-training job-id of a completed job)}}"
      }'
```

------

A Neptune ML `endpoints` command for updating an existing inference endpoint from a model created by a training job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata create-ml-endpoint \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique ID for the new endpoint)}}" \
  --update \
  --ml-model-training-job-id "{{(the model-training job-id of a completed job)}}"
```

For more information, see [create-ml-endpoint](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/create-ml-endpoint.html) in the AWS CLI Command Reference.

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

response = client.create_ml_endpoint(
    id='{{(a unique ID for the new endpoint)}}',
    update=True,
    mlModelTrainingJobId='{{(the model-training job-id of a completed job)}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique ID for the new endpoint)}}",
        "update" : "true",
        "mlModelTrainingJobId": "{{(the model-training job-id of a completed job)}}"
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl \
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique ID for the new endpoint)}}",
        "update" : "true",
        "mlModelTrainingJobId": "{{(the model-training job-id of a completed job)}}"
      }'
```

------

A Neptune ML `endpoints` command for creating an inference endpoint from a model created by a model-transform job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata create-ml-endpoint \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique ID for the new endpoint)}}" \
  --ml-model-transform-job-id "{{(the model-transform job-id of a completed job)}}"
```

For more information, see [create-ml-endpoint](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/create-ml-endpoint.html) in the AWS CLI Command Reference.

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

response = client.create_ml_endpoint(
    id='{{(a unique ID for the new endpoint)}}',
    mlModelTransformJobId='{{(the model-transform job-id of a completed job)}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique ID for the new endpoint)}}",
        "mlModelTransformJobId": "{{(the model-transform job-id of a completed job)}}"
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl \
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique ID for the new endpoint)}}",
        "mlModelTransformJobId": "{{(the model-transform job-id of a completed job)}}"
      }'
```

------

A Neptune ML `endpoints` command for updating an existing inference endpoint from a model created by a model-transform job looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata create-ml-endpoint \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(a unique ID for the new endpoint)}}" \
  --update \
  --ml-model-transform-job-id "{{(the model-transform job-id of a completed job)}}"
```

For more information, see [create-ml-endpoint](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/create-ml-endpoint.html) in the AWS CLI Command Reference.

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

response = client.create_ml_endpoint(
    id='{{(a unique ID for the new endpoint)}}',
    update=True,
    mlModelTransformJobId='{{(the model-transform job-id of a completed job)}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique ID for the new endpoint)}}",
        "update" : "true",
        "mlModelTransformJobId": "{{(the model-transform job-id of a completed job)}}"
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl \
  -X POST https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "{{(a unique ID for the new endpoint)}}",
        "update" : "true",
        "mlModelTransformJobId": "{{(the model-transform job-id of a completed job)}}"
      }'
```

------

**Parameters for `endpoints` inference endpoint creation**
+ **`id`**   –   (*Optional*) A unique identifier for the new inference endpoint.

  *Type*: string. *Default*: An autogenerated timestamped name.
+ **`mlModelTrainingJobId`**   –   The job Id of the completed model-training job that has created the model that the inference endpoint will point to.

  *Type*: string.

  *Note*: You must supply either the `mlModelTrainingJobId` or the `mlModelTransformJobId`.
+ **`mlModelTransformJobId`**   –   The job Id of the completed model-transform job.

  *Type*: string.

  *Note*: You must supply either the `mlModelTrainingJobId` or the `mlModelTransformJobId`.
+ **`update`**   –   (*Optional*) If present, this parameter indicates that this is an update request.

  *Type*: Boolean. *Default*: `false`

  *Note*: You must supply either the `mlModelTrainingJobId` or the `mlModelTransformJobId`.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role providing Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will be thrown.
+ **`modelName`**   –   (*Optional*) Model type for training. By default the ML model is automatically based on the `modelType` used in data processing, but you can specify a different model type here.

  *Type*: string. *Default*: `rgcn` for heterogeneous graphs and `kge` for knowledge graphs. *Valid values*: For heterogeneous graphs: `rgcn`. For knowledge graphs: `kge`, `transe`, `distmult`, or `rotate`.
+ **`instanceType`**   –   (*Optional*) The type of ML instance used for online servicing.

  *Type*: string. *Default*: `ml.m5.xlarge`.

  *Note*: Choosing the ML instance for an inference endpoint depends on the task type, the graph size, and your budget. See [Selecting an instance for an inference endpoint](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-inference-endpoint-instance-size).
+ **`instanceCount`**   –   (*Optional*) The minimum number of Amazon EC2 instances to deploy to an endpoint for prediction.

  *Type*: integer. *Default*: `1`.
+ **`volumeEncryptionKMSKey`**   –   (*Optional*) The AWS Key Management Service (AWS KMS) key that SageMaker AI uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the endpoints.

  *Type*: string. *Default*: *none*.

## Getting the status of an inference endpoint using the Neptune ML `endpoints` command
<a name="machine-learning-api-endpoints-get-endpoint-status"></a>

A sample Neptune ML `endpoints` command for the status of an instance endpoint looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata get-ml-endpoint \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(the inference endpoint ID)}}"
```

For more information, see [get-ml-endpoint](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-ml-endpoint.html) in the AWS CLI Command Reference.

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

response = client.get_ml_endpoint(
    id='{{(the inference endpoint ID)}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints/{{(the inference endpoint ID)}} \
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
  "https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints/{{(the inference endpoint ID)}}" \
  | python -m json.tool
```

------

**Parameters for `endpoints` instance-endpoint status**
+ **`id`**   –   (*Required*) The unique identifier of the inference endpoint.

  *Type*: string.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role providing Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will be thrown.

## Deleting an instance endpoint using the Neptune ML `endpoints` command
<a name="machine-learning-api-endpoints-delete-endpoint"></a>

A sample Neptune ML `endpoints` command for deleting an instance endpoint looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata delete-ml-endpoint \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(the inference endpoint ID)}}"
```

To also clean up related artifacts:

```
aws neptunedata delete-ml-endpoint \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --id "{{(the inference endpoint ID)}}" \
  --clean
```

For more information, see [delete-ml-endpoint](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/delete-ml-endpoint.html) in the AWS CLI Command Reference.

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

response = client.delete_ml_endpoint(
    id='{{(the inference endpoint ID)}}',
    clean=True
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints/{{(the inference endpoint ID)}} \
  --region {{us-east-1}} \
  --service neptune-db \
  -X DELETE
```

To also clean up related artifacts:

```
awscurl "https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints/{{(the inference endpoint ID)}}?clean=true" \
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
  -X DELETE "https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints/{{(the inference endpoint ID)}}"
```

Or this:

```
curl -s \
  -X DELETE "https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints/{{(the inference endpoint ID)}}?clean=true"
```

------

**Parameters for `endpoints` deleting an inference endpoint**
+ **`id`**   –   (*Required*) The unique identifier of the inference endpoint.

  *Type*: string.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role providing Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will be thrown.
+ **`clean`**   –   (*Optional*) Indicates that all artifacts related to this endpoint should also be deleted.

  *Type*: Boolean. *Default*: `FALSE`.

## Listing inference endpoints using the Neptune ML `endpoints` command
<a name="machine-learning-api-endpoints-list-endpoints"></a>

A Neptune ML `endpoints` command for listing inference endpoints looks like this:

------
#### [ AWS CLI ]

```
aws neptunedata list-ml-endpoints \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}}
```

To limit the number of results:

```
aws neptunedata list-ml-endpoints \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --max-items 3
```

For more information, see [list-ml-endpoints](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/list-ml-endpoints.html) in the AWS CLI Command Reference.

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

response = client.list_ml_endpoints(
    maxItems=3
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints \
  --region {{us-east-1}} \
  --service neptune-db \
  -X GET
```

To limit the number of results:

```
awscurl "https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints?maxItems=3" \
  --region {{us-east-1}} \
  --service neptune-db \
  -X GET
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -s "https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints" \
  | python -m json.tool
```

Or this:

```
curl -s "https://{{your-neptune-endpoint}}:{{port}}/ml/endpoints?maxItems=3" \
  | python -m json.tool
```

------

**Parameters for `dataprocessing` list inference endpoints**
+ **`maxItems`**   –   (*Optional*) The maximum number of items to return.

  *Type*: integer. *Default*: `10`. *Maximum allowed value*: `1024`.
+ **`neptuneIamRoleArn`**   –   (*Optional*) The ARN of an IAM role providing Neptune access to SageMaker AI and Amazon S3 resources.

  *Type*: string. *Note*: This must be listed in your DB cluster parameter group or an error will be thrown.