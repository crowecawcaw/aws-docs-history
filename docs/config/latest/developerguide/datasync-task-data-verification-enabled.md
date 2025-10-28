# datasync-task-data-verification-enabled

Checks if AWS DataSync tasks have data verification enabled to perform additional verification at the end of your transfer. The rule is NON_COMPLIANT if configuration.Options.VerifyMode is 'NONE'.

**Identifier:** DATASYNC_TASK_DATA_VERIFICATION_ENABLED

**Resource Types:** AWS::DataSync::Task

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
