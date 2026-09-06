

# Supported CloudWatch metrics
<a name="cloudtrail-lake-cloudwatch-metrics"></a>

**Note**  
AWS CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](cloudtrail-lake-service-availability-change.md).

CloudTrail Lake supports Amazon CloudWatch metrics. CloudWatch is a monitoring service for AWS resources. You can use CloudWatch to collect and track metrics, set alarms, and automatically react to changes in your AWS resources. 

 The `AWS/CloudTrail` namespace includes the following metrics for CloudTrail Lake. 



| Metric | Description | Units | 
| --- | --- | --- | 
| HourlyDataIngested | The amount of data ingested into the event data store during the last hour. This metric is updated every hour.<br />This metric is available for all event data store types. | Bytes | 
| TotalDataRetained | The amount of data retained in the event data store during its entire retention period. This metric is updated nightly.<br />This metric is available for all event data store types. | Bytes | 
| TotalStorageBytes | The total compressed bytes in the event data store as of the current day.<br />This metric is available for all event data store types. | Bytes | 
| TotalPaidStorageBytes |  For event data stores using the one-year extendable retention [pricing option](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option), this is the total compressed bytes after 366 days to the maximum retention period configured for the event data store.<br />For event data stores using the one-year extendable retention pricing option, storage is included at no additional cost with ingestion pricing for the first 366 days, which is the default retention period for the event data store. After 366 days, storage is pay-as-you-go. For information about pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).<br />This metric is only available for event data stores using the one-year extendable retention pricing option. | Bytes | 
| HourlyEventsAnalyzed | The total number of events analyzed by CloudTrail Insights in the event data store. This metric is updated every hour.<br />This metric is for CloudTrail event data stores that enable CloudTrail Insights. | Count | 

For more information about CloudWatch metrics, see the following topics.
+  [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) 
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) 