

# AWS Identity and Access Management (IAM)
<a name="aws-identity-and-access-management-iam"></a>

This guide provides security configuration requirements and implementation examples for AWS Identity and Access Management (IAM) in accordance with FedRAMP requirements.

## Document Information
<a name="aws_identity_and_access_management_iam_document_information"></a>


|  |  | 
| --- |--- |
| Version | 1.0.0 | 
| Last Updated | 2026-09-02 | 
| Documentation URL | https://docs.aws.amazon.com/IAM/latest/UserGuide/ | 

## Overview
<a name="aws_identity_and_access_management_iam_overview"></a>

AWS Identity and Access Management (IAM) security configuration involves implementing comprehensive controls for identities, credentials, and permissions to meet FedRAMP compliance requirements. This guidance covers the AWS account root user (the top-level administrative account) and IAM administrative principals, the security-related settings restricted to them, and privileged access controls for IAM operations.

 **Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

 **Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements
<a name="aws_identity_and_access_management_iam_fedramp_requirements"></a>

AWS Identity and Access Management (IAM) must comply with the following FedRAMP requirements:
+ SCG-CSO-RSC
+ SCG-CSO-SDF
+ SCG-ENH-CMP
+ SCG-ENH-EXP
+ SCG-ENH-API

## Administrative Account Model
<a name="aws_identity_and_access_management_iam_administrative_account_model"></a>

AWS Identity and Access Management (IAM) has an administrative account model.


|  |  | 
| --- |--- |
| Administrative Accounts | Yes | 
| Account Type | AWS account root user and IAM administrative principals | 

## SCG-CSO-RSC: Recommended Secure Configuration
<a name="aws_identity_and_access_management_iam_scg_cso_rsc_recommended_secure_configuration"></a>

 **Applicable:** Yes

This requirement consolidates guidance for: 1. Instructions on how to securely access, configure, operate, and decommission top-level administrative accounts 2. Explanations of security-related settings that can be operated only by top-level administrative accounts 3. Explanations of security-related settings that can be operated only by privileged accounts

### Part 1: Administrative Accounts
<a name="aws_identity_and_access_management_iam_part_1_administrative_accounts"></a>

 **Applicable:** Yes

 **Implementation Overview:** In AWS IAM the top-level administrative account is the AWS account **root user**, which has complete access to all resources in the account. Day-to-day administration is performed by IAM administrative principals (users and roles) granted elevated permissions. This guidance covers securing these accounts across their lifecycle: access, configuration, operation, and decommissioning.

### Root User Security
<a name="aws_identity_and_access_management_iam_root_user_security"></a>

 **Root User Configuration:** 
+ Enable MFA on the root user (a hardware or virtual MFA device); prefer a hardware device stored securely
+ Do not create or retain root user access keys; if any exist, delete them
+ Use a strong, unique root user password stored in a managed secrets store
+ Set correct account alternate contacts (security, billing, operations)
+ Use the root user only for the few tasks that require it, and never for routine operations

 **Accessing the Root User:** 
+ Restrict who can access root credentials; treat root access as a break-glass procedure with approval and logging
+ For organizations, use AWS Organizations centralized root access management to remove or reduce standalone member-account root credentials where supported

### IAM Administrative Principal Security
<a name="aws_identity_and_access_management_iam_iam_administrative_principal_security"></a>
+ Grant administrative access through IAM roles assumed with MFA, not long-lived users where possible
+ Apply least privilege: scope administrative policies to only the actions and resources required
+ Require MFA for privileged actions using the `aws:MultiFactorAuthPresent` condition key
+ Use permissions boundaries and Service Control Policies (SCPs) to bound maximum permissions
+ Rotate credentials regularly and remove unused users, roles, and access keys

### Monitoring and Auditing
<a name="aws_identity_and_access_management_iam_monitoring_and_auditing"></a>
+ Enable AWS CloudTrail for all IAM API activity and review administrative actions
+ Use IAM Access Analyzer to detect external/unintended access and validate policies
+ Generate and review IAM credential reports and use last-accessed information to remove unused access
+ Configure CloudWatch alarms for sensitive IAM events (for example, root user usage, policy changes)

### Decommissioning Administrative Accounts
<a name="aws_identity_and_access_management_iam_decommissioning_administrative_accounts"></a>
+ Remove IAM users, roles, and access keys when no longer required, following access reviews
+ Revoke active sessions for roles when offboarding by rotating/removing credentials and updating trust policies
+ When closing an AWS account, follow the account closure process and ensure dependent access is removed

### FedRAMP Controls Addressed
<a name="aws_identity_and_access_management_iam_fedramp_controls_addressed"></a>
+ AC-2: Account Management
+ AC-3: Access Enforcement
+ AC-6: Least Privilege
+ IA-2: Identification and Authentication
+ IA-5: Authenticator Management
+ AU-2: Audit Events

