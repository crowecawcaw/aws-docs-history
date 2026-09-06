

# ec2-enis-source-destination-check-enabled
<a name="ec2-enis-source-destination-check-enabled"></a>

Checks if EC2 ENIs managed by users have source/destination check enabled. The rule is NON\_COMPLIANT if source/destination check is disabled on these ENIs for 'lambda', 'aws\_codestar\_connections\_managed', 'branch', 'efa', 'interface', and 'quicksight'. 



**Identifier:** EC2\_ENIS\_SOURCE\_DESTINATION\_CHECK\_ENABLED

**Resource Types:** AWS::EC2::NetworkInterface

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d547c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).