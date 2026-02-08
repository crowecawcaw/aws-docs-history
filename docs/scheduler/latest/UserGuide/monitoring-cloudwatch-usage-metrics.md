# EventBridge Scheduler usage metrics

CloudWatch collects metrics that track the usage of some AWS resources.
These metrics correspond to AWS service quotas.
Tracking these metrics can help you proactively manage your quotas. For more information
about service quotas, see [Quotas for Amazon EventBridge Scheduler](scheduler-quotas.md "scheduler-quotas.md").

These metrics are contained in the `AWS/Usage` namespace, rather than `AWS/Scheduler`, and are collected every minute.
CloudWatch publishes metrics in this namespace with the dimensions
`Service`, `Class`, `Type`, and `Resource`.

| Common dimensions for usage metrics | Dimension                                                                                                                                                        | Description |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `Service`                           | The name of the AWS service containing the resource. For EventBridge Scheduler usage metrics, the value is `Scheduler`.                                          |
| `Class`                             | The class of resource being tracked. For EventBridge Scheduler usage metrics, the value is `None`.                                                               |
| `Type`                              | The type of resource being tracked. For API usage metrics, the value is `API`. For resource count metrics, the value is `Resource`.                              |
| `Resource`                          | The specific resource being tracked. For API usage metrics, this is the API operation name. For resource count metrics, this is the resource type being counted. |

## API usage metrics

API usage metrics track the number of API operations performed in your account. Use these metrics to monitor API call volume and manage your API rate quotas.

The metric name is `CallCount`. The most useful statistic for this metric is `SUM`, which represents the total operation count for the 1-minute period.

| API usage metrics | Metric                | Resource                                                                      | Description |
| ----------------- | --------------------- | ----------------------------------------------------------------------------- | ----------- |
| `CallCount`       | `CreateSchedule`      | The number of `CreateSchedule` API operations performed in your account.      |
| `CallCount`       | `CreateScheduleGroup` | The number of `CreateScheduleGroup` API operations performed in your account. |
| `CallCount`       | `DeleteSchedule`      | The number of `DeleteSchedule` API operations performed in your account.      |
| `CallCount`       | `DeleteScheduleGroup` | The number of `DeleteScheduleGroup` API operations performed in your account. |
| `CallCount`       | `GetSchedule`         | The number of `GetSchedule` API operations performed in your account.         |
| `CallCount`       | `GetScheduleGroup`    | The number of `GetScheduleGroup` API operations performed in your account.    |
| `CallCount`       | `ListScheduleGroups`  | The number of `ListScheduleGroups` API operations performed in your account.  |
| `CallCount`       | `ListSchedules`       | The number of `ListSchedules` API operations performed in your account.       |
| `CallCount`       | `ListTagsForResource` | The number of `ListTagsForResource` API operations performed in your account. |
| `CallCount`       | `TagResource`         | The number of `TagResource` API operations performed in your account.         |
| `CallCount`       | `UntagResource`       | The number of `UntagResource` API operations performed in your account.       |
| `CallCount`       | `UpdateSchedule`      | The number of `UpdateSchedule` API operations performed in your account.      |

For example, the `CallCount` metric with the following dimensions indicates the number of times the
`CreateSchedule` API operation has been called in your account:

- "Service": "Scheduler"
- "Class": "None"
- "Type": "API"
- "Resource": "CreateSchedule"

## Resource count metrics

Resource count metrics track the approximate number of resources in your account. Use these metrics to monitor when you are approaching your service quota limits, allowing you to request quota increases before running out of capacity.

The metric name is `ResourceCount`. The most useful statistic for this metric is `Maximum`.

| Resource count metrics | Metric                     | Resource                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ---------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `ResourceCount`        | `ApproximateSchedule`      | Approximate number of schedules in your account. Use this metric to monitor when you are approaching your schedules quota limit,<br>to help you avoid `ServiceQuotaExceededException` errors when calling `CreateSchedule`.<br>When the number of schedules is less than 1 million, this metric may show zero.<br>For an alarm to notify when nearing your schedules quota, we recommend using the `Maximum` statistic with a threshold of 5 million or higher, since the default schedules quota is 10 million. |
| `ResourceCount`        | `ApproximateScheduleGroup` | Approximate number of schedule groups in your account. Use this metric to monitor when you are approaching your schedule groups quota limit,<br>to help you avoid `ServiceQuotaExceededException` errors when calling `CreateScheduleGroup`.                                                                                                                                                                                                                                                                     |

For example, the `ResourceCount` metric with the following dimensions and the `Maximum` statistic indicates the approximate number of schedules in your account:

- "Service": "Scheduler"
- "Class": "None"
- "Type": "Resource"
- "Resource": "ApproximateSchedule"
