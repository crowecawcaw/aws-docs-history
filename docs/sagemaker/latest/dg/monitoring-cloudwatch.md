# Amazon SageMaker AI metrics in Amazon CloudWatch

You can monitor Amazon SageMaker AI using Amazon CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. These statistics are kept for 15 months. With them, you can
access historical information and gain a better perspective on how your web application or
service is performing. However, the Amazon CloudWatch console limits the search to metrics that were
updated in the last 2 weeks. This limitation ensures that the most current jobs are shown in
your namespace.

To graph metrics without using a search, specify its exact name in the source view. You
can also set alarms that watch for certain thresholds, and send notifications or take actions
when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### SageMaker AI Metrics and Dimensions

- [SageMaker AI endpoint metrics](#cloudwatch-metrics-endpoints "#cloudwatch-metrics-endpoints")
- [SageMaker AI endpoint invocation
  metrics](#cloudwatch-metrics-endpoint-invocation "#cloudwatch-metrics-endpoint-invocation")
- [SageMaker AI inference component
  metrics](#cloudwatch-metrics-inference-component "#cloudwatch-metrics-inference-component")
- [SageMaker AI multi-model endpoint
  metrics](#cloudwatch-metrics-multimodel-endpoints "#cloudwatch-metrics-multimodel-endpoints")
- [SageMaker AI job metrics](#cloudwatch-metrics-jobs "#cloudwatch-metrics-jobs")
- [SageMaker Inference Recommender jobs metrics](#cloudwatch-metrics-inference-recommender "#cloudwatch-metrics-inference-recommender")
- [SageMaker Ground Truth metrics](#cloudwatch-metrics-ground-truth "#cloudwatch-metrics-ground-truth")
- [Amazon SageMaker Feature Store metrics](#cloudwatch-metrics-feature-store "#cloudwatch-metrics-feature-store")
- [SageMaker pipelines metrics](#cloudwatch-metrics-pipelines "#cloudwatch-metrics-pipelines")

## SageMaker AI endpoint metrics

The `/aws/sagemaker/Endpoints` namespace includes the following metrics for
endpoint instances.

Metrics are available at a 1-minute frequency.

###### Note

Amazon CloudWatch supports [high-resolution custom
metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md") and its finest resolution is 1 second. However, the finer the
resolution, the shorter the lifespan of the CloudWatch metrics. For the 1-second frequency
resolution, the CloudWatch metrics are available for 3 hours. For more information about the
resolution and the lifespan of the CloudWatch metrics, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API
Reference_.

| Endpoint metrics                 | Metric                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `CPUReservation`                 | The sum of CPUs reserved by containers on an instance.<br>This metric is provided only for endpoints that host active inference components. The value ranges between 0%–100%. In the<br>settings for an inference component, you set the CPU reservation with the<br>`NumberOfCpuCoresRequired` parameter. For example, if there 4 CPUs,<br>and 2 are reserved, the `CPUReservation` metric is 50%.                    |
| `CPUUtilization`                 | The sum of each individual CPU core's utilization. The CPU utilization of each<br>core range is 0–100. For example, if there are four CPUs, the<br>`CPUUtilization` range is 0%–400%.<br>For endpoint variants, the value is the sum of the CPU utilization of the<br>primary and supplementary containers on the instance.<br>Units: Percent                                                                          |
| `CPUUtilizationNormalized`       | The normalized sum of the utilization of each individual CPU core.<br>This metric is provided only for endpoints that host active inference components. The value ranges between 0%–100%. For<br>example, if there are four CPUs, and the `CPUUtilization` metric is<br>200%, then the `CPUUtilizationNormalized` metric is 50%.                                                                                       |
| `DiskUtilization`                | The percentage of disk space used by the containers on an instance.<br>This value range is 0%–100%.For endpoint variants, the value is the sum<br>of the disk space utilization of the primary and supplementary containers on the<br>instance.Units: Percent                                                                                                                                                          |
| `GPUMemoryUtilization`           | The percentage of GPU memory used by the containers on an instance. The<br>value range is 0–100 and is multiplied by the number of GPUs. For example,<br>if there are four GPUs, the `GPUMemoryUtilization` range is<br>0%–400%.<br>For endpoint variants, the value is the sum of the GPU memory utilization of<br>the primary and supplementary containers on the instance.<br>Units: Percent                        |
| `GPUMemoryUtilizationNormalized` | The normalized percentage of GPU memory used by the containers on an<br>instance. This metric is provided only for endpoints that host active inference components. The value ranges between<br>0%–100%. For example, if there are four GPUs, and the<br>`GPUMemoryUtilization` metric is 200%, then the<br>`GPUMemoryUtilizationNormalized` metric is 50%.                                                            |
| `GPUReservation`                 | The sum of GPUs reserved by containers on an instance.<br>This metric is provided only for endpoints that host active inference components. The value ranges between 0%–100%. In the<br>settings for an inference component, you set the GPU reservation by<br>`NumberOfAcceleratorDevicesRequired`. For example, if there are 4<br>GPUs and 2 are reserved, the `GPUReservation` metric is 50%.                       |
| `GPUUtilization`                 | The percentage of GPU units that are used by the containers on an<br>instance. The value can range between 0–100 and is multiplied by the number<br>of GPUs. For example, if there are four GPUs, the `GPUUtilization`<br>range is 0%–400%.<br>For endpoint variants, the value is the sum of the GPU utilization of the<br>primary and supplementary containers on the instance.<br>Units: Percent                    |
| `GPUUtilizationNormalized`       | The normalized percentage of GPU units that are used by the containers on an<br>instance. This metric is provided only for endpoints that host active inference components. The value ranges between<br>0%–100%. For example, if there are four GPUs, and the<br>`GPUUtilization` metric is 200%, then the<br>`GPUUtilizationNormalized` metric is 50%.                                                                |
| `MemoryReservation`              | The sum of memory reserved by containers on an instance.<br>This metric is provided only for endpoints that host active inference components. The value ranges between 0%–100%. In the<br>settings for an inference component, you set the memory reservation with the<br>`MinMemoryRequiredInMb` parameter. For example, if a 32 GiB instance<br>reserved 1024 MB, the `MemoryReservation` metric would be<br>3.125%. |
| `MemoryUtilization`              | The percentage of memory that is used by the containers on an instance.<br>This value range is 0%–100%.<br>For endpoint variants, the value is the sum of the memory utilization of the<br>primary and supplementary containers on the instance.<br>Units: Percent                                                                                                                                                     |

| Dimensions for endpoint metrics | Dimension                                                                                    | Description |
| ------------------------------- | -------------------------------------------------------------------------------------------- | ----------- |
| `EndpointName, VariantName`     | Filters endpoint metrics for a `ProductionVariant` of the specified<br>endpoint and variant. |

## SageMaker AI endpoint invocation

metrics

The `AWS/SageMaker` namespace includes the following request metrics from
calls to [InvokeEndpoint](../APIReference/API_runtime_InvokeEndpoint.md "../APIReference/API_runtime_InvokeEndpoint.md").

Metrics are available at a 1-minute frequency.

The following illustration shows how a SageMaker AI endpoint interacts with the Amazon SageMaker Runtime
API. The overall time between sending a request to an endpoint and receiving a response
depends on the following three components.

- Network latency – the time that it takes between making a request to and
  receiving a response back from the SageMaker Runtime Runtime API.
- Overhead latency – the time that it takes to transport a request to the model
  container from and transport the response back to the SageMaker Runtime Runtime API.
- Model latency – the time that it takes the model container to process the
  request and return a response.

![An illustration showing that total latency is the sum of network, overhead and model latencies.](images/cloudwatch-latency-types.png)

For more information about total latency, see [Best practices for load testing Amazon SageMaker AI real-time inference endpoints](https://aws.amazon.com/blogs/machine-learning/best-practices-for-load-testing-amazon-sagemaker-real-time-inference-endpoints/ "https://aws.amazon.com/blogs/machine-learning/best-practices-for-load-testing-amazon-sagemaker-real-time-inference-endpoints/"). For
information about how long CloudWatch metrics are retained for, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API Reference_.

| Endpoint invocation metrics  | Metric                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `ConcurrentRequestsPerCopy`  | The number of concurrent requests being received by the inference component,<br>normalized by each copy of an inference component.<br>Valid statistics: Min, Max                                                                                                                                                                                                                                                                                                                                                                 |
| `ConcurrentRequestsPerModel` | The number of concurrent requests being received by the model.<br>Valid statistics: Min, Max                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `Invocation4XXErrors`        | The number of `InvokeEndpoint` requests where the model returned a<br>4xx HTTP response code. For each 4xx response, 1 is sent; otherwise, 0 is<br>sent.<br>Units: None<br>Valid statistics: Average, Sum                                                                                                                                                                                                                                                                                                                        |
| `Invocation5XXErrors`        | The number of `InvokeEndpoint` requests where the model returned a<br>5xx HTTP response code. For each 5xx response, 1 is sent; otherwise, 0 is<br>sent.<br>Units: None<br>Valid statistics: Average, Sum                                                                                                                                                                                                                                                                                                                        |
| `InvocationModelErrors`      | The number of model invocation requests that did not result in 2XX HTTP<br>response. This includes 4XX/5XX status codes, low-level socket errors, malformed<br>HTTP responses, and request timeouts. For each error response, 1 is sent;<br>otherwise, 0 is sent.<br>Units: None<br>Valid statistics: Average, Sum                                                                                                                                                                                                               |
| `Invocations`                | The number of `InvokeEndpoint` requests sent to a model endpoint.<br>To get the total number of requests sent to a model endpoint, use the Sum<br>statistic.<br>Units: None<br>Valid statistics: Sum                                                                                                                                                                                                                                                                                                                             |
| `InvocationsPerCopy`         | The number of invocations normalized by each copy of an inference<br>component.<br>Valid statistics: Sum                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `InvocationsPerInstance`     | The number of invocations sent to a model, normalized by<br>`InstanceCount` in each ProductionVariant.<br>1/`numberOfInstances` is sent as the value on each request.<br>`numberOfInstances` is the number of active instances for the<br>ProductionVariant behind the endpoint at the time of the request.<br>Units: None<br>Valid statistics: Sum                                                                                                                                                                              |
| `ModelLatency`               | The interval of time taken by a model to respond to a SageMaker Runtime API request.<br>This interval includes the local communication times taken to send the request and<br>to fetch the response from the model container. It also includes the time taken to<br>complete the inference in the container.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count, Percentiles                                                                                                                       |
| `ModelSetupTime`             | The time it takes to launch new compute resources for a serverless endpoint.<br>The time can vary depending on the model size, how long it takes to download the<br>model, and the start-up time of the container.<br>Units: Microseconds<br>Valid statistics: Average, Min, Max, Sample Count, Percentiles                                                                                                                                                                                                                      |
| `OverheadLatency`            | The interval of time added to the time taken to respond to a client request by<br>SageMaker AI overheads. This interval is measured from the time SageMaker AI receives the request<br>until it returns a response to the client, minus the `ModelLatency`.<br>Overhead latency can vary depending on multiple factors, including request and<br>response payload sizes, request frequency, and authentication/authorization of the<br>request.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count |

| Dimensions for endpoint invocation metrics | Dimension                                                                                               | Description |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------- | ----------- |
| `EndpointName, VariantName`                | Filters endpoint invocation metrics for a `ProductionVariant` of<br>the specified endpoint and variant. |
| `InferenceComponentName`                   | Filters inference component invocation metrics.                                                         |

## SageMaker AI inference component

metrics

The `/aws/sagemaker/InferenceComponents` namespace includes the following
metrics from calls to [InvokeEndpoint](../APIReference/API_runtime_InvokeEndpoint.md "../APIReference/API_runtime_InvokeEndpoint.md") for endpoints that host inference components.

Metrics are available at a 1-minute frequency.

| Inference component metrics      | Metric                                                                                                                                                                                                                                                                                                                                                                            | Description |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `CPUUtilizationNormalized`       | The value of the `CPUUtilizationNormalized` metric reported by each<br>copy of the inference component. The value ranges between 0%–100%. If you<br>set the `NumberOfCpuCoresRequired` parameter in the settings for the<br>inference component copy, the metric presents the utilization over the<br>reservation. Otherwise, the metric presents the utilization over the limit. |
| `GPUMemoryUtilizationNormalized` | The value of the `GPUMemoryUtilizationNormalized` metric reported<br>by each copy of the inference component.                                                                                                                                                                                                                                                                     |
| `GPUUtilizationNormalized`       | The value of the `GPUUtilizationNormalized` metric reported by each<br>copy of the inference component. If you set the<br>`NumberOfAcceleratorDevicesRequired` parameter in the settings for<br>the inference component copy, the metric presents the utilization over the<br>reservation. Otherwise, the metric presents the utilization over the limit.                         |
| `MemoryUtilizationNormalized`    | The value of `MemoryUtilizationNormalized` reported by each copy of<br>the inference component. If you set the `MinMemoryRequiredInMb`<br>parameter in the settings for the inference component copy, the metrics present<br>the utilization over the reservation. Otherwise, the metrics present the<br>utilization over the limit.                                              |

| Dimensions for inference component metrics | Dimension                            | Description |
| ------------------------------------------ | ------------------------------------ | ----------- |
| `InferenceComponentName`                   | Filters inference component metrics. |

## SageMaker AI multi-model endpoint

metrics

The `AWS/SageMaker` namespace includes the following model loading metrics
from calls to [InvokeEndpoint](../APIReference/API_runtime_InvokeEndpoint.md "../APIReference/API_runtime_InvokeEndpoint.md").

Metrics are available at a 1-minute frequency.

For information about how long CloudWatch metrics are retained for, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API Reference_.

| Multi-model endpoint model loading metrics | Metric                                                                                                                                                                                                                                                                             | Description |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `ModelLoadingWaitTime`                     | The interval of time that an invocation request has waited for the target<br>model to be downloaded, loaded, or both in order to run inference.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                   |
| `ModelUnloadingTime`                       | The interval of time that it took to unload the model through the container's<br>`UnloadModel` API call.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                                                          |
| `ModelDownloadingTime`                     | The interval of time that it took to download the model from Amazon Simple Storage Service<br>(Amazon S3).<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                                                        |
| `ModelLoadingTime`                         | The interval of time that it took to load the model through the container's<br>`LoadModel` API call.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count                                                                                              |
| `ModelCacheHit`                            | The number of `InvokeEndpoint` requests sent to the multi-model<br>endpoint for which the model was already loaded.<br>The Average statistic shows the ratio of requests for which the model was<br>already loaded.<br>Units: None<br>Valid statistics: Average, Sum, Sample Count |

| Dimensions for multi-model endpoint model loading metrics | Dimension                                                                                               | Description |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| `EndpointName, VariantName`                               | Filters endpoint invocation metrics for a `ProductionVariant` of<br>the specified endpoint and variant. |

The `/aws/sagemaker/Endpoints` namespaces include the following instance
metrics from calls to [InvokeEndpoint](../APIReference/API_runtime_InvokeEndpoint.md "../APIReference/API_runtime_InvokeEndpoint.md").

Metrics are available at a 1-minute frequency.

For information about how long CloudWatch metrics are retained for, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API Reference_.

| Multi-model endpoint model instance metrics | Metric                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `LoadedModelCount`                          | The number of models loaded in the containers of the multi-model endpoint.<br>This metric is emitted per instance.<br>The Average statistic with a period of 1 minute tells you the average number<br>of models loaded per instance.<br>The Sum statistic tells you the total number of models loaded across all<br>instances in the endpoint.<br>The models that this metric tracks are not necessarily unique because a model<br>might be loaded in multiple containers at the endpoint.<br>Units: None<br>Valid statistics: Average, Sum, Min, Max, Sample Count |

| Dimensions for multi-model endpoint model loading metrics | Dimension                                                                                               | Description |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| `EndpointName, VariantName`                               | Filters endpoint invocation metrics for a `ProductionVariant` of<br>the specified endpoint and variant. |

## SageMaker AI job metrics

The `/aws/sagemaker/ProcessingJobs`,
`/aws/sagemaker/TrainingJobs`, and `/aws/sagemaker/TransformJobs`
namespaces include the following metrics for processing jobs, training jobs, and batch
transform jobs.

Metrics are available at a 1-minute frequency.

###### Note

Amazon CloudWatch supports [high-resolution custom
metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md") and its finest resolution is 1 second. However, the finer the
resolution, the shorter the lifespan of the CloudWatch metrics. For the 1-second frequency
resolution, the CloudWatch metrics are available for 3 hours. For more information about the
resolution and the lifespan of the CloudWatch metrics, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API
Reference_.

###### Tip

To profile your training job with a finer resolution down to 100-millisecond (0.1
second) granularity and store the training metrics indefinitely in Amazon S3 for custom
analysis at any time, consider using [Amazon SageMaker Debugger](train-debugger.md "train-debugger.md"). SageMaker Debugger provides
built-in rules to automatically detect common training issues. It detects hardware
resource utilization issues (such as CPU, GPU, and I/O bottlenecks). It also detects
non-converging model issues (such as overfit, vanishing gradients, and exploding tensors).
SageMaker Debugger also provides visualizations through Studio Classic and its profiling report. To
explore the Debugger visualizations, see [SageMaker Debugger Insights
Dashboard Walkthrough](debugger-on-studio-insights.md "debugger-on-studio-insights.md"), [Debugger Profiling Report
Walkthrough](debugger-report.md "debugger-report.md"), and [Analyze Data Using the SMDebug
Client Library](debugger-analyze-data.md "debugger-analyze-data.md").

| Processing job, training job, and batch transform job metrics | Metric                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `CPUUtilization`                                              | The sum of each individual CPU core's utilization. The CPU utilization of each<br>core range is 0–100. For example, if there are four CPUs, the<br>`CPUUtilization` range is 0%–400%. For processing jobs, the value is the CPU utilization of<br>the processing container on the instance.For training jobs, the value is the<br>CPU utilization of the algorithm container on the instance.For batch<br>transform jobs, the value is the CPU utilization of the transform container on the<br>instance.NoteFor multi-instance jobs, each instance reports CPU utilization metrics.<br>However, the default view in CloudWatch shows the average CPU utilization across all<br>instances.Units: Percent                                                                              |
| `DiskUtilization`                                             | The percentage of disk space used by the containers on an instance.<br>This value range is 0%–100%. This metric is not supported for batch transform<br>jobs.For processing jobs, the value is the disk space utilization of the<br>processing container on the instance.For training jobs, the value is the disk<br>space utilization of the algorithm container on the instance.Units:<br>PercentNoteFor multi-instance jobs, each instance reports disk utilization metrics.<br>However, the default view in CloudWatch shows the average disk utilization across all<br>instances.                                                                                                                                                                                                |
| `GPUMemoryUtilization`                                        | The percentage of GPU memory used by the containers on an instance. The<br>value range is 0–100 and is multiplied by the number of GPUs. For example,<br>if there are four GPUs, the `GPUMemoryUtilization` range is<br>0%–400%.For processing jobs, the value is the<br>GPU memory utilization of the processing container on the instance.For<br>training jobs, the value is the GPU memory utilization of the algorithm container<br>on the instance.For batch transform jobs, the value is the GPU memory<br>utilization of the transform container on the instance.NoteFor multi-instance jobs, each instance reports GPU memory utilization<br>metrics. However, the default view in CloudWatch shows the average GPU memory<br>utilization across all instances.Units: Percent |
| `GPUUtilization`                                              | The percentage of GPU units that are used by the containers on an<br>instance. The value can range between 0–100 and is multiplied by the number<br>of GPUs. For example, if there are four GPUs, the `GPUUtilization`<br>range is 0%–400%.For processing jobs, the value is the GPU<br>utilization of the processing container on the instance.For training jobs, the<br>value is the GPU utilization of the algorithm container on the<br>instance.For batch transform jobs, the value is the GPU utilization<br>of the transform container on the instance.NoteFor multi-instance jobs, each instance reports GPU utilization metrics.<br>However, the default view in CloudWatch shows the average GPU utilization across all<br>instances.Units: Percent                         |
| `MemoryUtilization`                                           | The percentage of memory that is used by the containers on an instance.<br>This value range is 0%–100%.For processing jobs, the value is the<br>memory utilization of the processing container on the instance.For training<br>jobs, the value is the memory utilization of the algorithm container on the<br>instance.For batch transform jobs, the value is the memory<br>utilization of the transform container on the instance.Units:<br>PercentNoteFor multi-instance jobs, each instance reports memory utilization metrics.<br>However, the default view in CloudWatch shows the average memory utilization across<br>all instances.                                                                                                                                           |

| Dimensions for job metrics | Dimension                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `Host`                     | For processing jobs, the value for this dimension has the format<br>`[processing-job-name]/algo-[instance-number-in-cluster]`. Use this<br>dimension to filter instance metrics for the specified processing job and<br>instance. This dimension format is present only in the<br>`/aws/sagemaker/ProcessingJobs` namespace.<br>For training jobs, the value for this dimension has the format<br>`[training-job-name]/algo-[instance-number-in-cluster]`. Use this<br>dimension to filter instance metrics for the specified training job and instance.<br>This dimension format is present only in the<br>`/aws/sagemaker/TrainingJobs` namespace.<br>For batch transform jobs, the value for this dimension has the format<br>`[transform-job-name]/[instance-id]`. Use this dimension to filter<br>instance metrics for the specified batch transform job and instance. This<br>dimension format is present only in the `/aws/sagemaker/TransformJobs`<br>namespace. |

## SageMaker Inference Recommender jobs metrics

The `/aws/sagemaker/InferenceRecommendationsJobs` namespace includes the
following metrics for inference recommendation jobs.

| Inference Recommender metrics | Metric                                                                                                                                                                                                                                                                                                                                                     | Description |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `ClientInvocations`           | The number of `InvokeEndpoint` requests sent to a model endpoint,<br>as observed by Inference Recommender.<br>Units: None<br>Valid statistics: Sum                                                                                                                                                                                                         |
| `ClientInvocationErrors`      | The number of `InvokeEndpoint` requests that failed, as observed by<br>Inference Recommender.<br>Units: None<br>Valid statistics: Sum                                                                                                                                                                                                                      |
| `ClientLatency`               | The interval of time taken between sending an `InvokeEndpoint` call<br>and receiving a response as observed by Inference Recommender. Note that the time is in<br>milliseconds, whereas the `ModelLatency` endpoint invocation metric is<br>in microseconds.<br>Units: Milliseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count, Percentiles |
| `NumberOfUsers`               | The number of concurrent users sending `InvokeEndpoint` requests to<br>the model endpoint.<br>Units: None<br>Valid statistics: Max, Min, Average                                                                                                                                                                                                           |

| Dimensions for Inference Recommender job metrics | Dimension                                                                              | Description |
| ------------------------------------------------ | -------------------------------------------------------------------------------------- | ----------- |
| `JobName`                                        | Filters Inference Recommender job metrics for the specified Inference Recommender job. |
| `EndpointName`                                   | Filters Inference Recommender job metrics for the specified endpoint.                  |

## SageMaker Ground Truth metrics

| Ground Truth metrics           | Metric                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `ActiveWorkers`                | A single active worker on a private work team submitted, released, or declined<br>a task. To get the total number of active workers, use the Sum statistic. Ground Truth<br>tries to deliver each individual `ActiveWorkers` event once. If this<br>delivery is unsuccessful, this metric may not report the total number of active<br>workers.<br>Units: None<br>Valid statistics: Sum, Sample Count |
| `DatasetObjectsAutoAnnotated`  | The number of dataset objects auto-annotated in a labeling job. This metric is<br>only emitted when automated labeling is enabled. To view the labeling job<br>progress, use the Max metric.<br>Units: None<br>Valid statistics: Max                                                                                                                                                                  |
| `DatasetObjectsHumanAnnotated` | The number of dataset objects annotated by a human in a labeling job. To view<br>the labeling job progress, use the Max metric.<br>Units: None<br>Valid statistics: Max                                                                                                                                                                                                                               |
| `DatasetObjectsLabelingFailed` | The number of dataset objects that failed labeling in a labeling job. To view<br>the labeling job progress, use the Max metric.<br>Units: None<br>Valid statistics: Max                                                                                                                                                                                                                               |
| `JobsFailed`                   | A single labeling job failed. To get the total number of labeling jobs that<br>failed, use the Sum statistic.<br>Units: None<br>Valid statistics: Sum, Sample Count                                                                                                                                                                                                                                   |
| `JobsSucceeded`                | A single labeling job succeeded. To get the total number of labeling jobs that<br>succeeded, use the Sum statistic.<br>Units: None<br>Valid statistics: Sum, Sample Count                                                                                                                                                                                                                             |
| `JobsStopped`                  | A single labeling jobs was stopped. To get the total number of labeling jobs<br>that were stopped, use the Sum statistic.<br>Units: None<br>Valid statistics: Sum, Sample Count                                                                                                                                                                                                                       |
| `TasksAccepted`                | A single task was accepted by a worker. To get the total number of tasks<br>accepted by workers, use the Sum statistic. Ground Truth attempts to deliver each<br>individual `TaskAccepted` event once. If this delivery is unsuccessful,<br>this metric may not report the total number of tasks accepted.<br>Units: None<br>Valid statistics: Sum, Sample Count                                      |
| `TasksDeclined`                | A single task was declined by a worker. To get the total number of tasks<br>declined by workers, use the Sum statistic. Ground Truth attempts to deliver each<br>individual `TasksDeclined` event once. If this delivery is<br>unsuccessful, this metric may not report the total number of tasks<br>declined.<br>Units: None<br>Valid Statistics: Sum, Sample Count                                  |
| `TasksReturned`                | A single task was returned. To get the total number of tasks returned, use the<br>Sum statistic. Ground Truth attempts to deliver each individual `TasksReturned`<br>event once. If this delivery is unsuccessful, this metric may not report the total<br>number of tasks returned.<br>Units: None<br>Valid statistics: Sum, Sample Count                                                            |
| `TasksSubmitted`               | A single task was submitted/completed by a private worker. To get the total<br>number of tasks submitted by workers, use the Sum statistic. Ground Truth attempts to<br>deliver each individual `TasksSubmitted` event once. If this delivery<br>is unsuccessful, this metric may not report the total number of tasks<br>submitted.<br>Units: None<br>Valid statistics: Sum, Sample Count            |
| `TimeSpent`                    | Time spent on a task completed by a private worker. This metric does not<br>include time when a worker paused or took a break. Ground Truth attempts to deliver each<br>`TimeSpent` event once. If this delivery is unsuccessful, this metric<br>may not report the total amount of time spent.<br>Units: Seconds<br>Valid statistics: Sum, Sample Count                                              |
| `TotalDatasetObjectsLabeled`   | The number of dataset objects labeled successfully in a labeling job. To view<br>the labeling job progress, use the Max metric.<br>Units: None<br>Valid statistics: Max                                                                                                                                                                                                                               |

| Dimensions for dataset object metrics | Dimension                                                | Description |
| ------------------------------------- | -------------------------------------------------------- | ----------- |
| `LabelingJobName`                     | Filters dataset object count metrics for a labeling job. |

## Amazon SageMaker Feature Store metrics

| Feature Store consumption metrics | Metric                                                                                                                                                                                                                                                              | Description |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `ConsumedReadRequestsUnits`       | The number of consumed read units over the specified time period. You can<br>retrieve the consumed read units for a feature store runtime operation and its<br>corresponding feature group.<br>Units: None<br>Valid statistics: All                                 |
| `ConsumedWriteRequestsUnits`      | The number of consumed write units over the specified time period. You can<br>retrieve the consumed write units for a feature store runtime operation and its<br>corresponding feature group.<br>Units: None<br>Valid statistics: All                               |
| `ConsumedReadCapacityUnits`       | The number of provisioned read capacity units consumed over the specified time<br>period. You can retrieve the consumed read capacity units for a feature store<br>runtime operation and its corresponding feature group.<br>Units: None<br>Valid statistics: All   |
| `ConsumedWriteCapacityUnits`      | The number of provisioned write capacity units consumed over the specified<br>time period. You can retrieve the consumed write capacity units for a feature<br>store runtime operation and its corresponding feature group.<br>Units: None<br>Valid statistics: All |

| Dimensions for Feature Store consumption metrics | Dimension                                                                                                          | Description |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| `FeatureGroupName`, `OperationName`              | Filters feature store runtime consumption metrics of the feature group and the<br>operation that you've specified. |

| Feature Store operational metrics | Metric                                                                                                                                                                                                                                                                                                       | Description |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `Invocations`                     | The number of requests made to the feature store runtime operations over the<br>specified time period.<br>Units: None<br>Valid statistics: Sum                                                                                                                                                               |
| `Operation4XXErrors`              | The number of requests made to the Feature Store runtime operations where the operation<br>returned a 4xx HTTP response code. For each 4xx response, 1 is sent; else, 0 is<br>sent.<br>Units: None<br>Valid statistics: Average, Sum                                                                         |
| `Operation5XXErrors`              | The number of requests made to the feature store runtime operations where the<br>operation returned a 5xx HTTP response code. For each 5xx response, 1 is sent;<br>else, 0 is sent.<br>Units: None<br>Valid statistics: Average, Sum                                                                         |
| `ThrottledRequests`               | The number of requests made to the feature store runtime operations where the<br>request got throttled. For each throttled request, 1 is sent; else, 0 is<br>sent.<br>Units: None<br>Valid statistics: Average, Sum                                                                                          |
| `Latency`                         | The time interval to process requests made to the Feature Store runtime operations.<br>This interval is measured from the time SageMaker AI receives the request until it returns<br>a response to the client.<br>Units: Microseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count, Percentiles |

| Dimensions for Feature Store operational metrics | Dimension                                                                                                                                                                                                                    | Description |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `FeatureGroupName`, `OperationName`              | Filters feature store runtime operational metrics of the feature group and the<br>operation that you've specified. You can use these dimensions for non batch<br>operations, such as GetRecord, PutRecord, and DeleteRecord. |
| `OperationName`                                  | Filters feature store runtime operational metrics for the operation that<br>you've specified. You can use this dimension for batch operations such as<br>BatchGetRecord.                                                     |

## SageMaker pipelines metrics

The `AWS/Sagemaker/ModelBuildingPipeline` namespace includes the following
metrics for pipeline executions.

Two categories of pipeline execution metrics are available:

- **Execution Metrics across All Pipelines** – Account
  level pipeline execution metrics (for all pipelines in the current account)
- **Execution Metrics by Pipeline** – Pipeline
  execution metrics per pipeline

Metrics are available at a 1-minute frequency.

| Pipeline execution metrics | Metric                                                                                                                                         | Description |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `ExecutionStarted`         | The number of pipeline executions that started.<br>Units: Count<br>Valid statistics: Average, Sum                                              |
| `ExecutionFailed`          | The number of pipeline executions that failed.<br>Units: Count<br>Valid statistics: Average, Sum                                               |
| `ExecutionSucceeded`       | The number of pipeline executions that succeeded.<br>Units: Count<br>Valid statistics: Average, Sum                                            |
| `ExecutionStopped`         | The number of pipeline executions that stopped.<br>Units: Count<br>Valid statistics: Average, Sum                                              |
| `ExecutionDuration`        | The duration in milliseconds that the pipeline execution ran.<br>Units: Milliseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count |

| Dimensions for pipeline execution metrics | Dimension                                                    | Description |
| ----------------------------------------- | ------------------------------------------------------------ | ----------- |
| `PipelineName`                            | Filters pipeline execution metrics for a specified pipeline. |

The `AWS/Sagemaker/ModelBuildingPipeline` namespace includes the following
metrics for pipeline steps.

Metrics are available at a 1-minute frequency.

| Pipeline step metrics | Metric                                                                                                                           | Description |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `StepStarted`         | The number of steps that started.<br>Units: Count<br>Valid statistics: Average, Sum                                              |
| `StepFailed`          | The number of steps that failed.<br>Units: Count<br>Valid statistics: Average, Sum                                               |
| `StepSucceeded`       | The number of steps that succeeded.<br>Units: Count<br>Valid statistics: Average, Sum                                            |
| `StepStopped`         | The number of steps that stopped.<br>Units: Count<br>Valid statistics: Average, Sum                                              |
| `StepDuration`        | The duration in milliseconds that the step ran.<br>Units: Milliseconds<br>Valid statistics: Average, Sum, Min, Max, Sample Count |

| Dimensions for pipeline step metrics | Dimension                                               | Description |
| ------------------------------------ | ------------------------------------------------------- | ----------- |
| `PipelineName`, `StepName`           | Filters step metrics for a specified pipeline and step. |
