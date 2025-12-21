# iam-user-no-policies-check

Checks if none of your AWS Identity and Access Management (IAM) users have policies attached. IAM users must inherit permissions from IAM groups or roles. The rule is NON_COMPLIANT if there is at least one IAM user with policies attached.

**Identifier:** IAM_USER_NO_POLICIES_CHECK

**Resource Types:** AWS::IAM::User

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
