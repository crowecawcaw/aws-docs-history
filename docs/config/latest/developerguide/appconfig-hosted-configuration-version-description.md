# appconfig-hosted-configuration-version-description

Checks if AWS AppConfig hosted configuration versions have a description. The rule is NON_COMPLIANT if configuration.Description does not exist or is an empty string.

**Identifier:** APPCONFIG_HOSTED_CONFIGURATION_VERSION_DESCRIPTION

**Resource Types:** AWS::AppConfig::HostedConfigurationVersion

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
