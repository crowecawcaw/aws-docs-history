# Modify launch traffic

###### Important

End of support notice: On October 16, 2025, AWS 
 will discontinue support for CloudWatch Evidently. After October 16, 2025, you will 
 no longer be able to access the Evidently console or Evidently resources. 
 

You can modify the traffic allocation for a launch at any time, including while the launch
 is ongoing.

If you have both an ongoing launch and an ongoing experiment for the same feature, any changes
 to the feature traffic will cause a change in the experiment traffic. This is because the audience
 available to the experiment is the portion of your total audience that is not already allocated to the launch. 
 Increasing launch traffic will descrease the audience available to the experiment, and decreasing launch traffic
 or ending the launch will increase the audience available to the experiment.

###### To modify the traffic allocation for a launch

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **Evidently**.
3. Choose the name of the project that contains the launch.
4. Choose the **Launches** tab.
5. Choose the name of the launch.


Choose **Modify launch traffic**.
6. For **Serve**, select the new traffic percentage to assign to each variation. You can 
 also choose to exclude variations from being served to users. As you change these values, 
 you can see the updated effects on your overall feature traffic under **Traffic summary**.


The **Traffic summary** shows how much of your overall traffic is available
 for this launch, and how much of that available traffic is allocated to this launch.
7. Choose **Modify**.
