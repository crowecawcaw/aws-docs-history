

# Summary
<a name="service-managed-pk-kpl-summary"></a>


**KPL and KCL compatibility summary**  

| Scenario | Action required | Details | 
| --- | --- | --- | 
| Send records with null partition key | Upgrade KPL | Upgrade to the latest KPL version to support sending records without a partition key | 
| Send records with partition key (existing behavior) | No changes | Existing KPL works as-is. The service ignores the partition key on service-managed streams | 
| KCL consumers | No changes | KCL works as-is regardless of how records were produced | 
| Upgraded KPL producers | Grant kinesis:DescribeStreamSummary | The updated KPL calls DescribeStreamSummary to detect service-managed streams. Without this permission, the KPL falls back to aggregating. Aggregation is not supported on service-managed streams, so the aggregated records that are written can be silently dropped by KCL consumers during de-aggregation. | 
| KPL aggregation on service-managed streams | Not supported | Aggregation is not supported on service-managed streams in any KPL version. Aggregated records that are written can be silently dropped by KCL consumers during de-aggregation. Disable aggregation or upgrade the KPL. | 