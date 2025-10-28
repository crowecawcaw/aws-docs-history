After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Troubleshooting Amazon Kinesis Data Analytics for SQL Applications

The following can help you troubleshoot problems that you might encounter with Amazon Kinesis Data Analytics
for SQL Applications.

###### Topics

- [Stopped applications](#idle-applications "#idle-applications")
- [Unable to Run SQL Code](#sql-statement "#sql-statement")
- [Unable to Detect or Discover My Schema](#detect-schema "#detect-schema")
- [Reference Data is Out of Date](#reference-reload "#reference-reload")
- [Application Not Writing to Destination](#output "#output")
- [Important Application Health Parameters to Monitor](#parameters "#parameters")
- [Invalid Code Errors When Running an Application](#invalid-code "#invalid-code")
- [Application is Writing Errors to the Error Stream](#error-stream "#error-stream")
- [Insufficient Throughput or High MillisBehindLatest](#insufficient-throughput "#insufficient-throughput")

## Stopped applications

- **What is a stopped Kinesis Data Analytics for SQL application?**

A stopped application is an application that we have observed not processing any records for a minimum of three months. This means customers are paying for Kinesis Data Analytics for SQL resources they are not using.

- **When will AWS begin stopping idle applications?**

AWS will begin stopping idle applications on November 14, 2023 and complete by November 21, 2023.
We will stop idle applications in the office hours timezone of that Region.

- **Can stopped Kinesis Data Analytics for SQL applications be re-started?**

Yes. If you require to re-start your application you can do so as normal. There is no need to cut a support ticket.

- **When AWS stops an idle application will any of my query results also be deleted?**

No. First, because your application is idle it is not processing queries. Second, your query results are not stored in Kinesis Data Analytics for SQL. You configure your Kinesis Data Analytics for SQL application with a sink destination where the results of its calculations are sent (for example, in Amazon S3 or another data stream). As such, you retain full ownership of your data and it will remain retrievable under the terms of that storage service.

- **What do I do if I don’t want my application stopped?**

You can email the service team (kda-sql-questions@amazon.com) requesting applications not be stopped any time before November 10, 2023.
The email should include your account ID and application ARN.

## Unable to Run SQL Code

If you need to figure out how to get a particular SQL statement to work correctly, you
have several different resources when using Kinesis Data Analytics:

- For more information about SQL statements, see [Kinesis Data Analytics for SQL examples](examples.md "examples.md"). This section provides a number of SQL examples
  that you can use.
- The _[Amazon Kinesis Data Analytics SQL
  Reference](../sqlref/sqlrf_Preface.md "../sqlref/sqlrf_Preface.md")_ provides a detailed guide to authoring
  streaming SQL statements.
- If you're still running into issues, we recommend that you ask a question on the [Kinesis Data Analytics
  Forums](https://forums.aws.amazon.com/ann.jspa?annID=4153 "https://forums.aws.amazon.com/ann.jspa?annID=4153").

## Unable to Detect or Discover My Schema

In some cases, Kinesis Data Analytics can't detect or discover a schema. In many of these cases, you
can still use Kinesis Data Analytics.

Suppose that you have UTF-8 encoded data that doesn't use a delimiter, or data that
uses a format other than comma-separated values (CSV), or the discovery API did not
discover your schema. In these cases, you can define a schema manually or use string
manipulation functions to structure your data.

To discover the schema for your stream, Kinesis Data Analytics randomly samples the latest data in your
stream. If you aren't consistently sending data to your stream, Kinesis Data Analytics might not be able
to retrieve a sample and detect a schema. For more information, see [Using the Schema Discovery Feature on Streaming Data](sch-dis.md "sch-dis.md").

## Reference Data is Out of Date

Reference data is loaded from the Amazon Simple Storage Service (Amazon S3) object into the application when the
application is started or updated, or during application interruptions that are caused
by service issues.

Reference data is not loaded into the application when updates are made to the
underlying Amazon S3 object.

If the reference data in the application is not up to date, you can reload the data by
following these steps:

1. On the Kinesis Data Analytics console, choose the application name in the list, and then choose
   **Application details**.
2. Choose **Go to SQL editor** to open the **Real-time
   analytics** page for the application.
3. In the **Source Data** view, choose your reference data table
   name.
4. Choose **Actions**, **Synchronize reference data table**.

## Application Not Writing to Destination

If data is not being written to the destination, check the following:

- Verify that the application's role has sufficient permission to access the destination. For
  more information, see [Permissions Policy for Writing to a Kinesis Stream](iam-role.md#iam-role-permissions-policy-ak-stream "iam-role.md#iam-role-permissions-policy-ak-stream") or [Permissions Policy for Writing to a Firehose Delivery Stream](iam-role.md#iam-role-permissions-policy-af-delivery-stream "iam-role.md#iam-role-permissions-policy-af-delivery-stream").
- Verify that the application destination is correctly configured and that the application is
  using the correct name for the output stream.
- Check the Amazon CloudWatch metrics for your output stream to see if data is being written. For
  information about using CloudWatch metrics, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- Add a CloudWatch log stream using [AddApplicationCloudWatchLoggingOption](API_AddApplicationCloudWatchLoggingOption.md "API_AddApplicationCloudWatchLoggingOption.md"). Your
  application will write configuration errors to the log stream.

If the role and destination configuration look correct, try restarting the application, specifying `LAST_STOPPED_POINT` for the [InputStartingPositionConfiguration](API_InputStartingPositionConfiguration.md "API_InputStartingPositionConfiguration.md").

## Important Application Health Parameters to Monitor

To make sure that your application is running correctly, we recommend that you monitor
certain important parameters.

The most important parameter to monitor is the Amazon CloudWatch metric
`MillisBehindLatest`. This metric represents how far behind the current
time you are reading from the stream. This metric helps you determine whether you are
processing records from the source stream fast enough.

As a general rule, you should set up a CloudWatch alarm to trigger if you fall behind more
than one hour. However, the amount of time depends on your use case. You can adjust it
as needed.

For more information, see [Best Practices](best-practices.md "best-practices.md").

## Invalid Code Errors When Running an Application

When you can't save and run the SQL code for your Amazon Kinesis Data Analytics application, the following
are common causes:

- **The stream was redefined in your SQL code**
  – After you create a stream and the pump associated with the stream, you
  can't redefine the same stream in your code. For more information about creating
  a stream, see [CREATE STREAM](../sqlref/sql-reference-create-stream.md "../sqlref/sql-reference-create-stream.md") in the _Amazon Kinesis Data Analytics SQL Reference_.
  For more information about creating a pump, see [CREATE
  PUMP](../sqlref/sql-reference-create-pump.md "../sqlref/sql-reference-create-pump.md").
- **A GROUP BY clause uses multiple ROWTIME columns** – You can specify only one ROWTIME column in the GROUP BY
  clause. For more information, see [GROUP BY](../sqlref/sql-reference-group-by-clause.md "../sqlref/sql-reference-group-by-clause.md")
  and [ROWTIME](../sqlref/sql-reference-rowtime.md "../sqlref/sql-reference-rowtime.md") in
  the _Amazon Kinesis Data Analytics SQL Reference_.
- **One or more data types have an invalid casting** – In this case, your code has an invalid implicit cast. For
  example, you might be casting a `timestamp` to a `bigint`
  in your code.
- **A stream has the same name as a service reserved
  stream name** – A stream can't have the same name as the
  service-reserved stream `error_stream`.

## Application is Writing Errors to the Error Stream

If your application is writing errors to the in-application error stream, you can decode the value in the `DATA_ROW` field using standard libraries. For more information
about the error stream, see [Error Handling](error-handling.md "error-handling.md").

## Insufficient Throughput or High MillisBehindLatest

If your application's [MillisBehindLatest](../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md "../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md") metric is steadily increasing or consistently is above
1000 (one second), it can be due to the following reasons:

- Check your application's [InputBytes](../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md "../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md") CloudWatch metric. If you are ingesting more than 4 MB/sec,
  this can cause an increase in `MillisBehindLatest`. To improve your
  application's throughput, increase the value of the
  `InputParallelism` parameter. For more information, see [Parallelizing Input Streams for Increased Throughput](input-parallelism.md "input-parallelism.md").
- Check your application's output delivery [Success](../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md "../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md") metric
  for failures in delivering to your destination. Verify that you have correctly configured the output, and that your output stream
  has sufficient capacity.
- If your application uses an AWS Lambda function for pre-processing or as an output, check the application’s [InputProcessing.Duration](../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md "../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md") or
  [LambdaDelivery.Duration](../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md "../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md") CloudWatch metric. If the Lambda function invocation duration
  is longer than 5 seconds, consider doing the following:
  - Increase the Lambda function’s **Memory** allocation. You can do this on the
    AWS Lambda console, on the **Configuration** page, under
    **Basic settings**. For more information, see
    [Configuring Lambda
    Functions](../../../lambda/latest/dg/resource-model.md "../../../lambda/latest/dg/resource-model.md") in the _AWS Lambda Developer
    Guide_.
  - Increase the number of shards in your input stream of the application. This increases the
    number of parallel functions that the application will invoke, which
    might increase throughput.
  - Verify that the function is not making blocking calls that are affecting performance, such as
    synchronous requests for external resources.
  - Examine your AWS Lambda function to see whether there are other areas where you can improve
    performance. Check the CloudWatch Logs of the application Lambda function. For more
    information, see [Accessing Amazon CloudWatch Metrics for](../../../lambda/latest/dg/monitoring-functions-access-metrics.md "../../../lambda/latest/dg/monitoring-functions-access-metrics.md") in the
    _AWS Lambda Developer Guide_.

- Verify that your application is not reaching the default limit for
  Kinesis Processing Units (KPU). If your application is reaching this limit, you can request a limit increase. For more
  information, see [Automatically Scaling Applications to Increase
  Throughput](how-it-works-autoscaling.md "how-it-works-autoscaling.md").
- If your application is still having issues after having your KPU limit increase, check that your application's input throughput
  does not exceed 100MB/sec. If it exceeds 100MB/sec, we recommend implementing changes to reduce overall throughput to stabilize the application,
  for example by reducing the amount of data being sent to the data source that the Kinesis Data Analytics Sql application reads from.
  We also recommended other approaches, including increasing the paralellism of the application, reducing the time period of computations,
  changing columnar data types from VARCHAR to data types with smaller sizes (e.g., INTEGER, LONG, etc), and
  reducing data processed by sampling or filtering.

###### Note

We advise periodically reviewing your application’s `InputProcessing.OkBytes` metric so that you can plan ahead to use
multiple SQL applications or migrate to managed-flink/latest/java/ if your application’s projected input throughput will exceed 100 MB/sec.
