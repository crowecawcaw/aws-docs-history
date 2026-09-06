

# Evaluate with Inspect AI SDK
<a name="nova-eval-on-sagemaker-inference"></a>

This guide explains how to evaluate your customized Amazon Nova models deployed on SageMaker inference endpoints using [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai), an open-source evaluation framework.

**Note**  
For hands-on walkthroughs, see the [SageMaker Inspect AI sample notebooks](https://github.com/aws-samples/amazon-nova-samples/tree/main/customization/sagemaker-inspect-ai).

## Overview
<a name="nova-eval-sagemaker-overview"></a>

You can evaluate your customized Amazon Nova models deployed on SageMaker endpoints using standardized benchmarks from the AI research community. This approach enables you to:
+ Evaluate customized Amazon Nova models (fine-tuned, distilled, or otherwise adapted) at scale
+ Run evaluations with parallel inference across multiple endpoint instances
+ Compare model performance using benchmarks like MMLU, TruthfulQA, and HumanEval
+ Integrate with your existing SageMaker infrastructure

## Supported models
<a name="nova-eval-sagemaker-supported-models"></a>

The SageMaker inference provider works with:
+ Amazon Nova models (Nova Micro, Nova Lite, Nova Lite 2)
+ Models deployed via vLLM or OpenAI-compatible inference servers
+ Any endpoint that supports the OpenAI Chat Completions API format

## Prerequisites
<a name="nova-eval-sagemaker-prerequisites"></a>

Before you begin, ensure you have:
+ An AWS account with permissions to create and invoke SageMaker endpoints
+ AWS credentials configured via AWS CLI, environment variables, or IAM role
+ Python 3.9 or higher

**Required IAM permissions**

Your IAM user or role needs the following permissions:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sagemaker:InvokeEndpoint",
        "sagemaker:DescribeEndpoint"
      ],
      "Resource": "arn:aws:sagemaker:*:*:endpoint/*"
    }
  ]
}
```

## Step 1: Deploy a SageMaker endpoint
<a name="nova-eval-sagemaker-step1"></a>

Before running evaluations, you need a SageMaker inference endpoint running your model.

For instructions on creating a SageMaker inference endpoint with Amazon Nova models, see [Getting Started](nova-sagemaker-inference-getting-started.md).

Once your endpoint is in `InService` status, note the endpoint name for use in the evaluation commands.

## Step 2: Install evaluation dependencies
<a name="nova-eval-sagemaker-step2"></a>

Create a Python virtual environment and install the required packages.

```
# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install uv for faster package installation
pip install uv

# Install Inspect AI and evaluation benchmarks
uv pip install inspect-ai inspect-evals

# Install AWS dependencies
uv pip install aioboto3 boto3 botocore openai
```

## Step 3: Configure AWS credentials
<a name="nova-eval-sagemaker-step3"></a>

Choose one of the following authentication methods:

**Option 1: AWS CLI (Recommended)**

```
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, and default region when prompted.

**Option 2: Environment variables**

```
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-west-2
```

**Option 3: IAM role**

If running on Amazon EC2 or SageMaker notebooks, the instance's IAM role is used automatically.

**Verify credentials**

```
import boto3

sts = boto3.client('sts')
identity = sts.get_caller_identity()
print(f"Account: {identity['Account']}")
print(f"User/Role: {identity['Arn']}")
```

## Step 4: Download evaluation benchmarks
<a name="nova-eval-sagemaker-step4"></a>

Clone the Inspect Evals repository to access standard benchmarks:

```
git clone https://github.com/UKGovernmentBEIS/inspect_evals.git
```

This repository includes benchmarks such as:
+ MMLU and MMLU-Pro (knowledge and reasoning)
+ TruthfulQA (truthfulness)
+ HumanEval (code generation)
+ GSM8K (mathematical reasoning)

## Step 5: Run evaluations
<a name="nova-eval-sagemaker-step5"></a>

Run an evaluation using your SageMaker endpoint:

```
cd inspect_evals/src/inspect_evals/

inspect eval mmlu_pro/mmlu_pro.py \
  --model sagemaker/my-nova-endpoint \
  -M region_name=us-west-2 \
  --max-connections 256 \
  --max-retries 100 \
  --display plain
```

**Key parameters**


| Parameter | Default | Description | 
| --- | --- | --- | 
| --max-connections | 10 | Number of parallel requests to the endpoint. Scale with instance count (e.g., 10 instances × 25 = 250). | 
| --max-retries | 3 | Retry attempts for failed requests. Use 50-100 for large evaluations. | 
| -M region\_name | us-east-1 | AWS region where your endpoint is deployed. | 
| -M read\_timeout | 600 | Request timeout in seconds. | 
| -M connect\_timeout | 60 | Connection timeout in seconds. | 

**Tuning recommendations**

For a multi-instance endpoint:

```
# 10-instance endpoint example
--max-connections 250   # ~25 connections per instance
--max-retries 100       # Handle transient errors
```

Setting `--max-connections` too high may overwhelm the endpoint and cause throttling. Setting it too low underutilizes capacity.

## Step 6: View results
<a name="nova-eval-sagemaker-step6"></a>

Launch the Inspect AI viewer to analyze evaluation results:

```
inspect view
```

The viewer displays:
+ Overall scores and metrics
+ Per-sample results with model responses
+ Error analysis and failure patterns

## Managing endpoints
<a name="nova-eval-sagemaker-managing-endpoints"></a>

**Update an endpoint**

To update an existing endpoint with a new model or configuration:

```
import boto3

sagemaker = boto3.client('sagemaker', region_name=REGION)

# Create new model and endpoint configuration
# Then update the endpoint
sagemaker.update_endpoint(
    EndpointName=EXISTING_ENDPOINT_NAME,
    EndpointConfigName=NEW_ENDPOINT_CONFIG_NAME
)
```

**Delete an endpoint**

```
sagemaker.delete_endpoint(EndpointName=ENDPOINT_NAME)
```

## Onboarding custom benchmarks
<a name="nova-eval-sagemaker-custom-benchmarks"></a>

You can add new benchmarks to Inspect AI using the following workflow:

1. Study the benchmark's dataset format and evaluation metrics

1. Review similar implementations in `inspect_evals/`

1. Create a task file that converts dataset records to Inspect AI samples

1. Implement appropriate solvers and scorers

1. Validate with a small test run

Example task structure:

```
from inspect_ai import Task, task
from inspect_ai.dataset import hf_dataset
from inspect_ai.scorer import choice
from inspect_ai.solver import multiple_choice

@task
def my_benchmark():
    return Task(
        dataset=hf_dataset("dataset_name", split="test"),
        solver=multiple_choice(),
        scorer=choice()
    )
```

## Troubleshooting
<a name="nova-eval-sagemaker-troubleshooting"></a>

**Common issues**

**Endpoint throttling or timeouts**
+ Reduce `--max-connections`
+ Increase `--max-retries`
+ Check endpoint CloudWatch metrics for capacity issues

**Authentication errors**
+ Verify AWS credentials are configured correctly
+ Check IAM permissions include `sagemaker:InvokeEndpoint`

**Model errors**
+ Verify the endpoint is in `InService` status
+ Check that the model supports the OpenAI Chat Completions API format

## Related resources
<a name="nova-eval-sagemaker-related-resources"></a>
+ [Inspect AI Documentation](https://inspect.ai-safety-institute.org.uk/)
+ [Inspect Evals Repository](https://github.com/UKGovernmentBEIS/inspect_evals)
+ [SageMaker Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
+ [Deploy Models for Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
+ [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)