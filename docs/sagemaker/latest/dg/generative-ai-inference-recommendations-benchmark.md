# Benchmark generative AI inference endpoints

The SageMaker AI benchmarking service measures the performance of large language models (LLMs)
hosted on SageMaker AI endpoints. It runs benchmarks using NVIDIA AIPerf, producing metrics such
as request latency, throughput, time to first token, and inter-token latency.

## Prerequisites

Before you create a benchmark job, you need the following:

- A SageMaker AI endpoint in `InService` status hosting an LLM that
  supports the OpenAI-compatible chat completions API
- An Amazon S3 bucket for benchmark output
- An IAM execution role that grants SageMaker AI access to your endpoint and output
  bucket

## Step 1: Create a benchmark job

A benchmark job targets a specific SageMaker AI endpoint and references a workload
configuration.

**Python (boto3)**

```

response = client.create_ai_benchmark_job(
    AIBenchmarkJobName="my-benchmark-job",
    BenchmarkTarget={
        "Endpoint": {
            "Identifier": "my-sagemaker-endpoint"
        }
    },
    OutputConfig={
        "S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/benchmark-results/"
    },
    AIWorkloadConfigIdentifier="my-benchmark-config",
    RoleArn="arn:aws:iam::111122223333:role/ExampleRole",
)
print(response["AIBenchmarkJobArn"])

```

**AWS CLI**

```

aws sagemaker create-ai-benchmark-job \
  --ai-benchmark-job-name "my-benchmark-job" \
  --benchmark-target '{"Endpoint": {"Identifier": "my-sagemaker-endpoint"}}' \
  --output-config '{"S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/benchmark-results/"}' \
  --ai-workload-config-identifier "my-benchmark-config" \
  --role-arn "arn:aws:iam::111122223333:role/ExampleRole" \
  --region us-west-2

```

If your endpoint hosts multiple models through inference components, you can
specify them in the `InferenceComponents` parameter of the
`BenchmarkTarget`.

If your endpoint is in a VPC, pass the `NetworkConfig` parameter with
your `VpcConfig` settings, including security group IDs and
subnets.

## Benchmark inference components

If your endpoint uses _inference components_ instead of
deploying a model directly, you must specify the inference components to
benchmark in the `BenchmarkTarget`. When inference components are
specified, the benchmarking service routes requests to those specific components
rather than the endpoint's default model.

Pass one or more inference component names or ARNs in the
`InferenceComponents` list:

**Python (boto3)**

```

response = client.create_ai_benchmark_job(
    AIBenchmarkJobName="my-ic-benchmark",
    BenchmarkTarget={
        "Endpoint": {
            "Identifier": "my-multi-model-endpoint",
            "InferenceComponents": [
                {"Identifier": "my-inference-component-llama"}
            ]
        }
    },
    OutputConfig={
        "S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/benchmark-results/"
    },
    AIWorkloadConfigIdentifier="my-benchmark-config",
    RoleArn="arn:aws:iam::111122223333:role/ExampleRole",
)

```

**AWS CLI**

```

aws sagemaker create-ai-benchmark-job \
  --ai-benchmark-job-name "my-ic-benchmark" \
  --benchmark-target '{
    "Endpoint": {
      "Identifier": "my-multi-model-endpoint",
      "InferenceComponents": [
        {"Identifier": "my-inference-component-llama"}
      ]
    }
  }' \
  --output-config '{"S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/benchmark-results/"}' \
  --ai-workload-config-identifier "my-benchmark-config" \
  --role-arn "arn:aws:iam::111122223333:role/ExampleRole" \
  --region us-west-2

```

###### Note

If your endpoint is configured for inference components but you don't
specify `InferenceComponents` in the benchmark target, the job
fails with an error indicating that no model is deployed directly on the
endpoint. Always include the `InferenceComponents` parameter
when benchmarking inference-component-based endpoints.

## Benchmark multi-LoRA endpoints

To benchmark an endpoint that serves multiple LoRA adapters, specify each
adapter as an inference component in the `BenchmarkTarget`. You can
optionally use the `model_selection_strategy` workload parameter to
control how the benchmark distributes requests across adapters. If you don't
specify a strategy, the default is `round_robin`.

