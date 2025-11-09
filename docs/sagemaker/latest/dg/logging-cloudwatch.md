# CloudWatch Logs for Amazon SageMaker AI

To help you debug your compilation jobs, processing jobs, training jobs, endpoints,
transform jobs, notebook instances, and notebook instance lifecycle configurations, anything
an algorithm container, a model container, or a notebook instance lifecycle configuration
sends to `stdout` or `stderr` is also sent to Amazon CloudWatch Logs. In addition to
debugging, you can use these for progress analysis.

By default, log data is stored in CloudWatch Logs indefinitely. However, you can configure how long
to store log data in a log group. For information, see [Change Log Data Retention in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention") in the _Amazon CloudWatch Logs User
Guide_.

**Logs**

The following table lists all of the logs provided by Amazon SageMaker AI.

**Logs**

| Log Group Name                                                                                                                      | Log Stream Name                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `/aws/sagemaker/CompilationJobs`                                                                                                    | `[compilation-job-name]`                                                            |
| `/aws/sagemaker/Endpoints/[EndpointName]`                                                                                           | `[production-variant-name]/[instance-id]`                                           |
| (For Asynchronous Inference endpoints)<br>`[production-variant-name]/[instance-id]/data-log`                                        |
| (For Inference Pipelines)<br>`[production-variant-name]/[instance-id]/[container-name provided in SageMaker AI<br>model]`           |
| `/aws/sagemaker/groundtruth/WorkerActivity`                                                                                         | `aws/sagemaker/groundtruth/worker-activity/[requester-AWS-Id]-[region]/[timestamp]` |
| `/aws/sagemaker/InferenceRecommendationsJobs`                                                                                       | `[inference-recommendations-job-name]/execution`                                    |
| `[inference-recommendations-job-name]/CompilationJob/[compilation-job-name]`                                                        |
| `[inference-recommendations-job-name]/Endpoint/[endpoint-name]`                                                                     |
| `/aws/sagemaker/LabelingJobs`                                                                                                       | `[labeling-job-name]`                                                               |
| `/aws/sagemaker/NotebookInstances`                                                                                                  | `[notebook-instance-name]/[LifecycleConfigHook]`                                    |
| `[notebook-instance-name]/jupyter.log`                                                                                              |
| `/aws/sagemaker/ProcessingJobs`                                                                                                     | `[processing-job-name]/[hostname]-[epoch_timestamp]`                                |
| `/aws/sagemaker/studio`                                                                                                             | `[domain-id]/[user-profile-name]/[app-type]/[app-name]`                             |
| `[domain-id]/domain-shared/rstudioserverpro/default`                                                                                |
| `/aws/sagemaker/TrainingJobs`                                                                                                       | `[training-job-name]/algo-[instance-number-in-cluster]-[epoch_timestamp]`           |
| `/aws/sagemaker/TransformJobs`                                                                                                      | `[transform-job-name]/[instance-id]-[epoch_timestamp]`                              |
| `[transform-job-name]/[instance-id]-[epoch_timestamp]/data-log`                                                                     |
| `[transform-job-name]/[instance-id]-[epoch_timestamp]/[container-name<br>provided in SageMaker AI model] (For Inference Pipelines)` |

###### Note

1. The `/aws/sagemaker/NotebookInstances/[LifecycleConfigHook]` log stream is
   created when you create a notebook instance with a lifecycle configuration. For more
   information, see [Customization of a SageMaker notebook instance
   using an LCC script](notebook-lifecycle-config.md "notebook-lifecycle-config.md").

2. For Inference Pipelines, if you don't provide container names, the platform uses
   \*\*container-1, container-2\*\*, and so on, corresponding to the order provided in the SageMaker AI
   model.

For more information about logging events with CloudWatch logging, see [What is
Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") in the _Amazon CloudWatch User Guide_.
