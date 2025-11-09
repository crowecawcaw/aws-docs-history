# Configure contact

points

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Use contact points to define how your contacts are notified when an alert rule
fires.

###### Note

You can create and edit contact points for Grafana managed alerts. Contact points
for data source managed alerts are read-only.

## Working with contact points

The following procedures show how to add, edit, delete, and test a contact
point.

###### To add a contact point

1. In the left-side menu, choose **Alerting**.
2. Choose **Contact points**.
3. From the **Choose Alertmanager** dropdown, select an
   Alertmanager. The Grafana Alertmanager is selected by default.
4. On the **Contact Points** tab, choose **+ Add
   contact point**.
5. Enter a **Name** for the contact point.
6. From **Integration**, choose a type, and fill out the
   mandatory fields based on that type. For example, if you choose Slack,
   enter the Slack channels and users who should be contacted.
7. If available for the contact point you selected, choose any desired
   **Optional settings** to specify additional
   settings.
8. Under **Notification settings**, optionally select
   **Disable resolved message** if you do not want to be
   notified when an alert resolves.
9. To add another contact point integration, choose **Add contact
   point integration** and repeat the steps for each contact point
   type needed.
10. Save your changes.

###### To edit a contact point

1. In the left-side menu, choose **Alerting**.
2. Choose **Contact points** to see a list of existing
   contact points.
3. Select the contact point to edit, then choose
   **Edit**.
4. Update the contact point, and then save your changes.

You can delete contact points that are not in use by a notification policy.

###### To delete a contact point

1. In the left-side menu, choose **Alerting**.
2. Choose **Contact points** to open the list of existing
   contact points.
3. On the **Contact points**, select the contact point to
   delete, then choose **More**,
   **Delete**.
4. In the confirmation dialog box, choose **Yes,
   delete**.

###### Note

If the contact point is in use by a notification policy, you must delete the
notification policy or edit it to use a different contact point before deleting
the contact point.

After your contact point is created, you can send a test notification to verify
that it is configured properly.

###### To send a test notification

1. In the left-side menu, choose **Alerting**.
2. Choose **Contact points** to open the list of existing
   contact points.
3. On the **Contact points**, select the contact point to
   test, then choose **Edit**. You can also create a new
   contact point if needed.
4. Choose **Test** to open the contact point testing
   dialog.
5. Choose whether to send a predefined test notification or choose
   **Custom** to add your own custom annotations and
   labels in the test notification.
6. Choose **Send test notification** to test the alert with
   the given contact points.

## Configure

contact point integrations

Configure contact point integrations in Grafana to select your preferred
communication channel for receiving notifications when your alert rules are
firing. Each integration has its own configuration options and setup process.
In most cases, this involves providing an API key or a Webhook URL.

Once configured, you can use integrations as part of your contact points to
receive notifications whenever your alert changes its state. In this section,
we’ll cover the basic steps to configure an integration, using PagerDuty as an
example, so you can start receiving real-time alerts and stay on top of your
monitoring data.

**List of supported integrations**

The following table lists the contact point types supported by Grafana.

| Name       | Type        |
| ---------- | ----------- |
| Amazon SNS | `sns`       |
| OpsGenie   | `opsgenie`  |
| Pager Duty | `pagerduty` |
| Slack      | `slack`     |
| VictorOps  | `victorops` |

**Configuring PagerDuty for alerting**

To set up PagerDuty, you must provide an integration key. Provide the
following details.

| Setting         | Description                                                |
| --------------- | ---------------------------------------------------------- |
| Integration Key | Integration key for PagerDuty                              |
| Severity        | Level for dynamic notifications. Default is<br>`critical`. |
| Custom Details  | Additional details about the event                         |

The `CustomDetails` field is an object containing arbitrary
key-value pairs. The user-defined details are merged with the ones used by
default.

The default values for `CustomDetails` are:

```
{
	"firing":       `{{ template "__text_alert_list" .Alerts.Firing }}`,
	"resolved":     `{{ template "__text_alert_list" .Alerts.Resolved }}`,
	"num_firing":   `{{ .Alerts.Firing | len }}`,
	"num_resolved": `{{ .Alerts.Resolved | len }}`,
}
```

In case of duplicate keys, the user-defined details overwrite the default
ones.
