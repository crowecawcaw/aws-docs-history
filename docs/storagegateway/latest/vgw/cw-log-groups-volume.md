# Getting Volume Gateway health logs with

Amazon CloudWatch Logs

You can use Amazon CloudWatch Logs to get information about the health of your Volume Gateway and
related resources. You can use these logs to monitor your gateway for errors that it
encounters. In addition, you can use Amazon CloudWatch subscription filters to automate processing of
the log information in real time. For more information, see [Real-time Processing of Log Data with
Subscriptions](../../../AmazonCloudWatch/latest/logs/Subscriptions.md "../../../AmazonCloudWatch/latest/logs/Subscriptions.md") in the _Amazon CloudWatch User Guide._

For example, suppose that your gateway is deployed in a cluster activated with VMware High
Availability (HA) and you need to know about any errors. You can configure a CloudWatch log group
to monitor your gateway and get notified when your gateway encounters an error. You can
either configure the group when you are activating the gateway or after your gateway is
activated and up and running. For information about how to configure a CloudWatch log group when
activating a gateway, see [Configure your Volume Gateway](create-volume-gateway.md#configure-gateway-volume "create-volume-gateway.md#configure-gateway-volume"). For general information about CloudWatch log
groups, see [Working with Log Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch User Guide._

For information about how to troubleshoot and fix these types of errors, see [Troubleshooting volume issues](troubleshoot-volume-issues.md "troubleshoot-volume-issues.md").

The following procedure shows you how to configure a CloudWatch log group after your gateway is
activated.

###### To configure a CloudWatch log group to work with your gateway

1. Sign in to the AWS Management Console and open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the left navigation pane, choose **Gateways**, and then choose
   the gateway that you want to configure the CloudWatch log group for.
3. For **Actions**, choose **Edit gateway
   information**, or on the **Details** tab, under
   **Health logs** and **Not Enabled**, choose
   **Configure log group** to open the **Edit
   `CustomerGatewayName`** dialog box.
4. For **Gateway health log group**, choose one of the
   following:
   - **Disable logging** if you don't want to monitor
     your gateway using CloudWatch log groups.
   - **Create a new log group** to create a new CloudWatch log
     group.
   - **Use an existing log group** to use a CloudWatch log group
     that already exists. Choose a log group from the **Existing log
     group list**.

5. Choose **Save changes**.
6. To see the health logs for your gateway, do the following:
   1. In the left navigation pane, choose **Gateways**, and
      then choose the gateway that you configured the CloudWatch log group for.
   2. Choose the **Details** tab, and under **Health
      logs**, choose **CloudWatch Logs**. The
      **Log group details** page opens in the Amazon CloudWatch
      console.
