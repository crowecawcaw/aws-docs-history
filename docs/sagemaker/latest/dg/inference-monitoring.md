# OpenTelemetry metrics reference

This section provides a comprehensive list (non-exhaustive) of OpenTelemetry metrics emitted by
Amazon SageMaker AI detailed observability and available in SageMaker AI Insights.

## OpenTelemetry metric labels

OpenTelemetry metrics include labels (attributes) that identify the resource
associated with each data point. Use these labels to filter and group metrics
in queries.

| OpenTelemetry label                      | Description              |
| ---------------------------------------- | ------------------------ |
| `aws.sagemaker.endpoint.name`            | Endpoint name            |
| `aws.sagemaker.variant.name`             | Production variant name  |
| `aws.sagemaker.inference_component.name` | Inference component name |
| `@resource.host.id`                      | EC2 instance ID          |
| `aws.sagemaker.container.id`             | Container ID             |
| `@resource.cloud.availability_zone`      | Availability zone        |
| `@resource.host.type`                    | Instance type            |

## Account-level aggregate metrics

These metrics are at the account level.

| #   | Metric             | Description                                                        |
| --- | ------------------ | ------------------------------------------------------------------ |
| 1   | `TotalEndpoints`   | Total number of active endpoints in the account                    |
| 2   | `TotalICs`         | Total number of inference components deployed across all endpoints |
| 3   | `TotalInvocations` | Total number of inference requests across all endpoints            |

## GPU (DCGM) metrics

These metrics are collected from the Data Center GPU Manager (DCGM) exporter
and are available on all GPU endpoints regardless of inference framework.

Can be aggregated at the inference component, instance, or endpoint level.

| #   | Metric                     | Source metric(s)            | Description                                                                             |
| --- | -------------------------- | --------------------------- | --------------------------------------------------------------------------------------- |
| 4   | GPU utilization (%)        | `DCGM_FI_DEV_GPU_UTIL`      | Percentage of time the GPU was actively executing workloads                             |
| 5   | GPU memory utilization (%) | `DCGM_FI_DEV_MEM_COPY_UTIL` | Percentage of time the memory controller was actively moving data to or from GPU memory |

## Node (instance) metrics

These metrics are collected from the node exporter and provide instance-level
visibility into CPU, memory, and disk utilization.

Can be aggregated at the instance or endpoint level.

| #   | Metric                 | Source metric(s)                                                  | Description                                                                                                                                                                         |
| --- | ---------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 6   | CPU utilization (%)    | `node_cpu_seconds_total`                                          | A cumulative counter measuring total CPU seconds spent in each<br>execution mode (idle, user, system, iowait) since boot. Derive<br>utilization percentage from the idle mode rate. |
| 7   | Memory utilization (%) | `node_memory_MemAvailable_bytes`,<br>`node_memory_MemTotal_bytes` | Percentage of physical memory in use. Derived from total memory<br>minus available memory.                                                                                          |
| 8   | Disk utilization (%)   | `node_filesystem_avail_bytes`,<br>`node_filesystem_size_bytes`    | Percentage of filesystem space in use. Derived from total size<br>minus available space.                                                                                            |

## Inference framework metrics (vLLM / SGLang)

Inference framework metrics are emitted natively by the serving engine running inside
your model container. SageMaker AI automatically collects these metrics from supported
frameworks (vLLM and SGLang) when detailed observability is enabled. These metrics
provide visibility into token throughput, latency, KV cache pressure, and request
queuing at the inference component level.

These metrics can be attributed at the endpoint, inference component, or instance
level.

| #   | Metric                   | Source metric(s)                   | Description                                                        |
| --- | ------------------------ | ---------------------------------- | ------------------------------------------------------------------ |
| 9   | Input Tokens Per Second  | `vllm:prompt_tokens_total`         | Total number of prompt tokens processed per second                 |
| 10  | Output Tokens Per Second | `vllm:generation_tokens_total`     | Total number of generated tokens per second                        |
| 11  | Total TPS                | Derived from #9 + #10              | Combined input and output tokens per second                        |
| 12  | TPS Utilization %        | Derived from #11                   | Current token throughput as a percentage of the observed peak      |
| 13  | TTFT                     | `vllm:time_to_first_token_seconds` | Time from request arrival to the first generated token (histogram) |
| 14  | Inter-Token Latency      | `vllm:inter_token_latency_seconds` | Average time between consecutive generated tokens (histogram)      |
| 15  | KV Cache Utilization     | `vllm:gpu_cache_usage_perc`        | Percentage of GPU KV-cache memory currently in use                 |
| 16  | Queue Depth              | `vllm:num_requests_waiting`        | Number of requests waiting in the queue to be processed            |
| 17  | Batch Size               | `vllm:num_requests_running`        | Number of requests currently running (in-flight)                   |
| 18  | Model Latency            | `vllm:e2e_request_latency_seconds` | End-to-end request latency from arrival to final token (histogram) |

###### Note

Metrics prefixed with `vllm:` have equivalent `sglang:`
counterparts for SGLang endpoints.

## Operations-driven metrics

These metrics are event-driven and emitted by your Create, Update, or Scale
operations to an endpoint or inference component. They are not affected by
`MetricPublishFrequencyInSeconds`.

These metrics can be attributed at the endpoint and inference component level.

| #   | Metric                   | Source metric(s)       | Description                                                                                                                                                                                        |
| --- | ------------------------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 19  | Scaling Event            | `e2e_duration`         | Indicates that an auto-scaling or manual scaling action occurred<br>on your endpoint. Filter by label<br>`aws.sagemaker.scaling.direction` (`ScaleOut`<br>or `ScaleIn`) to identify the direction. |
| 20  | E2E Scaling Latency      | `e2e_duration`         | End-to-end scaling duration from trigger to completion (seconds).<br>Filter by label `aws.sagemaker.operation.type` (for<br>example, `UpdateWCEndpoint`).                                          |
| 21  | ICE Count                | `ice_count`            | Number of Insufficient Capacity Error events per AZ per instance type                                                                                                                              |
| 22  | Rebalancing Event Type   | `rebalancing_blocked`  | Type of rebalancing event and its current state                                                                                                                                                    |
| 23  | Rebalancing Duration     | `rebalancing_duration` | Rebalancing duration from start to completion (seconds)                                                                                                                                            |
| 24  | IC Copies Moved          | `ic_copy_moved`        | Number of inference component copies moved during rebalancing                                                                                                                                      |
| 25  | Instances Released       | `instances_released`   | Number of EC2 instances freed by consolidation during rebalancing                                                                                                                                  |
| 26  | Model Download Duration  | `model_download_time`  | Time to download model artifacts from S3 to the instance (seconds)                                                                                                                                 |
| 27  | GPU Load Duration        | `gpu_load_time`        | Time to load model weights into GPU memory (seconds)                                                                                                                                               |
| 28  | Container Start Duration | `container_start_time` | Time from container start to passing health check (seconds)                                                                                                                                        |

## Derived fleet placement metrics

In addition to the metrics listed above, the SageMaker AI Insights dashboard computes
derived metrics from control plane placement data. These are aggregated views visible
on the dashboard and are not individually queryable metric names in Amazon CloudWatch Query
Studio.

Derived fleet placement metrics include:

- Instance count per availability zone
- IC copy count per availability zone
- AZ skew (distribution imbalance percentage across your fleet)
- IC copies per instance

These values are visible on the Reliability tab of the SageMaker AI Insights
dashboard.
