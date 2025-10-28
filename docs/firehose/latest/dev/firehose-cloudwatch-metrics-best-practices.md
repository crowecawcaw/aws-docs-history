# Implement best practices

with CloudWatch Alarms

Add CloudWatch alarms for when the following metrics exceed the buffering limit (a maximum
of 15 minutes).

- `DeliveryToS3.DataFreshness`
- `DeliveryToIceberg.DataFreshness`
- `DeliveryToSplunk.DataFreshness`
- `DeliveryToAmazonOpenSearchService.DataFreshness`
- `DeliveryToAmazonOpenSearchServerless.DataFreshness`
- `DeliveryToHttpEndpoint.DataFreshness`
  Also, create alarms based on the following metric math expressions.

- ``IncomingBytes` (Sum per 5 Minutes) / 300`approaches a percentage of`BytesPerSecondLimit`.
- ``IncomingRecords` (Sum per 5 Minutes) / 300`approaches a percentage of`RecordsPerSecondLimit`.
- ``IncomingPutRequests` (Sum per 5 Minutes) / 300` approaches a percentage of`PutRequestsPerSecondLimit`.
Another metric for which we recommend an alarm is
 `ThrottledRecords`.

For information about troubleshooting when alarms go to the `ALARM`
state, see [Troubleshoot errors in Amazon Data Firehose](troubleshooting.md "troubleshooting.md").
