# Analyzing DB load for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard

With Performance Insights, you can track metrics at the shard group level and at the instance level for an Aurora PostgreSQL Limitless Database. When analyzing DB load for an Aurora PostgreSQL Limitless Database,
you might want to compare the DB load for each shard and router to the maximum vCPU.

###### Note

Aurora PostgreSQL Limitless Database always has Performance Insights and Enhanced Monitoring enabled. The minimum retention period for Performance Insights data for Limitless Database is 31 days (1 month).

The **Absolute** view shows the number of Average active sessions (AAS) and the estimated vCPU. The
**Relative** view shows the ratio of AAS to the estimated vCPU.

###### Topics

- [Analyzing relative DB load for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard](#USER_PerfInsights.AnalyzeLimitlessTables.RelativeLoad "#USER_PerfInsights.AnalyzeLimitlessTables.RelativeLoad")
- [Analyzing DB load by waits for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard](USER_PerfInsights.AnalyzeLimitlessTables.md "USER_PerfInsights.AnalyzeLimitlessTables.md")
- [Analyzing load distribution for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard](USER_PerfInsights.AnalyzeLimitlessTables.md "USER_PerfInsights.AnalyzeLimitlessTables.md")

## Analyzing relative DB load for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard

You might want to improve the performance of your Aurora PostgreSQL Limitless Database by tracking relative DB load. To analyze relative DB load by instance for your
Aurora PostgreSQL Limitless Database, use the following procedure.

###### To analyze relative DB load for Aurora PostgreSQL Limitless Database using the console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Performance Insights**.
3. Choose an Aurora PostgreSQL Limitless Database. The Performance Insights dashboard is displayed for that Aurora PostgreSQL Limitless Database.
4. In the **Database load (DB load)** section, choose **Instances** for
   **Sliced by**. To see the ratio of Average active sessions (AAS) to vCPU cores for all of the instances in your
   Aurora PostgreSQL Limitless Database, choose **Relative** for **Viewed as**.

The Average active sessions chart shows the DB load for instances in your Aurora PostgreSQL Limitless Database.

![View the Performance Insights dashboard for your Aurora PostgreSQL Limitless Database sliced by instances.](images/pi-relative-instances.png) 5. To view the top instances, choose the **Top instances** tab.

In the following example, the instance with the highest DB load is `DTR-2-2`.

![Use the Top instances tab for an Aurora PostgreSQL Limitless Database sliced by instances.](images/pi-top-instances.png) 6. (Optional) To analyze DB load for an instance in your Aurora PostgreSQL Limitless Database, choose the instance name in the **Instances**
column. To view the DB load for `DTR-2-2`, choose `DTR-2-2` in the **Instances** column.

###### Note

You can view Performance Insights metrics only for instances in an Aurora PostgreSQL Limitless Database.
