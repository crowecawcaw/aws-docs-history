# Use PagerDuty as an alert

receiver

You can configure Amazon Managed Service for Prometheus to send alerts directly to PagerDuty. This integration
requires you to store your PagerDuty integration key in AWS Secrets Manager and grant Amazon Managed Service for Prometheus
permission to read the secret.

PagerDuty integration enables automated incident response workflows and ensures
critical alerts reach the right team members at the right time. When you use
PagerDuty as an alert receiver, you can take advantage of PagerDuty's escalation
policies, on-call scheduling, and incident management features to ensure that alerts
are acknowledged and resolved quickly. This integration is particularly valuable for
production environments where rapid response to system issues is essential for
maintaining service availability and meeting SLA requirements. For more information,
see [PagerDuty Knowledge Base](https://support.pagerduty.com/ "https://support.pagerduty.com/") on
the _PagerDuty website_.

## PagerDuty

configuration options

| Option        | Description                                                                                                   | Required                |
| ------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `routing_key` | The PagerDuty routing key for an integration on a service.<br>You must specify this as an Secrets Manager ARN | Yes                     |
| `service_key` | The PagerDuty service key for an integration on a service.<br>You must specify this as an Secrets Manager ARN | Yes (for Events API v1) |
| `client`      | The client identification of the notifier                                                                     | No                      |
| `client_url`  | A backlink to the sender of the notification                                                                  | No                      |
| `description` | Description of the incident                                                                                   | No                      |
| `details`     | A set of arbitrary key/value pairs that provide further<br>detail about the incident                          | No                      |
| `severity`    | Severity of the incident                                                                                      | No                      |
| `class`       | The class, or type, of the event                                                                              | No                      |
| `component`   | Component of the source machine that is responsible for<br>the event                                          | No                      |
| `group`       | Logical grouping of components                                                                                | No                      |
| `source`      | The unique location of the affected system                                                                    | No                      |

###### Note

The `url`, `service_key_file`,
`routing_key_file`, and `http_config` options are
not supported.

The following topics describe how to configure PagerDuty as an alert receiver in
Amazon Managed Service for Prometheus.

###### Topics

- [Configure AWS Secrets Manager and
  permissions](AMP-alertmanager-pagerduty-permissions.md "AMP-alertmanager-pagerduty-permissions.md")
- [Configure
  alert manager to send alerts to PagerDuty](AMP-alertmanager-pagerduty-configure-alertmanager.md "AMP-alertmanager-pagerduty-configure-alertmanager.md")
