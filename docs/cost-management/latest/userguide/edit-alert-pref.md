

# Editing your alert preferences
<a name="edit-alert-pref"></a>

You can adjust your cost monitors and alert subscriptions in AWS Billing and Cost Management to match your needs. 

You can also edit your notification configurations in AWS User Notifications.

**Note**  
When using AWS managed monitors, consider that a single threshold applies to all tracked values. If you need different alert thresholds for different teams or accounts, you can:  
Create supplementary customer managed monitors with dedicated alert subscriptions with specific thresholds
Use AWS User Notifications to filter and route alerts based on anomaly attributes
Configure Amazon Amazon SNS topics with custom logic for alert routing 

------
#### [ Cost monitors ]<a name="edit-cost-monitor"></a>

**To edit your cost monitors**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Anomaly Detection**.

1. Choose the **Cost monitors** tab.

1. Select the monitor that you want to edit.

1. Choose **Edit**.
   + (Alternative) Choose the individual monitor name.
   + Choose **Edit monitor**.

1. On the **Edit monitor** page, change any settings for **monitor name ** and **attached alert subscriptions**.

1. Choose **Manage tags** to add, edit, or remove tags for the monitor.

1. Choose **Save**.

------
#### [ Alert subscriptions ]<a name="edit-alert-process"></a>

**To edit your alert subscriptions**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Anomaly Detection**.

1. Choose the **Alert subscriptions** tab.

1. Select the subscription that you want to edit.

1. Choose **Edit**.
   + (Alternative) Choose the individual monitor name.
   + Choose **Edit**.

1. On the **Edit alert subscription** page, change any settings for **subscription name**, **threshold**, **frequency**, **recipients**, or **cost monitors**.

1. Choose **Manage tags** to add, edit, or remove tags for the monitor.

1. Choose **Save**.

------
#### [ AWS User Notifications ]

For information about how to edit your notification configurations, see [Editing notification configurations in AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/edit-notifications.html) in the *AWS User Notifications User Guide*.

------