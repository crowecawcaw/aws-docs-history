

# Monitor consumption from service-managed streams
<a name="service-managed-pk-consuming-monitoring"></a>

Use the following Amazon CloudWatch metrics to monitor consumption from service-managed streams:
+ **GetRecords.Records** – The number of records retrieved per GetRecords call. Use this to verify that consumption is proceeding normally.
+ **GetRecords.IteratorAgeMilliseconds** – How far behind the consumer is from the latest record. Use this to detect consumer lag.
+ **ReadProvisionedThroughputExceeded** – The number of GetRecords calls throttled for the shard. This should not change based on the distribution strategy.