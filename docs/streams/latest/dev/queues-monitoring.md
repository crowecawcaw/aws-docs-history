

# Monitor a queue

When you consume records from a stream with a queue, Kinesis Data Streams sends metrics for the queue to CloudWatch every minute in the `AWS/Kinesis` namespace. Kinesis Data Streams publishes these metrics with the `QueueId` and `QueueName` dimensions.

**Note**  
After you create a queue, Kinesis Data Streams can take up to three minutes to publish its first metrics for the queue. Kinesis Data Streams also stops publishing metrics for a queue that has had no visible records for about six hours, and publishes them again as soon as a consumer instance receives from the queue.

The following table describes the metrics that Kinesis Data Streams publishes for the records in a queue.


| Metric | Description | 
| --- | --- | 
| ReceivedQueueRecords | The number of records that queue consumers received from the queue over the specified time period.<br />Dimensions: QueueId, QueueName<br />Statistics: Sum<br />Units: Count | 
| AcknowledgedQueueRecords | The number of records that queue consumers acknowledged over the specified time period.<br />Dimensions: QueueId, QueueName<br />Statistics: Sum<br />Units: Count | 
| EmptyReceives | The number of receive calls that returned no records over the specified time period.<br />Dimensions: QueueId, QueueName<br />Statistics: Sum<br />Units: Count | 
| VisibleQueueRecords | The approximate number of records in the queue that are visible and ready to be received. This metric reports up to 1,000,000 records.<br />Dimensions: QueueId, QueueName<br />Statistics: Average<br />Units: Count | 
| InFlightQueueRecords | The approximate number of records in the queue that are in flight: a consumer instance has received each one, and has not acknowledged it, and the queue has not yet made it visible again.<br />Dimensions: QueueId, QueueName<br />Statistics: Average<br />Units: Count | 

The following table describes the metrics that Kinesis Data Streams publishes for the dead-letter records in a queue. We recommend that you create a CloudWatch alarm on `VisibleDeadLetterQueueRecords` to detect records that a queue consumer cannot process.


| Metric | Description | 
| --- | --- | 
| ReceivedDeadLetterQueueRecords | The number of dead-letter records that queue consumers received over the specified time period.<br />Dimensions: QueueId, QueueName<br />Statistics: Sum<br />Units: Count | 
| AcknowledgedDeadLetterQueueRecords | The number of dead-letter records that queue consumers acknowledged over the specified time period.<br />Dimensions: QueueId, QueueName<br />Statistics: Sum<br />Units: Count | 
| EmptyDeadLetterReceives | The number of dead-letter receive calls that returned no records over the specified time period.<br />Dimensions: QueueId, QueueName<br />Statistics: Sum<br />Units: Count | 
| VisibleDeadLetterQueueRecords | The approximate number of dead-letter records that are visible and ready to be received. This metric reports up to 1,000,000 records.<br />Dimensions: QueueId, QueueName<br />Statistics: Average<br />Units: Count | 
| RestoredDeadLetterQueueRecords | The number of dead-letter records that `RestoreDeadLetterQueueRecords` returned to the normal receive path over the specified time period. Kinesis Data Streams publishes this metric only after you have restored at least one dead-letter record in the queue.<br />Dimensions: QueueId, QueueName<br />Statistics: Sum<br />Units: Count | 
| InFlightDeadLetterQueueRecords | The approximate number of dead-letter records that are in flight.<br />Dimensions: QueueId, QueueName<br />Statistics: Average<br />Units: Count | 