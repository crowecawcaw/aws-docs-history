

# AWS CloudHSM
<a name="aws-cloudhsm"></a>

This guide provides security configuration requirements and implementation examples for AWS CloudHSM in accordance with FedRAMP requirements.

## Document Information
<a name="aws_cloudhsm_document_information"></a>


|  |  | 
| --- |--- |
| Version | 1.0.0 | 
| Last Updated | 2026-09-02 | 
| Documentation URL | https://docs.aws.amazon.com/cloudhsm/latest/userguide/ | 

## Overview
<a name="aws_cloudhsm_overview"></a>

AWS CloudHSM security configuration involves implementing comprehensive security controls including encryption, access management, logging, and monitoring to meet FedRAMP compliance requirements. This guidance covers administrative account security for the HSM admin (Crypto Officer) and Crypto User (CU) accounts. It also describes the security-related settings restricted to those accounts and the privileged access controls for CloudHSM operations.

 **Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

 **Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements
<a name="aws_cloudhsm_fedramp_requirements"></a>

AWS CloudHSM must comply with the following FedRAMP requirements:
+ SCG-CSO-RSC
+ SCG-CSO-SDF
+ SCG-ENH-CMP
+ SCG-ENH-EXP
+ SCG-ENH-API

## Administrative Account Model
<a name="aws_cloudhsm_administrative_account_model"></a>

AWS CloudHSM has an administrative account model.


|  |  | 
| --- |--- |
| Administrative Accounts | Yes | 
| Account Type | HSM admin (Crypto Officer) and Crypto User (CU) accounts | 

## SCG-CSO-RSC: Recommended Secure Configuration
<a name="aws_cloudhsm_scg_cso_rsc_recommended_secure_configuration"></a>

 **Applicable:** Yes

This requirement consolidates guidance for: 1. Instructions on how to securely access, configure, operate, and decommission top-level administrative accounts 2. Explanations of security-related settings that can be operated only by top-level administrative accounts 3. Explanations of security-related settings that can be operated only by privileged accounts

### Part 1: Administrative Accounts
<a name="aws_cloudhsm_part_1_administrative_accounts"></a>

 **Applicable:** Yes

 **Implementation Overview:** AWS CloudHSM administrative access is managed through HSM users. These users are internal to the HSM and are distinct from AWS IAM identities. The **admin** is the top-level administrative account that manages HSM users and cluster administration. Crypto User (CU) accounts perform cryptographic operations. In Client SDK 5, the **admin** role is synonymous with the **crypto officer (CO)** role in the previous Client SDK 3. HSM users are managed with the CloudHSM CLI (`cloudhsm-cli`). This guidance provides security recommendations for the administrative account lifecycle: access, configuration, operation, and decommissioning.

### Admin (Crypto Officer) Account Security
<a name="aws_cloudhsm_admin_crypto_officer_account_security"></a>

 **Admin Account Configuration:** 
+ Set the default `admin` password when you activate the cluster, and protect it rigorously — AWS CloudHSM has no access to your HSM user credentials and cannot recover them if lost
+ Use strong, randomly generated passwords for all admin accounts and store them in a managed secrets store (for example, AWS Secrets Manager)
+ Maintain at least two admins so a lost admin password can be reset by another admin, preventing cluster lockout
+ Limit the number of admin accounts to the minimum required for administration and separation of duties
+ Rotate admin passwords on a regular schedule and after any personnel change
+ Never use the admin account for routine cryptographic operations — reserve it for user and cluster management

 **Authentication Methods:** 
+ Enable quorum authentication (M of N) for all user management operations so no single admin can act unilaterally
+ Manage HSM users only from hardened client instances using CloudHSM CLI (`cloudhsm-cli`); only admins can manage users
+ Restrict which principals can access the client instances used to run CloudHSM CLI

### Crypto User (CU) Account Security
<a name="aws_cloudhsm_crypto_user_cu_account_security"></a>
+ Create multiple CU accounts, each with limited permissions, so no single user has total control (for example, separate key-generation duties from key-usage duties)
+ Create individual CU accounts per application or workload; avoid shared CU credentials
+ Rotate CU credentials regularly and store them in a managed secrets store
+ Remove CU accounts that are no longer required as part of routine access reviews
+ Note: a crypto user that owns keys cannot be deleted until its keys are reassigned or deleted

### Access and Network Security
<a name="aws_cloudhsm_access_and_network_security"></a>
+ Deploy CloudHSM clusters in private subnets with VPC isolation; do not expose HSMs to the public internet
+ Use the cluster security group to allow connectivity only from the client instances that require it
+ Access HSM administrative functions only from hardened, access-controlled client instances
+ Use FIPS-mode clusters to meet FedRAMP cryptographic requirements

