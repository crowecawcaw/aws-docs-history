

# elasticache-rbac-auth-enabled
<a name="elasticache-rbac-auth-enabled"></a>

Checks if Amazon ElastiCache replication groups have RBAC authentication enabled. The rule is NON\_COMPLIANT if the Redis version is 6 or above and ‘UserGroupIds’ is missing, empty, or does not match an entry provided by the '`allowedUserGroupIDs`' parameter. 



**Identifier:** ELASTICACHE\_RBAC\_AUTH\_ENABLED

**Resource Types:** AWS::ElastiCache::ReplicationGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

allowedUserGroupIDs (Optional)Type: CSV  
A comma-separated list of User Group IDs that are approved for ElastiCache replication group access.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d741c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).