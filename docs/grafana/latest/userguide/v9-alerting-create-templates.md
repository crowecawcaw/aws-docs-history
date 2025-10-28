# Create notification

templates

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Create reusable notification templates to send to your contact points.

You can add one or more templates to your notification template.

Your notification template name must be unique. You cannot have two templates
with the same name in the same notification template or in different
notification templates. Avoid defining templates with the same name as default
templates, such as: `__subject`,
`__text_values_list`,
`__text_alert_list`,
`default.title` and
`default.message`.

In the Contact points tab, you can see a list of your notification
templates.

## Creating notification

templates

###### To create a notification template

1. Click **Add template**.
2. Choose a name for the notification template, such as
   `email.subject`.
3. Write the content of the template in the content field.

For example:

```
{{ if .Alerts.Firing -}}
   {{ len .Alerts.Firing }} firing alerts
   {{ end }}
   {{ if .Alerts.Resolved -}}
   {{ len .Alerts.Resolved }} resolved alerts
   {{ end }}
```

4. Click Save.

`{{ define "email.subject" }}` (where `email.subject`
is the name of your template) and
`{{ end }}` is automatically added to the start
and end of the content.

###### To create a notification template that contains more than one template:

1. Click **Add Template**.
2. Enter a name for the overall notification template. For example,
   `email`.
3. Write each template in the Content field, including
   `{{ define "`name-of-template`" }}`
   and `{{ end }}` at the start and end of
   each template. You can use descriptive names for each of the templates
   in the notification template, for example,
   `email.subject` or `email.message`. In this
   case, do not reuse the name of the notification template you entered
   above.

The following sections show detailed examples for templates you
might create. 4. Click Save.

## Creating a template

for the subject of an email

Create a template for the subject of an email that contains the number
of firing and resolved alerts, as in this example:

```
1 firing alerts, 0 resolved alerts
```

###### To create a template for the subject of an email

1. Create a template called
   `email.subject` with the
   following content:

```
{{ define "email.subject" }}
{{ len .Alerts.Firing }} firing alerts, {{ len .Alerts.Resolved }} resolved alerts
{{ end }}
```

2. Use the template when creating your contact
   point integration by putting it into the
   **Subject** field with
   the `template` keyword.

```
{{ template "email.subject" . }}
```

## Creating a template

for the message of an email

Create a template for the message of an email that contains a summary
of all firing and resolved alerts, as in this example:

```
There are 2 firing alerts, and 1 resolved alerts

Firing alerts:

- alertname=Test 1 grafana_folder=GrafanaCloud has value(s) B=1
- alertname=Test 2 grafana_folder=GrafanaCloud has value(s) B=2

Resolved alerts:

- alertname=Test 3 grafana_folder=GrafanaCloud has value(s) B=0

```

###### To create a template for the message of an email

1. Create a notification template called
   `email` with two templates in the
   content: `email.message_alert`
   and `email.message`.

The `email.message_alert`
template is used to print the labels and values for each firing
and resolved alert while the
`email.message` template contains
the structure of the email.

```
{{- define "email.message_alert" -}}
{{- range .Labels.SortedPairs }}{{ .Name }}={{ .Value }} {{ end }} has value(s)
{{- range $k, $v := .Values }} {{ $k }}={{ $v }}{{ end }}
{{- end -}}

{{ define "email.message" }}
There are {{ len .Alerts.Firing }} firing alerts, and {{ len .Alerts.Resolved }} resolved alerts

{{ if .Alerts.Firing -}}
Firing alerts:
{{- range .Alerts.Firing }}
- {{ template "email.message_alert" . }}
{{- end }}
{{- end }}

{{ if .Alerts.Resolved -}}
Resolved alerts:
{{- range .Alerts.Resolved }}
- {{ template "email.message_alert" . }}
{{- end }}
{{- end }}

{{ end }}
```

2. Use the template when creating your contact
   point integration by putting it into the **Text
   Body** field with
   the `template` keyword.

```
{{ template "email.message" . }}
```

## Creating a

template for the title of a Slack message

