

# AWS Managed Services (AMS)
<a name="aws-managed-services-ams"></a>

This guide provides security configuration requirements and implementation examples for AWS Managed Services (AMS) in accordance with FedRAMP requirements.

## Document Information
<a name="aws_managed_services_ams_document_information"></a>


|  |  | 
| --- |--- |
| Version | 1.0.0 | 
| Last Updated | 2026-09-02 | 
| Documentation URL | https://docs.aws.amazon.com/managedservices/ | 

## Overview
<a name="aws_managed_services_ams_overview"></a>

AWS Managed Services (AMS) manages your AWS infrastructure under a shared operating model. AMS security configuration involves controls over how customers request and authorize changes, how administrative access is granted, and how activity is logged and monitored to meet FedRAMP compliance requirements. This guidance covers the administrative access model (IAM principals and AMS change management). It also describes the security-related settings restricted to administrative principals and the privileged access controls for AMS operations.

**Note**  
This guidance applies to the **AMS Advanced** operations plan, which uses the Request for Change (RFC) change-management model and the `amscm` API. **AMS Accelerate** does not use RFCs; customers on AMS Accelerate should apply the secure-configuration guidance for the underlying AWS services they operate.

 **Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

 **Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements
<a name="aws_managed_services_ams_fedramp_requirements"></a>

AWS Managed Services (AMS) must comply with the following FedRAMP requirements:
+ SCG-CSO-RSC
+ SCG-CSO-SDF
+ SCG-ENH-CMP
+ SCG-ENH-EXP
+ SCG-ENH-API

## Administrative Account Model
<a name="aws_managed_services_ams_administrative_account_model"></a>

AWS Managed Services (AMS) has an administrative account model.


|  |  | 
| --- |--- |
| Administrative Accounts | Yes | 
| Account Type | IAM administrative principals governed by the AMS change management model | 

## SCG-CSO-RSC: Recommended Secure Configuration
<a name="aws_managed_services_ams_scg_cso_rsc_recommended_secure_configuration"></a>

 **Applicable:** Yes

This requirement consolidates guidance for: 1. Instructions on how to securely access, configure, operate, and decommission top-level administrative accounts 2. Explanations of security-related settings that can be operated only by top-level administrative accounts 3. Explanations of security-related settings that can be operated only by privileged accounts

### Part 1: Administrative Accounts
<a name="aws_managed_services_ams_part_1_administrative_accounts"></a>

 **Applicable:** Yes

 **Implementation Overview:** AWS Managed Services (AMS) operates under a shared operating model: AWS manages the underlying infrastructure while customers retain control over how administrative access is granted and how changes are authorized. Customer administrative access is exercised through AWS IAM principals and the AMS change management model (Requests for Change, or RFCs), rather than a service-native superuser account. This guidance covers securing administrative access across its lifecycle: access, configuration, operation, and decommissioning.

### Administrative Access Security
<a name="aws_managed_services_ams_administrative_access_security"></a>
+ Grant administrative access through least-privilege IAM roles assumed with MFA, not long-lived users
+ Use AMS-provided roles and the change management model so infrastructure changes go through reviewed, auditable Requests for Change (RFCs)
+ Restrict who can approve RFCs and who can invoke change types that modify security-relevant configuration
+ Store any required credentials in a managed secrets store and rotate them regularly

### Access and Network Security
<a name="aws_managed_services_ams_access_and_network_security"></a>
+ Access AMS-managed environments only through approved, access-controlled paths (console, API, or bastion/SSM as configured)
+ Enforce MFA for IAM principals that manage AMS resources or submit/approve RFCs
+ Apply least-privilege network controls to management access paths

### Monitoring and Auditing
<a name="aws_managed_services_ams_monitoring_and_auditing"></a>
+ Enable AWS CloudTrail across AMS-managed accounts to record administrative and change activity
+ Review RFC history and AMS reporting for administrative actions
+ Configure CloudWatch alarms for sensitive events and integrate findings with your monitoring pipeline

