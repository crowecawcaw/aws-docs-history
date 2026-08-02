# Failed records (FailedRowCount / FailedRecordCount greater than 0)

- **Symptom:** `FailedRowCount` (Iceberg) or `FailedRecordCount` (S3), or `DLQDeliverySuccess`, is greater than 0.
- **Causes:**

  - **For Iceberg destinations:** Data is not produced with a GSR-integrated producer when the Channel is created with `JSON_SCHEMA_GSR`; or records do not conform to the registered schema (for example, a missing required field, a type mismatch, or malformed data). Transient permission or connectivity issues are retried and do not count as failed records.
  - **For S3 destinations:** The record format does not conform to the configured source data type.

- **Resolution:** Inspect the DLQ entries and Amazon CloudWatch Logs for the failure reason, then fix the producer data or the registered schema so records conform.
