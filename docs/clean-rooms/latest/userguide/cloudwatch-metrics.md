# Detailed monitoring with CloudWatch in AWS Clean Rooms

_Detailed monitoring_ is an opt-in feature in AWS Clean Rooms.
When you [create a collaboration](create-collaboration.md "create-collaboration.md") and turn on
**Detailed monitoring**, members who can run queries and configured payors
can choose to receive detailed observability metrics in their CloudWatch account.

With detailed monitoring, members can monitor query performance, track resource
utilization, and create dashboards for operational insights. These metrics help with capacity
planning, cost analysis, and troubleshooting performance issues.

###### Note

Metric availability varies based on configured table data sources:

- For analyses that reference configured tables with Athena as the data source, the
  `BytesRead` and `QueryFileScanned` metrics always return

0.

- For analyses that reference configured tables with Snowflake as the data source, the
  `BytesRead`, `QueryFileScanned`, and `RecordsRead`
  metrics always return 0.
- For analyses that reference multiple configured tables with different data sources
  (e.g., Snowflake and S3-backed AWS Glue tables), `BytesRead` and
  `QueryFileScanned` return metrics only for S3-backed AWS Glue tables.
  `RecordsRead` returns metrics for S3-backed AWS Glue tables and Athena tables.

## Types of metrics

AWS Clean Rooms publishes two categories of metrics to CloudWatch:

### Aggregated detailed monitoring metrics

These metrics provide aggregate-level visibility across analyses:

`AnalysisRuntime`

Shows the total duration of an analysis in milliseconds.

`CRPUConsumed`

The CRPU (Clean Room Processing Units) consumed for a particular analysis.
For more information about CRPU calculation, see [AWS Clean Rooms Pricing](https://aws.amazon.com/clean-rooms/pricing/ "https://aws.amazon.com/clean-rooms/pricing/").

`ConcurrentVCPUs`

Concurrent vCPU utilized at a given point in time (related to service quotas).

`AnalysesCount`

Number of analyses run over a period of time for a specified dimension.

`ConcurrentQueries`

Concurrent query count at a given point in time (related to service quotas).

### Query-level detailed monitoring metrics

These metrics provide detailed insights into individual query execution:

`BytesRead`

Total data (in bytes) read from source tables for an analysis.

`BytesWritten`

Total data (in bytes) written for an analysis.

`RecordsRead`

Total number of records read from source tables for an analysis.

`RecordsWritten`

Total number of records returned in the analysis result.

`QueryFileScanned`

Total number of data files scanned for an analysis.

`Memory utilization`

Memory resource used for an analysis.

`vCPU utilization`

vCPU resource used for an analysis.

`Disk utilization`

Storage resource used for an analysis.

## Metric dimensions

Metrics are organized by the following dimensions:

- **Analysis Status**: Completed
- **Analysis Type**: SparkSQL
- **Membership**: The membership ID
- **Query**: Individual query ID (for query-level
  metrics)
- **Account/Region**: Your AWS account and Region

All metrics are published to the `AWS/CleanRooms` namespace in CloudWatch.

## Who can access metrics

Detailed monitoring metrics are available to:

- **Query runners**: Members who can run queries in the
  collaboration
- **Configured payors**: Members designated to pay for
  query execution costs

Members who only contribute data cannot access detailed monitoring metrics.

## Pricing

AWS Clean Rooms does not charge for publishing metrics to CloudWatch. However, standard CloudWatch
charges apply for metric storage, dashboard usage, and alarms. For more information, see
[Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
