

# Working with contact points
<a name="v9-alerting-contact-points"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 9.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

Use contact points to define how your contacts are notified when an alert is initiated. A contact point can have one or more contact point integrations, for example, Amazon Simple Notification Service or Slack. When an alert is initiated, a notification is sent to all contact point integrations listed for a contact point. Optionally, use [notification templates](v9-alerting-create-templates.md) to customize the notification messages for the contact point types.

**Note**  
You can create and edit contact points for Grafana managed alerts. Contact points for Alertmanager alerts are read-only.

## Working with contact points
<a name="v9-alerting-working-contact-points"></a>

The following procedures detail how to add, edit, test, and delete contact points.

**To add a contact point**

1. From your Grafana console, in the Grafana menu, choose the **Alerting** (bell) icon to open the **Alerting** page.

1. Choose **Contact points**, then **Add contact point**.

1. From the **Alertmanager** dropdown, select an Alertmanager. The Grafana Alertmanager is selected by default.

1. Enter a **Name** for the contact point.

1. From **Contact point integration**, choose a type, and the mandatory fields based on that type. For example, if you choose Slack, enter the Slack channels and users who should be contacted.

1. If available for the contact point you selected, choose any desired **Optional settings** to specify additional settings.

1. Under **Notification settings**, optionally select **Disable resolved message** if you do not want to be notified when an alert resolves.

1. If your contact point needs more contact points types, you can choose **Add contact point integration** and repeat the steps for each contact point type needed.

1. Choose **Save contact point** to save your changes.

**To edit a contact point**

1. Choose **Contact points** to see a list of existing contact points.

1. Select the contact point to edit, then choose the **Edit** icon (pen).

1. Make any necessary changes, and then choose **Save contact point** to save your changes.

After your contact point is created, you can send a test notification to verify that it is configured properly.

**To send a test notification**

1. Choose **Contact points** to open the list of existing contact points.

1. Select the contact point to test, then choose the **Edit** icon (pen).

1. Select the **Test** icon (paper airplane).

1. Choose whether to send a predefined test notification or choose **Custom** to add your own custom annotations and labels in the test notification.

1. Choose **Send test notification** to test the alert with the given contact points.

You can delete contact points that are not in use by a notification policy.

**To delete a contact point**

1. Choose **Contact points** to open the list of existing contact points.

1. Select the contact point to delete, then choose the **Delete** icon (trash can).

1. In the confirmation dialog box, choose **Yes, delete**.

**Note**  
If the contact point is in use by a notification policy, you must delete the notification policy or edit it to use a different contact point before deleting the contact point.

## List of supported notifiers
<a name="v9-alerting-contactpoint-supported-notifiers"></a>


|  Name  |  Type  | 
| --- | --- | 
| Amazon SNS  |  sns  | 
|  OpsGenie  |  opsgenie  | 
| Pager Duty  |  pagerduty  | 
| Slack  |  slack  | 
|  VictorOps  |  victorops  | 