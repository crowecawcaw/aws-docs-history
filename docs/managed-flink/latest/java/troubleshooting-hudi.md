Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Hudi configuration best practices

To run Hudi connectors on Managed Service for Apache Flink we recommend the following configuration
changes.

Disable `hoodie.embed.timeline.server`

Hudi connector on Flink sets up an embedded timeline (TM) server on the Flink
jobmanager (JM) to cache metadata to improve performance when job parallelism is high.
We recommend that you disable this embedded server on Managed Service for Apache Flink because we disable
non-Flink communication between JM and TM.

If this server is enabled, Hudi writes will first attempt to connect to the embedded
server on JM, and then fall back to reading metadata from Amazon S3. This means that Hudi
incurs a connection timeout that delays Hudi writes and causes a performance impact on
Managed Service for Apache Flink.
