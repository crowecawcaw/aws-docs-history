

# Creating an inference endpoint to query
<a name="machine-learning-on-graphs-inference-endpoint"></a>

An inference endpoint lets you query one specific model that the model-training process constructed. The endpoint attaches to the best-performing model of a given type that the training process was able to generate. The endpoint is then able to accept Gremlin queries from Neptune and return that model's predictions for inputs in the queries. After you have created an inference endpoint, it stays active until you delete it.

## Managing inference endpoints for Neptune ML
<a name="machine-learning-on-graphs-endpoint-managing"></a>

After you have completed model training on data that you exported from Neptune, you can create an inference endpoint using a command like the following:

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

You can also create an inference endpoint from a model created by a completed model transform job, in much the same way:

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

The details of how to use these commands are explained in [The endpoints command](machine-learning-api-endpoints.md), along with information about how to get the status of an endpoint, how to delete an endpoint, and how to list all inference endpoints.