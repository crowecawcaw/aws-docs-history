# WorkSpaces Applications Metrics and Dimensions

Amazon WorkSpaces Applications sends the following metrics and dimension information to Amazon CloudWatch.

All of the following metrics except `InsufficientConcurrencyLimitError`
apply to Always-On and On-Demand fleets. The only metrics that apply to Elastic fleets
are `InUseCapacity` and `InsufficientCapacityError`.

WorkSpaces Applications sends metrics to CloudWatch one time every minute. The `AWS/AppStream`
namespace includes the following metrics.

###### Topics

- [Fleet Usage Metrics for Single-session Fleets](appstream-dimensions.md "appstream-dimensions.md")
- [Fleet Usage Metrics for Multi-session Fleets](usage-metrics-multi-session.md "usage-metrics-multi-session.md")
- [Instance and Session Performance Metrics for Multi-session Fleets](instance-session-metrics-multi-session.md "instance-session-metrics-multi-session.md")
- [Dimensions for Amazon WorkSpaces Applications Metrics](dimensions-metrics.md "dimensions-metrics.md")
