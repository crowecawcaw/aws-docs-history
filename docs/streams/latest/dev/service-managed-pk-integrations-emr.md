

# Amazon EMR with service-managed streams
<a name="service-managed-pk-integrations-emr"></a>

Amazon EMR uses the Spark connector to read from and write to Kinesis Data Streams streams. The connector has no logic that depends on the partition key value for reading or writing data. When Amazon EMR consumes from a service-managed stream, no changes are required.

**Important**  
When Amazon EMR *produces* to a stream, the Spark connector writes through the KPL with aggregation enabled. Aggregation is not supported on service-managed streams. An Amazon EMR producer that uses a Spark connector with aggregation enabled can still write to a service-managed stream, but the aggregated records can be silently dropped by KCL consumers during de-aggregation, with no error surfaced by the producer or consumer. To produce to a service-managed stream from Amazon EMR safely, use a connector version that lets you disable KPL aggregation, or disable aggregation in your job configuration. For more information, see [KPL and KCL with service-managed streams](service-managed-pk-kpl.md).