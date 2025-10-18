# Disable resource tags on telemetry

If you don't need resource tags for telemetry, disable the feature. When disabled, CloudWatch stops enriching telemetry with tags. You can enable it again at any time. For more information, see [Enable resource tags on telemetry](EnableResourceTagsOnTelemetry.md "EnableResourceTagsOnTelemetry.md").

Verify you have permissions to disable resource tags for telemetry.

###### Note

To disable resource tags on telemetry, you must be signed in to an IAM principal that has the `resource-explorer-2:DeleteStreamingAccessForService` permission.

###### To disable resource tags for telemetry

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **CloudWatch**, then choose **Settings**.
3. In the **Enable resource tags for telemetry** pane, choose **off**.
4. In the confirm modal, read through the consequences of disabling resource tags for telemetry, then type `confirm` and choose **Disable resource tags**.


After you complete these steps, CloudWatch stops enriching telemetry with tags. Telemetry previously enriched with resource tags can still be discovered for up to 14 days after disabling.
