

# Troubleshooting
<a name="ResourceTagsTelemetryTroubleshooting"></a>

## CloudWatch cannot enable or disable resource tags for telemetry
<a name="CannotEnableDisableResourceTags"></a>

If you receive an error when trying to enable or disable resource tags for telemetry, verify that the required roles and permissions are correctly configured.

To enable resource tags on telemetry, you must be signed in to an IAM principal that has the `observabilityadmin:StartTelemetryEnrichment`, `iam:CreateServiceLinkedRole`, `resource-explorer-2:CreateIndex`, `resource-explorer-2:CreateManagedView` and `resource-explorer-2:CreateStreamingAccessForService` permissions.

To disable resource tags on telemetry, you must be signed in to an IAM principal that has the `observabilityadmin:StopTelemetryEnrichment` and `resource-explorer-2:DeleteStreamingAccessForService` permissions.

**Note**  
In the CloudWatch console, you must be signed in to an IAM principal that has the `observabilityadmin:GetTelemetryEnrichmentStatus` permission.

## Telemetry enrichment status is `Impaired`
<a name="TelemetryEnrichmentStatusImpaired"></a>

When the status shows as Impaired, the enable/disable request failed to complete. Retry your request to achieve the desired Running or Stopped status.

## Missing tags after enabling telemetry enrichment
<a name="CannotSeeAllTags"></a>

After you enable the feature, CloudWatch begins enriching telemetry with tags. CloudWatch can take up to 3 hours to discover all your tags for enrichment.

## I turned off resource tags for telemetry, I can still see tags enriching my telemetry
<a name="StillSeeTagsAfterDisabling"></a>

After you disable the feature:
+ Metrics previously enriched with resource tags can still be discovered for up to 14 days.
+ Logs previously enriched with resource tags can still be queried until the log group's retention period expires.