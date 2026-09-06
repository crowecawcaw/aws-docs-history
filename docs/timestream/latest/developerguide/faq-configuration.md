

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Configuration and parameter groups FAQ for Amazon Timestream for InfluxDB 3
<a name="faq-configuration"></a>

Questions about configuring Amazon Timestream for InfluxDB 3 clusters using parameter groups. For the full parameter reference, see [Parameter Groups for DB Clusters in Amazon Timestream](parameter-groups.md).

**How can I check the current running configuration of my cluster?**  
You can verify the effective parameter values on a running cluster by querying the `_internal` database's `nodes` table:  

```
SELECT * FROM _internal.nodes
```
This returns the active configuration for each node in your cluster. Use this to verify parameter values before and after applying a new parameter group.

**What are parameter groups?**  
Parameter groups contain engine configuration values that control how your InfluxDB 3 cluster operates. They include settings for query execution, memory management, compaction, caching, and more. Amazon Timestream provides default parameter groups, and you can create custom ones.

**How do I create a custom parameter group?**  
Use the AWS CLI or the AWS Management Console to create a parameter group. Specify the edition (Core or Enterprise) and the parameters you want to customize. For example:  

```
aws timestream-influxdb create-db-parameter-group \
  --name "my-custom-pg" \
  --description "Custom parameter group" \
  --parameters '{
    "InfluxDBv3Enterprise": {
      "queryFileLimit": 500,
      "queryLogSize": 2000
    }
  }'
```

**Can I modify a parameter group after creation?**  
No. Parameter groups are immutable once created. To change parameters, create a new parameter group and assign it to your cluster using the `update-db-cluster` command. The update applies immediately and reboots your instance.

**Are parameter changes applied at runtime?**  
No. All parameters are startup-only. There is no runtime reconfiguration. To apply changes, the cluster must be restarted with the updated parameter group.

**Which parameters should I avoid changing?**  
Some parameters must not be changed after initial cluster setup because they affect how data is physically organized on disk. Changing them can cause data corruption or query failures. These include:  
+ `gen1-duration` – Controls first-level compaction window (default: 10 minutes)
+ `compaction-gen2-duration` – Controls second-level compaction window
+ `compaction-multipliers` – Controls higher-level compaction ratios
When creating a new parameter group, always keep these values identical to your current configuration. For the full list of parameters and their impact, see [Detailed Parameter Reference](detailed-parameter-reference.md).

**What is the best practice for creating a parameter group?**  
Start from a default parameter group or clone an existing one, then modify only the specific parameters you need to change. Cloning is available through the AWS Management Console and ensures you inherit all safe defaults. Only adjust parameters you understand and have tested, and always preserve the compaction-related parameters (`gen1-duration`, `compaction-gen2-duration`, `compaction-multipliers`) unchanged.

**How should I size parameter values for my instance type?**  
Parameter values should be tuned based on your instance type's vCPU and memory capacity. Key guidelines:  
+ **DataFusion threads** – Set to the number of vCPUs on your instance (for example, 16 for `db.influx.4xlarge`).
+ **DataFusion max parquet fanout** – Scale with instance size: 250–500 for small instances, up to 5,000–10,000 for 12xlarge and above.
+ **exec-mem-pool-bytes** – Keep at the default of 20% for mixed workload nodes. For query-only nodes, you can increase up to 70%.
+ **parquet-mem-cache-size** – Keep at the default of 20% for most workloads. Increase to 25% for db.influx.4xlarge and above.
For detailed per-instance sizing tables, see [Detailed Parameter Reference](detailed-parameter-reference.md).