# Silencing alert notifications for Prometheus data

sources

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For external Alertmanager data sources (including Amazon Managed Service for Prometheus), you can suppress alert
notifications with a _silence_. A silence only stops notifications
from being created: Silences do not prevent alert rules from being evaluated, and they
do not stop alerting instances from being shown in the user interface. When you silence
an alert, you specify a window of time for it to be suppressed.

You can configure silences for an external Alertmanager data source.

###### Note

To suppress alert notifications at regular time intervals (for example, during
regular maintenance periods), use [Mute timings](alert-notifications.md#alert-notification-muting "alert-notifications.md#alert-notification-muting") rather than silences.

###### To add a silence

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page.
2. Choose **Silences** to open a page listing existing [contact points](alert-contact-points.md "alert-contact-points.md").
3. Choose the external Alertmanager from the **Alertmanager**
   dropdown.
4. Select **New Silence**.
5. Select the start and end date in **Silence start and end** to
   indicate when the silence should go into effect and when it should end.

As an alternative to setting an end time, in **Duration**,
specify how long the silence is enforced. This automatically updates the end
time in the **Silence start and end** field. 6. In the **Name** and **Value** fields, enter
one or more _Matching Labels_. Matchers
determine which rules the silence applies to. Label matching is discussed in
more detail following this procedure. 7. Optionally, add a **Comment**, or modify the
**Creator** to set the owner of the silence.
**Label matching for alert suppression**

When you create a silence, you create a set of _matching labels_ as
part of the silence. This is a set of rules about labels that must match for the alert
to be suppressed. The matching labels consist of three parts:

- **Label** – The name of the label to
  match. It must exactly match the label name of the alert.
- **Operator** – The operator used to
  compare the label value with the matching label value. The available operators
  are:
  - `=` Select labels whose value exactly matches the provided
    string.
  - `!=` Select labels whose value does not match the provided
    string.
  - `=~` Select labels whose value match the regex interpreted
    value of the provided string (the provided string is interpreted as a
    regular expression).
  - `!=` Select labels that do not match the provided regular
    expression.

- **Value** – The value to match the label
  value to. It can match as a string or as a regular expression, depending on the
  operator chosen.
  A silence ends at the indicated end date, but you can manually end the suppression at
  any time.

###### To end a silence manually

1. In the **Alerting** page, choose
   **Silences** to view the list of existing silences.
2. Select the silence that you want to end, and choose
   **Unsilence**. This ends the alert suppression.

###### Note

Unsilencing ends the alert suppression, as if the end time was set for the
current time. Silences that have ended (automatically or manually) are
retained and listed for five days. You cannot remove a silence from the list
manually.
**Creating a link to the silence creation form**

You can create a URL to the silence creation form with details already filled in.
Operators can use this to suppress an alarm quickly during an operational event.

When creating a link to a silence form, use a `matchers` query parameter to
specify the matching labels, and a `comment` query parameter to specify a
comment. The `matchers` parameter requires one or more values in the form
`[label][operator][value]`, separated by commas.

**Example URL**

To link to a silence form, with matching labels `severity=critical` and
`cluster!~europe-.*`, with a comment that says `Silencing critical
 EU alerts`, use a URL like the following. Replace
`mygrafana` with the hostname of your Grafana
instance.

```
https://`mygrafana`/alerting/silence/new?matchers=severity%3Dcritical%2Ccluster!~europe-*&comment=Silence%20critical%20EU%20alert
```

To link to a new silence page for an external Alertmanager, add an
`alertmanager` query parameter with the Alertmanage data source name,
such as `alertmanager=myAlertmanagerdatasource`.
