

# Comparison of record distribution strategies
<a name="service-managed-pk-comparison"></a>

The following table compares the two record distribution strategies available in Kinesis Data Streams.


**Record distribution strategy comparison**  

| Characteristic | User-managed partition keys | Service-managed record distribution | 
| --- | --- | --- | 
| Partition key required | Yes – you must provide a partition key with each record | No – the service distributes records automatically | 
| Record ordering | Records with the same partition key are delivered to the same shard in order | No ordering guarantees – records are distributed for optimal throughput | 
| Shard distribution | Depends on your partition key strategy – poorly distributed keys can cause hot shards | Even distribution managed by service algorithms – eliminates hot shards | 
| Supported stream modes | On-Demand Standard, On-Demand Advantage, and Provisioned | On-Demand Standard and On-Demand Advantage only | 
| Best for | Stateful workloads requiring ordering (CDC, financial transactions, session analytics) | Stateless workloads (logs, metrics, telemetry, clickstream) | 
| Producer code changes required | N/A (existing behavior) | Refer the section [KPL and KCL with service-managed streams](service-managed-pk-kpl.md) | 