# Limitations of AWS Clean Rooms Differential Privacy

AWS Clean Rooms Differential Privacy doesn't address the following situations:

1. AWS Clean Rooms Differential Privacy only supports
   queries with
   Amazon S3-backed AWS Glue tables. It
   doesn't
   support queries with Snowflake or Amazon Athena tables.
2. AWS Clean Rooms Differential Privacy doesn't address timing attacks. For example, these attacks
   are possible in scenarios where an individual user contributes a large number of rows and
   adding or removing this user significantly changes the query computation time.
3. AWS Clean Rooms Differential Privacy doesn't guarantee differential privacy when a SQL query can
   result in overflow or invalid cast errors at run time due to the use of certain SQL
   constructs.

The following table is a list of some, but not all, SQL constructs
that may produce run-time errors and should be verified in analysis templates. We
recommend that you approve analysis templates that minimize the chances of such run-time
errors and periodically review query logs to determine if the queries align with the
collaboration agreement.

The following SQL constructs are vulnerable to overflow errors:

| Category                       | SQL constructs vulnerable to overflow errors<br>in the Spark<br>SQL analytics engine | SQL<br>constructs vulnerable to overflow errors in the AWS Clean Rooms SQL analytics<br>engine |
| ------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ------------------------ | --- | --- | --------------------------------------- |
| Aggregate functions            | • AVG<br>• SUM/SUM_DISTINCT                                                          | • AVG<br>• LISTAVG<br>• PERCENTILE_COUNT<br>• PERCENTILE_DISC<br>• SUM/SUM_DISTINCT            |
| Data type formatting functions | • TO_TIMESTAMP<br>• TO_DATE                                                          | • TO_TIMESTAMP<br>• TO_DATE                                                                    |
| Date and time functions        | • ADD_MONTHS<br>• DATEADD<br>• DATEDIFF                                              | • ADD_MONTHS<br>• DATEADD<br>• DATEDIFF                                                        |
| Math functions                 | • +, -, \*, /<br>• POWER                                                             | • +, -, \*, /<br>• POWER                                                                       |
| String functions               | •                                                                                    |                                                                                                | <br>• CONCAT<br>• REPEAT | •   |     | <br>• CONCAT<br>• REPEAT<br>• REPLICATE |
| Window functions               | • AVG<br>• SUM                                                                       | • AVG<br>• LISTAVG<br>• PERCENTILE_COUNT<br>• PERCENTILE_DISC<br>• RATIO_TO_REPORT<br>• SUM    |

4. The CAST data type formatting function is vulnerable to invalid cast errors.

You can configure [CloudWatch to create a
metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") and then [create a CloudWatch alarm](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md")
on that metric filter to receive alerts if a potential overflow or cast error was
encountered.

Specifically, you should monitor for the error codes `CastError`,
`OverflowError`, `ConversionError`. The presence of these error
codes indicates a potential side-channel attack, but might indicate an erroneous SQL
query.

For more information, see [Analysis logging in AWS Clean Rooms](query-logs.md "query-logs.md").
