

# Log Performance Monitor API calls with AWS CloudTrail

Performance Monitor integrates with AWS CloudTrail to log API calls made to the service. CloudTrail captures API calls for Performance Monitor as events, including calls from the console and from code that uses the AWS SDKs or the AWS CLI. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

The following actions are logged as management events:
+ `CreatePerformanceMonitor`
+ `DeletePerformanceMonitor`
+ `GetPerformanceMonitor`
+ `ListPerformanceMonitors`
+ `UpdatePerformanceMonitor`
+ `UpdateScope`
+ `DeleteScope`

The following query actions are logged as data events, which you must turn on explicitly:
+ `StartQueryPerformanceMonitor`
+ `GetQueryStatusPerformanceMonitor`
+ `GetQueryResultsPerformanceMonitor`
+ `StopQueryPerformanceMonitor`

Performance Monitor events use the event source `networkflowmonitor.amazonaws.com`.