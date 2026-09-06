

# Alarm data queries
<a name="alarm-data-queries"></a>

CloudWatch alarms can monitor various data sources. Choose the appropriate query type based on your monitoring needs.

## Metrics
<a name="alarm-query-metrics"></a>

Monitor a single CloudWatch metric. This is the most common alarm type for tracking resource performance. For more information about metrics, see [CloudWatch Metrics concepts](cloudwatch_concepts.md).

For more information, see [Create a CloudWatch alarm based on a static threshold](ConsoleAlarms.md).

## Metric math
<a name="alarm-query-metric-math"></a>

You can set an alarm on the result of a math expression that is based on one or more CloudWatch metrics. A math expression used for an alarm can include as many as 10 metrics. Each metric must be using the same period.

For an alarm based on a math expression, you can specify how you want CloudWatch to treat missing data points. In this case, the data point is considered missing if the math expression doesn't return a value for that data point.

Alarms based on math expressions can't perform Amazon EC2 actions.

For more information about metric math expressions and syntax, see [Math expressions with metrics](using-metric-math.md).

For more information, see [Create a CloudWatch alarm based on a metric math expression](Create-alarm-on-metric-math-expression.md).

## Metrics Insights
<a name="alarm-query-metrics-insights"></a>

 A CloudWatch Metrics Insights query helps you query metrics at scale using SQL-like syntax. You can create an alarm on any Metrics Insights query, including queries that return multiple time series. This capability significantly expands your monitoring options. When you create an alarm based on a Metrics Insights query, the alarm automatically adjusts as resources are added to or removed from your monitored group. Create the alarm once, and any resource that matches your query definition and filters joins the alarm monitoring scope when its corresponding metric becomes available. For multi-time series queries, each returned time series becomes a contributor to the alarm, allowing for more granular and dynamic monitoring.

Here are two primary use cases for CloudWatch Metrics Insights alarms:
+ Anomaly Detection and Aggregate Monitoring

  Create an alarm on a Metrics Insights query that returns a single aggregated time series. This approach works well for dynamic alarms that monitor aggregated metrics across your infrastructure or applications. For example, you can monitor the maximum CPU utilization across all your instances, with the alarm automatically adjusting as you scale your fleet.

  To create an aggregate monitoring alarm, use this query structure:

  ```
  SELECT FUNCTION(metricName)
                    FROM SCHEMA(...)
                    WHERE condition;
  ```
+ Per-Resource Fleet Monitoring

  Create an alarm that monitors multiple time series, where each time series functions as a contributor with its own state. The alarm activates when any contributor enters the ALARM state, triggering resource-specific actions. For example, monitor database connections across multiple RDS instances to prevent connection rejections.

  To monitor multiple time series, use this query structure:

  ```
  SELECT AVG(DatabaseConnections)
                    FROM AWS/RDS
                    WHERE condition
                    GROUP BY DBInstanceIdentifier
                    ORDER BY AVG() DESC;
  ```

  When creating multi-time series alarms, you must include two key clauses in your query:
  + A `GROUP BY` clause that defines how to structure the time series and determines how many time series the query will produce
  + An `ORDER BY` clause that establishes a deterministic sorting of your metrics, enabling the alarm to evaluate the most important signals first

  These clauses are essential for proper alarm evaluation. The `GROUP BY` clause splits your data into separate time series (for example, by instance ID), while the `ORDER BY` clause ensures consistent and prioritized processing of these time series during alarm evaluation.

For more information on how to create a multi time series alarm, see [Create an alarm based on Metrics Insights](multi-time-series-alarm.md).

## Log group-metric filters
<a name="alarm-query-log-metric-filter"></a>

 You can create an alarm based on a log group-metric filter. With metric filters, you can look for terms and patterns in log data as the data is sent to CloudWatch. For more information, see [Create metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) in the *Amazon CloudWatch Logs User Guide*. 

For more information on how to create an alarm based on log group-metric filter, see [Alarming on logs](Alarm-On-Logs.md).

## Log Insights query
<a name="alarm-query-log-insights"></a>

You can create an alarm that uses a CloudWatch Logs Insights query to monitor log data directly. The query runs on a schedule using a Scheduled Query, and the alarm evaluates the aggregated results against a threshold. When the aggregation expression includes a `by` clause, each unique combination of field values is tracked as a contributor.

For more information about how Log Alarms work, see [Log alarms](alarm-log.md).

For more information about how to create a Log Alarm, see [Create a Log Alarm](Alarm-On-Logs.md#Create_Log_Alarm).

## PromQL
<a name="alarm-query-promql"></a>

You can create an alarm that uses a Prometheus Query Language (PromQL) instant query to monitor metrics ingested through the CloudWatch OTLP endpoint.

For more information about how PromQL alarms work, see [PromQL alarms](alarm-promql.md).

For more information on how to create a PromQL alarm, see [Create an alarm using a PromQL query](Create_PromQL_Alarm.md).

## External data source
<a name="alarm-query-external"></a>

You can create alarms that watch metrics from data sources that aren't in CloudWatch. For more information about creating connections to these other data sources, see [Query metrics from other data sources](MultiDataSourceQuerying.md).

For more information on how to create an alarm based on a connected data source, see [Create an alarm based on a connected data source](Create_MultiSource_Alarm.md).