

# Using foreign tables with Aurora Global Database
<a name="aurora-analytics-global-database"></a>

Aurora Global Database supports running analytical queries with per-Region setup. This section describes how to configure analytical queries across Regions, which resources replicate automatically, and how to plan for disaster recovery scenarios.

**Topics**
+ [Using aurora\_analytics with a Global Database](#aurora-analytics-gdb-using)
+ [Setting up on a Global Database](#aurora-analytics-gdb-setup)
+ [Region pinning of foreign tables](#aurora-analytics-gdb-region-pinning)
+ [Handling switchover and failover](#aurora-analytics-gdb-switchover-failover)
+ [Error messages on a Global Database](#aurora-analytics-gdb-errors)

## Using aurora\_analytics with a Global Database
<a name="aurora-analytics-gdb-using"></a>

A foreign table is a PostgreSQL table definition that points to your Apache Iceberg or Parquet data in Amazon S3, Amazon S3 Tables, or the AWS Glue Data Catalog. No data is copied into Aurora. Only the following replicate from the primary DB cluster to each secondary DB cluster:
+ The `aurora_analytics` extension installation
+ Foreign table definitions (DDL)

The following do not replicate and must be provisioned independently in every Region that contains a secondary DB cluster:
+ The IAM role association to the DB cluster
+ The IAM policy granting access to Amazon S3, AWS Glue, or Amazon S3 Tables
+ VPC networking (endpoints or NAT) used to reach those services

## Setting up on a Global Database
<a name="aurora-analytics-gdb-setup"></a>

### Step 1: Create the IAM policy and role in every Region
<a name="aurora-analytics-gdb-setup-step1"></a>

The IAM role association does not replicate between the primary and secondary DB clusters. You must create and attach an IAM role with the `AuroraAnalytics` feature name in every Region that contains a primary or secondary DB cluster.

1. Create an IAM policy granting read access to your data. The required permissions depend on your data format. For more information, see [IAM policies reference](aurora-analytics-iam-policies-reference.md).

1. Create an IAM role trusted by `rds.amazonaws.com` and attach the policy.

1. Associate the role with that Region's DB cluster:

   ```
   aws rds add-role-to-db-cluster \
     --db-cluster-identifier <cluster-in-this-region> \
     --role-arn arn:aws:iam::<account-id>:role/AuroraAnalyticsRole \
     --feature-name AuroraAnalytics
   ```

1. Wait until the role status shows as **Active**.

**Note**  
Immediately after a role is attached (or after an instance starts or is promoted), queries against foreign tables might briefly return the error: `credential to access AWS service is unavailable`. Wait until the role status is **Active** before running queries on foreign tables.

### Step 2: Set up networking in every Region
<a name="aurora-analytics-gdb-setup-step2"></a>

VPC configuration also does not replicate. In the VPC for each DB cluster (primary and every secondary), provide a network path to the required services so that the DB cluster can reach the foreign table data to resolve queries. Ensure each secondary's cluster networking configuration permits reaching the foreign table's Region.


**Required VPC endpoints for each Region**  

| Service | Endpoint type | Required for | 
| --- | --- | --- | 
| Amazon S3 (com.amazonaws.<region>.s3) | Gateway | All Amazon S3 and Amazon S3 Tables data access | 
| AWS Glue (com.amazonaws.<region>.glue) | Interface | AWS Glue Data Catalog access (Iceberg tables) | 
| AWS STS (com.amazonaws.<region>.sts) | Interface | IAM role credential retrieval | 

For the AWS Glue and AWS STS interface endpoints, enable Private DNS and allow inbound TCP 443 from your VPC CIDR.

### Step 3: Install the extension on the primary
<a name="aurora-analytics-gdb-setup-step3"></a>

Connect to the writer DB instance in the primary DB cluster and install the extension in each database where you intend to create foreign tables:

```
CREATE EXTENSION aurora_analytics;
```

The extension replicates to each secondary DB cluster automatically.

### Step 4: Create foreign tables on the primary
<a name="aurora-analytics-gdb-setup-step4"></a>

On the writer DB instance in the primary DB cluster, create foreign tables pointing to your data:

```
-- Parquet via S3 URI
CREATE FOREIGN TABLE ft_orders ()
SERVER aurora_analytics_server
OPTIONS (location 's3://my-bucket/orders/',
         format 'parquet', region 'us-east-1');

-- Iceberg via Glue ARN
CREATE FOREIGN TABLE ft_transactions ()
SERVER aurora_analytics_server
OPTIONS (location 'arn:aws:glue:us-east-1:123456789012:table/mydb/transactions',
         format 'iceberg');
```

Aurora replicates the DDL to each secondary DB cluster, where the foreign tables are available for querying.

### Step 5: Verify on the secondary
<a name="aurora-analytics-gdb-setup-step5"></a>

Connect to a secondary DB cluster and confirm replication and read access:

```
SELECT extname, extversion FROM pg_extension WHERE extname = 'aurora_analytics';
SELECT count(*) FROM ft_orders;
```

## Region pinning of foreign tables
<a name="aurora-analytics-gdb-region-pinning"></a>

When you create a foreign table, its data `location` and `Region` are stored in the table definition and replicate to every DB cluster in the global database. Every DB cluster reads from the same location.

This implies:
+ Each secondary DB cluster reads foreign table data from the Region specified in the table definition.
+ If that Region differs from the secondary's Region, reads are cross-Region, which adds data transfer costs and latency.
+ Each secondary's IAM role and networking permit reaching the foreign table's Region.

**Note**  
Amazon S3 Multi-Region Access Points (MRAPs) are not supported as a foreign table location. Aurora PostgreSQL accepts only `s3://` URIs, AWS Glue Table ARNs, and Amazon S3 Tables ARNs in the `location` option. MRAP ARNs and MRAP hostnames are not valid for the `location` option.

### General guidance for DR readiness
<a name="aurora-analytics-gdb-dr-readiness"></a>

Complete the per-Region setup in Steps 1–2 for the secondary DB cluster, then decide how the DB cluster will access foreign table data:
+ **Accept cross-Region reads:** This approach is suitable only for planned switchover scenarios where the original Region is healthy.
+ **Pre-stage a Region-local copy:** Use Amazon S3 Cross-Region Replication so analytical queries can read locally even if the original Region is unavailable. Prepare `ALTER FOREIGN TABLE ... OPTIONS (SET ...)` statements to update the foreign table locations to point to the Region-local copy.

**Note**  
The on-disk read cache is not persisted or transferred when a switchover or failover occurs. The first queries after the event read data from Amazon S3 and run with higher latency until the cache warms up.

## Handling switchover and failover
<a name="aurora-analytics-gdb-switchover-failover"></a>

During an Aurora Global Database switchover or failover, foreign table queries have an additional dependency beyond standard database client connections: they must reach Amazon S3, AWS Glue, and AWS STS in the Region named by each foreign table.

### Global Database Switchover
<a name="aurora-analytics-gdb-switchover"></a>

Both the primary and secondary DB clusters are healthy at the time of switchover. After the new primary DB cluster becomes available, queries continue to read from the Region named in each foreign table. If that Region is different from the new writer's Region, reads are cross-Region and incur data transfer costs and latency. To avoid cross-Region read latency, run the prepared `ALTER FOREIGN TABLE ... OPTIONS (SET ...)` statements to repoint foreign tables to a Region-local copy.

#### Resuming operations after a switchover
<a name="aurora-analytics-gdb-resuming"></a>

1. Allow clients to reconnect to the writer endpoint of the new primary DB cluster.

1. Wait until the IAM role status is **Active**. Run a test query against a foreign table (for example, `SELECT count(*) FROM ft_orders`) with retry logic to confirm that analytics queries are operational.

1. If using a Region-local copy, run the prepared `ALTER` statements on the new primary DB cluster to update the foreign table locations:

   ```
   ALTER FOREIGN TABLE ft_orders OPTIONS (SET location 's3://dr-region-bucket/orders/', SET region 'us-west-2');
   ALTER FOREIGN TABLE ft_transactions OPTIONS (SET location 'arn:aws:glue:us-west-2:123456789012:table/mydb/transactions');
   ```

**Note**  
`ALTER FOREIGN TABLE ... OPTIONS (SET ...)` is a catalog metadata-only change. It completes immediately with no data movement. It takes a brief `ACCESS EXCLUSIVE` lock on that single foreign table. Therefore, it is blocked by any in-flight query on the same table.

### Global Database Failover
<a name="aurora-analytics-gdb-failover"></a>

The original Region might be impaired or unreachable. If a foreign table names the impaired Region, queries against it experience high latency or fail with timeout errors until that Region recovers or you repoint the foreign table to data in a healthy Region. If you pre-staged a Region-local copy, run the prepared `ALTER FOREIGN TABLE ... OPTIONS (SET region ...)` statements to point foreign tables to the Region-local copy.

### Returning to the original primary Region
<a name="aurora-analytics-gdb-returning"></a>

When the original primary Region becomes available, Aurora automatically adds it back to the global database as a secondary DB cluster. Any `ALTER FOREIGN TABLE` changes made during the switchover or failover replicate to it through global replication. To restore the original primary Region, perform a switchover. After the switchover completes, determine whether to revert the foreign table locations to point to data in the restored primary Region.

## Error messages on a Global Database
<a name="aurora-analytics-gdb-errors"></a>

After a switchover or failover, queries in the new primary Region can fail with the same IAM role association, IAM permission, and networking errors that affect any Region running a secondary DB cluster. These errors and their resolutions are covered in Global Database switchover and failover under [Monitoring and troubleshooting](aurora-analytics-monitoring-troubleshooting.md). The prerequisites must be satisfied in each secondary Region, because the IAM role association, IAM policy, and VPC networking do not replicate.
+ Foreign table `location` and `region` are a single replicated definition with no per-Region override. Both clusters cannot hold different Regions for the same table.
+ Amazon S3 Multi-Region Access Points and Amazon S3 access-point ARNs are not supported as foreign table locations.
+ VPC gateway endpoints are regional and cannot reach another Region's Amazon S3. A cross-Region network path requires NAT/internet egress or Transit Gateway.
+ After a switchover, updating a foreign table location to the new primary DB cluster's Region causes the former primary DB cluster to read cross-Region instead.
+ Foreign table DDL and the extension replicate only after the secondary is attached and in sync. Install the `aurora_analytics` extension and create foreign tables on the primary after the secondary is connected so they propagate.