# redshift-cluster-kms-enabled

Checks if Amazon Redshift clusters are using a specified AWS Key Management Service (AWS KMS) key for encryption.
The rule is COMPLIANT if encryption is enabled and the cluster is encrypted with the key provided in the `kmsKeyArn` parameter.
The rule is NON_COMPLIANT if the cluster is not encrypted or encrypted with another key.

**Identifier:** REDSHIFT_CLUSTER_KMS_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Mexico (Central) Region

**Parameters:**

kmsKeyArns (Optional)
Type: CSV

Comma-separated list of AWS KMS key Amazon Resource Names (ARNs) used in Amazon Redshift clusters for encryption.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
