

# Connect to Amazon Managed Service for Prometheus and open-source Prometheus data sources
<a name="prometheus-data-source"></a>

 In Amazon Managed Grafana, the Prometheus data source supports using both self-managed Prometheus servers and Amazon Managed Service for Prometheus workspaces as data sources. For more information about Amazon Managed Service for Prometheus, see [What is Amazon Managed Service for Prometheus?](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)

 With Amazon Managed Grafana, you can add an Amazon Managed Service for Prometheus workspace as a data source by using the AWS data source configuration option in the Grafana workspace console. This feature simplifies adding Amazon Managed Service for Prometheus as a data source by discovering your existing Amazon Managed Service for Prometheus accounts and manages the configuration of the authentication credentials that are required to access Amazon Managed Service for Prometheus.

**Note**  
You can view your Prometheus alerts in the unified Grafana alerting interface, by [Configuring an Alertmanager data source](data-source-alertmanager.md#data-source-alertmanager-create).

**Important**  
Starting in Amazon Managed Grafana version 12, SigV4 authentication support in the Core Prometheus plugin has been removed. All Amazon Managed Service for Prometheus data sources that were previously using the Core Prometheus plugin are automatically migrated to the Amazon Managed Service for Prometheus plugin. Any dashboards using these data sources are automatically updated to reflect this change. See [Connect to an Amazon Managed Service for Prometheus data source](amazon-prometheus-data-source.md).

**Topics**
+ [Use AWS data source configuration to add Amazon Managed Service for Prometheus as a data source](AMP-adding-AWS-config.md)
+ [Manually adding the Prometheus data source](prometheus-manually-adding.md)
+ [Using the Prometheus data source](using-prometheus-datasource.md)
+ [Visualize alerts from Amazon Managed Service for Prometheus](amp-configure-alerts.md)
+ [Configure exemplars](amp-configure-exemplars.md)