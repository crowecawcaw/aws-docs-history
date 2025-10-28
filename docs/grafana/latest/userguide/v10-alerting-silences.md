# Silencing alert notifications

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can suppress alert notifications with a _silence_. A
silence only stops notifications from being created: Silences do not prevent alert
rules from being evaluated, and they do not stop alerting instances from being
shown in the user interface. When you silence an alert, you specify a window of
time for it to be suppressed.

###### Note

To suppress alert notifications at regular time intervals, for example,
during regular maintenance periods, use
[Mute timings](v10-alerting-manage-muting.md "v10-alerting-manage-muting.md") rather than silences.

###### To add a silence

1. From your Grafana console, in the Grafana menu, choose
   **Alerting**.
2. Choose **Silences**.
3. Choose an Alertmanager from the **Alertmanager**
   dropdown.
4. Choose **Create Silence**.
5. Select the start and end date in **Silence start and
   end** to indicate when the silence should go into effect and when
   it should end.
6. As an alternative to setting an end time, in **Duration**,
   specify how long the silence is enforced. This automatically updates the end
   time in the **Silence start and end** field.
7. In the **Label** and **Value** fields,
   enter one or more _Matching Labels_.
   Matchers determine which rules the silence applies to. Any matching alerts
   (in firing state), will show in the **Affected alerts
   instances** field.
8. Optionally, add a **Comment** describing the
   silence.
9. Choose **Submit**.

###### To edit a silence

1. From your Grafana console, in the Grafana menu, choose
   **Alerting**.
2. Choose **Silences** to view the list of existing silences.
3. Find the silence you want to edit, then choose **Edit**
   (pen icon).
4. Make any desired changes, then choose **Submit** to save
   your changes.
   You can edit an existing silence by choosing the **Edit** icon
   (pen).

**To create a URL link to a silence form**

When linking to a silence form, provide the default matching labels and comment
via `matcher` and `comment` query parameters. The
`matcher` parameter should be in the following format
`[label][operator][value]` where the `operator` parameter can
be one of the following: `=` (equals, not regex), `!=` (not
equals, not regex), `=~` (equals, regex), `!~` (not equals,
regex). The URL can contain many query parameters with the key `matcher`.
For example, to link to silence form with matching labels
`severity=critical` & `cluster!~europe-.*` and comment
`Silence critical EU alerts`, create a URL
`https://mygrafana/alerting/silence/new?matcher=severity%3Dcritical&matcher=cluster!~europe-*&comment=Silence%20critical%20EU%20alert`.

To link to a new silence page for an external Alertmanager, add an
`alertmanager` query parameter

###### To remove a silence

1. From your Grafana console, in the Grafana menu, choose
   **Alerting**.
2. Choose **Silences** to view the list of existing silences.
3. Select the silence that you want to end, and choose
   **Unsilence**. This ends the alert suppression.

###### Note

Unsilencing ends the alert suppression, as if the end time was set for the
current time. Silences that have ended (automatically or manually) are
retained and listed for five days. You cannot remove a silence from the list
manually.