### Implementation Checklist
<a name="aws_identity_and_access_management_iam_implementation_checklist"></a>

☐ Enable MFA on the root user and remove root access keys ☐ Set account alternate contacts ☐ Administer via least-privilege IAM roles with MFA ☐ Apply permissions boundaries and SCPs ☐ Enable CloudTrail and review IAM activity ☐ Use IAM Access Analyzer and credential reports ☐ Remove unused users, roles, and access keys ☐ Document administrative procedures and conduct regular access reviews

This guidance helps ensure that AWS IAM administrative accounts are configured according to security best practices and FedRAMP requirements.

### Part 2: Administrative Settings
<a name="aws_identity_and_access_management_iam_part_2_administrative_settings"></a>

 **Applicable:** Yes

### Security-Related Settings Restricted to the Root User
<a name="aws_identity_and_access_management_iam_security_related_settings_restricted_to_the_root_user"></a>

The AWS account root user can perform certain actions that no other principal can. The following operations and their security implications are restricted to the root user.

#### 1. Account-Level Settings
<a name="aws_identity_and_access_management_iam_1_account_level_settings"></a>

 **Operations:** 
+ Change the account root user email address and root password (standalone accounts)

 **Security Implications:** 
+ Control of these settings equates to control of the account
+ Compromise enables account takeover and recovery-path abuse

**Note**  
Other account settings — such as the account name, alternate contacts, and enabling or disabling AWS Regions — do not require root user credentials and can be managed by authorized IAM principals with the appropriate permissions.

#### 2. Root Credentials and MFA
<a name="aws_identity_and_access_management_iam_2_root_credentials_and_mfa"></a>

 **Operations:** 
+ Manage root user password, MFA device, and (legacy) root access keys

 **Security Implications:** 
+ Root MFA is the primary defense against account takeover
+ Root access keys, if present, are high-risk long-lived credentials

#### 3. Account Closure
<a name="aws_identity_and_access_management_iam_3_account_closure"></a>

 **Operations:** 
+ Close the AWS account (standalone accounts)

 **Security Implications:** 
+ Account closure is destructive and affects all resources

#### 4. Specific Root-Only Tasks
<a name="aws_identity_and_access_management_iam_4_specific_root_only_tasks"></a>

 **Operations:** 
+ A limited set of tasks documented by AWS as requiring the root user (for example, certain S3 or billing operations)

 **Security Implications:** 
+ These tasks require break-glass root access and must be tightly controlled and logged

### Part 3: Privileged Settings
<a name="aws_identity_and_access_management_iam_part_3_privileged_settings"></a>

 **Applicable:** Yes

Privileged access in IAM is controlled through IAM policies granted to users and roles. This section provides example IAM policies for varying levels of access to IAM itself. Because IAM permissions govern access to the entire account, privileged IAM access must be tightly scoped and require MFA.

## IAM Least Privilege Policies
<a name="aws_identity_and_access_management_iam_iam_least_privilege_policies"></a>

This section provides sample IAM policies for implementing least privilege access to IAM operations across different operational roles.

### Policy Selection Guide
<a name="aws_identity_and_access_management_iam_policy_selection_guide"></a>

Choose the appropriate policy based on your role:


| Policy | Use Case | MFA Required | 
| --- | --- | --- | 
| Read-Only Access | Auditors, compliance reviewers, monitoring dashboards | No | 
| Operator Access | Operators managing users, groups, and policies | Yes | 
| Administrator Access | IAM administrators with full management access | Yes (1-hour max) | 

### Read-Only Access Policy
<a name="aws_identity_and_access_management_iam_read_only_access_policy"></a>

 **Use this for:** Auditors, compliance reviewers, monitoring dashboards

 **Grants access to:** 
+ View IAM users, roles, groups, and policies
+ Generate and read credential and access reports

 **Does NOT grant:** 
+ Create, modify, or delete IAM resources
+ Change policies or credentials

 **Testing this policy:** 

```
# Verify read access works
aws iam list-users
aws iam get-account-authorization-details

# Verify write access is denied (should fail)
aws iam create-user --user-name test-user
```

 **Policy JSON:** 

 **Purpose:** Provides read-only access to IAM for monitoring and auditing purposes.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:Get*",
        "iam:List*",
        "iam:GenerateCredentialReport",
        "iam:GenerateServiceLastAccessedDetails"
      ],
      "Resource": "*"
    }
  ]
}
```

### Operator Access Policy
<a name="aws_identity_and_access_management_iam_operator_access_policy"></a>

 **Use this for:** Operators managing users, groups, and policies

 **Grants access to:** 
+ All read-only permissions
+ Create users (only with a required permissions boundary), and tag users
+ Attach/detach only an approved set of policies
+ Add/remove users to/from an approved set of non-administrative groups

 **Does NOT grant:** 
+ Delete roles or manage account-level settings
+ Create arbitrary groups, or add users to administrative groups
+ Attach administrative policies (for example, `AdministratorAccess`)
+ Modify SCPs or permissions boundaries without additional controls

 **Testing this policy:** 

```
# Verify operator access works (requires MFA)
aws iam add-user-to-group --user-name alice --group-name Developers

