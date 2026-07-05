This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Monitoring and management

## CloudWatch dashboards

Complete the following procedure to access CloudWatch dashboards.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, select the network name to
   navigate to that network.
3. In the navigation pane, choose **CloudWatch**.
4. Select **Dashboards**, and then select
   `WickrDataRetentionService-[NetworkID]`.

The deployment automatically creates CloudWatch dashboards showing:

- **Error Rate**: Failed message processing attempts
- **Storage Metrics**: S3 bucket size and object
  count

## Automatic alarms

Pre-configured CloudWatch alarms notify you of:

- **Processing Failures**: Any messages failing to decrypt
  or store

Complete the following procedure to configure alarm notifications.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, select the network name to
   navigate to that network.
3. In the navigation pane, choose **CloudWatch**.
4. Choose **Alarms**.
5. Select a **Wickr Data Retention** alarm.
6. Choose **Actions**, and then choose
   **Edit**.
7. Add SNS topic for email and SMS notifications.
