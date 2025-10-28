# Decompress CloudWatch Logs

If you are using Firehose to deliver CloudWatch Logs and want to deliver decompressed data to your
Firehose stream destination, use Firehose [Data Format Conversion](data-transformation.md "data-transformation.md")
(Parquet, ORC) or [Dynamic partitioning](dynamic-partitioning.md "dynamic-partitioning.md").
You must enable decompression for your Firehose stream.

You can enable decompression using the AWS Management Console, AWS Command Line Interface or AWS SDKs.

###### Note

If you enable the decompression feature on a stream, use that stream exclusively for CloudWatch Logs
subscriptions filters, and not for Vended Logs. If you enable the decompression
feature on a stream that is used to ingest both CloudWatch Logs and Vended Logs, the Vended
Logs ingestion to Firehose fails. This decompression feature is only for CloudWatch Logs.
