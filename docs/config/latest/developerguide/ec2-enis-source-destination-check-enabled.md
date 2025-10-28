# ec2-enis-source-destination-check-enabled

Checks if EC2 ENIs managed by users have source/destination check enabled. The rule is NON_COMPLIANT if source/destination check is disabled on these ENIs for 'lambda', 'aws_codestar_connections_managed', 'branch', 'efa', 'interface', and 'quicksight'.

**Identifier:** EC2_ENIS_SOURCE_DESTINATION_CHECK_ENABLED

**Resource Types:** AWS::EC2::NetworkInterface

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
