# Logging and monitoring Amazon MQ brokers

Monitoring is an important part of maintaining the reliability, availability, and
performance of your AWS solutions. You should collect monitoring data from all of the
parts of your AWS solution so that you can more easily debug a multi-point failure if one
occurs. AWS provides several tools for monitoring your Amazon MQ resources and responding to
potential incidents:

You can use CloudWatch to view and analyze metrics for your Amazon MQ broker.
You can view and analyze your broker metrics from the CloudWatch console, the AWS CLI, or the CloudWatch AWS CLI.
CloudWatch metrics for Amazon MQ are automatically polled from the broker and then pushed to CloudWatch every minute.
For ActiveMQ brokers, CloudWatch monitors only the first 1000 destinations.. For RabbitMQ brokers, CloudWatch monitors only the first 500 destinations, ordered by number of consumers..

For a full list of Amazon MQ metrics, see [Available CloudWatch metrics Amazon MQ for ActiveMQ brokers](activemq-logging-monitoring.md "activemq-logging-monitoring.md").

For information about creating a CloudWatch alarm for a metrics, see [Create or Edit a CloudWatch Alarm](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the
_Amazon CloudWatch User Guide_.
