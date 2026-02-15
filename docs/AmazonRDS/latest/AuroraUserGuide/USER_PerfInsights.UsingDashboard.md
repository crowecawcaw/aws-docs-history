# Creating a

performance analysis report in Performance Insights

You can create a performance analysis report for a specific period in the Performance Insights dashboard. You can select a time period and add one or more
tags to the analysis report.

The analysis period can range from 5 minutes to 6 days. There must be at least 24 hours of performance data before the analysis start time.

For the region, DB engine, and instance class support information for this feature, see
[Amazon Aurora DB engine, Region, and instance class support
for Performance Insights features](USER_PerfInsights.Overview.md#USER_PerfInsights.Overview.PIfeatureEngnRegSupport "USER_PerfInsights.Overview.md#USER_PerfInsights.Overview.PIfeatureEngnRegSupport")

###### To create a performance analysis report for a time period

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the left navigation pane, choose **Performance Insights**.
3. Choose a DB instance.
4. Choose **Analyze performance** in **Database load**
   section on the Performance Insights dashboard.

The fields to set the time period and add one or more tags to the performance analysis report are displayed.

![Performance Insights dashboard showing fields to create analysis report](images/PI_CreateAnalysisReport.png) 5. Choose the time period. If you set a time period in the **Relative range** or **Absolute range**
in the upper right, you can only enter or select the analysis report date and time within this time period.
If you select the analysis period outside of this time period, an error message displays.

To set the time period, you can do any of the following:

    * Press and drag any of the sliders on the DB load chart.


    The **Performance analysis period** box displays the selected time period and DB load chart highlights the selected time period.
    * Choose the **Start date**, **Start time**, **End date**, and **End time** in the
     **Performance analysis period** box.

![Performance Insights dashboard with analysis period selected](images/PI_CreateAnalysisRep_TimePeriod.png) 6. (Optional) Enter **Key** and **Value-_optional_** to add a tag for the report.

![Performance Insights dashboard with fields to add a new tag](images/PI_CreateAnalysisRep_AddTag.png) 7. Choose **Analyze performance**.

A banner displays a message whether the report generation is successful or failed. The message also provides the link to view the report.

The following example shows the banner with the report creation successful message.

![Analysis report creation successful message banner](images/PI_CreateAnaysisRep_SuccessMsg.png)

The report is available to view in **Performance analysis reports - new** tab.
You can create a performance analysis report using the AWS CLI.
For an example on how to create a report using AWS CLI, see [Creating a performance analysis report for a time period](USER_PerfInsights.API.md#USER_PerfInsights.API.Examples.CreatePerfAnalysisReport "USER_PerfInsights.API.md#USER_PerfInsights.API.Examples.CreatePerfAnalysisReport").
