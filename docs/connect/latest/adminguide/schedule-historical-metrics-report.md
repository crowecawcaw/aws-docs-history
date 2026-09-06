

# Schedule a historical metrics report in Connect Customer
<a name="schedule-historical-metrics-report"></a>

Before you schedule a historical metrics report, here are a few things you need to know:

**Others can access the report**
+ Scheduling a report makes the report accessible by any other users in your contact center who have permissions to view saved reports. 

**Anyone with Schedule permissions can create, edit, or delete the schedule of your report**
+ After you publish a report, any user with **Saved reports - Schedule** permissions in their security profile can create, edit, or delete the schedule of your report. They cannot delete the actual report.

**Scheduled reports are located in an Amazon S3 bucket**
+ Scheduled reports are saved as CSV files in the Amazon S3 bucket specified for reports for your contact center. When you set up the scheduled report, you can add a prefix to the location in Amazon S3 for the report files.
+ When the report is exported to your Amazon S3 bucket, the file name includes the date and UTC time when the report was created. The **Last modified date** for the file is displayed using the time zone for the Amazon S3 bucket, and might not match the creation time for the report, which is in UTC.

**There's a 15 minute delay**
+ For scheduled reports, there is a delay of 15 minutes after the scheduled report time before the report is generated. This is to make sure that the report includes the data for all of the activity that occurred during the time range specified for the report. Data from your contact center is not immediately processed and available to include in reports, so some data from the time range might not be captured in a report if the report is generated at the second the time range ends. 
+ For example, if you create a scheduled report for time frame of 8:00 AM to 5:00 PM, and there is activity in your contact center between 4:46:00 PM and 4:59:59 PM, the data about that activity might not be aggregated prior 5:00 PM when the report is scheduled to generate. Instead, the report is generated after 5:15 PM, by which time the data for the last 15 minutes of the time range is included in the report.

**The time range of the scheduled report is independent of the time range in the historical report**
+ The scheduled report uses the time range defined in the report schedule, not the time range of the historical metric report.

  For example:
  +  Today is January 14th. The time range set in the historical metric report is **Trailing 7 days: January 7th - January 14th**. However, the report schedule is set up to run every 1 day for the previous 1 day.
  + The generated scheduled report will contain data for January 13th to January 14th (the previous 1 day) as defined in the report schedule. It does not use the time range of Trailing 7 days in the historical metrics report.

**A scheduled report runs during the following time ranges:**
+ A scheduled report with **Generate this report** = **Daily** produces a report using trailing 24 hour intervals for the specified number of days.
  + For example, to create a scheduled report for yesterday that generates a report at 2:00PM EST every day apply the following settings:
    +  Generate this report **Daily**, running every **1 Day**, starting at 2:00PM EST for the previous **1 Days**.
    + If today was November 10th, the report would be delivered at 2:00PM EST November 10th and contain data from 2:00 PM EST November 9th to 2:00 PM EST November 10th. This 24 hour interval will appear as two rows in the generated report for every run.
      + Row 1: 2:00PM EST November 9th to midnight (00:00) November 10th
      + Row 2: Midnight (00:00) November 10th to 2:00PM EST November 10th  
![Settings to create a scheduled report for yesterday that generates a report at 2:00PM EST every day.](http://docs.aws.amazon.com/connect/latest/adminguide/images/metrics-scheduled-reports-historical-daily-2pm.png)
  + To create a scheduled report for yesterday that generates only one row for the 24 hour interval in each run, apply the following settings:
    +  Generate this report **Daily**, running every **1 Day**, starting at 12:00 AM in your **required timezone** for the previous **1 Days**.
    + If today was November 10th, the report would be delivered at 12:00 AM EST November 10th and contain data from midnight (00:00) November 9th to midnight (00:00) November 10th with 1 row for the 24 hour interval in each run.  
![Settings to create a scheduled report for yesterday that generates a report at 12:00AM EST every day.](http://docs.aws.amazon.com/connect/latest/adminguide/images/metrics-scheduled-reports-historical-daily-12am.png)
+ A scheduled report with **Generate this report** = **Hourly - - For the Previous 24 Hours** always produces a report where the start time is 24 hours before the set run time. The end time is set to the run time. 

  For example, a scheduled report is set to run hourly starting 2:00PM EST on October 5th for the trailing 24 hours. The start and end times are as follows:
  +  The start time for the first report is October 4th 2:00PM EST. The end time is October 5th 2:00PM EST.
  + The next report runs October 4th 3:00PM EST and has an end time of October 5th 3:00PM EST.

**No message if a scheduled report doesn't run**
+ If a scheduled report fails to run, you won't get any message in the Connect Customer UI. You just won't see the report in the Amazon S3 location. 

**Use your messaging system to email scheduled reports**
+ To email a scheduled report to a list of co-workers, you need to generate the email manually using your messaging system. Connect Customer doesn't provide an option to email the scheduled report automatically. 

## How to schedule a historical metrics report
<a name="howto-schedule-historical-metrics-report"></a>

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

1. Create a new report and save it, or open a saved report.

1. Choose the down arrow next to **Save** in the top-right corner of the page and choose **Schedule**.

1. On the **Recurrence** tab, specify how often this report should be run (for example, weekly on Saturdays) and the range (for example, from midnight for the previous 5 days).

1. (Optional) On the **Delivery Options** tab, specify a prefix for the location in Amazon S3 for the report files.

1. Choose **Create**.

## How to delete a scheduled report
<a name="howto-delete-scheduled-report"></a>

To get to the page where you can delete a scheduled report, you need to create another temporary scheduled report.

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

1. On the navigation menu, choose **Analytics and optimization**, **Dashboards and reports**. 

1. On the **View reports** page, choose the **Historical metrics** tab.

1. Choose or tap on the saved report that has been scheduled.

1. Choose the down arrow next to **Save** in the top-right corner of the page and choose **Schedule**.

1. Choose **Create**. 

1. On the **Schedule Report** page, choose **Delete** next to the scheduled reports you want to delete. 

For instructions on deleting saved reports, see [How to delete saved reports](save-reports.md#how-to-delete-saved-reports).

## Frequently Asked Questions
<a name="frequently-asked-questions"></a>

1. My scheduled reports are missing data for a specific time period?

   Compare the data in the generated report (published to your S3 bucket) with the historical report for that time period. If you find discrepancies, contact AWS Support for assistance.

1. My scheduled report failed to generate due to cell limits?

   Reports have a 200,000 cell limit (data cells, not total rows \* columns in the report). To resolve this, you can:
   + Reduce the number of metrics in your report
   + Apply filters to narrow the data scope
   + Split large reports into multiple smaller reports

1. My scheduled report is affected after a Daylight Saving transition?

   When you create a daily scheduled report, the selected start time is saved as a fixed UTC time and the schedule will always run at that same UTC time. It does not automatically adjust when Daylight Savings Time begins or ends.
   + To avoid this, we recommend configuring your schedule using UTC timezone, which never observes Daylight Saving Time and will produce consistent results year-round.
   + If you prefer to use a Daylight Savings Time-aware timezone, we recommend recreating the schedule with same configuration after each Daylight Saving Time transition to realign it with your intended local time.