# Verify admin access is denied (should fail)
aws iam delete-role --role-name SomeAdminRole
```

 **Policy JSON:** 

 **Purpose:** Provides operational access for routine identity management tasks with MFA. To preserve least privilege and prevent self-escalation, the operator can create users only with a required permissions boundary attached; can attach or detach only an approved set of policies; and can manage group membership only for an explicit list of approved (non-administrative) group ARNs. Because both the attachable policies and the assignable groups are restricted to safe, pre-approved sets, the operator cannot grant administrative access (for example, `AdministratorAccess`) to any user, including themselves. Replace `123456789012`, the policy names, and the group names with values for your account, and ensure the approved groups do not carry administrative permissions.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "ReadTagAndUserManagement",
      "Effect": "Allow",
      "Action": [
        "iam:Get*",
        "iam:List*",
        "iam:TagUser",
        "iam:UntagUser"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    },
    {
      "Sid": "ManageMembershipOfApprovedGroupsOnly",
      "Effect": "Allow",
      "Action": [
        "iam:AddUserToGroup",
        "iam:RemoveUserFromGroup"
      ],
      "Resource": [
        "arn:aws:iam::123456789012:group/Developers",
        "arn:aws:iam::123456789012:group/ReadOnly"
      ],
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    },
    {
      "Sid": "CreateUsersOnlyWithPermissionsBoundary",
      "Effect": "Allow",
      "Action": "iam:CreateUser",
      "Resource": "*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        },
        "StringEquals": {
          "iam:PermissionsBoundary": "arn:aws:iam::123456789012:policy/OperatorManagedBoundary"
        }
      }
    },
    {
      "Sid": "AttachOnlyApprovedPolicies",
      "Effect": "Allow",
      "Action": [
        "iam:AttachUserPolicy",
        "iam:DetachUserPolicy"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        },
        "ArnEquals": {
          "iam:PolicyARN": [
            "arn:aws:iam::123456789012:policy/DeveloperBaseline",
            "arn:aws:iam::aws:policy/job-function/ViewOnlyAccess"
          ]
        }
      }
    }
  ]
}
```

### Administrator Access Policy
<a name="aws_identity_and_access_management_iam_administrator_access_policy"></a>

 **Use this for:** IAM administrators with full management access

 **Grants access to:** 
+ All operator permissions
+ Full management of IAM users, roles, policies, and credentials

 **Requires:** 
+ MFA with maximum 1-hour session duration

 **Testing this policy:** 

```
# Verify full admin access works (requires MFA)
aws iam create-role --role-name NewAdminRole --assume-role-policy-document file://trust.json
aws iam delete-user --user-name old-user
```

 **Policy JSON:** 

 **Purpose:** Provides full IAM administrative access with MFA and session time restrictions.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iam:*",
      "Resource": "*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        },
        "NumericLessThan": {
          "aws:MultiFactorAuthAge": "3600"
        }
      }
    }
  ]
}
```

### Implementation Guidance
<a name="aws_identity_and_access_management_iam_implementation_guidance"></a>

 **Role-Based Access Control:** 
+ Create separate IAM roles for viewers, operators, and administrators
+ Always require MFA for privileged IAM operations and administrative access
+ Use time-based conditions to limit session duration for administrative roles
+ Apply permissions boundaries to cap the maximum permissions of IAM principals
+ Regularly review and audit policy assignments and usage patterns
+ Use AWS IAM Access Analyzer to validate least privilege implementations

 **Security Best Practices:** 
+ Start with read-only access and incrementally add permissions as needed
+ Use AWS managed policies as a baseline when available and appropriate
+ Monitor policy usage with CloudTrail and Access Analyzer
+ Document business justification for each permission granted

## SCG-CSO-SDF: Secure Defaults
<a name="aws_identity_and_access_management_iam_scg_cso_sdf_secure_defaults"></a>

 **Applicable:** Yes

AWS services are designed with security in mind. IAM is deny-by-default: newly created IAM principals have no permissions until explicitly granted. However, AWS allows customers to define the security configuration of their identities and does not enforce a minimum security standard (such as mandatory MFA) by default, enabling customers the flexibility to meet their specific business requirements and compliance needs.

AWS IAM should be configured using the above AWS Security Best Practice recommendations. AWS allows customers to define the security of their identities, and does not enforce a minimum security standard by default.

### Implementation Guidelines
<a name="aws_identity_and_access_management_iam_implementation_guidelines"></a>

Ensure IAM is configured with security-first defaults that align with AWS security best practices and organizational compliance requirements.

 **Security Configuration Best Practices:** 
+ Enable MFA on the root user and on all IAM principals with console access
+ Remove root access keys and avoid long-lived user access keys
+ Enforce least privilege with scoped policies, permissions boundaries, and SCPs
+ Enable CloudTrail and IAM Access Analyzer
+ Set an account password policy meeting your organization’s requirements
+ Regularly review credential reports and remove unused access

## SCG-ENH-CMP: Configuration Comparison
<a name="aws_identity_and_access_management_iam_scg_enh_cmp_configuration_comparison"></a>

 **Applicable:** Yes

 **Implementation Overview:** Use AWS Config, IAM Access Analyzer, credential reports, and IAM API queries to compare current IAM configuration against established FedRAMP baselines.

### Configuration Monitoring
<a name="aws_identity_and_access_management_iam_configuration_monitoring"></a>

```
# Generate and retrieve the IAM credential report for baseline comparison
aws iam generate-credential-report
aws iam get-credential-report --query 'Content' --output text | base64 --decode > credential-report.csv

