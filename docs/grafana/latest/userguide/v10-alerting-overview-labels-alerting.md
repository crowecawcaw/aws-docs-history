# Labels in Grafana

Alerting

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

This topic explains why labels are a fundamental component of alerting.

- The complete set of labels for an alert is what uniquely
  identifies an alert within Grafana alerts.
- The Alertmanager uses labels to match alerts for silences and
  alert groups in notification policies.
- The alerting UI shows labels for every alert instance generated
  during evaluation of that rule.
- Contact points can access labels to dynamically generate
  notifications that contain information specific to the alert that is
  resulting in a notification.
- You can add labels to an [alerting rule](v10-alerting-configure.md "v10-alerting-configure.md"). Labels are manually configurable, use
  template functions, and
  can reference other labels. Labels added to an alerting rule take
  precedence in the event of a collision between labels (except in the
  case of Grafana reserved labels, see below for more information).

## External

Alertmanager compatibility

Grafana’s built-in Alertmanager supports both Unicode label keys and values.
If you are using an external Prometheus Alertmanager, label keys must be
compatible with their [data model](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels "https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels"). This means that label keys must only contain **ASCII letters**, **numbers**, as well as **underscores**
and match the regex `[a-zA-Z_][a-zA-Z0-9_]*`. Any
invalid characters will be removed or replaced by the Grafana alerting engine
before being sent to the external Alertmanager according to the following
rules:

- `Whitespace` will be removed.
- `ASCII characters` will be replaced with
  `_`.
- `All other characters` will be replaced with their
  lower-case hex representation. If
  this is the first character it will be prefixed with
  `_`.

###### Note

If multiple label keys are sanitized to
the same value, the duplicates will have a short hash of the original label
appended as a suffix.

## Grafana

reserved labels

###### Note

Labels prefixed with
`grafana_` are reserved by Grafana for
special use. If a manually configured label is added beginning with
`grafana_` it will be overwritten in case of
collision.

Grafana reserved labels can be used in the same way as manually configured
labels. The current list of available reserved labels are:

| Label          | Description                               |
| -------------- | ----------------------------------------- |
| grafana_folder | Title of the folder containing the alert. |
