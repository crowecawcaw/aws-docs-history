

# Evaluate with Inspect AI Container
<a name="nova-eval-inspect-ai-container"></a>

The SageMaker Inspect AI container runs LLM model evaluations on SageMaker Training Jobs. The container uses [Inspect AI](https://inspect.ai-safety-institute.org.uk/) to provide a standardized evaluation process for models deployed to SageMaker inference endpoints or Amazon Bedrock — including Amazon Nova 1.0 (Micro, Lite, Pro) and 2.0 (Lite 2) models.

Previous [evaluation approaches](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-evaluation.html) (based on [lighteval](https://github.com/huggingface/lighteval)) tightly coupled offline inference and evaluation logic, which limited flexibility in how models could be served and tested. The Inspect AI container decouples evaluation logic from inference entirely.

## Overview
<a name="nova-eval-container-overview"></a>

Key benefits include:
+ **Bring your own benchmarks** — write evaluation tasks in the Inspect AI format, then plug in domain-specific evaluation tasks without depending on a centralized team to onboard them.
+ **Evaluate with different inference options** — works with SageMaker Inference (existing endpoint or create on-the-fly), Amazon Bedrock, and more inference backends incoming.
+ **Iterate faster** — go from benchmark development to production evaluation without infrastructure changes. New benchmark onboarding that previously took days happens in minutes.
+ **Run at scale** — chain multiple benchmarks in one job, mix standard benchmarks from the inspect-evals library with your own custom tasks in the same job.
+ **One entry point for all training techniques** — whether your model was fine-tuned with SFT (SMTJ, SMHP), CPT (SMHP), or RFT (SMTJ, SMHP), the container evaluates it through the same interface. Evaluating mid-training checkpoints saved at specific steps is also supported (for example, step 500, step 1000) by pointing `model_s3_uri` at the checkpoint path.

### How it works
<a name="nova-eval-container-how-it-works"></a>

You provide two inputs to the container:

1. A YAML configuration file (recipe) that defines the inference provider, benchmarks, and evaluation parameters

1. Benchmark files (Python scripts with the `@task` decorator) uploaded to Amazon S3

The container handles endpoint management, evaluation execution, and result collection. When the training job completes, results are written to your specified S3 output location.

## Container image
<a name="nova-eval-container-images"></a>

The following table lists the Inspect AI container image URIs by AWS Region.


| Region | Container image URI | 
| --- | --- | 
| us-east-1 | 763104351884.dkr.ecr.us-east-1.amazonaws.com/sagemaker-inspect-ai:latest | 
| us-west-2 | 763104351884.dkr.ecr.us-west-2.amazonaws.com/sagemaker-inspect-ai:latest | 
| eu-west-2 | 763104351884.dkr.ecr.eu-west-2.amazonaws.com/sagemaker-inspect-ai:latest | 

## Prerequisites
<a name="nova-eval-container-prerequisites"></a>

Before you begin, ensure you have the following resources and access.


| Requirement | Description | 
| --- | --- | 
| AWS account with SageMaker access | An active AWS account with permissions to create SageMaker Training Jobs | 
| S3 bucket | A bucket to store your evaluation recipes, benchmark files, and output results | 
| IAM execution role | A role that SageMaker can assume to access your resources | 
| SageMaker inference endpoint or Amazon Bedrock access | A deployed model endpoint or Amazon Bedrock model access for the model you want to evaluate | 
| AWS CLI or SageMaker Python SDK | Tools to submit training jobs and manage resources | 
| Capacity reservation (large models) | For models that require accelerated instances (such as p5 for Nova Lite 2), contact AWS Support to reserve capacity for SageMaker Inference or Amazon Bedrock | 

## Step 1: Set up IAM permissions
<a name="nova-eval-container-step1"></a>

The SageMaker Training Job runs under an execution role that you provide. This role needs permissions to read benchmarks from S3, write results, invoke the inference endpoint, and write CloudWatch logs.

**1.1 Create the trust policy**

Save the following as `trust_policy.json`:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**1.2 Create the role**

```
aws iam create-role \
  --role-name InspectLensEvalRole \
  --assume-role-policy-document file://trust_policy.json
```

**1.3 Attach the permissions policy**

Save the following as `eval_policy.json`, replacing all placeholder values (`REGION`, `ACCOUNT_ID`, bucket names) with your values:

**Scope down to resources in use**  
Scope down each resource ARN to only the resources you need. The policy below provides a starting template — restrict bucket names, endpoint ARNs, and other resources to match your environment.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "S3ReadBenchmarkData",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::YOUR_BENCHMARK_BUCKET",
        "arn:aws:s3:::YOUR_BENCHMARK_BUCKET/*"
      ]
    },
    {
      "Sid": "S3WriteResults",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::YOUR_RESULTS_BUCKET",
        "arn:aws:s3:::YOUR_RESULTS_BUCKET/*"
      ]
    },
    {
      "Sid": "SageMakerInvokeExistingEndpoint",
      "Effect": "Allow",
      "Action": [
        "sagemaker:InvokeEndpoint",
        "sagemaker:InvokeEndpointWithResponseStream",
        "sagemaker:DescribeEndpoint"
      ],
      "Resource": "arn:aws:sagemaker:REGION:ACCOUNT_ID:endpoint/*"
    },
    {
      "Sid": "BedrockInference",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:REGION::foundation-model/*",
        "arn:aws:bedrock:REGION:ACCOUNT_ID:inference-profile/*",
        "arn:aws:bedrock:REGION:ACCOUNT_ID:provisioned-model/*",
        "arn:aws:bedrock:REGION:ACCOUNT_ID:custom-model/*",
        "arn:aws:bedrock:REGION:ACCOUNT_ID:imported-model/*",
        "arn:aws:bedrock:REGION:ACCOUNT_ID:custom-model-deployment/*"
      ]
    },
    {
      "Sid": "BedrockCustomModelAccess",
      "Effect": "Allow",
      "Action": [
        "bedrock:GetCustomModel",
        "bedrock:GetImportedModel",
        "bedrock:GetProvisionedModelThroughput",
        "bedrock:GetCustomModelDeployment",
        "bedrock:GetInferenceProfile"
      ],
      "Resource": [
        "arn:aws:bedrock:REGION:ACCOUNT_ID:custom-model/*",
        "arn:aws:bedrock:REGION:ACCOUNT_ID:imported-model/*",
        "arn:aws:bedrock:REGION:ACCOUNT_ID:provisioned-model/*",
        "arn:aws:bedrock:REGION:ACCOUNT_ID:custom-model-deployment/*",
        "arn:aws:bedrock:REGION:ACCOUNT_ID:inference-profile/*"
      ]
    },
    {
      "Sid": "SageMakerCreateEndpointLifecycle",
      "Effect": "Allow",
      "Action": [
        "sagemaker:CreateModel",
        "sagemaker:DescribeModel",
        "sagemaker:DeleteModel",
        "sagemaker:CreateEndpointConfig",
        "sagemaker:DescribeEndpointConfig",
        "sagemaker:DeleteEndpointConfig",
        "sagemaker:CreateEndpoint",
        "sagemaker:DescribeEndpoint",
        "sagemaker:DeleteEndpoint",
        "sagemaker:InvokeEndpoint",
        "sagemaker:InvokeEndpointWithResponseStream"
      ],
      "Resource": [
        "arn:aws:sagemaker:REGION:ACCOUNT_ID:model/*",
        "arn:aws:sagemaker:REGION:ACCOUNT_ID:endpoint/*",
        "arn:aws:sagemaker:REGION:ACCOUNT_ID:endpoint-config/*"
      ]
    },
    {
      "Sid": "ECRAuth",
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    },
    {
      "Sid": "PassRoleToSageMaker",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::ACCOUNT_ID:role/InspectLensEvalRole",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "sagemaker.amazonaws.com"
        }
      }
    },
    {
      "Sid": "VPCNetworkingForEndpoint",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:CreateNetworkInterfacePermission",
        "ec2:DeleteNetworkInterface",
        "ec2:DeleteNetworkInterfacePermission",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeVpcs",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CloudWatchLogs",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams"
      ],
      "Resource": [
        "arn:aws:logs:REGION:ACCOUNT_ID:log-group:/aws/sagemaker/TrainingJobs:*",
        "arn:aws:logs:REGION:ACCOUNT_ID:log-group:/aws/sagemaker/Endpoints/*"
      ]
    },
    {
      "Sid": "MLflowTrackingServer",
      "Effect": "Allow",
      "Action": [
        "sagemaker:DescribeMlflowTrackingServer",
        "sagemaker:CreatePresignedMlflowTrackingServerUrl"
      ],
      "Resource": "arn:aws:sagemaker:REGION:ACCOUNT_ID:mlflow-tracking-server/*"
    },
    {
      "Sid": "MLflowTrackingOperations",
      "Effect": "Allow",
      "Action": [
        "sagemaker-mlflow:AccessUI",
        "sagemaker-mlflow:CreateExperiment",
        "sagemaker-mlflow:GetExperiment",
        "sagemaker-mlflow:GetExperimentByName",
        "sagemaker-mlflow:SearchExperiments",
        "sagemaker-mlflow:CreateRun",
        "sagemaker-mlflow:GetRun",
        "sagemaker-mlflow:UpdateRun",
        "sagemaker-mlflow:SearchRuns",
        "sagemaker-mlflow:LogMetric",
        "sagemaker-mlflow:LogParam",
        "sagemaker-mlflow:LogBatch",
        "sagemaker-mlflow:SetTag",
        "sagemaker-mlflow:LogArtifact",
        "sagemaker-mlflow:ListArtifacts"
      ],
      "Resource": "arn:aws:sagemaker:REGION:ACCOUNT_ID:mlflow-tracking-server/*"
    },
    {
      "Sid": "KMSForVolumeEncryption",
      "Effect": "Allow",
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:CreateGrant",
        "kms:DescribeKey"
      ],
      "Resource": "arn:aws:kms:REGION:ACCOUNT_ID:key/*"
    }
  ]
}
```

Attach the policy to the role:

```
aws iam put-role-policy \
  --role-name InspectLensEvalRole \
  --policy-name InspectLensEvalPolicy \
  --policy-document file://eval_policy.json
```

## Step 2: Write your eval recipe
<a name="nova-eval-container-step2"></a>

The eval recipe is a YAML configuration file that defines how the container runs your evaluations. The recipe specifies the inference provider, benchmarks, evaluation parameters, and output settings.

For end-to-end examples, see the following notebooks in the [Amazon Nova Samples](https://github.com/aws-samples/amazon-nova-samples) repository on GitHub:
+ [Evaluate an existing SageMaker endpoint](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_sagemaker_endpoint.ipynb)
+ [Evaluate with a managed endpoint](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_managed_endpoint.ipynb)
+ [Evaluate a Amazon Bedrock model](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_bedrock_model.ipynb)

### Option A: Evaluate an existing SageMaker endpoint
<a name="nova-eval-container-option-a"></a>

Use this option when you have a model already deployed on a SageMaker inference endpoint.

```
inference_provider:
  sagemaker_endpoint:
    endpoint_name: "my-existing-endpoint"
    region: "us-east-1"

benchmarks:
  s3_path: "s3://your-bucket/benchmarks/my_benchmarks/"
  tasks:
    - name: mmlu

eval:
  max_connections: 10
  max_retries: 100
  timeout: 600

output:
  s3_path: "s3://your-bucket/eval-results/"
```

### Option B: Create endpoint, evaluate, then clean up
<a name="nova-eval-container-option-b"></a>

Use this option to have the container deploy a Amazon Nova base or fine-tuned model, run evaluations, and tear down the endpoint automatically. This is the recommended approach for one-off evaluation runs. Retrieve the latest SageMaker inference container from the [Amazon Nova SageMaker Inference container images](https://docs.aws.amazon.com/nova/latest/userguide/nova-model-sagemaker-inference.html#nova-sagemaker-inference-container-images) documentation.

```
inference_provider:
  sagemaker_endpoint:
    endpoint_name: null                 # null = create new endpoint
    model_s3_uri: "s3://your-bucket/models/nova-micro/"
    inference_image_uri: "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-inference-repo:SM-Inference-latest"
    instance_type: "ml.p5.48xlarge"
    instance_count: 1
    execution_role_arn: "arn:aws:iam::ACCOUNT_ID:role/InspectLensEvalRole"
    region: "us-east-1"
    context_length: "16000"
    max_concurrency: "32"
    cleanup_endpoint: true              # Auto-delete after eval

benchmarks:
  s3_path: "s3://your-bucket/benchmarks/my_benchmarks/"
  tasks:
    - name: mmlu_pro
    - name: arc_c
    - name: boolq

eval:
  fail_on_error: false
  decoding:
    temperature: 0.0
    top_p: 1.0
    top_k: -1
    max_tokens: 16000
    reasoning_effort: null
  max_connections: 16
  max_retries: 100
  timeout: 600
  extra_args:
    - "-M"
    - "completion_mode=True"
    - "--logprobs"
    - "--top-logprobs"
    - "5"

output:
  s3_path: "s3://your-bucket/eval-results/"
```

**Note on `model_s3_uri`**  
**Amazon Nova GA models (base checkpoints)**: For example, `s3://escrow-nova-model-708977205387-us-east-1/nova-lite-2/prod/` — SageMaker manages access automatically, no additional S3 permissions needed.
**Customized Amazon Nova models (post-training checkpoints)**: `s3://customer-escrow-ACCOUNT_ID-SUFFIX/YOUR_RUN_NAME/outputs/checkpoints/step_N/` — this is the escrow bucket path from your training job output.

**Managed endpoint resources**  
Grant the following optional permission to your execution role so the container can tag managed inference resources with the originating training job name and ARN. Tagged resources include the endpoint, endpoint configuration, and model. This helps identify resources if cleanup is interrupted. The container only applies tags when running as a SageMaker Training Job.  

```
{
  "Sid": "SageMakerTagManagedResources",
  "Effect": "Allow",
  "Action": "sagemaker:AddTags",
  "Resource": [
    "arn:aws:sagemaker:REGION:ACCOUNT_ID:model/*",
    "arn:aws:sagemaker:REGION:ACCOUNT_ID:endpoint/*",
    "arn:aws:sagemaker:REGION:ACCOUNT_ID:endpoint-config/*"
  ]
}
```
The container applies the following tags to managed resources:  


| Tag key | Example value | 
| --- | --- | 
| sagemaker-inspect-ai:TrainingJobName | my-eval-job-20260828-145940 | 
| sagemaker-inspect-ai:TrainingJobArn | arn:aws:sagemaker:us-east-1:123456789012:training-job/my-eval-job-20260828-145940 | 
External sources can interrupt resource management during runtime. For information about handling leftover resources, see [Troubleshooting](#nova-eval-container-troubleshooting).

### Option C: Evaluate through Amazon Bedrock Runtime
<a name="nova-eval-container-option-c"></a>

Use this option to evaluate a model available through Amazon Bedrock Runtime without managing an endpoint. For more information about Amazon Bedrock endpoint options, see [Amazon Bedrock endpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html).

```
inference_provider:
  bedrock:
    model_id: amazon.nova-pro-v1:0
    region: us-east-1

benchmarks:
  - name: mmlu
    path: benchmarks/mmlu_pro.py
    limit: 100

eval:
  fail_on_error: false
  decoding:
    temperature: 0.0
    top_p: 1.0
    top_k: -1
    max_tokens: 8192
    reasoning_effort: null
  max_connections: 10
  max_retries: 50
  timeout: 600
  extra_args:
    - "--display"
    - "plain"

output:
  s3_path: s3://your-bucket/eval/output/
```

### Option D: Evaluate through Amazon Bedrock Mantle
<a name="nova-eval-container-option-d"></a>

[Amazon Bedrock Mantle](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-chat-completions-mantle.html) provides an OpenAI-compatible inference endpoint for models available through Amazon Bedrock. This option does not require a stored credential. The container generates a short-lived bearer token from your execution role's IAM credentials and automatically refreshes it between benchmarks.

```
inference_provider:
  openai_compatible_endpoint:
    auth: "bedrock_mantle"
    region: "us-east-1"
    model_name: "us.amazon.nova-pro-v1:0"

benchmarks:
  s3_path: "s3://your-bucket/benchmarks/my_benchmarks/"
  tasks:
    - name: mmlu

eval:
  max_connections: 10
  max_retries: 50
  timeout: 600

output:
  s3_path: s3://your-bucket/eval/output/
```

Add the following permission to your execution role (see [Step 1: Set up IAM permissions](#nova-eval-container-step1)):

```
{
  "Sid": "BedrockMantleInference",
  "Effect": "Allow",
  "Action": [
    "bedrock-mantle:CreateInference",
    "bedrock-mantle:CallWithBearerToken"
  ],
  "Resource": "*"
}
```

For permissions guidance, see [Amazon Bedrock inference permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html) and [API key permissions control](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-permissions.html) in the Amazon Bedrock documentation.

### Option E: Evaluate an OpenAI-compatible endpoint
<a name="nova-eval-container-option-e"></a>

Use this option to evaluate through any OpenAI-compatible API endpoint — including [SageMaker Inference](https://aws.amazon.com/blogs/machine-learning/announcing-openai-compatible-api-support-for-amazon-sagemaker-ai-endpoints/) (AWS blog) or other OpenAI-compatible providers. This option uses the Inspect AI [OpenAI-compatible API provider](https://inspect.aisi.org.uk/providers.html#openai-api) on the Inspect AI website, which sends the configured credential as a bearer token in the `Authorization` header with each inference request. Bearer tokens are not logged by default.

**Token provider guidance**  
Always check your token provider's documentation for its recommended key management practices, rotation policies, and security guidance before configuring credential delivery.

**HTTPS requirement**  
HTTPS is required for all endpoints that use bearer token authentication. HTTP is allowed only for localhost addresses.

#### Using AWS Secrets Manager (recommended)
<a name="nova-eval-container-option-e-secrets"></a>

[AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) provides encrypted storage, access auditing through CloudTrail, and automatic rotation for API keys and other secrets. Store the API key in Secrets Manager and reference it by ARN in the recipe. The container fetches the key at runtime and auto-refreshes between benchmarks.

```
inference_provider:
  openai_compatible_endpoint:
    model_name: "my-model"
    base_url: "https://my-endpoint/v1"
    auth: api_key
    api_key_secret_arn: "arn:aws:secretsmanager:us-east-1:123456789012:secret:prod/my-api-key"
    region: "us-east-1"

benchmarks:
  s3_path: "s3://your-bucket/benchmarks/my_benchmarks/"
  tasks:
    - name: mmlu

eval:
  max_connections: 10
  max_retries: 50
  timeout: 600

output:
  s3_path: s3://your-bucket/eval/output/
```

Add the following permission to your execution role (see [Step 1: Set up IAM permissions](#nova-eval-container-step1)):

```
{
  "Sid": "GetApiKeySecret",
  "Effect": "Allow",
  "Action": "secretsmanager:GetSecretValue",
  "Resource": "arn:aws:secretsmanager:REGION:ACCOUNT_ID:secret:YOUR_SECRET_NAME"
}
```

#### Using environment variables
<a name="nova-eval-container-option-e-env"></a>

The API key can be passed through the environment variable `INFERENCE_API_KEY`. Check with your runtime environment documentation for how environment variables are passed and the security implications. For SageMaker Training Jobs, environment variables are visible in [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html) API responses and limited to 512 characters. For more information, see [SageMaker Training Job environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html#automatic-model-tuning-define-variables).

```
inference_provider:
  openai_compatible_endpoint:
    model_name: "my-model"
    base_url: "https://my-endpoint/v1"
    auth: api_key
    # No key source specified — reads from INFERENCE_API_KEY environment variable

benchmarks:
  s3_path: "s3://your-bucket/benchmarks/my_benchmarks/"
  tasks:
    - name: mmlu

eval:
  max_connections: 10
  max_retries: 50
  timeout: 600

output:
  s3_path: s3://your-bucket/eval/output/
```

For example, on SageMaker Training Jobs:

```
aws sagemaker create-training-job \
    ...
    --environment '{"INFERENCE_API_KEY": "your-api-key"}'
```

**Benchmarks configuration**

The `benchmarks` section defines which evaluation tasks to run. You can chain multiple benchmarks in a single job.


| Field | Required | Default | Description | 
| --- | --- | --- | --- | 
| name | Yes | — | A descriptive name for the benchmark run | 
| path | Yes | — | Relative path to the benchmark Python file in your S3 benchmarks directory | 
| limit | No | None (all samples) | Maximum number of samples to evaluate. Use for testing before full runs. | 
| epochs | No | 1 | Number of times to repeat the evaluation for statistical significance | 
| task\_args | No | — | Key-value pairs passed as arguments to the benchmark task function | 

**Eval configuration**

The `eval` section controls how the container executes evaluations.


| Parameter | Required | Default | Description | 
| --- | --- | --- | --- | 
| fail\_on\_error | No | false | Stop the evaluation if any sample fails. Set to true for strict validation. | 
| max\_connections | No | 10 | Number of parallel requests to the inference endpoint | 
| max\_retries | No | 3 | Number of retry attempts for failed inference requests | 
| timeout | No | 600 | Request timeout in seconds for each inference call | 
| extra\_args | No | — | Additional key-value pairs passed directly to the Inspect AI eval command | 

**Decoding parameters**

Configure model decoding parameters within the `eval.decoding` section:


| Parameter | Required | Default | Description | 
| --- | --- | --- | --- | 
| temperature | No | 0.0 | Controls randomness in generation. Use 0.0 for deterministic, reproducible benchmark results. | 
| top\_p | No | 1.0 | Nucleus sampling threshold. 1.0 means no restriction. | 
| top\_k | No | -1 | Limits word choices to the top K most likely tokens. -1 disables this filter. | 
| max\_tokens | No | 8192 | Maximum number of tokens to generate per response. Increase for benchmarks requiring long reasoning chains. | 
| reasoning\_effort | No | null | Controls reasoning depth for models that support it (for example, Amazon Nova models with extended thinking). Options: low, high, or null to disable. | 

**Output configuration**

The `output` section defines where and how evaluation results are stored.


| Field | Required | Default | Description | 
| --- | --- | --- | --- | 
| s3\_path | Yes | — | S3 URI where evaluation results are written | 
| output\_format | No | eval | Format for result files. See the following table for options. | 

The following output formats are available:


| Format | Description | 
| --- | --- | 
| eval | Native Inspect AI format. Compatible with inspect view for interactive analysis. | 
| csv | Comma-separated values. Suitable for spreadsheet analysis and data pipelines. | 
| jsonl | JSON Lines format. One JSON object per line for streaming processing. | 
| json | Standard JSON format. Complete results in a single structured file. | 

**MLflow configuration**

Optionally, you can log evaluation metrics to an MLflow tracking server. Add the `tracking` section to your recipe:

```
tracking:
  mlflow_tracking_arn: null       # ARN of SageMaker MLflow tracking server
  mlflow_experiment_name: "inspectlens" # experiment name
  mlflow_tracing: true          # log full request/response traces
  mlflow_log_artifacts: true       # upload .eval files to MLflow
```


| Field | Required | Default | Description | 
| --- | --- | --- | --- | 
| mlflow\_tracking\_arn | No | null | ARN of your SageMaker MLflow tracking server. Setting this enables MLflow logging. Omit or set to null to disable. | 
| mlflow\_experiment\_name | No | inspectlens | Name of the MLflow experiment to log runs under. | 
| mlflow\_tracing | No | true | When true, logs full request/response traces for each sample. | 
| mlflow\_log\_artifacts | No | true | When true, uploads .eval log files as MLflow artifacts. | 

**Full recipe reference**

The following example shows a complete recipe with all available configuration options:

```
inference_provider:
  sagemaker_endpoint:
    endpoint_name: my-nova-endpoint
    model_s3_uri: s3://your-bucket/models/my-model/
    inference_image_uri: "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-inference-repo:SM-Inference-latest"
    instance_type: ml.g5.12xlarge
    cleanup_endpoint: true
    region: us-west-2

benchmarks:
  - name: mmlu
    path: benchmarks/mmlu_pro.py
    limit: 100
    epochs: 3
    task_args:
      subject: math
  - name: truthfulqa
    path: benchmarks/truthfulqa.py
    limit: 50

eval:
  fail_on_error: false
  decoding:
    temperature: 0.0
    top_p: 1.0
    top_k: -1
    max_tokens: 8192
    reasoning_effort: null
  max_connections: 256
  max_retries: 50
  timeout: 600
  extra_args:
    - "--display"
    - "plain"

output:
  s3_path: s3://your-bucket/eval/output/
  output_format: eval

tracking:
  mlflow_tracking_arn: "arn:aws:sagemaker:us-west-2:123456789012:mlflow-tracking-server/my-server"
  mlflow_experiment_name: "inspectlens"
  mlflow_tracing: true
  mlflow_log_artifacts: true
```

## Step 3: Prepare benchmark files
<a name="nova-eval-container-step3"></a>

Benchmarks are Python files that use the Inspect AI `@task` decorator to define evaluation tasks. The [inspect-evals repository](https://github.com/UKGovernmentBEIS/inspect_evals) provides 128\+ ready-to-use benchmarks, or you can write your own.

**Example benchmark**

The following example shows a minimal benchmark that evaluates multiple-choice performance on a HuggingFace dataset:

```
from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset
from inspect_ai.scorer import choice
from inspect_ai.solver import multiple_choice


@task
def my_benchmark():
    return Task(
        dataset=hf_dataset(
            path="cais/mmlu",
            name="abstract_algebra",
            split="test",
        ),
        solver=multiple_choice(),
        scorer=choice(),
    )
```

**Dependencies**

If your benchmark needs extra dependencies, include a `pyproject.toml` or `requirements.txt` in the same S3 directory:

```
[project]
name = "my-benchmark"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "datasets>=2.14.0",
]
```

**Pre-installed packages**

The container includes the following packages. You do not need to list these in your `pyproject.toml`.


| Package | Version | 
| --- | --- | 
| Python | 3.12 | 
| inspect-ai | 0.3.220 | 
| boto3 | 1.40.61 | 
| aioboto3 | 15.5.0 | 
| openai | 2.36.0 | 
| mlflow | 3.12.0 | 
| pyyaml | 6.0.3 | 

**Task selection**

The `tasks` field in your recipe controls which tasks within a benchmark file to run.


| Configuration | Example | Behavior | 
| --- | --- | --- | 
| Empty tasks | tasks: [] | Runs all tasks defined in the benchmark file | 
| Name filter | tasks: ["algebra"] | Runs tasks whose name contains the substring "algebra" | 
| limit | limit: 50 | Caps the number of samples evaluated per task | 
| epochs | epochs: 3 | Repeats evaluation multiple times to measure variance | 

## Step 4: Prepare your S3 structure
<a name="nova-eval-container-step4"></a>

The following structure is a recommendation for keeping configs, benchmarks, and results organized. You can point the container at any S3 location — the structure itself is not required.

```
s3://your-bucket/
├── config/
│   └── inspect_config.yaml       # Your eval recipe
├── benchmarks/
│   └── my_benchmarks/            # Your benchmark Python files
│       ├── pyproject.toml        # Optional: benchmark dependencies
│       ├── my_task.py            # @task decorated functions
│       └── _helpers.py           # Shared utilities
└── output/                       # Results written here
```

Upload your files to S3:

```
# Upload benchmark files
aws s3 cp my_benchmarks/ s3://your-bucket/benchmarks/my_benchmarks/ --recursive

# Upload your eval recipe
aws s3 cp inspect_config.yaml s3://your-bucket/config/inspect_config.yaml
```

## Step 5: Submit the training job
<a name="nova-eval-container-step5"></a>

Submit a SageMaker Training Job to run your evaluation. You can use the AWS CLI or the SageMaker Python SDK.

**Option A: AWS CLI**

```
aws sagemaker create-training-job \
    --training-job-name inspect-eval-$(date +%Y%m%d-%H%M%S) \
    --algorithm-specification \
        TrainingImage=763104351884.dkr.ecr.us-east-1.amazonaws.com/sagemaker-inspect-ai:latest,TrainingInputMode=File \
    --role-arn arn:aws:iam::123456789012:role/SageMakerInspectAIRole \
    --resource-config \
        InstanceType=ml.m5.large,InstanceCount=1,VolumeSizeInGB=30 \
    --stopping-condition MaxRuntimeInSeconds=86400 \
    --input-data-config '[
        {
            "ChannelName": "config",
            "DataSource": {
                "S3DataSource": {
                    "S3DataType": "S3Prefix",
                    "S3Uri": "s3://your-bucket/eval/config/",
                    "S3DataDistributionType": "FullyReplicated"
                }
            }
        }
    ]' \
    --output-data-config S3OutputPath=s3://your-bucket/eval/output/ \
    --region us-west-2
```

**Option B: SageMaker Python SDK v3**

```
from sagemaker.train.evaluate import InspectAIEvaluator

evaluator = InspectAIEvaluator(
    model="nova-textgeneration-lite",
    bedrock_model_id="us.amazon.nova-lite-v1:0",
    benchmarks_path="s3://your-bucket/benchmarks/my_benchmarks/",
    tasks=[{"name": "my_task", "limit": 100}],
    s3_output_path="s3://your-bucket/eval/output/",
    instance_type="ml.m5.large",
)

execution = evaluator.evaluate()
execution.wait()
execution.show_results()
```

**Key parameters**


| Parameter | Value | Description | 
| --- | --- | --- | 
| TrainingImage | 763104351884.dkr.ecr.us-east-1.amazonaws.com/sagemaker-inspect-ai:latest | The Inspect AI container image | 
| InstanceType | ml.m5.large | Orchestrator instance type (not the inference instance) | 
| VolumeSizeInGB | 30 | Storage for benchmark data and logs | 
| MaxRuntimeInSeconds | 86400 | Maximum job duration (24 hours) | 
| ChannelName | config | Input channel containing your recipe and benchmark files | 

**Orchestrator instance type guidance**

The training job instance runs the evaluation orchestration logic, not the model inference. Choose an instance type based on your evaluation workload.


| Instance type | Use case | Guidance | 
| --- | --- | --- | 
| ml.m5.large | Recommended default | Sufficient for most evaluation workloads with moderate parallelism | 
| ml.m5.4xlarge | Large benchmark suites | Use when running many benchmarks with high max\_connections values | 
| ml.c5.large | Cost-sensitive | Lower cost alternative for simple evaluations with low parallelism | 

**Environment variables**

You can pass environment variables to the container for authentication or configuration. Add the `--environment` parameter to the AWS CLI command:

```
aws sagemaker create-training-job \
    ...
    --environment '{
        "HF_TOKEN": "hf_your_token_here",
        "HF_HUB_DOWNLOAD_TIMEOUT": "300"
    }'
```

## Step 6: Monitor the job
<a name="nova-eval-container-step6"></a>

After you submit the training job, you can monitor its progress through the AWS CLI or CloudWatch Logs.

**Check job status**

```
aws sagemaker describe-training-job \
    --training-job-name your-job-name \
    --query "TrainingJobStatus" \
    --output text
```

**Stream logs**

```
aws logs tail /aws/sagemaker/TrainingJobs \
    --log-stream-name-prefix your-job-name \
    --follow
```

**What to expect in logs**

The container logs show progress through the following stages:

1. **Startup** — Container initialization and configuration validation

1. **Benchmark download** — Downloading benchmark files and installing dependencies

1. **Endpoint setup** — Creating or connecting to the inference endpoint

1. **Evaluation** — Running benchmark tasks with progress indicators

1. **Results upload** — Writing results to S3 and optionally logging to MLflow

1. **Cleanup** — Deleting temporary endpoints if `cleanup_endpoint: true`

**Estimated timelines**


| Stage | Estimated duration | 
| --- | --- | 
| Container startup | 2–5 minutes | 
| Endpoint creation (if applicable) | 15–30 minutes | 
| Evaluation | Varies by benchmark size and model latency | 
| Cleanup | 1–2 minutes | 

## Step 7: View and interpret results
<a name="nova-eval-container-step7"></a>

After the job completes, view your evaluation results.

**View with Inspect AI**

Use the Inspect AI viewer to interactively explore results directly from S3:

```
inspect view --log-dir s3://your-bucket/eval-results/
```

This command opens a local web interface where you can browse scores, view individual samples, and compare runs.

**Download and share**

To download results locally:

```
aws s3 cp s3://your-bucket/eval/output/ ./results/ --recursive

INSPECT_LOG_DIR=./results inspect view
```

**VS Code extension**

The [Inspect AI VS Code extension](https://inspect.aisi.org.uk/vscode.html) lets you browse eval logs directly from S3 without downloading them first.

1. Install the extension from the VS Code marketplace (search "Inspect AI")

1. In the Inspect Activity Bar, locate the Logs pane and choose the folder icon

1. Enter your S3 path: `s3://your-bucket/eval-results/`

**Output structure**

Each evaluation produces a `.eval` log file that contains the following sections:
+ `results.scores` — Aggregate scores for each metric
+ `samples` — Individual evaluation samples with inputs, outputs, and scores
+ `stats` — Runtime statistics including token usage and latency
+ `eval.config` — The configuration used for the evaluation run

**View results in MLflow (optional)**

If you configured MLflow in your recipe, generate a presigned URL to access the tracking server:

```
aws sagemaker create-presigned-mlflow-tracking-server-url \
    --tracking-server-name my-server \
    --region us-west-2
```

Open the returned URL in your browser to view metrics, compare runs, and analyze trends across evaluations.

## Available benchmarks
<a name="nova-eval-container-benchmarks"></a>

The Inspect AI container works with any benchmark written in the Inspect AI task format. The [inspect-evals repository](https://github.com/UKGovernmentBEIS/inspect_evals) provides 128\+ ready-to-use benchmarks covering areas such as reasoning, knowledge, coding, and safety.

To write your own benchmarks, see the [Inspect AI task writing documentation](https://inspect.aisi.org.uk/tasks.html). If you find a public benchmark that is not yet available in inspect-evals, you can use the [AI assistant onboarding prompt](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/ai_assisted_benchmark_creation.md) to help convert it to the Inspect AI format.

## Agentic evaluations
<a name="nova-eval-container-agentic"></a>

Agentic benchmarks test a model's ability to complete multi-step tasks that require tool use, planning, and iterative reasoning. These evaluations simulate real-world scenarios where the model must call tools, interpret results, and decide on next actions.

**Endpoint requirements**

Agentic evaluations require endpoints that support the following capabilities:
+ **Tool calling** — The endpoint must support function calling to enable the model to invoke tools during evaluation
+ **Large context size** — Multi-turn conversations with tool results require sufficient context length to maintain conversation history

**SageMaker Inference endpoint configuration**

When using a SageMaker Inference endpoint for agentic evaluations, configure the following environment variables on your endpoint:


| Environment variable | Value | Description | 
| --- | --- | --- | 
| ENABLE\_TOOL\_CALLING | True | Activates tool calling support on the inference endpoint | 
| CONTEXT\_LENGTH | Sufficient for multi-turn | Set to a value large enough to accommodate multi-turn conversations with tool results | 

For information about setting up Amazon Nova endpoints on SageMaker Inference, see [Deploy Amazon Nova models on SageMaker](https://docs.aws.amazon.com/nova/latest/userguide/deploy-sagemaker.html). For information about container features and configuration, see [Container features](https://docs.aws.amazon.com/nova/latest/userguide/container-features.html).

**Amazon Bedrock endpoints**

For Amazon Bedrock endpoints, tool calling is natively supported for compatible models. For more information, see [Tool use with Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html).

**Getting started with agentic evaluations**

To run agentic evaluations, complete the following prerequisites:

1. Deploy an endpoint with tool calling enabled

1. Choose an agentic benchmark from the [inspect-evals repository](https://github.com/UKGovernmentBEIS/inspect_evals) (look for benchmarks that use tool-calling solvers)

1. Configure your recipe with appropriate `timeout` and `max_tokens` values for multi-turn interactions

**Amazon Bedrock endpoint**
+ For full setup and deployment, see [Amazon Bedrock endpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html).
+ For tool calling support, see the client-side tool calling section in [Tool use with Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html).

**Sample notebooks**

The following notebook demonstrates running a tool-calling agentic benchmark with the Inspect AI container:
+ [tau-bench (job-based)](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_tau_bench.ipynb) — Evaluate tool-augmented reasoning on customer service tasks using the Inspect AI container

For agentic benchmarks that require a Docker sandbox, use the Inspect AI SDK:
+ [SWE-bench with Inspect AI SDK](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/local_inspect_sdk/eval_swe_bench.ipynb) — Evaluate software engineering capabilities using Docker sandbox

**Important**  
Agentic benchmarks that require a Docker sandbox (such as SWE-bench) are not supported in the Inspect AI container experience. The SageMaker Training Job environment does not provide Docker-in-Docker capabilities. To run these benchmarks, use the [Inspect AI SDK](nova-eval-on-sagemaker-inference.md) on a compute environment with Docker access (for example, an Amazon EC2 instance or SageMaker notebook with Docker installed).

## Troubleshooting
<a name="nova-eval-container-troubleshooting"></a>

This section provides solutions for common issues when running evaluations with the Inspect AI container.

**Quick iteration tip**

Before submitting a SageMaker Training Job, test your benchmarks locally with the Inspect AI SDK. Run `inspect eval my_benchmark.py` on your local machine to validate task definitions, dependencies, and scoring logic before running at scale.

**InsufficientInstanceCapacity error**

This error occurs when AWS does not have enough capacity for the requested instance type in your Region.
+ Try a different instance type, or submit the job in another AWS Region
+ Use a different instance type (for example, `ml.m5.xlarge` instead of `ml.m5.large`)
+ Retry the request after a few minutes

**AccessDenied error**

If the training job fails with an access denied error, verify the following:
+ The role ARN in your job configuration is correct
+ The trust policy allows `sagemaker.amazonaws.com` to assume the role
+ Your user or role has the `iam:PassRole` permission for the execution role
+ The execution role has permissions to access the S3 bucket, inference endpoint, or Amazon Bedrock model

**Endpoint creation fails**

When using `cleanup_endpoint: true` with automatic endpoint creation, the following issues might occur:


| Error | Solution | 
| --- | --- | 
| ResourceLimitExceeded | Request a service quota increase for the inference instance type in your Region | 
| OutOfMemoryError | Use a larger inference instance type or reduce model size | 
| Wrong model\_s3\_uri | Verify the S3 path points to a valid model artifact directory | 
| Wrong inference image URI | Verify the image URI is correct for your Region and model framework | 
| Endpoint stuck in Creating | Check CloudWatch Logs for the endpoint. The model might fail health checks. Increase MaxRuntimeInSeconds if the endpoint needs more time. | 

**Manually cleaning up managed resources**

With managed endpoints enabled, managed resource information is logged to CloudWatch with the filter term `INFRA`. The logs include AWS CLI commands for manual cleanup if the container cannot complete teardown. Only run manual termination steps after the job is no longer in a running state.

Example log output:

```
[WARNING] [INFRA] Managed SMI resources created; auto-deleted on normal completion or stop.
If this job is force-killed or stopped mid-creation, delete them manually:
  aws sagemaker delete-endpoint --endpoint-name inspectlens-ep-1787856688 --region us-east-1
  aws sagemaker delete-endpoint-config --endpoint-config-name inspectlens-config-1787856688 --region us-east-1
  aws sagemaker delete-model --model-name inspectlens-model-1787856688 --region us-east-1
```

Upon manual termination of the job through [stop-training-job](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/stop-training-job.html), the container performs a best-effort cleanup of managed resources within the 120-second grace period. If resources cannot be cleaned up, the job ends with an error state. If cleanup completes successfully, the job ends in a stopped state.

**HuggingFace download timeouts**

If benchmarks that download datasets from HuggingFace Hub time out, set the `HF_HUB_DOWNLOAD_TIMEOUT` environment variable to a higher value (in seconds):

```
--environment '{"HF_HUB_DOWNLOAD_TIMEOUT": "600"}'
```

**Benchmark dependency conflicts**

If a benchmark fails due to dependency conflicts with pre-installed packages, create a `pyproject.toml` in the benchmark directory with explicit version constraints. The container installs benchmark dependencies in isolation to minimize conflicts.

**Eval scores look wrong**

If evaluation scores are unexpectedly low or inconsistent, check the following settings in your recipe:
+ **temperature** — Set to `0.0` for deterministic, reproducible results
+ **max\_tokens** — Ensure the value is large enough for the model to complete its response
+ **completion\_mode** — For base (non-chat) models, set `completion_mode: true` in your recipe to use completion-style prompting instead of chat format

## Data privacy
<a name="nova-eval-container-data-privacy"></a>

Your evaluation data is handled differently depending on the inference provider you use.

**SageMaker endpoint**

When you use a SageMaker Inference endpoint, all data stays within your AWS account. Evaluation prompts and model responses are not sent outside your account and are not used to improve AWS services. No opt-out policy is needed.

**Amazon Bedrock**

When you use Amazon Bedrock as the inference provider, your data is subject to the AWS AI Services Opt-Out Policy. To prevent your data from being used to improve AWS AI services, enable the opt-out policy at the AWS Organizations level. For more information, see [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html).


| Inference provider | Opt-out required | Details | 
| --- | --- | --- | 
| SageMaker endpoint | No | Data stays in your account. Not covered by AI opt-out policy. | 
| Amazon Bedrock | Yes | Enable the AWS AI Services Opt-Out Policy at the Organizations level to prevent data use for service improvement. | 