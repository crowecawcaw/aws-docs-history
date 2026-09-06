

# Set up a workload configuration for generative AI inference recommendations
<a name="generative-ai-inference-recommendations-workload-config"></a>

A workload configuration defines the traffic patterns and benchmark parameters that SageMaker AI uses when evaluating your model or endpoint. You create a workload configuration before running a recommendation job or a benchmark job. The same workload configuration can be reused across multiple jobs.

You can define your workload in two ways:
+ **Inline specification.** Specify token distributions and traffic parameters directly in the API call.
+ **Dataset from Amazon S3.** Provide a representative dataset of real requests using the `DatasetConfig` parameter.

## Create a workload configuration with inline parameters
<a name="generative-ai-inference-recommendations-workload-config-inline"></a>

Use inline parameters to specify token distributions when you don't have a representative dataset.

**Python (boto3)**

```
import boto3
import json

client = boto3.client("sagemaker", region_name="us-west-2")

workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "prompt_input_tokens_mean": 550,
        "prompt_input_tokens_stddev": 150,
        "output_tokens_mean": 150,
        "output_tokens_stddev": 50,
    },
}

response = client.create_ai_workload_config(
    AIWorkloadConfigName="my-workload-config",
    AIWorkloadConfigs={
        "WorkloadSpec": {"Inline": json.dumps(workload_spec)}
    },
)
print(response["AIWorkloadConfigArn"])
```

**AWS CLI**

```
aws sagemaker create-ai-workload-config \
  --ai-workload-config-name "my-workload-config" \
  --ai-workload-configs '{"WorkloadSpec": {"Inline": "{\"benchmark\": {\"type\": \"aiperf\"}, \"parameters\": {\"prompt_input_tokens_mean\": 550, \"output_tokens_mean\": 150}}"}}' \
  --region us-west-2
```

## Create a workload configuration with a dataset
<a name="generative-ai-inference-recommendations-workload-config-dataset"></a>

If you have a representative dataset of real requests, provide it through Amazon S3 using the `DatasetConfig` parameter with an `InputDataConfig` channel.

```
response = client.create_ai_workload_config(
    AIWorkloadConfigName="my-dataset-workload",
    DatasetConfig={
        "InputDataConfig": [
            {
                "ChannelName": "traffic",
                "DataSource": {
                    "S3DataSource": {
                        "S3Uri": "s3://DOC-EXAMPLE-BUCKET/datasets/traffic-trace/"
                    }
                }
            }
        ]
    },
    AIWorkloadConfigs={
        "WorkloadSpec": {"Inline": json.dumps(workload_spec)}
    },
)
```

By default, synthetic prompts are generated. You can also use a public dataset or provide a custom dataset from Amazon S3.

## Workload configuration for benchmarking
<a name="generative-ai-inference-recommendations-workload-config-benchmark"></a>

When creating a workload configuration for benchmarking an existing endpoint, you can specify additional parameters such as the tokenizer, concurrency, request count, and request rate.

```
workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "tokenizer": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        "concurrency": 1,
        "request_count": 10,
        "streaming": True,
        "prompt_input_tokens_mean": 550,
        "prompt_input_tokens_stddev": 150,
        "output_tokens_mean": 50,
        "output_tokens_stddev": 10,
        "request_rate": 1.0,
        "benchmark_duration": 60,
    },
    "tooling": {"api_standard": "openai", "version": "0.6.0"},
}
```

## Manage workload configurations
<a name="generative-ai-inference-recommendations-workload-config-manage"></a>

Use the following operations to manage your workload configurations.

```
# List workload configurations
response = client.list_ai_workload_configs(MaxResults=10)
for config in response["AIWorkloadConfigs"]:
    print(f"{config['AIWorkloadConfigName']} - {config['AIWorkloadConfigArn']}")

# Describe a workload configuration
response = client.describe_ai_workload_config(
    AIWorkloadConfigName="my-workload-config"
)

# Delete a workload configuration
client.delete_ai_workload_config(
    AIWorkloadConfigName="my-workload-config"
)
```

## Workload specification reference
<a name="generative-ai-inference-recommendations-workload-config-reference"></a>

This section provides the complete schema for the workload specification JSON document that you pass in the `WorkloadSpec.Inline` field when creating a workload configuration.

