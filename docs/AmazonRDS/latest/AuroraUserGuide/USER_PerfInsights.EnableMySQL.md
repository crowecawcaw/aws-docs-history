# Determining whether

Performance Insights is managing the Performance Schema

To find out whether Performance Insights is currently managing the Performance Schema for
all supported major engine versions, review the following table.

| Setting of performance_schema parameter | Setting of the Source column | Performance Insights is managing the Performance Schema? |
| --------------------------------------- | ---------------------------- | -------------------------------------------------------- |
| `0`                                     | `System default`             | Yes                                                      |
| `0` or `1`                              | `Modified`                   | No                                                       |

In the following procedure, you determine whether Performance Insights is managing the Performance
Schema automatically.

###### To determine whether Performance Insights is managing the Performance Schema

automatically

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Parameter groups**.
3. Select the name of the parameter group for your DB instance.
4. Enter `performance_schema` in the search bar.
5. Check whether **Source** is the system default and
   **Value** is **0**. If so, Performance
   Insights is managing the Performance Schema automatically.

In the example shown here, Performance Insights isn't managing the Performance
Schema automatically.

![Shows that the settings for the performance_schema parameter are modified.](images/perf_schema_user.png)
