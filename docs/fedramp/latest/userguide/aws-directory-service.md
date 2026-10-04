

# AWS Directory Service
<a name="aws-directory-service"></a>

This guide provides security configuration requirements and implementation examples for AWS Directory Service in accordance with FedRAMP requirements.

## Document Information
<a name="aws_directory_service_document_information"></a>


|  |  | 
| --- |--- |
| Version | 1.0.0 | 
| Last Updated | 2026-09-02 | 
| Documentation URL | https://docs.aws.amazon.com/directoryservice/ | 

## Overview
<a name="aws_directory_service_overview"></a>

AWS Directory Service security configuration involves implementing comprehensive security controls including encryption, access management, logging, and monitoring to meet FedRAMP compliance requirements. This guidance covers the directory administrative account (the **Admin** account for AWS Managed Microsoft AD and the **Administrator** account for Simple AD), the security-related settings restricted to that account, and privileged access controls for directory operations.

 **Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

 **Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements
<a name="aws_directory_service_fedramp_requirements"></a>

AWS Directory Service must comply with the following FedRAMP requirements:
+ SCG-CSO-RSC
+ SCG-CSO-SDF
+ SCG-ENH-CMP
+ SCG-ENH-EXP
+ SCG-ENH-API

## Administrative Account Model
<a name="aws_directory_service_administrative_account_model"></a>

AWS Directory Service has an administrative account model.


|  |  | 
| --- |--- |
| Administrative Accounts | Yes | 
| Account Type | Directory administrative account (the `Admin` account for AWS Managed Microsoft AD; the `Administrator` account for Simple AD) | 

## SCG-CSO-RSC: Recommended Secure Configuration
<a name="aws_directory_service_scg_cso_rsc_recommended_secure_configuration"></a>

 **Applicable:** Yes

This requirement consolidates guidance for: 1. Instructions on how to securely access, configure, operate, and decommission top-level administrative accounts 2. Explanations of security-related settings that can be operated only by top-level administrative accounts 3. Explanations of security-related settings that can be operated only by privileged accounts

### Part 1: Administrative Accounts
<a name="aws_directory_service_part_1_administrative_accounts"></a>

 **Applicable:** Yes

 **Implementation Overview:** AWS Directory Service provides a directory administrative account — the **Admin** account for AWS Managed Microsoft AD and the **Administrator** account for Simple AD. This account has elevated privileges within the directory and is distinct from AWS IAM identities that manage the directory service through the `ds` API. This guidance covers securing the directory Admin account across its lifecycle: access, configuration, operation, and decommissioning.

### Admin Account Security
<a name="aws_directory_service_admin_account_security"></a>

 **Admin Account Configuration:** 
+ Set a strong, randomly generated password for the Admin account at directory creation and store it in a managed secrets store (for example, AWS Secrets Manager)
+ Configure a strong domain password policy for Managed Microsoft AD (complexity, minimum length, rotation, lockout thresholds) from a domain-joined management instance
+ Restrict membership of privileged directory groups (for example, AWS Delegated Administrators) to the minimum required
+ Rotate the Admin password on a regular schedule and after any personnel change

 **Authentication Methods:** 
+ For AWS Managed Microsoft AD and AD Connector, enable multi-factor authentication for directory users via RADIUS integration (`aws ds enable-radius`). Simple AD does not support RADIUS-based MFA.
+ Enforce MFA for IAM principals that manage the directory service
+ Use LDAPS to protect directory authentication traffic. For AWS Managed Microsoft AD, enable server-side LDAPS by installing a certificate from a domain-joined Microsoft enterprise CA on the domain controllers. For Simple AD, LDAPS requires a Network Load Balancer-based configuration rather than an API setting.

 **Configuring the Admin Account:** 

```
# Enable RADIUS-based MFA for the directory (requires a reachable RADIUS server)
aws ds enable-radius \
  --directory-id d-0123456789 \
  --radius-settings RadiusServers=10.0.1.100,RadiusPort=1812,RadiusTimeout=5,RadiusRetries=3,SharedSecret=<shared-secret>,AuthenticationProtocol=PAP,DisplayLabel=MFA,UseSameUsername=true

# Verify directory and RADIUS status
aws ds describe-directories --directory-ids d-0123456789 \
  --query 'DirectoryDescriptions[0].{Stage:Stage,RadiusStatus:RadiusStatus}'
```

### Access and Network Security
<a name="aws_directory_service_access_and_network_security"></a>
+ Deploy directories into private subnets across multiple Availability Zones using dedicated VPC settings
+ Use VPC security groups to restrict directory traffic to authorized instances only
+ For AWS Managed Microsoft AD, enable client-side LDAPS (`aws ds enable-ldaps --type Client`) to encrypt LDAP communications between AWS applications and your self-managed AD; enable server-side LDAPS (protecting the directory’s own inbound LDAP traffic) by installing a certificate on the domain controllers
+ Use conditional forwarders with trusted DNS servers for secure name resolution

