

# Recording rules
<a name="v12-alerting-explore-rule-recording"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 12.x**.  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

Recording rules are available for compatible Prometheus or Loki data sources, and for Grafana-managed alerts. Recording rules allow you to precompute frequently used queries for better performance.

A recording rule allows you to pre-compute frequently needed or computationally expensive expressions and save their result as a new set of time series. This is useful if you want to run alerts on aggregated data or if you have dashboards that query computationally expensive expressions repeatedly.

Querying this new time series is faster, especially for dashboards since they query the same expression every time the dashboards refresh.

Read more about [recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) in Prometheus.