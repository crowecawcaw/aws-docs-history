# SageMaker AI Insights OpenTelemetry metrics reference

This section provides a comprehensive list of OpenTelemetry metrics emitted by SageMaker AI detailed
observability. Detailed observability is built on OpenTelemetry (OTel) and collects fine‐grained
operational metrics from the GPU, node, and inference framework layers, publishing them to CloudWatch with
rich labels.

###### Note

Detailed observability publishes OpenTelemetry (OTel) metrics to CloudWatch through OTLP. These are not
Prometheus metrics. The metrics are natively stored in CloudWatch as OTel metric data and are queryable
using PromQL syntax.

## Account-level aggregate metrics

| Metric           | Type      | Description                                             |
| ---------------- | --------- | ------------------------------------------------------- |
| `TotalEndpoints` | Aggregate | Count of all endpoints in the account                   |
| `TotalICs`       | Aggregate | Count of all inference components                       |
| `TotalGPUs`      | Aggregate | Count of all GPUs (derived from `DCGM_FI_DEV_GPU_UTIL`) |

## Endpoint-level metrics

| Metric                     | Type      | Description                        |
| -------------------------- | --------- | ---------------------------------- |
| `InstanceCountPerEndpoint` | Aggregate | Instance count serving traffic     |
| `InstancesPerAZ`           | Aggregate | Instances per availability zone    |
| `EmptyInstanceCount`       | Aggregate | Instances with no ICs placed       |
| `ScalingAction`            | Raw       | Scaling event (in/out)             |
| `ICECount`                 | Raw       | Insufficient Capacity Error count  |
| `CPUUtilization` (EP)      | Aggregate | Endpoint-level CPU utilization     |
| `MemoryUtilization` (EP)   | Aggregate | Endpoint-level memory utilization  |
| `DiskUtilization` (EP)     | Aggregate | Endpoint-level disk utilization    |
| `E2EScalingLatency`        | Raw       | End-to-end scaling duration        |
| `RebalancingType`          | Raw       | Type of rebalancing event          |
| `RebalancingDuration`      | Raw       | Rebalancing duration (seconds)     |
| `RebalancingCopiesMoved`   | Raw       | IC copies moved during rebalancing |
| `AZSkewDelta`              | Raw       | AZ distribution imbalance          |
| `InstancesReleased`        | Raw       | Instances freed by rebalancing     |

## Inference framework metrics (vLLM / SGLang)

| Metric                   | Type      | Description                     |
| ------------------------ | --------- | ------------------------------- |
| `InputTokensPerSecond`   | Aggregate | Input token rate                |
| `OutputTokensPerSecond`  | Aggregate | Output token rate               |
| `TotalTPS`               | Aggregate | Total tokens per second         |
| `TPSUtilization`         | Aggregate | TPS utilization percentage      |
| `TTFT`                   | Raw       | Time to First Token (histogram) |
| `InterTokenLatency`      | Raw       | Inter-Token Latency (histogram) |
| `KVCacheUtilization`     | Raw       | KV cache usage percentage       |
| `QueueDepth`             | Raw       | Waiting requests (queue)        |
| `BatchSize`              | Raw       | Running requests (in-flight)    |
| `TPSPerInstance`         | Aggregate | TPS aggregated per instance     |
| `ConcurrentReqsPerCopy`  | Raw       | Per-copy in-flight requests     |
| `FirstChunkLatencyPerIC` | Raw       | TTFT per IC                     |
| `4XXErrorRatePerIC`      | Aggregate | Client errors per IC            |
| `5XXErrorRatePerIC`      | Aggregate | Server errors per IC            |
| `TTFTPerIC`              | Raw       | TTFT filtered by IC             |
| `ITLPerIC`               | Raw       | ITL filtered by IC              |
| `InputTPSPerIC`          | Aggregate | Input TPS per IC                |
| `OutputTPSPerIC`         | Aggregate | Output TPS per IC               |
| `KVCachePerIC`           | Raw       | KV cache per IC                 |
| `ModelErrorBreakdown`    | Aggregate | Error breakdown by type         |

