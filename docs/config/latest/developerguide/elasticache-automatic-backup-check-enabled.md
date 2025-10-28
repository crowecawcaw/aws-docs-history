# elasticache-automatic-backup-check-enabled

Checks if Amazon ElastiCache clusters (Valkey or Redis OSS) have automatic backup turned on. The rule is NON_COMPLIANT if automated backup is not enabled or the SnapshotRetentionLimit for a cluster is less than the specified `snapshotRetentionPeriod`.

**Identifier:** ELASTICACHE_AUTOMATIC_BACKUP_CHECK_ENABLED

**Resource Types:** AWS::ElastiCache::CacheCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

snapshotRetentionPeriod (Optional)
Type: int

Minimum snapshot retention period in days for Valkey or Redis OSS. Valid values are 1 to 35. Default value is 1.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
