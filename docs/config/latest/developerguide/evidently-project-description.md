# evidently-project-description

Checks if Amazon CloudWatch Evidently projects have a description. The rule is NON_COMPLIANT if configuration.Description does not exist or is an empty string.

**Identifier:** EVIDENTLY_PROJECT_DESCRIPTION

**Resource Types:** AWS::Evidently::Project

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
