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

To track the benchmark results with fully managed MLflow on SageMaker AI, add an
`MlflowConfig` object to `OutputConfig`. For more information, see
[Track inference recommendation and benchmark results with MLflow](generative-ai-inference-recommendations-mlflow.md "generative-ai-inference-recommendations-mlflow.md").

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

## Benchmark multimodal endpoints with synthetic images

You can benchmark vision-language models by generating synthetic images as part
of the workload configuration. The benchmarking service uses AIPerf to create
images with configurable dimensions and format, then sends them as base64-encoded
payloads to your endpoint.

The following example creates a workload configuration for benchmarking a
vision-language model with synthetic images:

```

import json

workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "image_width_mean": 640,
        "image_height_mean": 480,
        "prompt_input_tokens_mean": 100,
        "output_tokens_mean": 150,
        "concurrency": 8,
        "request_count": 100,
        "streaming": True,
        "tokenizer": "meta-llama/Llama-3.2-1B"
    },
    "secrets": {
        "hf_token": "arn:aws:secretsmanager:us-west-2:111122223333:secret:my-hf-token-AbCdEf"
    }
}

client.create_ai_workload_config(
    AIWorkloadConfigName="image-benchmark-config",
    WorkloadSpec={"Inline": json.dumps(workload_spec)}
)

```

The following parameters control synthetic image generation:

| Parameter             | Type   | Default | Description                                                                                                                              |
| --------------------- | ------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `image_width_mean`    | float  | None    | Mean image width in pixels.                                                                                                              |
| `image_width_stddev`  | float  | None    | Standard deviation of image width. Set to vary image<br>dimensions across requests.                                                      |
| `image_height_mean`   | float  | None    | Mean image height in pixels.                                                                                                             |
| `image_height_stddev` | float  | None    | Standard deviation of image height.                                                                                                      |
| `image_batch_size`    | int    | 1       | Number of images per request.                                                                                                            |
| `image_format`        | string | png     | Image format. Valid values: `png`<br>(lossless), `jpeg` (lossy, smaller<br>files), `random` (randomly selects PNG or JPEG<br>per image). |

**Variable-size images**

Use standard deviation parameters to generate images with varying dimensions,
simulating real-world workloads where image sizes differ:

```

workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "image_width_mean": 800,
        "image_width_stddev": 200,
        "image_height_mean": 600,
        "image_height_stddev": 150,
        "image_batch_size": 2,
        "concurrency": 4,
        "request_count": 50,
        "streaming": True,
        "tokenizer": "meta-llama/Llama-3.2-1B"
    }
}

```

## Benchmark multimodal endpoints with synthetic video

You can benchmark multimodal models that process video inputs by generating
synthetic videos as part of the workload configuration. The benchmarking service
uses AIPerf's synthetic video generation to create videos with configurable
resolution, frame rate, duration, and encoding, then sends them as base64-encoded
payloads to your endpoint.

###### Note

Video generation is disabled by default. You must specify both
`video_width` and `video_height` in your workload
configuration to enable it.

The following example creates a workload configuration for benchmarking a
multimodal model with synthetic video at 640×480 resolution:

```

import json

workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "video_width": 640,
        "video_height": 480,
        "video_fps": 4,
        "video_duration": 5.0,
        "output_tokens_mean": 150,
        "concurrency": 4,
        "request_count": 50,
        "streaming": True,
        "tokenizer": "meta-llama/Llama-3.2-1B"
    },
    "secrets": {
        "hf_token": "arn:aws:secretsmanager:us-west-2:111122223333:secret:my-hf-token-AbCdEf"
    }
}

client.create_ai_workload_config(
    AIWorkloadConfigName="video-benchmark-config",
    WorkloadSpec={"Inline": json.dumps(workload_spec)}
)

```

### Video parameters

The following parameters control synthetic video generation:

| Parameter          | Type   | Default       | Description                                                                                                                                                    |
| ------------------ | ------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `video_width`      | int    | None          | Frame width in pixels. Must be set with<br>`video_height` to enable video generation.                                                                          |
| `video_height`     | int    | None          | Frame height in pixels. Must be set with<br>`video_width` to enable video generation.                                                                          |
| `video_fps`        | int    | 4             | Frames per second.                                                                                                                                             |
| `video_duration`   | float  | 5.0           | Clip duration in seconds.                                                                                                                                      |
| `video_batch_size` | int    | 1             | Number of videos per request.                                                                                                                                  |
| `video_synth_type` | string | moving_shapes | Synthesis pattern. Valid values:<br>`moving_shapes` (animated geometric shapes),<br>`grid_clock` (grid with clock animation),<br>`noise` (random pixel noise). |
| `video_format`     | string | webm          | Container format. Valid value: `webm`.                                                                                                                         |
| `video_codec`      | string | libvpx-vp9    | Video codec. Supported value:<br>`libvpx-vp9` (VP9, WebM).                                                                                                     |

###### Note

The benchmarking service supports VP9 encoding with WebM format
only.

