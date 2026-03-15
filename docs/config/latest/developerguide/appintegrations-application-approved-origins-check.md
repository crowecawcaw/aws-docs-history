# appintegrations-application-approved-origins-check

Checks that Amazon AppIntegrations applications do not contain approved origins. The rule is NON_COMPLIANT if configuration.ApplicationSourceConfig.ExternalUrlConfig.ApprovedOrigins is not an empty list.

**Identifier:** APPINTEGRATIONS_APPLICATION_APPROVED_ORIGINS_CHECK

**Resource Types:** AWS::AppIntegrations::Application

**Trigger type:** Configuration changes

**AWS Region:** Only available in Africa (Cape Town), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

allowedApprovedOrigins (Optional)
Type: CSV

Comma-separated list of approved origins that are allowed to access the application. If provided, the rule is NON_COMPLIANT if configuration.ApplicationSourceConfig.ExternalUrlConfig.ApprovedOrigins contains origins not specified in this parameter.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
