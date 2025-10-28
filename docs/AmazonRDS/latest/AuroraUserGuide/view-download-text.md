# Viewing and downloading SQL text in the Performance Insights

dashboard

In the Performance Insights dashboard, you can view or download SQL text.

###### To view more SQL text in the Performance Insights dashboard

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Performance Insights**.
3. Choose a DB instance.
4. Scroll down to the **Top SQL** tab in the Performance Insights dashboard.
5. Choose the plus sign to expand a SQL digest and choose one of the digest's child queries.

SQL statements with text larger than 500 bytes look similar to the following image.

![SQL statements with large text](images/perf-insights-large-text-aurora-1.png) 6. Scroll down to the **SQL text** tab.

![SQL information section shows more of the SQL text](images/perf-insights-large-text-aurora-2.png)

The Performance Insights dashboard can display up to 4,096 bytes for each SQL statement. 7. (Optional) Choose **Copy** to copy the displayed SQL statement, or choose
**Download** to download the SQL statement to view the SQL text up to the DB engine
limit.

###### Note

To copy or download the SQL statement, disable pop-up blockers.
