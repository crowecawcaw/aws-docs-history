# Enable resource tags on telemetry

To add tag information to your telemetry data, enable resource tags for telemetry from the CloudWatch console, AWS SDK or CLI. The feature remains active until you turn it off. For more information, see [Disable resource tags on telemetry](DisableResourceTagsOnTelemetry.md "DisableResourceTagsOnTelemetry.md").

Make sure you have permissions to enable resource tags for telemetry.

###### Note

To enable resource tags on telemetry, you must be signed in to an IAM principal that has the `observabilityadmin:StartTelemetryEnrichment`, `iam:CreateServiceLinkedRole`, `resource-explorer-2:CreateIndex`, `resource-explorer-2:CreateManagedView` and `resource-explorer-2:CreateStreamingAccessForService` permissions.

###### To enable resource tags for telemetry (CloudWatch Console)

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **CloudWatch**, then choose **Settings**.
3. In the **Enable resource tags for telemetry** pane, toggle the feature On.

###### Note

In the CloudWatch console, you must be signed in to an IAM principal that has the `observabilityadmin:GetTelemetryEnrichmentStatus` permission.

###### To enable resource tags for telemetry (AWS CLI)

Use the `start-telemetry-enrichment` command to enable resource tags for telemetry.

```
aws observabilityadmin start-telemetry-enrichment
```

After you complete these steps, CloudWatch begins enriching telemetry with tags. CloudWatch can take up to 3 hours to discover all your resource tags for telemetry.
