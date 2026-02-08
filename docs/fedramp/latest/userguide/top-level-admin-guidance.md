# Top Level Admin Guidance

This topic discusses top level admin guidance.

**Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

**Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## Document Information

|              |            |
| ------------ | ---------- |
| Version      | 1.0.0      |
| Last Updated | 2026-01-09 |

## FRR-RSC-01: Top-Level Administrative Accounts Guidance

✓ MUST - Required for all FedRAMP services

**OSCAL Control ID: FRR-RSC-01**

**UUID: frr-rsc-01-control**

## Requirement

Providers MUST create and maintain guidance that includes instructions on how to securely access, configure, operate, and decommission top-level administrative accounts that control enterprise access to the entire cloud service offering.

Note: This guidance should explain how top-level administrative accounts are named and referred to in the cloud service offering.

Applies to: Low, Moderate, High

## Component Implementation (OSCAL)

**Component UUID**: iam-component-001

**Component Type**: Account

**Control Implementation**: AC-2 (Account Management), AC-6 (Least Privilege), IA-2 (Identification and Authentication)

**Implementation Status**: Available

## Executive Summary

This comprehensive guidance provides AWS recommended practices for managing AWS top-level administrative accounts in FedRAMP environments, offering instructions for securely accessing, configuring, operating, and decommissioning administrative accounts that control enterprise access to AWS cloud services. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

