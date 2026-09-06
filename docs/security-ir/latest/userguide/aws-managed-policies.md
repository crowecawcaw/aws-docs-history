

# AWS Managed Policies
<a name="aws-managed-policies"></a>

 An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles. 

 To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*. 

 AWS services maintain and update their associated AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions. 

 Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*. 

**Topics**
+ [AWS managed policy: AWSSecurityIncidentResponseServiceRolePolicy](#AWSSecurityIncidentResponseServiceRolePolicy)
+ [AWS managed policy: AWSSecurityIncidentResponseFullAccess](#AWSSecurityIncidentResponseFullAccess)
+ [AWS managed policy: AWSSecurityIncidentResponseReadOnlyAccess](#AWSSecurityIncidentResponseReadOnlyAccess)
+ [AWS managed policy: AWSSecurityIncidentResponseCaseFullAccess](#AWSSecurityIncidentResponseCaseFullAccess)
+ [AWS managed policy: AWSSecurityIncidentResponseTriageServiceRolePolicy](#AWSSecurityIncidentResponseTriageServiceRolePolicy)
+ [AWS Security Incident Response updates to SLRs and managed policies](#managed-policy-updates)

## AWS managed policy: AWSSecurityIncidentResponseServiceRolePolicy
<a name="AWSSecurityIncidentResponseServiceRolePolicy"></a>

AWS Security Incident Response uses the AWSSecurityIncidentResponseServiceRolePolicy AWS managed policy. This AWS managed policy is attached to the [AWSServiceRoleForSecurityIncidentResponse](using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse) service-linked role. The policy provides access for AWS Security Incident Response to identify accounts subscribed, create cases, update cases, create case comments, list cases, list case comments, and tag related resources.

**Important**  
 Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data 

* Permissions details *

 The service uses this policy to perform actions on the following resources:
+ *AWS Organizations:* Allows the service to lookup membership accounts for use with the service.
+ *CreateCase:* Allows the service create service cases on behalf of membership accounts.
+ *ListCases:* Allows the service’s AI agent to view cases for the purposes of security investigation.
+ *UpdateCase:* Allows the service’s AI agent to update case metadata.
+ *CreateCaseComment:* Allows the service’s AI agent to post its results as a case comment.
+ *ListComments:* Allows the service’s AI agent to view case comments needed to perform automated investigations.
+ *TagResource:* Allows the service tag resources configured as part of the service.

You can view the permissions associated with this policy in AWS managed policies for [ AWSSecurityIncidentResponseServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSecurityIncidentResponseServiceRolePolicy.html).

## AWS managed policy: AWSSecurityIncidentResponseFullAccess
<a name="AWSSecurityIncidentResponseFullAccess"></a>

AWS Security Incident Response uses the AWSSecurityIncidentResponseAdmin AWS managed policy. This policy grants full access to service resources and access to related AWS services. You can use this policy with your IAM principals to quickly add permissions for AWS Security Incident Response.

**Important**  
 Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data 

* Permissions details *

 The service uses this policy to perform actions on the following resources:
+ *IAM principal read-only access:* Grants a service user the ability to perform read-only actions against existing AWS Security Incident Response resources.
+ *IAM principal write access:* Grants a service user the ability to update, modify, delete, and create AWS Security Incident Response resources.

You can view the permissions associated with this policy in AWS managed policies for [ AWSSecurityIncidentResponseFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSecurityIncidentResponseFullAccess.html).

## AWS managed policy: AWSSecurityIncidentResponseReadOnlyAccess
<a name="AWSSecurityIncidentResponseReadOnlyAccess"></a>

AWS Security Incident Response uses the AWSSecurityIncidentResponseReadOnlyAccess AWS managed policy. The policy grants read-only access to service case resources. You can use this policy with your IAM principals to quickly add permissions for AWS Security Incident Response.

**Important**  
 Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data 

* Permissions details *

 The service uses this policy to perform actions on the following resources:
+ *IAM principal read-only access:* Grants a service user the ability to perform read-only actions against existing AWS Security Incident Response resources.

You can view the permissions associated with this policy in AWS managed policies for [ AWSSecurityIncidentResponseReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSecurityIncidentResponseReadOnlyAccess.html).

## AWS managed policy: AWSSecurityIncidentResponseCaseFullAccess
<a name="AWSSecurityIncidentResponseCaseFullAccess"></a>

AWS Security Incident Response uses the AWSSecurityIncidentResponseCaseFullAccess AWS managed policy. The policy grants full access to service case resources. You can use this policy with your IAM principals to quickly add permissions for AWS Security Incident Response.

**Important**  
 Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data 

* Permissions details *

 The service uses this policy to perform actions on the following resources:
+ *IAM principal case read-only access:* Grants a service user the ability to perform read-only actions against existing AWS Security Incident Response cases.
+ *IAM principal case write access:* Grants a service user the ability to update, modify, delete, and create AWS Security Incident Response cases.

You can view the permissions associated with this policy in AWS managed policies for [ AWSSecurityIncidentResponseCaseFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSecurityIncidentResponseCaseFullAccess.html).

## AWS managed policy: AWSSecurityIncidentResponseTriageServiceRolePolicy
<a name="AWSSecurityIncidentResponseTriageServiceRolePolicy"></a>

AWS Security Incident Response uses the AWSSecurityIncidentResponseTriageServiceRolePolicy AWS managed policy. This AWS managed policy is attached to the [AWSServiceRoleForSecurityIncidentResponse\_Triage ](using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse_Triage) service-linked role.

The policy provides access to AWS Security Incident Response to continuously monitor your environment for security threats, tune security services to reduce alert noise, and gather information to investigate potential incidents. You can't attach this policy to your IAM entities.

**Important**  
 Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. AWS Security Incident Response uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data 

* Permissions details *

 The service uses this policy to perform actions on the following resources:
+ *Events:* Allows the service to create an Amazon EventBridge managed rule. This rule is the infrastructure required in your AWS account to deliver events from your account to the service. This action is performed on any AWS resource managed by `triage.security-ir.amazonaws.com`.
+ *Amazon GuardDuty:* Allows the service to tune security services to reduce alert noise, gather information to investigate potential incidents, and initiate GuardDuty malware scans.
+ *AWS Security Hub CSPM:* Allows the service to list enabled standards and product integrations, list organization members and admin accounts, and tune security services to reduce alert noise and gather information to investigate potential incidents.
+ *AWS Identity and Access Management:* Allows the service to retrieve role information for the `AWSServiceRoleForAmazonGuardDutyMalwareProtection` service-linked role to verify whether GuardDuty MalwareProtection is configured.
+ *AWS Security Incident Response:* Allows the service to create and update cases and tag resources, restricted to resources tagged with `SecurityIncidentResponseManaged=true`. Allows the service to read membership information (GetMembership, ListMemberships).

You can view the permissions associated with this policy in AWS managed policies for [ AWSSecurityIncidentResponseTriageServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSecurityIncidentResponseTriageServiceRolePolicy.html).

## AWS Security Incident Response updates to SLRs and managed policies
<a name="managed-policy-updates"></a>

View details about updates to AWS Security Incident Response SLRs and managed policies roles since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| Updated – [`AWSSecurityIncidentResponseReadOnlyAccess`](#AWSSecurityIncidentResponseReadOnlyAccess) | The policy now includes the `security-ir:ListInvestigations` action. | April 22, 2026 | 
| Updated – [`AWSSecurityIncidentResponseFullAccess`](#AWSSecurityIncidentResponseFullAccess) | The policy now uses `security-ir:*` instead of listing explicit `security-ir` actions. Eight new AWS Organizations permissions were added (`organizations:ListAWSServiceAccessForOrganization`, `organizations:ListRoots`, `organizations:ListOrganizationalUnitsForParent`, `organizations:ListAccountsForParent`, `organizations:ListChildren`, `organizations:DescribeOrganizationalUnit`, `organizations:ListAccounts`, and `organizations:DescribeAccount`) to support the console's account picker when updating associations. The MFA condition has been removed. | April 22,2026 | 
| Updated – [`AWSSecurityIncidentResponseCaseFullAccess`](#AWSSecurityIncidentResponseCaseFullAccess) | The policy now includes two new actions: `security-ir:ListInvestigations` and `security-ir:SendFeedback`. The MFA condition has been removed. | April 22, 2026 | 
| Updated – [`AWSSecurityIncidentResponseTriageServiceRolePolicy`](#AWSSecurityIncidentResponseTriageServiceRolePolicy) | The policy now allows the service to modify GuardDuty filters that are tagged with `SecurityIncidentResponseManaged=true`, to update detector configurations, and to initiate GuardDuty malware scans. It allows the service to create and manage rules that automatically act on Security Hub CSPM findings, and to understand organizational structure. | March 27, 2026 | 
| Updated – [AWSSecurityIncidentResponseServiceRolePolicy](#AWSSecurityIncidentResponseServiceRolePolicy) | The policy now performs actions on the following resources: <br />ListCases: Allows the service’s AI agent to view cases for the purposes of security investigation<br />UpdateCase: Allows the service’s AI agent to update case metadata.<br />CreateCaseComment: Allows the service’s AI agent to post its results as a case comment<br />ListComments: Allows the service’s AI agent to view case comments needed to perform automated investigations | November 2025 | 
| Updated – [AWSSecurityIncidentResponseServiceRolePolicy](#AWSSecurityIncidentResponseServiceRolePolicy) | The policy now includes two new actions for `"organizations:DescribeAccount"`, `"organizations:ListDelegatedAdministrators"` and a new condition:<pre><br /><br />"Condition": {<br />      "StringEquals": {<br />        "aws:ResourceAccount": "${aws:PrincipalAccount}"<br />      }<br />    }<br />                </pre> | November 2025 | 
| Updates to SLR adding permissions to support service entitlements. | [AWSSecurityIncidentResponseTriageServiceRolePolicy](#AWSSecurityIncidentResponseTriageServiceRolePolicy) has been updated to add security-ir:GetMembership, security-ir:ListMemberships, security-ir:UpdateCase, guardduty:ListFilters, guarduty:UpdateFilter, guardduty:DeleteFilter, and guardduty:GetAdministratorAccount permissions. guardduty:GetAdministratorAccount was added to facilitate management of GuardDuty Auto-Archival filters in delegated accounts. | June 02, 2025 | 
| New SLR – [AWSServiceRoleForSecurityIncidentResponse](using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse)<br />New managed policy – [AWSSecurityIncidentResponseServiceRolePolicy](#AWSSecurityIncidentResponseServiceRolePolicy). | New service linked role and attached policy allowing service access into your AWS Organizations accounts to identify membership. | December 1, 2024 | 
| New SLR – [AWSServiceRoleForSecurityIncidentResponse\_Triage](using-service-linked-roles.md#AWSServiceRoleForSecurityIncidentResponse_Triage)<br />New managed policy – [AWSSecurityIncidentResponseTriageServiceRolePolicy](#AWSSecurityIncidentResponseTriageServiceRolePolicy) | New service linked role and attached policy allowing service access into your AWS Organizations accounts to perform triage of security events. | December 1, 2024 | 
| New managed policy – [AWSSecurityIncidentResponseFullAccess](#AWSSecurityIncidentResponseFullAccess) | AWS Security Incident Response add a new SLR to attach to IAM principals for read and write actions for the service. | December 1, 2024 | 
| New managed policy role – [AWSSecurityIncidentResponseReadOnlyAccess](#AWSSecurityIncidentResponseReadOnlyAccess) | AWS Security Incident Response add a new SLR to attach to IAM principals for read actions | December 1, 2024 | 
| New managed policy role – [AWSSecurityIncidentResponseCaseFullAccess](#AWSSecurityIncidentResponseCaseFullAccess) | AWS Security Incident Response add a new SLR to attach to IAM principals for read and write actions for service cases. | December 1, 2024 | 
| Started tracking changes. | Started tracking changes for AWS Security Incident Response SLRs and managed policies | December 1, 2024 | 