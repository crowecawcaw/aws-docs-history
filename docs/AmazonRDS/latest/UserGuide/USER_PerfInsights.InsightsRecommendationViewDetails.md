

# Viewing Database Insights proactive recommendations
<a name="USER_PerfInsights.InsightsRecommendationViewDetails"></a>

Amazon RDS monitors specific metrics and automatically creates thresholds by analyzing what levels might be potentially problematic for a specified resource. When the new metric values cross a predefined threshold over a given period of time, Amazon RDS generates a proactive recommendation. This recommendation helps to prevent future database performance impact. To receive these proactive recommendations, you must enable collecting detailed per-query and database counter metrics with a paid tier retention period.

For more information about enabling detailed per-query and database counter metrics, see [Enabling and disabling detailed per-query and database counter metrics](USER_PerfInsights.Enabling.md). For information about pricing and data retention for Database Insights, see [Pricing and data retention for Database Insights](USER_PerfInsights.Overview.cost.md).

To find out the regions, DB engines, and instance classes supported for the proactive recommendations, see [Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.html). 

You can view the detailed analysis and recommended investigations of proactive recommendations in the recommendation details page.

For more information about recommendations, see [Recommendations from Amazon RDS](monitoring-recommendations.md).

**To view the detailed analysis of a proactive recommendation**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, do any of the following:
   + Choose **Recommendations**.

     The **Recommendations** page displays a list of recommendations sorted by the severity for all the resources in your account.
   + Choose **Databases** and then choose **Recommendations** for a resource in the databases page.

     The **Recommendations** tab displays the recommendations and its details for the selected resource.

1. Find a proactive recommendation and choose **View details**.

   The recommendation details page appears. The title provides the name of the affected resource with the issue detected and the severity.

   The following are the components on the recommendation details page:
   + **Recommendation summary** – The detected issue, recommendation and issue status, issue start and end time, recommendation modified time, and the engine type.  
![Recommendation details page for proactive recommendation showing the Recommendation summary section in the console.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/RecommendationProactive-RecSummary.png)
   + **Metrics** – The graphs of the detected issue. Each graph displays a threshold determined by the resource's baseline behavior and data of the metric reported from the issue start time.  
![Recommendation details page for proactive recommendation showing the Metrics section in the console.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/RecommedationProactive_Metrics.png)
   + **Analysis and recommendations** – The recommendation and the reason for the suggested recommendation.  
![Recommendation details page for proactive recommendation showing the Analysis and recommendations section in the console.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/ProactiveRecommendation-AnalysisAndRec.png)

   You can review the cause of the issue and then perform the suggested recommended actions to fix the issue, or choose **Dismiss** to dismiss the recommendation.