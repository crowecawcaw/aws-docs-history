# Viewing Amazon Aurora recommendations

Using the Amazon RDS console, you can view Amazon Aurora recommendations for your database
resources. For a DB cluster, the recommendations appear for the DB cluster and its instances.

###### To view the Amazon Aurora recommendations

1.  Sign in to the AWS Management Console and open the Amazon RDS console at
    [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2.  In the navigation pane, do any of the following:

        * Choose **Recommendations**. The number of active recommendations for your
         resources and the number of recommendations with the highest
         severity generated in the last month are available next to **Recommendations**.
         To find the number of active recommendations for each severity,
         choose the number that shows the highest severity.



        ![Select Recommendations in the console](images/recommendations-select.png)

        By default, the **Recommendations** page displays a list of
         new recommendations in the last month. Amazon Aurora gives recommendations for all the resources in your account and sorts the recommendations by their severity.



        ![Main Recommendations page in the console which contains all the recommendations](images/Recommendations_List.png)

        You can choose a recommendation to view a section at the bottom of the page which contains the affected resources and details of how the recommendation will be applied.
        * In the **Databases** page, choose **Recommendations** for a resource.



        ![Recommendation option selected on Databases page in the console](images/Recommendations_DBpage.png)

        The **Recommendations** tab displays
         the recommendations and its details for the selected resource.



        ![Recommendations tab on Databases page in the console](images/RecommendationsTab_DBpage.png)

    The following details are available for the recommendations:

        * **Severity** – The implication level of the issue. The severity levels are
         **High**, **Medium**, **Low**, and **Informational**.
        * **Detection** – The number of affected resources and a short description of the issue.
         Choose this link to view the recommendation and the analysis details.
        * **Recommendation** – A short description of the recommended action to apply.
        * **Impact** – A short description of the possible impact when the recommendation isn't applied.
        * **Category** – The type of recommendation. The categories are **Performance efficiency**,
         **Security**, **Reliability**, **Cost optimization**, **Operational excellence**,
         and **Sustainability**.
        * **Status** – The current status of the recommendation. The possible statuses are **All**,
         **Active**, **Dismissed**, **Resolved**, and **Pending**.
        * **Start time** – The time when the issue began. For example,
         **18 hours ago**.
        * **Last modified** – The time when the recommendation was last updated
         by the system because of a change in the **Severity**,
         or the time you responded to the recommendation. For example,
         **10 hours ago**.
        * **End time** – The time when the issue ended. The time won't display for any continuing issues.
        * **Resource identifier** – The name of one or more resources.

3.  (Optional) Choose **Severity** or
    **Category** operators in the field to filter the list
    of recommendations.

![Recommendations page with severity operation in the console.](images/Recommendations_Severity.png)

The recommendations for the selected operation appear. 4. (Optional) Choose any of the following recommendation status:

    * **Active** (default) – Shows the current
     recommendations that you can apply, schedule it for the next
     maintenance window, or dismiss.
    * **All** – Shows all the recommendations with the current status.
    * **Dismissed** – Shows the dismissed recommendations.
    * **Resolved** – Shows the recommendations that
     are resolved.
    * **Pending** – Shows the recommendations whose
     recommended actions are in progress or scheduled for the next
     maintenance window.

![Recommendations filtered by status in the console](images/Recommendations_Status.png) 5. (Optional) Choose **Relative mode** or **Absolute mode** in
**Last modified** to modify the time period. The **Recommendations** page displays
the recommendations generated in the time period. The default time period is the last month. In the **Absolute mode**, you can
choose the time period, or enter the time in **Start date**
and **End date** fields.

![Recommendations filtered by time period in the console](images/Recommendations_TimeMode.png)

The recommendations for the set time period display.

Note that you can see all recommendations for resources in your account by setting the range to **All**. 6. (Optional) Choose **Preferences** in the right to customize
the details to display. You can choose a page size, wrap the lines of the
text, and allow or hide the columns. 7. (Optional) Choose a recommendation and then choose **View details**.

![Recommendations page in the console with a selected recommendation and view details button chosen.](images/Recommendations_viewDetailsSelect.png)

The recommendation details page appears. The title provides the total count of
the resources with the issue detected and the severity.

For information about the components on the details page for an anomaly based reactive
recommendation, see [Viewing reactive anomalies](../../../devops-guru/latest/userguide/working-with-rds.analyzing.md "../../../devops-guru/latest/userguide/working-with-rds.analyzing.md") in the _Amazon DevOps Guru User
Guide_.

For information about the components on the details page for a threshold based proactive recommendation, see [Viewing Performance Insights proactive recommendations](USER_PerfInsights.md "USER_PerfInsights.md").

The other automated recommendations display the following components on the recommendation details page:

    * **Recommendation** – A summary of the recommendation and whether downtime
     is required to apply the recommendation.



    ![Recommendations details page showing Recommendation section in the console.](images/RecommendationSummary.png)
    * **Resources affected** – Details of the affected resources.



    ![Recommendations details page showing Resources Affected section in the console.](images/Recommendations_AffectedResources.png)
    * **Recommendation details** – Supported engine information, any required associated
     cost to apply the recommendation, and documentation link to learn more.



    ![Recommendations details page showing Recommendation details section in the console.](images/RecommendationDetails.png)

To view Amazon RDS recommendations of the DB instances or DB clusters, use the following command in AWS CLI.

```
aws rds describe-db-recommendations
```

To view Amazon RDS recommendations using the Amazon RDS API, use the [DescribeDBRecommendations](../APIReference/API_DescribeDBRecommendations.md "../APIReference/API_DescribeDBRecommendations.md") operation.