### Syntax
<a name="generative-ai-inference-recommendations-workload-config-syntax"></a>

The following is a representative example of a workload specification with commonly used parameters. All parameters are documented in the reference table below.

```
{
    "benchmark": {
        "type": "aiperf"
    },
    "parameters": {
        "prompt_input_tokens_mean": 550,
        "prompt_input_tokens_stddev": 150.0,
        "output_tokens_mean": 150,
        "output_tokens_stddev": 50.0,
        "concurrency": 10,
        "request_count": 100,
        "request_rate": 5.0,
        "benchmark_duration": 120,
        "streaming": true,
        "tokenizer": "meta-llama/Llama-3.2-1B"
    },
    "secrets": {
        "hf_token": "arn:aws:secretsmanager:us-west-2:111122223333:secret:my-hf-token-AbCdEf"
    },
    "tooling": {
        "api_standard": "openai"
    }
}
```

### Workload specification keys
<a name="generative-ai-inference-recommendations-workload-config-keys"></a>

The workload specification contains the following top-level keys. Unknown keys are rejected.

#### benchmark
<a name="workload-config-ref-benchmark"></a>

Required mapping. Identifies the benchmarking tool to use.

`benchmark/type`  
Required. The benchmark engine. The only valid value is `aiperf`.

#### parameters
<a name="workload-config-ref-parameters"></a>

Optional mapping. Benchmark parameters passed to the AIPerf engine. Unknown parameter names are rejected. All parameters are optional unless noted otherwise.

**Token distribution**

`prompt_input_tokens_mean`  
Integer. Mean number of input tokens per request for synthetic prompt generation. Aliases: `synthetic_input_tokens_mean`, `isl`.

`prompt_input_tokens_stddev`  
Float. Standard deviation of input token count. Aliases: `synthetic_input_tokens_stddev`, `isl_stddev`.

`output_tokens_mean`  
Integer. Mean number of output tokens per request. Aliases: `prompt_output_tokens_mean`, `osl`.

`output_tokens_stddev`  
Float. Standard deviation of output token count. Aliases: `prompt_output_tokens_stddev`, `osl_stddev`.

**Traffic shaping**

`concurrency`  
Integer. Number of concurrent requests to send during the benchmark.

`request_count`  
Integer. Total number of requests to send. Alias: `num_requests`.

`request_rate`  
Float. Target requests per second.

`benchmark_duration`  
Integer. Duration of the benchmark in seconds.

`max_concurrency`  
Integer. Maximum number of concurrent requests allowed.

`request_rate_mode`  
String. Request arrival pattern. Alias: `arrival_pattern`.

`arrival_smoothness`  
Float. Controls burstiness of request arrivals. Higher values produce smoother traffic. Alias: `vllm_burstiness`.

`prefill_concurrency`  
Integer. Number of concurrent prefill requests.

**General**

`streaming`  
Boolean. Whether to use streaming responses. Default: `true`.

`tokenizer`  
String. HuggingFace model name or local directory path for the tokenizer used to count tokens. Example: `meta-llama/Llama-3.2-1B`.

`hf_token`  
String. Hugging Face access token for downloading gated models and tokenizers. Alias: `HF_TOKEN`. For sensitive values, use the `secrets` section instead of passing the token in plaintext.

`request_timeout_seconds`  
Integer. Timeout in seconds for individual requests.

`goodput`  
String. Define service level objectives (SLOs) for goodput measurement. Goodput is the number of completed requests per second that meet all specified latency constraints. Format: space-separated `metric:threshold_ms` pairs. For example, `"time_to_first_token:100 inter_token_latency:10"` measures throughput counting only requests where TTFT is under 100ms and ITL is under 10ms. When set, the benchmark results include a `goodput` metric (requests/sec meeting all SLOs) and a `good_request_fraction` metric (proportion of requests meeting all SLOs). Requires streaming mode for token-level metrics.

`benchmark_grace_period`  
Integer. Grace period in seconds after the benchmark completes to allow in-flight requests to finish.

`extra_inputs`  
String. Space-separated key-value pairs passed through to the benchmark tool. Each pair uses `key:value` format. Common keys include `payload_template:/path/to/template.jinja` for custom-format endpoints, `response_field:jmespath.query` for response extraction, and `ignore_eos:true` to force max\_tokens generation.

