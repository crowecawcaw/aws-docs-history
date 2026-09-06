

# ec2-launch-template-public-ip-disabled
<a name="ec2-launch-template-public-ip-disabled"></a>

Checks if Amazon EC2 Launch Templates are set to assign public IP addresses to Network Interfaces. The rule is NON\_COMPLIANT if the default version of an EC2 Launch Template has at least 1 Network Interface with 'AssociatePublicIpAddress' set to 'true'. 



**Identifier:** EC2\_LAUNCH\_TEMPLATE\_PUBLIC\_IP\_DISABLED

**Resource Types:** AWS::EC2::LaunchTemplate

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

exemptedLaunchTemplates (Optional)Type: CSV  
Comma-separated list of exempted EC2 Launch Template IDs that are allowed to have Network Interfaces with the AssociatePublicIpAddress value set to 'true'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d575c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).