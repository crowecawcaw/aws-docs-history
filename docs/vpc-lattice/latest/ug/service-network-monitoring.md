# Edit monitoring details for a VPC Lattice

service network

VPC Lattice generates metrics and logs for every request and response, making it more
efficient to monitor and troubleshoot applications.

You can enable access logs and specify the destination resource for your logs.
VPC Lattice can send logs to the following resources: CloudWatch Log groups, Firehose delivery
streams, and S3 buckets.

###### To enable access logs or update a log destination using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Service networks**.
3. Select the name of the service network to open its details page.
4. Choose the **Monitoring** tab. Check **Access
   logs** to see whether access logs are enabled.
5. To enable or disable access logs, choose **Edit access
   logs**, and then turn the **Access logs** toggle
   switch on or off.
6. When you enable access logs, you must select the type of delivery destination,
   and then create or choose the destination for the access logs. You can also
   change the delivery destination at any time. For example:
   - Select **CloudWatch Log group** and choose a
     CloudWatch Log group. To create a log group, choose **Create a
     log group in CloudWatch**.
   - Select **S3 bucket** and enter the S3 bucket path,
     including any prefix. To search your S3 buckets, choose **Browse
     S3**.
   - Select **Kinesis Data Firehose delivery stream** and
     choose a delivery stream. To create a delivery stream, choose
     **Create a delivery stream in Kinesis**.

7. Choose **Save changes**.

###### To enable access logs using the AWS CLI

Use the [create-access-log-subscription](../../../cli/latest/reference/vpc-lattice/create-access-log-subscription.md "../../../cli/latest/reference/vpc-lattice/create-access-log-subscription.md") command.

###### To update the log destination using the AWS CLI

Use the [update-access-log-subscription](../../../cli/latest/reference/vpc-lattice/update-access-log-subscription.md "../../../cli/latest/reference/vpc-lattice/update-access-log-subscription.md") command.

###### To disable access logs using the AWS CLI

Use the [delete-access-log-subscription](../../../cli/latest/reference/vpc-lattice/delete-access-log-subscription.md "../../../cli/latest/reference/vpc-lattice/delete-access-log-subscription.md") command.
