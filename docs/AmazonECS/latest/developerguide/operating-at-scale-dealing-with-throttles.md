# Handle Amazon ECS throttling issues

Throttling errors fall into two major categories: synchronous
throttling and asynchronous throttling.

## Synchronous throttling

When synchronous throttling occurs, you immediately receive an error response from
Amazon ECS. This category typically occurs when you call Amazon ECS APIs while running tasks or
creating services. For more information about the throttling involved and the relevant
throttle limits, see [Request throttling for
the Amazon ECS API](../APIReference/request-throttling.md "../APIReference/request-throttling.md").

When your application initiates API requests, for example, by using the AWS CLI or
an AWS SDK, you can remediate API throttling. You can do this by either
architecting your application to handle the errors or by implementing an exponential
backoff and jitter strategy with retry logic for the API calls. For more
information, see [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ "https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/").

If you use an AWS SDK, the automatic retry logic is built-in and
configurable.

## Asynchronous throttling

Asynchronous throttling occurs because of asynchronous workflows where Amazon ECS or
CloudFormation might be calling APIs on your behalf to provision resources. It's important to
know which AWS APIs that Amazon ECS invokes on your behalf. For example, the
`CreateNetworkInterface` API is invoked for tasks that use the
`awsvpc` network mode, and the `DescribeTargetHealth` API
is invoked when performing health checks for tasks registered to a load
balancer.

When your workloads reach a considerable scale, these API operations might be
throttled. That is, they might be throttled enough to breach the limits enforced by
Amazon ECS or the AWS service that is being called. For example, if you deploy hundreds
of services, each having hundreds of tasks concurrently that use the
`awsvpc` network mode, Amazon ECS invokes Amazon EC2 API operations such as
`CreateNetworkInterface` and Elastic Load Balancing API operations such as
`RegisterTarget` or `DescribeTargetHealth` to register the
elastic network interface and load balancer, respectively. These API calls can
exceed the API limits, resulting in throttling errors. The following is an example
of an Elastic Load Balancing throttling error that's included in the service event message.

```
{
   "userIdentity":{
      "arn":"arn:aws:sts::111122223333:assumed-role/AWSServiceRoleForECS/ecs-service-scheduler",
      "eventTime":"2022-03-21T08:11:24Z",
      "eventSource":"elasticloadbalancing.amazonaws.com",
      "eventName":" DescribeTargetHealth ",
      "awsRegion":"us-east-1",
      "sourceIPAddress":"ecs.amazonaws.com",
      "userAgent":"ecs.amazonaws.com",
      "errorCode":"ThrottlingException",
      "errorMessage":"Rate exceeded",
      "eventID":"0aeb38fc-229b-4912-8b0d-2e8315193e9c"
   }
}
```

When these API calls share limits with other API traffic in your account, they
might be difficult monitor even though they're emitted as service events.

## Monitor throttling

It's important to identify which API requests are throttled and who issues these
requests. You can use AWS CloudTrail which monitors throttling, and integrates with CloudWatch,
Amazon Athena, and Amazon EventBridge. You can configure CloudTrail to send specific events to CloudWatch Logs. CloudWatch Logs
log insights parses and analyzes the events. This identifies details in throttling
events such as the user or IAM role that made the call and the number of API calls
that were made. For more information, see [Monitoring CloudTrail log files with CloudWatch Logs](../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md "../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md").

For more information about CloudWatch Logs insights and instructions on how to query log
files, see [Analyzing log data with
CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md").

With Amazon Athena, you can create queries and analyze data using standard SQL. For
example, you can create an Athena table to parse CloudTrail events. For more information,
see [Using the
CloudTrail console to create an Athena table for CloudTrail logs](../../../athena/latest/ug/cloudtrail-logs.md#create-cloudtrail-table-ct "../../../athena/latest/ug/cloudtrail-logs.md#create-cloudtrail-table-ct").

After creating an Athena table, you can use SQL queries such as the following one to
investigate `ThrottlingException` errors.

Replace the `user-input` with your values.

```
select eventname, errorcode,eventsource,awsregion, useragent,COUNT(*) count
FROM cloudtrail_`table-name`
where errorcode = 'ThrottlingException'
AND eventtime between '`2024-09-24T00:00:08Z`' and '`2024-09-23T23:15:08Z`'
group by errorcode, awsregion, eventsource, useragent, eventname
order by count desc;
```

Amazon ECS also emits event notifications to Amazon EventBridge. There are resource state change
events and service action events. They include API throttling events such as
`ECS_OPERATION_THROTTLED` and
`SERVICE_DISCOVERY_OPERATION_THROTTLED`. For more information, see [Amazon ECS service action events](ecs_service_events.md "ecs_service_events.md").

These events can be consumed by a service such as AWS Lambda to perform actions in
response. For more information, see [Handling Amazon ECS events](ecs_cwet_handling.md "ecs_cwet_handling.md").

If you run standalone tasks, some API operations such as `RunTask` are
asynchronous, and retry operations aren't automatically performed. In such cases,
you can use services such as AWS Step Functions with EventBridge integration to retry throttled or
failed operations. For more information, see [Manage a container task (Amazon ECS, Amazon SNS)](../../../step-functions/latest/dg/sample-project-container-task-notification.md "../../../step-functions/latest/dg/sample-project-container-task-notification.md").

## Use CloudWatch to monitor throttling

CloudWatch offers API usage monitoring on the `Usage` namespace under
**By AWS Resource**. These metrics are logged with type
**API** and metric name **CallCount**. You can
create alarms to start whenever these metrics reach a certain threshold. For more
information, see [Visualizing your service quotas and setting alarms](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md").

CloudWatch also offers anomaly detection. This feature uses machine learning to analyze
and establish baselines based on the particular behavior of the metric that you
enabled it on. If there's unusual API activity, you can use this feature together
with CloudWatch alarms. For more information, see [Using
CloudWatch anomaly detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md").

By proactively monitoring throttling errors, you can contact Support to increase the
relevant throttling limits and also receive guidance for your unique application
needs.
