# Modify a launch's future steps

###### Important

End of support notice: On October 16, 2025, AWS 
 will discontinue support for CloudWatch Evidently. After October 16, 2025, you will 
 no longer be able to access the Evidently console or Evidently resources. 
 

You can modify the configuration of launch steps that haven't happened yet, and also
 add more steps to a launch.

###### To modify the steps for a launch

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **Evidently**.
3. Choose the name of the project that contains the launch.
4. Choose the **Launches** tab.
5. Choose the name of the launch.


Choose **Modify launch traffic**.
6. Choose **Schedule launch**.
7. For any steps that have not started yet, you can modify the percentage of the available
 audience to use in the experiment. You can also modify how their traffic is
 allocated among the variations.


You can add more steps to the launch by choosing **Add another
 step**. A launch can have a maximum of five steps.
8. Choose **Modify**.
