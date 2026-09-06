

# AWS managed policies for AWS Security Agents
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they’re available for all AWS customers to use. We recommend that you reduce permissions further by defining [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: SecurityAgentWebAppAPIPolicy
<a name="security-iam-awsmanpol-SecurityAgentWebAppAPIPolicy"></a>

Grants permissions to interact with the Security Agent web application API. This policy enables users to configure and execute automated security penetration tests, manage test executions, view security findings, and access Security Agent resources. This policy references the legacy Agent Instance resource type and specific legacy IAM actions.

 **Permissions details** 

This policy grants permissions to interact with the Security Testing Control service (securityagent:\*) for:
+ Penetration Test Management: Create, update, delete, and list penetration tests and their execution jobs
+ Security Findings: View, describe, and update security findings from completed tests, including related content and metadata.
+ Task Management: List and retrieve code review and documentation review tasks
+ Resource Discovery: List and view agent instances, artifacts, integrations, and discovered endpoints
+ Test Execution: Start and stop penetration test executions with real-time monitoring capabilities
+ Code Remediation: Start automated code remediation for security findings

To view the latest version of the JSON policy document, see [SecurityAgentWebAppAPIPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SecurityAgentWebAppAPIPolicy.html) in the AWS Managed Policy Reference Guide.

## AWS managed policy: AWSSecurityAgentWebAppPolicy
<a name="security-iam-awsmanpol-AWSSecurityAgentWebAppPolicy"></a>

Grants permissions to interact with the Security Agent web application API. This policy enables users to configure and execute automated security penetration tests, manage test executions, view security findings, and access Security Agent resources.

 **Permissions details** 

This policy grants permissions to interact with the Security Testing Control service (securityagent:\*) for:
+ Penetration Test Management: Create, update, delete, and list penetration tests and their jobs
+ Security Findings: View, describe, and update security findings from completed tests, including related content and metadata.
+ Task Management: List and retrieve code review and design review tasks
+ Resource Discovery: List and view Agent Spaces, artifacts, integrations, and discovered endpoints
+ Test Execution: Start and stop penetration test jobs with real-time monitoring capabilities
+ Code Remediation: Start automated code remediation for security findings

To view the latest version of the JSON policy document, see [AWSSecurityAgentWebAppPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSecurityAgentWebAppPolicy.html) in the AWS Managed Policy Reference Guide.

## AWS Security Agents updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Security Agents since this service began tracking these changes.

To receive notifications of all source file changes to this specific documentation page, you can subscribe to the following URL with an RSS reader:


| Change | Description | Date | 
| --- | --- | --- | 
| Added permissions to [AWSSecurityAgentWebAppPolicy](#security-iam-awsmanpol-AWSSecurityAgentWebAppPolicy). | Added `TargetDomain` and `DesignReviewFeedback` resource permissions for the new resource types. | March 31, 2026 | 
| Added a new managed policy [AWSSecurityAgentWebAppPolicy](#security-iam-awsmanpol-AWSSecurityAgentWebAppPolicy). | Added managed policy `AWSSecurityAgentWebAppPolicy` for the new AgentSpace resource type and IAM action name changes. | February 9, 2026 | 
| Added permissions to [SecurityAgentWebAppAPIPolicy](#security-iam-awsmanpol-SecurityAgentWebAppAPIPolicy). | Added `securityagent:StartCodeRemediation` to allow users to start automated code remediation for security findings. | January 20, 2026 | 
| Added permissions to [SecurityAgentWebAppAPIPolicy](#security-iam-awsmanpol-SecurityAgentWebAppAPIPolicy). | Added `securityagent:BatchGetSecurityTestContentMetadata` to allow users to view images in the console. | December 5, 2025 | 
| AWS Security Agents started tracking changes. | AWS Security Agents started tracking changes for its AWS managed policies. | December 2, 2025 | 