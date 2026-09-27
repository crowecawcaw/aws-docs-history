

# Streaming tables and Amazon S3 delivery with service-managed streams
<a name="service-managed-pk-integrations-streaming-tables"></a>

You can deliver records from a Kinesis Data Streams stream to streaming tables and to Amazon Simple Storage Service (Amazon S3) delivery destinations. On a service-managed stream, records written without a partition key are delivered normally, along with records that include a partition key. No changes are required.