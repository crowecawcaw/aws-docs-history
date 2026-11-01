

# dsql-cluster-multi-region-replication-enabled
<a name="dsql-cluster-multi-region-replication-enabled"></a>

Checks if an Amazon Aurora DSQL cluster is replicated to another AWS Region through multi-Region peering. The rule is NON\_COMPLIANT if configuration.MultiRegionProperties.Clusters does not exist, is empty, or the cluster status is not ACTIVE. 



**Identifier:** DSQL\_CLUSTER\_MULTI\_REGION\_REPLICATION\_ENABLED

**Resource Types:** AWS::DSQL::Cluster

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Canada (Central), Canada West (Calgary), Europe (Spain) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d511c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).