`random_seed`  
Integer. Seed for random number generation. Default: `42`.

`verbose`  
Boolean. Enable verbose logging. Default: `false`.

`num_conversations`  
Integer. Number of multi-turn conversations to simulate. Aliases: `conversation_num`, `num_sessions`.

`model_selection_strategy`  
String. Strategy for selecting models when multiple models are available on the endpoint.

**Warmup**

Warmup parameters control an optional warm-up phase that runs before the measured benchmark. This primes the model server's caches and JIT compilation.

`warmup_duration`  
Integer. Duration of the warmup phase in seconds.

`warmup_request_count`  
Integer. Number of warmup requests. Alias: `num_warmup_requests`.

`warmup_concurrency`  
Integer. Concurrency level during warmup.

`warmup_prefill_concurrency`  
Integer. Prefill concurrency during warmup.

`warmup_request_rate`  
Float. Request rate during warmup.

`warmup_arrival_pattern`  
String. Arrival pattern during warmup.

`warmup_grace_period`  
Float. Grace period in seconds after warmup completes.

`num_warmup_sessions`  
Integer. Number of warmup sessions.

**Dataset**

`public_dataset`  
String. Name of a public dataset to use for benchmark prompts instead of synthetic generation.

`custom_dataset_type`  
String. Format of a custom dataset provided via Amazon S3.

`input_file`  
String. Path to the input dataset file inside the benchmark container. When you provide a dataset through the `DatasetConfig` parameter, the data is mounted at `/opt/ml/input/data/{ChannelName}/`. Use this parameter to point to a specific file within that mount path.

`dataset_sampling_strategy`  
String. Controls how prompts are sampled from the dataset pool during benchmarking. Valid values: `shuffle` (default) — randomly shuffles the dataset and draws prompts without replacement; `sequential` — sends prompts in the order they appear in the dataset file. Use `sequential` when prompt order matters for your evaluation (for example, when measuring performance across increasing prompt lengths).

**Image inputs**

Parameters for benchmarking multimodal models that accept image inputs.

`image_width_mean`  
Float. Mean width of synthetic images in pixels.

`image_width_stddev`  
Float. Standard deviation of image width.

`image_height_mean`  
Float. Mean height of synthetic images in pixels.

`image_height_stddev`  
Float. Standard deviation of image height.

`image_batch_size`  
Integer. Number of images per request. Alias: `batch_size_image`.

`image_format`  
String. Image format (for example, `png`, `jpeg`).

**Video inputs**

Parameters for benchmarking multimodal models that accept video inputs.

`video_batch_size`  
Integer. Number of videos per request. Alias: `batch_size_video`.

`video_duration`  
Float. Duration of synthetic videos in seconds.

`video_fps`  
Integer. Frames per second for synthetic videos.

`video_width`  
Integer. Width of synthetic videos in pixels.

`video_height`  
Integer. Height of synthetic videos in pixels.

`video_synth_type`  
String. Type of synthetic video generation.

`video_format`  
String. Video container format.

`video_codec`  
String. Video codec.

`video_audio_sample_rate`  
Integer. Audio sample rate in Hz.

`video_audio_num_channels`  
Integer. Number of audio channels.

`video_audio_codec`  
String. Audio codec.

`video_audio_depth`  
String. Audio bit depth.

#### secrets
<a name="workload-config-ref-secrets"></a>

Optional mapping. Use this section to pass sensitive values (such as Hugging Face access tokens) by referencing AWS Secrets Manager secrets instead of including them as plaintext in `parameters`.

Each key is a parameter name, and the value is the ARN of the secret in AWS Secrets Manager. At job start time, the service resolves the secret and injects the value into the benchmark environment.

```
"secrets": {
    "hf_token": "arn:aws:secretsmanager:us-west-2:111122223333:secret:my-hf-token-AbCdEf"
}
```

#### tooling
<a name="workload-config-ref-tooling"></a>

Optional mapping. Specifies the API standard and tool version.

`tooling/api_standard`  
Optional. The API standard used by the endpoint. For example, `openai`.

`tooling/version`  
Optional. The version of the benchmarking tool. Defaults to the latest available version.