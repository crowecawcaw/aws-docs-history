# Supported configurations

| Configuration         | Streaming tables for Apache Iceberg                                  |
| --------------------- | -------------------------------------------------------------------- |
| Cluster / broker type | Amazon MSK Provisioned with Express brokers only                     |
| Input format          | JSON or JSON\_SCHEMA\_GSR                                            |
| Output format         | Apache Iceberg tables; Parquet files with ZSTD or Snappy compression |
| Schema source         | AWS Glue Schema Registry (required)                                  |
| Schema evolution      | Not supported                                                        |
| Partitioning          | Time-based (TIME\_HOUR)                                              |
| Data freshness        | 5–15 minutes (default 10)                                            |
| Storage class         | Managed by S3 Tables                                                 |

###### Note

**Input formats:** `JSON` is plain JSON objects — you provide the Glue Schema Registry ARN that defines the schema. `JSON_SCHEMA_GSR` is GSR-serialized JSON, where the schema ID is embedded in each record.
