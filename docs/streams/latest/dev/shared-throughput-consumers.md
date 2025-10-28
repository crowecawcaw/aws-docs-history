# Develop custom consumers with shared

throughput

###### Important

Amazon Kinesis Client Library (KCL) versions 1.x and 2.x are outdated. KCL 1.x will reach end-of-support on January 30, 2026. We **strongly recommend** that you migrate your KCL applications using version 1.x to the latest KCL version before January 30, 2026. To find the latest KCL version, see [Amazon Kinesis Client Library page on GitHub](https://github.com/awslabs/amazon-kinesis-client "https://github.com/awslabs/amazon-kinesis-client"). For information about the latest KCL versions, see [Use Kinesis Client Library](kcl.md "kcl.md"). For information about migrating from KCL 1.x to KCL 3.x, see [Migrating from KCL 1.x to KCL
3.x](kcl-migration-1-3.md "kcl-migration-1-3.md").

If you don't need dedicated throughput when receiving data from Kinesis Data Streams, and if you don't
need read propagation delays under 200 ms, you can build consumer applications as described
in the following topics. You can use the Kinesis Client Library (KCL) or the
AWS SDK for Java.

###### Topics

- [Develop custom consumers with shared throughput using
  KCL](custom-kcl-consumers.md "custom-kcl-consumers.md")
  For information about building consumers that can receive records from Kinesis data streams
  with dedicated throughput, see [Develop enhanced fan-out consumers with dedicated
  throughput](enhanced-consumers.md "enhanced-consumers.md").
