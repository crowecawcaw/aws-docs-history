

# What each component tolerates
<a name="dr-posture"></a>


| Component | Configuration | On Availability Zone loss | 
| --- | --- | --- | 
| DynamoDB | Point-in-time recovery enabled on 19 tables; most carry a retain-on-delete policy | Regionally redundant by service design. No action. | 
| Amazon S3 | Versioning enabled on the data buckets | Regionally redundant by service design. No action. | 
| ElastiCache for Redis | Two cache nodes, Multi-AZ with automatic failover | Fails over automatically. Live vehicle state survives. | 
| Managed Streaming for Apache Kafka | Two broker nodes across subnets; topics at replication factor 2 | Survives the loss of one broker, with no redundancy remaining until it is replaced. See the caution below. | 
| Managed Service for Apache Flink | Checkpointing enabled at 60-second intervals | The service restarts the application and resumes from the last checkpoint. Up to a minute of in-flight processing is reprocessed rather than lost. | 
| ECS services, Lambda, API Gateway | Regional services across the VPC’s subnets | Tasks reschedule automatically. Simulation sessions in progress are lost. | 

**Important**  
 **The Kafka cluster has two brokers and topics at replication factor 2, so a single broker loss leaves each partition with one in-sync replica and no tolerance for a second failure.** Ingestion continues, but the cluster is one fault from data loss until the broker is replaced. For a production deployment, raise the broker count and the replication factor together, and set a minimum in-sync replica count so a partition that cannot meet it rejects writes rather than silently accepting unreplicated ones.