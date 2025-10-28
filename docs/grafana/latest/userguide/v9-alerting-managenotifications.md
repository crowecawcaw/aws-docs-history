# Manage your alert

notifications

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Choosing how, when, and where to send your alert notifications is an important part of
setting up your alerting system. These decisions will have a direct impact on your
ability to resolve issues quickly and not miss anything important.

As a first step, define your _contact points_; where to send
your alert notifications
to. A contact point can be a set of destinations for matching notifications. Add
notification templates to contact points for reuse and consistent messaging in your
notifications.

Next, create a _notification policy_, which is a set of rules for
where, when and how your alerts are routed to contact points. In a notification policy,
you define where to send your alert notifications by choosing one of the contact points
you created. Add mute timings to your notification policy. A _mute
timing_ is a recurring interval of time during which you don’t want any
notifications to be sent out.

When an alert rule is evaluated, the alert ruler sends alert instances to the
Alertmanager — one alert rule can trigger multiple individual
_alert instances_.

The Alertmanager receives these alert instances and then handles mute timings, groups
alerts, and sends notifications to your contact points as defined in the notification
policy.

###### Topics

- [Alertmanager](v9-alerting-managenotifications-alertmanager.md "v9-alerting-managenotifications-alertmanager.md")
- [Working with contact points](v9-alerting-contact-points.md "v9-alerting-contact-points.md")
- [Working with notification
  policies](v9-alerting-notification-policies.md "v9-alerting-notification-policies.md")
- [Customize notifications](v9-alerting-notifications.md "v9-alerting-notifications.md")
- [Silencing alert notifications for
  Prometheus data sources](v9-alerting-silences.md "v9-alerting-silences.md")
- [Mute timings](v9-alerting-notification-muting.md "v9-alerting-notification-muting.md")
- [View and filter by alert
  groups](v9-alerting-viewfiltergroups.md "v9-alerting-viewfiltergroups.md")
- [View notification errors](v9-alerting-viewnotificationerrors.md "v9-alerting-viewnotificationerrors.md")
