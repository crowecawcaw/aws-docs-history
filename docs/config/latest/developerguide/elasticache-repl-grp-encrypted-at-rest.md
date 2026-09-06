

# elasticache-repl-grp-encrypted-at-rest
<a name="elasticache-repl-grp-encrypted-at-rest"></a>

Checks if Amazon ElastiCache replication groups have encryption-at-rest enabled. The rule is NON\_COMPLIANT for an ElastiCache replication group if 'AtRestEncryptionEnabled' is disabled or if the KMS key ARN does not match the approvedKMSKeyArns parameter. 



**Identifier:** ELASTICACHE\_REPL\_GRP\_ENCRYPTED\_AT\_REST

**Resource Types:** AWS::ElastiCache::ReplicationGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

approvedKMSKeyIds (Optional)Type: CSV  
Comma-separated list of KMS Key IDs that are approved for ElastiCache usage.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d747c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).