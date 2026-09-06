

# Metadata and ACL replication
<a name="msk-replicator-metadata-acl"></a>

MSK Replicator supports copying metadata from the source cluster to the target cluster. The metadata includes topic configuration, Access Control Lists (ACLs), and consumer group offsets. Like data replication, metadata replication happens asynchronously. For better performance, MSK Replicator prioritizes data replication over metadata replication.

The following table lists the Access Control Lists (ACLs) that MSK Replicator copies.


| Operation | Resource | APIs allowed | 
| --- | --- | --- | 
| Alter | Topic | CreatePartitions | 
| AlterConfigs | Topic | AlterConfigs | 
| Create | Topic | CreateTopics, Metadata | 
| Delete | Topic | DeleteRecords, DeleteTopics | 
| Describe | Topic | ListOffsets, Metadata, OffsetFetch, OffsetForLeaderEpoch | 
| DescribeConfigs | Topic | DescribeConfigs | 
| Read | Topic | Fetch, OffsetCommit, TxnOffsetCommit | 
| Write (deny only) | Topic | Produce, AddPartitionsToTxn | 

MSK Replicator copies LITERAL pattern type ACLs only for resource type Topic. PREFIXED pattern type ACLs and other resource type ACLs are not copied. MSK Replicator also does not delete ACLs on the target cluster. If you delete an ACL on the source cluster, you should also delete it on the target cluster at the same time. For more details on Kafka ACLs, see [Kafka ACL documentation](https://kafka.apache.org/documentation/#security_authz_cli).

MSK Replicator replicates only Kafka ACLs, which IAM access control does not use. If your clients are using IAM access control to read/write to your MSK clusters, you need to configure the relevant IAM policies on your target cluster as well for seamless failover. This is true for both Prefixed and Identical topic name replication configurations.

**Note**  
MSK Replicator does not replicate write ACLs since your producers should not be writing directly to the replicated topic in the target cluster. Your producers should write to the local topic in the target cluster after failover.