### Monitoring and Auditing
<a name="aws_cloudhsm_monitoring_and_auditing"></a>
+ Review the HSM audit logs that AWS CloudHSM automatically delivers to Amazon CloudWatch Logs, and monitor admin activity regularly
+ Enable AWS CloudTrail for all CloudHSM (`cloudhsmv2`) API calls
+ Configure CloudWatch alarms for unusual HSM operations or authentication failures
+ Set log retention appropriate to your compliance requirements

### Backup and Recovery Security
<a name="aws_cloudhsm_backup_and_recovery_security"></a>
+ Configure an appropriate backup retention policy for the cluster (7–379 days)
+ Restrict and audit access to backups and cross-Region backup copies; backups contain sensitive key material
+ Ensure the target cluster mode is appropriate for the key material in the backup; restore FIPS-mode backups into FIPS-mode clusters to preserve FIPS compliance

### Decommissioning Administrative Accounts
<a name="aws_cloudhsm_decommissioning_administrative_accounts"></a>
+ Delete HSM users that are no longer required with CloudHSM CLI, following separation-of-duties and quorum controls
+ When retiring a cluster, delete the HSMs and then the cluster via the CloudHSM API after securely handling key material per your key-management policy
+ Revoke access to client instances and rotate any shared secrets after decommissioning

### FedRAMP Controls Addressed
<a name="aws_cloudhsm_fedramp_controls_addressed"></a>
+ AC-2: Account Management
+ AC-3: Access Enforcement
+ AC-6: Least Privilege
+ AU-2: Audit Events
+ IA-2: Identification and Authentication
+ SC-12: Cryptographic Key Establishment and Management
+ SC-13: Cryptographic Protection
+ SC-28: Protection of Information at Rest

### Implementation Checklist
<a name="aws_cloudhsm_implementation_checklist"></a>

☐ Set and securely store strong admin credentials ☐ Maintain at least two admins to prevent lockout ☐ Enable quorum authentication for user management operations ☐ Create individual, least-privilege Crypto User accounts ☐ Deploy clusters in private subnets with restrictive security groups ☐ Use FIPS-mode clusters ☐ Enable HSM audit logging and CloudTrail ☐ Configure backup retention and restrict backup access ☐ Document administrative procedures and conduct regular access reviews

This guidance helps ensure that AWS CloudHSM administrative accounts are configured according to security best practices and FedRAMP requirements.

### Part 2: Administrative Settings
<a name="aws_cloudhsm_part_2_administrative_settings"></a>

 **Applicable:** Yes

### Security-Related Settings Restricted to the Admin Account
<a name="aws_cloudhsm_security_related_settings_restricted_to_the_admin_account"></a>

The admin (Crypto Officer) account in AWS CloudHSM has elevated privileges. The following operations and their security implications are restricted to the admin account.

#### 1. HSM User Management
<a name="aws_cloudhsm_1_hsm_user_management"></a>

 **Operations:** 
+ Create, delete, and manage Crypto Users (CU) and additional admins
+ Set and change user passwords

 **Security Implications:** 
+ Controls who can access the HSM and perform cryptographic operations
+ Unauthorized user creation could grant access to cryptographic keys
+ Improper password management weakens authentication to the HSM

#### 2. Quorum Authentication (M of N) Configuration
<a name="aws_cloudhsm_2_quorum_authentication_m_of_n_configuration"></a>

 **Operations:** 
+ Enable and configure quorum authentication for user management operations
+ Register quorum tokens and set the required number of approvers

 **Security Implications:** 
+ Prevents a single administrator from unilaterally performing sensitive operations
+ Misconfiguration can either weaken separation of duties or lock out administration

#### 3. Cluster and HSM Lifecycle
<a name="aws_cloudhsm_3_cluster_and_hsm_lifecycle"></a>

 **Operations:** 
+ Initialize the cluster, add and remove HSMs, delete the cluster

 **Security Implications:** 
+ Cluster deletion can result in permanent loss of key material
+ Adding or removing HSMs affects the trust boundary of the cluster

#### 4. Key Management Policy
<a name="aws_cloudhsm_4_key_management_policy"></a>

 **Operations:** 
+ Control key attributes and access to key material via CU capabilities
+ Manage key backup and restore within the cluster

 **Security Implications:** 
+ Key access controls determine confidentiality of cryptographic material
+ Backup handling affects both availability and confidentiality of keys

#### 5. Audit Log Review and Retention
<a name="aws_cloudhsm_5_audit_log_review_and_retention"></a>

 **Operations:** 
+ Review the HSM audit logs that AWS CloudHSM automatically delivers to Amazon CloudWatch Logs, and configure log retention and CloudTrail for `cloudhsmv2` API calls

 **Security Implications:** 
+ Loss or under-retention of audit records could conceal malicious or unauthorized activity
+ Audit records are critical for forensics and FedRAMP continuous monitoring

