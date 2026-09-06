

# Get generative AI inference deployment recommendations
<a name="generative-ai-inference-recommendations-get-started"></a>

AI recommendation jobs analyze your model and workload characteristics to generate deployment configurations optimized for cost, latency, or throughput. The service evaluates instance types, applies optimizations like speculative decoding, and benchmarks each configuration on real GPU infrastructure.

## Prerequisites
<a name="generative-ai-inference-recommendations-get-started-prereqs"></a>

Before you create a recommendation job, you need the following:
+ Model artifacts stored in Amazon S3 in HuggingFace checkpoint format with SafeTensor weights
+ An Amazon S3 bucket for recommendation output
+ An AWS Identity and Access Management (IAM) execution role that grants SageMaker AI access to your model artifacts and output bucket

## Step 1: Create a recommendation job
<a name="generative-ai-inference-recommendations-get-started-create"></a>

A recommendation job analyzes your model and generates deployment recommendations. You specify the model location, output location, workload configuration, and a performance target.

**Python (boto3)**

```
response = client.create_ai_recommendation_job(
    AIRecommendationJobName="my-recommendation-job",
    ModelSource={
        "S3": {
            "S3Uri": "s3://DOC-EXAMPLE-BUCKET/models/my-model/",
        }
    },
    OutputConfig={
        "S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/recommendations/"
    },
    PerformanceTarget={
        "Constraints": [
            {"Metric": "ttft-ms"}
        ]
    },
    AIWorkloadConfigIdentifier="my-recommendation-workload",
    RoleArn="arn:aws:iam::111122223333:role/ExampleRole",
)
print(response["AIRecommendationJobArn"])
```

**AWS CLI**

```
aws sagemaker create-ai-recommendation-job \
  --ai-recommendation-job-name "my-recommendation-job" \
  --model-source '{"S3": {"S3Uri": "s3://DOC-EXAMPLE-BUCKET/models/my-model/"}}' \
  --output-config '{"S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/recommendations/"}' \
  --performance-target '{"Constraints": [{"Metric": "ttft-ms"}]}' \
  --ai-workload-config-identifier "my-recommendation-workload" \
  --role-arn "arn:aws:iam::111122223333:role/ExampleRole" \
  --region us-west-2
```

You can also specify the following optional parameters:

`ComputeSpec`  
Restrict the instance types to evaluate (maximum three). For example: `{"InstanceTypes": ["ml.g5.12xlarge", "ml.p4d.24xlarge"]}`

`OptimizeModel`  
Set to `true` to allow model optimizations such as speculative decoding.

`InferenceSpecification`  
Specify the inference framework. Valid values: `LMI`, `VLLM`.

To track the recommendation results with fully managed MLflow on SageMaker AI, add an `MlflowConfig` object to `OutputConfig`. For more information, see [Track inference recommendation and benchmark results with MLflow](generative-ai-inference-recommendations-mlflow.md).

## Step 2: Monitor job status
<a name="generative-ai-inference-recommendations-get-started-monitor"></a>

Poll the job status until it reaches a terminal state.

**Python (boto3)**

```
import time

while True:
    response = client.describe_ai_recommendation_job(
        AIRecommendationJobName="my-recommendation-job"
    )
    status = response["AIRecommendationJobStatus"]
    print(f"Status: {status}")
    if status in ("Completed", "Failed", "Stopped"):
        break
    time.sleep(30)
```

**AWS CLI**

```
aws sagemaker describe-ai-recommendation-job \
  --ai-recommendation-job-name "my-recommendation-job" \
  --region us-west-2
```

## Step 3: Review recommendations
<a name="generative-ai-inference-recommendations-get-started-results"></a>

When the job completes, the describe response includes a `Recommendations` array. Each recommendation contains a deployment-ready configuration with the following information:

`DeploymentConfiguration`  
Container image URI, instance type, instance count, and environment variables. You can use this configuration to deploy directly to a SageMaker AI endpoint.

`ExpectedPerformance`  
Validated performance metrics including Time to First Token (TTFT), request latency at P90 and P99, throughput in tokens per second, and request throughput.

`OptimizationDetails`  
Applied optimization techniques such as speculative decoding or kernel tuning, with their configuration parameters.

The following optimization techniques may be applied:

Speculative decoding  
Speculative decoding speeds up text generation by processing multiple tokens in parallel rather than one token at a time. A lightweight speculator proposes several candidate tokens in a single step, and the primary model then verifies them together in one forward pass, keeping the candidates that agree with its own distribution and discarding the rest. The speculator is trained to align with the primary model's data distribution so that more of its proposals are accepted, which directly translates into more useful tokens produced per forward pass. The output distribution of the primary model is preserved, so response quality is unchanged. The result is higher output tokens per second and lower inter-token latency (ITL), thereby improving your throughput metrics.

Kernel tuning  
Kernel tuning starts with parsing the model execution graph to identify performance-critical kernels that are good candidates for tuning, such as attention and fused operator kernels. Their launch and tiling parameters are then tuned so the implementation is better matched to the target GPU hardware and the expected traffic pattern, such as concurrency. These parameters affect memory reuse, cache locality, and parallelism, improving execution efficiency. The number of pipeline stages used for loading data and computing is also tuned, helping overlap memory movement with computation. By tuning these parameters for the specific combination of model, hardware, and serving workload, kernel tuning improves throughput and latency by ensuring the GPU is fully utilized.

The following performance target metrics are available:

`ttft-ms`  
Time to first token in milliseconds.

`throughput`  
Tokens per second.

`cost`  
Cost per hour of the deployment configuration.

Each metric in the `ExpectedPerformance` response includes a `Stat` field indicating the statistical measure, a `Value`, and an optional `Unit`. Common statistics include: `average`, `p50`, `p90`, `p95`, `p99`, `max`, and `min`.

## Manage recommendation resources
<a name="generative-ai-inference-recommendations-get-started-manage"></a>

Use the following operations to manage your recommendation jobs and workload configurations.

```
# List recommendation jobs
response = client.list_ai_recommendation_jobs(MaxResults=10)
for job in response["AIRecommendationJobs"]:
    print(f"{job['AIRecommendationJobName']} - {job['AIRecommendationJobStatus']}")

# Stop a running job
client.stop_ai_recommendation_job(
    AIRecommendationJobName="my-recommendation-job"
)

# Delete a job (must be in a terminal state)
client.delete_ai_recommendation_job(
    AIRecommendationJobName="my-recommendation-job"
)

# List workload configurations
response = client.list_ai_workload_configs(MaxResults=10)
for config in response["AIWorkloadConfigs"]:
    print(f"{config['AIWorkloadConfigName']} - {config['AIWorkloadConfigArn']}")

# Delete a workload configuration
client.delete_ai_workload_config(
    AIWorkloadConfigName="my-recommendation-workload"
)
```