### Monitoring and Auditing
<a name="aws_directory_service_monitoring_and_auditing"></a>
+ Enable directory log forwarding to Amazon CloudWatch Logs (`aws ds create-log-subscription`)
+ Enable AWS CloudTrail for all Directory Service (`ds`) API calls
+ Monitor for anomalous authentication and administrative activity
+ Set log retention appropriate to your compliance requirements

### Decommissioning Administrative Accounts
<a name="aws_directory_service_decommissioning_administrative_accounts"></a>
+ Remove trust relationships and conditional forwarders that are no longer required
+ Delete the directory via the Directory Service API when it is retired, after confirming no dependent workloads remain
+ Rotate or revoke any service-account credentials (for example, AD Connector service accounts) after decommissioning

### FedRAMP Controls Addressed
<a name="aws_directory_service_fedramp_controls_addressed"></a>
+ AC-2: Account Management
+ AC-6: Least Privilege
+ IA-2: Identification and Authentication
+ IA-5: Authenticator Management
+ AU-2: Audit Events
+ SC-8: Transmission Confidentiality and Integrity

### Implementation Checklist
<a name="aws_directory_service_implementation_checklist"></a>

☐ Set and securely store a strong Admin account password ☐ Configure a strong domain password policy ☐ Enable MFA (RADIUS) for directory users and for IAM principals managing the directory ☐ Enable LDAPS for encrypted LDAP communications ☐ Deploy in private subnets with restrictive security groups ☐ Enable directory logging to CloudWatch Logs and CloudTrail ☐ Restrict privileged directory group membership ☐ Document administrative procedures and conduct regular access reviews

This guidance helps ensure that AWS Directory Service administrative accounts are configured according to security best practices and FedRAMP requirements.

### Part 2: Administrative Settings
<a name="aws_directory_service_part_2_administrative_settings"></a>

 **Applicable:** Yes

### Security-Related Settings Restricted to the Admin Account
<a name="aws_directory_service_security_related_settings_restricted_to_the_admin_account"></a>

The directory Admin account has elevated privileges. The following operations and their security implications are restricted to the Admin account (or delegated administrators).

#### 1. Domain User and Group Management
<a name="aws_directory_service_1_domain_user_and_group_management"></a>

 **Operations:** 
+ Create, modify, and delete domain users and groups
+ Manage membership of privileged/delegated administrator groups

 **Security Implications:** 
+ Controls who can authenticate to and administer the directory
+ Improper group membership can grant unintended elevated access

#### 2. Domain Password and Lockout Policy
<a name="aws_directory_service_2_domain_password_and_lockout_policy"></a>

 **Operations:** 
+ Configure domain password complexity, length, age, history, and lockout policies

 **Security Implications:** 
+ Weak policies undermine authentication strength across all directory users
+ Lockout settings affect resistance to brute-force attacks

#### 3. Trust Relationships and Conditional Forwarders
<a name="aws_directory_service_3_trust_relationships_and_conditional_forwarders"></a>

 **Operations:** 
+ Create and manage trust relationships and conditional forwarders

 **Security Implications:** 
+ Trusts extend the directory’s authentication boundary to other domains
+ Misconfigured DNS forwarding can enable spoofing or resolution failures

#### 4. LDAPS and Encryption Settings
<a name="aws_directory_service_4_ldaps_and_encryption_settings"></a>

 **Operations:** 
+ Enable/disable LDAPS; manage certificates for secure LDAP

 **Security Implications:** 
+ Disabling LDAPS exposes authentication traffic
+ Certificate mismanagement can break secure communication

#### 5. Logging and Monitoring Configuration
<a name="aws_directory_service_5_logging_and_monitoring_configuration"></a>

 **Operations:** 
+ Enable/disable directory log forwarding to CloudWatch Logs

 **Security Implications:** 
+ Disabling logging could conceal malicious or unauthorized activity
+ Audit records are critical for forensics and FedRAMP continuous monitoring

### Part 3: Privileged Settings
<a name="aws_directory_service_part_3_privileged_settings"></a>

 **Applicable:** Yes

Within AWS Directory Service there are two layers of privileged access. One layer is at the AWS IAM layer, where you control which principals can manage the directory service (create, configure, delete directories) via the `ds` API. This section covers those privileged settings and provides example IAM policies for varying levels of access. The second layer is inside the directory itself (the Admin account and delegated administrators), covered in the sections above.

## IAM Least Privilege Policies
<a name="aws_directory_service_iam_least_privilege_policies"></a>

This section provides sample IAM policies for implementing least privilege access to AWS Directory Service operations across different operational roles.

### Policy Selection Guide
<a name="aws_directory_service_policy_selection_guide"></a>

