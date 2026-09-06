

# redshift-cluster-configuration-check
<a name="redshift-cluster-configuration-check"></a>

Checks if Amazon Redshift clusters have the specified settings. The rule is NON\_COMPLIANT if the Amazon Redshift cluster is not encrypted or encrypted with another key, or if a cluster does not have audit logging enabled. 



**Identifier:** REDSHIFT\_CLUSTER\_CONFIGURATION\_CHECK

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central) Region

**Parameters:**

loggingEnabledType: booleanDefault: true  
Audit logging is enabled

clusterDbEncryptedType: booleanDefault: true  
Database encryption is enabled

nodeTypes (Optional)Type: CSVDefault: dc1.large  
Specify node type

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1295c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).