First, create a workload configuration. The following example includes the
optional `model_selection_strategy` parameter:

```

# Create a workload config for multi-LoRA benchmarking
workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "prompt_input_tokens_mean": 550,
        "output_tokens_mean": 150,
        "concurrency": 10,
        "streaming": True,
        "tokenizer": "meta-llama/Llama-3.2-1B",
        "model_selection_strategy": "round_robin"
    },
    "secrets": {
        "hf_token": "arn:aws:secretsmanager:us-west-2:111122223333:secret:my-hf-token-AbCdEf"
    },
    "tooling": {"api_standard": "openai"}
}

import json
client.create_ai_workload_config(
    AIWorkloadConfigName="multi-lora-config",
    WorkloadSpec={"Inline": json.dumps(workload_spec)}
)

```

Then, create a benchmark job that targets all the LoRA adapter inference
components:

```

response = client.create_ai_benchmark_job(
    AIBenchmarkJobName="multi-lora-benchmark",
    BenchmarkTarget={
        "Endpoint": {
            "Identifier": "my-lora-endpoint",
            "InferenceComponents": [
                {"Identifier": "lora-adapter-customer-support"},
                {"Identifier": "lora-adapter-code-generation"},
                {"Identifier": "lora-adapter-summarization"}
            ]
        }
    },
    OutputConfig={
        "S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/multi-lora-results/"
    },
    AIWorkloadConfigIdentifier="multi-lora-config",
    RoleArn="arn:aws:iam::111122223333:role/ExampleRole",
)

```

The `model_selection_strategy` parameter is optional and determines
how the benchmark tool distributes requests across the specified inference
components. Valid values are:

- `round_robin` (default) — each adapter receives requests
  in order. The nth request is sent to the (n mod number-of-models)th
  adapter.
- `random` — each request is assigned to an adapter
  uniformly at random.

If you don't specify `model_selection_strategy`, the benchmark
uses `round_robin` by default.

## Step 2: Monitor job status

Poll the job status until it reaches a terminal state.

**Python (boto3)**

```

import time

while True:
    response = client.describe_ai_benchmark_job(
        AIBenchmarkJobName="my-benchmark-job"
    )
    status = response["AIBenchmarkJobStatus"]
    print(f"Status: {status}")
    if status in ("Completed", "Failed", "Stopped"):
        break
    time.sleep(30)

if status == "Completed":
    print(f"Results at: {response['OutputConfig']['S3OutputLocation']}")
elif status == "Failed":
    print(f"Job failed: {response.get('FailureReason', 'unknown')}")

```

**AWS CLI**

```

aws sagemaker describe-ai-benchmark-job \
  --ai-benchmark-job-name "my-benchmark-job" \
  --region us-west-2

```

## Step 3: Review benchmark results

Benchmark results are written to the Amazon S3 output location that you specified. The
results include the following key metrics:

`request_throughput`

Requests per second.

`request_latency`

End-to-end request latency with percentile breakdowns (P50, P90,
P99).

`time_to_first_token`

Time from request submission to the first token received.

`inter_token_latency`

Time between consecutive output tokens.

`output_token_throughput`

Output tokens generated per second.

Each metric includes statistical summaries: average, minimum, maximum, P50, P90,
P99, and standard deviation.

## Manage benchmark resources

Use the following operations to manage your benchmark jobs and workload
configurations.

```

# List benchmark jobs
response = client.list_ai_benchmark_jobs(MaxResults=10)
for job in response["AIBenchmarkJobs"]:
    print(f"{job['AIBenchmarkJobName']} - {job['AIBenchmarkJobStatus']}")

# Stop a running job
client.stop_ai_benchmark_job(
    AIBenchmarkJobName="my-benchmark-job"
)

# Delete a job (must be in a terminal state)
client.delete_ai_benchmark_job(
    AIBenchmarkJobName="my-benchmark-job"
)

# List workload configurations
response = client.list_ai_workload_configs(MaxResults=10)
for config in response["AIWorkloadConfigs"]:
    print(f"{config['AIWorkloadConfigName']} - {config['AIWorkloadConfigArn']}")

# Delete a workload configuration
client.delete_ai_workload_config(
    AIWorkloadConfigName="my-benchmark-config"
)

```
