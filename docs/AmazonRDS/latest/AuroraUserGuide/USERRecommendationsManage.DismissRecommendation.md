

# Dismissing Amazon Aurora recommendations
<a name="USERRecommendationsManage.DismissRecommendation"></a>

You can dismiss one or more Amazon Aurora recommendations using the Amazon RDS console, AWS CLI, or Amazon RDS API.

## Console
<a name="USERRecommendationsManage.DismissRecommendation-Console"></a>

**To dismiss one or more recommendations**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, perform any of the following:
   + Choose **Recommendations**.

     The **Recommendations** page appears with the list of all recommendations.
   + Choose **Databases** and then choose **Recommendations** for a resource in the databases page.

     The details appear in the **Recommendations** tab for the selected recommendation.
   + Choose **Detection** for an active recommendation in the **Recommendations** page or the **Recommendations** tab in the **Databases** page.

     The recommendation details page displays the list of affected resources.

1. Choose one or more recommendation, or one or more affected resources in the recommendation details page, and then choose **Dismiss**.

   The following example shows the **Recommendations** page with multiple active recommendations selected to dismiss.  
![A few active recommendations selected and dismiss button highlighted in the console.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/Recommendations_Dismiss.png)

   A banner displays a message when the selected one or more recommendations are dismissed.

   The following example shows the banner with the successful message.   
![Console banner showing the number of resources successfully updated.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/Recommendation-Dismiss-Banner.png)

   The following example shows the banner with the failure message.  
![Console banner showing the resource that failed to update.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/Recommendation-Dismiss-Banner-failure.png)

## CLI
<a name="USERRecommendationsManage.DismissRecommendation-Cli"></a>

**To dismiss an Aurora recommendation using the AWS CLI**

1. Run the command `aws rds describe-db-recommendations --filters "Name=status,Values=active"`.

   The output provides a list of recommendations in `active` status.

1. Find the `recommendationId` for the recommendation that you want to dismiss from step 1.

1. Run the command `>aws rds modify-db-recommendation --status dismissed --recommendationId <ID>` with the `recommendationId` from step 2 to dismiss the recommendation.

## RDS API
<a name="USERRecommendationsManage.DismissRecommendation-API"></a>

To dismiss an Aurora recommendation using the Amazon RDS API, use the [ModifyDBRecommendation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBRecommendation.html) operation.