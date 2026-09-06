

# Set up Alerting
<a name="v10-alerting-setup"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 10.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

Configure the features and integrations that you need to create and manage your alerts.

**Prerequisites**

Before you set up alerting, you must do the following.
+ Configure your [data sources](AMG-data-sources.md).
+ Ensure that the data source you choose are compatible with and supported by [Grafana alerting](v10-alerting-overview-datasources.md).

**To set up alerting**

1. Configure [alert rules](v10-alerting-configure.md).
   + Create Grafana-managed or data-source managed alert rules and recording rules.

1. Configure [contact points](v10-alerting-configure-contactpoints.md).
   + Check the default contact point, and update the contact for your system.
   + Optionally, add new contact points and integrations.

1. Configure [notification policies](v10-alerting-explore-notifications-policies-details.md)
   + Check the default notification policy, and update for your system.
   + Optionally, add additional nested policies.
   + Optionally, add labels and label matchers to control alert routing.

The following topics give you more information about additional configuration options, including configuring external alert managers and routing Grafana-managed alerts outside of Grafana.

**Topics**
+ [Migrating classic dashboard alerts to Grafana alerting](v10-alerting-use-grafana-alerts.md)
+ [Adding an external Alertmanager](v10-alerting-setup-alertmanager.md)
+ [Provisioning Grafana Alerting resources](v10-alerting-setup-provision.md)