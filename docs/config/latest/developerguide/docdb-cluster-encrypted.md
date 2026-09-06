

# docdb-cluster-encrypted
<a name="docdb-cluster-encrypted"></a>

Checks if storage encryption is enabled for your Amazon DocumentDB (with MongoDB compatibility) clusters. The rule is NON\_COMPLIANT if storage encryption is not enabled. 



**Identifier:** DOCDB\_CLUSTER\_ENCRYPTED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Europe (Milan), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central), China (Ningxia) Region

**Parameters:**

kmsKeyArns (Optional)Type: CSV  
A comma-separated list of KMS key ARNs to compare with the KmsKeyID of the encrypted cluster.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d491c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).