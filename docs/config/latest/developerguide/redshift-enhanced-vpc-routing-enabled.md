# redshift-enhanced-vpc-routing-enabled

Checks if Amazon Redshift cluster has 'enhancedVpcRouting' enabled. The rule is NON_COMPLIANT if 'enhancedVpcRouting' is not enabled or if the configuration.enhancedVpcRouting field is 'false'.

**Identifier:** REDSHIFT_ENHANCED_VPC_ROUTING_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Mexico (Central) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
