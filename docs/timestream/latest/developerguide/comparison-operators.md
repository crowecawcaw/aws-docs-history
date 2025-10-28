For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Comparison operators

Timestream for LiveAnalytics supports the following comparison operators.

| Operator | Description              |
| -------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |
| =        | Equal                    |
| <>       | Not equal                |
| !=       | Not equal                | ###### Note <br>• The `BETWEEN` operator tests if a value is within a specified range. The syntax is as follows: `BETWEEN min AND max` The presence of `NULL` in a `BETWEEN` or `NOT BETWEEN` statement will result in the statement evaluating to `NULL`. <br>• `IS NULL` and `IS NOT NULL` operators test whether a value is null (undefined). Using `NULL` with `IS NULL` evaluates to true. <br>• In SQL, a `NULL` value signifies an unknown value. |
