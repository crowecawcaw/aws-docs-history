

# Create an AWS Cloud WAN Flow Logs record that publishes to Amazon Data Firehose

Create a Cloud WAN Flow Log that publishes to Amazon Data Firehose. Before you can create the flow log, create the Firehose delivery stream. If you're delivering to a delivery stream in a different account, also set up the source and destination IAM roles for cross account delivery. See [Amazon Data Firehose Flow Logs](cwan-flow-logs-kinesis.md) for more information. You can create a Firehose flow log using either the Network Manager console or the AWS CLI.

**To create a Cloud WAN flow log that publishes to Firehose using the console**

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Choose either **Core networks** or **Attachments**, and then select one or more core networks or attachments.

1. Choose **Actions**, **Create flow log**.

1. For **Destination** choose Send to a **Firehose Delivery System**.

1. For the **Firehose Delivery Stream ARN**, choose the ARN of a delivery stream you created where the flow log is to be published. 

1. For **Log record format**, specify the format for the flow log record.
   + To use the default flow log record format, choose **AWS default format**.
   + To create a custom format, choose **Custom format**. For **Log format**, choose the fields to include in the flow log record.

1. (Optional) To add a tag to the flow log, choose **Add new tag** and specify the tag key and value.

1. Choose **Create flow log**.

Use one of the following commands.

**To create a flow log that publishes to Firehose using the command line tool**
+ [create-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-flow-logs.html) (AWS CLI)
+ [New-EC2FlowLog](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2FlowLog.html) (AWS Tools for Windows PowerShell)

The following AWS CLI example creates a flow log that captures core network information and delivers the flow log to the specified Firehose delivery stream.

```
aws ec2 create-flow-logs \
                --resource-type CoreNetwork \
                --resource-ids core-network-1a2b3c4d \
                --log-destination-type kinesis-data-firehose \
                --log-destination arn:aws:firehose:us-east-1:123456789012:deliverystream/flowlogs_stream
```

The following AWS CLI example creates a flow log that captures core network information and delivers the flow log to a different Firehose delivery stream from the source account.

```
aws ec2 create-flow-logs  \
  --resource-type CoreNetwork \
  --resource-ids core-network-1a2b3c4d \
  --log-destination-type kinesis-data-firehose \
  --log-destination arn:aws:firehose:us-east-1:123456789012:deliverystream/flowlogs_stream \
  --deliver-logs-permission-arn arn:aws:iam::source-account:role/mySourceRole \
  --deliver-cross-account-role arn:aws:iam::destination-account:role/AWSLogDeliveryFirehoseCrossAccountRole
```