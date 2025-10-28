# EventBridge Scheduler usage metrics

CloudWatch collects metrics that track the usage of some AWS resources.
These metrics correspond to AWS service quotas.
Tracking these metrics can help you proactively manage your quotas. Use the following metrics to determine when you have exceeded your EventBridge Scheduler quotas. For more information
about service quotas, see [Quotas for Amazon EventBridge Scheduler](scheduler-quotas.md "scheduler-quotas.md").

These metrics are contained in the `AWS/Usage` namespace, rather than `AWS/Scheduler`, and are collected every minute.

Currently, the only metric name in this namespace that CloudWatch publishes
is `CallCount`. This metric is published with the dimensions
`Resource`, `Service`, and `Type`. The
`Resource` dimension specifies the name of the API operation being
tracked.

For example, the `CallCount` metric with the following dimensions indicates the number of times the
EventBridge Scheduler `CreateSchedule` API operation has been called in your account:

- "Service": "Scheduler"
- "Type": "API"
- "Resource": "CreateSchedule"
  The `CallCount` metric does not have a specified unit. The most useful statistic for the metric is `SUM`, which represents the total operation count for the 1-minute period.

## Metrics

| Metric      | Description                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `CallCount` | The number of specified operations performed in your account.                                                                                                                                                                                                                                                                                                       | ## Dimensions |
| Dimension   | Description                                                                                                                                                                                                                                                                                                                                                         |
| ---         | ---                                                                                                                                                                                                                                                                                                                                                                 |
| `Service`   | The name of the AWS service containing the resource. For EventBridge Scheduler usage metrics, the value for this dimension is `Scheduler`.                                                                                                                                                                                                                          |
| `Class`     | The class of resource being tracked. EventBridge Scheduler API usage metrics use this dimension with a value of `None`.                                                                                                                                                                                                                                             |
| `Type`      | The type of resource being tracked. Currently, when the `Service` dimension is `Scheduler`, the only valid value for `Type` is `API`.                                                                                                                                                                                                                               |
| `Resource`  | The name of the API operation. Valid values include the following: <br>• `CreateSchedule` <br>• `CreateScheduleGroup` <br>• `DeleteSchedule` <br>• `DeleteScheduleGroup` <br>• `GetSchedule` <br>• `GetScheduleGroup` <br>• `ListScheduleGroups` <br>• `ListSchedules` <br>• `ListTagsForResource` <br>• `TagResource` <br>• `UntagResource` <br>• `UpdateSchedule` |
