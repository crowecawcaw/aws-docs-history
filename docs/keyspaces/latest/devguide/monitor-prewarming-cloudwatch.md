# Monitor the performance of a pre-warmed table using Amazon CloudWatch

Amazon Keyspaces pre-warming doesn't introduce new CloudWatch metrics, but you can monitor the performance of pre-warmed tables using existing Amazon Keyspaces metrics:

SuccessfulRequestLatency

Monitor this metric to verify that the pre-warmed table is handling requests with expected latency.

WriteThrottleEvents and ReadThrottleEvents

These metrics should remain low for a properly pre-warmed table. If you
see insufficient capacity errors despite pre-warming, you might need to
adjust your warm-throughput values.

ConsumedReadCapacityUnits and ConsumedWriteCapacityUnits

These metrics show the actual consumption of capacity, which can help validate if your pre-warming configuration is appropriate.

ProvisionedReadCapacityUnits and ProvisionedWriteCapacityUnits

For provisioned tables, these metrics show the currently allocated capacity.

These metrics can be viewed in the CloudWatch console or queried using the CloudWatch API. For
more information, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
