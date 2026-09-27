

# Amazon Redshift streaming ingestion from service-managed streams
<a name="service-managed-pk-integrations-redshift"></a>

Amazon Redshift streaming ingestion lets you create a materialized view over a Kinesis Data Streams stream. The materialized view schema includes a partition key column. When you ingest from a service-managed stream, records written without a partition key appear with a blank partition key value in the materialized view. No changes are required, and both null and non-null partition key records are ingested successfully.