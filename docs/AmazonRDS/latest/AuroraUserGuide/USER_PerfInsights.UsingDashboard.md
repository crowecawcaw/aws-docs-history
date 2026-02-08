# Viewing a performance analysis

report in Performance Insights

The **Performance analysis reports - new** tab lists all the reports
that are created for the DB instance. The following are displayed for each report:

- **ID**: Unique identifier of the report.
- **Name**: Tag key added to the report.
- **Report creation time**: Time you created the report.
- **Analysis start time**: Start time of the analysis in the report.
- **Analysis end time**: End time of the analysis in the report.

###### To view a performance analysis report

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the left navigation pane, choose **Performance Insights**.
3. Choose a DB instance for which you want to view the analysis report.
4. Scroll down and choose **Performance analysis reports - new** tab in the Performance Insights dashboard.

All the analysis reports for the different time periods are displayed. 5. Choose **ID** of the report you want to view.

The DB load chart displays the entire analysis period by default if more than one insight is identified.
If the report has identified one insight then the DB load chart displays the insight by default.

The dashboard also lists the tags for the report in the **Tags** section.

The following example shows the entire analysis period for the report.

![DB load chart showing entire analysis report period](images/PI_EntireAnalysisRep.png) 6. Choose the insight in the **Database load insights** list you want to view if more than one insight is identified in the report.

The dashboard displays the insight message, DB load chart highlighting the time period of the insight,
analysis and recommendations, and the list of report tags.

The following example shows the DB load insight in the report.

![DB load chart showing insight in the report](images/PI_AnalysisRepInsight_chart.png)

![Report insight analysis and recommendation section](images/PI_AnalysisRepInsight_Recommendations.png)
