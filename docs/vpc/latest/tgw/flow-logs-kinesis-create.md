# Create an AWS Transit Gateway Flow Logs record that publishes to Amazon Data Firehose

Create a Transit Gateway Flow Log that publishes to Amazon Data Firehose. Before you can create the flow
log, ensure that you've set up the source and destination IAM account roles for
cross-account delivery and that you've created the Firehose delivery stream. See [Amazon Data Firehose Flow Logs](flow-logs-kinesis.md "flow-logs-kinesis.md") for more information. You can create a Firehose flow log using either the Amazon VPC Console or the AWS CLI.

###### To create a transit gateway flow log that publishes to Firehose using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit gateways** or
   **Transit gateway attachments**.
3. Select the checkboxes for one or more transit gateways or transit gateway attachments.
4. Choose **Actions**, **Create flow
   log**.
5. For **Destination** choose Send to a **Firehose
   Delivery System**.
6. For the **Firehose Delivery Stream ARN**, choose the ARN of a
   delivery stream you created where the flow log is to be published.
7. For **Log record format**, specify the format for the flow
   log record.
   - To use the default flow log record format, choose **AWS
     default format**.
   - To create a custom format, choose **Custom format**.
     For **Log format**, choose the fields to include in the
     flow log record.

8. (Optional) To add a tag to the flow log, choose **Add new
   tag** and specify the tag key and value.
9. Choose **Create flow log**.

###### To create a flow log that publishes to Firehose using the command line tool

Use one of the following commands:

- [create-flow-logs](../../../cli/latest/reference/ec2/create-flow-logs.md "../../../cli/latest/reference/ec2/create-flow-logs.md") (AWS CLI)
- [New-EC2FlowLog](../../../powershell/latest/reference/items/New-EC2FlowLog.md "../../../powershell/latest/reference/items/New-EC2FlowLog.md")
  (AWS Tools for Windows PowerShell)
  The following AWS CLI example creates a flow log that captures transit gateway
  information and delivers the flow log to the specified Firehose delivery
  stream.

```
aws ec2 create-flow-logs \
                --resource-type TransitGateway \
                --resource-ids tgw-1a2b3c4d \
                --log-destination-type kinesis-data-firehose \
                --log-destination arn:aws:firehose:us-east-1:123456789012:deliverystream:flowlogs_stream
```

The following AWS CLI example creates a flow log that captures transit gateway information
and delivers the flow log to a different Firehose delivery stream from the source
account.

```
aws ec2 create-flow-logs  \
  --resource-type TransitGateway \
  --resource-ids gw-1a2b3c4d \
  --log-destination-type kinesis-data-firehose \
  --log-destination arn:aws:firehose:us-east-1:123456789012:deliverystream:flowlogs_stream \
  --deliver-logs-permission-arn arn:aws:iam::source-account:role/mySourceRole \
  --deliver-cross-account-role arn:aws:iam::destination-account:role/AWSLogDeliveryFirehoseCrossAccountRole
```
