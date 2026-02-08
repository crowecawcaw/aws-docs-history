# Privileged Account Guidance

This guide provides security configuration for privileged account access.

**Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

**Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## Document Information

|              |            |
| ------------ | ---------- |
| Version      | 1.0.0      |
| Last Updated | 2026-01-09 |

## FedRAMP Requirements

## FRR-RSC-03: Privileged Accounts Guidance

✓ SHOULD - Recommended for all FedRAMP services

**OSCAL Control ID: FRR-RSC-03**
**UUID: frr-rsc-03-control**

### Requirement

Providers SHOULD create and maintain guidance that explains security-related settings that can be operated only by privileged accounts and their security implications.

### Component Implementation (OSCAL)

**Component UUID**: iam-privileged-component-003

**Component Type**: Account

**Control Implementation**: AC-2 (Account Management), AC-3 (Access Enforcement), AC-6 (Least Privilege), IA-2 (Identification and Authentication), IA-5 (Authenticator Management)

**Implementation Status**: Implemented

## Executive Summary

This guidance provides AWS recommended practices for managing privileged accounts and security-related settings that require elevated permissions in AWS environments. Privileged accounts control critical security configurations and require enhanced controls, monitoring, and governance to support FedRAMP compliance considerations. This guidance demonstrates how to implement granular privilege delegation by use case categories, helping organizations avoid broad administrative roles and reduce potential security impact.

This document covers security-related settings that can only be operated by privileged accounts, their security implications, and recommended implementation approaches. Key areas include AWS Organizations Service Control Policies, cross-account trust relationships, encryption key management, and organization-wide security service configuration.

The term "account: in these guides is not an isolated AWS account, but rather a pattern of usage and application to segregation of duties as applied to users in AWS. These are typically assigned via Users, Groups or roles.

**Key Coverage Areas**:

**Privileged Account Classification**: Defines security, network, infrastructure, and database administration account types with specific responsibilities and risk levels.

**Privileged-Only Security Settings**: Explains AWS configurations that require privileged access, including Service Control Policies, organization-wide security services, and cross-account trust relationships.

**Security Implications Analysis**: Details the blast radius, recovery complexity, and compliance considerations for each privileged setting.

**Access Management Framework**: Provides just-in-time access, break-glass procedures, and comprehensive monitoring for privileged operations.

**Compliance and Governance**: Offers automated compliance checking, regular access reviews, and incident response integration for privileged account management.

## Privileged Account Classification

This section defines the primary types of privileged accounts in AWS environments, their specific responsibilities, risk levels, and security requirements. The examples below provide an approach that provides segregation of duties, but would also apply to any user granted the AWS Managed Administrator policy that has unrestricted access to AWS resources.

### Security Administration Accounts

This subsection covers accounts responsible for managing security services, policies, and compliance configurations across AWS environments.

**Purpose**: Manage security services, policies, and compliance configurations

**Risk Level**: Critical - Can modify security controls and access policies

**Responsibilities and Permissions**:

- **AWS IAM Management**: Create, modify, and delete IAM users, roles, and policies
- **AWS CloudTrail**: Configure audit logging, modify trail settings, and manage log integrity
- **AWS Config**: Deploy and manage configuration rules, remediation actions, and compliance reporting
- **AWS Security Hub**: Manage security findings, configure integrations, and customize standards
- **Amazon GuardDuty**: Configure threat detection, manage findings, and set up automated responses
- **AWS KMS**: Manage encryption keys, key policies, and cryptographic operations

**Security Requirements**

- **Multi-Factor Authentication**: Hardware security keys (FIDO2) required for all security admin accounts
- **Session Duration**: Maximum 4-hour session duration with re-authentication required
- **IP Restrictions**: Access limited to corporate, trusted network ranges and approved VPN endpoints
- **Time-based Access**: Consider restricting access to business hours unless emergency procedures are invoked

