# View launch results in the dashboard

###### Important

End of support notice: On October 16, 2025, AWS 
 will discontinue support for CloudWatch Evidently. After October 16, 2025, you will 
 no longer be able to access the Evidently console or Evidently resources. 
 

You can see the progress and metric results of an experiment while it is ongoing and after it is completed.

###### To see the progress and results of a launch

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **Evidently**.
3. Choose the name of the project that contains the launch.
4. Choose the **Launch** tab.
5. Choose the name of the launch.
6. To see the launch steps and the traffic allocations for each step, 
 choose the **Launch** tab.
7. To see the number of user sessions assigned to each variation over time, and to 
 view the performance metrics for each variation in the launch, choose
 the **Monitoring** tab.


This view also displays whether any launch alarms have gone into
 `ALARM` state during the launch.
8. To see the variations, metrics, alarms, and tags for this launch,
 choose the **Configuration** tab.
