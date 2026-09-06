

# Available CloudWatch metrics for Amazon MQ for RabbitMQ brokers
<a name="rabbitmq-logging-monitoring"></a>

**Warning**  
Starting with RabbitMQ 4.2, `RabbitMQIOReadAverageTime` and `RabbitMQIOWriteAverageTime` are deprecated and will not publish meaningful values. These metrics will be removed from CloudWatch in the next major RabbitMQ release.

## RabbitMQ broker metrics
<a name="security-logging-monitoring-cloudwatch-metrics-rabbitmq"></a>

**Note**  
The management plugin is [not recommended for production or long-term monitoring by open source RabbitMQ](https://www.rabbitmq.com/docs/management). We recommend using Prometheus to query per-node metrics from RabbitMQ 4.2 onwards.


| Metric | Unit | Description | 
| --- | --- | --- | 
| ExchangeCount | Count | The total number of exchanges configured on the broker. | 
| QueueCount | Count | The total number of queues configured on the broker. | 
| ConnectionCount | Count | The total number of connections established on the broker. | 
| ChannelCount | Count | The total number of channels established on the broker. The concept of channels is specific to AMQP 0-9-1.  | 
| ConsumerCount | Count | The total number of consumers connected to the broker. | 
| MessageCount | Count | The total number of messages in the queues.  The number produced is the total sum of ready and unacknowledged messages on the broker.  | 
| MessageReadyCount | Count | The total number of ready messages in the queues. | 
| MessageUnacknowledgedCount | Count | The total number of unacknowledged messages in the queues. | 
| PublishRate | Count | The rate at which messages are published to the broker. The number produced represents the number of messages per second at the time of sampling.This metric reflects only AMQP 0-9-1 protocol activity. For AMQP 1.0 metrics, see [Accessing Prometheus metrics](rabbitmq-prometheus-metrics.md). | 
| ConfirmRate | Count | The rate at which the RabbitMQ server is confirming published messages. You can compare this metric with PublishRate to better understand how your broker is performing. The number produced represents the number of messages per second at the time of sampling.This metric reflects only AMQP 0-9-1 protocol activity. For AMQP 1.0 metrics, see [Accessing Prometheus metrics](rabbitmq-prometheus-metrics.md). | 
| AckRate | Count | The rate at which messages are being acknowledged by consumers. The number produced represents the number of messages per second at the time of sampling.This metric reflects only AMQP 0-9-1 protocol activity. For AMQP 1.0 metrics, see [Accessing Prometheus metrics](rabbitmq-prometheus-metrics.md). | 
| SystemCpuUtilization | Percent | The percentage of allocated Amazon EC2 compute units that the broker currently uses. For cluster deployments, this value represents the aggregate of all three RabbitMQ nodes' corresponding metric values. | 
| RabbitMQMemLimit | Bytes | The RAM limit for a RabbitMQ broker. This metric varies depending on instance type. For more information, see [Memory and disk alarms](rmq-broker-instance-types.md#rabbitmq-memory-disk-thresholds). For cluster deployments, this value represents the aggregate of all three RabbitMQ nodes' corresponding metric values. | 
| RabbitMQMemUsed | Bytes | The volume of RAM used by a RabbitMQ broker. For cluster deployments, this value represents the aggregate of all three RabbitMQ nodes' corresponding metric values. | 
| RabbitMQDiskFreeLimit | Bytes | The disk limit for a RabbitMQ broker. For cluster deployments, this value represents the aggregate of all three RabbitMQ nodes' corresponding metric values. This metric varies depending on instance type and deployment mode. For more information, see [Memory and disk alarms](rmq-broker-instance-types.md#rabbitmq-memory-disk-thresholds). | 
| RabbitMQDiskFree | Bytes | The total volume of free disk space available in a RabbitMQ broker. When disk usage goes above its limit, the cluster will block all producer connections. For cluster deployments, this value represents the aggregate of all three RabbitMQ nodes' corresponding metric values. | 
| RabbitMQFdUsed | Count | Number of file descriptors used. For cluster deployments, this value represents the aggregate of all three RabbitMQ nodes' corresponding metric values. | 
| RabbitMQIOReadAverageTime | Count | The average time (in milliseconds) for RabbitMQ to perform one read operation. The value is proportional to the message size. | 
| RabbitMQIOWriteAverageTime | Count | The average time (in milliseconds) for RabbitMQ to perform one write operation. The value is proportional to the message size. | 

## Dimensions for RabbitMQ broker metrics
<a name="security-logging-monitoring-cloudwatch-dimensions-rabbitmq"></a>


| Dimension | Description | 
| --- | --- | 
| Broker | The name of the broker. | 

## RabbitMQ node metrics
<a name="security-logging-monitoring-cloudwatch-destination-metrics-rabbitmq"></a>


| Metric | Unit | Description | 
| --- | --- | --- | 
| SystemCpuUtilization | Percent | The percentage of allocated Amazon EC2 compute units that the broker currently uses. | 
| RabbitMQMemLimit | Bytes | The RAM limit for a RabbitMQ node. This metric varies depending on instance type. For more information, see [Memory and disk alarms](rmq-broker-instance-types.md#rabbitmq-memory-disk-thresholds). | 
| RabbitMQMemUsed | Bytes | The volume of RAM used by a RabbitMQ node. When memory use goes above the limit, the cluster will block all producer connections. | 
| RabbitMQDiskFreeLimit | Bytes | The disk limit for a RabbitMQ node. This metric varies depending on instance type and deployment mode. For more information, see [Memory and disk alarms](rmq-broker-instance-types.md#rabbitmq-memory-disk-thresholds). | 
| RabbitMQDiskFree | Bytes | The total volume of free disk space available in a RabbitMQ node. When disk usage goes above its limit, the cluster will block all producer connections. | 
| RabbitMQFdUsed | Count | Number of file descriptors used. | 
| ExchangeCount | Count | The total number of exchanges configured on the node. Available for RabbitMQ 4.2 and above. | 
| QueueCount | Count | The total number of queues configured on the node. Available for RabbitMQ 4.2 and above. | 
| ConnectionCount | Count | The total number of connections established on the node. Available for RabbitMQ 4.2 and above. | 
| ChannelCount | Count | The total number of channels established on the node. Available for RabbitMQ 4.2 and above. | 
| ConsumerCount | Count | The total number of consumers connected to the node. Available for RabbitMQ 4.2 and above. | 
| MessageCount | Count | The total number of messages in queues on the node. Available for RabbitMQ 4.2 and above. | 
| MessageReadyCount | Count | The total number of ready messages in queues on the node. Available for RabbitMQ 4.2 and above. | 
| MessageUnacknowledgedCount | Count | The total number of unacknowledged messages in queues on the node. Available for RabbitMQ 4.2 and above. | 

## Aggregating cluster-wide metrics from RabbitMQ node metrics
<a name="security-logging-monitoring-cloudwatch-aggregated-cluster-metrics-rabbitmq"></a>

To get aggregated cluster-wide metrics, you can find the corresponding per-node metrics on the CloudWatch console by filtering on broker name and metric name. Then, select those metrics by clicking on the checkboxes, and choose **Add math** > **Common** > **Sum**.

## Dimensions for RabbitMQ node metrics
<a name="security-logging-monitoring-cloudwatch-destination-dimensions-rabbitmq"></a>


| Dimension | Description | 
| --- | --- | 
| Node | The name of the node.  A node name consists of two parts: a prefix (usuallly `rabbit`) and a hostname. For example, `rabbit@ip-10-0-0-230.us-west-2.compute.internal` is a node name with the prefix `rabbit` and the hostname `ip-10-0-0-230.us-west-2.compute.internal`.   | 
| Broker | The name of the broker. | 

## RabbitMQ queue metrics
<a name="security-logging-monitoring-cloudwatch-queue-metrics-rabbitmq"></a>


| Metric | Unit | Description | 
| --- | --- | --- | 
| ConsumerCount | Count | The number of consumers subscribed to the queue. | 
| MessageReadyCount | Count | The number of messages that are currently available to be delivered. | 
| MessageUnacknowledgedCount | Count | The number of messages for which the server is awaiting acknowledgement. | 
| MessageCount | Count | The total number of MessageReadyCount and MessageUnacknowledgedCount (also known as queue depth). | 

## Dimensions for RabbitMQ queue metrics
<a name="security-logging-monitoring-cloudwatch-dimensions-queue-rabbitmq"></a>

**Note**  
Amazon MQ for RabbitMQ will not publish metrics for virtual hosts and queues with names containing blank spaces, tabs or other non-ASCII characters.  
For more information about dimension names, see [Dimension](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Dimension.html#API_Dimension_Contents) in the *Amazon CloudWatch API Reference*. 


| Dimension | Description | 
| --- | --- | 
| Queue | The name of the queue. | 
| VirtualHost | The name of the virtual host. | 
| Broker | The name of the broker. | 

## RabbitMQ network metrics
<a name="security-logging-monitoring-cloudwatch-network-metrics-rabbitmq"></a>


| Metric | Unit | Description | 
| --- | --- | --- | 
| NetworkOut | Bytes | The number of bytes sent out by the instance on all network interfaces. This metric identifies the volume of outgoing network traffic from a single instance. The number reported is the number of bytes sent during the period. If you are using basic (5-minute) monitoring and the statistic is Sum, you can divide this number by 300 to find Bytes/second. If you have detailed (1-minute) monitoring and the statistic is Sum, divide it by 60. You can also use the CloudWatch metric math function `DIFF_TIME` to find the bytes per second. For example, if you have graphed NetworkOut in CloudWatch as `m1`, the metric math formula `m1/(DIFF_TIME(m1))` returns the metric in bytes/second. For more information about `DIFF_TIME` and other metric math functions, see [Using metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html).<br />**Meaningful Statistics:** Sum, Average, Minimum, Maximum | 
| NetworkIn | Bytes | The number of bytes received by the instance on all network interfaces. This metric identifies the volume of incoming network traffic to a single instance. The number reported is the number of bytes received during the period. If you are using basic (5-minute) monitoring and the statistic is Sum, you can divide this number by 300 to find Bytes/second. If you have detailed (1-minute) monitoring and the statistic is Sum, divide it by 60. You can also use the CloudWatch metric math function `DIFF_TIME` to find the bytes per second. For example, if you have graphed NetworkIn in CloudWatch as `m1`, the metric math formula `m1/(DIFF_TIME(m1))` returns the metric in bytes/second. For more information about `DIFF_TIME` and other metric math functions, see [Using metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html).<br />**Meaningful Statistics:** Sum, Average, Minimum, Maximum | 

## Dimensions for RabbitMQ brokers
<a name="security-logging-monitoring-dimensions-rabbitmq"></a>


| Dimension | Description | 
| --- | --- | 
| Broker | The name of the broker. | 

## Configuring Amazon MQ for RabbitMQ logs
<a name="security-logging-monitoring-rabbitmq"></a>

 When you enable CloudWatch logging for your RabbitMQ brokers, Amazon MQ uses a service-linked role to publish general logs to CloudWatch. If no Amazon MQ service-linked role exists when you first create a broker, Amazon MQ will automatically create one. All subsequent RabbitMQ brokers will use the same service-linked role to publish logs to CloudWatch. 

 For more information about service-linked roles, see [ Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *AWS Identity and Access Management User Guide*. For more information about how Amazon MQ uses service-linked roles, see [Using service-linked roles for Amazon MQ](using-service-linked-roles.md). 