**Example IAM Policy (Security Administrator)**:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:*",
        "cloudtrail:*",
        "config:*",
        "securityhub:*",
        "guardduty:*",
        "kms:*",
        "organizations:List*",
        "organizations:Describe*"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        },
        "NumericLessThan": {
          "aws:MultiFactorAuthAge": "14400"
        },
        "IpAddress": {
          "aws:SourceIp": [
            "203.0.113.0/24",
            "198.51.100.0/24"
          ]
        }
      }
    }
  ]
}
```

### Network Administration Accounts

This subsection covers accounts responsible for managing network infrastructure, connectivity, and network security controls.

**Purpose**: Manage network infrastructure, connectivity, and security controls
**Risk Level**: High - Can modify network security controls and connectivity

**Responsibilities and Permissions**:

- **Amazon VPC**: Create and modify VPCs, subnets, route tables, and network ACLs
- **Security Groups**: Configure firewall rules and network access controls
- **AWS Direct Connect**: Manage dedicated network connections and virtual interfaces
- **AWS Transit Gateway**: Configure inter-VPC and on-premises connectivity
- **AWS Network Firewall**: Deploy and manage stateful network security controls
- **Amazon Route 53**: Manage DNS configurations and health checks

**Security Controls**:

- **Change Management**: All network changes require approval through formal change control process
- **Backup Configurations**: Automated backup of network configurations before changes
- **Testing Requirements**: Network changes must be tested in non-production environments first
- **Rollback Procedures**: Documented rollback procedures for all network modifications

### Infrastructure Administration Accounts

This subsection covers accounts responsible for managing compute resources, storage, and system-level configurations.

**Purpose**: Manage compute resources, storage, and system-level configurations
**Risk Level**: High - Can access and modify system resources and data

**Responsibilities and Permissions**:

- **Amazon EC2**: Launch, terminate, and modify EC2 instances and associated resources
- **Amazon EBS**: Create, attach, and manage encrypted storage volumes
- **AWS Systems Manager**: Execute commands, manage patches, and configure systems
- **Amazon CloudWatch**: Configure monitoring, alarms, and log management
- **AWS Lambda**: Deploy and manage serverless functions and execution roles
- **Amazon S3**: Manage storage buckets, objects, and access policies

**Privileged Access Management**:

- **Session Manager**: Use AWS Systems Manager Session Manager for secure shell access
- **Instance Profiles**: Assign minimal IAM roles to EC2 instances based on function
- **Encryption Requirements**: All storage volumes and S3 buckets must use AWS KMS encryption
- **Audit Logging**: Enable detailed CloudTrail logging for all system administration activities

### Database Administration Accounts

This subsection covers accounts responsible for managing database services, configurations, and access controls with direct access to sensitive data.

**Purpose**: Manage database services, configurations, and access controls
**Risk Level**: Critical - Direct access to sensitive data and database configurations

**Database Services Coverage**

- **Amazon RDS**: Relational database management (MySQL, PostgreSQL, Oracle, SQL Server)
- **Amazon Aurora**: High-performance managed database clusters
- **Amazon DynamoDB**: NoSQL database management and configuration
- **Amazon ElastiCache**: In-memory caching services (Redis, Memcached)
- **Amazon DocumentDB**: MongoDB-compatible document database
- **Amazon Neptune**: Graph database for connected data applications

**Enhanced Security Controls**

- **Database Authentication**: Use IAM database authentication where supported
- **Credential Management**: Store master credentials in AWS Secrets Manager with automatic rotation
- **Network Isolation**: Deploy databases in private subnets with restrictive security groups
- **Encryption at Rest**: Enable encryption for all database instances using customer-managed KMS keys
- **Encryption in Transit**: Force SSL/TLS connections for all database communications
- **Audit Logging**: Enable database audit logs and forward to CloudWatch Logs

**Example RDS Configuration with Enhanced Security**

**Create RDS instance with comprehensive security controls**

```
aws rds create-db-instance \
  --db-instance-identifier secure-db-instance \
  --db-instance-class db.r5.large \
  --engine postgres \
  --engine-version 13.7 \
  --master-username dbadmin \
  --manage-master-user-password \
  --master-user-secret-kms-key-id alias/rds-secrets \
  --allocated-storage 100 \
  --storage-type gp3 \
  --storage-encrypted \
  --kms-key-id alias/rds-encryption \
  --vpc-security-group-ids sg-12345678 \
  --db-subnet-group-name private-db-subnet-group \
  --backup-retention-period 30 \
  --backup-window "03:00-04:00" \
  --maintenance-window "sun:04:00-sun:05:00" \
  --enable-performance-insights \
  --performance-insights-kms-key-id alias/rds-performance \
  --enable-cloudwatch-logs-exports postgresql \
  --deletion-protection \
  --copy-tags-to-snapshot
