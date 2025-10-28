# Connect to Amazon Managed Service for Prometheus and open-source Prometheus

data sources

In Amazon Managed Grafana, the Prometheus data source supports using both self-managed
Prometheus servers and Amazon Managed Service for Prometheus workspaces as data sources. For more information about
Amazon Managed Service for Prometheus, see [What is Amazon Managed Service for Prometheus?](../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md "../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md")

With Amazon Managed Grafana, you can add an Amazon Managed Service for Prometheus workspace as a data source by using the
AWS data source configuration option in the Grafana workspace console. This
feature simplifies adding Amazon Managed Service for Prometheus as a data source by discovering your existing Amazon Managed Service for Prometheus
accounts and manages the configuration of the authentication credentials that are
required to access Amazon Managed Service for Prometheus.

###### Note

You can view your Prometheus alerts in the unified Grafana alerting interface,
by [Configuring an Alertmanager
data source](data-source-alertmanager.md#data-source-alertmanager-create "data-source-alertmanager.md#data-source-alertmanager-create").

###### Topics

- [Use AWS data source configuration to
  add Amazon Managed Service for Prometheus as a data source](AMP-adding-AWS-config.md "AMP-adding-AWS-config.md")
- [Manually adding the Prometheus data
  source](prometheus-manually-adding.md "prometheus-manually-adding.md")
- [Using the Prometheus data
  source](using-prometheus-datasource.md "using-prometheus-datasource.md")
- [Visualize alerts from Amazon Managed Service for Prometheus](amp-configure-alerts.md "amp-configure-alerts.md")
- [Configure exemplars](amp-configure-exemplars.md "amp-configure-exemplars.md")
