

# Amazon CloudWatch metrics
<a name="msk-data-delivery-s3-metrics"></a>


| Metric name | Description | Unit | 
| --- | --- | --- | 
| `DeliveryToS3.DataFreshness` | Age of the oldest record delivered; rising values indicate delivery lag or stall. | Seconds | 
| `DeliveryToS3.BytesIn` | Volume read into the delivery path. | Bytes | 
| `DeliveryToS3.BytesProcessed` | Volume processed. | Bytes | 
| `DeliveryToS3.BytesOut` | Volume written to the destination. | Bytes | 
| `DeliveryToS3.RecordCount` | Total records seen. | Count | 
| `DeliveryToS3.SuccessfulRecordCount` | Records delivered successfully. | Count | 
| `DeliveryToS3.FailedRecordCount` | Records that failed delivery; non-zero is the key error signal. | Count | 
| `DeliveryToS3.DeliverySuccess` | Successful delivery operations. | Count | 
| `DeliveryToS3.DLQDeliverySuccess` | Records successfully routed to the dead-letter queue. | Count | 