**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Access AWS-Managed Component Logs For EKS Auto

You can access AWS-managed component logs from EKS Auto Mode to gain deeper observability into your cluster operations. EKS Auto Mode supports logs for the following sources:

- Compute autoscaling - Karpenter
- Block storage - EBS CSI
- Load balancing - AWS Load Balancer Controller
- Pod networking - VPC CNI IP Address Management
  Logs can be delivered to a [delivery destination](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") of your choice.

When you create an EKS Auto cluster, you have the option to enable control plane logging (API server, Audit, Authenticator, Controller manager, Scheduler). EKS Auto managed component logs (such as Compute, Block storage, Load balancing, and IPAM) require separate configuration through log delivery.

## Setting up log delivery

To configure AWS-managed component log delivery for your EKS Auto Mode cluster, use the Amazon CloudWatch Logs API. For detailed setup instructions, see [Enabling logging from AWS services](../../../AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions-V2.md "../../../AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions-V2.md") in the Amazon CloudWatch Logs User Guide. Each Auto Mode capability can be configured as an individual CloudWatch Vended Logs delivery source, allowing you to select which logs you’d like to have access to.

EKS Auto Mode supports the following log types:

- **AUTO_MODE_COMPUTE_LOGS**
- **AUTO_MODE_BLOCK_STORAGE_LOGS**
- **AUTO_MODE_LOAD_BALANCING_LOGS**
- **AUTO_MODE_IPAM_LOGS**

### Using Amazon CloudWatch APIs

Setting up logging requires three steps:

1. Create a delivery source for the capability using the CloudWatch PutDeliverySource API
2. Create a delivery destination using PutDeliveryDestination
3. Create a delivery to connect the source and destination using CreateDelivery

You can configure the details of the destination for Auto Mode’s logs using the deliveryDestinationConfiguration object in the CloudWatch PutDeliveryDestination API. It takes the ARN of either a CloudWatch log group, S3 bucket, or Kinesis Data Firehose delivery stream.

You can configure a single Auto Mode capability (delivery source) to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

### IAM permissions

Depending on the destination selected, you may need to configure IAM Policies or Roles for the CloudWatch log group, S3 bucket, and Kinesis Data Firehose to ensure successful log delivery. Additionally, if you’re sending logs across AWS accounts, you’ll need to use the PutDeliveryDestinationPolicy API to configure an IAM policy that allows delivery to the destination. See the [CloudWatch Vended Logs permissions documentation](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs") for additional information.

## Viewing your logs

Once log delivery is configured, logs will be delivered to your specified destination. The method for accessing logs depends on your chosen destination type:

- **CloudWatch Logs** - View logs in the CloudWatch Logs console, use AWS CLI commands, or query with CloudWatch Logs Insights
- **Amazon S3** - Access logs as objects in your S3 bucket through the S3 console, AWS CLI, or analytics tools like Amazon Athena
- **Amazon Data Firehose** - Logs are streamed to your configured Firehose target (such as S3, OpenSearch Service, Redshift, etc)

## Pricing

CloudWatch Vended Logs charges apply for log delivery and storage based on your chosen delivery destination. CloudWatch Vended Logs enables reliable, secure log delivery with built-in AWS authentication and authorization at a reduced price compared to standard CloudWatch Logs. See the [Vended Logs section of the CloudWatch pricing page](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") for more details.

### Related Resources

- [Amazon EKS control plane logging](control-plane-logs.md "control-plane-logs.md")
- [PutDeliverySource API](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") in the CloudWatch Logs API Reference
- [PutDeliveryDestination API](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") in the CloudWatch Logs API Reference
- [CreateDelivery API](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") in the CloudWatch Logs API Reference
