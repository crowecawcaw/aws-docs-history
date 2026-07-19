# Viewing CloudWatch logs for capacity providers

You can view Amazon CloudWatch Logs logs for your capacity provider using the Lambda console, the CloudWatch console, or the AWS Command Line Interface (AWS CLI). Follow the instructions in the following sections to access your capacity provider's logs.

## Stream logs with CloudWatch Logs Live Tail

Amazon CloudWatch Logs Live Tail helps you quickly troubleshoot your capacity providers by displaying a streaming list of new log events in real time. You can view and filter ingested logs from your capacity provider, helping you to detect and resolve issues quickly.

###### Note

Live Tail sessions incur costs by session usage time, per minute. For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

To start a Live Tail session, open your capacity provider's log group in the CloudWatch console and choose **Live Tail**. For more information, see [Use Live Tail to view logs in near real time](../../../AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.md "../../../AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.md") in the _Amazon CloudWatch User Guide_.

## View logs in the Lambda console

###### To view logs in the Lambda console

1. Open the [Capacity providers page](https://console.aws.amazon.com/lambda/home#/capacity-providers "https://console.aws.amazon.com/lambda/home#/capacity-providers") of the Lambda console.
2. Choose a capacity provider.
3. Choose the **Monitor** tab.
4. Choose **View logs in CloudWatch** to open the log group in the CloudWatch console.

## View logs in the CloudWatch console

###### To view logs in the CloudWatch console

1. Open the CloudWatch console at [console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, then **Log groups**.
3. Choose the log group for your capacity provider. By default, the log group is named `/aws/lambda/capacity-provider/`<capacity-provider-name>``.
4. Choose a log stream to view the log events.

## View logs with the AWS CLI

To view logs using the AWS CLI, use the `aws logs` commands. The following example retrieves the most recent log events for a capacity provider:

```
`aws logs get-log-events \
 --log-group-name /aws/lambda/capacity-provider/`my-capacity-provider` \
 --log-stream-name `my-capacity-provider`/managed-instances`
```

You can also use CloudWatch Logs Insights to query and analyze your capacity provider system logs. The following example queries for all ERROR level events:

```
`aws logs start-query \
 --log-group-name /aws/lambda/capacity-provider/`my-capacity-provider` \
 --start-time $(date -d '1 hour ago' +%s) \
 --end-time $(date +%s) \
 --query-string 'fields @timestamp, @message | filter level = "ERROR" | sort @timestamp desc'`
```
