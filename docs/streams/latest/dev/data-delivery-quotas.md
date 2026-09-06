# Delivery quotas and limits

The following tables describe the quotas and delivery constraints for streaming tables
and Amazon S3 delivery in Amazon Kinesis Data Streams.

## Resource quotas

| Resource              | Default | Adjustable | Notes                                                                                                         |
| --------------------- | ------- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| Deliveries per stream | 2       | No         | One delivery to streaming tables on Apache Iceberg and one<br>delivery to a general purpose Amazon S3 bucket. |
| Streams per delivery  | 1       | No         | Each delivery reads from exactly one stream.                                                                  |
| Tables per delivery   | 1       | No         | Each delivery writes to exactly one destination table.                                                        |

###### Note

The number of deliveries in an account is bounded by the On-Demand streams per
account per Region quota, because each stream can have a maximum of two deliveries.
For the streams-per-account quota, see [Quotas and limits](service-sizes-and-limits.md "service-sizes-and-limits.md").

## API limits

| Limit                                      | Default                         | Notes                                                 |
| ------------------------------------------ | ------------------------------- | ----------------------------------------------------- |
| API throttle rate (per account per Region) | 5 transactions per second (TPS) | Applies to control plane API operations.              |
| ListChannels maximum results per page      | 100                             | Use pagination tokens to retrieve additional results. |

## Delivery constraints

The following constraints apply to all delivery configurations:

- Deliveries support append-only delivery. Records cannot be updated or deleted
  at the destination.
- Data delivery does not support cross-Region delivery for either destination
  type. The Kinesis Data Streams stream and the destination must be in the same Region.
- Streaming table (Apache Iceberg) delivery does not support cross-account
  delivery. The source stream, the destination S3 table bucket, and AWS Glue Schema
  Registry must all be in the same AWS account.
- For general purpose Amazon S3 delivery, only the destination bucket can be in a
  different AWS account. The channel and its source stream must be in the same
  account.
- No transformations are applied to the data. Records are delivered as-is from
  the stream to the destination.
- Data delivery does not support schema evolution. Changing the schema requires deleting and
  recreating the delivery.
- Deliveries do not backfill existing data. Only records written to the stream
  after the delivery reaches ACTIVE state are delivered.
- Each delivery creates a new table at the destination. You cannot deliver to
  an existing table.
- The source Kinesis Data Streams stream must be in On-Demand Standard or On-Demand Advantage
  capacity mode. Provisioned mode is not supported.

## Update constraints

Only the following properties can be updated on an existing delivery:

- `DataFreshnessInSeconds`
- `LoggingConfiguration`

All other configuration properties are immutable after creation. To change any other
setting, you must delete the existing delivery and create a new one with the
desired configuration.
