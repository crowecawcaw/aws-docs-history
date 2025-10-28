# View alert history or job reports

###### To view alert history or job reports of failed executions, complete the following

steps:

1.  Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2.  Choose **Governance** in the left panel.
3.  Choose **Model Dashboard**.
4.  In the **Models** section of the Model Dashboard, select the model name of
    the alert history you want to view.
5.  In the **Schedule name** column, select the monitor name of the
    alert history you want to view.
6.  To view alert history, select the **Alert history** tab.
7.  (optional) To view job reports of monitoring executions, complete the following
    steps:
    1. In the **Alert history** tab, choose **View
       executions** for the alert you want to investigate.
    2. In the **Execution history** table, choose **View
       report** of the monitoring execution you want to investigate.

    ###### The report displays the following information:

        * **Feature**: The user-defined ML feature monitored
        * **Constraint**: The specific check within the
         monitor
        * **Violation details**: Information about why the
         constraint was violated
