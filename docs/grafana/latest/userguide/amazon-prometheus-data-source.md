

# Connect to an Amazon Managed Service for Prometheus data source
<a name="amazon-prometheus-data-source"></a>

**Note**  
The Amazon Managed Service for Prometheus data source is available starting in Amazon Managed Grafana version 12.

 In Amazon Managed Grafana, you can use Amazon Managed Service for Prometheus workspaces as data sources. For more information about Amazon Managed Service for Prometheus, see [What is Amazon Managed Service for Prometheus?](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)

 With Amazon Managed Grafana, you can add an Amazon Managed Service for Prometheus workspace as a data source by using the AWS data source configuration option in the Grafana workspace console. This feature simplifies adding Amazon Managed Service for Prometheus as a data source by discovering your existing Amazon Managed Service for Prometheus accounts and manages the configuration of the authentication credentials that are required to access Amazon Managed Service for Prometheus.

**Note**  
You can view your Prometheus alerts in the unified Grafana alerting interface, by [Configuring an Alertmanager data source](data-source-alertmanager.md#data-source-alertmanager-create).

**Topics**
+ [Use AWS data source configuration to add Amazon Managed Service for Prometheus as a data source](amazon-AMP-adding-AWS-config.md)
+ [Using the Prometheus data source](amazon-using-prometheus-datasource.md)
+ [Visualize alerts from Amazon Managed Service for Prometheus](amazon-amp-configure-alerts.md)
+ [Query Amazon CloudWatch metrics using PromQL](cloudwatch-promql.md)