### Embedded audio tracks

For models that process video and audio together, you can embed a synthetic
audio track in the generated videos. Audio is disabled by default. Set
`video_audio_num_channels` to `1` (mono) or
`2` (stereo) to enable it.

| Parameter                  | Type   | Default | Description                                                                                                                        |
| -------------------------- | ------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `video_audio_num_channels` | int    | 0       | 0 = disabled, 1 = mono, 2 = stereo.                                                                                                |
| `video_audio_sample_rate`  | int    | 44100   | Sample rate in Hz (8000–96000).                                                                                                    |
| `video_audio_codec`        | string | auto    | Audio codec. Auto-selects `libvorbis` for WebM<br>and `aac` for MP4. You can override with<br>`aac`, `libvorbis`, or<br>`libopus`. |
| `video_audio_depth`        | int    | 16      | Bit depth per sample (8, 16, 24, or 32).                                                                                           |

### Video benchmarking examples

**Low-resolution video understanding**

```

workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "video_width": 320,
        "video_height": 240,
        "video_fps": 2,
        "video_duration": 3.0,
        "video_synth_type": "moving_shapes",
        "concurrency": 4,
        "request_count": 50,
        "streaming": True,
        "tokenizer": "meta-llama/Llama-3.2-1B"
    }
}

```

**HD video benchmarking**

```

workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "video_width": 1920,
        "video_height": 1080,
        "video_fps": 8,
        "video_duration": 10.0,
        "concurrency": 2,
        "request_count": 20,
        "streaming": True,
        "tokenizer": "meta-llama/Llama-3.2-1B"
    }
}

```

**Video with audio for multimodal models**

```

workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "video_width": 640,
        "video_height": 480,
        "video_fps": 4,
        "video_duration": 5.0,
        "video_audio_num_channels": 1,
        "video_audio_sample_rate": 16000,
        "concurrency": 4,
        "request_count": 50,
        "streaming": True,
        "tokenizer": "meta-llama/Llama-3.2-1B"
    }
}

```

**Mixed text and video**

Combine video with text prompts for video question-answering or captioning
workloads:

```

workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "video_width": 640,
        "video_height": 480,
        "video_fps": 4,
        "video_duration": 5.0,
        "prompt_input_tokens_mean": 100,
        "output_tokens_mean": 50,
        "concurrency": 8,
        "request_count": 100,
        "streaming": True,
        "tokenizer": "meta-llama/Llama-3.2-1B"
    }
}

```

### Performance considerations

- Higher resolution and frame rates increase video encoding time and
  payload size. For high-throughput testing, use lower resolutions
  (320×240 or 640×480).
- VP9 (`libvpx-vp9`) with WebM format is the only
  supported codec and provides good compression for benchmarking
  payloads.
- Audio adds minimal overhead compared to the video stream. Use mono
  (`1`) at 16 kHz for speech-focused workloads.

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

## Benchmark custom-format endpoints

