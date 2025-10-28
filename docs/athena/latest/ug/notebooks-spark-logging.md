# Log Spark application events in Athena

The Athena notebook editor allows for standard Jupyter, Spark, and Python logging. You can
use `df.show()` to display PySpark DataFrame contents or use
`print("Output")` to display values in the cell output. The
`stdout`, `stderr`, and `results` outputs for your
calculations are written to your query results bucket location in Amazon S3.

## Log Spark application events to Amazon CloudWatch

Your Athena sessions can also write logs to [Amazon CloudWatch](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") in the account that you are using.

### Understand log streams and log groups

CloudWatch organizes log activity into log streams and log groups.

Log streams – A CloudWatch log stream is a
sequence of log events that share the same source. Each separate source of logs in
CloudWatch Logs makes up a separate log stream.

Log groups – In CloudWatch Logs, a log group is a
group of log streams that share the same retention, monitoring, and access control
settings.

There is no limit on the number of log streams that can belong to one log
group.

In Athena, when you start a notebook session for the first time, Athena creates a
log group in CloudWatch that uses the name of your Spark-enabled workgroup, as in the
following example.

```
/aws-athena/workgroup-name
```

This log group receives one log stream for each executor in your session that
produces at least one log event. An executor is the smallest unit of compute that a
notebook session can request from Athena. In CloudWatch, the name of the log stream begins
with the session ID and executor ID.

For more information about CloudWatch log groups and log streams, see [Working with log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the Amazon CloudWatch Logs User Guide.

### Use standard logger objects in Athena for Spark

In an Athena for Spark session, you can use the following two global standard
logger objects to write logs to Amazon CloudWatch:

- athena_user_logger – Sends logs to
  CloudWatch only. Use this object when you want to log information your Spark
  applications directly to CloudWatch, as in the following example.

```
athena_user_logger.info("CloudWatch log line.")
```

The example writes a log event to CloudWatch like the following:

```
AthenaForApacheSpark: 2022-01-01 12:00:00,000 INFO builtins: CloudWatch log line.
```

- athena_shared_logger – Sends the
  same log both to CloudWatch and to AWS for support purposes. You can use this
  object to share logs with AWS service teams for troubleshooting, as in the
  following example.

```
athena_shared_logger.info("Customer debug line.")
var = [...some variable holding customer data...]
athena_shared_logger.info(var)
```

The example logs the `debug` line and the value of the
`var` variable to CloudWatch Logs and sends a copy of each line to
Support.

###### Note

For your privacy, your calculation code and results are not shared
with AWS. Make sure that your calls to
`athena_shared_logger` write only the information that
you want to make visible to Support.

The provided loggers write events through [Apache Log4j](https://logging.apache.org/log4j/ "https://logging.apache.org/log4j/") and inherit the
logging levels of this interface. Possible log level values are `DEBUG`,
`ERROR`, `FATAL`, `INFO`, and `WARN`
or `WARNING`. You can use the corresponding named function on the logger
to produce these values.

###### Note

Do not rebind the names `athena_user_logger` or
`athena_shared_logger`. Doing so makes the logging objects unable
to write to CloudWatch for the remainder of the session.

The following procedure shows how to log Athena notebook events to Amazon CloudWatch
Logs.

###### To log Athena notebook events to Amazon CloudWatch Logs

1. Follow [Get started with Apache Spark on
   Amazon Athena](notebooks-spark-getting-started.md "notebooks-spark-getting-started.md") to create a Spark
   enabled workgroup in Athena with a unique name. This tutorial uses the
   workgroup name `athena-spark-example`.
2. Follow the steps in [Step 7:
   Create your own notebook](notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook "notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook") to create a notebook and launch a new session.
3. In the Athena notebook editor, in a new notebook cell, enter the
   following command:

```
athena_user_logger.info("Hello world.")
```

4. Run the cell.
5. Retrieve the current session ID by doing one of the following:
   - View the cell output (for example, `...
session=72c24e73-2c24-8b22-14bd-443bdcd72de4`).
   - In a new cell, run the [magic](notebooks-spark-magics.md "notebooks-spark-magics.md") command
     `%session_id`.

6. Save the session ID.
7. With the same AWS account that you are using to run the notebook
   session, open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
8. In the CloudWatch console navigation pane, choose **Log
   groups**.
9. In the list of log groups, choose the log group that has the name of
   your Spark-enabled Athena workgroup, as in the following example.

```
/aws-athena/athena-spark-example
```

The **Log streams** section contains a list of one or
more log stream links for the workgroup. Each log stream name contains
the session ID, executor ID, and unique UUID separated by forward slash
characters.

For example, if the session ID is
`5ac22d11-9fd8-ded7-6542-0412133d3177` and the executor
ID is `f8c22d11-9fd8-ab13-8aba-c4100bfba7e2`, the name of the
log stream resembles the following example.

```
5ac22d11-9fd8-ded7-6542-0412133d3177/f8c22d11-9fd8-ab13-8aba-c4100bfba7e2/f012d7cb-cefd-40b1-90b9-67358f003d0b
```

10. Choose the log stream link for your session.
11. On the **Log events** page, view the
    **Message** column.

The log event for the cell that you ran resembles the
following:

```
AthenaForApacheSpark: 2022-01-01 12:00:00,000 INFO builtins: Hello world.
```

12. Return to the Athena notebook editor.
13. In a new cell, enter the following code. The code logs a variable to
    CloudWatch:

```
x = 6
athena_user_logger.warn(x)
```

14. Run the cell.
15. Return to the CloudWatch console **Log events** page for
    the same log stream.
16. The log stream now contains a log event entry with a message like the
    following:

```
AthenaForApacheSpark: 2022-01-01 12:00:00,000 WARN builtins: 6
```