Choose the appropriate policy based on your role:


| Policy | Use Case | MFA Required | 
| --- | --- | --- | 
| Read-Only Access | Auditors, compliance reviewers, monitoring dashboards | No | 
| Operator Access | Operators managing directory resources | Yes | 
| Administrator Access | Service administrators with full management access | Yes (1-hour max) | 

### Read-Only Access Policy
<a name="aws_directory_service_read_only_access_policy"></a>

 **Use this for:** Auditors, compliance reviewers, monitoring dashboards

 **Grants access to:** 
+ View directory configurations and status
+ List directories, trusts, and settings

 **Does NOT grant:** 
+ Create, modify, or delete directories
+ Change security configurations

 **Testing this policy:** 

```
# Verify read access works
aws ds describe-directories --output json

# Verify write access is denied (should fail)
aws ds create-microsoft-ad --name corp.example.com --password <pw> --vpc-settings VpcId=vpc-123,SubnetIds=subnet-1,subnet-2
```

 **Policy JSON:** 

 **Purpose:** Provides read-only access to Directory Service resources for monitoring and auditing purposes.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ds:Describe*",
        "ds:List*",
        "ds:Get*"
      ],
      "Resource": "*"
    }
  ]
}
```

### Operator Access Policy
<a name="aws_directory_service_operator_access_policy"></a>

 **Use this for:** Operators managing directory resources

 **Grants access to:** 
+ All read-only permissions
+ Manage tags, RADIUS, LDAPS, and log subscriptions

 **Does NOT grant:** 
+ Delete directories
+ Manage IAM access policies

 **Testing this policy:** 

```
# Verify operator access works (requires MFA)
aws ds enable-ldaps --directory-id d-0123456789 --type Client

# Verify admin access is denied (should fail)
aws ds delete-directory --directory-id d-0123456789
```

 **Policy JSON:** 

 **Purpose:** Provides operational access for routine directory management tasks with MFA requirement.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ds:Describe*",
        "ds:List*",
        "ds:Get*",
        "ds:AddTagsToResource",
        "ds:RemoveTagsFromResource",
        "ds:EnableLDAPS",
        "ds:DisableLDAPS",
        "ds:EnableRadius",
        "ds:DisableRadius",
        "ds:CreateLogSubscription",
        "ds:DeleteLogSubscription"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
```

### Administrator Access Policy
<a name="aws_directory_service_administrator_access_policy"></a>

 **Use this for:** Service administrators with full management access

 **Grants access to:** 
+ All operator permissions
+ Create and delete directories
+ Manage trusts and all directory settings

 **Requires:** 
+ MFA with maximum 1-hour session duration

 **Testing this policy:** 

```
# Verify full admin access works (requires MFA)
aws ds create-microsoft-ad --name corp.example.com --password <pw> --vpc-settings VpcId=vpc-123,SubnetIds=subnet-1,subnet-2
aws ds delete-directory --directory-id d-0123456789
```

 **Policy JSON:** 

 **Purpose:** Provides full administrative access with MFA and session time restrictions.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ds:*",
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
<a name="aws_directory_service_implementation_guidance"></a>

 **Role-Based Access Control:** 
+ Create separate IAM roles for Directory Service viewers, operators, and administrators
+ Always require MFA for privileged directory operations and administrative access
+ Use time-based conditions to limit session duration for administrative roles
+ Apply resource-specific conditions where possible to limit blast radius
+ Regularly review and audit policy assignments and usage patterns
+ Use AWS IAM Access Analyzer to validate least privilege implementations

 **Security Best Practices:** 
+ Start with read-only access and incrementally add permissions as needed
+ Use AWS managed policies as a baseline when available and appropriate
+ Monitor policy usage with CloudTrail and Access Analyzer
+ Document business justification for each permission granted

## SCG-CSO-SDF: Secure Defaults
<a name="aws_directory_service_scg_cso_sdf_secure_defaults"></a>

 **Applicable:** Yes

AWS services are designed with security in mind, providing multiple layers of security controls and encryption capabilities. However, AWS allows customers to define the security configuration of services and does not enforce a minimum security standard by default, enabling customers the flexibility to meet their specific business requirements and compliance needs.

AWS Directory Service should be configured using the above AWS Security Best Practice recommendations. AWS allows customers to define the security of services, and does not enforce a minimum security standard by default.

### Implementation Guidelines
<a name="aws_directory_service_implementation_guidelines"></a>

Ensure AWS Directory Service resources are created with security-first configurations that align with AWS security best practices and organizational compliance requirements.

 **Security Configuration Best Practices:** 
+ Enable LDAPS encryption for AWS Managed Microsoft AD
+ Configure strong domain password and lockout policies
+ Enable MFA for administrative access (RADIUS integration)
+ Enable comprehensive logging to CloudWatch Logs and CloudTrail
+ Deploy in private subnets with least-privilege security groups
+ Configure conditional forwarders with secure DNS resolution