```

## Privileged-Only Security Settings

This section explains AWS security-related settings that can only be operated by privileged accounts, their security implications, and recommended management approaches.

### AWS Organizations Service Control Policies

This subsection covers organization-wide policy controls that can only be managed by privileged accounts in the management account.

**Security Significance**: Service Control Policies act as guardrails for all accounts in the organization and can prevent or allow specific AWS service actions across the entire organization.

**Privileged-Only Operations**

- Create and modify Service Control Policies at the organization level
- Attach SCPs to organizational units or individual member accounts
- Enable and disable AWS service access organization-wide
- Manage policy inheritance hierarchy and precedence rules
- Configure policy exceptions and exemptions for specific accounts

**Security Implications**

- **Immediate Impact**: SCP changes take effect immediately across all affected accounts
- **Blast Radius**: Can affect hundreds or thousands of accounts simultaneously
- **Recovery Complexity**: Overly restrictive SCPs may require root account access to resolve
- **Compliance Considerations**: SCP changes may affect FedRAMP boundary definitions and control implementations

**Implementation Requirements**

- Formal change management process for all SCP modifications
- Testing in non-production organizational units before production deployment
- Documentation of business justification for policy changes
- Rollback procedures and emergency access protocols

**Create Service Control Policy with security guardrails**:

The example policy uses a sample IAM role of SecurityAdministratorRole to indicate you organizations security administrtor role that has far reaching access to your org. EmergencyAccessRole is a role your organization can adopt as a break-glass mechanism for access to AWS. AWS recommends implementing a break-glass mechanism to your AWS accounts in case of emergencies. Please read more in the [AWS DevOps Guidance docs](../../../wellarchitected/latest/devops-guidance/ag.sad.md "../../../wellarchitected/latest/devops-guidance/ag.sad.md")

```
aws organizations create-policy \
  --name "SecurityGuardrails-SCP" \
  --description "Prevent high-risk security actions" \
  --type SERVICE_CONTROL_POLICY \
  --content '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Deny",
        "Action": [
          "iam:DeleteRole",
          "iam:DeletePolicy",
          "cloudtrail:StopLogging",
          "cloudtrail:DeleteTrail",
          "config:DeleteConfigRule",
          "guardduty:DeleteDetector"
        ],
        "Resource": "*",
        "Condition": {
          "StringNotEquals": {
            "aws:PrincipalArn": [
              "arn:aws:iam:*:role/SecurityAdministratorRole",
              "arn:aws:iam:*:role/EmergencyAccessRole"
            ]
          }
        }
      }
    ]
  }'
```

### Cross-Account Trust Relationships

This subsection covers IAM trust policies that enable cross-account access and can only be established by privileged accounts.

**Security Significance**: Cross-account trust relationships enable resource sharing and centralized management but can create security vulnerabilities if misconfigured.

**Privileged-Only Operations**:

- Create and modify IAM role trust policies for cross-account access
- Establish trust relationships between AWS Organizations accounts
- Configure external account trust for third-party integrations
- Manage assume role permissions and conditions

**Security Implications**:

- **Immediate Impact**: Trust policy changes can immediately grant or revoke cross-account access
- **Blast Radius**: Affects security boundaries between AWS accounts
- **Recovery Complexity**: Broken trust relationships may require coordination across multiple accounts
- **Compliance Considerations**: Cross-account access must align with data classification and access control requirements

**Create secure cross-account trust relationship**

In this example the important factor is the ExternalID IAM condition that limits access to assume the role to only accounts that are allowed and provide the unique external ID.

```
aws iam create-role \
  --role-name CrossAccountSecurityRole \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam:TRUSTED-ACCOUNT-ID:root"
        },
        "Action": "sts:AssumeRole",
        "Condition": {
          "StringEquals": {
            "sts:ExternalId": "unique-external-id"
          },
          "Bool": {
            "aws:MultiFactorAuthPresent": "true"
          },
          "NumericLessThan": {
            "aws:MultiFactorAuthAge": "3600"
          }
        }
      }
    ]
  }'
