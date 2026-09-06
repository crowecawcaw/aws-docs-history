

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Access AWS-Managed Component Logs For EKS Auto
<a name="auto-managed-component-logs"></a>

You can access AWS-managed component logs from EKS Auto Mode to gain deeper observability into your cluster operations. EKS Auto Mode supports logs for the following sources:
+ Compute autoscaling - Karpenter
+ Block storage - EBS CSI
+ Load balancing - AWS Load Balancer Controller
+ Pod networking - VPC CNI IP Address Management

Logs can be delivered to a [delivery destination](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) of your choice.

When you create an EKS Auto Mode cluster, you have the option to enable control plane logging (API server, Audit, Authenticator, Controller manager, Scheduler). EKS Auto managed component logs (such as Compute, Block storage, Load balancing, and IPAM) require separate configuration through log delivery.

## Setting up log delivery
<a name="_setting_up_log_delivery"></a>

To configure AWS-managed component log delivery for your EKS Auto Mode cluster, use the Amazon CloudWatch Logs API. For detailed setup instructions, see [Enabling logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions-V2.html) in the Amazon CloudWatch Logs User Guide. Each Auto Mode capability can be configured as an individual CloudWatch Vended Logs delivery source, allowing you to select which logs you’d like to have access to.

EKS Auto Mode supports the following log types:
+  **AUTO\_MODE\_COMPUTE\_LOGS** 
+  **AUTO\_MODE\_BLOCK\_STORAGE\_LOGS** 
+  **AUTO\_MODE\_LOAD\_BALANCING\_LOGS** 
+  **AUTO\_MODE\_IPAM\_LOGS** 

### Using Amazon CloudWatch APIs
<a name="_using_amazon_cloudwatch_apis"></a>

Setting up logging requires three steps:

1. Create a delivery source for the capability using the CloudWatch PutDeliverySource API

1. Create a delivery destination using PutDeliveryDestination

1. Create a delivery to connect the source and destination using CreateDelivery

You can configure the details of the destination for Auto Mode’s logs using the deliveryDestinationConfiguration object in the CloudWatch PutDeliveryDestination API. It takes the ARN of either a CloudWatch log group, S3 bucket, or Amazon Data Firehose delivery stream.

You can configure a single Auto Mode capability (delivery source) to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

### IAM permissions
<a name="_iam_permissions"></a>

Depending on the destination selected, you may need to configure IAM Policies or Roles for the CloudWatch log group, S3 bucket, and Amazon Data Firehose to ensure successful log delivery. Additionally, if you’re sending logs across AWS accounts, you’ll need to use the PutDeliveryDestinationPolicy API to configure an IAM policy that allows delivery to the destination. See the [CloudWatch Vended Logs permissions documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-V2-CloudWatchLogs) for additional information.

## Viewing your logs
<a name="_viewing_your_logs"></a>

Once log delivery is configured, logs will be delivered to your specified destination. The method for accessing logs depends on your chosen destination type:
+  **CloudWatch Logs** - View logs in the CloudWatch Logs console, use AWS CLI commands, or query with CloudWatch Logs Insights
+  **Amazon S3** - Access logs as objects in your S3 bucket through the S3 console, AWS CLI, or analytics tools like Amazon Athena
+  **Amazon Data Firehose** - Logs are streamed to your configured Firehose target (such as S3, OpenSearch Service, Redshift, etc)

## Pricing
<a name="_pricing"></a>

CloudWatch Vended Logs charges apply for log delivery and storage based on your chosen delivery destination. CloudWatch Vended Logs enables reliable, secure log delivery with built-in AWS authentication and authorization at a reduced price compared to standard CloudWatch Logs. See the [Vended Logs section of the CloudWatch pricing page](https://aws.amazon.com/cloudwatch/pricing/) for more details.

### Related Resources
<a name="_related_resources"></a>
+  [Amazon EKS control plane logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) 
+  [PutDeliverySource API](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) in the CloudWatch Logs API Reference
+  [PutDeliveryDestination API](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html) in the CloudWatch Logs API Reference
+  [CreateDelivery API](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) in the CloudWatch Logs API Reference