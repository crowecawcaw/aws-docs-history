

# Viewing CloudWatch Logs Live Tail for Amazon ECS services and tasks
<a name="monitoring-cloudwatchlogs-view"></a>

CloudWatch Logs Live Tail helps you quickly troubleshoot incidents by viewing a streaming list of new log events as they are ingested. You can view task and service events in the Amazon ECS console. This view provides a cohesive view of your task and service health.

Each task in an Amazon ECS service has dedicated log streams for each container. If a service scales up, each task instance has its own set of log streams. The naming convention for log streams follows the pattern:

```
{{log-group-prefix}}/{{container-name}}/{{task-id}}
```

A single task writes to the same log streams during its lifetime. The log stream contains messages from that task's containers and also any output from your application code. Every message is timestamped, including your custom logs.

**Note**  
Live Tail sessions incur costs by session usage time, per minute. For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Required permissions
<a name="live-tail-permissions"></a>

The following permissions are required for the console IAM user to start and stop CloudWatch Logs Live Tail sessions:
+ `logs:DescribeLogGroups`
+ `logs:StartLiveTail`
+ `logs:StopLiveTail`

## Procedure
<a name="access-logs-console"></a>

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. Determine the resource you want to view    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-cloudwatchlogs-view.html)

1. Choose **CloudWatch Logs Live Tail**, and then choose **Start**.

1. (Optional) To filter the streams, under **Filter**, for **Select log groups**, choose the log group.

## AWS CLI references
<a name="cli-references"></a>

You can also use the AWS CLI to start Live Tail sessions for CloudWatch Logs. The following resources provide detailed information about using the AWS CLI with Live Tail:
+ [start-live-tail command reference](https://docs.aws.amazon.com/cli/latest/reference/logs/start-live-tail.html) - Complete command syntax, parameters, and examples for the `aws logs start-live-tail` command.
+ [CloudWatch Logs Live Tail user guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) - Comprehensive guide including AWS CLI usage with both print-only and interactive modes.
+ [StartLiveTail SDK examples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_StartLiveTail_section.html) - Programmatic examples for using the StartLiveTail API with various AWS SDKs.