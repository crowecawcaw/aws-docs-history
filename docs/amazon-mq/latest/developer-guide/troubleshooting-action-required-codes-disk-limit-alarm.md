# RabbitMQ on Amazon MQ: Disk limit alarm

Disk limit alarm is an indication that the volume of disk used by a RabbitMQ node has decreased due to
a high number of messages not consumed while new messages were added. RabbitMQ will raise a disk limit alarm when the broker's
free disk space, identified by Amazon CloudWatch metric `RabbitMQDiskFree`, reaches the disk limit, identified by `RabbitMQDiskFreeLimit`.
`RabbitMQDiskFreeLimit` is set by Amazon MQ and has been defined considering the disk space available for each broker instance type.
For more information, see [Memory and disk alarms](rmq-broker-instance-types.md#rabbitmq-memory-disk-thresholds "rmq-broker-instance-types.md#rabbitmq-memory-disk-thresholds").

An RabbitMQ on Amazon MQ broker that has raised a disk limit alarm will become unavailable for new messages being published.
If you have a publisher and consumer on the same connection, the consumer will also be unavailable to receive messages.
When running RabbitMQ in a cluster,
the disk alarm is cluster-wide. If one node goes under the limit, all other nodes will block incoming messages.
Due to the lack of disk space, your broker might also experience other issues that complicate diagnosis and resolution of the alarm.

Amazon MQ will not restart a broker experiencing a disk alarm and will return an exception for `RebootBroker`
API operations as long as the broker continues to raise the alarm.

###### Note

You cannot downgrade a broker from an `mq.m5` instance type to an `mq.t3.micro` instance type.
If you wish to downgrade, you must delete your broker and create a new one.

## Diagnosing and addressing disk limit alarm

Amazon MQ enables metrics for your broker by default. You can [view your broker metrics](amazon-mq-accessing-metrics.md "amazon-mq-accessing-metrics.md") by accessing the Amazon CloudWatch console,
or by using the CloudWatch API.`MessageCount` is a useful metric when diagnosing the RabbitMQ disk limit alarm.
Messages are stored in memory until they are consumed or discarded. A high message count indicates overutilization of
disk storage and can lead to a disk alarm.

To diagnose the disk limit alarm, use the Amazon MQ Management Console to:

- Create a new connection to consume messages published to the queues.
- Purge messages from queues.
- Delete the queues from your broker.

###### Note

It may take up to several hours for the RABBITMQ\_DISK\_ALARM status to clear after you take the required actions.

To prevent the disk limit alarm from reoccurring, you can upgrade your host [instance type](rmq-broker-instance-types.md "rmq-broker-instance-types.md") to an instance with additional resources.
For information on how to update your broker's instance type see `UpdateBrokerInput`
in the Amazon MQ REST API Reference. We also recommend keeping your publishers and
consumers on different connections.

## Mitigating disk limit alarm by increasing configurable storage

You can also mitigate a disk limit alarm by increasing the broker's configurable EBS
storage size. This option is available when your current EBS volume is below the maximum
allowable storage for your instance type. Before proceeding, review
[Configurable storage best practices for Amazon MQ for RabbitMQ](best-practices-configurable-storage.md "best-practices-configurable-storage.md") to understand the supported
storage ranges.

To increase configurable storage, apply an update and reboot the broker. Because the broker
is in a critical action required state due to the disk usage alarm, _RabbitMQ does not restart_. Amazon MQ
applies the storage increase, and the broker exits the critical action required state once the disk usage alarm
clears.

###### Note

While the broker is in a critical action required state due to the disk usage alarm, only a configurable storage increase
is permitted. You cannot change the broker's instance type until the broker has exited
the alarm state.

After updating, monitor the `RabbitMQDiskFree` and
`RabbitMQDiskFreeLimit` Amazon CloudWatch metrics to confirm the broker exits the alarm
state. To prevent disk alarm events from reoccurring, monitor disk usage over time and
follow the guidance in [Amazon MQ for RabbitMQ best practices](best-practices-rabbitmq.md "best-practices-rabbitmq.md"). If additional disk or
other resource capacity is needed, consider upgrading the broker's instance type as well.
