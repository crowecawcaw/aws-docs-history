# Troubleshooting

## CloudWatch cannot enable or disable resource tags for telemetry

If you receive an error when trying to enable or disable resource tags for telemetry, verify that the required roles and permissions are correctly configured.

To enable resource tags on telemetry, you must be signed in to an IAM principal that has the `observabilityadmin:StartTelemetryEnrichment`, `iam:CreateServiceLinkedRole`, `resource-explorer-2:CreateIndex`, `resource-explorer-2:CreateManagedView` and `resource-explorer-2:CreateStreamingAccessForService` permissions.

To disable resource tags on telemetry, you must be signed in to an IAM principal that has the `observabilityadmin:StopTelemetryEnrichment` and `resource-explorer-2:DeleteStreamingAccessForService` permissions.

## Telemetry enrichment status is `Impaired`

When the status shows as Impaired, the enable/disable request failed to complete. Retry your request to achieve the desired Running or Stopped status.

## Missing tags after enabling telemetry enrichment

After you enable the feature, CloudWatch begins enriching telemetry with tags. CloudWatch can take up to 3 hours to discover all your tags for enrichment.

## I turned off resource tags for telemetry, I can still see tags enriching my telemetry

After you disable the feature, previously enriched telemetry data remains visible for up to 14 days.
