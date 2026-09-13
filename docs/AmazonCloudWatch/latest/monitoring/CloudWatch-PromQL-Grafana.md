

# Grafana integration
<a name="CloudWatch-PromQL-Grafana"></a>

After you ingest OpenTelemetry metrics into CloudWatch and make them queryable with PromQL, you can visualize and explore that data in Grafana and Amazon Managed Grafana. Both connect to the CloudWatch monitoring endpoint through the **Amazon Managed Service for Prometheus** data source plugin, which signs requests with Signature Version 4 (SigV4). This section describes how to configure each.

## Querying from Grafana
<a name="CloudWatch-PromQL-Querying-Grafana"></a>

You can query CloudWatch PromQL data from Grafana by adding the **Amazon Managed Service for Prometheus** data source plugin and pointing it at the CloudWatch monitoring endpoint. SigV4 signing is built in to the plugin and is always enabled, so there is no toggle to turn on. The plugin is published at [grafana.com/grafana/plugins/grafana-amazonprometheus-datasource/](https://grafana.com/grafana/plugins/grafana-amazonprometheus-datasource/); install it from the Grafana plugins catalog before adding the data source. AMP plugin v3.0.0 requires Grafana `>=11.6.11 <12 || >=12.0.10 <12.1 || >=12.1.7 <12.2 || >=12.2.5`.

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

## Querying from Amazon Managed Grafana
<a name="CloudWatch-PromQL-Querying-AMG"></a>

You can query CloudWatch PromQL data from an Amazon Managed Grafana workspace by adding an **Amazon Managed Service for Prometheus** data source that points at the CloudWatch monitoring endpoint. This data source plugin signs requests with SigV4 using the workspace IAM role automatically; SigV4 is always enabled, with no toggle to configure. The plugin is available in Amazon Managed Grafana version 12 and later. For more information, see [Connect to an Amazon Managed Service for Prometheus data source](https://docs.aws.amazon.com/grafana/latest/userguide/amazon-prometheus-data-source.html) in the *Amazon Managed Grafana User Guide*.

**IAM prerequisites** — the Amazon Managed Grafana workspace IAM role must have both `cloudwatch:GetMetricData` (required for instant and range queries) and `cloudwatch:ListMetrics` (required for series and label discovery). For details, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM).

To configure the data source, complete the following steps.

1. In your Amazon Managed Grafana workspace, add an **Amazon Managed Service for Prometheus** data source.

1. Set the data source **URL** to `https://monitoring.{{AWS Region}}.amazonaws.com`.

1. Set the **Region** to your AWS Region. Amazon Managed Grafana injects credentials from the workspace IAM role automatically; you do not need to configure static keys.

1. Set the **Service** field to `monitoring`. The plugin defaults this field to `aps`, but the CloudWatch PromQL endpoint requires `monitoring`.

1. Choose **Save & test**.