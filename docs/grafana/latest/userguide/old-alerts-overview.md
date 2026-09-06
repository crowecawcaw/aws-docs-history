

# Classic dashboard alerts
<a name="old-alerts-overview"></a>

****  
This documentation topic discusses legacy alerting in Grafana. Legacy alerting is removed in Amazon Managed Grafana version 12. You must migrate to Grafana alerting before upgrading to v12. For more information, see one of the following topics.  
For Grafana workspaces that support Grafana version 10.x, see [Alerts in Grafana version 10](v10-alerts.md).  
For Grafana workspaces that support Grafana version 9.x, see [Alerts in Grafana version 9](v9-alerts.md).  
For Grafana workspaces that support Grafana version 8.x, see [Grafana alerting](alerts-overview.md).

**Note**  
This section describes the classic dashboard alerts system in Grafana. To learn about migrating to, and using, the new Grafana alerting, which is designed to view Prometheus Alertmanager alerts along with Grafana alerts, see [Alerts in Grafana version 10](v10-alerts.md).

 Classic dashboard alerts consist of two parts: 
+  Alert rules – When the alert is triggered. Alert rules are defined by one or more conditions that are regularly evaluated by Grafana. 
+  Notification channel – How the alert is delivered. When the conditions of an alert rule are met, the Grafana notifies the channels configured for that alert. 

 Currently, only the graph panel visualization supports alerts. 

## Alert configuration
<a name="old-alert-tasks"></a>

You can configure alerts in your Amazon Managed Grafana workspace. 
+  Add or edit an alert notification channel. For more information, see [Notifications](#old-notifications). 
+  Create an alert rule. For more information, see [Creating alerts](old-create-alerts.md). 
+  View existing alert rules and their current state. For more information, see [Viewing existing alert rules](old-view-existing-alert-rules.md). 
+  Test alert rules and troubleshoot. For more information, see [Troubleshooting alerts](old-troubleshoot-alerts.md). 

## Clustering
<a name="old-clustering"></a>

 Currently, alerting supports a limited form of high availability. Alert notifications are deduplicated when you run multiple workspaces. This means that all alerts are run on every server, but no duplicate alert notifications are sent due to the deduping logic. 

## Notifications
<a name="old-notifications"></a>

 You can create alert rules with detailed messages including information such as how you might solve the issue, a link to a runbook, and so on.

 The actual notifications are configured and shared between multiple alerts. 

## Alert execution
<a name="old-alert-execution"></a>

 Alert rules are evaluated in Amazon Managed Grafana in a scheduler and query execution engine.