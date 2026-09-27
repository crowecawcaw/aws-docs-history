

# Amazon Managed Service for Apache Flink consuming from service-managed streams
<a name="service-managed-pk-integrations-flink"></a>

Amazon Managed Service for Apache Flink is a hosting platform that runs your Flink application; the Kinesis connector you choose determines compatibility with service-managed streams.
+ **Current connector (`flink-connector-aws-kinesis-streams`)** – Consumes from service-managed streams without modification, including records written with a null partition key. If your application uses partition keys for keyed state or windowing, be aware that partition keys may be `null`; review your logic to ensure it does not depend on partition key values for processing correctness.
+ **Legacy connector (`flink-connector-kinesis`)** – Not recommended for service-managed streams. The legacy connector uses the KPL with aggregation, and aggregation is not supported on service-managed streams. In addition, a custom deserializer that reads the partition key must guard against `null`. If you use the legacy connector, migrate to the current connector before enabling service-managed record distribution.