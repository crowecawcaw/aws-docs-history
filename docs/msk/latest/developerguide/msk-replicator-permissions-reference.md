

# Service execution role permissions reference
<a name="msk-replicator-permissions-reference"></a>

This topic describes the minimal permissions that the Amazon MSK Replicator service execution role requires for each replicator feature. When you create a replicator, some features are enabled by default and others are optional. Use this reference to build a least-privilege policy tailored to the features you enable.

The following table summarizes which features require permissions on the source cluster, target cluster, and caller role.


| Feature | Optional | Source cluster permissions | Target cluster permissions | 
| --- | --- | --- | --- | 
| Topic replication | No | [Topic replication permissions](msk-replicator-perms-topic-replication.md) | [Topic replication permissions](msk-replicator-perms-topic-replication.md) | 
| Topic configuration replication (`copyTopicConfigurations`) | Yes (enabled by default) | [Topic configuration replication permissions](msk-replicator-perms-topic-config-replication.md) | [Topic configuration replication permissions](msk-replicator-perms-topic-config-replication.md) | 
| Access control list (ACL) replication (`copyAccessControlListsForTopics`) | Yes (enabled by default) | [ACL replication permissions](msk-replicator-perms-acl-replication.md) | [ACL replication permissions](msk-replicator-perms-acl-replication.md) | 
| Consumer group offset sync (`synchroniseConsumerGroupOffsets`) | Yes (enabled by default) | [Consumer group offset sync permissions](msk-replicator-perms-consumer-group-sync.md) | [Consumer group offset sync permissions](msk-replicator-perms-consumer-group-sync.md) | 

**Note**  
You attach log delivery permissions to the *caller role* (the IAM principal that calls `CreateReplicator`), not to the service execution role. For more information, see [Log delivery permissions](msk-replicator-perms-log-delivery.md).