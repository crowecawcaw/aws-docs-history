# Direct queries in Amazon Managed Service for Prometheus

You can use Amazon OpenSearch Service to directly query operational metrics stored in Amazon Managed Service for Prometheus. This integration allows you to analyze and visualize your Prometheus time-series data alongside your logs and traces within OpenSearch UI, enabling a unified observability experience.

Unlike storage-based direct queries (such as Amazon S3 or CloudWatch Logs), the Prometheus integration uses a live-call architecture. OpenSearch Service acts as a direct client, translating your queries and making live API calls to your Prometheus workspace. Because OpenSearch Service does not provision temporary compute to scan data, you do not incur OpenSearch Compute Unit (OCU) charges for these queries.

To set up and use this integration, you must first create the data source and then configure your workspaces to query the data.

###### Topics

- [Creating an Amazon Managed Service for Prometheus data source](direct-query-prometheus-creating.md "direct-query-prometheus-creating.md")
- [Querying Prometheus metrics](direct-query-prometheus-configure.md "direct-query-prometheus-configure.md")
- [Pricing](#direct-query-prometheus-pricing "#direct-query-prometheus-pricing")
- [Limitations](#direct-query-prometheus-limitations "#direct-query-prometheus-limitations")
- [Recommendations](#direct-query-prometheus-recommendations "#direct-query-prometheus-recommendations")
- [Quotas](#direct-query-prometheus-quotas "#direct-query-prometheus-quotas")
- [Supported AWS Regions](#direct-query-prometheus-regions "#direct-query-prometheus-regions")

## Pricing

For Amazon Managed Service for Prometheus, OpenSearch Service makes live calls directly to your Prometheus workspace to fetch data. Because OpenSearch Service does not provision separate compute resources to execute these queries, you do not incur OpenSearch Compute Unit (OCU) charges. You are only responsible for the standard querying costs associated with Amazon Managed Service for Prometheus.

For more information, see the Direct Query and Serverless sections within [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").

## Limitations

The following limitations apply to direct queries in Amazon Managed Service for Prometheus:

- **Time range constraints** – Live queries are optimized for operational dashboards. Querying highly granular, non-downsampled metrics over very long time horizons (for example, spanning multiple months) might hit payload size limits or result in timeouts from the Prometheus API.
- **Prometheus API quotas** – Your queries are subject to the standard Amazon Managed Service for Prometheus service quotas, including limits on Query Samples Processed (QSP) and concurrent query execution.
- **Query timeout** – Long-running queries time out after 30 seconds.

## Recommendations

We recommend the following when using direct queries in Amazon Managed Service for Prometheus:

- **Use recording rules for long time ranges** – Because direct queries make live API calls to your workspace, querying highly granular data over long periods (such as multiple months) can result in API timeouts or payload limits. Use Amazon Managed Service for Prometheus recording rules to create downsampled metrics for historical analysis.
- **Apply narrow time filters** – Always specify a targeted time range in your OpenSearch UI queries to minimize the volume of data fetched dynamically from the Prometheus API.
- **Monitor your Prometheus quotas** – Because these live queries do not incur OpenSearch Compute Unit (OCU) charges, monitor your Amazon Managed Service for Prometheus usage instead. Monitor your Query Samples Processed (QSP) and concurrent query limits to avoid throttling at the workspace level.

## Quotas

Unlike other direct query data sources, each time you initiate a query to Amazon Managed Service for Prometheus, OpenSearch Service makes a live call to Amazon Managed Service for Prometheus. No sessions are created. The following quotas are applicable per account and Region. For example, an account is allotted 20 data sources in us-east-1 and 20 in us-east-2.

| Description                                                          | Maximum | Can override |
| -------------------------------------------------------------------- | ------- | ------------ |
| Data sources                                                         | 20      | Yes          |
| Execute queries – instant and range queries (TPS)                    | 500     | Yes          |
| Read resources – labels, metrics, alerts, rules, alert manager (TPS) | 50      | Yes          |
| Write resources – create/update silence, create/update rule (TPS)    | 50      | Yes          |
| Maximum query execution time (seconds)                               | 30      | No           |

## Supported AWS Regions

The following AWS Regions are supported for direct queries in Amazon Managed Service for Prometheus:

- Asia Pacific (Hong Kong)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Spain)
- Europe (Stockholm)
- South America (São Paulo)
- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
