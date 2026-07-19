# Monitoring and troubleshooting multilocation canaries

When you create a multilocation canary, CloudWatch Synthetics consolidates run data,
artifacts, and key metrics in the primary Region, giving you a unified view of your
canary's performance across all locations. If the primary Region becomes unavailable, you
can still access run data, metrics, and logs directly in each replica Region.

## Canary runs

In the CloudWatch Synthetics console in the primary Region, you can view canary runs from the
primary and all replica Regions in a single table on the canary detail page. Each run
includes a **Location** column that shows the Region where it was
executed. You can filter runs by location to compare performance and identify issues in
specific Regions.

You can also navigate to the CloudWatch Synthetics console in any replica Region to view runs
that were executed in that Region independently.

## Artifacts

Screenshots, HAR files, and reports from all locations are stored in the same Amazon S3
bucket configured for your canary. Replicas write artifacts directly to the primary
Region's Amazon S3 bucket under a regional prefix, so that you can identify which location
generated them:

- Primary runs:
  `s3://bucket/canary/primaryRegion/canaryName/year/month/day/hour/minute-second-millisecond`
- Replica runs:
  `s3://bucket/canary/primaryRegion/canaryName/year/month/day/hour/replicaRegion/minute-second-millisecond`

Because Amazon S3 buckets are globally accessible, you can retrieve artifacts from any
Region. When you select a run on the canary detail page, the CloudWatch Synthetics console displays
the associated screenshots and reports inline, regardless of which location executed the
run.

## Metrics

Multilocation canaries publish the following metrics to CloudWatch in the primary
Region:

- **SuccessPercent**—Published with a
  `Location` dimension for each Region where the canary runs. An aggregate
  `SuccessPercent` metric without the `Location` dimension
  represents the combined success rate across all locations. To monitor overall canary
  health across all locations, create a CloudWatch alarm on this aggregate metric.
- **Duration**—Published with a
  `Location` dimension for each Region where the canary runs.

All canary metrics are also published in the respective replica Region. If the
primary Region is unavailable, you can navigate to the CloudWatch console in any replica
Region to view metrics for that location.

For a complete list of metrics published by canaries, see [CloudWatch metrics published by canaries](CloudWatch_Synthetics_Canaries_metrics.md "CloudWatch_Synthetics_Canaries_metrics.md").

## Logs

When you select a run on the canary detail page, you can view the associated logs
for that run regardless of which location executed it. This allows you to debug failures
from any location directly in the primary Region.

To centralize canary logs from all Regions into a single CloudWatch Logs view, you can
configure cross-Region log centralization. For more information, see [Using log centralization with multilocation canaries](CloudWatch_Synthetics_MultiLocation_Log_Centralization.md "CloudWatch_Synthetics_MultiLocation_Log_Centralization.md").
