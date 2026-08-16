# AWS vended metrics in OpenTelemetry format

###### Tip

To learn more about OpenTelemetry on CloudWatch, check out the
[Cloud Operations Enablement workshop and event series](https://aws-experience.com/amer/smb/events/series/Cloud-Operations-Enablement "https://aws-experience.com/amer/smb/events/series/Cloud-Operations-Enablement").

You can enable OTel enrichment to make vended metrics for [supported AWS resources](UsingResourceTagsForTelemetry.md "UsingResourceTagsForTelemetry.md") queryable through PromQL. After you enable OTel enrichment, metrics that contain a
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
console, AWS CLI, CloudFormation, Terraform, or AWS SDK.

You will need permissions for the following operation: `cloudwatch:StartOTelEnrichment`

###### To enable OTel enrichment for AWS metrics (CloudWatch Console)

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **CloudWatch**, then choose **Settings**.
3. In the **Enable OTel Enrichment for AWS Metrics** pane, toggle the feature On.

**AWS CLI**

```
aws cloudwatch start-otel-enrichment
```

**CloudFormation**

###### Note

The `AWS::CloudWatch::OTelEnrichment` resource requires the
`AWS::ObservabilityAdmin::TelemetryEnrichment` resource to be configured
first. For more information, see [enable resource tags on telemetry](EnableResourceTagsOnTelemetry.md "EnableResourceTagsOnTelemetry.md").

```
Resources:
  TelemetryEnrichmentExample:
    Type: AWS::ObservabilityAdmin::TelemetryEnrichment
  OTelEnrichmentExample:
    Type: AWS::CloudWatch::OTelEnrichment
    DependsOn: TelemetryEnrichmentExample
```

**Terraform**

###### Note

The `aws_cloudwatch_otel_enrichment` Terraform resource requires the
`aws_observabilityadmin_telemetry_enrichment` resource to be configured first.

```
resource "aws_observabilityadmin_telemetry_enrichment" "example" {
}

resource "aws_cloudwatch_otel_enrichment" "example" {
  depends_on = [aws_observabilityadmin_telemetry_enrichment.example]
}
```

For more information, see [aws\_cloudwatch\_otel\_enrichment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_otel_enrichment "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_otel_enrichment") in the Terraform Registry.

To enable across multiple regions, create the same resource in each regional stack or invoke the API in each region of interest.

After enrichment is enabled, you can start querying vended metrics through PromQL. See:
[Querying vended AWS metrics with PromQL](CloudWatch-PromQL-Querying.md#CloudWatch-PromQL-Querying-Vended "CloudWatch-PromQL-Querying.md#CloudWatch-PromQL-Querying-Vended").
