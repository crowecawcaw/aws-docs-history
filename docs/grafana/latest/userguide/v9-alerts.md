

# Alerts in Grafana version 9
<a name="v9-alerts"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 9.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

Grafana alerting provides you with robust and actionable alerts that help you learn about problems in the systems moments after they occur, minimizing disruption to your services.

Amazon Managed Grafana includes access to an updated alerting system, *Grafana alerting*, that centralizes alerting information in a single, searchable view. It includes the following features:
+ Create and manage Grafana alerts in a centralized view.
+ Create and manage Cortex and Loki managed alerts through a single interface.
+ View alerting information from Prometheus, Amazon Managed Service for Prometheus, and other Alertmanager compatible data sources.

When you create your Amazon Managed Grafana workspace, you have the choice of using Grafana alerting, or the [Classic dashboard alerts](old-alerts-overview.md). This section covers Grafana alerting.

**Note**  
If you created your workspace with the Classic alerts enabled, and want to switch to Grafana alerting, you can [switch between the two alerting systems.](v9-alerting-use-grafana-alerts.md).

## Grafana alerting limitations
<a name="v9-alert-limitations"></a>
+ The Grafana alerting system can retrieve rules from all available Amazon Managed Service for Prometheus, Prometheus, Loki, and Alertmanager data sources. It might not be able to fetch rules from other supported data sources.
+ Alert rules defined in Grafana, rather than in Prometheus, send multiple notifications to your contact point. If you are using native Grafana alerts, we recommend that you stay on classic dashboard alerting and not enable the new Grafana alerting feature. If you would like to view Alerts defined in your Prometheus data source, then we recommend you enable Grafana Alerting, which sends only a single notification for alerts created in Prometheus Alertmanager.
**Note**  
This limitation is no longer a limitation in Amazon Managed Grafana workspaces that support Grafana v10.4 and later.

**Topics**
+ [Grafana alerting limitations](#v9-alert-limitations)
+ [Overview](v9-alerting-overview.md)
+ [Exploring alerting](v9-alerting-explore.md)
+ [Set up Alerting](v9-alerting-setup.md)
+ [Migrating classic dashboard alerts to Grafana alerting](v9-alerting-use-grafana-alerts.md)
+ [Manage your alert rules](v9-alerting-managerules.md)
+ [Manage your alert notifications](v9-alerting-managenotifications.md)