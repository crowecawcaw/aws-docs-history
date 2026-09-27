

# CloudFront real-time logs to service-managed streams
<a name="service-managed-pk-integrations-cloudfront"></a>

Amazon CloudFront can publish real-time logs directly to an Kinesis Data Streams stream through its native integration. Amazon CloudFront produces log records to the stream; it does not use the KPL and has no aggregation logic that depends on associating a partition key with a specific shard. Although the records Amazon CloudFront generates include a partition key, the value is not used for routing on a service-managed stream. Enabling service-managed record distribution on a stream that receives Amazon CloudFront real-time logs requires no changes and has no impact on log delivery. For more information about Amazon CloudFront real-time logs, see [Real-time logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html) in the *Amazon CloudFront Developer Guide*.