### Part 3: Privileged Settings
<a name="aws_cloudhsm_part_3_privileged_settings"></a>

 **Applicable:** Yes

Within AWS CloudHSM there are two layers of privileged access. One layer is at the AWS IAM layer, where you control which principals can manage the CloudHSM service (clusters, HSMs, backups) via the `cloudhsmv2` API. This section covers those privileged settings and provides example IAM policies for varying levels of access. The second layer of privileged access is at the HSM layer itself (admin and CU accounts), which is covered in the other sections of this document.

## IAM Least Privilege Policies
<a name="aws_cloudhsm_iam_least_privilege_policies"></a>

This section provides sample IAM policies for implementing least privilege access to AWS CloudHSM service operations across different operational roles.

### Policy Selection Guide
<a name="aws_cloudhsm_policy_selection_guide"></a>

Choose the appropriate policy based on your role:


| Policy | Use Case | MFA Required | 
| --- | --- | --- | 
| Read-Only Access | Auditors, compliance reviewers, monitoring dashboards | No | 
| Operator Access | Operators managing CloudHSM resources | Yes | 
| Administrator Access | Service administrators with full management access | Yes (1-hour max) | 

### Read-Only Access Policy
<a name="aws_cloudhsm_read_only_access_policy"></a>

 **Use this for:** Auditors, compliance reviewers, monitoring dashboards

 **Grants access to:** 
+ View cluster and HSM configurations
+ List CloudHSM resources
+ Describe backups and tags

 **Does NOT grant:** 
+ Create, modify, or delete clusters or HSMs
+ Change configurations

 **Testing this policy:** 

```
# Verify read access works
aws cloudhsmv2 describe-clusters --output json

# Verify write access is denied (should fail)
aws cloudhsmv2 delete-cluster --cluster-id cluster-1234567890abcdef0
```

 **Policy JSON:** 

 **Purpose:** Provides read-only access to CloudHSM resources for monitoring and auditing purposes.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudhsmv2:Describe*",
        "cloudhsmv2:List*"
      ],
      "Resource": "*"
    }
  ]
}
```

### Operator Access Policy
<a name="aws_cloudhsm_operator_access_policy"></a>

 **Use this for:** Operators managing CloudHSM resources

 **Grants access to:** 
+ All read-only permissions
+ Create HSMs and copy backups
+ Tag resources

 **Does NOT grant:** 
+ Delete clusters
+ Manage IAM access policies

 **Testing this policy:** 

```
# Verify operator access works (requires MFA)
aws cloudhsmv2 create-hsm --cluster-id cluster-1234567890abcdef0 --availability-zone us-east-1a

# Verify admin access is denied (should fail)
aws cloudhsmv2 delete-cluster --cluster-id cluster-1234567890abcdef0
```

 **Policy JSON:** 

 **Purpose:** Provides operational access for routine CloudHSM management tasks with MFA requirement.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudhsmv2:Describe*",
        "cloudhsmv2:List*",
        "cloudhsmv2:CreateHsm",
        "cloudhsmv2:CopyBackupToRegion",
        "cloudhsmv2:TagResource"
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
<a name="aws_cloudhsm_administrator_access_policy"></a>

 **Use this for:** Service administrators with full management access

 **Grants access to:** 
+ All operator permissions
+ Create and delete clusters and HSMs
+ Manage backups and cross-Region copies

 **Requires:** 
+ MFA with maximum 1-hour session duration

 **Testing this policy:** 

```
# Verify full admin access works (requires MFA)
aws cloudhsmv2 create-cluster --hsm-type hsm2m.medium --mode FIPS --backup-retention-policy Type=DAYS,Value=90 --subnet-ids subnet-12345678 subnet-87654321
aws cloudhsmv2 delete-cluster --cluster-id cluster-1234567890abcdef0
```

 **Policy JSON:** 

 **Purpose:** Provides full administrative access with MFA and session time restrictions.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudhsmv2:*",
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
<a name="aws_cloudhsm_implementation_guidance"></a>

 **Role-Based Access Control:** 
+ Create separate IAM roles for CloudHSM viewers, operators, and administrators
+ Always require MFA for privileged CloudHSM operations and administrative access
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
<a name="aws_cloudhsm_scg_cso_sdf_secure_defaults"></a>

 **Applicable:** Yes

AWS services are designed with security in mind, providing multiple layers of security controls and encryption capabilities. However, AWS allows customers to define the security configuration of services and does not enforce a minimum security standard by default, enabling customers the flexibility to meet their specific business requirements and compliance needs.

AWS CloudHSM should be configured using the above AWS Security Best Practice recommendations. AWS allows customers to define the security of services, and does not enforce a minimum security standard by default.

### Implementation Guidelines
<a name="aws_cloudhsm_implementation_guidelines"></a>

Ensure AWS CloudHSM resources are created with security-first configurations that align with AWS security best practices and organizational compliance requirements.

 **Security Configuration Best Practices:** 
+ Deploy CloudHSM clusters in FIPS mode to meet FedRAMP cryptographic requirements
+ Deploy clusters in private subnets with restrictive security groups
+ Protect admin and Crypto User credentials and enforce strong password practices
+ Enable quorum authentication for user management operations
+ Enable comprehensive audit logging (HSM audit logs and CloudTrail)
+ Configure appropriate backup retention and restrict access to backups

## SCG-ENH-CMP: Configuration Comparison
<a name="aws_cloudhsm_scg_enh_cmp_configuration_comparison"></a>

 **Applicable:** Yes

 **Implementation Overview:** Use AWS Config, custom compliance checks, and CloudHSM API queries to compare current CloudHSM configurations against established FedRAMP baselines.

### Configuration Monitoring
<a name="aws_cloudhsm_configuration_monitoring"></a>

```
# Describe clusters and compare against baseline
aws cloudhsmv2 describe-clusters \
  --query 'Clusters[*].{Id:ClusterId,State:State,HsmType:HsmType,Mode:Mode}' \
  --output table

