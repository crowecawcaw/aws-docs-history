# Create an AWS Transit Gateway Flow Logs record that publishes

to Amazon S3

After you have created and configured your Amazon S3 bucket, you can create flow logs for
transit gateways. You can create an Amazon S3 flow log using either the Amazon VPC Console or the
AWS CLI.

###### To create a transit gateway flow log that publishes to Amazon S3 using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit gateways** or
   **Transit gateway attachments**.
3. Select the checkboxes for one or more transit gateways or transit gateway attachments.
4. Choose **Actions**, **Create flow
   log**.
5. Configure the flow log settings. For more information, see [To configure flow log
   settings](#configure-flow-log "#configure-flow-log").

###### To configure flow log settings using the console

1. For **Destination**, choose **Send to an S3
   bucket**.
2. For **S3 bucket ARN**, specify the Amazon Resource Name
   (ARN) of an existing Amazon S3 bucket. You can optionally include a subfolder.
   For example, to specify a subfolder named `my-logs` in a
   bucket named `my-bucket`, use the following ARN:

`arn:aws::s3:::my-bucket/my-logs/`

The bucket cannot use `AWSLogs` as a subfolder name, as this is
a reserved term.

If you own the bucket, we automatically create a resource policy and
attach it to the bucket. For more information, see [Amazon S3 bucket permissions for flow
logs](flow-logs-s3.md#flow-logs-s3-permissions "flow-logs-s3.md#flow-logs-s3-permissions"). 3. For **Log record format**, specify the format for the
flow log record.

    * To use the default flow log record format, choose **AWS
     default format**.
    * To create a custom format, choose **Custom
     format**. For **Log format**, choose
     the fields to include in the flow log record.

4. For **Log file format**, specify the format for the log
   file.
   - **Text** – Plain text. This is the default
     format.
   - **Parquet** – Apache Parquet is a columnar
     data format. Queries on data in Parquet format are 10 to 100 times
     faster compared to queries on data in plain text. Data in Parquet
     format with Gzip compression takes 20 percent less storage space
     than plain text with Gzip compression.

5. (Optional) To use Hive-compatible S3 prefixes, choose
   **Hive-compatible S3 prefix**,
   **Enable**.
6. (Optional) To partition your flow logs per hour, choose **Every 1
   hour (60 mins)**.
7. (Optional) To add a tag to the flow log, choose **Add new
   tag** and specify the tag key and value.
8. Choose **Create flow log**.

###### To create a flow log that publishes to Amazon S3 using a command line tool

Use one of the following commands.

- [create-flow-logs](../../../cli/latest/reference/ec2/create-flow-logs.md "../../../cli/latest/reference/ec2/create-flow-logs.md")
  (AWS CLI)
- [New-EC2FlowLog](../../../powershell/latest/reference/items/New-EC2FlowLog.md "../../../powershell/latest/reference/items/New-EC2FlowLog.md")
  (AWS Tools for Windows PowerShell)
  The following AWS CLI example creates a flow log that captures all transit gateway traffic for VPC
  `tgw-00112233344556677` and delivers the flow logs to an Amazon S3 bucket
  called `flow-log-bucket`. The `--log-format` parameter specifies a
  custom format for the flow log records.

```
aws ec2 create-flow-logs --resource-type TransitGateway --resource-ids tgw-00112233344556677 --log-destination-type s3 --log-destination arn:aws:s3:::flow-log-bucket/my-custom-flow-logs/'
```
