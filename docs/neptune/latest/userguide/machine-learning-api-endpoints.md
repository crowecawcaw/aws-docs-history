# Managing inference endpoints using the `endpoints` command

You use the Neptune ML `endpoints` command to create an inference endpoint,
check its status, delete it, or list existing inference endpoints.

## Creating an inference endpoint using the Neptune ML `endpoints` command

A Neptune ML `endpoints` command for creating an inference endpoint
from a model created by a training job looks like this:

AWS CLI

```
aws neptunedata create-ml-endpoint \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(a unique ID for the new endpoint)`" \
  --ml-model-training-job-id "`(the model-training job-id of a completed job)`"
```

For more information, see [create-ml-endpoint](../../../cli/latest/reference/neptunedata/create-ml-endpoint.md "../../../cli/latest/reference/neptunedata/create-ml-endpoint.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.create_ml_endpoint(
    id='`(a unique ID for the new endpoint)`',
    mlModelTrainingJobId='`(the model-training job-id of a completed job)`'
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/endpoints \
  --region `us-east-1` \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "mlModelTrainingJobId": "`(the model-training job-id of a completed job)`"
      }'
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl \
  -X POST https://`your-neptune-endpoint`:`port`/ml/endpoints \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "mlModelTrainingJobId": "`(the model-training job-id of a completed job)`"
      }'
```

A Neptune ML `endpoints` command for updating an existing inference endpoint
from a model created by a training job looks like this:

AWS CLI

```
aws neptunedata create-ml-endpoint \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(a unique ID for the new endpoint)`" \
  --update \
  --ml-model-training-job-id "`(the model-training job-id of a completed job)`"
```

For more information, see [create-ml-endpoint](../../../cli/latest/reference/neptunedata/create-ml-endpoint.md "../../../cli/latest/reference/neptunedata/create-ml-endpoint.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.create_ml_endpoint(
    id='`(a unique ID for the new endpoint)`',
    update=True,
    mlModelTrainingJobId='`(the model-training job-id of a completed job)`'
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/endpoints \
  --region `us-east-1` \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "update" : "true",
        "mlModelTrainingJobId": "`(the model-training job-id of a completed job)`"
      }'
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl \
  -X POST https://`your-neptune-endpoint`:`port`/ml/endpoints \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "update" : "true",
        "mlModelTrainingJobId": "`(the model-training job-id of a completed job)`"
      }'
```

A Neptune ML `endpoints` command for creating an inference endpoint
from a model created by a model-transform job looks like this:

AWS CLI

```
aws neptunedata create-ml-endpoint \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(a unique ID for the new endpoint)`" \
  --ml-model-transform-job-id "`(the model-transform job-id of a completed job)`"
```

For more information, see [create-ml-endpoint](../../../cli/latest/reference/neptunedata/create-ml-endpoint.md "../../../cli/latest/reference/neptunedata/create-ml-endpoint.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.create_ml_endpoint(
    id='`(a unique ID for the new endpoint)`',
    mlModelTransformJobId='`(the model-transform job-id of a completed job)`'
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/endpoints \
  --region `us-east-1` \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "mlModelTransformJobId": "`(the model-transform job-id of a completed job)`"
      }'
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl \
  -X POST https://`your-neptune-endpoint`:`port`/ml/endpoints \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "mlModelTransformJobId": "`(the model-transform job-id of a completed job)`"
      }'
```

A Neptune ML `endpoints` command for updating an existing inference endpoint
from a model created by a model-transform job looks like this:

AWS CLI

```
aws neptunedata create-ml-endpoint \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(a unique ID for the new endpoint)`" \
  --update \
  --ml-model-transform-job-id "`(the model-transform job-id of a completed job)`"
