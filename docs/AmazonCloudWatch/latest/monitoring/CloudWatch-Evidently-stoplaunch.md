# Stop a launch

###### Important

End of support notice: On October 16, 2025, AWS 
 will discontinue support for CloudWatch Evidently. After October 16, 2025, you will 
 no longer be able to access the Evidently console or Evidently resources. 
 

If you stop an ongoing launch, you will not be able to resume it or restart it. Also, it 
 will not be evaluated as a rule for traffic allocation, and the traffic that was allocated to the launch
 will instead be available to the feature's experiment, if there is one. Otherwise, all traffic
 will be served the default variation after the launch is stopped.

###### To permanently stop a launch

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **Evidently**.
3. Choose the name of the project that contains the launch.
4. Choose the **Launch** tab.
5. Choose the button to the left of the name of the launch.
6. Choose **Actions**, **Cancel launch**
 or **Actions**, **Mark as complete**.
