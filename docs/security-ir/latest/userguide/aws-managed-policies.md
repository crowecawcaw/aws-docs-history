# AWS Managed Policies

An AWS managed policy is a standalone policy that is created and
administered by AWS. AWS managed policies are designed to
provide permissions for many common use cases so that you can
start assigning permissions to users, groups, and roles.

To add permissions to users, groups, and roles, it is easier to
use AWS managed policies than to write policies yourself. It
takes time and expertise to
[create
IAM customer managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with
only the permissions they need. To get started quickly, you can
use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more
information about AWS managed policies, see
[AWS
managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User
Guide_.

AWS services maintain and update their associated AWS managed
policies. You can't change the permissions in AWS managed
policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update
affects all identities (users, groups, and roles) where the
policy is attached. Services are most likely to update an AWS
managed policy when a new feature is launched or when new
operations become available. Services do not remove permissions
from an AWS managed policy, so policy updates won't break your
existing permissions.

Additionally, AWS supports managed policies for job functions
that span multiple services. For example, the
**ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and
resources. When a service launches a new feature, AWS adds
read-only permissions for new operations and resources. For a
list and descriptions of job function policies, see
[AWS
managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM
User Guide_.

###### Contents

- [AWS managed policy: AWSSecurityIncidentResponseServiceRolePolicy](#AWSSecurityIncidentResponseServiceRolePolicy "#AWSSecurityIncidentResponseServiceRolePolicy")
- [AWS managed policy: AWSSecurityIncidentResponseFullAccess](#AWSSecurityIncidentResponseFullAccess "#AWSSecurityIncidentResponseFullAccess")
- [AWS managed policy: AWSSecurityIncidentResponseReadOnlyAccess](#AWSSecurityIncidentResponseReadOnlyAccess "#AWSSecurityIncidentResponseReadOnlyAccess")
- [AWS managed policy: AWSSecurityIncidentResponseCaseFullAccess](#AWSSecurityIncidentResponseCaseFullAccess "#AWSSecurityIncidentResponseCaseFullAccess")
- [AWS managed policy: AWSSecurityIncidentResponseTriageServiceRolePolicy](#AWSSecurityIncidentResponseTriageServiceRolePolicy "#AWSSecurityIncidentResponseTriageServiceRolePolicy")
- [AWS Security Incident Response updates to SLRs and managed policies](#managed-policy-updates "#managed-policy-updates")

## AWS managed policy: AWSSecurityIncidentResponseServiceRolePolicy

AWS Security Incident Response uses the AWSSecurityIncidentResponseServiceRolePolicy AWS managed policy.
This AWS managed policy is attached to the [AWSServiceRoleForSecurityIncidentResponse](using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse "using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse")
service-linked role. The policy provides access for AWS Security Incident Response to identify accounts subscribed, create cases, and tag related resources.

###### Important

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags.
AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data

_Permissions details_

The service uses this policy to perform actions on the following resources:

- _AWS Organizations:_ Allows the service to lookup membership accounts for use with the service.
- _CreateCase:_ Allows the service create service cases on behalf of membership accounts.
- _TagResource:_ Allows the service tag resources configured as part of the service.

You can view the permissions associated with this policy in AWS managed policies for
[AWSSecurityIncidentResponseServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseServiceRolePolicy.md").

## AWS managed policy: AWSSecurityIncidentResponseFullAccess

AWS Security Incident Response uses the AWSSecurityIncidentResponseAdmin AWS managed policy. This policy grants full access to service
resources and access to related AWS services. You can use this policy with your IAM principals to quickly add permissions
for AWS Security Incident Response.

###### Important

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags.
AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data

_Permissions details_

The service uses this policy to perform actions on the following resources:

- _IAM principal read-only access:_ Grants a service user the ability to perform read-only actions
  against existing AWS Security Incident Response resources.
- _IAM principal write access:_ Grants a service user the ability to update, modify,
  delete, and create AWS Security Incident Response resources.

You can view the permissions associated with this policy in AWS managed policies for
[AWSSecurityIncidentResponseFullAccess](../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseFullAccess.md "../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseFullAccess.md").

## AWS managed policy: AWSSecurityIncidentResponseReadOnlyAccess

AWS Security Incident Response uses the AWSSecurityIncidentResponseReadOnlyAccess AWS managed policy. The policy grants read-only access to service case resources.
You can use this policy with your IAM principals to quickly add permissions for AWS Security Incident Response.

###### Important

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags.
AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data

_Permissions details_

The service uses this policy to perform actions on the following resources:

- _IAM principal read-only access:_ Grants a service user the ability to perform read-only actions
  against existing AWS Security Incident Response resources.

You can view the permissions associated with this policy in AWS managed policies for
[AWSSecurityIncidentResponseReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseReadOnlyAccess.md").

## AWS managed policy: AWSSecurityIncidentResponseCaseFullAccess

AWS Security Incident Response uses the AWSSecurityIncidentResponseCaseFullAccess AWS managed policy. The policy grants full access to service case resources.
You can use this policy with your IAM principals to quickly add permissions for AWS Security Incident Response.

###### Important

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags.
AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data

_Permissions details_

The service uses this policy to perform actions on the following resources:

- _IAM principal case read-only access:_ Grants a service user the ability to perform read-only actions
  against existing AWS Security Incident Response cases.
- _IAM principal case write access:_ Grants a service user the ability to update, modify,
  delete, and create AWS Security Incident Response cases.

You can view the permissions associated with this policy in AWS managed policies for
[AWSSecurityIncidentResponseCaseFullAccess](../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseCaseFullAccess.md "../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseCaseFullAccess.md").

## AWS managed policy: AWSSecurityIncidentResponseTriageServiceRolePolicy

AWS Security Incident Response uses the AWSSecurityIncidentResponseTriageServiceRolePolicy AWS managed policy.
This AWS managed policy is attached to the [AWSServiceRoleForSecurityIncidentResponse_Triage](using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse_Triage "using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse_Triage") service-linked role.

The policy provides access to AWS Security Incident Response to continuously monitor your environment for security threats,
tune security services to reduce alert noise, and gather information to investigate potential incidents. You can't attach
this policy to your IAM entities.

###### Important

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags.
AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data

_Permissions details_

The service uses this policy to perform actions on the following resources:

- _Events:_ Allows the service to create an Amazon EventBridge managed rule.
  This rule is the infrastructure required in your AWS account to deliver events from your account to the service.
  This action is performed on any AWS resource managed by `triage.security-ir.amazonaws.com`.
- _Amazon GuardDuty:_ Allows the service to tune security services to reduce alert noise and gather
  information to investigate potential incidents. This action is performed on any AWS resource.
- _AWS Security Hub:_ Allows the service to tune security services to reduce alert noise and gather
  information to investigate potential incidents. This action is performed on any AWS resource.

You can view the permissions associated with this policy in AWS managed policies for
[AWSSecurityIncidentResponseTriageServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseTriageServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSSecurityIncidentResponseTriageServiceRolePolicy.md").

## AWS Security Incident Response updates to SLRs and managed policies

View details about updates to AWS Security Incident Response SLRs and managed policies roles since this service
began tracking these changes.

| Change                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Date             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Updated – [AWSSecurityIncidentResponseServiceRolePolicy](#AWSSecurityIncidentResponseServiceRolePolicy "#AWSSecurityIncidentResponseServiceRolePolicy")                                                                                                                                                                                                                                                            | The policy now includes two new actions for `"organizations:DescribeAccount"`, `"organizations:ListDelegatedAdministrators"` and a new condition: `"Condition": { "StringEquals": { "aws:ResourceAccount": "${aws:PrincipalAccount}" } }`                                                                                                                                                                                                                                                                                       | TBD              |
| Updates to SLR adding permissions to support service entitlements.                                                                                                                                                                                                                                                                                                                                                 | [AWSSecurityIncidentResponseTriageServiceRolePolicy](#AWSSecurityIncidentResponseTriageServiceRolePolicy "#AWSSecurityIncidentResponseTriageServiceRolePolicy") has been updated to add security-ir:GetMembership, security-ir:ListMemberships, security-ir:UpdateCase, guardduty:ListFilters, guarduty:UpdateFilter, guardduty:DeleteFilter, and guardduty:GetAdministratorAccount permissions. guardduty:GetAdministratorAccount was added to facilitate management of GuardDuty Auto-Archival filters in delegated accounts. | June 02, 2025    |
| New SLR – [AWSServiceRoleForSecurityIncidentResponse](using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse "using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse") New managed policy – [AWSSecurityIncidentResponseServiceRolePolicy](#AWSSecurityIncidentResponseServiceRolePolicy "#AWSSecurityIncidentResponseServiceRolePolicy").                                       | New service linked role and attached policy allowing service access into your AWS Organizations accounts to identify membership.                                                                                                                                                                                                                                                                                                                                                                                                | December 1, 2024 |
| New SLR – [AWSServiceRoleForSecurityIncidentResponse_Triage](using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse_Triage "using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse_Triage") New managed policy – [AWSSecurityIncidentResponseTriageServiceRolePolicy](#AWSSecurityIncidentResponseTriageServiceRolePolicy "#AWSSecurityIncidentResponseTriageServiceRolePolicy") | New service linked role and attached policy allowing service access into your AWS Organizations accounts to perform triage of security events.                                                                                                                                                                                                                                                                                                                                                                                  | December 1, 2024 |
| New managed policy – [AWSSecurityIncidentResponseFullAccess](#AWSSecurityIncidentResponseFullAccess "#AWSSecurityIncidentResponseFullAccess")                                                                                                                                                                                                                                                                      | AWS Security Incident Response add a new SLR to attach to IAM principals for read and write actions for the service.                                                                                                                                                                                                                                                                                                                                                                                                            | December 1, 2024 |
| New managed policy role – [AWSSecurityIncidentResponseReadOnlyAccess](#AWSSecurityIncidentResponseReadOnlyAccess "#AWSSecurityIncidentResponseReadOnlyAccess")                                                                                                                                                                                                                                                     | AWS Security Incident Response add a new SLR to attach to IAM principals for read actions                                                                                                                                                                                                                                                                                                                                                                                                                                       | December 1, 2024 |
| New managed policy role – [AWSSecurityIncidentResponseCaseFullAccess](#AWSSecurityIncidentResponseCaseFullAccess "#AWSSecurityIncidentResponseCaseFullAccess")                                                                                                                                                                                                                                                     | AWS Security Incident Response add a new SLR to attach to IAM principals for read and write actions for service cases.                                                                                                                                                                                                                                                                                                                                                                                                          | December 1, 2024 |
| Started tracking changes.                                                                                                                                                                                                                                                                                                                                                                                          | Started tracking changes for AWS Security Incident Response SLRs and managed policies                                                                                                                                                                                                                                                                                                                                                                                                                                           | December 1, 2024 |