```

For more information, see [create-ml-endpoint](../../../cli/latest/reference/neptunedata/create-ml-endpoint.md "../../../cli/latest/reference/neptunedata/create-ml-endpoint.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.create_ml_endpoint(
    id='`(a unique ID for the new endpoint)`',
    update=True,
    mlModelTransformJobId='`(the model-transform job-id of a completed job)`'
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/endpoints \
  --region `us-east-1` \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "update" : "true",
        "mlModelTransformJobId": "`(the model-transform job-id of a completed job)`"
      }'
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl \
  -X POST https://`your-neptune-endpoint`:`port`/ml/endpoints \
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "update" : "true",
        "mlModelTransformJobId": "`(the model-transform job-id of a completed job)`"
      }'
```

###### Parameters for `endpoints` inference endpoint creation

- **`id`**   –  
  (_Optional_) A unique identifier for the new inference endpoint.

_Type_: string. _Default_: An autogenerated timestamped
name.

- **`mlModelTrainingJobId`**   –  
  The job Id of the completed model-training job that has created the model
  that the inference endpoint will point to.

_Type_: string.

_Note_: You must supply either the `mlModelTrainingJobId`
or the `mlModelTransformJobId`.

- **`mlModelTransformJobId`**   –  
  The job Id of the completed model-transform job.

_Type_: string.

_Note_: You must supply either the `mlModelTrainingJobId`
or the `mlModelTransformJobId`.

- **`update`**   –  
  (_Optional_) If present, this parameter indicates that this is
  an update request.

_Type_: Boolean. _Default_: `false`

_Note_: You must supply either the `mlModelTrainingJobId`
or the `mlModelTransformJobId`.

- **`neptuneIamRoleArn`**   –  
  (_Optional_) The ARN of an IAM role providing Neptune access to
  SageMaker AI and Amazon S3 resources.

_Type_: string. _Note_: This must be
listed in your DB cluster parameter group or an error will be thrown.

- **`modelName`**   –  
  (_Optional_) Model type for training. By default the ML model
  is automatically based on the `modelType` used in data processing, but you
  can specify a different model type here.

_Type_: string. _Default_: `rgcn`
for heterogeneous graphs and `kge` for knowledge graphs.
_Valid values_: For heterogeneous graphs: `rgcn`. For
knowledge graphs: `kge`, `transe`, `distmult`, or `rotate`.

- **`instanceType`**   –  
  (_Optional_) The type of ML instance used for online servicing.

_Type_: string. _Default_: `ml.m5.xlarge`.

_Note_: Choosing the ML instance for an inference endpoint
depends on the task type, the graph size, and your budget. See [Selecting an instance for an inference endpoint](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-inference-endpoint-instance-size "machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-inference-endpoint-instance-size").

- **`instanceCount`**   –  
  (_Optional_) The minimum number of Amazon EC2 instances to deploy to
  an endpoint for prediction.

_Type_: integer. _Default_: `1`.

- **`volumeEncryptionKMSKey`**   –  
  (_Optional_) The AWS Key Management Service (AWS KMS) key that SageMaker AI uses to
  encrypt data on the storage volume attached to the ML compute instance(s)
  that run the endpoints.

_Type_: string. _Default_: _none_.

## Getting the status of an inference endpoint using the Neptune ML `endpoints` command

A sample Neptune ML `endpoints` command for the status of an instance
endpoint looks like this:

AWS CLI

```
aws neptunedata get-ml-endpoint \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(the inference endpoint ID)`"
```

For more information, see [get-ml-endpoint](../../../cli/latest/reference/neptunedata/get-ml-endpoint.md "../../../cli/latest/reference/neptunedata/get-ml-endpoint.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.get_ml_endpoint(
    id='`(the inference endpoint ID)`'
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/endpoints/`(the inference endpoint ID)` \
  --region `us-east-1` \
  --service neptune-db \
  -X GET
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl -s \
  "https://`your-neptune-endpoint`:`port`/ml/endpoints/`(the inference endpoint ID)`" \
  | python -m json.tool
```

###### Parameters for `endpoints` instance-endpoint status

- **`id`**   –  
  (_Required_) The unique identifier of the inference endpoint.

_Type_: string.

