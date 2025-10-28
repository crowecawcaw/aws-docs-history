# Read data from Amazon Kinesis Data Streams

A _consumer_ is an application that processes all data
from a Kinesis data stream. When a consumer uses _enhanced
fan-out_, it gets its own 2 MB/sec allotment of read throughput, allowing
multiple consumers to read data from the same stream in parallel, without contending for
read throughput with other consumers. To use the enhanced fan-out capability of shards, see
[Develop enhanced fan-out consumers with dedicated
throughput](enhanced-consumers.md "enhanced-consumers.md").

You can build consumers for Kinesis Data Streams using Kinesis Client Library (KCL) or AWS SDK for Java.
You can also develop consumers using other AWS services such as AWS Lambda, Amazon Managed Service for Apache Flink, and
Amazon Data Firehose. Kinesis Data Streams supports integrations with other AWS services such as Amazon EMR, Amazon EventBridge,
AWS Glue, and Amazon Redshift It also supports third party integrations including Apache Flink, Adobe
Experience Platform, Apache Druid, Apache Spark, Databricks, Confluent Platform, Kinesumer,
and Talend.

###### Topics

- [Develop enhanced fan-out consumers with dedicated
  throughput](enhanced-consumers.md "enhanced-consumers.md")
- [Use the Data Viewer in the Kinesis console](data-viewer.md "data-viewer.md")
- [Query your data streams in the Kinesis console](querying-data.md "querying-data.md")
- [Use Kinesis Client Library](kcl.md "kcl.md")
- [Develop consumers with the AWS SDK for Java](develop-consumers-sdk.md "develop-consumers-sdk.md")
- [Develop consumers using AWS Lambda](lambda-consumer.md "lambda-consumer.md")
- [Develop consumers using Amazon Managed Service for Apache Flink](kda-consumer.md "kda-consumer.md")
- [Develop consumers using Amazon Data Firehose](kdf-consumer.md "kdf-consumer.md")
- [Read data from Kinesis Data Streams using other AWS services](using-other-services-read.md "using-other-services-read.md")
- [Read from Kinesis Data Streams using third-party
  integrations](using-services-third-party-read.md "using-services-third-party-read.md")
- [Troubleshoot Kinesis Data Streams consumers](troubleshooting-consumers.md "troubleshooting-consumers.md")
- [Optimize Amazon Kinesis Data Streams consumers](advanced-consumers.md "advanced-consumers.md")
