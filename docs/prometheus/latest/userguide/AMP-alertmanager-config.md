# Create an alert manager configuration in

Amazon Managed Service for Prometheus to manage and route alerts

To use alert manager and templating in Amazon Managed Service for Prometheus, you create an alert manager
configuration YAML file. An Amazon Managed Service for Prometheus alert manager file has two main sections:

- `template_files:` contains the templates used for messages sent by
  receivers. For more information, see [Template Reference](https://prometheus.io/docs/prometheus/latest/configuration/template_reference/ "https://prometheus.io/docs/prometheus/latest/configuration/template_reference/") and [Template Examples](https://prometheus.io/docs/prometheus/latest/configuration/template_examples/ "https://prometheus.io/docs/prometheus/latest/configuration/template_examples/") in the Prometheus documentation.
- `alertmanager_config:` contains the alert manager configuration.
  This uses the same structure as an alert manager config file in standalone
  Prometheus. For more information, see [Configuration](https://prometheus.io/docs/alerting/latest/configuration/ "https://prometheus.io/docs/alerting/latest/configuration/") in the Alertmanager documentation.

###### Note

The `repeat_interval` configuration described in the Prometheus
documentation above has an additional limitation in Amazon Managed Service for Prometheus. The maximum
allowed value is five days. If you set it higher than five days, it will be
treated as five days and notifications will be sent again after the five day
period has passed.

###### Note

You can also edit the configuration file directly in the Amazon Managed Service for Prometheus console, but it
must still follow the format specified here. For more information on uploading or
editing a configuration file, see [Upload your alert manager configuration file
to Amazon Managed Service for Prometheus](AMP-alertmanager-upload.md "AMP-alertmanager-upload.md").

In Amazon Managed Service for Prometheus, your alert manager configuration file must have all your alert manager
configuration content inside of an `alertmanager_config` key at the root of
the YAML file.

The following is a basic example alert manager configuration file:

```
alertmanager_config: |
  route:
    receiver: 'default'
  receivers:
    - name: 'default'
      sns_configs:
      - topic_arn: arn:aws:sns:us-east-2:123456789012:My-Topic
        sigv4:
          region: us-east-2
        attributes:
          key: key1
          value: value1
```

The only receiver currently supported is Amazon Simple Notification Service (Amazon SNS). If you have other types of
receivers listed in the configuration, it will be rejected.

Here is another sample alert manager configuration file that uses both the
`template_files` block and the `alertmanager_config`
block.

```
template_files:
  default_template: |
    {{ define "sns.default.subject" }}[{{ .Status | toUpper }}{{ if eq .Status "firing" }}:{{ .Alerts.Firing | len }}{{ end }}]{{ end }}
    {{ define "__alertmanager" }}AlertManager{{ end }}
    {{ define "__alertmanagerURL" }}{{ .ExternalURL }}/#/alerts?receiver={{ .Receiver | urlquery }}{{ end }}
alertmanager_config: |
  global:
  templates:
    - 'default_template'
  route:
    receiver: default
  receivers:
    - name: 'default'
      sns_configs:
      - topic_arn: arn:aws:sns:us-east-2:accountid:My-Topic
        sigv4:
          region: us-east-2
        attributes:
          key: severity
          value: SEV2
```

**Default Amazon SNS template block**

The default Amazon SNS configuration uses the following template unless you explicitly
override it.

```
{{ define "sns.default.message" }}{{ .CommonAnnotations.SortedPairs.Values | join " " }}
  {{ if gt (len .Alerts.Firing) 0 -}}
  Alerts Firing:
    {{ template "__text_alert_list" .Alerts.Firing }}
  {{- end }}
  {{ if gt (len .Alerts.Resolved) 0 -}}
  Alerts Resolved:
    {{ template "__text_alert_list" .Alerts.Resolved }}
  {{- end }}
{{- end }}

```
