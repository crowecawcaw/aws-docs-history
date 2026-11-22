

# Quotas and limits for queues

The following quotas and limits apply to queues. A queue works only on a stream in On-demand Standard or On-demand Advantage capacity mode. Provisioned mode is not supported.

## Resource quotas
<a name="queues-quotas-resource"></a>


| Resource | Value | Notes | 
| --- | --- | --- | 
| Receive throughput | Virtually unlimited | A queue suits workloads that receive large volumes of records across many consumer instances. A record counts against the queue's in-flight limit from the time a consumer instance receives it until the instance acknowledges it, so monitor InFlightQueueRecords to see how close your queue consumer is to that limit. | 
| Queues per stream | 20 on On-demand Standard, 50 on On-demand Advantage | A queue counts as one registered consumer, and queues share this limit with enhanced fan-out consumers, so the two together cannot exceed it. For more information, see [Registered consumer sharing](#queues-quotas-consumers). | 
| Streams per queue | 1 | A queue delivers records from exactly one stream, and StreamConfigurationList must contain exactly one entry. To consume a second stream, create a second queue. | 
| Concurrent queues in CREATING or DELETING state per account per Region | 5 | The number of queues that can be in the CREATING or DELETING state at the same time in an account in a Region. | 
| Maximum in-flight records per queue | 120,000 | The number of records that can be in flight for a queue at the same time. | 
| Visible records a metric reports | 1,000,000 | VisibleQueueRecords and VisibleDeadLetterQueueRecords each report up to 1,000,000 records. A queue can hold more visible records than its metric reports. | 
| Records per call | 10 | A receive call returns up to 10 records, set by Limit. An acknowledge, visibility, or restore call accepts up to 10 entries. Both limits apply to records and to dead-letter records. | 
| Maximum record size a queue delivers | The stream's maximum record size | A queue delivers any record written to its stream, up to 10 MiB. | 

## Configuration ranges
<a name="queues-quotas-config"></a>


| Setting | Range | Notes | 
| --- | --- | --- | 
| Visibility timeout | 0 to 43,200 seconds | Up to 12 hours. Set per queue or per receive call. Set to 0 to make a record visible immediately. | 
| MaxReceiveCount | 1 to 1,000 | The number of times a record can be received without being acknowledged before it becomes a dead-letter record. Required when TargetType is BUILT\_IN. A queue that you create without DeadLetterConfiguration gets a MaxReceiveCount of 6. | 
| Receive wait time | 1 to 20 seconds (default 9) | How long a receive call waits for records to arrive. | 
| ListQueues maximum results per page | 1 to 10,000 | Use pagination tokens to retrieve additional results. | 
| Queue name length | 1 to 128 characters | The pattern is [a-zA-Z0-9\_.-]\+. | 

## Control plane API limits
<a name="queues-quotas-throttle"></a>

These limits apply per AWS account per Region to the queue control plane operations, which create and manage your queues. A control plane call that exceeds a limit fails with `LimitExceededException`, and a throttled data plane call fails with `ThrottlingException`. Retry the call with exponential backoff.


| API | API call limit | 
| --- | --- | 
| CreateQueue | 5 TPS | 
| DeleteQueue | 5 TPS | 
| DeleteResourcePolicy | 5 TPS | 
| DescribeQueue | 20 TPS | 
| GetResourcePolicy | 5 TPS | 
| ListQueues | 5 TPS | 
| PutResourcePolicy | 5 TPS | 
| UpdateQueue | 5 TPS | 

## Registered consumer sharing
<a name="queues-quotas-consumers"></a>

A queue counts as one registered consumer on its stream. A queue shares the stream registered consumer limit with enhanced fan-out consumers: 20 on On-demand Standard and 50 on On-demand Advantage. For more information about registered consumers, see [Develop enhanced fan-out consumers with dedicated throughput](enhanced-consumers.md).