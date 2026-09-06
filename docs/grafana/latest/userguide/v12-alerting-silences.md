

# Silencing alert notifications
<a name="v12-alerting-silences"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 12.x**.  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

You can suppress alert notifications with a *silence*. A silence only stops notifications from being created: Silences do not prevent alert rules from being evaluated, and they do not stop alerting instances from being shown in the user interface. When you silence an alert, you specify a window of time for it to be suppressed.

**Note**  
To suppress alert notifications at regular time intervals, for example, during regular maintenance periods, use [Mute timings](v12-alerting-manage-muting.md) rather than silences.

**To add a silence**

1. From your Grafana console, in the Grafana menu, choose **Alerting**.

1. Choose **Silences**.

1. Choose an Alertmanager from the **Alertmanager** dropdown.

1. Choose **Create Silence**.

1. Select the start and end date in **Silence start and end** to indicate when the silence should go into effect and when it should end.

1. As an alternative to setting an end time, in **Duration**, specify how long the silence is enforced. This automatically updates the end time in the **Silence start and end** field.

1. In the **Label** and **Value** fields, enter one or more *Matching Labels*. Matchers determine which rules the silence applies to. Any matching alerts (in firing state), will show in the **Affected alerts instances** field.

1. Optionally, add a **Comment** describing the silence.

1. Choose **Submit**.

**To edit a silence**

1. From your Grafana console, in the Grafana menu, choose **Alerting**.

1. Choose **Silences** to view the list of existing silences.

1. Find the silence you want to edit, then choose **Edit** (pen icon).

1. Make any desired changes, then choose **Submit** to save your changes.

You can edit an existing silence by choosing the **Edit** icon (pen).

**To create a URL link to a silence form**

When linking to a silence form, provide the default matching labels and comment via `matcher` and `comment` query parameters. The `matcher` parameter should be in the following format `[label][operator][value]` where the `operator` parameter can be one of the following: `=` (equals, not regex), `!=` (not equals, not regex), `=~` (equals, regex), `!~` (not equals, regex). The URL can contain many query parameters with the key `matcher`. For example, to link to silence form with matching labels `severity=critical` & `cluster!~europe-.*` and comment `Silence critical EU alerts`, create a URL `https://mygrafana/alerting/silence/new?matcher=severity%3Dcritical&matcher=cluster!~europe-*&comment=Silence%20critical%20EU%20alert`.

To link to a new silence page for an external Alertmanager, add an `alertmanager` query parameter

**To remove a silence**

1. From your Grafana console, in the Grafana menu, choose **Alerting**.

1. Choose **Silences** to view the list of existing silences.

1. Select the silence that you want to end, and choose **Unsilence**. This ends the alert suppression.
**Note**  
Unsilencing ends the alert suppression, as if the end time was set for the current time. Silences that have ended (automatically or manually) are retained and listed for five days. You cannot remove a silence from the list manually.