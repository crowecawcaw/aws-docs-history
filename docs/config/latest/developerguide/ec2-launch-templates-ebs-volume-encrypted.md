# ec2-launch-templates-ebs-volume-encrypted

Checks whether Amazon EC2 launch templates have encryption enabled for all attached EBS volumes.The rule is NON_COMPLIANT if encryption is set to False for any EBS volume configured in the launch template.

**Identifier:** EC2_LAUNCH_TEMPLATES_EBS_VOLUME_ENCRYPTED

**Resource Types:** AWS::EC2::LaunchTemplate

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