```

### AWS KMS Key Policies and Administrative Access

This subsection covers encryption key management operations that require privileged access to maintain data security.

**Security Significance**: KMS key policies control access to encryption keys that protect sensitive data across AWS services.

**Privileged-Only Operations**

- Create and modify KMS key policies and administrative permissions
- Enable and disable encryption keys for data protection
- Configure key rotation policies and schedules
- Manage cross-account key access and sharing
- Grant and revoke key usage permissions for AWS services

**Security Implications**

- **Immediate Impact**: Key policy changes can immediately affect data access across multiple services
- **Blast Radius**: Can impact encrypted data in S3, EBS, RDS, and other AWS services
- **Recovery Complexity**: Incorrect key policies may cause data access issues requiring emergency procedures
- **Compliance Considerations**: Key management changes must maintain encryption requirements for sensitive data

**Create KMS key with comprehensive administrative controls**

```
aws kms create-key \
  --description "Privileged access encryption key" \
  --key-usage ENCRYPT_DECRYPT \
  --key-spec SYMMETRIC_DEFAULT \
  --policy '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "KeyAdministration",
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam:ACCOUNT-ID:role/KMSAdministratorRole"
        },
        "Action": [
          "kms:Create*",
          "kms:Describe*",
          "kms:Enable*",
          "kms:List*",
          "kms:Put*",
          "kms:Update*",
          "kms:Revoke*",
          "kms:Disable*",
          "kms:Get*",
          "kms:Delete*",
          "kms:ScheduleKeyDeletion",
          "kms:CancelKeyDeletion"
        ],
        "Resource": "*"
      }
    ]
  }'
```

### Organization-Wide Security Service Configuration

This subsection covers AWS security services that can only be configured at the organization level by management account privileged users.

**Security Significance**: Organization-wide security services provide centralized visibility and control but require careful configuration to avoid service disruptions. Being able to aggregate and delgate these service can help you to centralize your AWS security services and limit access to one AWS account only.

**Privileged-Only Operations**:

- Configure AWS Security Hub master account and member account aggregation
- Set up AWS Config organization aggregators and compliance rules
- Establish AWS CloudTrail organization trails with cross-account logging
- Configure Amazon GuardDuty master account and threat intelligence sharing
- Manage AWS Access Analyzer organization-wide findings

**Security Implications**:

- **Immediate Impact**: Configuration changes affect security monitoring across all organization accounts
- **Blast Radius**: Can impact compliance reporting and security incident detection organization-wide
- **Recovery Complexity**: Service misconfigurations may require coordination across multiple security teams
- **Compliance Considerations**: Changes must maintain continuous monitoring requirements for FedRAMP compliance

**Enable Security Hub organization-wide with compliance standards**

```
# Enable Security Hub in management account
aws securityhub enable-security-hub \
  --enable-default-standards

# Create organization configuration
aws securityhub create-configuration-policy \
  --name "OrganizationSecurityPolicy" \
  --description "Organization-wide security configuration" \
  --configuration-policy '{
    "SecurityHub": {
      "ServiceEnabled": true,
      "EnabledStandardIdentifiers": [
        "arn:aws:securityhub::ruleset/finding-format/aws-foundational-security-standard/v/1.0.0",
        "arn:aws:securityhub:us-east-1:standard/cis-aws-foundations-benchmark/v/1.2.0"
      ]
    }
  }'
```

### S3 Bucket Policies with Deny Statements

This subsection covers S3 bucket policies that can create access lockouts requiring privileged account intervention.

**Security Significance**: S3 bucket policies with deny statements can override all other access controls and may require root account access to resolve.

**Privileged-Only Operations**:

- Create and modify S3 bucket policies with explicit deny statements
- Remove bucket policies that deny access to all principals including bucket owner
- Configure bucket policies that restrict access based on IP addresses or VPC endpoints
- Manage cross-account bucket access policies and permissions

**Security Implications**:

- **Immediate Impact**: Deny policies take effect immediately and can lock out all users including administrators
- **Blast Radius**: Can affect applications and services that depend on S3 bucket access
- **Recovery Complexity**: May require root account access or AWS Support intervention to resolve
- **Compliance Considerations**: Bucket policy changes must maintain data access controls and audit requirements

**Create S3 bucket policy with secure access controls**

```
aws s3api put-bucket-policy \
  --bucket secure-data-bucket \
  --policy '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "DenyInsecureConnections",
        "Effect": "Deny",
        "Principal": "*",
        "Action": "s3:*",
        "Resource": [
          "arn:aws:s3::secure-data-bucket",
          "arn:aws:s3::secure-data-bucket/*"
        ],
        "Condition": {
          "Bool": {
            "aws:SecureTransport": "false"
          }
        }
      },
      {
        "Sid": "AllowPrivilegedAccess",
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam:ACCOUNT-ID:role/S3AdministratorRole"
        },
        "Action": "s3:*",
        "Resource": [
          "arn:aws:s3::secure-data-bucket",
          "arn:aws:s3::secure-data-bucket/*"
        ]
      }
    ]
  }'
