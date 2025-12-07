# Monitoring Amazon Nova Act

## Monitoring

Monitoring is an important part of maintaining the reliability, availability, and performance of Nova Act and your other AWS solutions. When deployed to AWS, you can monitor Nova Act using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics. You can graph the metrics using the CloudWatch console. You can also set alarms that watch for certain thresholds and send notifications or take actions when values exceed those thresholds. For more information, visit [What is Amazon CloudWatch](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.

The following table describes the runtime metrics provided by Nova Act.

| Metric Name  | Unit         | Dimensions        | Description                                                                                                        |
| ------------ | ------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Invocations  | Count        | Workflow, ApiName | Number of API requests received for a workflow.                                                                    |
| Latency      | Milliseconds | Workflow, ApiName | End-to-end latency for the API call. You can query percentiles (p50, p90, p99) to understand latency distribution. |
| UserErrors   | Count        | Workflow, ApiName | Count of user-side errors, such as invalid parameters, bad workflow or session IDs, or IAM permission issues.      |
| SystemErrors | Count        | Workflow, ApiName | Count of service-side errors, including internal faults, dependency failures, and timeouts.                        |
| Throttles    | Count        | Workflow, ApiName | Number of requests rejected due to throttling or exceeding service quotas.                                         |

### Metric dimensions

Amazon Nova Act metrics use the following dimensions:

- **Workflow** - The name of the workflow. This dimension allows you to filter metrics by specific workflows in your account.
- **ApiName** - The name of the API operation. This dimension allows you to filter metrics by specific API calls.

### Viewing metrics in CloudWatch

You can view Amazon Nova Act metrics using the CloudWatch console, AWS Command Line Interface, or CloudWatch API.

**To view metrics in the CloudWatch console:**

- Open the CloudWatch console at [console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
- In the navigation pane, choose **Metrics**, then choose **All metrics**.
- Choose the **AWS/NovaAct** namespace.
- Select a metric dimension (for example, **By Workflow**) to view available metrics.
- Select the checkbox next to the metrics you want to view.

The metrics appear in the graph on the page. You can customize the time range, statistic, and period for the metrics.

### Setting alarms

You can create CloudWatch alarms to monitor Nova Act metrics and receive notifications when metric values exceed thresholds you define. For example, you can create an alarm to notify you when:

- The number of system errors exceeds a threshold
- Workflow latency increases beyond acceptable levels
- Throttling occurs, indicating you may need to request quota increases

For information about creating alarms, visit [docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the Amazon CloudWatch User Guide.

### Monitoring best practices

Consider the following best practices when monitoring Nova Act:

- **Monitor error rates** - Track both UserErrors and SystemErrors metrics to identify issues with your workflows or service availability.
- **Set up latency alarms** - Create alarms for the Latency metric to detect performance degradation early.
- **Track throttling** - Monitor the Throttles metric to identify when you’re approaching service quotas.
- **Use percentile statistics** - For the Latency metric, use p90 or p99 statistics to understand tail latency and ensure consistent performance.
- **Create dashboards** - Build CloudWatch dashboards that combine multiple metrics to get a comprehensive view of your workflow health.
