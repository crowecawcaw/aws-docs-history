# CloudWatch Metrics for Multi-Model

Endpoint Deployments

Amazon SageMaker AI provides metrics for endpoints so you can monitor the cache hit rate, the number
of models loaded and the model wait times for loading, downloading, and uploading at a
multi-model endpoint. Some of the metrics are different for CPU and GPU backed multi-model
endpoints, so the following sections describe the Amazon CloudWatch metrics that you can use for each
type of multi-model endpoint.

For more information about the metrics, see **Multi-Model Endpoint
Model Loading Metrics** and **Multi-Model Endpoint Model
Instance Metrics** in [Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"). Per-model metrics aren't supported.

## CloudWatch metrics for CPU backed

multi-model endpoints

You can monitor the following metrics on CPU backed multi-model endpoints.

The `AWS/SageMaker` namespace includes the following model loading metrics
from calls to [InvokeEndpoint](../APIReference/API_InvokeEndpoint.md "../APIReference/API_InvokeEndpoint.md").

Metrics are available at a 1-minute frequency.

For information about how long CloudWatch metrics are retained for, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API Reference_.

**Multi-Model Endpoint Model Loading Metrics**

| Metric                 | Description                                                                                                                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ModelLoadingWaitTime` | The interval of time that an invocation request has waited for the target<br>model to be downloaded, or loaded, or both in order to perform inference.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                            |
| `ModelUnloadingTime`   | The interval of time that it took to unload the model through the container's<br>`UnloadModel` API call.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                                                          |
| `ModelDownloadingTime` | The interval of time that it took to download the model from Amazon Simple Storage Service<br>(Amazon S3).<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                                                        |
| `ModelLoadingTime`     | The interval of time that it took to load the model through the container's<br>`LoadModel` API call.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                                                              |
| `ModelCacheHit`        | The number of `InvokeEndpoint` requests sent to the multi-model<br>endpoint for which the model was already loaded.<br>The Average statistic shows the ratio of requests for which the model was<br>already loaded.<br>Units: None<br>Valid statistics: Average, Sum, Sample Count |

**Dimensions for Multi-Model Endpoint Model Loading Metrics**

| Dimension                   | Description                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------- |
| `EndpointName, VariantName` | Filters endpoint invocation metrics for a `ProductionVariant` of<br>the specified endpoint and variant. |

The `/aws/sagemaker/Endpoints` namespaces include the following instance
metrics from calls to [InvokeEndpoint](../APIReference/API_InvokeEndpoint.md "../APIReference/API_InvokeEndpoint.md").

Metrics are available at a 1-minute frequency.

For information about how long CloudWatch metrics are retained for, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API Reference_.

**Multi-Model Endpoint Model Instance Metrics**

| Metric              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LoadedModelCount`  | The number of models loaded in the containers of the multi-model endpoint.<br>This metric is emitted per instance.<br>The Average statistic with a period of 1 minute tells you the average number<br>of models loaded per instance.<br>The Sum statistic tells you the total number of models loaded across all<br>instances in the endpoint.<br>The models that this metric tracks are not necessarily unique because a model<br>might be loaded in multiple containers at the endpoint.<br>Units: None<br>Valid statistics: Average, Sum, Min, Max, Sample Count |
| `CPUUtilization`    | The sum of each individual CPU core's utilization. The CPU utilization of each<br>core range is 0–100. For example, if there are four CPUs, the<br>`CPUUtilization` range is 0%–400%.<br>For endpoint variants, the value is the sum of the CPU utilization of the<br>primary and supplementary containers on the instance.<br>Units: Percent                                                                                                                                                                                                                       |
| `MemoryUtilization` | The percentage of memory that is used by the containers on an instance. This<br>value range is 0%–100%.<br>For endpoint variants, the value is the sum of the memory utilization of the<br>primary and supplementary containers on the instance.<br>Units: Percent                                                                                                                                                                                                                                                                                                  |
| `DiskUtilization`   | The percentage of disk space used by the containers on an instance. This value<br>range is 0%–100%.<br>For endpoint variants, the value is the sum of the disk space utilization of<br>the primary and supplementary containers on the instance.<br>Units: Percent                                                                                                                                                                                                                                                                                                  |

## CloudWatch metrics for GPU

multi-model endpoint deployments

You can monitor the following metrics on GPU backed multi-model endpoints.

The `AWS/SageMaker` namespace includes the following model loading metrics
from calls to [InvokeEndpoint](../APIReference/API_InvokeEndpoint.md "../APIReference/API_InvokeEndpoint.md").

Metrics are available at a 1-minute frequency.

For information about how long CloudWatch metrics are retained for, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API Reference_.

**Multi-Model Endpoint Model Loading Metrics**

| Metric                 | Description                                                                                                                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ModelLoadingWaitTime` | The interval of time that an invocation request has waited for the target<br>model to be downloaded, or loaded, or both in order to perform inference.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                            |
| `ModelUnloadingTime`   | The interval of time that it took to unload the model through the container's<br>`UnloadModel` API call.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                                                          |
| `ModelDownloadingTime` | The interval of time that it took to download the model from Amazon Simple Storage Service<br>(Amazon S3).<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                                                        |
| `ModelLoadingTime`     | The interval of time that it took to load the model through the container's<br>`LoadModel` API call.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                                                              |
| `ModelCacheHit`        | The number of `InvokeEndpoint` requests sent to the multi-model<br>endpoint for which the model was already loaded.<br>The Average statistic shows the ratio of requests for which the model was<br>already loaded.<br>Units: None<br>Valid statistics: Average, Sum, Sample Count |

**Dimensions for Multi-Model Endpoint Model Loading Metrics**

| Dimension                   | Description                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------- |
| `EndpointName, VariantName` | Filters endpoint invocation metrics for a `ProductionVariant` of<br>the specified endpoint and variant. |

The `/aws/sagemaker/Endpoints` namespaces include the following instance
metrics from calls to [InvokeEndpoint](../APIReference/API_InvokeEndpoint.md "../APIReference/API_InvokeEndpoint.md").

Metrics are available at a 1-minute frequency.

For information about how long CloudWatch metrics are retained for, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API Reference_.

**Multi-Model Endpoint Model Instance Metrics**

| Metric                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LoadedModelCount`     | The number of models loaded in the containers of the multi-model endpoint.<br>This metric is emitted per instance.<br>The Average statistic with a period of 1 minute tells you the average number<br>of models loaded per instance.<br>The Sum statistic tells you the total number of models loaded across all<br>instances in the endpoint.<br>The models that this metric tracks are not necessarily unique because a model<br>might be loaded in multiple containers at the endpoint.<br>Units: None<br>Valid statistics: Average, Sum, Min, Max, Sample Count |
| `CPUUtilization`       | The sum of each individual CPU core's utilization. The CPU utilization of each<br>core range is 0‐100. For example, if there are four CPUs, the<br>`CPUUtilization` range is 0%–400%.<br>For endpoint variants, the value is the sum of the CPU utilization of the<br>primary and supplementary containers on the instance.<br>Units: Percent                                                                                                                                                                                                                       |
| `MemoryUtilization`    | The percentage of memory that is used by the containers on an instance. This<br>value range is 0%‐100%.<br>For endpoint variants, the value is the sum of the memory utilization of the<br>primary and supplementary containers on the instance.<br>Units: Percent                                                                                                                                                                                                                                                                                                  |
| `GPUUtilization`       | The percentage of GPU units that are used by the containers on an instance.<br>The value can range betweenrange is 0‐100 and is multiplied by the number of<br>GPUs. For example, if there are four GPUs, the `GPUUtilization` range<br>is 0%–400%.<br>For endpoint variants, the value is the sum of the GPU utilization of the<br>primary and supplementary containers on the instance.<br>Units: Percent                                                                                                                                                         |
| `GPUMemoryUtilization` | The percentage of GPU memory used by the containers on an instance. The value<br>range is 0‐100 and is multiplied by the number of GPUs. For example, if there<br>are four GPUs, the `GPUMemoryUtilization` range is 0%‐400%.<br>For endpoint variants, the value is the sum of the GPU memory utilization of<br>the primary and supplementary containers on the instance.<br>Units: Percent                                                                                                                                                                        |
| `DiskUtilization`      | The percentage of disk space used by the containers on an instance. This value<br>range is 0%–100%.<br>For endpoint variants, the value is the sum of the disk space utilization of<br>the primary and supplementary containers on the instance.<br>Units: Percent                                                                                                                                                                                                                                                                                                  |
