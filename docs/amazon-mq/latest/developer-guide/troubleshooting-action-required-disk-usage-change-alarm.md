

# Amazon MQ for RabbitMQ: Disk usage change alarm
<a name="troubleshooting-action-required-disk-usage-change-alarm"></a>

 `RABBITMQ_DISK_USAGE_TOO_HIGH_FOR_CHANGE` indicates that a requested broker instance type change, storage size change, or both cannot proceed because of high disk usage on the current RabbitMQ node. Amazon MQ for RabbitMQ raises this alarm when current disk usage exceeds what would be available after the requested change, as identified by the CloudWatch metric `RabbitMQDiskFree`. 

 RabbitMQ brokers that enter the `RABBITMQ_DISK_USAGE_TOO_HIGH_FOR_CHANGE` state remain available for your applications. However, Amazon MQ does not apply the requested change. In this state, you can restart your broker. You cannot change the instance type or storage size while disk usage exceeds the threshold for the requested configuration. 

## Diagnosing and addressing RABBITMQ\_DISK\_USAGE\_TOO\_HIGH\_FOR\_CHANGE
<a name="w2aac40c29b7"></a>

 By default, your broker metrics are enabled. You can view them in the CloudWatch console or by using the CloudWatch API. Use the `MessageCount` and `RabbitMQDiskFree` metrics to diagnose `RABBITMQ_DISK_USAGE_TOO_HIGH_FOR_CHANGE`. 

 To resolve the alarm, reduce your disk usage. Use the Amazon MQ Management Console to do one of the following: 
+  Create a new connection to consume messages published to the queues 
+  Purge messages from queues 
+  Delete the queues from your broker 

 Alternatively, you can remove your pending changes by calling the `UpdateBroker` API to revert the requested instance type or storage size back to the current configuration. This removes the pending change and clears the quarantine state. 

**Note**  
It might take up to several hours for the `RABBITMQ_DISK_USAGE_TOO_HIGH_FOR_CHANGE` status to clear after you take the required actions.