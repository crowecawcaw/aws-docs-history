# Forward alerts to an alert receiver with

alert manager in Amazon Managed Service for Prometheus

When an alert is raised by an alert rule, it is sent to alert manager. Alert manager
performs functions such as de-duplicating alerts, inhibiting alerts during maintenance,
or grouping them as needed. It then forwards the alert as a message to an
_alert receiver_. You can set up an alert receiver that can
notify operators, have automated responses, or respond to the alerts in other
ways.

You can configure Amazon Simple Notification Service (Amazon SNS) and PagerDuty as alert receivers in Amazon Managed Service for Prometheus. The
following topics describe how to create and configure your alert receiver.

###### Topics

- [Use Amazon SNS as an alert
  receiver](AMP-alertmanager-receiver-createtopic.md "AMP-alertmanager-receiver-createtopic.md")
- [Use PagerDuty as an alert
  receiver](AMP-alertmanager-pagerduty.md "AMP-alertmanager-pagerduty.md")
