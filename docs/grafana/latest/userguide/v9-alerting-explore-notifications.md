# Notifications

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Grafana uses Alertmanagers to send notifications for firing and resolved alerts.
Grafana has its own Alertmanager, referred to as “Grafana” in the user interface,
but also supports sending notifications from other Alertmanagers too, such as the
[Prometheus
Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/ "https://prometheus.io/docs/alerting/latest/alertmanager/"). The Grafana Alertmanager uses notification policies and
contact points to configure how and where a notification is sent; how often a
notification should be sent; and whether alerts should all be sent in the same
notification, sent in grouped notifications based on a set of labels, or as separate
notifications.

## Notification

policies

Notification policies control when and where notifications are sent. A
notification policy can choose to send all alerts together in the same
notification, send alerts in grouped notifications based on a set of labels, or
send alerts as separate notifications. You can configure each notification
policy to control how often notifications should be sent as well as having one
or more mute timings to inhibit notifications at certain times of the day and on
certain days of the week.

Notification policies are organized in a tree structure where at the root of
the tree there is a notification policy called the root policy. There can be
only one root policy and the root policy cannot be deleted.

Specific routing policies are children of the root policy and can be used to
match either all alerts or a subset of alerts based on a set of matching labels.
A notification policy matches an alert when its matching labels match the labels
in the alert.

A specific routing policy can have its own child policies, called nested
policies, which allow for additional matching of alerts. An example of a
specific routing policy could be sending infrastructure alerts to the Ops team;
while a child policy might send high priority alerts to Pagerduty and low
priority alerts to Slack.

All alerts, irrespective of their labels, match the root policy. However, when
the root policy receives an alert it looks at each specific routing policy and
sends the alert to the first specific routing policy that matches the alert. If
the specific routing policy has further child policies, then it can attempt to
the match the alert against one of its nested policies. If no nested policies
match the alert then the specific routing policy is the matching policy. If
there are no specific routing policies, or no specific routing policies match
the alert, then the root policy is the matching policy.

## Contact

points

Contact points contain the configuration for sending notifications. A contact
point is a list of integrations, each of which sends a notification to a
particular email address, service or URL. Contact points can have multiple
integrations of the same kind, or a combination of integrations of different
kinds. For example, a contact point could contain a Pager Duty integration; a
Pager Duty and Slack integration; or a Pager Duty integration, a Slack
integration, and two Amazon SNS integrations. You can also configure a contact point
with no integrations; in which case no notifications are sent.

A contact point cannot send notifications until it has been added to a
notification policy. A notification policy can only send alerts to one contact
point, but a contact point can be added to a number of notification policies at
the same time. When an alert matches a notification policy, the alert is sent to
the contact point in that notification policy, which then sends a notification
to each integration in its configuration.

###### Note

For information about supported integrations for contact points, see
[Contact points](v9-alerting-explore-contacts.md "v9-alerting-explore-contacts.md").

## Templating

notifications

You can customize notifications with templates. For example, templates can be
used to change the title and message of notifications sent to Slack.

Templates are not limited to an individual integration or contact point, but
instead can be used in a number of integrations in the same contact point and
even integrations across different contact points. For example, a Grafana user
can create a template called `custom_subject_or_title` and use it for
both templating subjects in Pager Duty and titles of Slack messages without
having to create two separate templates.

All notifications templates are written in [Go’s templating language](https://pkg.go.dev/text/template "https://pkg.go.dev/text/template"), and
are in the Contact points tab on the Alerting page.

## Silences

You can use silences to mute notifications from one or more firing rules.
Silences do not stop alerts from firing or being resolved, or hide firing alerts
in the user interface. A silence lasts as long as its duration which can be
configured in minutes, hours, days, months or years.
