# Viewing CloudWatch Logs Live Tail for Amazon ECS services and tasks

CloudWatch Logs Live Tail helps you quickly troubleshoot incidents by viewing a streaming list of
new log events as they are ingested. You can view task and service events in the Amazon ECS
console. This view provides a cohesive view of your task and service health.

Each task in an Amazon ECS service has dedicated log streams for each container. If a service
scales up, each task instance has its own set of log streams. The naming convention for log
streams follows the pattern:

```
`log-group-prefix`/`container-name`/`task-id`
```

A single task writes to the same log streams during its lifetime. The log stream contains
messages from that task's containers and also any output from your application code. Every
message is timestamped, including your custom logs.

###### Note

Live Tail sessions incur costs by session usage time, per minute. For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

## Required permissions

The following permissions are required for the console IAM user to start and stop CloudWatch Logs Live Tail sessions:

- `logs:DescribeLogGroups`
- `logs:StartLiveTail`
- `logs:StopLiveTail`

## Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. Determine the resource you want to view

| Resource | Steps                                                                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tasks    | 1. On the **Clusters** page, choose the cluster. The cluster details page displays. 2. Choose the **Tasks** tab. The task details page displays. 3. Choose the **Logs** tab. |
| Services | 1. On the **Clusters** page, choose the cluster. The cluster details page displays. 2. Choose the service. The service details page displays. 3. Choose the **Logs** tab.    | 3. Choose **CloudWatch Logs Live Tail**, and then choose **Start**. 4. (Optional) To filter the streams, under **Filter**, for **Select log groups**, choose the log group. ## AWS CLI references You can also use the AWS CLI to start Live Tail sessions for CloudWatch Logs. The following resources provide detailed information about using the AWS CLI with Live Tail: <br>• [start-live-tail command reference](../../../cli/latest/reference/logs/start-live-tail.md "../../../cli/latest/reference/logs/start-live-tail.md") - Complete command syntax, parameters, and examples for the `aws logs start-live-tail` command. <br>• [CloudWatch Logs Live Tail user guide](../../../AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.md "../../../AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.md") - Comprehensive guide including AWS CLI usage with both print-only and interactive modes. <br>• [StartLiveTail SDK examples](../../../AmazonCloudWatch/latest/logs/example_cloudwatch-logs_StartLiveTail_section.md "../../../AmazonCloudWatch/latest/logs/example_cloudwatch-logs_StartLiveTail_section.md") - Programmatic examples for using the StartLiveTail API with various AWS SDKs. |
