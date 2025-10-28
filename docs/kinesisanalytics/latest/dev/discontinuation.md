After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Amazon Kinesis Data Analytics for SQL Applications discontinuation

## Discontinuation plan

After careful consideration, we have made the decision to discontinue Amazon Kinesis Data Analytics for SQL applications. To help you plan and migrate away from Amazon Kinesis Data Analytics for SQL applications, we will discontinue the offering gradually over 15 months. These are important dates to note, **September 1, 2025**, **October 15, 2025**, and **January 27, 2026**.

1. On **October 15, 2025**, we will stop your
   applications and place them into a `READY` state. You will be able to
   _re-start_ your applications at that time and continue to
   use your applications as normal, subject to service limits.
2. From **October 15, 2025**, you will not be able
   to create _new_ Amazon Kinesis Data Analytics for SQL applications. You will
   be able to run any _existing_ applications as normal, subject
   to service limits.
3. We will delete your applications starting **January 27,
   2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics
   for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for
   SQL applications from that time.

We recommend that you migrate your applications to [Amazon Managed Service for Apache Flink](../../../managed-flink/latest/java/what-is.md "../../../managed-flink/latest/java/what-is.md") or [Amazon Managed Service for Apache Flink
Studio](https://aws.amazon.com/managed-service-apache-flink/studio/ "https://aws.amazon.com/managed-service-apache-flink/studio/") before October 15, 2025. For resources to assist with your migration,
see [Migrating to Managed Service for Apache
Flink Studio Examples](migrating-to-kda-studio-overview.md "migrating-to-kda-studio-overview.md"). To learn more about Amazon Managed Service for Apache Flink or
Amazon Managed Service for Apache Flink Studio, see the [Amazon Managed Service for Apache Flink developer
guide](../../../managed-flink/latest/java/what-is.md "../../../managed-flink/latest/java/what-is.md").

###### Note

To view a full list of your Amazon Kinesis Data Analytics for SQL applications, you can call the
`ListApplications` API. For more information, see [ListApplications](API_ListApplications.md "API_ListApplications.md").

## Migrating to Amazon Managed Service for Apache Flink Studio

To learn more about migrating your applications and view code and architecture
examples, see [Migrating to Managed Service for Apache
Flink Studio Examples](migrating-to-kda-studio-overview.md "migrating-to-kda-studio-overview.md").

## FAQ

**Why are you no longer offering Amazon Kinesis Data Analytics for SQL
applications?**

We have found that customers prefer Amazon Managed Service for Apache Flink offerings for real-time data stream
processing workloads. Amazon Managed Service for Apache Flink is a serverless, low latency, highly scalable and
available real-time stream processing service using Apache Flink, an open source engine
for processing data streams. Amazon Managed Service for Apache Flink offers functionality such as native scaling,
exactly once processing semantics, multi-language support (including SQL), over 40
source and destination connectors, durable application state, and more. These features
help customers build end to end streaming pipelines and ensure the accuracy and
timeliness of data.

**What are customers' options now?**

We recommend customers upgrade their existing Amazon Kinesis Data Analytics for SQL applications to
either Amazon Managed Service for Apache Flink Studio or Amazon Managed Service for Apache Flink. In Amazon Managed Service for Apache Flink Studio, customers create queries
using SQL, Python, or Scala using interactive notebooks. For long running applications
in Amazon Kinesis Data Analytics for SQL, we recommend Amazon Managed Service for Apache Flink, where customers can create
applications using Java, Python, Scala, and embedded SQL using all of Apache Flink’s
APIs, connectors, and more.

**How many customers are using Amazon Kinesis Data Analytics for SQL
applications?**

We can't disclose customer information details.

**How do customers upgrade from Amazon Kinesis Data Analytics for SQL applications
to an Amazon Managed Service for Apache Flink offering?**

To upgrade to Amazon Managed Service for Apache Flink or Amazon Managed Service for Apache Flink Studio, customers must re-create their
application. To help, we have provided a library of common SQL queries and how to re-write them in Amazon Managed Service for Apache Flink
Studio. See [Replicating Kinesis Data Analytics for SQL Queries in
Managed Service for Apache Flink Studio](migrating-to-kda-studio-overview.md#examples-migrating-to-kda-studio "migrating-to-kda-studio-overview.md#examples-migrating-to-kda-studio"). We have also provided common pattern architectures that customers can followv if
they are building long running applications or using machine learning in Amazon Managed Service for Apache Flink. See [Replacing Kinesis Data Firehose as a source with
Kinesis Data Streams](migrating-to-kda-studio-overview.md#examples-firehose "migrating-to-kda-studio-overview.md#examples-firehose")

To learn more about Amazon Managed Service for Apache Flink, see [Amazon Managed Service for Apache Flink](../../../managed-flink/latest/java/what-is.md "../../../managed-flink/latest/java/what-is.md").

For migration guides, see [Migrating to Managed Service for Apache
Flink Studio Examples](migrating-to-kda-studio-overview.md "migrating-to-kda-studio-overview.md").

**Will Amazon Managed Service for Apache Flink support the existing Amazon Kinesis Data Analytics for SQL
applications features?**

Amazon Managed Service for Apache Flink supports many of the concepts available in Amazon Kinesis Data Analytics for SQL
applications such as connectors and windowing, as well as features that were unavailable
in Amazon Kinesis Data Analytics for SQL applications, such as native scaling, exactly-once processing
semantics, multi-language support (including SQL), over 40 source and destination
connectors, durable application state, and more.
