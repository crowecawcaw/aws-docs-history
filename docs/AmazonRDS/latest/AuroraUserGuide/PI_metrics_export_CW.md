# Adding Performance Insights metrics to an existing CloudWatch dashboard

Add a preconfigured or custom metrics dashboard to an existing CloudWatch dashboard. You can add a label to the
metrics dashboard to appear in a separate section in the CloudWatch dashboard.

###### To export the metrics to an existing CloudWatch dashboard

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the left navigation pane, choose **Performance Insights**.
3. Choose a DB instance.

The Performance Insights dashboard appears for the DB instance. 4. Scroll down and choose **Metrics**.

By default, the preconfigured dashboard with Performance Insights metrics appears. 5. Choose the preconfigured or custom dashboard and then choose **Export to
CloudWatch**.

The **Export to CloudWatch** window appears. 6. Choose **Add to existing dashboard**.

![Export to CloudWatch window with add to existing dashboard option selected](images/Pi-ExprtToCW-AddToExistingBoard.png) 7. Specify the dashboard destination and label, and then choose
**Confirm**.

    * **CloudWatch dashboard destination** - Choose an existing CloudWatch dashboard.
    * **CloudWatch dashboard section label - optional** - Enter a name for the Performance Insights metrics
     to appear in this section in the CloudWatch dashboard.

A banner displays a message after the dashboard export is successful. 8. Choose the link or **View in CloudWatch** in the banner
to view the metrics dashboard in the CloudWatch console.