Create a template for the title of a Slack message that contains the
number of firing and resolved alerts, as in the following example:

```
1 firing alerts, 0 resolved alerts
```

###### To create a template for the title of a Slack message

1. Create a template called
   `slack.title` with the following
   content:

```
{{ define "slack.title" }}
{{ len .Alerts.Firing }} firing alerts, {{ len .Alerts.Resolved }} resolved alerts
{{ end }}
```

2. Use the template when creating your contact
   point integration by putting it into the **Title**
   field with the `template` keyword.

```
{{ template "slack.title" . }}
```

## Creating a

template for the content of a Slack message

Create a template for the content of a Slack message that contains
a description of all firing and resolved alerts, including their labels,
annotations, and Dashboard URL:

```
1 firing alerts:

[firing] Test1
Labels:
- alertname: Test1
- grafana_folder: GrafanaCloud
Annotations:
- description: This is a test alert
Go to dashboard: https://example.com/d/dlhdLqF4z?orgId=1

1 resolved alerts:

[firing] Test2
Labels:
- alertname: Test2
- grafana_folder: GrafanaCloud
Annotations:
- description: This is another test alert
Go to dashboard: https://example.com/d/dlhdLqF4z?orgId=1
```

###### To create a template for the content of a Slack message

1. Create a template called
   `slack` with two templates in the
   content: `slack.print_alert` and
   `slack.message`.

The `slack.print_alert`
template is used to print the labels, annotations, and
DashboardURL while the
`slack.message` template contains
the structure of the notification.

```
{{ define "slack.print_alert" -}}
[{{.Status}}] {{ .Labels.alertname }}
Labels:
{{ range .Labels.SortedPairs -}}
- {{ .Name }}: {{ .Value }}
{{ end -}}
{{ if .Annotations -}}
Annotations:
{{ range .Annotations.SortedPairs -}}
- {{ .Name }}: {{ .Value }}
{{ end -}}
{{ end -}}
{{ if .DashboardURL -}}
  Go to dashboard: {{ .DashboardURL }}
{{- end }}
{{- end }}

{{ define "slack.message" -}}
{{ if .Alerts.Firing -}}
{{ len .Alerts.Firing }} firing alerts:
{{ range .Alerts.Firing }}
{{ template "slack.print_alert" . }}
{{ end -}}
{{ end }}
{{ if .Alerts.Resolved -}}
{{ len .Alerts.Resolved }} resolved alerts:
{{ range .Alerts.Resolved }}
{{ template "slack.print_alert" .}}
{{ end -}}
{{ end }}
{{- end }}
```

2. Use the template when creating your contact
   point integration by putting it into the **Text
   Body** field with the `template`
   keyword.

```
{{ template "slack.message" . }}
```

## Template both

email and Slack with shared templates

Instead of creating separate notification templates for each contact
point, such as email and Slack, you can share the same template.

For example, if you want to send an email with this subject and Slack
message with this title `1 firing alerts, 0 resolved 
 alerts`, you can create a shared template.

###### To create a shared template

1. Create a template called
   `common.subject_title` with the
   following content:

```
{{ define "common.subject_title" }}
{{ len .Alerts.Firing }} firing alerts, {{ len .Alerts.Resolved }} resolved alerts
{{ end }}
```

2. For email, run the template from the subject field in your
   email contact point integration:

```
{{ template "common.subject_title" . }}
```

3. For Slack, run the template from the title field in your
   Slack contact point integration:

```
{{ template "common.subject_title" . }}
```

## Using notification

templates

Use templates in contact points to customize your notifications.

###### To use a template when creating a contact point

1. From the **Alerting** menu, choose
   **Contact points** to see a list of existing
   contact points.
2. Choose **Add contact point**. Alternately, you can
   edit an existing contact point by choosing the **Edit**
   icon (pen) next to the contact point you wish to edit.
3. Enter the templates you wish to use in one or more field, such as
   **Message** or **Subject**. To enter
   a template, use the form `{{ template 
"`template_name`" . }}`, replacing
   `template_name` with the name of the template
   you want to use.
4. Click **Save contact point**.
