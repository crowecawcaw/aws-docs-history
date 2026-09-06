

# Failed records (FailedRowCount greater than 0)
<a name="msk-data-delivery-iceberg-ts-failed-records"></a>
+ **Symptom:** `FailedRowCount`, or `DLQDeliverySuccess`, is greater than 0.
+ **Causes:** Data is not produced with a GSR-integrated producer when the Channel is created with `JSON_SCHEMA_GSR`; or records do not conform to the registered schema (for example, a missing required field, a type mismatch, or malformed data). Transient permission or connectivity issues are retried and do not count as failed records.
+ **Resolution:** Inspect the DLQ entries and Amazon CloudWatch Logs for the failure reason, then fix the producer data or the registered schema so records conform.