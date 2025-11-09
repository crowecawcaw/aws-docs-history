# Using messaging templates

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Notifications sent via [Working with contact points](alert-contact-points.md "alert-contact-points.md") are built using _messaging
templates_. Grafana’s default templates are based on the [Go templating system](https://golang.org/pkg/text/template "https://golang.org/pkg/text/template") where some
fields are evaluated as text, while others are evaluated as HTML (which can affect
escaping).

Since most of the contact point fields can be templated, you can create reusable
custom templates and use them in multiple contact points. The [Template data](#alert-template-data "#alert-template-data") topic lists
variables that are available for templating.

**Using templates**

Templates are used to create a message. For example, with a Slack alert message, you
can set the title and body in the contact point. The following example shows how to use
default templates to create a title that contains a count of alerts firing and resolved,
and a body that lists the alerts and their statuses.

- **Title**:

```
{{ len .Alerts.Firing }} firing, {{ len .Alerts.Resolved }} resolved
```

- **Text Body**:

```
{{ range .Alerts }}{{ .Status }}: {{ .Labels.alertname }}
{{end }}
```

You can create your own custom templates, as in the following example.

- **Title**:

```
{{ template "slack.default.title" .}}
```

- **Text Body**:

```
{{ template "mymessage" .}}
```

The following is a sample template.

```
{{ define "myalert" }}
  [{{.Status}}] {{ .Labels.alertname }}

  Labels:
  {{ range .Labels.SortedPairs }}
    {{ .Name }}: {{ .Value }}
  {{ end }}

  {{ if gt (len .Annotations) 0 }}
  Annotations:
  {{ range .Annotations.SortedPairs }}
    {{ .Name }}: {{ .Value }}
  {{ end }}
  {{ end }}

  {{ if gt (len .SilenceURL ) 0 }}
    Silence alert: {{ .SilenceURL }}
  {{ end }}
  {{ if gt (len .DashboardURL ) 0 }}
    Go to dashboard: {{ .DashboardURL }}
  {{ end }}
{{ end }}
```

The following procedures show how to create, edit, and delete custom message
templates.

###### To create a message template

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page.
2. Choose **Contact points**.
3. From the **Alertmanager** dropdown, select the Alertmanager
   instance you want to create a message template for. The default is the Grafana
   Alertmanager.
4. Choose **Add template**.
5. Add a descriptive **Name**.
6. Add the **Content** for the template, for example:

```
{{ define "mymessage" }}
  {{ range .Alerts }}
    [{{ .Status }}] {{ range .Labels }} {{ .Name }}={{.Value }}{{end}}
  {{ end }}
{{ end }}
```

The `define` tag in the Content section assigns the template name.
This tag is optional, and when omitted, the template name is derived from the
**Name** field. When both are specified, it is a best
practice to keep them the same. 7. Choose **Save template**.

###### Note

HTML in alerting message templates is rendered as text, with control characters
escaped. Rendering of HTML in the resulting notification is not supported by
Grafana.

###### To edit a message template

1. In the **Alerting** page, choose **Contact
   points** to open the list of contact points.
2. In the **Template table**, find the template you want to
   edit, then choose the **Edit** icon (pen).
3. Make your changes, then choose **Save template**.

###### To delete a message template

1. In the **Alerting** page, choose **Contact
   points** to open the list of contact points.
2. In the **Template table**, find the template you want to
   remove, then choose the **Delete** icon (trash can).
3. Choose **Yes, delete** to delete the template.
   **Nested templates**

You can embed templates within other templates.

For example, you can define a template fragment using the `define`
keyword:

```
{{ define "mytemplate" }}
  {{ len .Alerts.Firing }} firing. {{ len .Alerts.Resolved }} resolved.
{{ end }}
```

You can then embed custom templates within this fragment using the
`template` keyword. For example:

```
Alert summary:
{{ template "mytemplate" . }}
```

You can use the following built-in template options to embed custom templates.

| Name              | Notes                                                       |
| ----------------- | ----------------------------------------------------------- |
| `default.title`   | Displays high-level status information.                     |
| `default.message` | Provides a formatted summary of firing and resolved alerts. |

**Custom template examples**

Here are examples of how to use custom templates.

Template to render a single alert:

```
{{ define "myalert" }}
  [{{.Status}}] {{ .Labels.alertname }}

  Labels:
  {{ range .Labels.SortedPairs }}
    {{ .Name }}: {{ .Value }}
  {{ end }}

  {{ if gt (len .Annotations) 0 }}
  Annotations:
  {{ range .Annotations.SortedPairs }}
    {{ .Name }}: {{ .Value }}
  {{ end }}
  {{ end }}

  {{ if gt (len .SilenceURL ) 0 }}
    Silence alert: {{ .SilenceURL }}
  {{ end }}
  {{ if gt (len .DashboardURL ) 0 }}
    Go to dashboard: {{ .DashboardURL }}
  {{ end }}
{{ end }}
```

Template to render entire notification message:

```
{{ define "mymessage" }}
  {{ if gt (len .Alerts.Firing) 0 }}
    {{ len .Alerts.Firing }} firing:
    {{ range .Alerts.Firing }} {{ template "myalert" .}} {{ end }}
  {{ end }}
  {{ if gt (len .Alerts.Resolved) 0 }}
    {{ len .Alerts.Resolved }} resolved:
    {{ range .Alerts.Resolved }} {{ template "myalert" .}} {{ end }}
  {{ end }}
{{ end }}
```

## Template data

The following data is passed to message templates.

| Name                | Type     | Notes                                                                                                                   |
| ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- |
| `Receiver`          | string   | Name of the contact point that the notification is being sent<br>to.                                                    |
| `Status`            | string   | firing if at least one alert is firing, otherwise<br>resolved.                                                          |
| `Alerts`            | Alert    | List of alert objects that are included in this notification<br>(see below).                                            |
| `GroupLabels`       | KeyValue | Labels these alerts were grouped by.                                                                                    |
| `CommonLabels`      | KeyValue | Labels common to all the alerts included in this<br>notification.                                                       |
| `CommonAnnotations` | KeyValue | Annotations common to all the alerts included in this<br>notification.                                                  |
| `ExternalURL`       | string   | Back link to the Grafana that sent the notification. If using<br>external Alertmanager, back link to this Alertmanager. |

The `Alerts` type exposes two functions for filtering the alerts
returned.

- `Alerts.Firing` – Returns a list of firing
  alerts.
- `Alerts.Resolved` – Returns a list of resolved
  alerts.

**Alert (type)**

The alert type contains the following data.

| Name         | Type      | Notes                                                                                                                                                |
| ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Status       | string    | `firing` or `resolved`.                                                                                                                              |
| Labels       | KeyValue  | A set of labels attached to the alert.                                                                                                               |
| Annotations  | KeyValue  | A set of annotations attached to the alert.                                                                                                          |
| StartsAt     | time.Time | Time the alert started firing.                                                                                                                       |
| EndsAt       | time.Time | Only set if the end time of an alert is known. Otherwise set<br>to a configurable timeout period from the time since the last<br>alert was received. |
| GeneratorURL | string    | A back link to Grafana or external Alertmanager.                                                                                                     |
| SilenceURL   | string    | Link to grafana silence for with labels for this alert<br>pre-filled. Only for Grafana managed alerts.                                               |
| DashboardURL | string    | Link to grafana dashboard, if alert rule belongs to one. Only<br>for Grafana managed alerts.                                                         |
| PanelURL     | string    | Link to grafana dashboard panel, if alert rule belongs to one.<br>Only for Grafana managed alerts.                                                   |
| Fingerprint  | string    | Fingerprint that can be used to identify the alert.                                                                                                  |
| ValueString  | string    | A string that contains the labels and value of each reduced<br>expression in the alert.                                                              |

**KeyValue type**

The `KeyValue` type is a set of key/value string pairs that represent
labels and annotations.

In addition to direct access of the data stored as a `KeyValue`, there
are also methods for sorting, removing and transforming the data.

| Name        | Arguments | Returns                                   | Notes                                                          |
| ----------- | --------- | ----------------------------------------- | -------------------------------------------------------------- |
| SortedPairs |           | Sorted list of key and value string pairs |                                                                |
| Remove      | []string  | KeyValue                                  | Returns a copy of the Key/Value map without the given<br>keys. |
| Names       |           | []string                                  | List of label names                                            |
| Values      |           | []string                                  | List of label values                                           |

## Template functions

Using template functions you can process labels and annotations to generate
dynamic notifications. The following functions are available.

| Name                 | Argument type                                                  | Return type            | Description                                                                                                                              |
| -------------------- | -------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `humanize`           | number or string                                               | string                 | Converts a number to a more readable format, using metric<br>prefixes.                                                                   |
| `humanize1024`       | number or string                                               | string                 | Like humanize, but uses 1024 as the base rather than<br>1000.                                                                            |
| `humanizeDuration`   | number or string                                               | string                 | Converts a duration in seconds to a more readable<br>format.                                                                             |
| `humanizePercentage` | number or string                                               | string                 | Converts a ratio value to a fraction of 100.                                                                                             |
| `humanizeTimestamp`  | number or string                                               | string                 | Converts a Unix timestamp in seconds to a more readable<br>format.                                                                       |
| `title`              | string                                                         | string                 | strings.Title, capitalizes first character of each<br>word.                                                                              |
| `toUpper`            | string                                                         | string                 | strings.ToUpper, converts all characters to upper case.                                                                                  |
| `toLower`            | string                                                         | string                 | strings.ToLower, converts all characters to lower case.                                                                                  |
| `match`              | pattern, text                                                  | boolean                | regexp.MatchString Tests for an unanchored regexp<br>match.                                                                              |
| `reReplaceAll`       | pattern, replacement, text                                     | string                 | Regexp.ReplaceAllString Regexp substitution,<br>unanchored.                                                                              |
| `graphLink`          | string<br>• JSON Object with `expr` and<br>`datasource` fields | string                 | Returns the path to graphical view in Explore for the given<br>expression and data source.                                               |
| `tableLink`          | string<br>• JSON Object with `expr` and<br>`datasource` fields | string                 | Returns the path to tabular view in Explore for the given<br>expression and data source.                                                 |
| `args`               | []interface{}                                                  | map[string]interface{} | Converts a list of objects to a map with keys, for example,<br>arg0, arg1. Use this function to pass multiple arguments to<br>templates. |
| `externalURL`        | nothing                                                        | string                 | Returns a string representing the external URL.                                                                                          |
| `pathPrefix`         | nothing                                                        | string                 | Returns the path of the external URL.                                                                                                    |

The following table shows examples of using each function.

| Function           | TemplateString                                                               | Input          | Expected                                                                                                                   |
| ------------------ | ---------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------- | -------- |
| humanize           | { humanize $value }                                                          | 1234567.0      | 1.235M                                                                                                                     |
| humanize1024       | { humanize1024 $value }                                                      | 1048576.0      | 1Mi                                                                                                                        |
| humanizeDuration   | { humanizeDuration $value }                                                  | 899.99         | 14m 59s                                                                                                                    |
| humanizePercentage | { humanizePercentage $value }                                                | 0.1234567      | 12.35%                                                                                                                     |
| humanizeTimestamp  | { humanizeTimestamp $value }                                                 | 1435065584.128 | 2015-06-23 13:19:44.128 +0000 UTC                                                                                          |
| title              | { $value                                                                     | title }        | aa bB CC                                                                                                                   | Aa Bb Cc |
| toUpper            | { $value                                                                     | toUpper }      | aa bB CC                                                                                                                   | AA BB CC |
| toLower            | { $value                                                                     | toLower }      | aa bB CC                                                                                                                   | aa bb cc |
| match              | { match "a+" $labels.instance }                                              | aa             | true                                                                                                                       |
| reReplaceAll       | {{ reReplaceAll "localhost:(.\*)" "my.domain:$1"<br>$labels.instance }}      | localhost:3000 | my.domain:3000                                                                                                             |
| graphLink          | {{ graphLink "{\"expr\": \"up\", \"datasource\":<br>\"gdev-prometheus\"}" }} |                | /explore?left=["now-1h","now","gdev-prometheus",{"datasource":"gdev-prometheus","expr":"up","instant":false,"range":true}] |
| tableLink          | {{ tableLink "{\"expr\":\"up\",<br>\"datasource\":\"gdev-prometheus\"}" }}   |                | /explore?left=["now-1h","now","gdev-prometheus",{"datasource":"gdev-prometheus","expr":"up","instant":true,"range":false}] |
| args               | {{define "x"}}{{.arg0}} {{.arg1}}{{end}}{{template "x" (args 1<br>"2")}}     |                | 1 2                                                                                                                        |
| externalURL        | { externalURL }                                                              |                | http://localhost/path/prefix                                                                                               |
| pathPrefix         | { pathPrefix }                                                               |                | /path/prefix                                                                                                               |
