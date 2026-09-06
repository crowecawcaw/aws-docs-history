

# Prerequisites and limitations
<a name="Redis-Global-Datastores-Getting-Started"></a>

Before getting started with global datastores, be aware of the following:
+ Global datastores are supported in the following AWS Regions:
  + **Africa** - Cape Town
  + **Asia Pacific** - Hong Kong, Hyderabad, Jakarta, Malaysia, Melbourne, Mumbai, Osaka, Seoul, Singapore, Sydney, Thailand, and Tokyo 
  + **Canada** - Canada Central and Canada West (Calgary)
  + **China** - Beijing and Ningxia
  + **Europe ** - Frankfurt, London, Ireland, Milan, Paris, Spain, Stockholm, and Zurich
  + **AWS GovCloud** -US-West and US-East
  + **Israel** - Tel Aviv
  + **Middle East** - Bahrain and UAE
  + **US** - East (N. Virginia and Ohio) and US West (N. California and Oregon)
  + **South America** - Mexico (Central) and São Paulo
+  All clusters—primary and secondary—in your global datastore should have the same number of primary nodes, node type, engine version, and number of shards (in case of cluster-mode enabled). Each cluster in your global datastore can have a different number of read replicas to accommodate the read traffic local to that cluster. 

  Replication must be enabled if you plan to use an existing single-node cluster.
**Important**  
When you add a secondary cluster to a global datastore, the secondary cluster inherits the Multi-AZ and automatic failover settings from the primary cluster. Automatic failover requires at least 2 nodes (1 primary and 1 replica). If you enabled automatic failover on the primary cluster, each secondary cluster must also have at least 1 replica. You cannot add a single-node secondary cluster to a global datastore if you enabled automatic failover on the primary.
+ Global datastores are supported on the following instance families in size large and above: M5, M6g, M7g, M8g, R5, R6g, R6gd, R7g, R8g, C7gn, and C8gn. Previous generation instance types (such as M4 and R4) are not supported.
**Note**  
Supported node types may vary between AWS Regions. For more details, see [Amazon ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/).
+ You can set up replication for a primary cluster from one AWS Region to a secondary cluster in up to two other AWS Regions. 
**Note**  
The exception to this are China (Beijing) Region and China (Ningxia) regions, where replication can only occur between the two regions. 
+ Global datastores require clusters running in an Amazon VPC. For more information, see [Access Patterns for Accessing an ElastiCache Cache in an Amazon VPC](elasticache-vpc-accessing.md).
**Note**  
At this time, you can't use global datastores in [Using local zones with ElastiCache](Local_zones.md).
+ ElastiCache doesn't support autofailover from one AWS Region to another. When needed, you can promote a secondary cluster manually. For an example, see [Promoting the secondary cluster to primary](Redis-Global-Datastores-Console.md#Redis-Global-Datastores-Console-Promote-Secondary). 
+ To bootstrap from existing data, use an existing cluster as primary to create a global datastore. We don't support adding an existing cluster as secondary. The process of adding the cluster as secondary wipes data, which may result in data loss. 
+ Parameter updates are applied to all clusters when you modify a local parameter group of a cluster belonging to a global datastore. 
+ You can scale regional clusters both vertically (scaling up and down) and horizontally (scaling in and out). You can scale the clusters by modifying the global datastore. All the regional clusters in the global datastore are then scaled without interruption. For more information, see [Scaling ElastiCache](Scaling.md).
+ Global datastores support [encryption at rest](at-rest-encryption.md), [encryption in transit](in-transit-encryption.md), and [AUTH](auth.md). 
+ Global datastores doesn't support Internet Protocol version 6 (IPv6).
+  Global datastores support AWS KMS keys. For more information, see [AWS key management service concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) in the *AWS Key Management Service Developer Guide.* 
+ Global datastores are not supported with durability-enabled clusters.
+ When a cluster is associated with a global datastore, ElastiCache automatically disables the *Auto upgrade minor versions* setting to prevent engine version inconsistencies between member clusters. This setting cannot be re-enabled while the cluster belongs to a global datastore.
+ Global Datastore doesn't support cross-account deployments. All primary and secondary clusters must reside within the same AWS account.

**Note**  
Global datastores support [pub/sub messaging](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-use-cases.html#elasticache-for-redis-use-cases-messaging) with the following stipulations:  
For cluster-mode disabled, pub/sub is fully supported. Events published on the primary cluster of the primary AWS Region are propagated to secondary AWS Regions.
For cluster mode enabled, the following applies:  
For published events that aren't in a keyspace, only subscribers in the same AWS Region receive the events.
For published keyspace events, subscribers in all AWS Regions receive the events.