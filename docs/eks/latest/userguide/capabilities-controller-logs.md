

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Access EKS Capabilities controller logs
<a name="capabilities-controller-logs"></a>

EKS Capabilities controllers for ACK, kro, and Argo CD run in AWS-managed infrastructure outside your clusters. You can configure log delivery for these controllers using Amazon CloudWatch Vended Logs, giving you visibility into controller behavior for monitoring and troubleshooting.

Logs are delivered in structured JSON format and include operational fields such as log level, message, controller name, and reconciliation identifiers. Internal AWS metadata is filtered before delivery — you receive only the operational log content relevant to your capability controllers.

## Supported log types
<a name="_supported_log_types"></a>

Each capability has one or more log types that you can configure independently as CloudWatch Vended Logs delivery sources.

 **ACK** 
+  **EKS\_CAPABILITY\_ACK\_LOGS** 

 **kro** 
+  **EKS\_CAPABILITY\_KRO\_LOGS** 

 **Argo CD** 
+  **EKS\_CAPABILITY\_ARGOCD\_APPLICATION\_LOGS** 
+  **EKS\_CAPABILITY\_ARGOCD\_APPLICATIONSET\_LOGS** 
+  **EKS\_CAPABILITY\_ARGOCD\_COMMITSERVER\_LOGS** 
+  **EKS\_CAPABILITY\_ARGOCD\_REPOSERVER\_LOGS** 
+  **EKS\_CAPABILITY\_ARGOCD\_SERVER\_LOGS** 

ACK uses a single log type covering all ACK service controllers. Log records include a `controllerGroup` field (for example, `s3.services.k8s.aws`, `rds.services.k8s.aws`) that identifies which ACK service controller generated the log. You can use this field to filter logs for a specific service controller in CloudWatch Logs Insights or other query tools.

Argo CD has five separate log types, one per controller component. This lets you enable logging for only the controllers you need and route them to different destinations.

## Setting up log delivery
<a name="_setting_up_log_delivery"></a>

To configure capability controller log delivery, use the AWS Management Console or the Amazon CloudWatch Logs API. For detailed setup instructions, see [Enabling logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions-V2.html) in the Amazon CloudWatch Logs User Guide. Each capability controller can be configured as an individual CloudWatch Vended Logs delivery source, so you can select which logs to receive.

### Console
<a name="_console"></a>

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home\#/clusters.

1. Select your cluster name.

1. Choose the **Capabilities** tab, then select your capability.

1. In the **Log delivery** section, choose **Add**.

1. Select the log type for your capability and choose a destination.

1. Choose **Add** to create the delivery.

### Using Amazon CloudWatch APIs
<a name="_using_amazon_cloudwatch_apis"></a>

Setting up logging requires three steps:

1. Create a delivery source for the capability using the CloudWatch `PutDeliverySource` API. Use the capability ARN as the `resourceArn` and specify the desired log type.

1. Create a delivery destination using `PutDeliveryDestination`. Specify the ARN of a CloudWatch log group, S3 bucket, or Amazon Data Firehose delivery stream.

1. Create a delivery to connect the source and destination using `CreateDelivery`.

You can retrieve the capability ARN using the `describe-capability` command:

```
aws eks describe-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name {{my-capability}} \
  --query 'capability.capabilityArn' --output text
```

You can configure a single capability (delivery source) to send logs to multiple destinations by creating multiple deliveries. You can also send logs from multiple capabilities to the same destination.

### IAM permissions
<a name="_iam_permissions"></a>

Depending on the destination selected, you might need to configure IAM policies or roles for the CloudWatch log group, S3 bucket, or Data Firehose delivery stream to ensure successful log delivery. If you’re sending logs across AWS accounts, use the `PutDeliveryDestinationPolicy` API to configure an IAM policy that allows delivery to the destination. See the [CloudWatch Vended Logs permissions documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-V2-CloudWatchLogs) for additional information.

## Example: Querying logs with CloudWatch Logs Insights
<a name="_example_querying_logs_with_cloudwatch_logs_insights"></a>

To view error logs across all controllers:

```
fields @timestamp, controller, message, error
| filter level = "error"
| sort @timestamp desc
| limit 50
```

For more query examples including filtering by service controller, tracking reconciliation cycles, and Argo CD application filtering, see [Use controller logs for troubleshooting](capabilities-troubleshooting.md).

## Viewing your logs
<a name="_viewing_your_logs"></a>

After you configure log delivery, logs are delivered to your specified destination. The method for accessing logs depends on your chosen destination type:
+  **CloudWatch Logs** — View logs in the CloudWatch Logs console, use AWS CLI commands, or query with CloudWatch Logs Insights.
+  **Amazon S3** — Access logs as objects in your S3 bucket through the S3 console, AWS CLI, or analytics tools like Amazon Athena.
+  **Amazon Data Firehose** — Logs are streamed to your configured Firehose target (such as S3, OpenSearch Service, Redshift, etc).

## Pricing
<a name="_pricing"></a>

CloudWatch Vended Logs charges apply for log delivery and storage based on your chosen delivery destination. CloudWatch Vended Logs enables reliable, secure log delivery with built-in AWS authentication and authorization at a reduced price compared to standard CloudWatch Logs. See the [Vended Logs section of the CloudWatch pricing page](https://aws.amazon.com/cloudwatch/pricing/) for more details.