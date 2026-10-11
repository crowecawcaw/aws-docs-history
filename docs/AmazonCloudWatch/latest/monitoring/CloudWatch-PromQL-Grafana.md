

# Grafana integration
<a name="CloudWatch-PromQL-Grafana"></a>

After you ingest OpenTelemetry metrics into CloudWatch and make them queryable with PromQL, you can visualize and explore that data in Grafana and Amazon Managed Grafana. We recommend that you use the **PromQL** query type in the **Amazon CloudWatch** data source plugin. It uses the same authentication and Region settings as your other CloudWatch queries, so you don't need to configure a separate data source. For more information, see [Querying with the CloudWatch data source](#CloudWatch-PromQL-Querying-CloudWatch-datasource).

Alternatively, you can connect to the CloudWatch monitoring endpoint through the **Amazon Managed Service for Prometheus** data source plugin, which signs requests with Signature Version 4 (SigV4). Use this option if your Grafana version or Amazon Managed Grafana workspace doesn't support the PromQL query type in the CloudWatch data source. For more information, see [Querying from Grafana with the Amazon Managed Service for Prometheus data source](#CloudWatch-PromQL-Querying-Grafana) and [Querying from Amazon Managed Grafana with the Amazon Managed Service for Prometheus data source](#CloudWatch-PromQL-Querying-AMG).

## Querying with the CloudWatch data source
<a name="CloudWatch-PromQL-Querying-CloudWatch-datasource"></a>

The **Amazon CloudWatch** data source plugin includes a **PromQL** query type, alongside the **Metric Search** and **Metric Insights** query types. The plugin sends SigV4-signed requests to the CloudWatch PromQL endpoint for the selected Region. You don't need to change the data source configuration or set a signing service.

The PromQL query type is available in the following environments:
+ **Amazon Managed Grafana** — workspaces that use Grafana version 13 or later. For more information, see [Grafana version 13](https://docs.aws.amazon.com/grafana/latest/userguide/version-differences.html#version-diff-v13) in the *Amazon Managed Grafana User Guide*.
+ **Grafana** — version 12.10.0 or later of the CloudWatch data source plugin, which includes both the Builder and Code editing modes. The plugin requires Grafana `>=11.6.11 <12 || >=12.0.10 <12.1 || >=12.1.7 <12.2 || >=12.2.5`. To update the plugin, use the Grafana plugins catalog.

**IAM prerequisites** — the IAM principal that the CloudWatch data source uses, such as the Amazon Managed Grafana workspace IAM role, must have both `cloudwatch:GetMetricData` (required for instant and range queries) and `cloudwatch:ListMetrics` (required for metric, label key, and label value autocomplete). For details, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM).

**Note**  
If the IAM principal has only these permissions, choosing **Save & test** on the CloudWatch data source reports an error for the CloudWatch Logs check because it can't call `logs:DescribeLogGroups`. The metrics check still succeeds, and PromQL queries aren't affected. To clear the error, also grant the permissions that the CloudWatch data source needs for logs queries.

To query CloudWatch metrics with PromQL, complete the following steps.

