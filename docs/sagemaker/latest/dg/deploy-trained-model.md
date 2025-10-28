# Deploy a custom model

After training completes, deploy your model for inference. You can deploy a custom model using either the CLI or the SDK.

## Locate your model artifacts

- **Check your S3 bucket**: Verify that model artifacts are saved at `s3://my-bucket/model-artifacts/`
- **Note the exact path**: You'll need the full path (for example, `s3://my-bucket/model-artifacts/test-pytorch-job/model.tar.gz`)

## Deploy using the CLI

Run the following command to deploy your custom model:

```
hyp create hyp-custom-endpoint \
    --version 1.0 \
    --env '{"HF_MODEL_ID":"/opt/ml/model", "SAGEMAKER_PROGRAM":"inference.py", }' \
    --model-source-type s3 \
    --model-location test-pytorch-job \
    --s3-bucket-name my-bucket \
    --s3-region us-east-2 \
    --prefetch-enabled true \
    --image-uri 763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:latest \
    --model-volume-mount-name model-weights \
    --container-port 8080 \
    --resources-requests '{"cpu": "30000m", "nvidia.com/gpu": 1, "memory": "100Gi"}' \
    --resources-limits '{"nvidia.com/gpu": 1}' \
    --tls-output-s3-uri s3://`<bucket_name>` \
    --instance-type ml.g5.8xlarge \
    --endpoint-name endpoint-custom-pytorch \
    --model-name pytorch-custom-model
```

This command deploys the trained model as an endpoint named `endpoint-custom-pytorch`.
The `--model-location` references the artifact path from the training job.

## Deploy using the Python SDK

Create a Python script with the following content:

```
from sagemaker.hyperpod.inference.config.hp_custom_endpoint_config import Model, Server, SageMakerEndpoint, TlsConfig, EnvironmentVariables
from sagemaker.hyperpod.inference.hp_custom_endpoint import HPCustomEndpoint

model = Model(
    model_source_type="s3",
    model_location="test-pytorch-job",
    s3_bucket_name="my-bucket",
    s3_region="us-east-2",
    prefetch_enabled=True
)

server = Server(
    instance_type="ml.g5.8xlarge",
    image_uri="763104351884.dkr.ecr.us-east-2.amazonaws.com/huggingface-pytorch-tgi-inference:2.4.0-tgi2.3.1-gpu-py311-cu124-ubuntu22.04-v2.0",
    container_port=8080,
    model_volume_mount_name="model-weights"
)

resources = {
    "requests": {"cpu": "30000m", "nvidia.com/gpu": 1, "memory": "100Gi"},
    "limits": {"nvidia.com/gpu": 1}
}

env = EnvironmentVariables(
    HF_MODEL_ID="/opt/ml/model",
    SAGEMAKER_PROGRAM="inference.py",
    SAGEMAKER_SUBMIT_DIRECTORY="/opt/ml/model/code",
    MODEL_CACHE_ROOT="/opt/ml/model",
    SAGEMAKER_ENV="1"
)

endpoint_name = SageMakerEndpoint(name="endpoint-custom-pytorch")

tls_config = TlsConfig(tls_certificate_output_s3_uri="s3://`<bucket_name>`")

custom_endpoint = HPCustomEndpoint(
    model=model,
    server=server,
    resources=resources,
    environment=env,
    sage_maker_endpoint=endpoint_name,
    tls_config=tls_config
)

custom_endpoint.create()
```

## Invoke the endpoint

### Using the CLI

Test the endpoint with a sample input:

```
hyp invoke hyp-custom-endpoint \
    --endpoint-name endpoint-custom-pytorch \
    --body '{"inputs":"What is the capital of USA?"}'
```

This returns the model’s response, such as “The capital of the USA is Washington, D.C.”

### Using the SDK

Add the following code to your Python script:

```
data = '{"inputs":"What is the capital of USA?"}'
response = custom_endpoint.invoke(body=data).body.read()
print(response)
```

## Manage the endpoint

### Using the CLI

List and inspect the endpoint:

```
hyp list hyp-custom-endpoint
hyp get hyp-custom-endpoint --name endpoint-custom-pytorch
```

### Using the SDK

Add the following code to your Python script:

```
logs = custom_endpoint.get_logs()
print(logs)
```

## Clean up resources

When you're done, delete the endpoint to avoid unnecessary costs.

### Using the CLI

```
hyp delete hyp-custom-endpoint --name endpoint-custom-pytorch
```

### Using the SDK

```
custom_endpoint.delete()
```

## Next steps

You've successfully deployed and tested a custom model using SageMaker HyperPod. You can now use this endpoint for inference in your applications.
