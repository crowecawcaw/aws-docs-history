# Opting out of Cost Anomaly Detection

You can opt out of Cost Anomaly Detection at any time. To opt out, you need to delete all cost monitors
and alert subscriptions in your account. After you opt out, Cost Anomaly Detection no longer monitors your
spend patterns for anomalies. You also won’t receive any further notifications.

###### To opt out of Cost Anomaly Detection

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Anomaly Detection**.
3. To delete any existing cost monitors:
   1. Choose the **Cost monitors** tab.
   2. Select the cost monitor that you want to delete.
   3. Choose **Delete**.
   4. In the **Delete cost monitor** dialog box, choose
      **Delete**.
   5. Repeat the steps for any additional cost monitors.

4. To delete any existing alert subscriptions:
   1. Choose the **Alert subscriptions** tab.
   2. Select the alert subscription that you want to delete.
   3. Choose **Delete**.
   4. In the **Delete alert subscription** dialog box,
      choose **Delete**.
   5. Repeat the steps for any additional alert subscriptions.

###### Note

You can also opt out of Cost Anomaly Detection by deleting your cost monitors and alert
subscriptions in the Cost Explorer API. To do so, you need to use [DeleteAnomalyMonitor](../../../aws-cost-management/latest/APIReference/API_DeleteAnomalyMonitor.md "../../../aws-cost-management/latest/APIReference/API_DeleteAnomalyMonitor.md") and [DeleteAnomalySubscription](../../../aws-cost-management/latest/APIReference/API_DeleteAnomalySubscription.md "../../../aws-cost-management/latest/APIReference/API_DeleteAnomalySubscription.md").
