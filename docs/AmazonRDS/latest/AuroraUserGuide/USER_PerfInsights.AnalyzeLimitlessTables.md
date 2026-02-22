# Analyzing load distribution for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard

You might want to balance the load distribution for instances on your Aurora PostgreSQL Limitless Database. To analyze load distribution of the instances on an Aurora PostgreSQL Limitless Database,
use the following procedure.

###### To analyze load distribution of the instances on an Aurora PostgreSQL Limitless Database using the console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Performance Insights**.
3. Choose an Aurora PostgreSQL Limitless Database. The Performance Insights dashboard is displayed for that Aurora PostgreSQL Limitless Database.
4. In the **Database load (DB load)** section, choose **Instances** for **Sliced
   by**. To view the number of AAS and the estimated vCPU for all instances in your Aurora PostgreSQL Limitless Database, choose
   **Absolute** for **Viewed as**.

The Average active sessions chart shows the DB load for instances in your Aurora PostgreSQL Limitless Database.

![View the absolute Performance Insights dashboard for your Aurora PostgreSQL Limitless Database sliced by instances.](images/pi-absolute-instances.png) 5. To see a chart of the load distribution of the instances in your Aurora PostgreSQL Limitless Database, choose the **Load
distribution** tab.

In the following example, the instance with the highest DB load is `DTR-2-2`.

![Top SQL tab when you slice by waits at the instance level.](images/pi-load-distribution.png)