- **`neptuneIamRoleArn`**   –  
  (_Optional_) The ARN of an IAM role providing Neptune access to
  SageMaker AI and Amazon S3 resources.

_Type_: string. _Note_: This must be
listed in your DB cluster parameter group or an error will be thrown.

## Deleting an instance endpoint using the Neptune ML `endpoints` command

A sample Neptune ML `endpoints` command for deleting an instance
endpoint looks like this:

AWS CLI

```
aws neptunedata delete-ml-endpoint \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(the inference endpoint ID)`"
```

To also clean up related artifacts:

```
aws neptunedata delete-ml-endpoint \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(the inference endpoint ID)`" \
  --clean
```

For more information, see [delete-ml-endpoint](../../../cli/latest/reference/neptunedata/delete-ml-endpoint.md "../../../cli/latest/reference/neptunedata/delete-ml-endpoint.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.delete_ml_endpoint(
    id='`(the inference endpoint ID)`',
    clean=True
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/endpoints/`(the inference endpoint ID)` \
  --region `us-east-1` \
  --service neptune-db \
  -X DELETE
```

To also clean up related artifacts:

```
awscurl "https://`your-neptune-endpoint`:`port`/ml/endpoints/`(the inference endpoint ID)`?clean=true" \
  --region `us-east-1` \
  --service neptune-db \
  -X DELETE
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl -s \
  -X DELETE "https://`your-neptune-endpoint`:`port`/ml/endpoints/`(the inference endpoint ID)`"
```

Or this:

```
curl -s \
  -X DELETE "https://`your-neptune-endpoint`:`port`/ml/endpoints/`(the inference endpoint ID)`?clean=true"
```

###### Parameters for `endpoints` deleting an inference endpoint

- **`id`**   –  
  (_Required_) The unique identifier of the inference endpoint.

_Type_: string.

- **`neptuneIamRoleArn`**   –  
  (_Optional_) The ARN of an IAM role providing Neptune access to
  SageMaker AI and Amazon S3 resources.

_Type_: string. _Note_: This must be
listed in your DB cluster parameter group or an error will be thrown.

- **`clean`**   –  
  (_Optional_) Indicates that all artifacts related to
  this endpoint should also be deleted.

_Type_: Boolean. _Default_: `FALSE`.

## Listing inference endpoints using the Neptune ML `endpoints` command

A Neptune ML `endpoints` command for listing inference
endpoints looks like this:

AWS CLI

```
aws neptunedata list-ml-endpoints \
  --endpoint-url https://`your-neptune-endpoint`:`port`
```

To limit the number of results:

```
aws neptunedata list-ml-endpoints \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --max-items 3
```

For more information, see [list-ml-endpoints](../../../cli/latest/reference/neptunedata/list-ml-endpoints.md "../../../cli/latest/reference/neptunedata/list-ml-endpoints.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.list_ml_endpoints(
    maxItems=3
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/endpoints \
  --region `us-east-1` \
  --service neptune-db \
  -X GET
```

To limit the number of results:

```
awscurl "https://`your-neptune-endpoint`:`port`/ml/endpoints?maxItems=3" \
  --region `us-east-1` \
  --service neptune-db \
  -X GET
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl -s "https://`your-neptune-endpoint`:`port`/ml/endpoints" \
  | python -m json.tool
```

Or this:

```
curl -s "https://`your-neptune-endpoint`:`port`/ml/endpoints?maxItems=3" \
  | python -m json.tool
```

###### Parameters for `dataprocessing` list inference endpoints

- **`maxItems`**   –  
  (_Optional_) The maximum number of items to return.

_Type_: integer. _Default_: `10`.
_Maximum allowed value_: `1024`.

- **`neptuneIamRoleArn`**   –  
  (_Optional_) The ARN of an IAM role providing Neptune access to
  SageMaker AI and Amazon S3 resources.

_Type_: string. _Note_: This must be
listed in your DB cluster parameter group or an error will be thrown.
