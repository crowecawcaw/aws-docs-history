After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# What Is Amazon Kinesis Data Analytics for SQL Applications?

With Amazon Kinesis Data Analytics for SQL Applications, you can process and analyze streaming data using
standard SQL. The service enables you to quickly author and run powerful SQL code against
streaming sources to perform time series analytics, feed real-time dashboards, and create
real-time metrics.

To get started with Kinesis Data Analytics, you create a Kinesis Data Analytics application that continuously
reads and processes streaming data. The service supports ingesting data from Amazon Kinesis Data Streams and
Amazon Data Firehose streaming sources. Then, you author your SQL code using the interactive editor and
test it with live streaming data. You can also configure destinations where you want Kinesis Data Analytics
to send the results.

Kinesis Data Analytics supports Amazon Data Firehose (Amazon S3, Amazon Redshift, Amazon OpenSearch Service, and Splunk), AWS Lambda, and Amazon Kinesis Data Streams as
destinations.

## When Should I Use Amazon Kinesis Data Analytics?

Amazon Kinesis Data Analytics enables you to quickly author SQL code that continuously reads, processes,
and stores data in near real time. Using standard SQL queries on the streaming data, you
can construct applications that transform and provide insights into your data. Following
are some of example scenarios for using Kinesis Data Analytics:

- **Generate time-series analytics** – You
  can calculate metrics over time windows, and then stream values to Amazon S3 or Amazon Redshift
  through a Kinesis data delivery stream.
- **Feed real-time dashboards** – You can
  send aggregated and processed streaming data results downstream to feed
  real-time dashboards.
- **Create real-time metrics** – You can
  create custom metrics and triggers for use in real-time monitoring,
  notifications, and alarms.

For information about the SQL language elements that are supported by Kinesis Data Analytics, see
[Amazon Kinesis Data Analytics SQL
Reference](../sqlref/analytics-sql-reference.md "../sqlref/analytics-sql-reference.md").

## Are You a First-Time User of Amazon Kinesis Data Analytics?

If you are a first-time user of Amazon Kinesis Data Analytics, we recommend that you read the following
sections in order:

1. Read the How It Works section of this guide.
   This section introduces various Kinesis Data Analytics components that you work with to create an
   end-to-end experience. For more information, see [Amazon Kinesis Data Analytics for SQL Applications: How It Works](how-it-works.md "how-it-works.md").
2. Try the Getting Started exercises. For more
   information, see [Getting Started with Amazon Kinesis Data Analytics for SQL
   Applications](getting-started.md "getting-started.md").
3. Explore the streaming SQL concepts. For more
   information, see [Streaming SQL Concepts](streaming-sql-concepts.md "streaming-sql-concepts.md").
4. Try additional examples. For more information,
   see [Kinesis Data Analytics for SQL examples](examples.md "examples.md").
