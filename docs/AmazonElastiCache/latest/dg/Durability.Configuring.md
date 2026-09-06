

# Configuring durability
<a name="Durability.Configuring"></a>

When creating an ElastiCache cluster, you can set the `--durability` parameter to one of the following values:


**Durability parameter values**  

| --durability value | Behavior | EffectiveDurability (Valkey 9.0) | 
| --- | --- | --- | 
| sync | Writes persisted to Multi-AZ transactional log before responding to client | sync | 
| async | Writes persisted to Multi-AZ transactional log after responding to client | async | 
| disabled | No durability; standard ElastiCache behavior | disabled | 
| default | ElastiCache determines setting based on engine version and cluster configuration | disabled | 

The `EffectiveDurability` property in the API response always shows the actual durability mode in effect (sync, async, or disabled). Whether durability is enabled or disabled is determined at cluster creation time and cannot be changed afterward. You can switch between sync and async modes on an existing cluster by calling `ModifyReplicationGroup` with the `--durability` parameter.

For snapshots, ElastiCache stores the `EffectiveDurability` value so that restoring from a snapshot preserves the actual durability setting.

When you enable durability, ElastiCache automatically enables encryption at-rest on your cluster. All data at rest is encrypted, including snapshots and data in the Multi-AZ transactional log. By default, the cluster uses a service-managed KMS key, but you can also specify your own customer-managed KMS key. The encryption status is visible in the `StorageEncryptionType` field for the replication group.