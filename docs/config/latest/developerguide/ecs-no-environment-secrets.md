# ecs-no-environment-secrets

Checks if secrets are passed as container environment variables. The rule is NON\_COMPLIANT if 1 or more environment variable key matches a key listed in the '`secretKeys`' parameter (excluding environmental variables from other locations such as Amazon S3).

###### Note

This rule only evaluates the latest active revision of an Amazon ECS task definition.

**Identifier:** ECS\_NO\_ENVIRONMENT\_SECRETS

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei) Region

**Parameters:**

secretKeys
Type: CSV

Comma-separated list of key names to search for in the environment variables of container definitions within Task Definitions. Extra spaces will be removed.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
