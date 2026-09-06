

# Disable resource tags on telemetry
<a name="DisableResourceTagsOnTelemetry"></a>

If you don't need resource tags for telemetry, disable the feature. When disabled, CloudWatch stops enriching telemetry with tags. You can enable it again at any time. For more information, see [Enable resource tags on telemetry](EnableResourceTagsOnTelemetry.md).

Verify you have permissions to disable resource tags for telemetry.

**Note**  
To disable resource tags on telemetry, you must be signed in to an IAM principal that has the `observabilityadmin:StopTelemetryEnrichment` and `resource-explorer-2:DeleteStreamingAccessForService` permissions.

**To disable resource tags for telemetry (CloudWatch Console)**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **CloudWatch**, then choose **Settings**.

1. In the **Enable resource tags for telemetry** pane, choose **off**.

1. In the confirm modal, read through the consequences of disabling resource tags for telemetry, then type **confirm** and choose **Disable resource tags**.

**Note**  
In the CloudWatch console, you must be signed in to an IAM principal that has the `observabilityadmin:GetTelemetryEnrichmentStatus` permission.

**To disable resource tags for telemetry (AWS CLI)**  
Use the `stop-telemetry-enrichment` command to disable resource tags for telemetry.

```
aws observabilityadmin stop-telemetry-enrichment
```

After you complete these steps, CloudWatch stops enriching telemetry with tags. Metrics previously enriched with resource tags can still be discovered for up to 14 days. Logs previously enriched with resource tags can still be queried until the log group's retention period expires.

**To disable resource tags for telemetry (AWS CloudFormation)**  
If you enabled resource tags for telemetry by using an [AWS::ObservabilityAdmin::TelemetryEnrichment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-observabilityadmin-telemetryenrichment.html) resource, disable the feature by removing that resource from your CloudFormation template and updating the stack.