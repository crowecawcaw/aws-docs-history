# redshift-require-tls-ssl

Checks if Amazon Redshift clusters require TLS/SSL encryption to connect to SQL clients. The rule is NON_COMPLIANT if any Amazon Redshift cluster has parameter require_SSL not set to true.

**Identifier:** REDSHIFT_REQUIRE_TLS_SSL

**Resource Types:** AWS::Redshift::Cluster, AWS::Redshift::ClusterParameterGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Mexico (Central) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
