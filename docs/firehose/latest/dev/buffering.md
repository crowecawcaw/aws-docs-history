# Buffer data for dynamic partitioning

Amazon Data Firehose buffers incoming streaming data to a certain size and for a certain period
of time before delivering it to the specified destinations. You can configure the buffer
size and the buffer interval while creating new Firehose streams or update the buffer size
and the buffer interval on your existing Firehose streams. A buffer size is measured in MBs
and a buffer interval is measured in seconds.

###### Note

Zero buffering feature is not available for dynamic partitioning.

When dynamic partitioning is enabled, Firehose internally buffers records that belong to
a given partition based on the configured buffering hint (size and time) before
delivering these records to your Amazon S3 bucket. In order to deliver maximum size
objects, Firehose uses multi-stage buffering internally. Therefore, end-to-end delay of a
batch of records might be 1.5 times of the configured buffering hint time. This affects
the data freshness of a Firehose stream.

The active partition count is the total number of active partitions within the
delivery buffer. For example, if the dynamic partitioning query constructs 3 partitions
per second and you have a buffer hint configuration triggering delivery every 60
seconds, then on average you would have 180 active partitions. If Firehose cannot deliver
the data in a partition to a destination, this partition is counted as active in the
delivery buffer until it can be delivered.

A new partition is created when an S3 prefix is evaluated to a new value based on the
record data fields and the S3 prefix expressions. A new buffer is created for each
active partition. Every subsequent record with the same evaluated S3 prefix is delivered
to that buffer.

Once the buffer meets the buffer size limit or the buffer time interval, Firehose creates
an object with the buffer data and delivers it to the specified Amazon S3 prefix. After the
object is delivered, the buffer for that partition and the partition itself are deleted
and removed from the active partitions count.

Firehose delivers each buffer data as a single object once the buffer size or interval
are met for each partition separately. Once the number of active partitions reaches a
limit of 500 per Firehose stream, the rest of the records in the Firehose stream are delivered to
the specified S3 error bucket prefix (activePartitionExceeded). You can use the [Amazon Data Firehose Limits form](https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=kinesis-firehose-limits "https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=kinesis-firehose-limits") to request an increase of this quota up to 5000
active partitions per given Firehose stream. If you need more partitions, you can create more
Firehose streams and distribute the active partitions across them.
