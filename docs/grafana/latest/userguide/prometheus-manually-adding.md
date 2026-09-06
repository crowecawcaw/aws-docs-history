

# Manually adding the Prometheus data source
<a name="prometheus-manually-adding"></a>

**Important**  
Starting in Amazon Managed Grafana version 12, SigV4 authentication support in the Core Prometheus plugin has been removed. All Amazon Managed Service for Prometheus data sources that were previously using the Core Prometheus plugin are automatically migrated to the Amazon Managed Service for Prometheus plugin. Any dashboards using these data sources are automatically updated to reflect this change. See [Connect to an Amazon Managed Service for Prometheus data source](amazon-prometheus-data-source.md).

**To manually add the Prometheus data source**

1.  In the Grafana console side menu, pause on the **Administration** menu item (or the **Configuration** (gear) icon in Grafana v8), then choose **Data Sources**.

1. Choose **Add data source**.

1. Choose the **Prometheus** data source. If necessary, you can start typing **Prometheus** in the search box to help you find it.