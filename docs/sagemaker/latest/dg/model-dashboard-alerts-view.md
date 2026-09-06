

# View alert history or job reports
<a name="model-dashboard-alerts-view"></a>

**To view alert history or job reports of failed executions, complete the following steps:**

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/).

1. Choose **Governance** in the left panel.

1. Choose **Model Dashboard**.

1. In the **Models** section of the Model Dashboard, select the model name of the alert history you want to view.

1. In the **Schedule name** column, select the monitor name of the alert history you want to view.

1. To view alert history, select the **Alert history** tab.

1. (optional) To view job reports of monitoring executions, complete the following steps:

   1. In the **Alert history** tab, choose **View executions** for the alert you want to investigate.

   1. In the **Execution history** table, choose **View report** of the monitoring execution you want to investigate.

**The report displays the following information:**
      + **Feature**: The user-defined ML feature monitored
      + **Constraint**: The specific check within the monitor
      + **Violation details**: Information about why the constraint was violated