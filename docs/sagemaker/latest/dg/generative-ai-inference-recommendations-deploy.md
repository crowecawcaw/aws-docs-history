

# Deploy a generative AI inference recommendation
<a name="generative-ai-inference-recommendations-deploy"></a>

When a recommendation job completes, each recommendation includes a deployment-ready configuration. You can deploy the chosen configuration to a SageMaker AI inference endpoint with a single action from SageMaker AI Studio, or programmatically through the API.

## Understanding deployment configurations
<a name="generative-ai-inference-recommendations-deploy-overview"></a>

Each recommendation in the job response contains a `DeploymentConfiguration` object with the following information:

`ImageUri`  
The container image URI optimized for the recommended instance type.

`InstanceType`  
The recommended instance type for deployment.

`InstanceCount`  
The number of instances needed to meet the performance target.

`CopyCountPerInstance`  
The number of model copies to run per instance. When set to a value greater than one, multiple copies of the model are loaded on each instance to increase throughput.

`EnvironmentVariables`  
Environment variables configured for optimal performance, such as tensor parallel size and maximum sequence length.

`S3`  
S3 channel references for model artifacts, including any optimized model outputs.

## Deploy using the API
<a name="generative-ai-inference-recommendations-deploy-api"></a>

To deploy a recommendation programmatically, use the model package from the recommendation to create a SageMaker AI model and endpoint. Each recommendation includes a `ModelDetails` object with the model package ARN and inference specification name. This is the simplest deployment path because the model package already contains the container image, environment variables, and model artifact channels.

```
import boto3

client = boto3.client("sagemaker", region_name="us-west-2")

# Get the recommendation from a completed job
response = client.describe_ai_recommendation_job(
    AIRecommendationJobName="my-recommendation-job"
)

# Select a recommendation (e.g., the first one)
recommendation = response["Recommendations"][0]
model_details = recommendation["ModelDetails"]
deploy_config = recommendation["DeploymentConfiguration"]

# Create a model from the model package.
# The model package already contains the container image, environment
# variables, and S3 data channels (base model + optimization artifacts).
model_name = "my-recommended-model"
container_def = {
    "ModelPackageName": model_details["ModelPackageArn"],
}
# If the recommendation uses a named inference specification (e.g., for
# a specific optimization variant), specify it so SageMaker selects the
# correct container and instance configuration from the model package.
if model_details.get("InferenceSpecificationName"):
    container_def["InferenceSpecificationName"] = model_details["InferenceSpecificationName"]

client.create_model(
    ModelName=model_name,
    PrimaryContainer=container_def,
    ExecutionRoleArn="arn:aws:iam::111122223333:role/ExampleRole",
)

# Create an endpoint configuration
endpoint_config_name = "my-recommended-endpoint-config"
production_variant = {
    "VariantName": "AllTraffic",
    "ModelName": model_name,
    "InstanceType": deploy_config["InstanceType"],
    "InitialInstanceCount": deploy_config.get("InstanceCount", 1),
}
copy_count = deploy_config.get("CopyCountPerInstance")
if copy_count and copy_count > 1:
    production_variant["InferenceAmiVersion"] = "al2-ami-sagemaker-inference-gpu-2"
    production_variant["RoutingConfig"] = {"RoutingStrategy": "LEAST_OUTSTANDING_REQUESTS"}

client.create_endpoint_config(
    EndpointConfigName=endpoint_config_name,
    ProductionVariants=[production_variant],
)

# Create the endpoint
endpoint_name = "my-recommended-endpoint"
client.create_endpoint(
    EndpointName=endpoint_name,
    EndpointConfigName=endpoint_config_name,
)
print(f"Endpoint {endpoint_name} is being created.")
```

After the endpoint is created, you can monitor its status using the `DescribeEndpoint` API until it reaches `InService` status.

```
import time

while True:
    response = client.describe_endpoint(EndpointName=endpoint_name)
    status = response["EndpointStatus"]
    print(f"Endpoint status: {status}")
    if status in ("InService", "Failed"):
        break
    time.sleep(60)
```

## Deploy from SageMaker AI Studio
<a name="generative-ai-inference-recommendations-deploy-studio"></a>

You can also deploy a recommended configuration directly from SageMaker AI Studio with a single action. In SageMaker AI Studio, navigate to the completed recommendation job, review the recommendations and their performance metrics, and choose the configuration you want to deploy.