```

### Break-Glass Emergency Access

This subsection covers emergency access procedures for critical incidents requiring immediate privileged access outside normal approval processes. This is a recommendation on how customers could apply this to their organization. It is not a required configuraiton within your AWS account.

**Purpose**: Emergency access procedures for critical incidents requiring immediate response while maintaining security controls and audit trails.

**Emergency Access Triggers**

- Security incidents requiring immediate containment or response actions
- System outages affecting critical business operations or customer services
- Data recovery operations necessary for business continuity
- Compliance violations requiring immediate remediation to prevent regulatory impact

**Break-Glass Procedures**

- **Incident Declaration**: Formal declaration of emergency requiring privileged access through incident management system
- **Emergency Role Assumption**: Use pre-configured emergency IAM roles with enhanced monitoring
- **Immediate Notification**: Automated alerts to security and management teams within 5 minutes
- **Enhanced Logging**: Comprehensive logging and monitoring during emergency access period
- **Time Limitation**: Emergency access limited to maximum 2 hours with extension requiring additional approval
- **Post-Incident Review**: Mandatory review of all emergency access activities within 24 hours
- **Documentation Requirements**: Complete documentation of actions taken and business justification

**Assume emergency access role with enhanced monitoring**

```
aws sts assume-role \
  --role-arn "arn:aws:iam:ACCOUNT-ID:role/EmergencyAccessRole" \
  --role-session-name "emergency-$(date +%Y%m%d-%H%M%S)" \
  --duration-seconds 7200
```

### Privileged Session Monitoring

This subsection covers comprehensive monitoring and analysis of privileged account activities for security and compliance purposes.

**CloudWatch metric filter for privileged account activities**

```
aws logs put-metric-filter \
--log-group-name CloudTrail/PrivilegedAccounts \
--filter-name PrivilegedAccountActivity \
--filter-pattern '{ $.userIdentity.type = "AssumedRole" && $.userIdentity.arn = "_PrivilegedRole_" }' \
--metric-transformations \
metricName=PrivilegedAccountActivity,metricNamespace=Security/PrivilegedAccess,metricValue=1
```

**CloudWatch alarm for unusual privileged activity**

```
aws cloudwatch put-metric-alarm \
  --alarm-name "Unusual-Privileged-Activity" \
  --alarm-description "Alert on unusual privileged account activity" \
  --metric-name PrivilegedAccountActivity \
  --namespace Security/PrivilegedAccess \
  --statistic Sum \
  --period 300 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold \
  --alarm-actions arn:aws:sns:region:account:security-alerts
```

**Session Recording and Analysis**:

- **AWS CloudTrail**: Comprehensive API call logging for all privileged activities with log file validation
- **AWS Config**: Configuration change tracking and compliance monitoring for privileged operations
- **VPC Flow Logs**: Network traffic analysis for privileged instances and security assessment
- **Systems Manager Session Manager**: Shell session recording and audit trails for system access

## Compliance and Governance

This section covers ongoing compliance monitoring, access reviews, and governance processes for privileged account management. There are many ways to monitor and implement compliance. This is an example of how you can apply this in AWS.

### Regular Access Reviews

This subsection covers systematic review processes for privileged account permissions and usage patterns.

**Quarterly Privileged Account Review Process**:

- **Account Inventory**: Comprehensive list of all privileged accounts and roles with current status
- **Permission Analysis**: Review of assigned permissions against current job functions and responsibilities
- **Usage Assessment**: Analysis of account usage patterns, frequency, and access times
- **Risk Evaluation**: Assessment of security risks and potential impact based on current permissions
- **Remediation Actions**: Remove unnecessary permissions, disable unused accounts, and update role assignments
- **Documentation Update**: Update privileged account documentation, procedures, and approval matrices

**Access Review Automation**:

**Generate privileged account usage report**

```
# Generate credential report for privileged account analysis
aws iam generate-credential-report

# Get credential report data
aws iam get-credential-report \
  --query 'Content' \
  --output text | base64 -d > privileged-accounts-report.csv

# Analyze last used dates for privileged roles
aws iam list-roles \
  --query 'Roles[?contains(RoleName, `Admin`) || contains(RoleName, `Privileged`)].{RoleName:RoleName,LastUsed:RoleLastUsed.LastUsedDate}' \
  --output table