### Decommissioning Administrative Accounts
<a name="aws_managed_services_ams_decommissioning_administrative_accounts"></a>
+ Remove IAM users, roles, and access keys used for AMS administration when no longer required, following access reviews
+ Offboard personnel by revoking role access and updating trust policies and RFC approver lists
+ Follow the applicable AMS offboarding/decommissioning process when retiring an AMS-managed account or workload

### FedRAMP Controls Addressed
<a name="aws_managed_services_ams_fedramp_controls_addressed"></a>
+ AC-2: Account Management
+ AC-3: Access Enforcement
+ AC-6: Least Privilege
+ AU-2: Audit Events
+ CM-3: Configuration Change Control
+ IA-2: Identification and Authentication

### Implementation Checklist
<a name="aws_managed_services_ams_implementation_checklist"></a>

☐ Administer via least-privilege IAM roles with MFA ☐ Use the AMS change management (RFC) model for infrastructure changes ☐ Restrict RFC submission/approval to authorized principals ☐ Enable CloudTrail across AMS-managed accounts ☐ Review RFC history and AMS reporting regularly ☐ Remove unused administrative credentials ☐ Document administrative procedures and conduct regular access reviews

This guidance helps ensure that AWS Managed Services administrative access is configured according to security best practices and FedRAMP requirements.

### Part 2: Administrative Settings
<a name="aws_managed_services_ams_part_2_administrative_settings"></a>

 **Applicable:** Yes

### Security-Related Settings Restricted to Administrative Principals
<a name="aws_managed_services_ams_security_related_settings_restricted_to_administrative_principals"></a>

Within AMS, security-relevant changes are governed by the change management model and are restricted to authorized administrative principals. The following operations and their security implications are restricted to those principals.

#### 1. Change Management (RFC) Authorization
<a name="aws_managed_services_ams_1_change_management_rfc_authorization"></a>

 **Operations:** 
+ Submit, approve, and reject Requests for Change (RFCs)
+ Invoke change types that modify security-relevant configuration

 **Security Implications:** 
+ RFC approval authority determines what changes can be applied to the environment
+ Unauthorized change approval could weaken the security posture of managed resources

#### 2. IAM Access and Role Management
<a name="aws_managed_services_ams_2_iam_access_and_role_management"></a>

 **Operations:** 
+ Grant, modify, and remove IAM access used to administer AMS resources

 **Security Implications:** 
+ Controls who can operate the managed environment and submit changes
+ Excessive permissions violate least privilege and increase blast radius

#### 3. Logging and Monitoring Configuration
<a name="aws_managed_services_ams_3_logging_and_monitoring_configuration"></a>

 **Operations:** 
+ Configure CloudTrail, log delivery, and monitoring integrations for managed accounts

 **Security Implications:** 
+ Disabling or misconfiguring logging could conceal unauthorized activity
+ Audit records are critical for forensics and FedRAMP continuous monitoring

#### 4. Account and Environment Lifecycle
<a name="aws_managed_services_ams_4_account_and_environment_lifecycle"></a>

 **Operations:** 
+ Onboard and offboard AMS-managed accounts and workloads

 **Security Implications:** 
+ Lifecycle changes alter the security boundary of the managed environment
+ Improper offboarding can leave residual access or resources

### Part 3: Privileged Settings
<a name="aws_managed_services_ams_part_3_privileged_settings"></a>

 **Applicable:** Yes

Privileged access to AWS Managed Services is controlled through AWS IAM combined with the AMS change management model. This section provides example IAM policies for varying levels of access to AMS APIs. Infrastructure-level changes remain governed by RFCs regardless of IAM access level.

## IAM Least Privilege Policies
<a name="aws_managed_services_ams_iam_least_privilege_policies"></a>

This section provides sample IAM policies for implementing least privilege access to AWS Managed Services operations across different operational roles.

### Policy Selection Guide
<a name="aws_managed_services_ams_policy_selection_guide"></a>

Choose the appropriate policy based on your role:


| Policy | Use Case | MFA Required | 
| --- | --- | --- | 
| Read-Only Access | Auditors, compliance reviewers, monitoring dashboards | No | 
| Operator Access | Operators submitting and tracking RFCs | Yes | 
| Administrator Access | AMS administrators with full management access | Yes (1-hour max) | 

