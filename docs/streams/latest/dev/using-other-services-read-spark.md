# Apache Spark

Apache Spark is a unified analytics engine for large-scale data processing. It
provides high-level APIs in Java, Scala, Python and R, and an optimized engine that
supports general execution graphs. You can use Apache Spark to build stream processing
applications that consume the data in your Kinesis data streams.

To consume Kinesis data streams using Apache Spark Structured Streaming, use the
Amazon Kinesis Data Streams [connector](https://github.com/awslabs/spark-sql-kinesis-connector "https://github.com/awslabs/spark-sql-kinesis-connector"). This connector supports consumption with Enhanced Fan-Out, which
provides your application with dedicated read throughput of up to 2 MB of data per
second per shard. For more information, see [Developing Custom Consumers with Dedicated Throughput (Enhanced Fan-Out)](enhanced-consumers.md "enhanced-consumers.md").

To consume Kinesis data streams using Spark Streaming, see [Spark
Streaming + Kinesis Integration](https://spark.apache.org/docs/latest/streaming-kinesis-integration.html "https://spark.apache.org/docs/latest/streaming-kinesis-integration.html").
