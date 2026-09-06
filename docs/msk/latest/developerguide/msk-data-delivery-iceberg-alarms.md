

# Recommended alarms
<a name="msk-data-delivery-iceberg-alarms"></a>


| Alarm | Condition | Recommended threshold | Action | 
| --- | --- | --- | --- | 
| High data freshness | `DeliveryToIceberg.DataFreshness` exceeds threshold | Above your configured freshness | Investigate throughput or service issues | 
| Failed records | `DeliveryToIceberg.FailedRowCount` greater than 0 | > 0 for 5 consecutive minutes | Check IAM permissions, destination bucket access, schema/data compatibility | 
| DLQ deliveries | `DeliveryToIceberg.DLQDeliverySuccess` greater than 0 | > 0 | Inspect DLQ entries for the failure reason | 