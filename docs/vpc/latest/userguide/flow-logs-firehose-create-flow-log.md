# Create a flow log that publishes to Amazon Data Firehose

You can create flow logs for your VPCs, subnets, or network interfaces.

###### Prerequisites

- Create the destination Amazon Data Firehose delivery stream. Use **Direct Put**
  as the source. For more information, see [Creating an Amazon Data Firehose delivery stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md").
- If you're publishing flow logs to a different account, create the required IAM roles,
  as described in [IAM roles for cross account delivery](firehose-cross-account-delivery.md "firehose-cross-account-delivery.md").

###### To create a flow log that publishes to Amazon Data Firehose

1. Do one of the following:
   - Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
     In the navigation pane, choose **Network Interfaces**.
     Select the checkbox for the network interface.
   - Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
     In the navigation pane, choose **Your VPCs**.
     Select the checkbox for the VPC.
   - Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
     In the navigation pane, choose **Subnets**.
     Select the checkbox for the subnet.

2. Choose **Actions**, **Create flow log**.
3. For **Filter**, specify the type of traffic to log.
   - **Accept** – Log only accepted traffic
   - **Reject** – Log only rejected traffic
   - **All** – Log accepted and rejected traffic

4. For **Maximum aggregation interval**, choose the maximum
   period of time during which a flow is captured and aggregated into one flow
   log record.
5. For **Destination**, choose either of the following options:
   - **Send to Amazon Data Firehose in the same account** –
     The delivery stream and the resource to monitor are in the same
     account.
   - **Send to Amazon Data Firehose in a different account**
     – The delivery stream and the resource to monitor are in
     different accounts.

6. For **Amazon Data Firehose** stream name, choose the
   delivery stream that you created.
7. [Cross account delivery only] For **Service access**,
   choose an existing [IAM service role for cross account delivery](firehose-cross-account-delivery.md "firehose-cross-account-delivery.md") that has permissions to publish logs or choose **Set up permissions** to open the IAM console and create a service role.
8. For **Log record format**, specify the format for the
   flow log record.
   - To use the default flow log record format, choose **AWS
     default format**.
   - To create a custom format, choose **Custom format**.
     For **Log format**, choose the fields to include in
     the flow log record.

9. For **Additional metadata**, select if you want to include metadata from Amazon ECS in the log format.
10. (Optional) Choose **Add tag** to apply tags to the flow
    log.
11. Choose **Create flow log**.

###### To create a flow log that publishes to Amazon Data Firehose using the command line

Use one of the following commands:

- [create-flow-logs](../../../cli/latest/reference/ec2/create-flow-logs.md "../../../cli/latest/reference/ec2/create-flow-logs.md")
  (AWS CLI)
- [New-EC2FlowLog](../../../powershell/latest/reference/items/New-EC2FlowLog.md "../../../powershell/latest/reference/items/New-EC2FlowLog.md")
  (AWS Tools for Windows PowerShell)
  The following AWS CLI example creates a flow log that captures all traffic for the
  specified VPC and delivers the flow logs to the specified Amazon Data Firehose delivery stream
  in the same account.

```
aws ec2 create-flow-logs --traffic-type ALL \
  --resource-type `VPC` \
  --resource-ids `vpc-00112233344556677` \
  --log-destination-type `kinesis-data-firehose` \
  --log-destination arn:aws:firehose:`us-east-1`:`123456789012`:deliverystream/`flowlogs_stream`
```

The following AWS CLI example creates a flow log that captures all traffic for the
specified VPC and delivers the flow logs to the specified Amazon Data Firehose delivery stream
in a different account.

```
aws ec2 create-flow-logs --traffic-type ALL \
  --resource-type `VPC` \
  --resource-ids `vpc-00112233344556677` \
  --log-destination-type `kinesis-data-firehose` \
  --log-destination arn:aws:firehose:`us-east-1`:`123456789012`:deliverystream/`flowlogs_stream` \
  --deliver-logs-permission-arn arn:aws:iam::`source-account`:role/`mySourceRole` \
  --deliver-cross-account-role arn:aws:iam::`destination-account`:role/AWSLogDeliveryFirehoseCrossAccountRole
```

As a result of creating the flow log, you can get the flow log data from the
destination that you configured for the delivery stream.
