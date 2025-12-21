# AWS managed policies for AWS Security Agents

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they’re available for all AWS customers to use. We recommend that you reduce permissions further by defining [customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

## AWS managed policy: SecurityAgentWebAppAPIPolicy

Grants permissions to interact with the Security Agent Web Application API. This policy enables users to configure and execute automated security penetration tests, manage test executions, view security findings, and access Security Agent resources.

**Permissions details**

This policy grants permissions to interact with the Security Testing Control service (securityagent:\*) for:

- Pentest Management: Create, update, delete, and list penetration tests and their execution jobs
- Security Findings: View, describe, and update security findings from completed tests, including related content and metadata.
- Task Management: List and retrieve code review and documentation review tasks
- Resource Discovery: List and view agent spaces, artifacts, integrations, and discovered endpoints
- Test Execution: Start and stop pentest executions with real-time monitoring capabilities

To view the latest version of the JSON policy document, see [SecurityAgentWebAppAPIPolicy](../../../aws-managed-policy/latest/reference/SecurityAgentWebAppAPIPolicy.md "../../../aws-managed-policy/latest/reference/SecurityAgentWebAppAPIPolicy.md") in the AWS Managed Policy Reference Guide.

## AWS Security Agents updates to AWS managed policies

View details about updates to AWS managed policies for AWS Security Agents since this service began tracking these changes.

To receive notifications of all source file changes to this specific documentation page, you can subscribe to the following URL with an RSS reader:

| Change                                                                                                                                                            | Description                                                                                             | Date             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------- |
| Added permissions to [SecurityAgentWebAppAPIPolicy](#security-iam-awsmanpol-SecurityAgentWebAppAPIPolicy "#security-iam-awsmanpol-SecurityAgentWebAppAPIPolicy"). | Added `securityagent:BatchGetSecurityTestContentMetadata` to allow users to view images in the console. | December 5, 2025 |
| AWS Security Agents started tracking changes.                                                                                                                     | AWS Security Agents started tracking changes for its AWS managed policies.                              | December 2, 2025 |
