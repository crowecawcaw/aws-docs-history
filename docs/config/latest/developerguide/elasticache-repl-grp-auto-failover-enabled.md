

# elasticache-repl-grp-auto-failover-enabled
<a name="elasticache-repl-grp-auto-failover-enabled"></a>

Checks if Amazon ElastiCache Redis replication groups have automatic failover enabled. The rule is NON\_COMPLIANT for an ElastiCache replication group if ‘AutomaticFailover’ is not set to ‘enabled’. 



**Identifier:** ELASTICACHE\_REPL\_GRP\_AUTO\_FAILOVER\_ENABLED

**Resource Types:** AWS::ElastiCache::ReplicationGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d745c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).