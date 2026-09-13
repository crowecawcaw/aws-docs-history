

# Verify execution log delivery
<a name="rest-api-verify-log-delivery"></a>

After you create a log delivery, verify that the delivery is active and that execution logs are arriving at your destination.

To confirm a delivery is active, use the `describe-deliveries` command:

```
aws logs describe-deliveries
```

Then send a test request and check your destination:

1. Send a test request to your REST API.

   ```
   curl https://{{{rest-api-id}}}.execute-api.{{{region}}}.amazonaws.com/{{{stage}}}/{{{resource}}}
   ```

1. Wait 1–2 minutes for logs to propagate.

1. Check your destination for log events:
   + **CloudWatch Logs** – Open the CloudWatch Logs console and navigate to your log group. You should see a log stream with recent events.
   + **Amazon S3** – Open the Amazon S3 console and navigate to your bucket. Look for objects with a path prefix that includes your REST API ID.
   + **Firehose** – Check the delivery stream metrics in the Firehose console to confirm data is flowing.

## Troubleshooting
<a name="rest-api-verify-log-delivery-troubleshooting"></a>

If logs are not arriving at your destination, check the following:
+ **Logging is enabled** – Confirm that `loggingLevel` is set to `ERROR` or `INFO` on the stage. If logging is `OFF`, no logs are generated regardless of delivery configuration.
+ **Delivery status** – Use the `get-delivery` CLI command to check the delivery status and confirm it is active.

  ```
  aws logs get-delivery --id {{{delivery-id}}}
  ```
+ **Permissions** – Verify that the resource policy on your destination allows Amazon CloudWatch Logs to write to it. For more information, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*.