### Read-Only Access Policy
<a name="aws_managed_services_ams_read_only_access_policy"></a>

 **Use this for:** Auditors, compliance reviewers, monitoring dashboards

 **Grants access to:** 
+ View change types, RFCs, and their status
+ List AMS resources and reports

 **Does NOT grant:** 
+ Submit, approve, or reject RFCs
+ Modify AMS configuration

 **Testing this policy:** 

```
# Verify read access works
aws amscm list-rfc-summaries --output json

# Verify write access is denied (should fail)
aws amscm create-rfc --change-type-id <id> --change-type-version 1.0 --title test --execution-parameters '{}'
```

 **Policy JSON:** 

 **Purpose:** Provides read-only access to AMS change management resources for monitoring and auditing purposes.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "amscm:List*",
        "amscm:Get*",
        "amscm:Describe*"
      ],
      "Resource": "*"
    }
  ]
}
```

### Operator Access Policy
<a name="aws_managed_services_ams_operator_access_policy"></a>

 **Use this for:** Operators submitting and tracking RFCs

 **Grants access to:** 
+ All read-only permissions
+ Create and submit RFCs for approved change types

 **Does NOT grant:** 
+ Approve RFCs
+ Manage IAM access for other principals

 **Testing this policy:** 

```
# Verify operator access works (requires MFA)
aws amscm create-rfc --change-type-id <id> --change-type-version 1.0 --title "Patch window" --execution-parameters '{}'

# Verify approval is denied (should fail)
aws amscm approve-rfc --rfc-id <rfc-id>
```

 **Policy JSON:** 

 **Purpose:** Provides operational access to submit and track AMS RFCs with MFA requirement.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "amscm:List*",
        "amscm:Get*",
        "amscm:Describe*",
        "amscm:CreateRfc",
        "amscm:SubmitRfc",
        "amscm:UpdateRfc"
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
<a name="aws_managed_services_ams_administrator_access_policy"></a>

 **Use this for:** AMS administrators with full management access

 **Grants access to:** 
+ All operator permissions
+ Approve/reject RFCs and manage AMS change management configuration

 **Requires:** 
+ MFA with maximum 1-hour session duration

 **Testing this policy:** 

```
# Verify full admin access works (requires MFA)
aws amscm approve-rfc --rfc-id <rfc-id>
```

 **Policy JSON:** 

 **Purpose:** Provides full AMS administrative access with MFA and session time restrictions.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "amscm:*",
        "amsskms:*"
      ],
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
<a name="aws_managed_services_ams_implementation_guidance"></a>

 **Role-Based Access Control:** 
+ Create separate IAM roles for AMS viewers, RFC operators, and administrators
+ Always require MFA for privileged AMS operations and RFC approval
+ Use time-based conditions to limit session duration for administrative roles
+ Separate RFC submission from RFC approval to enforce separation of duties
+ Regularly review and audit policy assignments and RFC history
+ Use AWS IAM Access Analyzer to validate least privilege implementations

 **Security Best Practices:** 
+ Start with read-only access and incrementally add permissions as needed
+ Use AWS managed policies as a baseline when available and appropriate
+ Monitor policy usage and change activity with CloudTrail and AMS reporting
+ Document business justification for each permission granted

## SCG-CSO-SDF: Secure Defaults
<a name="aws_managed_services_ams_scg_cso_sdf_secure_defaults"></a>

 **Applicable:** Yes

AWS services are designed with security in mind, providing multiple layers of security controls and encryption capabilities. However, AWS allows customers to define the security configuration of services and does not enforce a minimum security standard by default, enabling customers the flexibility to meet their specific business requirements and compliance needs.

AWS Managed Services should be operated using the above AWS Security Best Practice recommendations and the AMS change management model. AWS allows customers to define the security of their environment, and does not enforce a minimum security standard by default.

### Implementation Guidelines
<a name="aws_managed_services_ams_implementation_guidelines"></a>

Ensure AWS Managed Services environments are operated with security-first configurations that align with AWS security best practices and organizational compliance requirements.

 **Security Configuration Best Practices:** 
+ Administer through least-privilege IAM roles with MFA
+ Route infrastructure changes through the AMS change management (RFC) model
+ Enforce separation of duties between RFC submission and approval
+ Enable CloudTrail across all AMS-managed accounts
+ Review RFC history and AMS reporting for administrative activity

## SCG-ENH-CMP: Configuration Comparison
<a name="aws_managed_services_ams_scg_enh_cmp_configuration_comparison"></a>

 **Applicable:** Yes

 **Implementation Overview:** Use AWS Config, AMS reporting, and change management history to compare current AMS configuration and change activity against established FedRAMP baselines.

### Configuration Monitoring
<a name="aws_managed_services_ams_configuration_monitoring"></a>

```
# List change type categories and review RFC activity against baseline
aws amscm list-change-type-categories --output table
aws amscm list-rfc-summaries --output json > current-ams-rfcs.json
```

### Automation Framework
<a name="aws_managed_services_ams_automation_framework"></a>
+ Use AWS Config to monitor resource configurations in AMS-managed accounts
+ Use AMS reporting to review change activity and compliance posture
+ Integrate with AWS Security Hub for centralized compliance reporting

## SCG-ENH-EXP: Configuration Export
<a name="aws_managed_services_ams_scg_enh_exp_configuration_export"></a>

 **Applicable:** Yes

 **Implementation Overview:** Export AWS Managed Services change management and configuration data using AWS CLI commands in machine-readable JSON format for backup, audit, and compliance documentation.

### Export Procedures
<a name="aws_managed_services_ams_export_procedures"></a>

 **Export Format:** JSON via AWS CLI

 **Primary Export Commands:** 

```
# Export AMS change management data
aws amscm list-rfc-summaries --output json > ams-rfcs.json
aws amscm list-change-type-categories --output json > ams-change-type-categories.json
```

 **Configuration Export Use Cases:** 
+ Backup current change management state
+ Compare configurations across environments
+ Audit and compliance reporting requirements
+ Disaster recovery planning and documentation

## SCG-ENH-API: API Configuration
<a name="aws_managed_services_ams_scg_enh_api_api_configuration"></a>

 **Applicable:** Yes

 **Implementation Overview:** AWS Managed Services operations are manageable through AWS APIs, CLI commands, and the change management model, enabling automated and auditable security implementations.

### Change Request Submission
<a name="aws_managed_services_ams_change_request_submission"></a>

 **API Command:** 

```
# Create a Request for Change (RFC) for an approved change type
aws amscm create-rfc \
  --change-type-id <change-type-id> \
  --change-type-version 1.0 \
  --title "Security configuration update" \
  --execution-parameters '{}'
