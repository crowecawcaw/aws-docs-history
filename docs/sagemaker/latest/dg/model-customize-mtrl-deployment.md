

# Model deployment
<a name="model-customize-mtrl-deployment"></a>

 After your training job completes, the trained model is available as a Model Package in your Output Model Package Group. You have two options for deploying it. 

## Option 1: Deploy with SageMaker AI AI Inference
<a name="model-customize-mtrl-deployment-sagemaker"></a>

 Host your model on a SageMaker AI AI inference endpoint for real-time, serverless, or asynchronous predictions. This option gives you fine-grained control over instance types, scaling policies, and network configuration. It's a good fit when you need low-latency serving, custom inference logic, or tight integration with existing SageMaker AI AI workflows. 

 To deploy, retrieve the `OutputModelPackageArn` from your completed training job and use it to create an endpoint. 

```
# Retrieve the output model ARN from your completed job
aws sagemaker describe-job \
  --job-name "my-agent-rft-job" \
  --job-category AgentRFT \
  --region us-west-2
```

 For full deployment options and configuration, see [Deploy models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) in the SageMaker AI AI documentation. 

## Option 2: Import into Amazon Bedrock
<a name="model-customize-mtrl-deployment-bedrock"></a>

 Import your model into Amazon Bedrock to use Bedrock's managed inference APIs with no endpoint configuration required. Amazon Bedrock supports importing customized open-source foundation models (such as Mistral AI or Llama) and Amazon Nova models fine-tuned in SageMaker AI AI. For more information, see [Import a pre-trained model into Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/import-pre-trained-model.html) in the Amazon Bedrock User Guide. For Nova models, see [Import with create custom model](https://docs.aws.amazon.com/bedrock/latest/userguide/import-with-create-custom-model.html). 

## Deploy using SageMaker AI Studio
<a name="model-customize-mtrl-deployment-studio"></a>
+ Navigate to **Jobs > Training** and select the **Multi-turn RL** tab.
+ Select a completed job and choose the model under **Custom Model Details** to review performance metrics, model lineage, and training logs.
+ Under the **Governance** tab, approve the model to make it eligible for deployment.
+ Choose **Deploy**. Select whether to deploy to a SageMaker AI AI real-time endpoint or through Amazon Bedrock, and whether to create a new endpoint or reuse an existing one.
+ Select the instance type and optionally configure VPC settings, IAM role, and KMS encryption key.
+ Monitor deployment progress under the **Deployments** tab.
+ Navigate to **Deployments > Endpoints**. When your endpoint and associated inference components reach a status of InService, your endpoint is ready for invocation.

## Deploy using SageMaker AI Python SDK
<a name="model-customize-mtrl-deployment-python-sdk"></a>

 Deploy to a SageMaker AI endpoint: 

```
from sagemaker.serve import ModelBuilder
from sagemaker.core.resources import ModelPackage

# Get the output model package from your completed training job
model_package = ModelPackage.get(
    model_package_name=job.output_model_package_arn
)

model_builder = ModelBuilder(
    model=model_package,
    image_uri="763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.36.0-lmi24.0.0-cu129",
    instance_type="ml.g6e.48xlarge",
)
model_builder.accept_eula = True
model_builder.build()

endpoint = model_builder.deploy(
    endpoint_name="mtrl-finetuned-endpoint",
    instance_type="ml.g6e.48xlarge",
    initial_instance_count=1,
)
```

 Invoke the endpoint: 

```
import json

response = endpoint.invoke(
    body=json.dumps({
        "model": "/opt/ml/model",
        "messages": [{"role": "user", "content": "What is 25 * 4?"}],
        "max_tokens": 200,
        "stream": False,
    }).encode("utf-8"),
    content_type="application/json",
)
```