## SCG-ENH-CMP: Configuration Comparison
<a name="aws_directory_service_scg_enh_cmp_configuration_comparison"></a>

 **Applicable:** Yes

 **Implementation Overview:** Use AWS Config, custom compliance checks, and Directory Service API queries to compare current directory configurations against established FedRAMP baselines.

### Configuration Monitoring
<a name="aws_directory_service_configuration_monitoring"></a>

```
# Describe directories and compare against baseline
aws ds describe-directories \
  --query 'DirectoryDescriptions[*].{Id:DirectoryId,Type:Type,Stage:Stage,RadiusStatus:RadiusStatus}' \
  --output table

# Export configuration for comparison
aws ds describe-directories --output json > current-ds-config.json
```

### Automation Framework
<a name="aws_directory_service_automation_framework"></a>
+ Use AWS Config to monitor Directory Service resource configurations
+ Implement custom checks for LDAPS status, logging, and network placement
+ Integrate with AWS Security Hub for centralized compliance reporting

## SCG-ENH-EXP: Configuration Export
<a name="aws_directory_service_scg_enh_exp_configuration_export"></a>

 **Applicable:** Yes

 **Implementation Overview:** Export AWS Directory Service configuration using AWS CLI describe commands in machine-readable JSON format for backup, audit, and compliance documentation.

### Export Procedures
<a name="aws_directory_service_export_procedures"></a>

 **Export Format:** JSON via AWS CLI

 **Primary Export Commands:** 

```
# Export complete Directory Service configuration
aws ds describe-directories --output json > ds-directories.json
aws ds describe-trusts --output json > ds-trusts.json
aws ds list-log-subscriptions --output json > ds-log-subscriptions.json
```

 **Configuration Export Use Cases:** 
+ Backup current configuration state
+ Compare configurations across environments
+ Audit and compliance reporting requirements
+ Disaster recovery planning and documentation

## SCG-ENH-API: API Configuration
<a name="aws_directory_service_scg_enh_api_api_configuration"></a>

 **Applicable:** Yes

 **Implementation Overview:** AWS Directory Service security configurations are manageable through AWS APIs, CLI commands, and Infrastructure as Code tools, enabling automated and repeatable security implementations.

### Managed Microsoft AD Creation
<a name="aws_directory_service_managed_microsoft_ad_creation"></a>

 **API Command:** 

```
# Create AWS Managed Microsoft AD in private subnets
aws ds create-microsoft-ad \
  --name corp.example.com \
  --password <secure-admin-password> \
  --vpc-settings VpcId=vpc-12345678,SubnetIds=subnet-12345678,subnet-87654321 \
  --edition Standard
```

 **Control Mapping:** IA-5 (Authenticator Management)

### LDAPS Configuration
<a name="aws_directory_service_ldaps_configuration"></a>

 **API Command:** 

```
# Enable client-side LDAPS (AWS Managed Microsoft AD acting as an LDAP client to a self-managed AD).
# For server-side LDAPS that protects the directory's own inbound LDAP traffic, install a
# certificate from a domain-joined Microsoft enterprise CA on the domain controllers.
aws ds enable-ldaps --directory-id d-0123456789 --type Client
```

 **Control Mapping:** SC-8 (Transmission Confidentiality and Integrity)

### Directory Logging
<a name="aws_directory_service_directory_logging"></a>

 **API Command:** 

```
# Forward directory logs to CloudWatch Logs
aws ds create-log-subscription \
  --directory-id d-0123456789 \
  --log-group-name /aws/directoryservice/d-0123456789
```

 **Control Mapping:** AU-2 (Audit Events)

## Additional Resources
<a name="aws_directory_service_additional_resources"></a>

For more information about AWS security best practices, see the following resources:

 ** AWS Security Documentation:** 
+  [AWS Security Documentation](https://docs.aws.amazon.com/security/) - Comprehensive security guidance across all AWS services
+  [AWS FedRAMP Compliance](https://docs.aws.amazon.com/compliance/fedramp/) - FedRAMP-specific compliance information and resources
+  [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Security design principles and best practices

 **AWS Directory Service-Specific Resources:** 
+  [AWS Directory Service Administration Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) - Service documentation and configuration guidance
+  [AWS Managed Microsoft AD Best Practices](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_best_practices.html) - Service-specific security recommendations
+  [Enable LDAPS](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_ldap.html) - Secure LDAP configuration guidance

 **Compliance and Governance:** 
+  [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) - Automated compliance monitoring and evaluation
+  [AWS CloudTrail User Guide](https://docs.aws.amazon.com/cloudtrail/latest/userguide/cloudtrail-user-guide.html) - API logging and audit trail management