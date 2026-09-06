

# Getting Started
<a name="nova-sagemaker-inference-getting-started"></a>

This guide shows you how to deploy customized Amazon Nova models on SageMaker real-time endpoints, configure inference parameters, and invoke your models for testing.

## Prerequisites
<a name="nova-sagemaker-inference-prerequisites"></a>

The following are prerequisites to deploy Amazon Nova models on SageMaker inference:
+ Create an AWS account - If you don't have one already, see [Creating an AWS account](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-set-up.html#sign-up-for-aws).
+ Required IAM permissions - Ensure your IAM user or role has the following managed policies attached:
  + `AmazonSageMakerFullAccess`
  + `AmazonS3FullAccess`
+ Required SDKs/CLI versions - The following SDK versions have been tested and validated with Amazon Nova models on SageMaker inference:
  + SageMaker Python SDK v3.0.0\+ (`sagemaker>=3.0.0`) for resource-based API approach
  + Boto3 version 1.35.0\+ (`boto3>=1.35.0`) for direct API calls. The examples in this guide use this approach.
+ Service quota increase - Request an Amazon SageMaker service quota increase for the ML instance type you plan to use for your SageMaker Inference endpoint (for example, `ml.p5.48xlarge for endpoint usage`). For a list of supported instance types, see [Supported models and instances](nova-model-sagemaker-inference.md#nova-sagemaker-inference-supported). To request an increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html). For information about SageMaker instance quotas, see [SageMaker endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html).

**Tip**  
For a quick end-to-end deployment, you can run the [Custom Nova Model SageMaker Inference notebook](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/Nova_2.0/05_deployment/Custom-Nova-Model-SageMaker-Inference.ipynb) to deploy a customized Amazon Nova model on SageMaker inference in a single notebook.

## Step 1: Configure AWS credentials
<a name="nova-sagemaker-inference-step1"></a>

Configure your AWS credentials using one of the following methods:

**Option 1: AWS CLI (Recommended)**

```
aws configure
```

Enter your AWS access key, secret key, and default region when prompted.

**Option 2: AWS credentials file**

Create or edit `~/.aws/credentials`:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

**Option 3: Environment variables**

```
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
```

**Note**  
For more information about AWS credentials, see [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

**Initialize AWS clients**

Create a Python script or notebook with the following code to initialize the AWS SDK and verify your credentials:

```
import boto3

# AWS Configuration - Update these for your environment
REGION = "us-east-1"  # Supported regions: us-east-1, us-west-2
AWS_ACCOUNT_ID = "YOUR_ACCOUNT_ID"  # Replace with your AWS account ID

# Initialize AWS clients using default credential chain
sagemaker = boto3.client('sagemaker', region_name=REGION)
sts = boto3.client('sts')

# Verify credentials
try:
    identity = sts.get_caller_identity()
    print(f"Successfully authenticated to AWS Account: {identity['Account']}")
    
    if identity['Account'] != AWS_ACCOUNT_ID:
        print(f"Warning: Connected to account {identity['Account']}, expected {AWS_ACCOUNT_ID}")

except Exception as e:
    print(f"Failed to authenticate: {e}")
    print("Please verify your credentials are configured correctly.")
```

If the authentication is successful, you should see output confirming your AWS account ID.

## Step 2: Create a SageMaker execution role
<a name="nova-sagemaker-inference-step2"></a>

A SageMaker execution role is an IAM role that grants SageMaker permissions to access AWS resources on your behalf, such as Amazon S3 buckets for model artifacts and CloudWatch for logging.

**Creating the execution role**

**Note**  
Creating IAM roles requires `iam:CreateRole` and `iam:AttachRolePolicy` permissions. Ensure your IAM user or role has these permissions before proceeding.

The following code creates an IAM role with the necessary permissions for deploying Amazon Nova customized models:

```
import json

# Create SageMaker Execution Role
role_name = f"SageMakerInference-ExecutionRole-{AWS_ACCOUNT_ID}"

trust_policy = {
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "sagemaker.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
}

iam = boto3.client('iam', region_name=REGION)

# Create the role
role_response = iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(trust_policy),
    Description='SageMaker execution role with S3 and SageMaker access'
)

# Attach required policies
iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'
)

iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
)

SAGEMAKER_EXECUTION_ROLE_ARN = role_response['Role']['Arn']
print(f"Created SageMaker execution role: {SAGEMAKER_EXECUTION_ROLE_ARN}")
```

**Using an existing execution role (Optional)**

If you already have a SageMaker execution role, you can use it instead:

```
# Replace with your existing role ARN
SAGEMAKER_EXECUTION_ROLE_ARN = "arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_EXISTING_ROLE_NAME"
```

To find existing SageMaker roles in your account:

```
iam = boto3.client('iam', region_name=REGION)
response = iam.list_roles()
sagemaker_roles = [role for role in response['Roles'] if 'SageMaker' in role['RoleName']]
for role in sagemaker_roles:
    print(f"{role['RoleName']}: {role['Arn']}")
```

**Important**  
The execution role must have trust relationship with `sagemaker.amazonaws.com` and permissions to access Amazon S3 and SageMaker resources.

For more information about SageMaker execution roles, see [SageMaker Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html).

## Step 3: Configure model parameters
<a name="nova-sagemaker-inference-step3"></a>

Configure the deployment parameters for your Amazon Nova model. These settings control model behavior, resource allocation, and inference characteristics. For a list of supported instance types and supported CONTEXT\_LENGTH and MAX\_CONCURRENCY values for each, see [Supported models and instances](nova-model-sagemaker-inference.md#nova-sagemaker-inference-supported). For a complete list of additional container features such as sampling defaults, speculative decoding, and quantization, see [Inference Container Features](nova-sagemaker-inference-container-features.md).

**Required parameters**
+ `IMAGE`: The Docker container image URI for Amazon Nova inference container. This will be provided by AWS.
+ `CONTEXT_LENGTH`: Model context length.
+ `MAX_CONCURRENCY`: Maximum number of sequences per iteration; sets the limit on how many individual user requests (prompts) can be processed concurrently within a single batch on the GPU. Range: integer greater than 0.

**Configure your deployment**

```
# AWS Configuration
REGION = "us-east-1"  # Must match region from Step 1

# ECR Account mapping by region
ECR_ACCOUNT_MAP = {
    "us-east-1": "708977205387",
    "us-west-2": "176779409107"
}

# Container Image
IMAGE = f"{ECR_ACCOUNT_MAP[REGION]}.dkr.ecr.{REGION}.amazonaws.com/nova-inference-repo:SM-Inference-latest"
print(f"IMAGE = {IMAGE}")

# Required parameters
CONTEXT_LENGTH = "16000"       # Maximum total context length
MAX_CONCURRENCY = "2"          # Maximum concurrent sequences

# Build environment variables for the container
environment = {
    'CONTEXT_LENGTH': CONTEXT_LENGTH,
    'MAX_CONCURRENCY': MAX_CONCURRENCY,
    # Optional: add container feature environment variables here.
    # See "Inference Container Features" for the full list.
    # Examples:
    # 'DEFAULT_TEMPERATURE': '0.7',
    # 'DEFAULT_MAX_NEW_TOKENS': '512',
    # 'QUANTIZATION_DTYPE': 'fp8',
}

print("Environment configuration:")
for key, value in environment.items():
    print(f"  {key}: {value}")
```

**Configure deployment-specific parameters**

Now configure the specific parameters for your Amazon Nova model deployment, including model artifacts location and instance type selection.

**Set deployment identifier**

```
# Deployment identifier - use a descriptive name for your use case
JOB_NAME = "my-nova-deployment"
```

**Specify model artifacts location**

Provide the Amazon S3 URI where your trained Amazon Nova model artifacts are stored. This should be the output location from your model training or fine-tuning job.

```
# S3 location of your trained Nova model artifacts
# Replace with your model's S3 URI - must end with /
MODEL_S3_LOCATION = "s3://your-bucket-name/path/to/model/artifacts/"
```

**Select model variant and instance type**

```
# Configure model variant and instance type
TESTCASE = {
    "model": "lite2",              # Options: micro, lite, lite2
    "instance": "ml.p5.48xlarge"   # Refer to "Supported models and instances" section
}

# Generate resource names
INSTANCE_TYPE = TESTCASE["instance"]
MODEL_NAME = JOB_NAME + "-" + TESTCASE["model"] + "-" + INSTANCE_TYPE.replace(".", "-")
ENDPOINT_CONFIG_NAME = MODEL_NAME + "-Config"
ENDPOINT_NAME = MODEL_NAME + "-Endpoint"

print(f"Model Name: {MODEL_NAME}")
print(f"Endpoint Config: {ENDPOINT_CONFIG_NAME}")
print(f"Endpoint Name: {ENDPOINT_NAME}")
```

**Naming conventions**

The code automatically generates consistent names for AWS resources:
+ Model Name: `{JOB_NAME}-{model}-{instance-type}`
+ Endpoint Config: `{MODEL_NAME}-Config`
+ Endpoint Name: `{MODEL_NAME}-Endpoint`

## Step 4: Create SageMaker resources and deploy the endpoint
<a name="nova-sagemaker-inference-step4"></a>

SageMaker offers two approaches for deploying models to real-time endpoints. Choose the approach that fits your use case:
+ **Inference components** (Recommended): Deploys models as inference components on an endpoint. This approach enables you to host multiple models on a single endpoint, scale models independently, and optimize resource utilization.
+ **Single model endpoints**: Deploys a single model directly to an endpoint using a model object and endpoint configuration. This approach is simpler to set up and suitable for development, testing, or workloads that require only one model per endpoint.

### Option A: Creating with inference components
<a name="nova-sagemaker-inference-step4-ic"></a>

With inference components, you first create an endpoint, then deploy your model as an inference component on that endpoint. This decouples the model from the endpoint infrastructure, giving you more flexibility.

**Create the endpoint configuration**

Create an endpoint configuration that defines the infrastructure without specifying a model. The instance type and count are managed at the endpoint level:

```
# Create Endpoint Configuration for inference components
INFERENCE_COMPONENT_NAME = MODEL_NAME + "-IC"

try:
    config_response = sagemaker.create_endpoint_config(
        EndpointConfigName=ENDPOINT_CONFIG_NAME,
        ProductionVariants=[
            {
                'VariantName': 'primary',
                'InstanceType': INSTANCE_TYPE,
                'InitialInstanceCount': 1,
                'RoutingConfig': {
                    'RoutingStrategy': 'LEAST_OUTSTANDING_REQUESTS'
                }
            }
        ],
        Tags=[
            {
                'Key': 'sagemaker:nova-inference-component',
                'Value': 'true'
            }
        ]
    )
    print("Endpoint configuration created successfully!")
    print(f"Config ARN: {config_response['EndpointConfigArn']}")

except sagemaker.exceptions.ClientError as e:
    print(f"Error creating endpoint configuration: {e}")
```

**Create and deploy the endpoint**

```
import time

try:
    endpoint_response = sagemaker.create_endpoint(
        EndpointName=ENDPOINT_NAME,
        EndpointConfigName=ENDPOINT_CONFIG_NAME
    )
    print("Endpoint creation initiated successfully!")
    print(f"Endpoint ARN: {endpoint_response['EndpointArn']}")
except Exception as e:
    print(f"Error creating endpoint: {e}")

# Wait for endpoint to be InService
print("Waiting for endpoint to be InService...")
print("This typically takes 5-10 minutes...\n")

while True:
    try:
        response = sagemaker.describe_endpoint(EndpointName=ENDPOINT_NAME)
        status = response['EndpointStatus']
        
        if status == 'Creating':
            print(f"⏳ Status: {status} - Provisioning infrastructure...")
        elif status == 'InService':
            print(f"✅ Status: {status}")
            print(f"\nEndpoint '{ENDPOINT_NAME}' is ready.")
            break
        elif status == 'Failed':
            print(f"❌ Status: {status}")
            print(f"Failure Reason: {response.get('FailureReason', 'Unknown')}")
            break
        else:
            print(f"Status: {status}")
    except Exception as e:
        print(f"Error checking endpoint status: {e}")
        break
    
    time.sleep(30)
```

**Create the inference component**

Once the endpoint is InService, deploy your Amazon Nova model as an inference component:

```
try:
    ic_response = sagemaker.create_inference_component(
        InferenceComponentName=INFERENCE_COMPONENT_NAME,
        EndpointName=ENDPOINT_NAME,
        VariantName='primary',
        Specification={
            'Container': {
                'Image': IMAGE,
                'ArtifactUrl': MODEL_S3_LOCATION,
                'Environment': environment
            },
            'ComputeResourceRequirements': {
                'NumberOfCpuCoresRequired': 15,
                'NumberOfAcceleratorDevicesRequired': 4,
                'MinMemoryRequiredInMb': 25000
            }
        },
        RuntimeConfig={
            'CopyCount': 1
        }
    )
    print("Inference component creation initiated!")
    print(f"Inference Component ARN: {ic_response['InferenceComponentArn']}")

except sagemaker.exceptions.ClientError as e:
    print(f"Error creating inference component: {e}")
```

Key parameters:
+ `InferenceComponentName`: Unique identifier for your inference component
+ `EndpointName`: The endpoint to deploy the component on
+ `Image`: Docker container image URI for Amazon Nova inference
+ `ArtifactUrl`: Amazon S3 location of your model artifacts
+ `Environment`: Environment variables configured in Step 3
+ `NumberOfCpuCoresRequired`: Number of CPU cores required per model copy
+ `NumberOfAcceleratorDevicesRequired`: Number of accelerator devices (GPUs) required per model copy
+ `MinMemoryRequiredInMb`: Minimum memory in MB required per model copy
+ `CopyCount`: Number of model copies to deploy

**Monitor inference component deployment**

```
# Wait for inference component to be InService
print("Waiting for inference component deployment...")
print("This typically takes 10-20 minutes as the model is loaded...\n")

while True:
    try:
        ic_desc = sagemaker.describe_inference_component(
            InferenceComponentName=INFERENCE_COMPONENT_NAME
        )
        ic_status = ic_desc['InferenceComponentStatus']
        
        if ic_status == 'Creating':
            print(f"⏳ Status: {ic_status} - Loading model artifacts...")
        elif ic_status == 'InService':
            print(f"✅ Status: {ic_status}")
            print(f"\nInference component '{INFERENCE_COMPONENT_NAME}' is ready!")
            break
        elif ic_status == 'Failed':
            print(f"❌ Status: {ic_status}")
            print(f"Failure Reason: {ic_desc.get('FailureReason', 'Unknown')}")
            break
        else:
            print(f"Status: {ic_status}")
    except Exception as e:
        print(f"Error checking inference component status: {e}")
        break
    
    time.sleep(30)
```

**Note**  
When invoking the endpoint in Step 5, you must include the `InferenceComponentName` parameter in your invoke calls. See Step 5 for details.

### Option B: Creating with single model endpoints
<a name="nova-sagemaker-inference-step4-single"></a>

With single model endpoints, you create a SageMaker model object, an endpoint configuration, and then deploy the endpoint. This approach packages the model directly into the endpoint configuration.

**Create the SageMaker model**

The following code creates a SageMaker model that references your Amazon Nova model artifacts:

```
try:
    model_response = sagemaker.create_model(
        ModelName=MODEL_NAME,
        PrimaryContainer={
            'Image': IMAGE,
            'ModelDataSource': {
                'S3DataSource': {
                    'S3Uri': MODEL_S3_LOCATION,
                    'S3DataType': 'S3Prefix',
                    'CompressionType': 'None'
                }
            },
            'Environment': environment
        },
        ExecutionRoleArn=SAGEMAKER_EXECUTION_ROLE_ARN,
        EnableNetworkIsolation=True
    )
    print("Model created successfully!")
    print(f"Model ARN: {model_response['ModelArn']}")
    
except sagemaker.exceptions.ClientError as e:
    print(f"Error creating model: {e}")
```

Key parameters:
+ `ModelName`: Unique identifier for your model
+ `Image`: Docker container image URI for Amazon Nova inference
+ `ModelDataSource`: Amazon S3 location of your model artifacts
+ `Environment`: Environment variables configured in Step 3
+ `ExecutionRoleArn`: IAM role from Step 2
+ `EnableNetworkIsolation`: Set to True for enhanced security (prevents container from making outbound network calls)

**Create the endpoint configuration**

Next, create an endpoint configuration that defines your deployment infrastructure:

```
# Create Endpoint Configuration
try:
    production_variant = {
        'VariantName': 'primary',
        'ModelName': MODEL_NAME,
        'InitialInstanceCount': 1,
        'InstanceType': INSTANCE_TYPE,
    }
    
    config_response = sagemaker.create_endpoint_config(
        EndpointConfigName=ENDPOINT_CONFIG_NAME,
        ProductionVariants=[production_variant]
    )
    print("Endpoint configuration created successfully!")
    print(f"Config ARN: {config_response['EndpointConfigArn']}")
    
except sagemaker.exceptions.ClientError as e:
    print(f"Error creating endpoint configuration: {e}")
```

Key parameters:
+ `VariantName`: Identifier for this model variant (use 'primary' for single-model deployments)
+ `ModelName`: References the model created above
+ `InitialInstanceCount`: Number of instances to deploy (start with 1, scale later if needed)
+ `InstanceType`: ML instance type selected in Step 3

**Deploy the endpoint**

```
import time

try:
    endpoint_response = sagemaker.create_endpoint(
        EndpointName=ENDPOINT_NAME,
        EndpointConfigName=ENDPOINT_CONFIG_NAME
    )
    print("Endpoint creation initiated successfully!")
    print(f"Endpoint ARN: {endpoint_response['EndpointArn']}")
except Exception as e:
    print(f"Error creating endpoint: {e}")
```

**Monitor endpoint creation**

The following code polls the endpoint status until deployment is complete:

```
# Monitor endpoint creation progress
print("Waiting for endpoint creation to complete...")
print("This typically takes 15-30 minutes...\n")

while True:
    try:
        response = sagemaker.describe_endpoint(EndpointName=ENDPOINT_NAME)
        status = response['EndpointStatus']
        
        if status == 'Creating':
            print(f"⏳ Status: {status} - Provisioning infrastructure and loading model...")
        elif status == 'InService':
            print(f"✅ Status: {status}")
            print("\nEndpoint creation completed successfully!")
            print(f"Endpoint Name: {ENDPOINT_NAME}")
            print(f"Endpoint ARN: {response['EndpointArn']}")
            break
        elif status == 'Failed':
            print(f"❌ Status: {status}")
            print(f"Failure Reason: {response.get('FailureReason', 'Unknown')}")
            print("\nFull response:")
            print(response)
            break
        else:
            print(f"Status: {status}")
        
    except Exception as e:
        print(f"Error checking endpoint status: {e}")
        break
    
    time.sleep(30)  # Check every 30 seconds
```

**Verify resource creation**

You can verify that your resources were created successfully:

```
# Describe the model
model_info = sagemaker.describe_model(ModelName=MODEL_NAME)
print(f"Model Status: {model_info['ModelName']} created")

# Describe the endpoint configuration
config_info = sagemaker.describe_endpoint_config(EndpointConfigName=ENDPOINT_CONFIG_NAME)
print(f"Endpoint Config Status: {config_info['EndpointConfigName']} created")
```

**Verify endpoint is ready**

Regardless of which approach you chose, you can verify the endpoint configuration:

```
# Get detailed endpoint information
endpoint_info = sagemaker.describe_endpoint(EndpointName=ENDPOINT_NAME)

print("\n=== Endpoint Details ===")
print(f"Endpoint Name: {endpoint_info['EndpointName']}")
print(f"Endpoint ARN: {endpoint_info['EndpointArn']}")
print(f"Status: {endpoint_info['EndpointStatus']}")
print(f"Creation Time: {endpoint_info['CreationTime']}")
print(f"Last Modified: {endpoint_info['LastModifiedTime']}")

# Get endpoint config for instance type details
endpoint_config_name = endpoint_info['EndpointConfigName']
endpoint_config = sagemaker.describe_endpoint_config(EndpointConfigName=endpoint_config_name)

# Display production variant details
for variant in endpoint_info['ProductionVariants']:
    print(f"\nProduction Variant: {variant['VariantName']}")
    print(f"  Current Instance Count: {variant['CurrentInstanceCount']}")
    print(f"  Desired Instance Count: {variant['DesiredInstanceCount']}")
    # Get instance type from endpoint config
    for config_variant in endpoint_config['ProductionVariants']:
        if config_variant['VariantName'] == variant['VariantName']:
            print(f"  Instance Type: {config_variant['InstanceType']}")
            break
```

**Troubleshooting endpoint creation failures**

Common failure reasons:
+ **Insufficient capacity**: The requested instance type is not available in your region
  + Solution: Try a different instance type or request a quota increase
+ **IAM permissions**: The execution role lacks necessary permissions
  + Solution: Verify the role has access to Amazon S3 model artifacts and necessary SageMaker permissions
+ **Model artifacts not found**: The Amazon S3 URI is incorrect or inaccessible
  + Solution: Verify the Amazon S3 URI and check bucket permissions, make sure you're in the correct region
+ **Resource limits**: Account limits exceeded for endpoints or instances
  + Solution: Request a service quota increase through Service Quotas or AWS Support

**Note**  
If you need to delete a failed endpoint and start over:  

```
sagemaker.delete_endpoint(EndpointName=ENDPOINT_NAME)
```

## Step 5: Invoke the endpoint
<a name="nova-sagemaker-inference-step5"></a>

Once your endpoint is InService, you can send inference requests to generate predictions from your Amazon Nova model. SageMaker supports synchronous endpoints (real-time with streaming/non-streaming modes) and asynchronous endpoints (Amazon S3-based for batch processing).

**Set up the runtime client**

Create a SageMaker Runtime client with appropriate timeout settings:

```
import json
import boto3
import botocore
from botocore.exceptions import ClientError

# Configure client with appropriate timeouts
config = botocore.config.Config(
    read_timeout=120,      # Maximum time to wait for response
    connect_timeout=10,    # Maximum time to establish connection
    retries={'max_attempts': 3}  # Number of retry attempts
)

# Create SageMaker Runtime client
runtime_client = boto3.client('sagemaker-runtime', config=config, region_name=REGION)
```

**Create a universal inference function**

The following function handles both streaming and non-streaming requests. It uses the `INFERENCE_COMPONENT_NAME` variable defined in Step 4. If you deployed using inference components (Option A), this was set to `MODEL_NAME + "-IC"`. If you deployed using single model endpoints (Option B), this was not defined, so set it to `None` before running this step:

```
# Only needed if you followed Option B (single model endpoints) in Step 4:
# INFERENCE_COMPONENT_NAME = None

def invoke_nova_endpoint(request_body):
    """
    Invoke Nova endpoint with automatic streaming detection.
    Supports both inference component and single model endpoint deployments.
    
    Args:
        request_body (dict): Request payload containing prompt and parameters
    
    Returns:
        dict: Response from the model (for non-streaming requests)
        None: For streaming requests (prints output directly)
    """
    body = json.dumps(request_body)
    is_streaming = request_body.get("stream", False)
    
    # Build invoke parameters
    invoke_params = {
        'EndpointName': ENDPOINT_NAME,
        'ContentType': 'application/json',
        'Body': body
    }
    
    # Add InferenceComponentName if using inference components
    if INFERENCE_COMPONENT_NAME:
        invoke_params['InferenceComponentName'] = INFERENCE_COMPONENT_NAME
    
    try:
        print(f"Invoking endpoint ({'streaming' if is_streaming else 'non-streaming'})...")
        
        if is_streaming:
            response = runtime_client.invoke_endpoint_with_response_stream(**invoke_params)
            
            event_stream = response['Body']
            for event in event_stream:
                if 'PayloadPart' in event:
                    chunk = event['PayloadPart']
                    if 'Bytes' in chunk:
                        data = chunk['Bytes'].decode()
                        print("Chunk:", data)
        else:
            # Non-streaming inference
            invoke_params['Accept'] = 'application/json'
            response = runtime_client.invoke_endpoint(**invoke_params)
            
            response_body = response['Body'].read().decode('utf-8')
            result = json.loads(response_body)
            print("✅ Response received successfully")
            return result
    
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        print(f"❌ AWS Error: {error_code} - {error_message}")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
```

**Example 1: Non-streaming chat completion**

Use the chat format for conversational interactions:

```
# Non-streaming chat request
chat_request = {
    "messages": [
        {"role": "user", "content": "Hello! How are you?"}
    ],
    "max_tokens": 100,
    "max_completion_tokens": 100,  # Alternative to max_tokens
    "stream": False,
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "logprobs": True,
    "top_logprobs": 3,
    "reasoning_effort": "low",  # Options: "low", "high"
    "allowed_token_ids": None,  # List of allowed token IDs
    "truncate_prompt_tokens": None,  # Truncate prompt to this many tokens
    "stream_options": None
}

response = invoke_nova_endpoint(chat_request)
```

**Sample response:**

```
{
    "id": "chatcmpl-123456",
    "object": "chat.completion",
    "created": 1234567890,
    "model": "default",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Hello! I'm doing well, thank you for asking. I'm here and ready to help you with any questions or tasks you might have. How can I assist you today?"
            },
            "logprobs": {
                "content": [
                    {
                        "token": "Hello",
                        "logprob": -0.123,
                        "top_logprobs": [
                            {"token": "Hello", "logprob": -0.123},
                            {"token": "Hi", "logprob": -2.456},
                            {"token": "Hey", "logprob": -3.789}
                        ]
                    }
                    # Additional tokens...
                ]
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 12,
        "completion_tokens": 28,
        "total_tokens": 40
    }
}
```

**Example 2: Simple text completion**

Use the completion format for simple text generation:

```
# Simple completion request
completion_request = {
    "prompt": "The capital of France is",
    "max_tokens": 50,
    "stream": False,
    "temperature": 0.0,
    "top_p": 1.0,
    "top_k": -1,  # -1 means no limit
    "logprobs": 3,  # Number of log probabilities to return
    "allowed_token_ids": None,  # List of allowed token IDs
    "truncate_prompt_tokens": None,  # Truncate prompt to this many tokens
    "stream_options": None
}

response = invoke_nova_endpoint(completion_request)
```

**Sample response:**

```
{
    "id": "cmpl-789012",
    "object": "text_completion",
    "created": 1234567890,
    "model": "default",
    "choices": [
        {
            "text": " Paris.",
            "index": 0,
            "logprobs": {
                "tokens": [" Paris", "."],
                "token_logprobs": [-0.001, -0.002],
                "top_logprobs": [
                    {" Paris": -0.001, " London": -5.234, " Rome": -6.789},
                    {".": -0.002, ",": -4.567, "!": -7.890}
                ]
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 6,
        "completion_tokens": 2,
        "total_tokens": 8
    }
}
```

**Example 3: Streaming chat completion**

```
# Streaming chat request
streaming_request = {
    "messages": [
        {"role": "user", "content": "Tell me a short story about a robot"}
    ],
    "max_tokens": 200,
    "stream": True,
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "logprobs": True,
    "top_logprobs": 2,
    "reasoning_effort": "high",  # For more detailed reasoning
    "stream_options": {"include_usage": True}
}

invoke_nova_endpoint(streaming_request)
```

**Sample streaming output:**

```
Chunk: data: {"id":"chatcmpl-029ca032-fa01-4868-80b7-c4cb1af90fb9","object":"chat.completion.chunk","created":1772060532,"model":"default","choices":[{"index":0,"delta":{"role":"assistant","content":"","reasoning_content":null},"logprobs":null,"finish_reason":null}],"prompt_token_ids":null}
Chunk: data: {"id":"chatcmpl-029ca032-fa01-4868-80b7-c4cb1af90fb9","object":"chat.completion.chunk","created":1772060532,"model":"default","choices":[{"index":0,"delta":{"content":" Once","reasoning_content":null},"logprobs":{"content":[{"token":"\u2581Once","logprob":-0.6078429222106934,"bytes":[226,150,129,79,110,99,101],"top_logprobs":[{"token":"\u2581Once","logprob":-0.6078429222106934,"bytes":[226,150,129,79,110,99,101]},{"token":"\u2581In","logprob":-0.7864127159118652,"bytes":[226,150,129,73,110]}]}]},"finish_reason":null,"token_ids":null}]}
Chunk: data: {"id":"chatcmpl-029ca032-fa01-4868-80b7-c4cb1af90fb9","object":"chat.completion.chunk","created":1772060532,"model":"default","choices":[{"index":0,"delta":{"content":" upon","reasoning_content":null},"logprobs":{"content":[{"token":"\u2581upon","logprob":-0.0012345,"bytes":[226,150,129,117,112,111,110],"top_logprobs":[{"token":"\u2581upon","logprob":-0.0012345,"bytes":[226,150,129,117,112,111,110]},{"token":"\u2581a","logprob":-6.789,"bytes":[226,150,129,97]}]}]},"finish_reason":null,"token_ids":null}]}
Chunk: data: {"id":"chatcmpl-029ca032-fa01-4868-80b7-c4cb1af90fb9","object":"chat.completion.chunk","created":1772060532,"model":"default","choices":[{"index":0,"delta":{"content":" a","reasoning_content":null},"logprobs":{"content":[{"token":"\u2581a","logprob":-0.0001234,"bytes":[226,150,129,97],"top_logprobs":[{"token":"\u2581a","logprob":-0.0001234,"bytes":[226,150,129,97]},{"token":"\u2581time","logprob":-9.123,"bytes":[226,150,129,116,105,109,101]}]}]},"finish_reason":null,"token_ids":null}]}
Chunk: data: {"id":"chatcmpl-029ca032-fa01-4868-80b7-c4cb1af90fb9","object":"chat.completion.chunk","created":1772060532,"model":"default","choices":[{"index":0,"delta":{"content":" time","reasoning_content":null},"logprobs":{"content":[{"token":"\u2581time","logprob":-0.0023456,"bytes":[226,150,129,116,105,109,101],"top_logprobs":[{"token":"\u2581time","logprob":-0.0023456,"bytes":[226,150,129,116,105,109,101]},{"token":",","logprob":-6.012,"bytes":[44]}]}]},"finish_reason":null,"token_ids":null}]}

# Additional chunks...

Chunk: data: {"id":"chatcmpl-029ca032-fa01-4868-80b7-c4cb1af90fb9","object":"chat.completion.chunk","created":1772060532,"model":"default","choices":[{"index":0,"delta":{},"logprobs":null,"finish_reason":"stop"}],"usage":{"prompt_tokens":15,"completion_tokens":87,"total_tokens":102}}
Chunk: data: [DONE]
```

**Example 4: Multimodal chat completion**

Use multimodal format for image and text inputs:

```
# Multimodal chat request (if supported by your model)
multimodal_request = {
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}
            ]
        }
    ],
    "max_tokens": 150,
    "temperature": 0.3,
    "top_p": 0.8,
    "stream": False
}

response = invoke_nova_endpoint(multimodal_request)
```

**Sample response:**

```
{
    "id": "chatcmpl-345678",
    "object": "chat.completion",
    "created": 1234567890,
    "model": "default",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "The image shows..."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 1250,
        "completion_tokens": 45,
        "total_tokens": 1295
    }
}
```

## Step 6: Clean up resources (Optional)
<a name="nova-sagemaker-inference-step6"></a>

To avoid incurring unnecessary charges, delete the AWS resources you created during this tutorial. SageMaker endpoints incur charges while they're running, even if you're not actively making inference requests.

**Important**  
Deleting resources is permanent and cannot be undone. Ensure you no longer need these resources before proceeding.

**Initialize the cleanup client**

```
import boto3
import time

# Initialize SageMaker client
sagemaker = boto3.client('sagemaker', region_name=REGION)
```

**Delete inference component (if using Option A)**

If you deployed using inference components, delete the inference component first before deleting the endpoint:

```
# Delete inference component (Option A only)
try:
    print("Deleting inference component...")
    sagemaker.delete_inference_component(InferenceComponentName=INFERENCE_COMPONENT_NAME)
    print(f"✅ Inference component '{INFERENCE_COMPONENT_NAME}' deletion initiated")
except Exception as e:
    print(f"❌ Error deleting inference component: {e}")

# Wait for inference component to be deleted before proceeding
print("Waiting for inference component deletion...")
while True:
    try:
        sagemaker.describe_inference_component(InferenceComponentName=INFERENCE_COMPONENT_NAME)
        time.sleep(10)
    except sagemaker.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ValidationException':
            print("✅ Inference component successfully deleted")
            break
        else:
            print(f"Error: {e}")
            break
```

**Delete the endpoint**

```
try:
    print("Deleting endpoint...")
    sagemaker.delete_endpoint(EndpointName=ENDPOINT_NAME)
    print(f"✅ Endpoint '{ENDPOINT_NAME}' deletion initiated")
    print("Charges will stop once deletion completes (typically 2-5 minutes)")
except Exception as e:
    print(f"❌ Error deleting endpoint: {e}")
```

**Note**  
The endpoint deletion is asynchronous. You can monitor the deletion status:  

```
import time

print("Monitoring endpoint deletion...")
while True:
    try:
        response = sagemaker.describe_endpoint(EndpointName=ENDPOINT_NAME)
        status = response['EndpointStatus']
        print(f"Status: {status}")
        time.sleep(10)
    except sagemaker.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ValidationException':
            print("✅ Endpoint successfully deleted")
            break
        else:
            print(f"Error: {e}")
            break
```

**Delete the endpoint configuration**

After the endpoint is deleted, remove the endpoint configuration:

```
try:
    print("Deleting endpoint configuration...")
    sagemaker.delete_endpoint_config(EndpointConfigName=ENDPOINT_CONFIG_NAME)
    print(f"✅ Endpoint configuration '{ENDPOINT_CONFIG_NAME}' deleted")
except Exception as e:
    print(f"❌ Error deleting endpoint configuration: {e}")
```

**Delete the model (Option B only)**

If you used single model endpoints, remove the SageMaker model object:

```
try:
    print("Deleting model...")
    sagemaker.delete_model(ModelName=MODEL_NAME)
    print(f"✅ Model '{MODEL_NAME}' deleted")
except Exception as e:
    print(f"❌ Error deleting model: {e}")
```