# Enable or disable Verified Access logs

You can use the procedures in this section to enable or disable logging. When you
enable logging, you need to configure a destination for the logs to be sent. The IAM
principal that is used to configure the logging destination needs to have certain
permissions for logging to work properly. The required IAM permissions for each
logging destination can be seen in the [Verified Access logging permissions](access-logs-permissions.md "access-logs-permissions.md") section.

###### Contents

- [Enable access logs](#enable-access-logs "#enable-access-logs")
- [Disable access logs](#disable-access-logs "#disable-access-logs")

## Enable access logs

###### To enable Verified Access logs

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access
   instances**.
3. Select the Verified Access instance.
4. On the **Verified Access instance logging configuration** tab,
   choose **Modify Verified Access instance logging
   configuration**.
5. (Optional) To include trust data sent from trust providers in the logs, do the following:
   1. Select **ocsf-1.0.0-rc.2** from the **Update log
      version** drop-down list.
   2. Choose **Include trust context**.

6. Do one of the following:
   - Turn on **Deliver to Amazon CloudWatch Logs**. Choose the destination log group.
   - Turn on **Deliver to Amazon S3**. Enter the name, owner, and prefix of
     the destination bucket.
   - Turn on **Deliver to Firehose**. Choose the destination delivery stream.

7. Choose **Modify Verified Access instance logging
   configuration**.

###### To enable Verified Access logs using the AWS CLI

Use the [modify-verified-access-instance-logging-configuration](../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md "../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md") command.

## Disable access logs

You can disable access logs for your Verified Access instance at any time. After you disable
access logs, your log data remains in your log destination until you delete
it.

###### To disable Verified Access logs

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access
   instances**.
3. Select the Verified Access instance.
4. On the **Verified Access instance logging configuration** tab,
   choose **Modify Verified Access instance logging
   configuration**.
5. Turn off log delivery.
6. Choose **Modify Verified Access instance logging
   configuration**.

###### To disable Verified Access logs using the AWS CLI

Use the [modify-verified-access-instance-logging-configuration](../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md "../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md") command.
