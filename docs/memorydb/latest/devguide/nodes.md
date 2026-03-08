# Supported node types

MemoryDB supports the following node types.

**Memory optimized**

| Instance type   | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Enhanced I/O Multiplexing (Valkey 7.2 and Redis OSS 7.0.4+) | Minimum engine version |
| --------------- | ------------------------- | ---------------------- | ----------------------------------------------------------- | ---------------------- |
| db.r7g.large    | 0.937                     | 12.5                   | No                                                          | 6.2                    |
| db.r7g.xlarge   | 1.876                     | 12.5                   | No                                                          | 6.2                    |
| db.r7g.2xlarge  | 3.75                      | 15                     | Yes                                                         | 6.2                    |
| db.r7g.4xlarge  | 7.5                       | 15                     | Yes                                                         | 6.2                    |
| db.r7g.8xlarge  | 15                        | N/A                    | Yes                                                         | 6.2                    |
| db.r7g.12xlarge | 22.5                      | N/A                    | Yes                                                         | 6.2                    |
| db.r7g.16xlarge | 30                        | N/A                    | Yes                                                         | 6.2                    |
| db.r6g.large    | 0.75                      | 10.0                   | No                                                          | 6.2                    |
| db.r6g.xlarge   | 1.25                      | 10.0                   | No                                                          | 6.2                    |
| db.r6g.2xlarge  | 2.5                       | 10.0                   | Yes                                                         | 6.2                    |
| db.r6g.4xlarge  | 5.0                       | 10.0                   | Yes                                                         | 6.2                    |
| db.r6g.8xlarge  | 12                        | N/A                    | Yes                                                         | 6.2                    |
| db.r6g.12xlarge | 20                        | N/A                    | Yes                                                         | 6.2                    |
| db.r6g.16xlarge | 25                        | N/A                    | Yes                                                         | 6.2                    |

**Memory optimized with data tiering**

| Instance type   | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Enhanced I/O Multiplexing (Valkey 7.2 and Redis OSS 7.0.4+) | Minimum engine version |
| --------------- | ------------------------- | ---------------------- | ----------------------------------------------------------- | ---------------------- |
| db.r6gd.xlarge  | 1.25                      | 10                     | No                                                          | 6.2                    |
| db.r6gd.2xlarge | 2.5                       | 10                     | No                                                          | 6.2                    |
| db.r6gd.4xlarge | 5.0                       | 10                     | No                                                          | 6.2                    |
| db.r6gd.8xlarge | 12                        | N/A                    | No                                                          | 6.2                    |

**General purpose nodes**

| Instance type | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Enhanced I/O Multiplexing (Valkey 7.2 and Redis OSS 7.0.4+) | Minimum engine version |
| ------------- | ------------------------- | ---------------------- | ----------------------------------------------------------- | ---------------------- |
| db.t4g.small  | 0.128                     | 5.0                    | No                                                          | 6.2                    |
| db.t4g.medium | 0.256                     | 5.0                    | No                                                          | 6.2                    |

For AWS Region availability, see [MemoryDB Pricing](https://aws.amazon.com/memorydb/pricing/ "https://aws.amazon.com/memorydb/pricing/")

All node types are created in a virtual private cloud (VPC).
