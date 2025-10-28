# Grafana alerting

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Grafana alerting provides you with robust and actionable alerts that help you learn about
problems in the systems moments after they occur, minimizing disruption to your
services.

Amazon Managed Grafana includes access to an updated alerting system, _Grafana
alerting_, that centralizes alerting information in a single, searchable view.
It includes the following features:

- Create and manage Grafana alerts in a centralized view.
- Create and manage Cortex and Loki managed alerts through a single
  interface. For more information, see [Manage your alert rules](v9-alerting-managerules.md "v9-alerting-managerules.md").
- View alerting information from Prometheus, Amazon Managed Service for Prometheus, and other Alertmanager
  compatible data sources.
- Create multiple alert instances from a single alert rule. For more
  information, see [Single and multidimensional rules](v9-alerting-managerules-grafana.md#v9-alerting-single-multi-rule "v9-alerting-managerules-grafana.md#v9-alerting-single-multi-rule").
- Manage your alerting resources with terraform or provisioning APIs. For
  more information, see [Provisioning Grafana Alerting
  resources](v9-alerting-setup-provision.md "v9-alerting-setup-provision.md").
  For existing Amazon Managed Grafana workspace, the default is the [Classic dashboard alerts](old-alerts-overview.md "old-alerts-overview.md"). To migrate to
  Grafana alerting, you must [migrate to Grafana
  alerting](alert-opt-in.md "alert-opt-in.md").

To learn more about Grafana alerting, see [What's new in Grafana alerting](alerts-whats-new.md "alerts-whats-new.md").

Grafana alerting has four key components:

- [Alerting rule](alert-rules.md "alert-rules.md") - Evaluation criteria that
  determines whether an alert is initiated. It consists of one or more queries and
  expressions, a condition, the frequency of evaluation, and optionally, the duration
  over which the condition is met.
- [Contact point](alert-contact-points.md "alert-contact-points.md") - Channel for sending
  notifications when the conditions of an alerting rule are met.
- [Notification policy](alert-notifications.md "alert-notifications.md") - Set of matching
  and grouping criteria used to determine the frequency of notifications.
- [Silences](alert-silences.md "alert-silences.md") - Date and matching criteria used
  to silence notifications.
  When Grafana alerting is enabled, you can:

- [Create Grafana managed alerting
  rules](alert-rules.md#create-grafana-alert-rule "alert-rules.md#create-grafana-alert-rule")
- [Create Cortex or Loki managed alerting
  rules](alert-rules.md#create-alert-rule "alert-rules.md#create-alert-rule")
- [View existing alerting rules and manage their
  current state](alert-rules.md#manage-alert-rules "alert-rules.md#manage-alert-rules")
- [View the state and health of alerting
  rules](alert-fundamentals.md#alerts-state "alert-fundamentals.md#alerts-state")
- [Add or edit an alert contact
  point](alert-contact-points.md#alert-working-contact-points "alert-contact-points.md#alert-working-contact-points")
- [Add or edit notification
  policies](alert-notifications.md#alert-notifications-working "alert-notifications.md#alert-notifications-working")
- [Add or edit silences](alert-silences.md "alert-silences.md")

## Limitations

- The Grafana alerting system can retrieve rules from all available Amazon Managed Service for Prometheus,
  Prometheus, Loki, and Alertmanager data sources. It might not be able to fetch
  rules from other supported data sources.
- Alert rules defined in Grafana, rather than in Prometheus, send multiple
  notifications to your contact point. If you are using native Grafana alerts, we
  recommend that you stay on classic dashboard alerting and not enable the new
  Grafana alerting feature. If you would like to view Alerts defined in your
  Prometheus data source, then we recommend you enable Grafana Alerting, which
  sends only a single notification for alerts created in Prometheus
  Alertmanager.

###### Note

This limitation is no longer a limitation in Amazon Managed Grafana workspaces that
support Grafana v10.4 and later.

###### Topics

- [What's new in Grafana alerting](alerts-whats-new.md "alerts-whats-new.md")
- [Migrating classic dashboard alerts to Grafana
  alerting](alert-opt-in.md "alert-opt-in.md")
- [Alerting fundamentals](alert-fundamentals.md "alert-fundamentals.md")
- [Create and manage Grafana alerting rules](alert-rules.md "alert-rules.md")
- [Alert groups](alert-groups.md "alert-groups.md")
- [Silencing alert notifications for Prometheus data
  sources](alert-silences.md "alert-silences.md")
- [Working with contact points](alert-contact-points.md "alert-contact-points.md")
- [Using messaging templates](alert-message-templates.md "alert-message-templates.md")
- [Working with notification policies](alert-notifications.md "alert-notifications.md")
