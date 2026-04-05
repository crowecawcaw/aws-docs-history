# Enabling vended metrics in PromQL

You can enable OTel enrichment to make vended metrics for [supported AWS resources](UsingResourceTagsForTelemetry.md "UsingResourceTagsForTelemetry.md") queryable via PromQL. Once enabled, metrics that contain a
resource identifier dimension (for example, EC2 CPUUtilization with an InstanceId dimension) are
enriched with resource ARN and resource tag labels and become queryable using PromQL.

The enriched metric preserves the original metric name and CloudWatch dimensions, and adds:

- **Resource attributes** – the resource ARN
  (`cloud.resource_id`), cloud provider, region, and account ID.
- **Instrumentation scope** – identifies the source
  service and marks the metric as OTel-enriched.
- **Resource tags** – any AWS resource tags
  associated with the resource, queryable as PromQL labels.
  The original classic CloudWatch metric is not modified and remains available through existing CloudWatch APIs.

## Enabling OpenTelemetry enrichment for vended metrics

Before you start OTel enrichment, you must [enable resource tags on telemetry](EnableResourceTagsOnTelemetry.md "EnableResourceTagsOnTelemetry.md") for your account.

You can enable OTel enrichment for your account in a specific region using the CloudWatch
console, AWS CLI, or AWS SDK.

You will need permissions for the following operation: `cloudwatch:StartOTelEnrichment`

###### To enable OTel enrichment for AWS metrics (CloudWatch Console)

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **CloudWatch**, then choose **Settings**.
3. In the **Enable OTel Enrichment for AWS Metrics** pane, toggle the feature On.

**AWS CLI**

```
aws cloudwatch start-o-tel-enrichment
```

To enable across multiple regions, invoke the API in each region of interest.

Once enrichment is enabled, you can start querying vended metrics via PromQL. See:
[Querying vended AWS metrics with PromQL](CloudWatch-PromQL-Querying.md#CloudWatch-PromQL-Querying-Vended "CloudWatch-PromQL-Querying.md#CloudWatch-PromQL-Querying-Vended").
