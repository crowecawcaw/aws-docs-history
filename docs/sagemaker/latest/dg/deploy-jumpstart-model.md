

# Deploy a JumpStart model
<a name="deploy-jumpstart-model"></a>

You can deploy a pre-trained JumpStart model for inference using either the CLI or the SDK.

## Using the CLI
<a name="deploy-jumpstart-cli"></a>

Run the following command to deploy a JumpStart model:

```
hyp create hyp-jumpstart-endpoint \
  --version 1.0 \
  --model-id deepseek-llm-r1-distill-qwen-1-5b \
  --instance-type ml.g5.8xlarge \
  --endpoint-name endpoint-test-jscli
```

## Using the SDK
<a name="deploy-jumpstart-sdk"></a>

Create a Python script with the following content:

```
from sagemaker.hyperpod.inference.config.hp_jumpstart_endpoint_config import Model, Server, SageMakerEndpoint, TlsConfig
from sagemaker.hyperpod.inference.hp_jumpstart_endpoint import HPJumpStartEndpoint

model=Model(
    model_id='deepseek-llm-r1-distill-qwen-1-5b'
)

server=Server(
    instance_type='ml.g5.8xlarge',
)

endpoint_name=SageMakerEndpoint(name='{{<endpoint-name>}}')

# create spec
js_endpoint=HPJumpStartEndpoint(
    model=model,
    server=server,
    sage_maker_endpoint=endpoint_name
)
```

## Invoke the endpoint
<a name="invoke-jumpstart-endpoint"></a>

### Using the CLI
<a name="invoke-jumpstart-cli"></a>

Test the endpoint with a sample input:

```
hyp invoke hyp-jumpstart-endpoint \
    --endpoint-name endpoint-jumpstart \
    --body '{"inputs":"What is the capital of USA?"}'
```

### Using the SDK
<a name="invoke-jumpstart-sdk"></a>

Add the following code to your Python script:

```
data = '{"inputs":"What is the capital of USA?"}'
response = js_endpoint.invoke(body=data).body.read()
print(response)
```

## Manage the endpoint
<a name="manage-jumpstart-endpoint"></a>

### Using the CLI
<a name="manage-jumpstart-cli"></a>

List and inspect the endpoint:

```
hyp list hyp-jumpstart-endpoint
hyp get hyp-jumpstart-endpoint --name endpoint-jumpstart
```

### Using the SDK
<a name="manage-jumpstart-sdk"></a>

Add the following code to your Python script:

```
endpoint_iterator = HPJumpStartEndpoint.list()
for endpoint in endpoint_iterator:
    print(endpoint.name, endpoint.status)

logs = js_endpoint.get_logs()
print(logs)
```

## Clean up resources
<a name="cleanup-jumpstart-resources"></a>

When you're done, delete the endpoint to avoid unnecessary costs.

### Using the CLI
<a name="cleanup-jumpstart-cli"></a>

```
hyp delete hyp-jumpstart-endpoint --name endpoint-jumpstart
```

### Using the SDK
<a name="cleanup-jumpstart-sdk"></a>

```
js_endpoint.delete()
```

## Next steps
<a name="jumpstart-next-steps"></a>

Now that you've trained a PyTorch model, deployed it as a custom endpoint, and deployed a JumpStart model using HyperPod's CLI and SDK, explore advanced features:
+ **Multi-node training**: Scale training across multiple instances
+ **Custom containers**: Build specialized training environments
+ **Integration with SageMaker Pipelines**: Automate your ML workflows
+ **Advanced monitoring**: Set up custom metrics and alerts

For more examples and advanced configurations, visit the [SageMaker HyperPod GitHub repository](https://github.com/aws/amazon-sagemaker-examples).