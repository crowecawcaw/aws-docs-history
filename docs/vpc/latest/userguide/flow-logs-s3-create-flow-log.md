# Create a flow log that publishes to

Amazon S3

After you have created and configured your Amazon S3 bucket, you can create flow logs
for your network interfaces, subnets, and VPCs.

**Prerequisite**

The IAM principal that creates the flow log must be using an IAM role that has
the following permissions, which are required to publish flow logs to the
destination Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:DeleteLogDelivery"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### To create a flow log using the console

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
3. For **Filter**, specify the type of IP traffic data to
   log.
   - **Accept** – Log only accepted
     traffic.
   - **Reject** – Log only rejected
     traffic.
   - **All** – Log accepted and rejected traffic.

4. For **Maximum aggregation interval**, choose the maximum
   period of time during which a flow is captured and aggregated into one flow
   log record.
5. For **Destination**, choose **Send to an Amazon
   S3 bucket**.
6. For **S3 bucket ARN**, specify the Amazon Resource Name
   (ARN) of an existing Amazon S3 bucket. You can optionally include a subfolder.
   For example, to specify a subfolder named `my-logs` in
   a bucket named `my-bucket`, use the following ARN:

`arn:aws:s3:::my-bucket/my-logs/`

The bucket cannot use `AWSLogs` as a subfolder name, as this
is a reserved term.

If you own the bucket, we automatically create a resource policy and
attach it to the bucket. For more information, see [Amazon S3 bucket permissions for flow
logs](flow-logs-s3-permissions.md "flow-logs-s3-permissions.md"). 7. For **Log record format**, specify the format for the
flow log record.

    * To use the default flow log record format, choose **AWS
     default format**.
    * To create a custom format, choose **Custom format**.
     For **Log format**, choose the fields to include in
     the flow log record.

8. For **Additional metadata**, select if you want to include metadata from Amazon ECS in the log format.
9. For **Log file format**, specify the format for the
   log file.
   - **Text** – Plain text. This is the default
     format.
   - **Parquet** – Apache Parquet is a columnar
     data format. Queries on data in Parquet format are 10 to 100 times
     faster compared to queries on data in plain text. Data in Parquet
     format with Gzip compression takes 20 percent less storage space than
     plain text with Gzip compression.

10. (Optional) To use Hive-compatible S3 prefixes, choose **Hive-compatible
    S3 prefix**, **Enable**.
11. (Optional) To partition your flow logs per hour, choose **Every 1 hour
    (60 mins)**.
12. (Optional) To add a tag to the flow log, choose **Add new tag**
    and specify the tag key and value.
13. Choose **Create flow log**.

###### To create a flow log that publishes to Amazon S3 using the command line

Use one of the following commands:

- [create-flow-logs](../../../cli/latest/reference/ec2/create-flow-logs.md "../../../cli/latest/reference/ec2/create-flow-logs.md")
  (AWS CLI)
- [New-EC2FlowLog](../../../powershell/latest/reference/items/New-EC2FlowLog.md "../../../powershell/latest/reference/items/New-EC2FlowLog.md")
  (AWS Tools for Windows PowerShell)
  The following AWS CLI example creates a flow log that captures all traffic for the
  specified VPC and delivers the flow logs to the specified Amazon S3 bucket. The
  `--log-format` parameter specifies a custom format for the flow log records.

```
aws ec2 create-flow-logs --resource-type `VPC` --resource-ids `vpc-00112233344556677` --traffic-type ALL --log-destination-type `s3` --log-destination arn:aws:s3:::`flow-log-bucket`/`custom-flow-logs`/ --log-format '${version} ${vpc-id} ${subnet-id} ${instance-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${tcp-flags} ${type} ${pkt-srcaddr} ${pkt-dstaddr}'
```
