

# Limitations of AWS Clean Rooms Differential Privacy
<a name="dp-limitations"></a>

AWS Clean Rooms Differential Privacy doesn't address the following situations:

1. AWS Clean Rooms Differential Privacy only supports queries with Amazon S3-backed AWS Glue tables. It doesn't support queries with Snowflake or Amazon Athena tables.

1. AWS Clean Rooms Differential Privacy doesn't address timing attacks. For example, these attacks are possible in scenarios where an individual user contributes a large number of rows and adding or removing this user significantly changes the query computation time.

1. AWS Clean Rooms Differential Privacy doesn't guarantee differential privacy when a SQL query can result in overflow or invalid cast errors at run time due to the use of certain SQL constructs. 

   The following table is a list of some, but not all, SQL constructs that may produce run-time errors and should be verified in analysis templates. We recommend that you approve analysis templates that minimize the chances of such run-time errors and periodically review query logs to determine if the queries align with the collaboration agreement.

   The following SQL constructs are vulnerable to overflow errors:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/dp-limitations.html)

1. The CAST data type formatting function is vulnerable to invalid cast errors.

   You can configure [CloudWatch to create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) and then [create a CloudWatch alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) on that metric filter to receive alerts if a potential overflow or cast error was encountered. 

   Specifically, you should monitor for the error codes `CastError`, `OverflowError`, `ConversionError`. The presence of these error codes indicates a potential side-channel attack, but might indicate an erroneous SQL query.

   For more information, see [Analysis logging in AWS Clean Rooms](query-logs.md).