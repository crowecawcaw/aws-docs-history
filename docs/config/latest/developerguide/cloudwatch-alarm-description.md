# cloudwatch-alarm-description

Checks if AWS CloudWatch Alarm resources contain an alarm description. The rule is NON_COMPLIANT if the CloudWatch Alarm resource does not contain an AlarmDescription field or the AlarmDescription is empty.

**Identifier:** CLOUDWATCH_ALARM_DESCRIPTION

**Resource Types:** AWS::CloudWatch::Alarm

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
