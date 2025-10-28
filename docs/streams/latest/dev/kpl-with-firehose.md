# Use the KPL with Amazon Data Firehose

If you use the Kinesis Producer Library (KPL) to write data to a Kinesis data stream, you can
use aggregation to combine the records that you write to that Kinesis data stream. If you then
use that data stream as a source for your Firehose delivery stream, Firehose de-aggregates the
records before it delivers them to the destination. If you configure your delivery stream to
transform the data, Firehose de-aggregates the records before it delivers them to AWS Lambda. For
more information, see [Writing to
Amazon Firehose Using Kinesis Data Streams](../../../firehose/latest/dev/writing-with-kinesis-streams.md "../../../firehose/latest/dev/writing-with-kinesis-streams.md").