# Export full account authorization details for comparison
aws iam get-account-authorization-details --output json > iam-authz-details.json
```

### Automation Framework
<a name="aws_identity_and_access_management_iam_automation_framework"></a>
+ Use AWS Config managed rules (for example, iam-user-mfa-enabled, iam-root-access-key-check) to evaluate IAM posture
+ Use IAM Access Analyzer to identify external access and validate policies
+ Integrate with AWS Security Hub for centralized compliance reporting

## SCG-ENH-EXP: Configuration Export
<a name="aws_identity_and_access_management_iam_scg_enh_exp_configuration_export"></a>

 **Applicable:** Yes

 **Implementation Overview:** Export IAM configuration using AWS CLI commands in machine-readable JSON/CSV format for backup, audit, and compliance documentation.

### Export Procedures
<a name="aws_identity_and_access_management_iam_export_procedures"></a>

 **Export Format:** JSON / CSV via AWS CLI

 **Primary Export Commands:** 

```
# Export IAM identities, policies, and credential posture
aws iam get-account-authorization-details --output json > iam-authz-details.json
aws iam get-account-summary --output json > iam-account-summary.json
aws iam generate-credential-report
aws iam get-credential-report --query 'Content' --output text | base64 --decode > credential-report.csv
```

 **Configuration Export Use Cases:** 
+ Backup current identity and permission state
+ Compare configurations across environments
+ Audit and compliance reporting requirements
+ Disaster recovery planning and documentation

## SCG-ENH-API: API Configuration
<a name="aws_identity_and_access_management_iam_scg_enh_api_api_configuration"></a>

 **Applicable:** Yes

 **Implementation Overview:** IAM security configurations are manageable through AWS APIs, CLI commands, and Infrastructure as Code tools, enabling automated and repeatable security implementations.

### Account Password Policy
<a name="aws_identity_and_access_management_iam_account_password_policy"></a>

 **API Command:** 

```
# Set an account password policy
aws iam update-account-password-policy \
  --minimum-password-length 14 \
  --require-symbols --require-numbers \
  --require-uppercase-characters --require-lowercase-characters \
  --max-password-age 90 --password-reuse-prevention 24
```

 **Control Mapping:** IA-5 (Authenticator Management)

### Access Analyzer
<a name="aws_identity_and_access_management_iam_access_analyzer"></a>

 **API Command:** 

```
# Create an IAM Access Analyzer to detect external access
aws accessanalyzer create-analyzer --analyzer-name org-analyzer --type ACCOUNT
```

 **Control Mapping:** AC-6 (Least Privilege)

## Additional Resources
<a name="aws_identity_and_access_management_iam_additional_resources"></a>

For more information about AWS security best practices, see the following resources:

 ** AWS Security Documentation:** 
+  [AWS Security Documentation](https://docs.aws.amazon.com/security/) - Comprehensive security guidance across all AWS services
+  [AWS FedRAMP Compliance](https://docs.aws.amazon.com/compliance/fedramp/) - FedRAMP-specific compliance information and resources
+  [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Security design principles and best practices

 **AWS IAM-Specific Resources:** 
+  [IAM Security Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) - Service-specific security recommendations
+  [AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) - Root user security guidance
+  [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) - Detecting external access and validating policies

 **Compliance and Governance:** 
+  [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) - Automated compliance monitoring and evaluation
+  [AWS CloudTrail User Guide](https://docs.aws.amazon.com/cloudtrail/latest/userguide/cloudtrail-user-guide.html) - API logging and audit trail management