A top-level account within AWS is identified as a [Management Account](../../../organizations/latest/userguide/orgs-manage_accounts_management.md "../../../organizations/latest/userguide/orgs-manage_accounts_management.md") that serves as the central control point for an [AWS Organization](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"). This guidance provides comprehensive information on multiple components of AWS account management, including the account itself, management account operations, and the secure access and configuration of accounts in association with administrative accounts and top-level administrative accounts that control access to the AWS management account and subsequent organizational structure.

**Key Coverage Areas**:

**Account Types and Naming Standards**: Recommends standardized naming conventions and hierarchical organization for Management Accounts, Security Accounts, Shared Services Accounts, and Workload Accounts, with clear reference methods for both console and programmatic access.

**Modern Root Access Management**: Describes how to leverage [AWS Organizations' centralized root access management](../../../organizations/latest/userguide/orgs_manage_accounts_access.md "../../../organizations/latest/userguide/orgs_manage_accounts_access.md") capabilities to eliminate long-term root credentials while maintaining necessary administrative capabilities through temporary, task-scoped root sessions.

**Configuration Management**: Provides guidance for implementing organization-wide configuration baselines using [AWS Config rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md"), [Service Control Policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md"), and automated drift detection to help maintain consistent security posture across all administrative accounts.

**Operational Procedures**: Offers structured daily, weekly, and monthly administrative tasks with specific AWS CLI commands for routine security checks, compliance monitoring, and administrative reporting.

**Decommissioning Framework**: Outlines comprehensive account closure procedures including data retention requirements, resource inventory and transfer processes, dependency analysis, and post-decommissioning validation steps.

**Emergency Response**: Details incident response procedures for account compromise scenarios, emergency access activation processes, and recovery workflows with proper approval mechanisms and audit trails.

**Access Control and Governance**: Describes role-based access control matrix with defined approval workflows for standard changes, elevated privilege operations, and emergency access scenarios using [IAM best practices](../../../iam/latest/userguide/best-practices.md "../../../iam/latest/userguide/best-practices.md").

**FedRAMP Compliance Considerations**: Provides guidance for continuous monitoring requirements through automated evidence collection, [audit trail management](../../../cloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../cloudtrail/latest/userguide/cloudtrail-user-guide.md") with 7-year retention, and real-time compliance reporting considerations for FedRAMP assessments.

This guidance presents AWS recommended approaches for transforming traditional AWS account management from a credential-based approach to a modern, centralized, and auditable framework that supports FedRAMP Rev5 requirements while helping to reduce security risks and operational complexity. Organizations may use these recommendations to help achieve enhanced security posture, simplified compliance reporting, and streamlined administrative operations across their AWS environment.

## AWS Administrative Account Types and Naming Conventions

### Account Type Hierarchy

This section defines the four primary types of AWS accounts in an organization and their specific purposes, naming conventions, and administrative scope.

**Management Account (Organization Root)**:

- **Purpose**: Central control point for AWS Organizations
- **Naming Convention**: `[org-name]-management-[environment]` (e.g., `acme-management-prod`)
- **Account ID Reference**: 12-digit unique identifier (e.g., `123456789012`)
- **Administrative Scope**: Full organizational control, billing consolidation, service control policies

**Security Account (Audit/Log Archive)**:

- **Purpose**: Centralized security logging and compliance monitoring
- **Naming Convention**: `[org-name]-security-[function]` (e.g., `acme-security-audit`)
- **Administrative Scope**: CloudTrail log aggregation, AWS Config compliance, Security Hub findings

**Shared Services Account**:

- **Purpose**: Common infrastructure services (DNS, Active Directory, monitoring)
- **Naming Convention**: `[org-name]-shared-[service]` (e.g., `acme-shared-network`)
- **Administrative Scope**: Cross-account resource sharing, centralized services

**Workload Accounts (Member Accounts)**:

- **Purpose**: Application and service hosting
- **Naming Convention**: `[org-name]-[workload]-[environment]` (e.g., `acme-webapp-prod`)
- **Administrative Scope**: Application-specific resources and permissions

### Administrative Role Naming Standards

This section establishes consistent naming patterns for administrative roles across AWS accounts, including both AWS-managed and custom roles.

**Cross-Account Administrative Roles**:

- **OrganizationAccountAccessRole**: Default cross-account access role created by AWS Organizations
- **AWSControlTowerExecution**: AWS Control Tower service role for governance
- **AWSServiceRoleFor[ServiceName]**: Service-linked roles for AWS services

**Custom Administrative Roles**:

- **Naming Pattern**: `[Function]-[Scope]-[Environment]Role`
- **Examples**:
  - `SecurityAdmin-Organization-ProdRole`
  - `NetworkAdmin-Account-DevRole`
  - `ComplianceAuditor-ReadOnly-AllRole`

### Account Reference Methods

This section explains the various ways to identify and reference AWS accounts in different contexts, from console navigation to programmatic access.

**AWS Console Navigation**:

- Account Switcher: Displays account name and ID
- Organization view: Shows account hierarchy and organizational units
- Billing console: Lists all accounts with names and IDs

**Programmatic Access**:

- AWS CLI: Use account ID or account alias for cross-account operations
- AWS APIs: Reference accounts by 12-digit account ID
- CloudFormation: Use account ID in cross-account resource references

## AWS Root Account Security Architecture

### AWS Organizations Root Access Management (Recommended)

This section describes AWS’s modern approach to root account management that eliminates long-term credentials while maintaining necessary administrative capabilities.

**FedRAMP Impact**: Eliminates long-term root credentials, helping to reduce potential security exposure and supporting better credential management practices.

**Central Management of Root Credentials**:

**AWS Organizations now provides centralized root access management that addresses longstanding security challenges**

- **Remove Long-term Root Credentials**: Programmatically eliminate root user passwords, access keys, and signing certificates from member accounts
- **Prevent Credential Recovery**: Block unauthorized recovery of root credentials, supporting secure credential management
- **Secure-by-Default Provisioning**: Create new AWS accounts without root credentials from inception, supporting streamlined security configuration
- **Compliance Visibility**: Centralized discovery and monitoring of root credential status across all organization accounts

**Root Sessions for Privileged Operations**:
**When root-level access is required, AWS Organizations provides temporary, task-scoped access through root sessions**

- **Auditing Root User Credentials**: Read-only access to review root user information and security posture
- **Re-enabling Account Recovery**: Restore account recovery capabilities without requiring long-term root credentials
- **Deleting Root User Credentials**: Remove console passwords, access keys, signing certificates, and MFA devices
- **Unlocking S3 Bucket Policies**: Edit or delete S3 bucket policies that deny all principals (emergency access)
- **Unlocking SQS Queue Policies**: Edit or delete Amazon SQS resource policies that deny all principals

## Implementation Commands

###### Important

The commands below are provided as samples for how to enable and leverage the features in AWS. Review all commands and adjust as needed for your organization and use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS service specific documentation before implementation.

**Enable Organizations Root Access Management**:

To enable organization root access management in AWS, you must first enable the necessary service access and then configure the root access management features. This process eliminates long-term root credentials while maintaining necessary administrative capabilities.

**Prerequisites**:

- You must be signed in as the management account root user or have appropriate IAM permissions
- Your AWS Organization must already be created
- You need the `organizations:EnableAWSServiceAccess` permission

**Step 1: Enable AWS SSO service access**:

```
aws organizations enable-aws-service-access --service-principal sso.amazonaws.com
```

**Step 2: Enable additional organization services (recommended)**:

```
# Enable AWS Config service access
aws organizations enable-aws-service-access --service-principal config.amazonaws.com

# Enable AWS CloudTrail service access
aws organizations enable-aws-service-access --service-principal cloudtrail.amazonaws.com
```

**Step 3: Enable IAM service access in Organizations**:

```
aws organizations enable-aws-service-access --service-principal iam.amazonaws.com
```

**Enable root credentials management**:

```
# Note: Root access management is configured through the AWS Organizations console
# Navigate to AWS Organizations > Settings > Root access management
# This cannot be enabled via CLI at this time
```

**Enable root sessions capability**:

```
# Note: Root sessions are configured through the AWS Organizations console
# Navigate to AWS Organizations > Settings > Root access management
# This cannot be enabled via CLI at this time
```

**Obtain Temporary Root Access**:

Request temporary root credentials for specific task

```
# Note: Root sessions must be initiated through the AWS Organizations console
# Navigate to AWS Organizations > Accounts > Select account > Root access
# CLI access for root sessions is not currently available
```

**Credentials are valid for 15 minutes maximum and can be used to perform necessary actions.**
Use returned AccessKeyId, SecretAccessKey, and SessionToken

### Traditional Root Account Security (Legacy Approach)

This section covers security practices for standalone accounts or organizations not yet implementing centralized root management.

**Use Case**: Standalone accounts or organizations not yet implementing centralized root management

Root Account Hardening Requirements

**Multi-Factor Authentication (MFA)**: Hardware security key (FIDO2/WebAuthn) or virtual MFA device required

**Access Key Elimination**: Delete all root account access keys immediately after account creation

**Strong Password Policy**: Minimum 14 characters with complexity requirements

**Account Contact Information**: Secure, monitored email address with restricted access

**Security Questions**: Unique, non-guessable answers stored securely

Root Account Usage Restrictions

**Root account access should be limited to these specific scenarios**:

Initial account setup and MFA configuration
Billing and account management tasks that cannot be delegated
Recovery scenarios when standard IAM access is unavailable
Specific AWS services that require root account permissions
Account closure and decommissioning
Administrative Account Hierarchy

### AWS Organizations Management Account

This section details the security requirements and configuration for the central management account in an AWS Organization.

**Purpose**: Central control point for multi-account AWS environments

**Security Requirements**:

Implement centralized root access management
Enable AWS CloudTrail organization trail with log file validation
Configure AWS Config organization-wide rules
Implement Service Control Policies (SCPs) for security guardrails
Enable AWS Security Hub for centralized security findings

#### AWS IAM Identity Center (Successor to AWS SSO)

**Purpose**: Centralized workforce identity management and federated access

**Security Configuration**:

Enable MFA for all users with hardware tokens or authenticator apps
Configure session duration limits (maximum 12 hours for FedRAMP)
Implement permission sets based on job functions and least privilege
Enable audit logging and integrate with SIEM systems
Configure external identity provider integration (SAML 2.0/OIDC)

#### AWS Control Tower Landing Zone

**Purpose**: Automated governance and compliance for multi-account environments

**Security Guardrails**:

**Mandatory guardrails**: CloudTrail enabled, access logging configured

**Strongly recommended**: MFA for root users, S3 bucket public access blocked

**Elective guardrails**: Additional security controls based on compliance requirements

#### Service-Level Administrative Accounts

**Database Administrative Accounts**:

**Applicable Services**: Amazon RDS, Amazon Aurora, Amazon ElastiCache, Amazon DocumentDB, Amazon Neptune

**Security Requirements**:

**Primary User Credentials**: Store in AWS Secrets Manager with automatic rotation

**Database Authentication**: Implement IAM database authentication where supported

**Network Security**: Deploy in private subnets with security group restrictions

**Encryption**: Enable encryption at rest and in transit for all database instances

**Audit Logging**: Enable database audit logs and forward to CloudWatch Logs

**Implementation Example (RDS)**:

```
# Create RDS instance with IAM authentication
aws rds create-db-instance \
    --db-instance-identifier mydb-instance \
    --db-instance-class db.t3.micro \
    --engine mysql \
    --master-username admin \
    --manage-master-user-password \
    --master-user-secret-kms-key-id alias/aws/rds \
    --enable-iam-database-authentication \
    --storage-encrypted \
    --kms-key-id alias/aws/rds
```

#### Container Administrative Access

This section provides guidance for managing administrative access to containerized workloads on AWS services like EKS, ECS, and Fargate.

**Applicable Services**: Amazon EKS, Amazon ECS, AWS Fargate

**EKS Cluster Administrative Access**:

- **Cluster Authentication**: Use IAM roles for service accounts (IRSA)
- **RBAC Configuration**: Implement Kubernetes role-based access control
- **Pod Security**: Enable Pod Security Standards and admission controllers
- **Network Policies**: Implement Kubernetes network policies for micro-segmentation
- **Audit Logging**: Enable EKS control plane logging to CloudWatch

## Administrative Account Configuration Management

### Configuration Baselines

This section describes how to establish and maintain consistent security configurations across all administrative accounts using AWS Config and Service Control Policies.

**AWS Config Organization Rules**:

Establish organization-wide configuration compliance rules for administrative accounts

```
# Deploy organization-wide Config rule for root account MFA
aws configservice put-organization-config-rule \
    --organization-config-rule-name "org-root-mfa-enabled" \
    --organization-managed-rule-metadata \
        RuleIdentifier=ROOT_MFA_ENABLED,Description="Checks whether MFA is enabled for root account"
```

**Service Control Policies (SCPs)**:

Implement preventive guardrails for administrative account security

```
# Create SCP to prevent root account usage
aws organizations create-policy \
    --name "PreventRootAccountUsage" \
    --description "Deny root account actions except emergency scenarios" \
    --type SERVICE_CONTROL_POLICY \
    --content '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Deny",
                "Principal": {
                    "AWS": "*"
                },
                "Action": "*",
                "Resource": "*",
                "Condition": {
                    "StringEquals": {
                        "aws:PrincipalType": "Root"
                    },
                    "StringNotEquals": {
                        "aws:RequestedRegion": ["us-east-1", "us-west-2"]
                    }
                }
            }
        ]
    }'
```

#### Configuration Drift Detection

This section explains how to monitor and detect unauthorized changes to administrative account configurations using AWS Config and Systems Manager.

**AWS Config Compliance Monitoring**:

```
# Get compliance status for administrative accounts
aws configservice get-compliance-details-by-config-rule \
    --config-rule-name "root-mfa-enabled" \
    --compliance-types NON_COMPLIANT
```

**AWS Systems Manager Compliance**:

```
# Create compliance association for administrative instances
aws ssm create-association \
    --name "AWS-GatherSoftwareInventory" \
    --targets "Key=tag:AccountType,Values=Administrative"
```

## Daily Operations and Maintenance

### Routine Administrative Tasks

This section outlines structured schedules for security checks, compliance activities, and administrative reviews to maintain ongoing security posture.

**Daily Security Checks**:

- Review CloudTrail logs for root account activity
- Verify MFA status for all administrative users
- Check AWS Config compliance dashboard
- Monitor Security Hub findings for important security issues

**Weekly Administrative Reviews**:

- Audit IAM user and role permissions
- Review AWS Trusted Advisor security recommendations
- Validate backup and recovery procedures
- Update security group and NACL rules as needed

**Monthly Compliance Activities**:

- Generate compliance reports for FedRAMP assessments
- Review and update administrative procedures
- Conduct access reviews for administrative accounts
- Test incident response procedures

### Administrative Task Commands

This section provides specific AWS CLI commands for generating reports and monitoring administrative account activities.

**Generate Administrative Access Report**:

```
# List all administrative users and their last activity
aws iam generate-credential-report
aws iam get-credential-report --query 'Content' --output text | base64 -d > credential-report.csv
```

**Review Root Account Activity**:

```
# Query CloudTrail for root account usage in last 30 days
aws logs filter-log-events \
    --log-group-name "CloudTrail/RootAccountActivity" \
    --start-time $(date -d '30 days ago' +%s)000 \
    --filter-pattern '{ $.userIdentity.type = "Root" }'
```

## Account Decommissioning Procedures

### Pre-Decommissioning Requirements

This section covers the essential steps that must be completed before closing an AWS account, including data backup and dependency analysis.

**Data Retention and Backup**:

- Export all CloudTrail logs to long-term storage
- Backup AWS Config configuration history
- Archive Security Hub findings and compliance reports
- Export billing and usage reports for audit purposes

**Resource Inventory and Transfer**:

```
# List all resources in account before decommissioning
aws resourcegroupstaggingapi get-resources \
    --resources-per-page 100 \
    --output table
```

**Dependency Analysis**:

- Identify cross-account resource dependencies
- Document shared services and integrations
- Review IAM cross-account trust relationships
- Catalog DNS and network dependencies

### Decommissioning Steps

This section provides the step-by-step process for safely closing AWS accounts while maintaining compliance records and documentation.

**Step 1: Remove from AWS Organizations**:

```
# Remove account from organization (if member account)
aws organizations remove-account-from-organization \
    --account-id 123456789012
```

**Step 2: Close AWS Account**:

```
# Note: Account closure must be done through the AWS Console
# 1. Sign in as root user to the account being closed
# 2. Navigate to Account Settings in the AWS Console
# 3. Scroll to "Close Account" section
# 4. Follow the account closure process
# CLI account closure is not available
```

**Step 3: Update Documentation**:

- Remove account from organizational charts
- Update network diagrams and architecture documentation
- Archive administrative procedures and runbooks
- Update compliance documentation and evidence

### Post-Decommissioning Validation

This section describes how to verify successful account closure and maintain required compliance documentation after decommissioning.

**Verify Account Closure**:

```
# Verify account is no longer accessible
aws organizations list-accounts \
    --query 'Accounts[?Id==`123456789012`]'
```

**Compliance Record Keeping**:

- Maintain decommissioning records for audit purposes
- Archive final compliance reports and assessments
- Document lessons learned and process improvements
- Update incident response procedures if needed
  == Monitoring and Compliance

### CloudTrail Configuration

This section explains how to set up comprehensive audit logging for administrative account activities using AWS CloudTrail.

**Root Account Activity Monitoring**:

```
# Create CloudTrail for root account monitoring
aws cloudtrail create-trail \
    --name root-account-trail \
    --s3-bucket-name security-audit-logs \
    --include-global-service-events \
    --is-multi-region-trail \
    --enable-log-file-validation \
    --event-selectors '[{
        "ReadWriteType": "All",
        "IncludeManagementEvents": true,
        "DataResources": []
    }]'
```

### Real-time Alerting

This section covers setting up automated alerts for suspicious or unauthorized administrative account activities using CloudWatch.

**CloudWatch Alarms for Root Account Usage**:

```
# Create metric filter for root account usage
aws logs put-metric-filter \
    --log-group-name CloudTrail/RootAccountActivity \
    --filter-name RootAccountUsage \
    --filter-pattern '{ $.userIdentity.type = "Root" }' \
    --metric-transformations \
        metricName=RootAccountUsageCount,metricNamespace=Security/RootAccount,metricValue=1
```

## Emergency Procedures

### Root Account Compromise Response

This section provides response procedures for suspected or confirmed compromise of root account credentials.

**Initial Response Actions**:

1. Change root account password as soon as possible
2. Disable or rotate all access keys
3. Review and update MFA devices
4. Verify AWS CloudTrail is active and collecting logs
5. Contact AWS Support for assistance if needed

**Investigation**:

- Review CloudTrail logs for unusual activities
- Check AWS Config for configuration changes
- Analyze VPC Flow Logs for network anomalies
- Review IAM policy changes and user creations

**Recovery**:

- Consider implementing AWS Organizations root access management
- Remove long-term root credentials where possible
- Update incident response procedures based on lessons learned
- Conduct security assessment and review

### Emergency Access Procedures

This section details how to activate emergency access to administrative accounts during security incidents or system failures.

**Emergency Access Activation**:

```
# Assume emergency access role (pre-configured)
aws sts assume-role \
    --role-arn "arn:aws:iam:ACCOUNT-ID:role/EmergencyAccessRole" \
    --role-session-name "emergency-$(date +%Y%m%d-%H%M%S)"
```

**Emergency Root Session Request**:

```
# Note: Emergency root access must be requested through AWS Organizations console
# 1. Navigate to AWS Organizations > Accounts
# 2. Select the target account
# 3. Choose "Root access"
# 4. Select appropriate task policy and provide justification
# 5. Complete the root session request process
# CLI-based root session requests are not currently available
```

## Access Control Matrix and Approval Workflows

### Role-Based Access Permissions

This section defines the different administrative roles, their access levels, approval requirements, and permitted actions in a structured matrix format.

| Administrative Role        | Access Level       | Approval Required             | Permitted Actions                                           |
| -------------------------- | ------------------ | ----------------------------- | ----------------------------------------------------------- |
| Organization Administrator | Full               | Dual approval + CISO          | All organization-level operations, account creation/closure |
| Security Administrator     | Security-focused   | Security team lead            | Security service configuration, compliance monitoring       |
| Network Administrator      | Network-focused    | Infrastructure lead           | VPC, routing, DNS, load balancer management                 |
| Compliance Auditor         | Read-only          | Compliance manager            | Audit log access, compliance report generation              |
| Emergency Responder        | Temporary elevated | Incident commander + Security | Emergency access during security incidents                  |

### Approval Workflow Requirements

This section establishes the approval processes required for different types of administrative changes, from routine updates to emergency access.

**Standard Administrative Changes**:

- Single approver from appropriate team lead
- Change request documentation required
- Automated testing in non-production first

**Elevated Privilege Operations**:

- Dual approval required (requestor + approver)
- Business justification documented
- Time-limited access (maximum 4 hours)

**Emergency Access**:

- Incident commander approval
- Real-time notification to security team
- Post-incident review within 24 hours recommended

## FedRAMP Continuous Monitoring Requirements

### Evidence Collection and Reporting

This section describes how to automate the collection of compliance evidence and generate reports required for FedRAMP assessments.

**Monthly Compliance Reports**:

```
# Generate AWS Config compliance summary
aws configservice get-compliance-summary-by-config-rule \
    --output table > monthly-config-compliance.txt

# Export Security Hub findings
aws securityhub get-findings \
    --filters '{"ComplianceStatus":[{"Value":"FAILED","Comparison":"EQUALS"}]}' \
    --output json > monthly-security-findings.json
```

**Continuous Monitoring Automation**:

```
# Create EventBridge rule for real-time compliance monitoring
aws events put-rule \
    --name "FedRAMP-ComplianceMonitoring" \
    --event-pattern '{
        "source": ["aws.config"],
        "detail-type": ["Config Rules Compliance Change"],
        "detail": {
            "newEvaluationResult": {
                "complianceType": ["NON_COMPLIANT"]
            }
        }
    }'
```

### Audit Trail Requirements

This section covers the configuration of audit logging systems to meet FedRAMP requirements for log retention and cross-account aggregation.

**Log Retention Configuration**:

```
# Set CloudTrail log retention to 7 years for FedRAMP
aws logs put-retention-policy \
    --log-group-name "CloudTrail/FedRAMP-AuditLogs" \
    --retention-in-days 2557  # 7 years
```

**Cross-Account Log Aggregation**:

```
# Create organization-wide CloudTrail
aws cloudtrail create-trail \
    --name "FedRAMP-OrganizationTrail" \
    --s3-bucket-name "fedramp-audit-logs-bucket" \
    --is-organization-trail \
    --enable-log-file-validation \
    --include-global-service-events
```

## Compliance Validation

### AWS Config Rules for Root Account Security

This section provides specific AWS Config rules for monitoring and enforcing security requirements on root accounts across the organization.

```
# Deploy Config rule for root account MFA
aws configservice put-config-rule \
    --config-rule '{
        "ConfigRuleName": "root-mfa-enabled",
        "Source": {
            "Owner": "AWS",
            "SourceIdentifier": "ROOT_MFA_ENABLED"
        }
    }'
```

```
# Deploy Config rule for root account access key check
aws configservice put-config-rule \
    --config-rule '{
        "ConfigRuleName": "root-access-key-check",
        "Source": {
            "Owner": "AWS",
            "SourceIdentifier": "ROOT_ACCESS_KEY_CHECK"
        }
    }'
```

## Best Practices Summary

**Administrative Account Management**:

- Consider implementing AWS Organizations root access management for centralized, secure root account control
- Eliminate long-term root credentials in favor of temporary, task-scoped access
- Use standardized naming conventions for accounts and administrative roles
- Maintain clear documentation of account hierarchy and administrative responsibilities

**Security and Compliance**:

- Enable comprehensive logging and monitoring for all administrative account activities
- Implement least privilege access through IAM roles and policies with time-limited sessions
- Use AWS managed services for credential management and rotation
- Consider establishing automated compliance monitoring and real-time alerting for policy violations

**Operational Excellence**:

- Regularly audit and review administrative account usage and permissions
- Maintain incident response procedures for account security scenarios
- Implement proper change management processes for administrative account modifications
- Conduct regular testing of emergency access procedures and account recovery processes

**FedRAMP Compliance Considerations**:

- Maintain audit trails with appropriate retention periods (7 years minimum recommended)
- Generate regular compliance reports and evidence collection as required by your organization
- Consider implementing continuous monitoring for security and compliance posture
- Document all administrative procedures and maintain version control

**Important Note**: This guidance provides AWS recommended practices and considerations. Organizations are responsible for evaluating these recommendations against their specific compliance requirements and implementing appropriate controls to meet their regulatory obligations.

## Additional Resources

**AWS Documentation References**:

- [AWS Organizations User Guide](organizations/latest/userguide/orgs_introduction.md "organizations/latest/userguide/orgs_introduction.md")
- [IAM Best Practices](iam/latest/userguide/best-practices.md "iam/latest/userguide/best-practices.md")
- [AWS Control Tower User Guide](controltower/latest/userguide/what-is-control-tower.md "controltower/latest/userguide/what-is-control-tower.md")
- [AWS Security Hub User Guide](securityhub/latest/userguide/what-is-securityhub.md "securityhub/latest/userguide/what-is-securityhub.md")

**FedRAMP Resources**:

- [FedRAMP Security Controls Baseline](https://www.fedramp.gov/assets/resources/documents/FedRAMP_Security_Controls_Baseline.xlsx "https://www.fedramp.gov/assets/resources/documents/FedRAMP_Security_Controls_Baseline.xlsx")
- [FedRAMP OSCAL Profile](https://www.fedramp.gov/assets/resources/templates/FedRAMP_OSCAL_Based_FedRAMP_High_Baseline_Profile.json "https://www.fedramp.gov/assets/resources/templates/FedRAMP_OSCAL_Based_FedRAMP_High_Baseline_Profile.json")
