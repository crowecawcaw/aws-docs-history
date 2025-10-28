# Configure alert manager to send

messages to Amazon SNS as JSON

By default, Amazon Managed Service for Prometheus alert manager outputs messages in a plain text list
format. This can be more difficult for other services to parse. You can
configure alert manager to send alerts in JSON format instead. JSON can make it
simpler to process the messages downstream from Amazon SNS in AWS Lambda or in
webhook-receiving endpoints. Instead of using the default template, you can
define a custom template to output the message contents in JSON, making it
easier to parse in downstream functions.

To output messages from alert manager to Amazon SNS in JSON format, update your
alert manager configuration to contain the following code inside your
`template_files` root section:

```
default_template: |
   {{ define "sns.default.message" }}{{ "{" }}"receiver": "{{ .Receiver }}","status": "{{ .Status }}","alerts": [{{ range $alertIndex, $alerts := .Alerts }}{{ if $alertIndex }}, {{ end }}{{ "{" }}"status": "{{ $alerts.Status }}"{{ if gt (len $alerts.Labels.SortedPairs) 0 -}},"labels": {{ "{" }}{{ range $index, $label := $alerts.Labels.SortedPairs }}{{ if $index }}, {{ end }}"{{ $label.Name }}": "{{ $label.Value }}"{{ end }}{{ "}" }}{{- end }}{{ if gt (len $alerts.Annotations.SortedPairs ) 0 -}},"annotations": {{ "{" }}{{ range $index, $annotations := $alerts.Annotations.SortedPairs }}{{ if $index }}, {{ end }}"{{ $annotations.Name }}": "{{ $annotations.Value }}"{{ end }}{{ "}" }}{{- end }},"startsAt": "{{ $alerts.StartsAt }}","endsAt": "{{ $alerts.EndsAt }}","generatorURL": "{{ $alerts.GeneratorURL }}","fingerprint": "{{ $alerts.Fingerprint }}"{{ "}" }}{{ end }}]{{ if gt (len .GroupLabels) 0 -}},"groupLabels": {{ "{" }}{{ range $index, $groupLabels := .GroupLabels.SortedPairs }}{{ if $index }}, {{ end }}"{{ $groupLabels.Name }}": "{{ $groupLabels.Value }}"{{ end }}{{ "}" }}{{- end }}{{ if gt (len .CommonLabels) 0 -}},"commonLabels": {{ "{" }}{{ range $index, $commonLabels := .CommonLabels.SortedPairs }}{{ if $index }}, {{ end }}"{{ $commonLabels.Name }}": "{{ $commonLabels.Value }}"{{ end }}{{ "}" }}{{- end }}{{ if gt (len .CommonAnnotations) 0 -}},"commonAnnotations": {{ "{" }}{{ range $index, $commonAnnotations := .CommonAnnotations.SortedPairs }}{{ if $index }}, {{ end }}"{{ $commonAnnotations.Name }}": "{{ $commonAnnotations.Value }}"{{ end }}{{ "}" }}{{- end }}{{ "}" }}{{ end }}
   {{ define "sns.default.subject" }}[{{ .Status | toUpper }}{{ if eq .Status "firing" }}:{{ .Alerts.Firing | len }}{{ end }}]{{ end }}
```

###### Note

This template creates JSON from alphanumeric data. If your data has
special characters, encode them before using this template.

To make sure that this template is used in outgoing notifications, reference
it in your `alertmanager_config` block as follows:

```
alertmanager_config: |
  global:
  templates:
    - 'default_template'

```

###### Note

This template is for the entire message body as JSON. This template
overwrites the entire message body. You cannot override the message body if
you wish to use this specific template. Any overrides that are manually done
will take precedence over the template.

For more information about:

- The alert manager configuration file, see [Create an alert manager configuration in
  Amazon Managed Service for Prometheus to manage and route alerts](AMP-alertmanager-config.md "AMP-alertmanager-config.md").
- Uploading your configuration file, see [Upload your alert manager configuration file
  to Amazon Managed Service for Prometheus](AMP-alertmanager-upload.md "AMP-alertmanager-upload.md").
