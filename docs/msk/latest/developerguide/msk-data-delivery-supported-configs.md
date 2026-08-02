# Supported configurations

| Configuration         | S3 Tables (Iceberg)                                                  | S3 bucket                                        |
| --------------------- | -------------------------------------------------------------------- | ------------------------------------------------ |
| Cluster / broker type | Amazon MSK Provisioned with Express brokers only                     | Amazon MSK Provisioned with Express brokers only |
| Input format          | JSON or JSON\_SCHEMA\_GSR                                            | JSON, ByteArray, String                          |
| Output format         | Apache Iceberg tables; Parquet files with ZSTD or Snappy compression | Objects (compression: NONE, GZIP, or ZSTD)       |
| Schema source         | AWS Glue Schema Registry (required)                                  | Not required                                     |
| Schema evolution      | Not supported                                                        | Not applicable                                   |
| Partitioning          | Time-based (TIME\_HOUR)                                              | Object key template                              |
| Data freshness        | 5–15 minutes (default 10)                                            | 5–15 minutes (default 10)                        |
| Storage class         | Managed by S3 Tables                                                 | STANDARD, INTELLIGENT\_TIERING, GLACIER\_IR      |

###### Note

**S3 Tables input formats:** `JSON` is plain JSON objects — you provide the Glue Schema Registry ARN that defines the schema. `JSON_SCHEMA_GSR` is GSR-serialized JSON, where the schema ID is embedded in each record.
