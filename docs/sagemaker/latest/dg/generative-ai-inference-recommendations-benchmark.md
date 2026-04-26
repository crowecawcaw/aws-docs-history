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
