# Verify and Troubleshoot KMS key

permissions

After enabling encryption on a Kinesis stream, we recommend that you monitor the success
of your `putRecord`, `putRecords`, and `getRecords`
calls using the following Amazon CloudWatch metrics:

- `PutRecord.Success`
- `PutRecords.Success`
- `GetRecords.Success`
  For more information, see [Monitor Kinesis Data Streams](monitoring.md "monitoring.md")
