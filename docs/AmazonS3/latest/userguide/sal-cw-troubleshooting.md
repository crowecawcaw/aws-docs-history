

# Troubleshooting CloudWatch Logs delivery
<a name="sal-cw-troubleshooting"></a>

## Logs not appearing in CloudWatch Logs log group
<a name="sal-cw-ts-no-logs"></a>

If you have configured delivery but do not see logs in your CloudWatch Logs log group, check the following:
+ **Verify the delivery is active.** Run `aws logs describe-deliveries` and confirm that your delivery shows a status of `ACTIVE`.
+ **Verify the delivery source.** Run `aws logs describe-delivery-sources` and confirm that the source bucket ARN and log type (`S3_SERVER_ACCESS_LOGS`) are correct.
+ **Confirm the source bucket has traffic.** Server access logs are only generated when requests are made to the source bucket. If the bucket has no traffic, no logs are produced.
+ **Check the log group Region.** The log group must be in the same AWS Region as the source bucket.
+ **Allow time for initial delivery.** After setup, it may take a few minutes for the first logs to appear.

## S3 Tables integration not populating
<a name="sal-cw-ts-no-integration"></a>

If logs appear in CloudWatch Logs but the S3 Tables integration is empty, check the following:
+ **Verify the integration exists.** In the CloudWatch console, go to **Settings**, **Global**, and confirm that an S3 Table Integration is listed.
+ **Verify the source is associated.** Run `aws logs list-sources-for-s3-table-integration --integration-arn {{integration-arn}}` and confirm that your delivery source name and type appear in the list.
+ **Check the service role permissions.** The IAM role used for the integration must have the `logs:integrateWithS3Table` permission scoped to your log group ARN. See [Enabling the S3 Tables integration (optional)](sal-cw-enabling.md#sal-cw-tables-integration).
+ **Confirm the `aws-cloudwatch` table bucket exists.** In the Amazon S3 console, navigate to **Table buckets** and look for the `aws-cloudwatch` bucket. If it does not exist, the integration may not have completed successfully.
+ **Allow time for data to appear.** The integration may lag behind CloudWatch Logs delivery. Data typically appears within an hour of the first delivery to CloudWatch Logs.
+ **Check that the integration processes only new data.** The S3 Tables integration does not backfill logs from before the association was created. Only log events added after the association are delivered to S3 Tables.

## Permission errors
<a name="sal-cw-ts-permissions"></a>

The following are common permission errors and how to resolve them.
+ **Access Denied on `PutDeliverySource`** – The caller needs the `logs:PutDeliverySource` and `s3:AllowVendedLogDeliveryForResource` permission.
+ **Access Denied on `CreateDelivery`** – The caller needs the `logs:CreateDelivery` permission.
+ **Access Denied on `CreateS3TableIntegration`** – The caller needs the `observabilityadmin:CreateS3TableIntegration` permission, plus `s3tables:CreateTableBucket`, `s3tables:PutTableBucketEncryption`, and `s3tables:PutTableBucketPolicy`.
+ **AWS KMS errors on log group** – If your log group uses AWS KMS encryption, verify that the AWS KMS key policy grants access to the CloudWatch Logs service principal. See [Encryption](sal-cw-enabling.md#sal-cw-encryption).
+ **AWS KMS errors on S3 Tables integration** – If your log group uses AWS KMS encryption and the S3 Tables integration is enabled, verify that the AWS KMS key policy grants access to both `systemtables.cloudwatch.amazonaws.com` and `maintenance.s3tables.amazonaws.com`. See [Encryption](sal-cw-enabling.md#sal-cw-encryption).
+ **Access Denied when querying in Athena** – Verify that the IAM principal running the query has permissions to access the `aws-cloudwatch` table bucket and the S3 Tables catalog. If you are using AWS Lake Formation, verify that `SELECT` and `DESCRIBE` grants are in place.

## Delivery stopped unexpectedly
<a name="sal-cw-ts-stopped"></a>

If logs were previously being delivered but have stopped, check the following:
+ **Source bucket deleted.** If the source bucket was deleted, delivery stops. If the bucket is recreated, you must create a new delivery again. 
+ **Log group deleted.** If the log group was deleted, delivery stops. Create a new log group and update the delivery destination.
+ **IAM permissions revoked.** If the permissions required for delivery were removed, delivery may stop. Verify that the delivery configuration still has the required permissions.
+ **Service quotas.** Check CloudWatch Logs service quotas for delivery limits per account. You may have reached the maximum number of deliveries.

## Managing ingestion costs
<a name="sal-cw-ts-cost"></a>

If your CloudWatch Logs ingestion costs are higher than expected, consider the following:
+ **Reduce retention.** Set a shorter retention period on the log group to reduce storage costs. CloudWatch Logs automatically deletes data that exceeds the retention period.
+ **Review source bucket traffic.** High-traffic buckets generate more logs. Consider whether all source buckets need CloudWatch Logs delivery, or whether the free general purpose bucket delivery path is sufficient for some buckets.
+ **Use volume-based pricing.** CloudWatch Logs vended logs ingestion pricing is tiered by volume. Higher volumes receive lower per-GB rates. For current rates, see [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).