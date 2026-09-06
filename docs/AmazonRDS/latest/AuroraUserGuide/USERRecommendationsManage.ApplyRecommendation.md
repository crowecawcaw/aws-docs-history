

# Applying Amazon Aurora recommendations
<a name="USERRecommendationsManage.ApplyRecommendation"></a>

To apply Amazon Aurora recommendations using the Amazon RDS console, select a configuration based recommendation or an affected resource in the details page. Then, choose to apply the recommendation immediately or schedule it for the next maintenance window. The resource might need to restart for the change to take effect. For a few DB parameter group recommendations, you might need to restart the resources.

The threshold based proactive or anomaly based reactive recommendations won't have the apply option and might need additional review.

## Console
<a name="USERRecommendationsManage.ApplyRecommendation-Console"></a>

**To apply a configuration based recommendation**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, perform any of the following:
   + Choose **Recommendations**.

     The **Recommendations** page appears with the list of all recommendations.
   + Choose **Databases** and then choose **Recommendations** for a resource in the databases page.

     The details appear in the **Recommendations** tab for the selected recommendation.
   + Choose **Detection** for an active recommendation in the **Recommendations** page or the **Recommendations** tab in the **Databases** page.

     The recommendation details page appears.

1. Choose a recommendation, or one or more affected resources in the recommendation details page, and do any of the following:
   + Choose **Apply** and then choose **Apply immediately** to apply the recommendation immediately.
   + Choose **Apply** and then choose **Apply in next maintenance window** to schedule in the next maintenance window.

     The selected recommendation status is updated to pending until the next maintenance window.  
![An active recommendation selected and Apply button with its options highlighted in the console.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/Recommendations_Apply_Defer.png)

   A confirmation window appears.

1. Choose **Confirm application** to apply the recommendation. This window confirms whether the resources need an automatic or manual restart for the changes to take effect.

   The following example shows the confirmation window to apply the recommendation immediately.  
![The confirmation window in the console to apply the recommendation immediately.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/Recommendations_ApplyImmediately.png)

   The following example shows the confirmation window to schedule applying the recommendation in the next maintenance window.  
![The confirmation window in the console to schedule applying the recommendation in the next maintenance window.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/Recommendations_Defer.png)

   A banner displays a message when the recommendation applied is successful or has failed.

   The following example shows the banner with the successful message.   
![Console banner showing the number of resources to apply the recommendation to.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/Recommendation-Apply-Banner.png)

   The following example shows the banner with the failure message.   
![Console banner showing the resource that failed to apply the recommendation.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/Recommendation-Apply-Banner-failure.png)

## RDS API
<a name="USERRecommendationsManage.ApplyRecommendation-API"></a>

**To apply a configuration based Aurora recommendation using the Amazon RDS API**

1. Use the [DescribeDBRecommendations](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBRecommendations.html) operation. The `RecommendedActions` in the output can have one or more recommended actions.

1. Use the [RecommendedAction](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RecommendedAction.html) object for each recommended action from step 1. The output contains `Operation` and `Parameters`.

   The following example shows the output with one recommended action.

   ```
       "RecommendedActions": [
           {
               "ActionId": "0b19ed15-840f-463c-a200-b10af1b552e3",
               "Title": "Turn on auto backup", // localized
               "Description": "Turn on auto backup for my-mysql-instance-1", // localized
               "Operation": "ModifyDbInstance",
               "Parameters": [
                   {
                       "Key": "DbInstanceIdentifier",
                       "Value": "my-mysql-instance-1"
                   },
                   {
                       "Key": "BackupRetentionPeriod",
                       "Value": "7"
                   }
               ],
               "ApplyModes": ["immediately", "next-maintenance-window"],
               "Status": "applied"
           },
           ... // several others
       ],
   ```

1. Use the `operation` for each recommended action from the output in step 2 and input the `Parameters` values.

1. After the operation in step 2 is successful, use the [ModifyDBRecommendation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBRecommendation.html) operation to modify the recommendation status.