# Create and manage Kinesis data streams

Amazon Kinesis Data Streams ingests a large amount of data in real time, durably stores the data, and makes
the data available for consumption. The unit of data stored by Kinesis Data Streams is a _data
record_. A _data stream_ represents a group of data
records. The data records in a data stream are distributed into shards.

A _shard_ has a sequence of data records in a stream. It serves as a
base throughput unit of a Kinesis data stream. A shard supports 1 MB/s and 1000 records per
second for _writes_ and 2 MB/s for _reads_ in both
on-demand and provisioned capacity modes. The shard limits ensure predictable performance,
making it easier to design and operate a highly reliable data streaming workflow.

In this section, you learn how to set the capacity mode for the stream and how to create a
stream using either the AWS Management Console or APIs. Then you can take additional actions on the
stream.

###### Topics

- [Choose the right mode to stream in](how-do-i-size-a-stream.md "how-do-i-size-a-stream.md")
- [Create a stream using the AWS Management Console](how-do-i-create-a-stream.md "how-do-i-create-a-stream.md")
- [Create a stream using the
  APIs](kinesis-using-sdk-java-create-stream.md "kinesis-using-sdk-java-create-stream.md")
- [Update a stream](updating-a-stream.md "updating-a-stream.md")
- [List streams](kinesis-using-sdk-java-list-streams.md "kinesis-using-sdk-java-list-streams.md")
- [List shards](kinesis-using-sdk-java-list-shards.md "kinesis-using-sdk-java-list-shards.md")
- [Delete a stream](kinesis-using-sdk-java-delete-stream.md "kinesis-using-sdk-java-delete-stream.md")
- [Reshard a stream](kinesis-using-sdk-java-resharding.md "kinesis-using-sdk-java-resharding.md")
- [Change the data retention period](kinesis-extended-retention.md "kinesis-extended-retention.md")
- [Tag your Amazon Kinesis Data Streams resources](tagging.md "tagging.md")
- [Handle large records](large-records.md "large-records.md")
- [Perform resilience testing with AWS Fault Injection Service](kinesis-fis.md "kinesis-fis.md")
