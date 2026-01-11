# Amazon DocumentDB Quotas and limits

This topic describes the resource quotas, limits, and naming constraints for Amazon DocumentDB (with MongoDB compatibility).

For certain management features, Amazon DocumentDB uses operational technology that is shared with Amazon Relational Database Service (Amazon RDS) and Amazon Neptune.

###### Topics

- [Supported instance types](#limits-suported_instance_types "#limits-suported_instance_types")
- [Supported regions](#limits-region_availability "#limits-region_availability")
- [Regional quotas](#limits-regional_quotas "#limits-regional_quotas")
- [Aggregation limits](#limits-aggregation "#limits-aggregation")
- [Cluster limits](#limits-cluster "#limits-cluster")
- [Instance limits](#limits.instance "#limits.instance")
- [Naming constraints](#limits-naming_constraints "#limits-naming_constraints")
- [TTL constraints](#limits.ttl-constraints "#limits.ttl-constraints")
- [Elastic cluster limits](#elastic.cluster.limits "#elastic.cluster.limits")
- [Elastic cluster shard limits](#elastic.cluster.shard.limits "#elastic.cluster.shard.limits")
- [Elastic cluster CPU, memory, connection, and cursor limits per shard](#elastic.cluster.memory.limits "#elastic.cluster.memory.limits")

## Supported instance types

Amazon DocumentDB supports on-demand instances and the following instance types:

- NVMe-backed:
  - **R6GD instance types:**
    `db.r6gd.xlarge`, `db.r6gd.2xlarge`,
    `db.r6gd.4xlarge`, `db.r6gd.8xlarge`,
    `db.r6gd.12xlarge`, `db.r6gd.16xlarge`.

- Memory optimized:
  - **R6G instance types:**
    `db.r6g.large`, `db.r6g.2xlarge`,
    `db.r6g.4xlarge`, `db.r6g.8xlarge`, `db.r6g.12xlarge`, `db.r6g.16xlarge`.
  - **R5 instance types:**
    `db.r5.large`, `db.r5.2xlarge`,
    `db.r5.4xlarge`, `db.r5.8xlarge`, `db.r5.12xlarge`, `db.r5.16xlarge`
    `db.r5.24xlarge`.
  - **R4 instance types:**
    `db.r4.large`, `db.r4.2xlarge`,
    `db.r4.4xlarge`, `db.r4.8xlarge`,
    `db.r4.16xlarge`.

- Burstable performance:
  - **T4G instance types:**
    `db.t4g.medium`.
  - **T3 instance types:**
    `db.t3.medium`.

For more information on the supported instance types and their specifications, see [Instance class specifications](db-instance-classes.md#db-instance-class-specs "db-instance-classes.md#db-instance-class-specs").

## Supported regions

Amazon DocumentDB is available in the following AWS regions:

| Region Name               | Region           | Availability Zones (compute) |
| ------------------------- | ---------------- | ---------------------------- |
| US East (Ohio)            | `us-east-2`      | 3                            |
| US East (N. Virginia)     | `us-east-1`      | 6                            |
| US West (Oregon)          | `us-west-2`      | 4                            |
| Africa (Cape Town)        | `af-south-1`     | 3                            |
| South America (São Paulo) | `sa-east-1`      | 3                            |
| Asia Pacific (Hong Kong)  | `ap-east-1`      | 3                            |
| Asia Pacific (Hyderabad)  | `ap-south-2`     | 3                            |
| Asia Pacific (Malaysia)   | `ap-southeast-5` | 3                            |
| Asia Pacific (Mumbai)     | `ap-south-1`     | 3                            |
| Asia Pacific (Osaka)      | `ap-northeast-3` | 3                            |
| Asia Pacific (Seoul)      | `ap-northeast-2` | 4                            |
| Asia Pacific (Singapore)  | `ap-southeast-1` | 3                            |
| Asia Pacific (Sydney)     | `ap-southeast-2` | 3                            |
| Asia Pacific (Jakarta)    | `ap-southeast-3` | 3                            |
| Asia Pacific (Thailand)   | `ap-southeast-7` | 3                            |
| Asia Pacific (Tokyo)      | `ap-northeast-1` | 3                            |
| Canada (Central)          | `ca-central-1`   | 3                            |
| China (Beijing) Region    | `cn-north-1`     | 3                            |
| China (Ningxia)           | `cn-northwest-1` | 3                            |
| Europe (Frankfurt)        | `eu-central-1`   | 3                            |
| Europe (Ireland)          | `eu-west-1`      | 3                            |
| Europe (London)           | `eu-west-2`      | 3                            |
| Europe (Milan)            | `eu-south-1`     | 3                            |
| Europe (Paris)            | `eu-west-3`      | 3                            |
| Europe (Spain)            | `eu-south-2`     | 3                            |
| Europe (Stockholm)        | `eu-north-1`     | 3                            |
| Mexico (Central)          | `mx-central-1`   | 3                            |
| Middle East (UAE)         | `me-central-1`   | 3                            |
| Israel (Tel Aviv)         | `il-central-1`   | 3                            |
| AWS GovCloud (US-West)    | `us-gov-west-1`  | 3                            |
| AWS GovCloud (US-East)    | `us-gov-east-1`  | 3                            |

## Regional quotas

For certain management features, Amazon DocumentDB uses operational technology
that is shared with Amazon Relational Database Service (Amazon RDS). The following
table contains regional limits that are shared among Amazon DocumentDB and Amazon RDS.

###### Note

The Amazon RDS shared technology described above only applies to Amazon DocumentDB instance-based clusters. Amazon DocumentDB elastic clusters do not share technology with Amazon RDS.

The following limits apply to Amazon DocumentDB instance-based clusters and are per AWS account per region.

| Resource                         | AWS default limit |
| -------------------------------- | ----------------- |
| Clusters                         | 40                |
| Cluster parameter groups         | 50                |
| Event subscriptions              | 20                |
| Instances                        | 40                |
| Manual cluster snapshots         | 100               |
| Read replicas per cluster        | 15                |
| Subnet groups                    | 50                |
| Subnets per subnet group         | 20                |
| Tags per resource                | 50                |
| VPC security groups per instance | 5                 |

The following limits apply to Amazon DocumentDB elastic clusters and are per AWS account per region.

| Resource                        | AWS default limit |
| ------------------------------- | ----------------- |
| Elastic clusters                | 20                |
| Elastic clusters vCPU           | 1024              |
| Manual elastic cluster snapshot | 20                |

You can use Service Quotas to request an increase for a quota, if the
quota is adjustable. Some requests are automatically resolved, while
others are submitted to Support. You can track the status of a quota
increase request that is submitted to Support. Requests to increase
service quotas do not receive priority support. If you have an urgent
request, please contact [Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
For more information on Service Quotas, see [What Is Service Quotas?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md")

###### To request a quota increase for Amazon DocumentDB:

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas") and, if
   necessary, sign in.
2. In the navigation pane, choose **AWS services**.
3. Select Amazon DocumentDB (with MongoDB compatibility) or Amazon DocumentDB Elastic Cluster from the list, or type either in the search
   field.
4. If the quota is adjustable, you can select its radio button or
   its name, and then choose **Request quota increase** from the top right of the page.
5. For **Change quota value**, enter the new
   value. The new value must be greater than the current value.
6. Choose **Request**. After the request is
   resolved, the **Applied quota value** for the
   quota is set to the new value.
7. To view any pending or recently resolved requests, choose
   **Dashboard** from the navigation pane. For
   pending requests, choose the status of the request to open the
   request receipt. The initial status of a request is `Pending`.
   After the status changes to `Quota requested`, you'll
   see the case number with Support. Choose the case number to
   open the ticket for your request.

## Aggregation limits

The following table describes aggregation limits in Amazon DocumentDB.

| Resource                           | Limit |
| ---------------------------------- | ----- |
| Maximum number of supported stages | 500   |

## Cluster limits

The following table describes Amazon DocumentDB instance-based cluster limits.

| Resource                                                                                                  | Limit       |
| --------------------------------------------------------------------------------------------------------- | ----------- |
| Cluster size (sum of all collections and indexes)                                                         | 128 TiB     |
| Collection size  (sum of all collections can't exceed<br>cluster limit) – does not include the index size | 32 TiB      |
| Collections per cluster                                                                                   | 100,000     |
| Databases per cluster                                                                                     | 100,000     |
| Database size (sum of all databases can't exceed cluster<br>limit)                                        | 128 TiB     |
| Document nesting depth                                                                                    | 200 levels  |
| Document size                                                                                             | 16 MiB      |
| Index key size                                                                                            | 2,048 bytes |
| Indexes per collection                                                                                    | 64          |
| Keys in a compound index                                                                                  | 32          |
| Maximum number of writes in a single batch command                                                        | 100,000     |
| Number of users per cluster                                                                               | 1000        |

## Instance limits

The following table describes Amazon DocumentDB limits per instance.

| Instance type  | Instance memory (GiB) | Connections (all) | Cursor limit | Open transactions | Connections (active) |
| -------------- | --------------------- | ----------------- | ------------ | ----------------- | -------------------- |
| T3.medium      | 4                     | 1000              | 30           | 50                | 102                  |
| T4G.medium     | 4                     | 1000              | 30           | 50                | 102                  |
| R4.large       | 15.25                 | 1700              | 450          | N/A               | 1100                 |
| R4.xlarge      | 30.5                  | 3400              | 450          | N/A               | 2700                 |
| R4.2xlarge     | 61                    | 6800              | 450          | N/A               | 4500                 |
| R4.4xlarge     | 122                   | 13600             | 725          | N/A               | 4500                 |
| R4.8xlarge     | 288                   | 27200             | 1450         | N/A               | 4500                 |
| R4.16xlarge    | 488                   | 30000             | 2900         | N/A               | 4500                 |
| R5.large       | 16                    | 3400              | 450          | 200               | 1100                 |
| R5.xlarge      | 32                    | 7000              | 450          | 400               | 2700                 |
| R5.2xlarge     | 64                    | 14200             | 450          | 800               | 4500                 |
| R5.4xlarge     | 128                   | 28400             | 760          | 1600              | 4500                 |
| R5.8xlarge     | 256                   | 60000             | 1520         | 3200              | 4500                 |
| R5.12xlarge    | 384                   | 60000             | 2280         | 4800              | 4500                 |
| R5.16xlarge    | 512                   | 60000             | 3040         | 6400              | 4500                 |
| R5.24xlarge    | 768                   | 60000             | 4560         | 9600              | 4500                 |
| R6G.large\*    | 16                    | 3400              | 450          | 200               | 1100                 |
| R6G.xlarge\*   | 32                    | 7000              | 450          | 400               | 2700                 |
| R6G.2xlarge\*  | 64                    | 14200             | 450          | 800               | 4500                 |
| R6G.4xlarge\*  | 128                   | 28400             | 760          | 1600              | 4500                 |
| R6G.8xlarge\*  | 256                   | 60000             | 1520         | 3200              | 4500                 |
| R6G.12xlarge\* | 384                   | 60000             | 2280         | 4800              | 4500                 |
| R6G.16xlarge\* | 512                   | 60000             | 3040         | 6400              | 4500                 |

\* including R6GD

You can monitor and alarm on the per instance limits using the following CloudWatch metrics. For more on Amazon DocumentDB CloudWatch metrics, see [Monitoring Amazon DocumentDB with CloudWatch](cloud_watch.md "cloud_watch.md").

| Resource          | CloudWatch limit metric  | CloudWatch usage metric (1-min. max) | CloudWatch usage metric |
| ----------------- | ------------------------ | ------------------------------------ | ----------------------- |
| Instance Memory   | -                        | -                                    | FreeableMemory          |
| Connections (all) | DatabaseConnectionsLimit | DatabaseConnectionsMax               | DatabaseConnections     |
| Cursors           | DatabaseCursorsLimit     | DatabaseCursorsMax                   | DatabaseCursors         |
| Transactions      | TransactionsOpenLimit    | TransactionsOpenMax                  | TransactionsOpen        |

## Naming constraints

The following table describes naming constraints in Amazon DocumentDB.

| Resource                                         | Default limit                                                                                                                                                                                                                                                                          |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cluster identifier                               | • Length is [1–63] letters, numbers, or hyphens.<br>• First character must be a letter.<br>• Cannot end with a hyphen or contain two consecutive hyphens.<br>• Must be unique for all clusters (across Amazon RDS, Amazon Neptune, and Amazon DocumentDB) per AWS account, per Region. |
| Collection name: `<col>`                         | Length is [1–57] characters.                                                                                                                                                                                                                                                           |
| Database name: `<db>`                            | Length is [1–63] characters.                                                                                                                                                                                                                                                           |
| Fully qualified collection name: `<db>.<col>`    | Length is [3–120] characters.                                                                                                                                                                                                                                                          |
| Fully qualified index name: `<db>.<col>$<index>` | Length is [6–377] characters.                                                                                                                                                                                                                                                          |
| Index name: `<col>$<index>`                      | Length is [3–255] characters.                                                                                                                                                                                                                                                          |
| Instance identifier                              | • Length is [1–63] letters, numbers, or hyphens<br>• First character must be a letter<br>• Cannot end with a hyphen or contain two consecutive hyphens<br>• Must be unique for all instances (across Amazon RDS, Amazon Neptune, and Amazon DocumentDB) per AWS account, per Region.   |
| Primary password                                 | • Length is [8-100] printable ASCII characters.<br>• Can use any printable ASCII characters except for the following:<br>+ `/` (forward slash)<br>+ `"` (double quotation mark)<br>+ `@` (at symbol)                                                                                   |
| Primary user name                                | • Length is [1-63] alphanumeric characters.<br>• First character must be a letter.<br>• Cannot be a word reserved by the database engine.                                                                                                                                              |
| Parameter group name                             | • Length is [1–255] alphanumeric characters.<br>• First character must be a letter.<br>• Cannot end with a hyphen or contain two consecutive hyphens.                                                                                                                                  |

## TTL constraints

Deletes from a TTL index are not guaranteed within a specific timeframe
and are best effort. Factors like instance resource utilization, document
size, and overall throughput can affect the timing of a TTL delete.

## Elastic cluster limits

The following table describes maximum limits in Amazon DocumentDB elastic clusters.

| Resource                                                               | Limit                                                                                                           |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Elastic clusters per region                                            | 20                                                                                                              |
| vCPU summed across all elastic clusters per region                     | 1024                                                                                                            |
| Manual cluster snapshots per region                                    | 20                                                                                                              |
| Shards per cluster                                                     | 32                                                                                                              |
| Storage per cluster (when data is evenly distributed by shard-key)     | 4 PiB                                                                                                           |
| Connections to cluster                                                 | The lower value of either 300,000 or the number of shards x the connection limit associated with vCPU per shard |
| UnSharded collection size                                              | 32 TiB                                                                                                          |
| Sharded collection size (when data is evenly distributed by shard-key) | 1PB                                                                                                             |
| Databases per cluster                                                  | 10,000                                                                                                          |
| UnSharded collections per cluster                                      | 100,000                                                                                                         |
| Sharded collections per cluster                                        | 1000                                                                                                            |
| Users per cluster                                                      | 100                                                                                                             |
| Writes in a single batch command                                       | 100,000                                                                                                         |
| Indexes per collection                                                 | 64                                                                                                              |
| Document nesting depth                                                 | 100 levels                                                                                                      |
| Document size                                                          | 16MB                                                                                                            |
| Index key size                                                         | 2048 bytes                                                                                                      |
| Keys in a compound index                                               | 32                                                                                                              |

## Elastic cluster shard limits

The following table describes maximum shard limits in Amazon DocumentDB elastic clusters.

| Resource                         | Limit   |
| -------------------------------- | ------- |
| vCPU per shard instance          | 64      |
| Instances per shard              | 16      |
| Storage per shard                | 128 TiB |
| Storage per collection per shard | 32 TiB  |

## Elastic cluster CPU, memory, connection, and cursor limits per shard

The following table describes maximum CPU, memory, connection, and cursor limits in Amazon DocumentDB elastic cluster shards.

| vCPUs per shard | Instance memory (GiB) | Connection limit | Cursor limit |
| --------------- | --------------------- | ---------------- | ------------ |
| 2               | 16                    | 1700             | 450          |
| 4               | 32                    | 3500             | 450          |
| 8               | 64                    | 7100             | 450          |
| 16              | 128                   | 14200            | 760          |
| 32              | 256                   | 28400            | 1520         |
| 48              | 384                   | 30000            | 2280         |
| 64              | 512                   | 30000            | 3040         |
