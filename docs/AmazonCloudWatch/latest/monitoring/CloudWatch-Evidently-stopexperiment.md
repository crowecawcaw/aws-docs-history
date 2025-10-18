# Stop an experiment

###### Important

End of support notice: On October 16, 2025, AWS 
 will discontinue support for CloudWatch Evidently. After October 16, 2025, you will 
 no longer be able to access the Evidently console or Evidently resources. 
 

If you stop an ongoing experiment, you will not be able to resume it or restart it. The portion of traffic
 that was previously used in the experiment will be served the default variation.

When an experiment is not manually stopped and passes its end date, the traffic does not change. 
 The portion of traffic allocated to the experiment still goes to the experiment. To stop this, and cause
 the experiment traffic to instead be served the default variation, mark the experiment as complete.

When you stop an experiment, you can choose to cancel it or mark it as complete. If you cancel, it will 
 be shown as **Cancelled** in the list of experiments. If you choose to mark it as complete,
 it is shown as **Completed**.

###### To permanently stop an experiment

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **Evidently**.
3. Choose the name of the project that contains the experiment.
4. Choose the **Experiments** tab.
5. Choose the button to the left of the name of the experiment.
6. Choose **Actions**, **Cancel experiment**
 or **Actions**, **Mark as complete**.
