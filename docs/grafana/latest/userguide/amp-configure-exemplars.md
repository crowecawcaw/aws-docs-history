

# Configure exemplars
<a name="amp-configure-exemplars"></a>

**Important**  
Starting in Amazon Managed Grafana version 12, SigV4 authentication support in the Core Prometheus plugin has been removed. All Amazon Managed Service for Prometheus data sources that were previously using the Core Prometheus plugin are automatically migrated to the Amazon Managed Service for Prometheus plugin. Any dashboards using these data sources are automatically updated to reflect this change. See [Connect to an Amazon Managed Service for Prometheus data source](amazon-prometheus-data-source.md).

**Note**  
This feature requires Prometheus version 2.26 or later.  
Exemplars are not supported in Amazon Managed Service for Prometheus.

You can show exemplars data alongside a metric both in Explore and Dashboards. Exemplars associate higher-cardinality metadata from a specific event with traditional time series data.

You can configure exemplars in the data source settings by adding links to your exemplars. You can use macros in your URL. For example, you could create a URL such as `https://example.com/${__value.raw}`.