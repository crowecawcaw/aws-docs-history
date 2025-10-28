# Develop enhanced fan-out consumers

with KCL 2.x

###### Important

Amazon Kinesis Client Library (KCL) versions 1.x and 2.x are outdated. KCL 1.x will reach end-of-support on January 30, 2026. We **strongly recommend** that you migrate your KCL applications using version 1.x to the latest KCL version before January 30, 2026. To find the latest KCL version, see [Amazon Kinesis Client Library page on GitHub](https://github.com/awslabs/amazon-kinesis-client "https://github.com/awslabs/amazon-kinesis-client"). For information about the latest KCL versions, see [Use Kinesis Client Library](kcl.md "kcl.md"). For information about migrating from KCL 1.x to KCL 3.x, see [Migrating from KCL 1.x to KCL
3.x](kcl-migration-1-3.md "kcl-migration-1-3.md").

Consumers that use _enhanced fan-out_ in Amazon Kinesis Data Streams can receive
records from a data stream with dedicated throughput of up to 2 MB of data per second
per shard. This type of consumer doesn't have to contend with other consumers that are
receiving data from the stream. For more information, see [Develop enhanced fan-out consumers with dedicated
throughput](enhanced-consumers.md "enhanced-consumers.md").

You can use version 2.0 or later of the Kinesis Client Library (KCL) to develop
applications that use enhanced fan-out to receive data from streams. The KCL
automatically subscribes your application to all the shards of a stream, and ensures
that your consumer application can read with a throughput value of 2 MB/sec per shard.
If you want to use the KCL without turning on enhanced fan-out, see [Developing Consumers Using the Kinesis Client Library 2.0](developing-consumers-with-kcl-v2.md "developing-consumers-with-kcl-v2.md").

###### Topics

- [Develop enhanced fan-out
  consumers using KCL 2.x in Java](building-enhanced-consumers-kcl-java.md "building-enhanced-consumers-kcl-java.md")
