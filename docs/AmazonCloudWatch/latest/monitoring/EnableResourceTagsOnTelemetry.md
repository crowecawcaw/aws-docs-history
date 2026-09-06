

# Enable resource tags on telemetry
<a name="EnableResourceTagsOnTelemetry"></a>

To add tag information to your telemetry data, enable resource tags for telemetry from the CloudWatch console, AWS SDK, CLI, or CloudFormation. The feature remains active until you turn it off. For more information, see [Disable resource tags on telemetry](DisableResourceTagsOnTelemetry.md).

Make sure you have permissions to enable resource tags for telemetry.

**Note**  
To enable resource tags on telemetry, you must be signed in to an IAM principal that has the `observabilityadmin:StartTelemetryEnrichment`, `iam:CreateServiceLinkedRole`, `resource-explorer-2:CreateIndex`, `resource-explorer-2:CreateManagedView` and `resource-explorer-2:CreateStreamingAccessForService` permissions.

**To enable resource tags for telemetry (CloudWatch Console)**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **CloudWatch**, then choose **Settings**.

1. In the **Enable resource tags for telemetry** pane, toggle the feature On.

**Note**  
In the CloudWatch console, you must be signed in to an IAM principal that has the `observabilityadmin:GetTelemetryEnrichmentStatus` permission.

**To enable resource tags for telemetry (AWS CLI)**  
Use the `start-telemetry-enrichment` command to enable resource tags for telemetry.

```
aws observabilityadmin start-telemetry-enrichment
```

After you complete these steps, CloudWatch begins enriching telemetry with tags.

**To enable resource tags for telemetry (AWS CloudFormation)**  
You can enable resource tags for telemetry by adding an [AWS::ObservabilityAdmin::TelemetryEnrichment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-observabilityadmin-telemetryenrichment.html) resource to your CloudFormation template. Set the `Scope` property to `ACCOUNT` to enable the feature for your account.