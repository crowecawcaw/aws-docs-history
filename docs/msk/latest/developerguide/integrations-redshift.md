# Amazon Redshift streaming data ingestion for Amazon MSK

Amazon Redshift supports streaming ingestion from Amazon MSK. The Amazon Redshift streaming ingestion feature
provides low-latency, high-speed ingestion of streaming data from Amazon MSK into an
Amazon Redshift materialized view. Because it doesn't need to stage data in Amazon S3, Amazon Redshift can ingest
streaming data at a lower latency and at a reduced storage cost. You can configure Amazon Redshift
streaming ingestion on an Amazon Redshift cluster using SQL statements to authenticate and connect
to an Amazon MSK topic.

For more information, see [Streaming ingestion](../../../redshift/latest/dg/materialized-view-streaming-ingestion.md "../../../redshift/latest/dg/materialized-view-streaming-ingestion.md") in the _Amazon Redshift Database Developer Guide_.
