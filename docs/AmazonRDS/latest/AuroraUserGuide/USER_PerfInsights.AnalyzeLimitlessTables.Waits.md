

# Analyzing DB load by waits for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard
<a name="USER_PerfInsights.AnalyzeLimitlessTables.Waits"></a>

You might want to improve the performance for your Aurora PostgreSQL Limitless Database by tracking wait events. To analyze DB load by wait events for your Aurora PostgreSQL Limitless Database, use the following procedure.

**To analyze DB load by waits for Aurora PostgreSQL Limitless Database using the console**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Performance Insights**.

1. Choose an Aurora PostgreSQL Limitless Database. The Performance Insights dashboard is displayed for that Aurora PostgreSQL Limitless Database.

1. In the **Database load (DB load)** section, choose **Waits** for **Sliced by**. To view the number of AAS and the estimated vCPU, choose **Absolute** for **Viewed as**.

   The Average active sessions chart shows the DB load for instances in your Aurora PostgreSQL Limitless Database.  
![Sliced by waits.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/pi-absolute-waits.png)

1. Scroll down to the **Top SQL** tab.

   In the following example, the SQL statement with the highest load by waits is the `DELETE` statement.  
![Top SQL tab when sliced by waits.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/pi-waits-top-sql.png)

1. Choose the SQL statement to expand it into its component statements.

   In the following example, the `SELECT` statement has 3 component statements.  
![A SQL statement selected to expand details.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/pi-waits-top-sql-selected.png)