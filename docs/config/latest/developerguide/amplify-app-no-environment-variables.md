# amplify-app-no-environment-variables

Checks that AWS Amplify apps do not contain environment variables. The rule is NON_COMPLIANT if configuration.EnvironmentVariables is not an empty list.

**Identifier:** AMPLIFY_APP_NO_ENVIRONMENT_VARIABLES

**Resource Types:** AWS::Amplify::App

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