1. Add an **Amazon CloudWatch** data source, or use an existing one. In Amazon Managed Grafana, you can use the AWS data source configuration option to add the data source and manage its credentials. For more information, see [Connect to an Amazon CloudWatch data source](https://docs.aws.amazon.com/grafana/latest/userguide/using-amazon-cloudwatch-in-AMG.html) in the *Amazon Managed Grafana User Guide*.

1. In a dashboard panel or in **Explore**, select the CloudWatch data source.

1. In the query editor, choose **PromQL** as the query type.

1. For **Region**, keep the data source default or choose the AWS Region that contains your OpenTelemetry metrics.

1. Build the query in one of the following editing modes. Use the **Builder**/**Code** toggle to switch between them.
   + **Builder** — select a metric, add label filters, and optionally add operations such as aggregations and functions.
   + **Code** — enter a PromQL expression directly. The editor suggests metric names, label keys, and label values. To build a selector visually, choose **Metrics browser**.

1. (Optional) Under the query options, set **Legend**, **Min step**, **Format** (`Time series` or `Table`), and **Type** (`Range` or `Instant`).

## Querying from Grafana with the Amazon Managed Service for Prometheus data source
<a name="CloudWatch-PromQL-Querying-Grafana"></a>

You can also query CloudWatch PromQL data from Grafana by adding the **Amazon Managed Service for Prometheus** data source plugin and pointing it at the CloudWatch monitoring endpoint. SigV4 signing is built in to the plugin and is always enabled, so there is no toggle to turn on. The plugin is published at [grafana.com/grafana/plugins/grafana-amazonprometheus-datasource/](https://grafana.com/grafana/plugins/grafana-amazonprometheus-datasource/); install it from the Grafana plugins catalog before adding the data source. AMP plugin v3.0.0 requires Grafana `>=11.6.11 <12 || >=12.0.10 <12.1 || >=12.1.7 <12.2 || >=12.2.5`.

**IAM prerequisites** — the IAM principal whose credentials Grafana uses must have both `cloudwatch:GetMetricData` (required for instant and range queries) and `cloudwatch:ListMetrics` (required for series and label discovery). For details, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM).

To configure Grafana, complete the following steps.

1. Install the **Amazon Managed Service for Prometheus** data source plugin from the Grafana plugins catalog.

1. In Grafana, go to **Connections**, **Data sources**, choose **Add data source**, and select **Amazon Managed Service for Prometheus**.

1. Set the data source **URL** to `https://monitoring.{{AWS Region}}.amazonaws.com`.

1. Set the **Region** to your AWS Region. Choose an **Authentication provider** appropriate for your environment (default credential chain, access keys, or workspace IAM role).

1. Set the **Service** field to `monitoring`. The plugin defaults this field to `aps` for Amazon Managed Service for Prometheus, but the CloudWatch PromQL endpoint requires `monitoring`.

1. Choose **Save & test**.

**Important**  
If you leave **Service** at the default value `aps`, every query fails with HTTP 403. The response includes the message `Credential should be scoped to correct service: 'monitoring'`. When you provision the data source as YAML or Terraform, set the equivalent key `sigv4Service` to `monitoring`.

## Querying from Amazon Managed Grafana with the Amazon Managed Service for Prometheus data source
<a name="CloudWatch-PromQL-Querying-AMG"></a>

If your Amazon Managed Grafana workspace uses Grafana version 12, you can query CloudWatch PromQL data by adding an **Amazon Managed Service for Prometheus** data source that points at the CloudWatch monitoring endpoint. For workspaces that use Grafana version 13 or later, we recommend the CloudWatch data source instead. For more information, see [Querying with the CloudWatch data source](#CloudWatch-PromQL-Querying-CloudWatch-datasource).

This data source plugin signs requests with SigV4 using the workspace IAM role automatically; SigV4 is always enabled, with no toggle to configure. The plugin is available in Amazon Managed Grafana version 12 and later. For more information, see [Connect to an Amazon Managed Service for Prometheus data source](https://docs.aws.amazon.com/grafana/latest/userguide/amazon-prometheus-data-source.html) in the *Amazon Managed Grafana User Guide*.

**IAM prerequisites** — the Amazon Managed Grafana workspace IAM role must have both `cloudwatch:GetMetricData` (required for instant and range queries) and `cloudwatch:ListMetrics` (required for series and label discovery). For details, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM).

To configure the data source, complete the following steps.

1. In your Amazon Managed Grafana workspace, add an **Amazon Managed Service for Prometheus** data source.

1. Set the data source **URL** to `https://monitoring.{{AWS Region}}.amazonaws.com`.

1. Set the **Region** to your AWS Region. Amazon Managed Grafana injects credentials from the workspace IAM role automatically; you do not need to configure static keys.

1. Set the **Service** field to `monitoring`. The plugin defaults this field to `aps`, but the CloudWatch PromQL endpoint requires `monitoring`.

1. Choose **Save & test**.