```

### Automated Compliance Checking

This subsection covers automated monitoring and validation of privileged account compliance with security policies.

**AWS Config rule for privileged account MFA compliance**

```
aws configservice put-config-rule \
  --config-rule '{
    "ConfigRuleName": "privileged-accounts-mfa-enabled",
    "Description": "Checks that privileged IAM users have MFA enabled",
    "Source": {
      "Owner": "AWS",
      "SourceIdentifier": "IAM_USER_MFA_ENABLED"
    },
    "Scope": {
      "ComplianceResourceTypes": ["AWS:IAM:User"]
    }
  }'
```

### Incident Response Integration

This subsection covers integration of privileged account management with security incident response procedures.

**Privileged Account Compromise Response**:

**Immediate Containment Actions**:

- Disable compromised account credentials and revoke active sessions
- Revoke temporary credentials and assume role permissions
- Block identified source IP addresses and suspicious network traffic
- Enable enhanced monitoring and alerting for affected accounts and resources

**Impact Assessment Procedures**:

- Review CloudTrail logs for unauthorized activities and configuration changes
- Analyze configuration changes and resource modifications during compromise period
- Assess data access patterns and evaluate potential data exfiltration
- Evaluate lateral movement attempts and privilege escalation activities

**Recovery and Remediation Steps**:

- Reset credentials, regenerate access keys, and update MFA devices
- Review and update IAM policies, permissions, and trust relationships
- Implement additional security controls and enhanced monitoring capabilities
- Conduct comprehensive security assessment and penetration testing
- Update incident response procedures based on lessons learned

## Best Practices and Recommendations

This section provides comprehensive guidance for implementing effective privileged account management in AWS environments.

### Principle of Least Privilege

This subsection covers implementation of least privilege access controls for privileged accounts.

**Granular Permissions Implementation**: Grant only the minimum permissions necessary for specific job functions and time-limited tasks

**Resource-Specific Access Controls**: Use resource-based policies and conditions to limit access to specific AWS resources and services

**Condition-Based Policy Enforcement**: Implement conditional access based on time windows, geographic location, and multi-factor authentication

**Regular Permission Optimization**: Conduct quarterly reviews to identify and remove unnecessary permissions and unused access rights

### Defense in Depth Strategy

This subsection covers layered security controls for comprehensive privileged account protection.

**Multi-Factor Authentication Requirements**: Hardware security keys (FIDO2/WebAuthn) required for all privileged accounts with backup authentication methods

**Network Segmentation Controls**: Isolate privileged access networks and implement dedicated administrative workstations

**Endpoint Security Enhancement**: Deploy advanced security controls on privileged access workstations including EDR and application whitelisting

**Behavioral Analytics Monitoring**: Implement user and entity behavior analytics (UEBA) to detect unusual privileged account activity patterns

### Automation and Orchestration

This subsection covers automated processes for consistent and secure privileged account management.

**Automated Provisioning Processes**: Use Infrastructure as Code (IaC) for consistent privileged account setup and configuration management

**Policy Enforcement Automation**: Implement Service Control Policies (SCPs) and AWS Config rules for organization-wide security controls

**Compliance Monitoring Systems**: Deploy automated compliance checking, remediation workflows, and continuous monitoring capabilities

**Incident Response Automation**: Implement automated response procedures for privileged account security events and policy violations

## Summary and Implementation Guidance

This section provides a comprehensive overview of privileged account management requirements and implementation recommendations.

**Critical Implementation Areas**:

**Privileged Account Classification**: Establish clear categories for security, network, infrastructure, and database administration accounts with defined responsibilities and risk levels.

**Privileged-Only Settings Management**: Implement comprehensive controls for AWS Organizations SCPs, cross-account trust relationships, KMS key policies, and organization-wide security service configuration.

**Access Management Framework**: Deploy just-in-time access, break-glass emergency procedures, and comprehensive session monitoring for all privileged operations.

**Compliance and Governance**: Maintain regular access reviews, automated compliance checking, and integrated incident response procedures for privileged account security.

**Operational Excellence**: Privileged account management requires ongoing attention to security controls, monitoring capabilities, and governance processes. Organizations should implement comprehensive controls including just-in-time access, enhanced monitoring, regular reviews, and incident response procedures. The combination of AWS native security services, proper IAM configuration, and operational procedures provides a robust framework for managing privileged access while supporting FedRAMP compliance considerations.

**Important Note**: This guidance provides AWS recommended practices and considerations for privileged account management. Organizations are responsible for evaluating these recommendations against their specific compliance requirements and implementing appropriate controls to meet their regulatory obligations. Regular review and updates of privileged account procedures help ensure continued effectiveness and compliance alignment.
