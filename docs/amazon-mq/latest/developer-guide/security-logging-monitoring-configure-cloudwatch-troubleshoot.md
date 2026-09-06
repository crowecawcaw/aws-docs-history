

# Troubleshooting CloudWatch Logs Configuration with Amazon MQ
<a name="security-logging-monitoring-configure-cloudwatch-troubleshoot"></a>

In some cases, CloudWatch Logs might not always behave as expected. This section gives an overview of common issues and shows how to resolve them.

## Log Groups Don't Appear in CloudWatch
<a name="security-logging-monitoring-configure-cloudwatch-do-not-appear"></a>

[Add the `CreateLogGroup` permission to your Amazon MQ user](configure-logging-monitoring-activemq.md#security-logging-monitoring-configure-cloudwatch-permissions) and reboot the broker. This allows Amazon MQ to create the log group.

## Log Streams Don't Appear in CloudWatch Log Groups
<a name="security-logging-monitoring-configure-cloudwatch-streams-do-not-appear"></a>

[Configure a resource-based policy for Amazon MQ](configure-logging-monitoring-activemq.md#security-logging-monitoring-configure-cloudwatch-resource-permissions). This allows your broker to publish its logs.