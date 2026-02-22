# Getting Started

This guide shows you how to deploy customized Amazon Nova models on SageMaker real-time endpoints, configure inference parameters, and invoke your models for testing.

## Prerequisites

The following are prerequisites to deploy Amazon Nova models on SageMaker inference:

- Create an AWS account - If you don't have one already, see [Creating an AWS account](../../../sagemaker/latest/dg/gs-set-up.md#sign-up-for-aws "../../../sagemaker/latest/dg/gs-set-up.md#sign-up-for-aws").
- Required IAM permissions - Ensure your IAM user or role has the following managed policies attached:
  - `AmazonSageMakerFullAccess`
  - `AmazonS3FullAccess`

- Required SDKs/CLI versions - The following SDK versions have been tested and validated with Amazon Nova models on SageMaker inference:
  - SageMaker Python SDK v3.0.0+ (`sagemaker>=3.0.0`) for resource-based API approach
  - Boto3 version 1.35.0+ (`boto3>=1.35.0`) for direct API calls. The examples in this guide use this approach.

## Step 1: Configure AWS credentials

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

###### Note

For more information about AWS credentials, see [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md").

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

A SageMaker execution role is an IAM role that grants SageMaker permissions to access AWS resources on your behalf, such as Amazon S3 buckets for model artifacts and CloudWatch for logging.

**Creating the execution role**

###### Note

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

###### Important

The execution role must have trust relationship with `sagemaker.amazonaws.com` and permissions to access Amazon S3 and SageMaker resources.

For more information about SageMaker execution roles, see [SageMaker Roles](../../../sagemaker/latest/dg/sagemaker-roles.md "../../../sagemaker/latest/dg/sagemaker-roles.md").

## Step 3: Configure model parameters

Configure the deployment parameters for your Amazon Nova model. These settings control model behavior, resource allocation, and inference characteristics.

**Required parameters**

- `IMAGE`: The Docker container image URI for Amazon Nova inference container. This will be provided by AWS.
- `CONTEXT_LENGTH`: Model context length.
- `MAX_CONCURRENCY`: Maximum number of sequences per iteration; sets the limit on how many individual user requests (prompts) can be processed concurrently within a single batch on the GPU. Range: integer greater than 0.

**Optional generation parameters**

- `DEFAULT_TEMPERATURE`: Controls randomness in generation. Range: 0.0 to 2.0 (0.0 = deterministic, higher = more random).
- `DEFAULT_TOP_P`: Nucleus sampling threshold for token selection. Range: 1e-10 to 1.0.
- `DEFAULT_TOP_K`: Limits token selection to top K most likely tokens. Range: integer -1 or greater (-1 = no limit).
- `DEFAULT_MAX_NEW_TOKENS`: Maximum number of tokens to generate in response (i.e. max output tokens). Range: integer 1 or greater.
- `DEFAULT_LOGPROBS`: Number of log probabilities to return per token. Range: integer 1 to 20.

**Configure your deployment**

```
# AWS Configuration
REGION = "us-east-1"  # Must match region from Step 1

# ECR Account mapping by region
ECR_ACCOUNT_MAP = {
    "us-east-1": "708977205387",
    "us-west-2": "176779409107"
}

# Container Image - Replace with the image URI provided by your AWS contact
# Two image tags are available (both point to the same image):
IMAGE_LATEST = f"{ECR_ACCOUNT_MAP[REGION]}.dkr.ecr.{REGION}.amazonaws.com/nova-inference-repo:SM-Inference-latest"
IMAGE_VERSIONED = f"{ECR_ACCOUNT_MAP[REGION]}.dkr.ecr.{REGION}.amazonaws.com/nova-inference-repo:v1.0.0"

# Use the versioned tag for production deployments (recommended)
IMAGE = IMAGE_VERSIONED
print(f"IMAGE = {IMAGE}")
print(f"Available tags:")
print(f"  Latest: {IMAGE_LATEST}")
print(f"  Versioned: {IMAGE_VERSIONED}")

# Model Parameters
CONTEXT_LENGTH = "16000"       # Maximum total context length
MAX_CONCURRENCY = "2"          # Maximum concurrent sequences

# Optional: Default generation parameters (uncomment to use)
DEFAULT_TEMPERATURE = "0.0"   # Deterministic output
DEFAULT_TOP_P = "1.0"         # Consider all tokens
# DEFAULT_TOP_K = "50"        # Uncomment to limit to top 50 tokens
# DEFAULT_MAX_NEW_TOKENS = "2048"  # Uncomment to set max output tokens
# DEFAULT_LOGPROBS = "1"      # Uncomment to enable log probabilities

# Build environment variables for the container
environment = {
    'CONTEXT_LENGTH': CONTEXT_LENGTH,
    'MAX_CONCURRENCY': MAX_CONCURRENCY,
}

# Add optional parameters if defined
if 'DEFAULT_TEMPERATURE' in globals():
    environment['DEFAULT_TEMPERATURE'] = DEFAULT_TEMPERATURE
if 'DEFAULT_TOP_P' in globals():
    environment['DEFAULT_TOP_P'] = DEFAULT_TOP_P
if 'DEFAULT_TOP_K' in globals():
    environment['DEFAULT_TOP_K'] = DEFAULT_TOP_K
if 'DEFAULT_MAX_NEW_TOKENS' in globals():
    environment['DEFAULT_MAX_NEW_TOKENS'] = DEFAULT_MAX_NEW_TOKENS
if 'DEFAULT_LOGPROBS' in globals():
    environment['DEFAULT_LOGPROBS'] = DEFAULT_LOGPROBS

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

- Model Name: `{JOB_NAME}-{model}-{instance-type}`
- Endpoint Config: `{MODEL_NAME}-Config`
- Endpoint Name: `{MODEL_NAME}-Endpoint`

## Step 4: Create SageMaker model and endpoint configuration

In this step, you'll create two essential resources: a SageMaker model object that references your Amazon Nova model artifacts, and an endpoint configuration that defines how the model will be deployed.

**SageMaker Model**: A model object that packages the inference container image, model artifacts location, and environment configuration. This is a reusable resource that can be deployed to multiple endpoints.

**Endpoint Configuration**: Defines the infrastructure settings for deployment, including instance type, instance count, and model variants. This allows you to manage deployment settings separately from the model itself.

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

- `ModelName`: Unique identifier for your model
- `Image`: Docker container image URI for Amazon Nova inference
- `ModelDataSource`: Amazon S3 location of your model artifacts
- `Environment`: Environment variables configured in Step 3
- `ExecutionRoleArn`: IAM role from Step 2
- `EnableNetworkIsolation`: Set to True for enhanced security (prevents container from making outbound network calls)

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

- `VariantName`: Identifier for this model variant (use 'primary' for single-model deployments)
- `ModelName`: References the model created above
- `InitialInstanceCount`: Number of instances to deploy (start with 1, scale later if needed)
- `InstanceType`: ML instance type selected in Step 3

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

## Step 5: Deploy the endpoint

The next step is to deploy your Amazon Nova model by creating a SageMaker real-time endpoint. This endpoint will host your model and provide a secure HTTPS endpoint for making inference requests.

Endpoint creation typically takes 15-30 minutes as AWS provisions the infrastructure, downloads your model artifacts, and initializes the inference container.

**Create the endpoint**

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

**Verify endpoint is ready**

Once the endpoint is InService, you can verify its configuration:

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

- **Insufficient capacity**: The requested instance type is not available in your region
  - Solution: Try a different instance type or request a quota increase

- **IAM permissions**: The execution role lacks necessary permissions
  - Solution: Verify the role has access to Amazon S3 model artifacts and necessary SageMaker permissions

- **Model artifacts not found**: The Amazon S3 URI is incorrect or inaccessible
  - Solution: Verify the Amazon S3 URI and check bucket permissions, make sure you're in the correct region

- **Resource limits**: Account limits exceeded for endpoints or instances
  - Solution: Request a service quota increase through Service Quotas or AWS Support

###### Note

If you need to delete a failed endpoint and start over:

```
sagemaker.delete_endpoint(EndpointName=ENDPOINT_NAME)
```

## Step 6: Invoke the endpoint

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

The following function handles both streaming and non-streaming requests:

```
def invoke_nova_endpoint(request_body):
    """
    Invoke Nova endpoint with automatic streaming detection.

    Args:
        request_body (dict): Request payload containing prompt and parameters

    Returns:
        dict: Response from the model (for non-streaming requests)
        None: For streaming requests (prints output directly)
    """
    body = json.dumps(request_body)
    is_streaming = request_body.get("stream", False)

    try:
        print(f"Invoking endpoint ({'streaming' if is_streaming else 'non-streaming'})...")

        if is_streaming:
            response = runtime_client.invoke_endpoint_with_response_stream(
                EndpointName=ENDPOINT_NAME,
                ContentType='application/json',
                Body=body
            )

            event_stream = response['Body']
            for event in event_stream:
                if 'PayloadPart' in event:
                    chunk = event['PayloadPart']
                    if 'Bytes' in chunk:
                        data = chunk['Bytes'].decode()
                        print("Chunk:", data)
        else:
            # Non-streaming inference
            response = runtime_client.invoke_endpoint(
                EndpointName=ENDPOINT_NAME,
                ContentType='application/json',
                Accept='application/json',
                Body=body
            )

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

## Step 7: Clean up resources (Optional)

To avoid incurring unnecessary charges, delete the AWS resources you created during this tutorial. SageMaker endpoints incur charges while they're running, even if you're not actively making inference requests.

###### Important

Deleting resources is permanent and cannot be undone. Ensure you no longer need these resources before proceeding.

**Delete the endpoint**

```
import boto3

# Initialize SageMaker client
sagemaker = boto3.client('sagemaker', region_name=REGION)

try:
    print("Deleting endpoint...")
    sagemaker.delete_endpoint(EndpointName=ENDPOINT_NAME)
    print(f"✅ Endpoint '{ENDPOINT_NAME}' deletion initiated")
    print("Charges will stop once deletion completes (typically 2-5 minutes)")
except Exception as e:
    print(f"❌ Error deleting endpoint: {e}")
```

###### Note

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

**Delete the model**

Remove the SageMaker model object:

```
try:
    print("Deleting model...")
    sagemaker.delete_model(ModelName=MODEL_NAME)
    print(f"✅ Model '{MODEL_NAME}' deleted")
except Exception as e:
    print(f"❌ Error deleting model: {e}")
```
