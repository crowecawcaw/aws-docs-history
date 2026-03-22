# Exporting Performance Insights metrics as a new dashboard to CloudWatch

Choose a preconfigured or custom metrics dashboard from the Performance Insights dashboard and export
it as a new dashboard to CloudWatch. You can view the exported dashboard in the CloudWatch
console.

###### To export a Performance Insights metric dashboard as a new dashboard to CloudWatch

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the left navigation pane, choose **Performance Insights**.
3. Choose a DB instance.

The Performance Insights dashboard appears for the DB instance. 4. Scroll down and choose **Metrics**.

By default, the preconfigured dashboard with Performance Insights metrics appears. 5. Choose a preconfigured or custom dashboard and then choose **Export to
CloudWatch**.

The **Export to CloudWatch** window appears.

![Performance Insights dashboard with export to CloudWatch button](images/PI-ExprtToCW.png) 6. Choose **Export as new dashboard**.

![Export to CloudWatch window with export as new dashboard option selected](images/PI-ExprtToCW-NewDashboard.png) 7. Enter a name for the new dashboard in the **Dashboard name** field and choose **Confirm**.

A banner displays a message after the dashboard export is successful.

![Banner with successful message](images/PI-ExprtToCW-SuccessBanner.png) 8. Choose the link or **View in CloudWatch** in the banner
to view the metrics dashboard in the CloudWatch console.
