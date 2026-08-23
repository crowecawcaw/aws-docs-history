# Supported configurations

| Configuration         | Amazon S3 general purpose buckets                |
| --------------------- | ------------------------------------------------ |
| Cluster / broker type | Amazon MSK Provisioned with Express brokers only |
| Input format          | JSON, ByteArray, String                          |
| Output format         | Objects (compression: NONE, GZIP, or ZSTD)       |
| Schema source         | Not required                                     |
| Schema evolution      | Not applicable                                   |
| Partitioning          | Object key template                              |
| Data freshness        | 5–15 minutes (default 10)                        |
| Storage class         | STANDARD, INTELLIGENT\_TIERING, GLACIER\_IR      |