# Export configuration for comparison
aws cloudhsmv2 describe-clusters --output json > current-cloudhsm-config.json
```

### Automation Framework
<a name="aws_cloudhsm_automation_framework"></a>
+ Use AWS Config to monitor CloudHSM-related resource configurations
+ Implement custom checks for cluster placement, FIPS mode, backup retention, and logging
+ Integrate with AWS Security Hub for centralized compliance reporting

## SCG-ENH-EXP: Configuration Export
<a name="aws_cloudhsm_scg_enh_exp_configuration_export"></a>

 **Applicable:** Yes

 **Implementation Overview:** Export AWS CloudHSM configuration using AWS CLI describe commands in machine-readable JSON format for backup, audit, and compliance documentation.

### Export Procedures
<a name="aws_cloudhsm_export_procedures"></a>

 **Export Format:** JSON via AWS CLI

 **Primary Export Commands:** 

```
# Export complete CloudHSM configuration
aws cloudhsmv2 describe-clusters --output json > cloudhsm-clusters.json
aws cloudhsmv2 describe-backups --output json > cloudhsm-backups.json
```

 **Configuration Export Use Cases:** 
+ Backup current configuration state
+ Compare configurations across environments
+ Audit and compliance reporting requirements
+ Disaster recovery planning and documentation

## SCG-ENH-API: API Configuration
<a name="aws_cloudhsm_scg_enh_api_api_configuration"></a>

 **Applicable:** Yes

 **Implementation Overview:** AWS CloudHSM security configurations are manageable through AWS APIs, CLI commands, and Infrastructure as Code tools, enabling automated and repeatable security implementations.

### FIPS-Mode Cluster Creation
<a name="aws_cloudhsm_fips_mode_cluster_creation"></a>

 **API Command:** 

```
# Create a FIPS-mode cluster in private subnets (required for FedRAMP)
aws cloudhsmv2 create-cluster \
  --hsm-type hsm2m.medium \
  --mode FIPS \
  --backup-retention-policy Type=DAYS,Value=90 \
  --subnet-ids subnet-12345678 subnet-87654321
```

 **Control Mapping:** SC-13 (Cryptographic Protection)

### Backup Configuration
<a name="aws_cloudhsm_backup_configuration"></a>

 **API Command:** 

```
# Copy a backup to another Region for disaster recovery
aws cloudhsmv2 copy-backup-to-region \
  --destination-region us-west-2 \
  --backup-id backup-1234567890abcdef0
```

 **Control Mapping:** CP-9 (Information System Backup)

## Additional Resources
<a name="aws_cloudhsm_additional_resources"></a>

For more information about AWS security best practices, see the following resources:

 ** AWS Security Documentation:** 
+  [AWS Security Documentation](https://docs.aws.amazon.com/security/) - Comprehensive security guidance across all AWS services
+  [AWS FedRAMP Compliance](https://docs.aws.amazon.com/compliance/fedramp/) - FedRAMP-specific compliance information and resources
+  [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Security design principles and best practices

 **AWS CloudHSM-Specific Resources:** 
+  [AWS CloudHSM User Guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/) - Service documentation and configuration guidance
+  [Managing HSM Users](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-hsm-users.html) - Admin (Crypto Officer) and Crypto User account management
+  [AWS CloudHSM Best Practices](https://docs.aws.amazon.com/cloudhsm/latest/userguide/best-practices.html) - Service-specific security recommendations

 **Compliance and Governance:** 
+  [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) - Automated compliance monitoring and evaluation
+  [AWS CloudTrail User Guide](https://docs.aws.amazon.com/cloudtrail/latest/userguide/cloudtrail-user-guide.html) - API logging and audit trail management