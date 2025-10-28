# appconfig-deployment-strategy-minimum-final-bake-time

Checks if an AWS AppConfig deployment strategy requires the specified minimum bake time. The rule is NON_COMPLIANT if the deployment strategy has a final bake time less than value specified in the rule parameter. The default value is 30 minutes.

**Identifier:** APPCONFIG_DEPLOYMENT_STRATEGY_MINIMUM_FINAL_BAKE_TIME

**Resource Types:** AWS::AppConfig::DeploymentStrategy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

minBakeTime (Optional)
Type: int
Default: 30

The minimum bake time in minutes of the AWS AppConfig deployment strategy for the rule to check. The rule is NON_COMPLIANT if the bake time is less than the value specified in this parameter. Valid values are 0 to 1440. The default value is 30.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
