After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Limits

## Discontinuation dates

After careful consideration, we have made the decision to discontinue Amazon Kinesis Data Analytics
for SQL applications. To help you plan and migrate away from Amazon Kinesis Data Analytics for SQL
applications, we will discontinue the offering gradually over 15 months. There are two
important dates to note, **October 15, 2025**, and
**January 27, 2026**.

1. On **October 15, 2025**, we will stop your
   applications and place them into a `READY` state. You will be able to
   _re-start_ your applications at that time and continue to
   use your applications as normal, subject to service limits.
2. From **October 15, 2025**, you will not be able to
   create _new_ Amazon Kinesis Data Analytics for SQL applications. You will be able
   to run any _existing_ applications as normal, subject to service
   limits.
3. We will delete your applications starting **January 27,
   2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics
   for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for
   SQL applications from that time.

We recommend that you migrate your applications to [Amazon Managed Service for Apache Flink](../../../managed-flink/latest/java/what-is.md "../../../managed-flink/latest/java/what-is.md") or [Amazon Managed Service for Apache Flink
Studio](https://aws.amazon.com/managed-service-apache-flink/studio/ "https://aws.amazon.com/managed-service-apache-flink/studio/") before October 15, 2025. For resources to assist with your migration,
see [Migrating to Managed Service for Apache
Flink Studio Examples](migrating-to-kda-studio-overview.md "migrating-to-kda-studio-overview.md"). To learn more about Amazon Managed Service for Apache Flink or
Amazon Managed Service for Apache Flink Studio, see the [Amazon Managed Service for Apache Flink developer guide](../../../managed-flink/latest/java/what-is.md "../../../managed-flink/latest/java/what-is.md").

## Limits

When working with Amazon Kinesis Data Analytics for SQL Applications, note the following limits:

- Kinesis Data Analytics for SQL is available in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Canada (Central), Europe (Paris), Europe (Ireland), Europe (Frankfurt), Europe (London), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Sydney), Asia Pacific (Singapore), Asia Pacific (Seoul), Asia Pacific (Tokyo), South America (Sao Paulo), AWS GovCloud (US-East), AWS GovCloud (US-West). We have no plans to launch Kinesis Data Analytics for SQL into additional AWS Regions.
- After June 28, 2023, you will be not be able to create new Kinesis Data Analytics for SQL
  applications using the AWS management console if you do not already use
  Kinesis Data Analytics for SQL. For information about Kinesis Data Analytics for
  SQL discontinuation dates, see [Discontinuation dates](#discontinuation-dates "#discontinuation-dates"). If you created a Kinesis Data Analytics for SQL
  application before June 28 2023, there are no changes to how you create and run
  applications today in an AWS Region where you already use Kinesis Data
  Analytics for SQL. However, you will no longer be able to create new
  applications using the AWS Console in a Region where you do not use Kinesis
  Data Analytics for SQL.
- After September 12, 2023, you will not be able to create new applications using Kinesis Data
  Firehose as a source if you do not already use Kinesis Data Analytics for SQL. For information about Kinesis Data Analytics for
  SQL discontinuation dates, see [Discontinuation dates](#discontinuation-dates "#discontinuation-dates").
  Existing customers using Kinesis Data Analytics for SQL applications with
  `KinesisFirehoseInput` can continue to add applications with
  `KinesisFirehoseInput` within an existing account using Kinesis Data
  Analytics. If you are an existing customer and wish to create a new account with
  Kinesis Data Analytics for SQL applications with `KinesisFirehoseInput`
  you can open a support case. For more information, see the
  [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
- The size of a row in an in-application stream is limited to 512 KB. Kinesis Data Analytics uses up to 1 KB to store metadata. This metadata counts against
  the row limit.
  If record size on the streaming source is greater than 50 KB, you can split the record into multiple rows in your application stream by providing appropriate schema in the input configuration by providing row delimiter.
- The SQL code in an application is limited to 100 KB.
- The longest window we recommend for a windowed query is one hour. In-application streams are stored in volatile
  storage, and unexpected application interruptions will cause the application to rebuild the stream from the source
  data in the volatile storage.
- The most throughput we recommend for a single in-application stream is between 2 and 20 MB/second, depending
  on the complexity of the application's query.
- You can create up to 50 Kinesis Data Analytics applications per AWS Region in your account. You
  can create a case to request additional applications via the service limit increase
  form. For more information, see the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
- The maximum streaming throughput a single Kinesis Data Analytics for SQL application can process is approximately
  100 MB/sec. This assumes that you have increased the number of in-application streams to the maximum
  value of 64, and you have increased your KPU limit beyond 8 (see the following limit for details).
  If your application needs to process more than 100 MB/sec of input, do one of the following:
  - Use multiple Kinesis Data Analytics for SQL applications to process input
  - Use [Managed Service for Apache Flink for Java Applications](../../../managed-flink/latest/java/what-is.md "../../../managed-flink/latest/java/what-is.md")
    if you want to continue to use a single stream and application.

###### Note

We advise periodically reviewing your application’s `InputProcessing.OkBytes`
metric so that you can plan ahead to use multiple SQL applications or
migrate to Amazon Managed Service for Apache Flink for Java Applications if your application’s projected
input throughput exceeds 100 MB/sec. We also advise creating a CloudWatch alarm on
`InputProcessing.OkBytes` so that you are notified when your
application is nearing input throughput limit. This can be useful as you can
update your application query to tradeoff for higher throughput, thereby
avoiding backpressure and delay in analytics. For more information, see
[Troubleshooting](troubleshooting.md "troubleshooting.md"). Alarming can also be useful if you have a
mechanism to reduce throughput in upstream.

- The number of Kinesis processing units (KPU) is limited to eight. For
  instructions on how to request an increase to this limit, see **To request a limit increase** in [Amazon Service Limits](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

With Kinesis Data Analytics, you pay only for what you use. You are charged an hourly rate
based on the average number of KPUs that are used to run your stream-processing
application. A single KPU provides you with 1 vCPU and 4 GB of memory.

- Each application can have one streaming source and up to one reference data
  source.
- You can configure up to three destinations for your Kinesis Data Analytics application. We recommend
  that you use one of these destinations to persist in-application error stream data.
- The Amazon S3 object that stores reference data can be up to 1 GB in size.
- If you change the reference data that is stored in the S3 bucket after you
  upload reference data to an in-application table, you need to use the [UpdateApplication](API_UpdateApplication.md "API_UpdateApplication.md")
  operation (using the API or AWS CLI) to refresh the data in the in-application table.
  Currently, the AWS Management Console doesn't support refreshing reference data in your
  application.
- Currently, Kinesis Data Analytics doesn't support data generated by the [Amazon Kinesis Producer
  Library (KPL)](../../../kinesis/latest/dev/developing-producers-with-kpl.md "../../../kinesis/latest/dev/developing-producers-with-kpl.md").
- You can assign up to 50 tags per application.
