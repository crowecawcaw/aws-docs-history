

# Opting out of Cost Anomaly Detection
<a name="opting-out-cad"></a>

You can opt out of Cost Anomaly Detection at any time. To opt out, you need to delete all cost monitors and alert subscriptions in your account. After you opt out, Cost Anomaly Detection no longer monitors your spend patterns for anomalies. You also won’t receive any further notifications.

**To opt out of Cost Anomaly Detection**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Anomaly Detection**.

1. To delete any existing cost monitors:

   1. Choose the **Cost monitors** tab.

   1. Select the cost monitor that you want to delete.

   1. Choose **Delete**.

   1. In the **Delete cost monitor** dialog box, choose **Delete**.

   1. Repeat the steps for any additional cost monitors.

1. To delete any existing alert subscriptions:

   1. Choose the **Alert subscriptions** tab.

   1. Select the alert subscription that you want to delete.

   1. Choose **Delete**.

   1. In the **Delete alert subscription** dialog box, choose **Delete**.

   1. Repeat the steps for any additional alert subscriptions.

**Note**  
You can also opt out of Cost Anomaly Detection by deleting your cost monitors and alert subscriptions in the Cost Explorer API. To do so, you need to use [DeleteAnomalyMonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteAnomalyMonitor.html) and [DeleteAnomalySubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteAnomalySubscription.html).