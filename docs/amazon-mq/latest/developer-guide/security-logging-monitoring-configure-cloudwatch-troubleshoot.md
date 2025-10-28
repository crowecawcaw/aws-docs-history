# Troubleshooting CloudWatch Logs Configuration with Amazon MQ

In some cases, CloudWatch Logs might not always behave as expected. This section gives an
overview of common issues and shows how to resolve them.

## Log Groups Don't Appear in CloudWatch

[Add the
CreateLogGroup permission to your Amazon MQ user](configure-logging-monitoring-activemq.md#security-logging-monitoring-configure-cloudwatch-permissions "configure-logging-monitoring-activemq.md#security-logging-monitoring-configure-cloudwatch-permissions") and
reboot the broker. This allows Amazon MQ to create the log group.

## Log Streams Don't Appear in CloudWatch Log Groups

[Configure a resource-based
policy for Amazon MQ](configure-logging-monitoring-activemq.md#security-logging-monitoring-configure-cloudwatch-resource-permissions "configure-logging-monitoring-activemq.md#security-logging-monitoring-configure-cloudwatch-resource-permissions"). This allows your broker to publish its logs.
