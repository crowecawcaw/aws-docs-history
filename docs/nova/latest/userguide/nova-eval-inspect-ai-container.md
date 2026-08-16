# Evaluate with Inspect AI Container

The SageMaker Inspect AI container runs LLM model evaluations on SageMaker Training Jobs. The container uses [Inspect AI](https://inspect.ai-safety-institute.org.uk/ "https://inspect.ai-safety-institute.org.uk/") to provide a standardized evaluation process for models deployed to SageMaker inference endpoints or Amazon Bedrock — including Amazon Nova 1.0 (Micro, Lite, Pro) and 2.0 (Lite 2) models.

Previous [evaluation approaches](../nova2-userguide/nova-model-evaluation.md "../nova2-userguide/nova-model-evaluation.md") (based on [lighteval](https://github.com/huggingface/lighteval "https://github.com/huggingface/lighteval")) tightly coupled offline inference and evaluation logic, which limited flexibility in how models could be served and tested. The Inspect AI container decouples evaluation logic from inference entirely.

## Overview

Key benefits include:

- **Bring your own benchmarks** — write evaluation tasks in the Inspect AI format, then plug in domain-specific evaluation tasks without depending on a centralized team to onboard them.
- **Evaluate with different inference options** — works with SageMaker Inference (existing endpoint or create on-the-fly), Amazon Bedrock, and more inference backends incoming.
- **Iterate faster** — go from benchmark development to production evaluation without infrastructure changes. New benchmark onboarding that previously took days happens in minutes.
- **Run at scale** — chain multiple benchmarks in one job, mix standard benchmarks from the inspect-evals library with your own custom tasks in the same job.
- **One entry point for all training techniques** — whether your model was fine-tuned with SFT (SMTJ, SMHP), CPT (SMHP), or RFT (SMTJ, SMHP), the container evaluates it through the same interface. Evaluating mid-training checkpoints saved at specific steps is also supported (for example, step 500, step 1000) by pointing `model_s3_uri` at the checkpoint path.

### How it works

You provide two inputs to the container:

1. A YAML configuration file (recipe) that defines the inference provider, benchmarks, and evaluation parameters
2. Benchmark files (Python scripts with the `@task` decorator) uploaded to Amazon S3

The container handles endpoint management, evaluation execution, and result collection. When the training job completes, results are written to your specified S3 output location.

## Container image

The following table lists the Inspect AI container image URIs by AWS Region.

| Region    | Container image URI                                                        |
| --------- | -------------------------------------------------------------------------- |
| us-east-1 | `763104351884.dkr.ecr.us-east-1.amazonaws.com/sagemaker-inspect-ai:latest` |
| us-west-2 | `763104351884.dkr.ecr.us-west-2.amazonaws.com/sagemaker-inspect-ai:latest` |
| eu-west-2 | `763104351884.dkr.ecr.eu-west-2.amazonaws.com/sagemaker-inspect-ai:latest` |

## Prerequisites

Before you begin, ensure you have the following resources and access.

| Requirement                                           | Description                                                                                                                                                   |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS account with SageMaker access                     | An active AWS account with permissions to create SageMaker Training Jobs                                                                                      |
| S3 bucket                                             | A bucket to store your evaluation recipes, benchmark files, and output results                                                                                |
| IAM execution role                                    | A role that SageMaker can assume to access your resources                                                                                                     |
| SageMaker inference endpoint or Amazon Bedrock access | A deployed model endpoint or Amazon Bedrock model access for the model you want to evaluate                                                                   |
| AWS CLI or SageMaker Python SDK                       | Tools to submit training jobs and manage resources                                                                                                            |
| Capacity reservation (large models)                   | For models that require accelerated instances (such as p5 for Nova Lite 2), contact AWS Support to reserve capacity for SageMaker Inference or Amazon Bedrock |

## Step 1: Set up IAM permissions

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

The eval recipe is a YAML configuration file that defines how the container runs your evaluations. The recipe specifies the inference provider, benchmarks, evaluation parameters, and output settings.

For end-to-end examples, see the following notebooks:

- [Evaluate an existing SageMaker endpoint](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_sagemaker_endpoint.ipynb "https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_sagemaker_endpoint.ipynb")
- [Evaluate with a managed endpoint](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_managed_endpoint.ipynb "https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_managed_endpoint.ipynb")
- [Evaluate a Amazon Bedrock model](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_bedrock_model.ipynb "https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_bedrock_model.ipynb")

**Option A: Evaluate an existing SageMaker endpoint**

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

**Option B: Create endpoint, evaluate, then clean up**

Use this option to have the container deploy a Amazon Nova base or fine-tuned model, run evaluations, and tear down the endpoint automatically. This is the recommended approach for one-off evaluation runs. Retrieve the latest SageMaker inference container from the [Amazon Nova SageMaker Inference container images](nova-model-sagemaker-inference.md#nova-sagemaker-inference-container-images "nova-model-sagemaker-inference.md#nova-sagemaker-inference-container-images") documentation.

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

**Note on `model_s3_uri`:**

- **Amazon Nova GA models (base checkpoints)**: For example, `s3://escrow-nova-model-708977205387-us-east-1/nova-lite-2/prod/` — SageMaker manages access automatically, no additional S3 permissions needed.
- **Customized Amazon Nova models (post-training checkpoints)**: `s3://customer-escrow-ACCOUNT_ID-SUFFIX/YOUR_RUN_NAME/outputs/checkpoints/step_N/` — this is the escrow bucket path from your training job output.

**Option C: Evaluate through Amazon Bedrock**

Use this option to evaluate a model available through Amazon Bedrock without managing an endpoint.

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

**Benchmarks configuration**

The `benchmarks` section defines which evaluation tasks to run. You can chain multiple benchmarks in a single job.

| Field       | Required | Default            | Description                                                                |
| ----------- | -------- | ------------------ | -------------------------------------------------------------------------- |
| `name`      | Yes      | —                  | A descriptive name for the benchmark run                                   |
| `path`      | Yes      | —                  | Relative path to the benchmark Python file in your S3 benchmarks directory |
| `limit`     | No       | None (all samples) | Maximum number of samples to evaluate. Use for testing before full runs.   |
| `epochs`    | No       | 1                  | Number of times to repeat the evaluation for statistical significance      |
| `task_args` | No       | —                  | Key-value pairs passed as arguments to the benchmark task function         |

**Eval configuration**

The `eval` section controls how the container executes evaluations.

| Parameter         | Required | Default | Description                                                                   |
| ----------------- | -------- | ------- | ----------------------------------------------------------------------------- |
| `fail_on_error`   | No       | false   | Stop the evaluation if any sample fails. Set to `true` for strict validation. |
| `max_connections` | No       | 10      | Number of parallel requests to the inference endpoint                         |
| `max_retries`     | No       | 3       | Number of retry attempts for failed inference requests                        |
| `timeout`         | No       | 600     | Request timeout in seconds for each inference call                            |
| `extra_args`      | No       | —       | Additional key-value pairs passed directly to the Inspect AI eval command     |

**Decoding parameters**

Configure model decoding parameters within the `eval.decoding` section:

| Parameter          | Required | Default | Description                                                                                                                                                 |
| ------------------ | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `temperature`      | No       | 0.0     | Controls randomness in generation. Use `0.0` for deterministic, reproducible benchmark results.                                                             |
| `top_p`            | No       | 1.0     | Nucleus sampling threshold. `1.0` means no restriction.                                                                                                     |
| `top_k`            | No       | -1      | Limits word choices to the top K most likely tokens. `-1` disables this filter.                                                                             |
| `max_tokens`       | No       | 8192    | Maximum number of tokens to generate per response. Increase for benchmarks requiring long reasoning chains.                                                 |
| `reasoning_effort` | No       | null    | Controls reasoning depth for models that support it (for example, Amazon Nova models with extended thinking). Options: `low`, `high`, or `null` to disable. |

**Output configuration**

The `output` section defines where and how evaluation results are stored.

| Field           | Required | Default | Description                                                   |
| --------------- | -------- | ------- | ------------------------------------------------------------- |
| `s3_path`       | Yes      | —       | S3 URI where evaluation results are written                   |
| `output_format` | No       | eval    | Format for result files. See the following table for options. |

The following output formats are available:

| Format  | Description                                                                        |
| ------- | ---------------------------------------------------------------------------------- |
| `eval`  | Native Inspect AI format. Compatible with `inspect view` for interactive analysis. |
| `csv`   | Comma-separated values. Suitable for spreadsheet analysis and data pipelines.      |
| `jsonl` | JSON Lines format. One JSON object per line for streaming processing.              |
| `json`  | Standard JSON format. Complete results in a single structured file.                |

**MLflow configuration**

Optionally, you can log evaluation metrics to an MLflow tracking server. Add the `tracking` section to your recipe:

```
tracking:
  mlflow_tracking_arn: null       # ARN of SageMaker MLflow tracking server
  mlflow_experiment_name: "inspectlens" # experiment name
  mlflow_tracing: true          # log full request/response traces
  mlflow_log_artifacts: true       # upload .eval files to MLflow
```

| Field                    | Required | Default     | Description                                                                                                          |
| ------------------------ | -------- | ----------- | -------------------------------------------------------------------------------------------------------------------- |
| `mlflow_tracking_arn`    | No       | null        | ARN of your SageMaker MLflow tracking server. Setting this enables MLflow logging. Omit or set to `null` to disable. |
| `mlflow_experiment_name` | No       | inspectlens | Name of the MLflow experiment to log runs under.                                                                     |
| `mlflow_tracing`         | No       | true        | When `true`, logs full request/response traces for each sample.                                                      |
| `mlflow_log_artifacts`   | No       | true        | When `true`, uploads `.eval` log files as MLflow artifacts.                                                          |

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

Benchmarks are Python files that use the Inspect AI `@task` decorator to define evaluation tasks. The [inspect-evals repository](https://github.com/UKGovernmentBEIS/inspect_evals "https://github.com/UKGovernmentBEIS/inspect_evals") provides 128+ ready-to-use benchmarks, or you can write your own.

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

| Package    | Version |
| ---------- | ------- |
| Python     | 3.12    |
| inspect-ai | 0.3.220 |
| boto3      | 1.40.61 |
| aioboto3   | 15.5.0  |
| openai     | 2.36.0  |
| mlflow     | 3.12.0  |
| pyyaml     | 6.0.3   |

**Task selection**

The `tasks` field in your recipe controls which tasks within a benchmark file to run.

| Configuration | Example              | Behavior                                               |
| ------------- | -------------------- | ------------------------------------------------------ |
| Empty `tasks` | `tasks: []`          | Runs all tasks defined in the benchmark file           |
| Name filter   | `tasks: ["algebra"]` | Runs tasks whose name contains the substring "algebra" |
| `limit`       | `limit: 50`          | Caps the number of samples evaluated per task          |
| `epochs`      | `epochs: 3`          | Repeats evaluation multiple times to measure variance  |

## Step 4: Prepare your S3 structure

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

**Option B: SageMaker Python SDK V3**

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

| Parameter             | Value                                                                      | Description                                              |
| --------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| `TrainingImage`       | `763104351884.dkr.ecr.us-east-1.amazonaws.com/sagemaker-inspect-ai:latest` | The Inspect AI container image                           |
| `InstanceType`        | `ml.m5.large`                                                              | Orchestrator instance type (not the inference instance)  |
| `VolumeSizeInGB`      | `30`                                                                       | Storage for benchmark data and logs                      |
| `MaxRuntimeInSeconds` | `86400`                                                                    | Maximum job duration (24 hours)                          |
| `ChannelName`         | `config`                                                                   | Input channel containing your recipe and benchmark files |

**Orchestrator instance type guidance**

The training job instance runs the evaluation orchestration logic, not the model inference. Choose an instance type based on your evaluation workload.

| Instance type   | Use case               | Guidance                                                            |
| --------------- | ---------------------- | ------------------------------------------------------------------- |
| `ml.m5.large`   | Recommended default    | Sufficient for most evaluation workloads with moderate parallelism  |
| `ml.m5.4xlarge` | Large benchmark suites | Use when running many benchmarks with high `max_connections` values |
| `ml.c5.large`   | Cost-sensitive         | Lower cost alternative for simple evaluations with low parallelism  |

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
2. **Benchmark download** — Downloading benchmark files and installing dependencies
3. **Endpoint setup** — Creating or connecting to the inference endpoint
4. **Evaluation** — Running benchmark tasks with progress indicators
5. **Results upload** — Writing results to S3 and optionally logging to MLflow
6. **Cleanup** — Deleting temporary endpoints if `cleanup_endpoint: true`

**Estimated timelines**

| Stage                             | Estimated duration                         |
| --------------------------------- | ------------------------------------------ |
| Container startup                 | 2–5 minutes                                |
| Endpoint creation (if applicable) | 15–30 minutes                              |
| Evaluation                        | Varies by benchmark size and model latency |
| Cleanup                           | 1–2 minutes                                |

## Step 7: View and interpret results

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

The [Inspect AI VS Code extension](https://inspect.aisi.org.uk/vscode.html "https://inspect.aisi.org.uk/vscode.html") lets you browse eval logs directly from S3 without downloading them first.

1. Install the extension from the VS Code marketplace (search "Inspect AI")
2. In the Inspect Activity Bar, locate the Logs pane and choose the folder icon
3. Enter your S3 path: `s3://your-bucket/eval-results/`

**Output structure**

Each evaluation produces a `.eval` log file that contains the following sections:

- `results.scores` — Aggregate scores for each metric
- `samples` — Individual evaluation samples with inputs, outputs, and scores
- `stats` — Runtime statistics including token usage and latency
- `eval.config` — The configuration used for the evaluation run

**View results in MLflow (optional)**

If you configured MLflow in your recipe, generate a presigned URL to access the tracking server:

```
aws sagemaker create-presigned-mlflow-tracking-server-url \
    --tracking-server-name my-server \
    --region us-west-2
```

Open the returned URL in your browser to view metrics, compare runs, and analyze trends across evaluations.

## Available benchmarks

The Inspect AI container works with any benchmark written in the Inspect AI task format. The [inspect-evals repository](https://github.com/UKGovernmentBEIS/inspect_evals "https://github.com/UKGovernmentBEIS/inspect_evals") provides 128+ ready-to-use benchmarks covering areas such as reasoning, knowledge, coding, and safety.

To write your own benchmarks, see the [Inspect AI task writing documentation](https://inspect.aisi.org.uk/tasks.html "https://inspect.aisi.org.uk/tasks.html"). If you find a public benchmark that is not yet available in inspect-evals, you can use the [AI assistant onboarding prompt](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/ai_assisted_benchmark_creation.md "https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/ai_assisted_benchmark_creation.md") to help convert it to the Inspect AI format.

## Agentic evaluations

Agentic benchmarks test a model's ability to complete multi-step tasks that require tool use, planning, and iterative reasoning. These evaluations simulate real-world scenarios where the model must call tools, interpret results, and decide on next actions.

**Endpoint requirements**

Agentic evaluations require endpoints that support the following capabilities:

- **Tool calling** — The endpoint must support function calling to enable the model to invoke tools during evaluation
- **Large context size** — Multi-turn conversations with tool results require sufficient context length to maintain conversation history

**SageMaker Inference endpoint configuration**

When using a SageMaker Inference endpoint for agentic evaluations, configure the following environment variables on your endpoint:

| Environment variable  | Value                     | Description                                                                           |
| --------------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| `ENABLE_TOOL_CALLING` | `True`                    | Activates tool calling support on the inference endpoint                              |
| `CONTEXT_LENGTH`      | Sufficient for multi-turn | Set to a value large enough to accommodate multi-turn conversations with tool results |

For information about setting up Amazon Nova endpoints on SageMaker Inference, see [Deploy Amazon Nova models on SageMaker](deploy-sagemaker.md "deploy-sagemaker.md"). For information about container features and configuration, see [Container features](container-features.md "container-features.md").

**Amazon Bedrock endpoints**

For Amazon Bedrock endpoints, tool calling is natively supported for compatible models. For more information, see [Tool use with Amazon Bedrock](../../../bedrock/latest/userguide/tool-use.md "../../../bedrock/latest/userguide/tool-use.md").

**Getting started with agentic evaluations**

To run agentic evaluations, complete the following prerequisites:

1. Deploy an endpoint with tool calling enabled
2. Choose an agentic benchmark from the [inspect-evals repository](https://github.com/UKGovernmentBEIS/inspect_evals "https://github.com/UKGovernmentBEIS/inspect_evals") (look for benchmarks that use tool-calling solvers)
3. Configure your recipe with appropriate `timeout` and `max_tokens` values for multi-turn interactions

**Amazon Bedrock endpoint**

- For full setup and deployment, see [Amazon Bedrock endpoints](../../../bedrock/latest/userguide/endpoints.md "../../../bedrock/latest/userguide/endpoints.md").
- For tool calling support, see the client-side tool calling section in [Tool use with Amazon Bedrock](../../../bedrock/latest/userguide/tool-use.md "../../../bedrock/latest/userguide/tool-use.md").

**Sample notebooks**

The following notebook demonstrates running a tool-calling agentic benchmark with the Inspect AI container:

- [tau-bench (job-based)](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_tau_bench.ipynb "https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/inspect_eval_container/eval_tau_bench.ipynb") — Evaluate tool-augmented reasoning on customer service tasks using the Inspect AI container

For agentic benchmarks that require a Docker sandbox, use the Inspect AI SDK:

- [SWE-bench with Inspect AI SDK](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/local_inspect_sdk/eval_swe_bench.ipynb "https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/local_inspect_sdk/eval_swe_bench.ipynb") — Evaluate software engineering capabilities using Docker sandbox

###### Important

Agentic benchmarks that require a Docker sandbox (such as SWE-bench) are not supported in the Inspect AI container experience. The SageMaker Training Job environment does not provide Docker-in-Docker capabilities. To run these benchmarks, use the [Inspect AI SDK](nova-eval-on-sagemaker-inference.md "nova-eval-on-sagemaker-inference.md") on a compute environment with Docker access (for example, an Amazon EC2 instance or SageMaker notebook with Docker installed).

## Troubleshooting

This section provides solutions for common issues when running evaluations with the Inspect AI container.

**Quick iteration tip**

Before submitting a SageMaker Training Job, test your benchmarks locally with the Inspect AI SDK. Run `inspect eval my_benchmark.py` on your local machine to validate task definitions, dependencies, and scoring logic before running at scale.

**InsufficientInstanceCapacity error**

This error occurs when AWS does not have enough capacity for the requested instance type in your Region.

- Try a different instance type, or submit the job in another AWS Region
- Use a different instance type (for example, `ml.m5.xlarge` instead of `ml.m5.large`)
- Retry the request after a few minutes

**AccessDenied error**

If the training job fails with an access denied error, verify the following:

- The role ARN in your job configuration is correct
- The trust policy allows `sagemaker.amazonaws.com` to assume the role
- Your user or role has the `iam:PassRole` permission for the execution role
- The execution role has permissions to access the S3 bucket, inference endpoint, or Amazon Bedrock model

**Endpoint creation fails**

When using `cleanup_endpoint: true` with automatic endpoint creation, the following issues might occur:

| Error                      | Solution                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| ResourceLimitExceeded      | Request a service quota increase for the inference instance type in your Region                                                             |
| OutOfMemoryError           | Use a larger inference instance type or reduce model size                                                                                   |
| Wrong `model_s3_uri`       | Verify the S3 path points to a valid model artifact directory                                                                               |
| Wrong inference image URI  | Verify the image URI is correct for your Region and model framework                                                                         |
| Endpoint stuck in Creating | Check CloudWatch Logs for the endpoint. The model might fail health checks. Increase `MaxRuntimeInSeconds` if the endpoint needs more time. |

**HuggingFace download timeouts**

If benchmarks that download datasets from HuggingFace Hub time out, set the `HF_HUB_DOWNLOAD_TIMEOUT` environment variable to a higher value (in seconds):

```
--environment '{"HF_HUB_DOWNLOAD_TIMEOUT": "600"}'
```

**Job killed but endpoint still running**

If the training job is interrupted before cleanup completes, the inference endpoint might remain active. Manually delete the endpoint to avoid ongoing charges:

```
# List endpoints to find the orphaned one
aws sagemaker list-endpoints \
    --name-contains inspect \
    --query "Endpoints[].EndpointName" \
    --output table

# Delete the endpoint
aws sagemaker delete-endpoint \
    --endpoint-name your-endpoint-name

# Delete the endpoint configuration
aws sagemaker delete-endpoint-config \
    --endpoint-config-name your-endpoint-name

# Delete the model
aws sagemaker delete-model \
    --model-name your-endpoint-name
```

**Benchmark dependency conflicts**

If a benchmark fails due to dependency conflicts with pre-installed packages, create a `pyproject.toml` in the benchmark directory with explicit version constraints. The container installs benchmark dependencies in isolation to minimize conflicts.

**Eval scores look wrong**

If evaluation scores are unexpectedly low or inconsistent, check the following settings in your recipe:

- **temperature** — Set to `0.0` for deterministic, reproducible results
- **max\_tokens** — Ensure the value is large enough for the model to complete its response
- **completion\_mode** — For base (non-chat) models, set `completion_mode: true` in your recipe to use completion-style prompting instead of chat format

## Data privacy

Your evaluation data is handled differently depending on the inference provider you use.

**SageMaker endpoint**

When you use a SageMaker Inference endpoint, all data stays within your AWS account. Evaluation prompts and model responses are not sent outside your account and are not used to improve AWS services. No opt-out policy is needed.

**Amazon Bedrock**

When you use Amazon Bedrock as the inference provider, your data is subject to the AWS AI Services Opt-Out Policy. To prevent your data from being used to improve AWS AI services, enable the opt-out policy at the AWS Organizations level. For more information, see [AI services opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md").

| Inference provider | Opt-out required | Details                                                                                                           |
| ------------------ | ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| SageMaker endpoint | No               | Data stays in your account. Not covered by AI opt-out policy.                                                     |
| Amazon Bedrock     | Yes              | Enable the AWS AI Services Opt-Out Policy at the Organizations level to prevent data use for service improvement. |