If your endpoint uses a custom request or response format (for example, DJL
custom handlers, TensorRT-LLM native format, or other serving frameworks that
don't support the OpenAI chat completions API), you can benchmark it using a
Jinja2 template to define your endpoint's payload shape.

The benchmarking service renders the template per-request with synthetic or
custom prompts, then forwards the payload to your SageMaker AI endpoint. You also specify
a JMESPath query to extract the generated text from your endpoint's response.

### Create the payload template

Define your endpoint's request format as a Jinja2 template file. The
following variables are available in the template:

| Variable     | Description                                     |
| ------------ | ----------------------------------------------- |
| `text`       | First text content (synthetic or from dataset). |
| `texts`      | List of all text contents.                      |
| `model`      | Model name.                                     |
| `max_tokens` | Output token limit.                             |
| `stream`     | Whether streaming is enabled.                   |

Use the `|tojson` filter for proper JSON escaping of string
values. The following example shows a template for a DJL endpoint with
tool-calling format:

```
{
  "messages": [{"role": "user", "content": {{ text|tojson }}}],
  "tools": [
    {"function": {"name": "Chit_Chat", "description": "casual conversation",
      "parameters": {"type": "object", "properties": {}}}}
  ],
  "max_tokens": {{ max_tokens }}
}
```

Upload the template file to Amazon S3 (for example,
`s3://DOC-EXAMPLE-BUCKET/templates/my_endpoint_template.jinja`).

### Create the workload configuration

Create a workload configuration that references the template file. Use the
`extra_inputs` parameter to specify the template path and the
response extraction query. Deliver the template file to the benchmark
container through a `DatasetConfig` channel.

```

import json

TEMPLATE_LOCAL_PATH = "/opt/ml/input/data/template/my_endpoint_template.jinja"
RESPONSE_FIELD = "generation_details.generations[0].content"

workload_spec = {
    "benchmark": {"type": "aiperf"},
    "parameters": {
        "extra_inputs": f"payload_template:{TEMPLATE_LOCAL_PATH} response_field:{RESPONSE_FIELD}",
        "tokenizer": "meta-llama/Llama-3.2-1B",
        # ... other benchmark parameters (concurrency, request_count, etc.)
    },
}

response = client.create_ai_workload_config(
    AIWorkloadConfigName="custom-format-config",
    AIWorkloadConfigs={"WorkloadSpec": {"Inline": json.dumps(workload_spec)}},
    DatasetConfig={
        "InputDataConfig": [
            {
                "ChannelName": "template",
                "DataSource": {
                    "S3DataSource": {
                        "S3Uri": "s3://DOC-EXAMPLE-BUCKET/templates/my_endpoint_template.jinja",
                    }
                },
            }
        ]
    },
)

```

The `ChannelName` determines where the file appears inside the
benchmark container. A channel named `template` makes the file
available at `/opt/ml/input/data/template/<filename>`.

The `response_field` value is a
[JMESPath](https://jmespath.org/ "https://jmespath.org/") query that extracts the
generated text from your endpoint's response. Common patterns include:

- `choices[0].message.content` — OpenAI format
- `generation_details.generations[0].content` — DJL
  format
- `output.text` — simple text response

If you omit `response_field`, the benchmarking tool
auto-detects the response format.

### Run the benchmark

Create a benchmark job targeting your endpoint. The service automatically
detects template mode from the `payload_template` key in
`extra_inputs` and routes requests through the appropriate proxy
path.

```

response = client.create_ai_benchmark_job(
    AIBenchmarkJobName="custom-format-benchmark",
    BenchmarkTarget={"Endpoint": {"Identifier": "my-custom-endpoint"}},
    OutputConfig={"S3OutputLocation": "s3://DOC-EXAMPLE-BUCKET/results/"},
    AIWorkloadConfigIdentifier="custom-format-config",
    RoleArn="arn:aws:iam::111122223333:role/ExampleRole",
)

```

### Considerations

- Templates must be delivered as files through Amazon S3. Inline JSON
  templates in the `extra_inputs` string are not supported
  because commas in JSON conflict with the parameter parser.
- Endpoints with a single inference component are supported. Endpoints
  with multiple inference components are not supported in template mode
  because the service cannot determine which component to route each
  request to from an arbitrary payload format.
- Both streaming and non-streaming endpoints are supported. Set
  `"streaming": true` or `"streaming": false` in
  the workload parameters.

## Correlate benchmark prompts and responses

After a benchmark job completes, the output artifacts include per-request
input and output data that you can join together for post-processing. This
enables use cases such as quality evaluation, safety auditing, response
comparison across configurations, and debugging unexpected model behavior.

### Benchmark output artifacts

The `output.tar.gz` archive in your Amazon S3 output location
contains the following files relevant to prompt-response correlation:

`inputs.json`

The full synthetic dataset of generated conversations. Each
record has a `session_id` and the complete request
payload (messages, max_tokens, model).

`outputs.json`

Per-request response metadata for requests that were sent to
the endpoint. Each record includes the model's response text,
per-request latency, output token count, and a
`conversation_id` that maps back to the input.

### Join inputs to outputs

Correlate prompts with their responses using the
`conversation_id` field in `outputs.json` and the
`session_id` field in `inputs.json`:

```

import json

# Load the artifacts extracted from output.tar.gz in your S3 output location
with open("inputs.json") as f:
    inputs = json.load(f)
with open("outputs.json") as f:
    outputs = json.load(f)

# Build lookup tables and join
inputs_by_id = {rec["session_id"]: rec for rec in inputs["data"]}
outputs_by_id = {rec["conversation_id"]: rec for rec in outputs["data"]}

matched_ids = set(inputs_by_id.keys()) & set(outputs_by_id.keys())
print(f"Matched: {len(matched_ids)} prompt-response pairs")

# Display a correlated sample
for sid in sorted(matched_ids)[:3]:
    in_rec = inputs_by_id[sid]
    out_rec = outputs_by_id[sid]
    prompt = in_rec["payloads"][0]["messages"][0]["content"][:100]
    response = out_rec.get("response_text", "")[:100]
    latency = out_rec["metrics"]["request_latency"]
    print(f"\n[{sid}] Latency: {latency:.0f}ms")
    print(f"  Prompt:   {prompt}...")
    print(f"  Response: {response}...")

```

### Important notes

- **Join key.** Use
  `conversation_id` in `outputs.json` to match
  against `session_id` in `inputs.json`. Do not
  use `session_num` as a positional index — it represents
  execution order, which differs from input creation order when
  concurrency is greater than 1.
- **Not all inputs have outputs.** The
  `inputs.json` file contains the full generated dataset
  pool. When `request_count` is less than the pool size, only
  a subset of conversations are sent to the endpoint. The unmatched
  inputs are conversations that were generated but not used.
- **Output schema.** Each record in
  `outputs.json` includes `conversation_id`,
  `response_text`, `metrics` (with
  `request_latency` and
  `output_sequence_length`), and timing fields
  (`request_start_ns`,
  `request_end_ns`).

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
