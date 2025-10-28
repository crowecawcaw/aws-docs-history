# Working with contact points

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Use contact points to define how your contacts are notified when an alert is
initiated. A contact point can have one or more contact point types, for example,
Amazon Simple Notification Service or Slack. When an alert is initiated, a notification is sent to all contact
point types listed for a contact point. Optionally, use [Using messaging templates](alert-message-templates.md "alert-message-templates.md") to
customize the notification messages for the contact point types.

###### Note

You can create and edit contact points for Grafana managed alerts. Contact points
for Alertmanager alerts are read-only.

## Working with contact points

The following procedures detail how to add, edit, test, and delete contact
points.

###### To add a contact point

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page.
2. Choose **Contact points**, then **New contact
   point**.
3. From the **Alertmanager** dropdown, select an
   Alertmanager. The Grafana Alertmanager is selected by default.
4. Enter a **Name** for the contact point.
5. From **Contact point type**, choose a type, and the
   mandatory fields based on that type. For example, if you choose Slack, enter
   the Slack channels and users who should be contacted.
6. If available for the contact point you selected, optionally choose the
   **Optional settings** to specify additional
   settings.
7. Under **Notification settings**, optionally select
   **Disable resolved message** if you do not want to be
   notified when an alert resolves.
8. If your contact point needs more contact points types, you can chooose
   **New contact point type** and repeat the steps for
   each contact point type needed.
9. Choose **Save contact point** to save your
   changes.

###### To edit a contact point

1. Choose **Contact points** to see a list of existing
   contact points.
2. Select the contact point to edit, then choose the
   **Edit** icon (pen).
3. Make any necessary changes, and then choose **Save contact
   point** to save your changes.

After your contact point is created, you can send a test notification to verify
that it is configured properly.

###### To send a test notification

1. Choose **Contact points** to open the list of existing
   contact points.
2. Select the contact point to test, then choose the
   **Edit** icon (pen).
3. Select the **Test** icon (paper airplane).
4. Choose whether to send a predefined test notification or choose
   **Custom** to add your own custom annotations and
   labels in the test notification.
5. Choose **Send test notification** to test the alert with
   the given contact points.

You can delete contact points that are not in use by a notification policy.

###### To delete a contact point

1. Choose **Contact points** to open the list of existing
   contact points.
2. Select the contact point to delete, then choose the
   **Delete** icon (trash can).
3. In the confirmation dialog box, choose **Yes,
   delete**.

###### Note

If the contact point is in use by a notification policy, you must delete the
notification policy or edit it to use a different contact point before deleting
the contact point.

## List of supported notifiers

| Name       | Type        |
| ---------- | ----------- |
| Amazon SNS | `sns`       |
| OpsGenie   | `opsgenie`  |
| Pager Duty | `pagerduty` |
| Slack      | `slack`     |
| VictorOps  | `victorops` |
