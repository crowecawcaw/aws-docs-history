# appconfig-deployment-strategy-description

Checks if AWS AppConfig deployment strategies have a description. The rule is NON_COMPLIANT if configuration.Description does not exist or is an empty string.

**Identifier:** APPCONFIG_DEPLOYMENT_STRATEGY_DESCRIPTION

**Resource Types:** AWS::AppConfig::DeploymentStrategy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
