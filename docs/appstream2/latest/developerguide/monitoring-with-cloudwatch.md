

# WorkSpaces Applications Metrics and Dimensions

Amazon WorkSpaces Applications sends the following metrics and dimension information to Amazon CloudWatch.

All of the following metrics except `InsufficientConcurrencyLimitError` apply to Always-On and On-Demand fleets. The only metrics that apply to Elastic fleets are `InUseCapacity` and `InsufficientCapacityError`.

WorkSpaces Applications sends fleet usage metrics to CloudWatch one time every minute, and instance and session performance metrics one time every 5 minutes. The `AWS/AppStream` namespace includes the following metrics.

**Topics**
+ [Fleet Usage Metrics for Single-session Fleets](appstream-dimensions.md)
+ [Fleet Usage Metrics for Multi-session Fleets](usage-metrics-multi-session.md)
+ [Instance and Session Performance Metrics for Single-session and Multi-session Fleets](instance-session-metrics-single-session-multi-session.md)
+ [Dimensions for Amazon WorkSpaces Applications Metrics](dimensions-metrics.md)