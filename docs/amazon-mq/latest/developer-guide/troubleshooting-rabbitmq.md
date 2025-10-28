# Troubleshooting: RabbitMQ on Amazon MQ

Use the information in this section to help you diagnose and resolve common issues you might encounter when working
with RabbitMQ on Amazon MQ brokers.

###### Contents

- [I can't see metrics for my queues or virtual hosts in CloudWatch.](troubleshooting-rabbitmq.md#issues-cw-metrics-rabbitmq "troubleshooting-rabbitmq.md#issues-cw-metrics-rabbitmq")
- [How do I enable plugins in RabbitMQ on Amazon MQ?](troubleshooting-rabbitmq.md#issues-enabling-plugins-rabbitmq "troubleshooting-rabbitmq.md#issues-enabling-plugins-rabbitmq")
- [I'm unable to change Amazon VPC configuration for the broker.](troubleshooting-rabbitmq.md#issues-changing-vpc-configration-rabbitmq "troubleshooting-rabbitmq.md#issues-changing-vpc-configration-rabbitmq")
- [Cluster deployments have paused my queue synchronizations.](troubleshooting-rabbitmq.md#addressing-paused-queue-sync "troubleshooting-rabbitmq.md#addressing-paused-queue-sync")
- [My Amazon MQ for RabbitMQ single-instance broker is in a restart loop.](troubleshooting-rabbitmq.md#single-instance-broker-restart-loop "troubleshooting-rabbitmq.md#single-instance-broker-restart-loop")

## I can't see metrics for my queues or virtual hosts in CloudWatch.

If you're unable to view metrics for your queues or virtual hosts in CloudWatch, check if your queue or virtual host names
contain any blank spaces, tabs, or other non-ASCII characters.

Amazon MQ cannot publish metrics for virtual hosts and queues with names containing blank spaces, tabs or other non-ASCII characters.

For more information on dimension names, see [Dimension](../../../AmazonCloudWatch/latest/APIReference/API_Dimension.md#API_Dimension_Contents "../../../AmazonCloudWatch/latest/APIReference/API_Dimension.md#API_Dimension_Contents")
in the _Amazon CloudWatch API Reference_.

## How do I enable plugins in RabbitMQ on Amazon MQ?

RabbitMQ on Amazon MQ currently only supports the RabbitMQ management, shovel, federation,
consistent-hash exchange plugin, which are enabled by default. For more information on using
supported plugins, see [Plugins for Amazon MQ for RabbitMQ](rabbitmq-basic-elements-plugins.md "rabbitmq-basic-elements-plugins.md").

## I'm unable to change Amazon VPC configuration for the broker.

Amazon MQ does not support changing Amazon VPC configuration after your broker is created. Please note that you will
need to create a new broker with the new Amazon VPC configuration and update the client connection URL with the new
broker connection URL.

##

Cluster deployments have paused my queue synchronizations.

While addressing RabbitMQ's high memory alarms, you may find that messages on one or
multiple queues cannot be consumed. These queues may be in the process of synchronizing
messages between nodes, during which the respective queues become unavailable for publishing
and consuming. Queue synchronizations might become paused due to the high memory alarm, and even contribute to the memory alarm.

For information about stopping and retrying paused queue syncs, see [Resolving RabbitMQ paused queue synchronization](rabbitmq-queue-sync.md "rabbitmq-queue-sync.md").

##

My Amazon MQ for RabbitMQ single-instance broker is in a restart loop.

An Amazon MQ for RabbitMQ single-instance broker that raises a high memory alarm is at
risk of becoming unavailable if it restarts and doesn't have enough memory to start up.
This can cause RabbitMQ to enter a restart loop and prevent any further interactions with the broker until the issue is resolved.
If your broker is in a restart loop, you won't be able to apply the Amazon MQ recommended
[best practices](troubleshooting-action-required-codes-rabbitmq-memory-alarm.md "troubleshooting-action-required-codes-rabbitmq-memory-alarm.md") to
resolve the high memory alarm.

To recover your broker, we recommend upgrading to a larger instance type with more memory.
Unlike in cluster deployments, you can upgrade a single-instance broker while it's experiencing a high memory alarm
because there are no queue synchronizations to perform between nodes during a restart.
