

# Determining whether Database Insights is managing the Performance Schema
<a name="USER_PerfInsights.EnableMySQL.determining-status"></a>

To find out whether Database Insights is currently managing the Performance Schema for all supported major engine versions, review the following table.


| Setting of performance\_schema parameter | Setting of the Source column | Database Insights is managing the Performance Schema? | 
| --- | --- | --- | 
| 0 | System default | Yes | 
| 0 or 1 | Modified | No | 

In the following procedure, you determine whether Database Insights is managing the Performance Schema automatically.

**To determine whether Database Insights is managing the Performance Schema automatically**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Parameter groups**.

1. Select the name of the parameter group for your DB instance.

1. Enter **performance\_schema** in the search bar.

1. Check whether **Source** is the system default and **Value** is **0**. If so, Database Insights is managing the Performance Schema automatically.

   In the example shown here, Database Insights isn't managing the Performance Schema automatically.  
![Shows that the settings for the performance_schema parameter are modified.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/perf_schema_user.png)