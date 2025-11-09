# redshift-cluster-configuration-check

Checks if Amazon Redshift clusters have the specified settings. The rule is NON_COMPLIANT if the Amazon Redshift cluster is not encrypted or encrypted with another key, or if a cluster does not have audit logging enabled.

**Identifier:** REDSHIFT_CLUSTER_CONFIGURATION_CHECK

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Mexico (Central) Region

**Parameters:**

clusterDbEncrypted
Type: boolean
Default: true

Database encryption is enabled.

loggingEnabled
Type: boolean
Default: true

Audit logging is enabled.

nodeTypes (Optional)
Type: CSV
Default: dc1.large

Specify node type.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