```

 **Control Mapping:** CM-3 (Configuration Change Control)

### Change Activity Review
<a name="aws_managed_services_ams_change_activity_review"></a>

 **API Command:** 

```
# Retrieve details of a specific RFC for audit
aws amscm get-rfc --rfc-id <rfc-id>
```

 **Control Mapping:** AU-2 (Audit Events)

## Additional Resources
<a name="aws_managed_services_ams_additional_resources"></a>

For more information about AWS security best practices, see the following resources:

 ** AWS Security Documentation:** 
+  [AWS Security Documentation](https://docs.aws.amazon.com/security/) - Comprehensive security guidance across all AWS services
+  [AWS FedRAMP Compliance](https://docs.aws.amazon.com/compliance/fedramp/) - FedRAMP-specific compliance information and resources
+  [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Security design principles and best practices

 **AWS Managed Services-Specific Resources:** 
+  [AWS Managed Services User Guide](https://docs.aws.amazon.com/managedservices/latest/userguide/what-is-ams.html) - Service documentation and operating model
+  [AMS Change Management](https://docs.aws.amazon.com/managedservices/latest/userguide/change-management.html) - Requests for Change (RFCs) and change types
+  [AMS Access Management](https://docs.aws.amazon.com/managedservices/latest/userguide/access-management.html) - Administrative access controls

 **Compliance and Governance:** 
+  [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) - Automated compliance monitoring and evaluation
+  [AWS CloudTrail User Guide](https://docs.aws.amazon.com/cloudtrail/latest/userguide/cloudtrail-user-guide.html) - API logging and audit trail management