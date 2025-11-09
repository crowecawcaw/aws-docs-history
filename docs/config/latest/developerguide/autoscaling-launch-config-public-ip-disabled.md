# autoscaling-launch-config-public-ip-disabled

Checks if Amazon EC2 Auto Scaling groups have public IP addresses enabled through Launch Configurations. The rule is NON_COMPLIANT if the Launch Configuration for an Amazon EC2 Auto Scaling group has AssociatePublicIpAddress set to 'true'.

**Identifier:** AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED

**Resource Types:** AWS::AutoScaling::LaunchConfiguration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