###### Note

`TTFT` and `InterTokenLatency` are framework‐dependent and only
supported for vLLM and SGLang.

## GPU (DCGM) metrics

These metrics are collected from the NVIDIA Data Center GPU Manager (DCGM) exporter. They are
available on all GPU endpoints regardless of inference framework.

| Metric                      | Type | Description                         |
| --------------------------- | ---- | ----------------------------------- |
| `DCGM_FI_DEV_GPU_UTIL`      | Raw  | GPU utilization (%)                 |
| `DCGM_FI_DEV_MEM_COPY_UTIL` | Raw  | Memory copy utilization (%)         |
| `DCGM_FI_DEV_GPU_TEMP`      | Raw  | GPU temperature (°C)                |
| `DCGM_FI_DEV_MEMORY_TEMP`   | Raw  | Memory temperature (°C)             |
| `DCGM_FI_DEV_FB_FREE`       | Raw  | Framebuffer memory free (bytes)     |
| `DCGM_FI_DEV_FB_USED`       | Raw  | Framebuffer memory used (bytes)     |
| `DCGM_FI_DEV_SM_ACTIVE`     | Raw  | Streaming multiprocessor active (%) |

## Node (instance) metrics

These metrics are collected from the node exporter. They provide instance‐level visibility
into CPU, memory, and disk utilization.

| Metric                           | Type | Description                          |
| -------------------------------- | ---- | ------------------------------------ |
| `node_cpu_seconds_total`         | Raw  | CPU time per mode per core (seconds) |
| `node_memory_MemTotal_bytes`     | Raw  | Total memory (bytes)                 |
| `node_memory_MemAvailable_bytes` | Raw  | Available memory (bytes)             |
| `node_filesystem_size_bytes`     | Raw  | Filesystem total size (bytes)        |
| `node_filesystem_avail_bytes`    | Raw  | Filesystem available space (bytes)   |

## HA and IC placement metrics

| Metric                | Type      | Description                         |
| --------------------- | --------- | ----------------------------------- |
| `ICCopyCountPerAZ`    | Aggregate | IC copies per AZ                    |
| `ICCopiesPerAZ`       | Aggregate | IC copies per AZ (alternative view) |
| `AZSkewScore`         | Aggregate | AZ imbalance score                  |
| `AZBalanceScore`      | Aggregate | Endpoint-level balance              |
| `ICDensityPerAZ`      | Aggregate | IC density per AZ                   |
| `ICCopiesPerInstance` | Aggregate | IC copies per instance              |
| `ICListPerInstance`   | Aggregate | Which ICs on which instance         |

## Lifecycle and provisioning metrics

| Metric                   | Type | Description                              |
| ------------------------ | ---- | ---------------------------------------- |
| `ModelDownloadTime`      | Raw  | Time for Amazon S3 to instance download  |
| `GPULoadTime`            | Raw  | Time for weights to GPU memory           |
| `ContainerStartDuration` | Raw  | Container start to health check          |
| `ColdStartDuration`      | Raw  | End-to-end: creation to first invocation |

## Metrics available only as CloudWatch classic metrics

The following metrics are available only as CloudWatch classic metrics (namespace and dimension model)
and require OTel enrichment to appear as OpenTelemetry metrics.

| Metric                 | Notes                                                                  |
| ---------------------- | ---------------------------------------------------------------------- |
| `InvocationsPerIC`     | Blocked from direct OpenTelemetry emission                             |
| `InvocationsPerCopy`   | Blocked                                                                |
| `ModelLatencyPerIC`    | Blocked—use `vllm:e2e_request_latency_seconds` as the OTel alternative |
| `OverheadLatencyPerIC` | Blocked                                                                |
| `MidStreamErrorsPerIC` | Blocked (bidirectional streaming only)                                 |
