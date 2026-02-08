# Root Security Guidance

This topic discusses root security guidance.

**Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

**Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## Document Information

|              |            |
| ------------ | ---------- |
| Version      | 1.0.0      |
| Last Updated | 2026-01-09 |

## FRR-RSC-02: Root Security Settings Guidance

✓ MUST - Required for all FedRAMP services

**OSCAL Control ID: FRR-RSC-02**

**UUID: frr-rsc-02-control**

## Requirement

Providers MUST create and maintain guidance that explains security-related settings that can be operated only by top-level administrative accounts and their security implications.

## Component Implementation (OSCAL)

**Component UUID**: account-mgmt-component-002

**Component Type**: Account

**Control Implementation**: AC-2 (Account Management), AC-6 (Least Privilege), SC-28 (Protection of Information at Rest)

**Implementation Status**: Available

## Executive Summary

This guidance provides AWS recommended practices for security-related settings and operations that require root-level administrative privileges in AWS environments. These settings are critical for maintaining the security posture of AWS accounts and cannot be delegated to IAM users or roles, making proper root account management essential for FedRAMP compliance considerations.

## Root-Only Security Operations

### Account-Level Security Settings

This section covers fundamental account security configurations that can only be modified by root account credentials.

**Account Information and Contact Details**:

- **Security Significance**: Account contact information is used for security notifications, billing alerts, and account recovery procedures.
- **Root Account Email Address**: Primary contact for AWS security notifications and account recovery
- **Alternate Contacts**: Security, billing, and operations contacts for incident response
- **Security Challenge Questions**: Account recovery mechanism requiring root access to modify

**Implementation Requirements**:

- Use organizational email addresses, not personal accounts, or individual corporate emails, use a dedicate email for the account as needed.
- Implement email security controls (SPF, DKIM, DMARC)
- Monitor email accounts for unauthorized access
- Establish procedures for email account changes

### Account Recovery and Authentication Settings

This section describes security settings that control how account access can be restored if primary authentication methods are compromised.

**Account Recovery Configuration**:

**Security Significance**: Account recovery mechanisms are critical security controls that can bypass primary authentication if compromised. Weak recovery settings can enable account takeover even when primary credentials are secure.

**Root-Only Operations**:

- Password recovery email address configuration
- Security challenge questions setup and modification
- Account recovery phone number management
- Alternate authentication method configuration

**Security Implications**:

- Compromise of recovery email may allow unauthorized account access
- Weak security questions could be researched or guessed by unauthorized users
- Recovery phone numbers may be subject to social engineering attacks
- Recovery information should be secured independently from primary account credentials

**Implementation Requirements**:

- Use organizational email addresses with strong security controls
- Implement unique, non-guessable security challenge questions
- Secure recovery phone numbers with carrier-level protections
- Regular review and update of recovery information
- Monitor recovery mechanisms for unauthorized changes

### Billing and Financial Security Controls

This section covers financial security settings that require root account access to prevent unauthorized cost exposure and financial fraud.

**Billing Contact Information Management**:

**Security Significance**: Billing contacts receive financial notifications and have access to cost information that could reveal business intelligence or enable financial fraud.

**Root-Only Operations**:

- Primary billing contact configuration
- Alternate billing contact setup
- Payment method configuration and updates
- Tax information and compliance settings
- Cost allocation tag policy enforcement

**Security Implications**:

- Unauthorized billing contact changes may obscure unusual charges
- Modified payment methods could allow unauthorized resource provisioning
- Billing information may reveal organizational spending patterns
- Tax setting modifications could result in compliance issues

**Implementation Requirements**:

- Use secure, monitored email addresses for billing contacts
- Implement approval workflows for payment method changes
- Regular audit of billing contact information
- Monitor for unauthorized cost allocation changes
- Establish cost anomaly detection and alerting

### Regional Service Configuration

This section covers region-specific security settings that require root account management.

**Regional Service Enablement**:

**Security Significance**: Regional service availability affects data sovereignty, compliance boundaries, and incident response capabilities.

**Root-Only Operations**:

- New region enablement for account
- Region-specific service activation
- Cross-region replication configuration
- Regional compliance setting management

**Security Implications**:

- Unauthorized region enablement may affect data sovereignty requirements
- New regions require additional monitoring and logging configuration
- Cross-region data transfer should align with compliance policies
- Regional service differences may require security control adjustments

**Implementation Requirements**:

- Compliance review required before enabling new regions
- Update monitoring and logging for new regions
- Verify data classification policies for regional data
- Establish incident response procedures for new regions
- Document regional security control variations

### Account Closure and Decommissioning

This section provides guidance for the permanent closure of AWS accounts, which requires root account authorization.

[Close an AWS account](../../../accounts/latest/reference/manage-acct-closing.md "../../../accounts/latest/reference/manage-acct-closing.md")

**Security Significance**: Permanent account closure is irreversible and requires root authorization to prevent unauthorized account termination. There is a 90 day grace period in account closures, during this time the account remains recoverable, but resources within the account may be impacted.

**Root-Only Operations**:

- Account closure initiation
- Account closure confirmation
- Grace period management
- Final data export and backup

**Security Implications**:

- Unauthorized closure can cause business disruption
- Data loss risk during grace period
- Compliance record retention requirements
- Cross-account dependency impacts

**Implementation Requirements**:

- Formal approval process for account closure
- Complete data backup before closure initiation
- Notification to dependent systems and accounts
- Documentation of closure rationale and timeline
- Compliance team review for record retention requirements

### Support and Service Plan Management

This section covers AWS Support plan modifications that affect security incident response capabilities.

[Change AWS Support Plans](../../../awssupport/latest/user/changing-support-plans.md "../../../awssupport/latest/user/changing-support-plans.md")

**AWS Support Plan Configuration**:

**Security Significance**: Modification of a support plan can limit your ability to interact with AWS Support, and impact additional entitlements that come with your support tier.

**Root-Only Operations**:

- Support plan tier changes (Basic, Developer, Business, Enterprise)
- Support case access level modifications
- Technical Account Manager assignment changes
- Concierge support activation/deactivation

**Security Implications**:

- **Support Case Access**: Higher support tiers provide faster response times for security incidents
- **Trusted Advisor**: Business and Enterprise plans include security recommendations
- **Technical Account Manager**: Enterprise plans provide dedicated security guidance
- **Concierge Support**: Assistance with account and billing security issues
- Downgrading support can delay security incident response
- Loss of security advisory services may increase risk exposure

**Implementation Requirements**:

- Security team approval required for support plan changes
- Document impact on incident response capabilities
- Ensure alternative security advisory resources if downgrading
- Maintain emergency contact procedures regardless of support tier
- Regular review of support plan adequacy for security needs

### Root account functionality

This section provides an overview of AWS root account capabilities and references to detailed guidance on avoiding root account usage.

The root account controls specific functionality in AWS. Refer to the [Top Level Guidance](../../../admin-guidance/top-level-admin-guidance.md "../../../admin-guidance/top-level-admin-guidance.md") for detailed information on how to avoid using the root account in your AWS environment.

###### Important

AWS strongly recommends that you don’t use the root user for your everyday tasks and that you follow the root user best practices for your AWS account. Safeguard your root user credentials and use them to perform the tasks that only the root user can perform. For the complete list of tasks that require you to sign in as the root user, see Tasks that require root user credentials.

The AWS Documentation contains information on what requests can be performed by a root user and how to [perform a privileged task](../../../IAM/latest/UserGuide/id_root-user-privileged-task.md "../../../IAM/latest/UserGuide/id_root-user-privileged-task.md").

## Management Account Exclusive Security Operations

### Organization-Wide Security Service Configuration

This section covers security services that can only be configured at the organization level by the management account.

**AWS Config Organization Aggregator Setup**:

**Security Significance**: Centralized compliance data collection across all organization accounts enables comprehensive security posture monitoring.

**Management Account Only Operations**:

- Organization aggregator creation and configuration
- Cross-account authorization for compliance data collection
- Aggregated compliance rule deployment
- Organization-wide configuration baseline enforcement

**Security Implications**:

- Centralized visibility into security configuration across all accounts
- Ability to detect configuration drift organization-wide
- Compliance reporting aggregation for audit purposes
- Centralized monitoring requires appropriate access controls and redundancy planning

**Security Hub Master Account Configuration**:

**Security Significance**: Centralized security findings management enables coordinated threat response across the organization.

**Management Account Only Operations**:

- Security Hub master account designation
- Cross-account finding aggregation setup
- Organization-wide security standard enablement
- Centralized finding workflow configuration

**Security Implications**:

- Unified security dashboard for entire organization
- Coordinated incident response across multiple accounts
- Standardized security control implementation
- Centralized security data requires appropriate access controls and protection measures

**GuardDuty Master Account Configuration**:

**Security Significance**: Centralized threat detection coordination enables organization-wide security monitoring.

**Management Account Only Operations**:

- GuardDuty master account setup
- Member account invitation and management
- Organization-wide threat intelligence sharing
- Centralized finding and alert management

**Security Implications**:

- Comprehensive threat detection across all organization accounts
- Coordinated response to multi-account security incidents
- Centralized threat intelligence and IOC sharing
- Member account configuration should be validated to ensure complete coverage

### Identity and Access Management at Organization Level

This section covers identity and access management configurations that require management account privileges.

**AWS SSO/Identity Center Organization Setup**:

**Security Significance**: Centralized workforce identity management affects access control across the entire organization.

**Management Account Only Operations**:

- Identity Center instance creation and configuration
- Organization-wide SSO enablement
- External identity provider integration
- Permission set deployment across accounts

**Security Implications**:

- Single sign-on security for entire organization
- Centralized access control and audit capabilities
- Centralized identity management requires appropriate redundancy and access controls
- Identity provider integration should include security dependency assessment

**Cross-Account Role Trust Relationship Management**:

**Security Significance**: Cross-account trust relationships enable secure resource sharing but can create security vulnerabilities if misconfigured.

**Management Account Only Operations**:

- Organization-wide cross-account role creation
- Trust policy establishment between accounts
- Centralized role assumption monitoring
- Cross-account permission boundary enforcement

**Security Implications**:

- Secure resource sharing across organization accounts
- Trust policies should follow least privilege principles to prevent excessive permissions
- Centralized monitoring of cross-account access patterns
- Cross-account access should be regularly reviewed and validated

## Root Account Specific Security Operations

### S3 Security Controls

**S3 MFA Delete Protection**:

**Security Purpose**: Prevents accidental or malicious deletion of S3 objects and bucket versions.

**Implementation**:

**Enable MFA Delete (requires root account with MFA)**

```
aws s3api put-bucket-versioning \
--bucket BUCKET-NAME \
--versioning-configuration Status=Enabled,MFADelete=Enabled \
--mfa "SERIAL-NUMBER TOKEN-CODE"
```

**Verify MFA Delete status**

```
aws s3api get-bucket-versioning --bucket BUCKET-NAME
```

**Operational Impact**:

- Requires MFA token for object version deletion
- Protects against automated deletion scripts
- Adds additional verification step for data protection
- Cannot be enabled through IAM users or roles

### IAM Access Recovery Operations

**IAM Permission Boundary Restoration**:

**Security Purpose**: Restore IAM access when administrative users are locked out due to overly restrictive policies.

**Common Lockout Scenarios**:

- Misconfigured IAM policies denying all access
- Incorrect permission boundaries blocking administrative actions
- Service Control Policies (SCPs) preventing IAM operations
- Resource-based policies denying IAM principals

**Recovery Procedures**:

- **Root Account Access**: Use root credentials to access AWS Console
- **Policy Analysis**: Review IAM policies, SCPs, and resource policies
- **Temporary Fix**: Create emergency administrative role with necessary permissions
- **Permanent Resolution**: Correct the underlying policy issues
- **Testing**: Verify administrative access is restored

### Emergency Resource Policy Recovery

**S3 Bucket Policy Unlock**:

**Use Case**: Remove S3 bucket policies that deny access to all principals, including the bucket owner. In some cases, users may create an access control list for an S3 bucket that "locks" the user out of the bucket. In this situation the only way to restore access is to access the AWS account as a root user and remove the bucket policy. This can be done now with the usage of [privileged actions](../../../IAM/latest/UserGuide/security-iam-awsmanpol.md#security-iam-awsmanpol-S3UnlockBucketPolicy "../../../IAM/latest/UserGuide/security-iam-awsmanpol.md#security-iam-awsmanpol-S3UnlockBucketPolicy") which further removes the need to log onto the root account. Some organization may not have centralzied root management enabled and this it’s important to understand that this is still limited to root account only in some situations.

**Example Problematic Policy**:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3::bucket-name",
        "arn:aws:s3::bucket-name/*"
      ]
    }
  ]
}
```

**Root-Only Resolution**:

**Using AWS Organizations privileged actions with temporary elevated permissions.**

```
aws organizations enable-policy-type \
--root-id r-example \
--policy-type SERVICE_CONTROL_POLICY

aws iam create-role \
--role-name S3BucketPolicyRemovalRole \
--assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam:MANAGEMENT-ACCOUNT-ID:user/USERNAME"},
    "Action": "sts:AssumeRole"
  }]
}'

aws iam attach-role-policy \
--role-name S3BucketPolicyRemovalRole \
--policy-arn arn:aws:iam:aws:policy/AmazonS3FullAccess

aws sts assume-role \
--role-arn arn:aws:iam:TARGET-ACCOUNT-ID:role/S3BucketPolicyRemovalRole \
--role-session-name s3-policy-removal-session
```

**Delete the problematic bucket policy using assumed role credentials**

```
export AWS_ACCESS_KEY_ID=ASSUMED-ROLE-ACCESS-KEY
export AWS_SECRET_ACCESS_KEY=ASSUMED-ROLE-SECRET-KEY
export AWS_SESSION_TOKEN=ASSUMED-ROLE-SESSION-TOKEN

aws s3api delete-bucket-policy --bucket bucket-name
```

### Security Best Practices for Root-Only Operations

#### Access Control and Authentication

Limit access to usage of AWS root account actions. You can implement AWS Organizations Security Control Policies to limit root logon permission in an AWS Organization. You can limit both the creation of root access keys, and dissallow actions as root user as well. AWS Control Tower offers [strong recommended preventive](../../../controltower/latest/controlreference/strongly-recommended-preventive-controls.md "../../../controltower/latest/controlreference/strongly-recommended-preventive-controls.md") controls that you can implement in your organization. If you are allowing root logons you should secure them with the appropriate measures.

#### Multi Factor Authentication

**Multi-Factor Authentication Requirements**:

- **Hardware Security Keys**: FIDO2/WebAuthn devices (YubiKey, etc.) - Highest security
- **Virtual MFA Devices**: Authenticator apps (Google Authenticator, Authy) - Good security
- **SMS MFA**: Consider alternative methods for FedRAMP environments due to potential social engineering risks

#### Session Management

- **Session Timeout**: Configure automatic logout after inactivity
- **Concurrent Sessions**: Monitor for multiple simultaneous root sessions
- **Geographic Restrictions**: Implement IP-based access controls where possible
- **Time-based Access**: Restrict root access to business hours when feasible

#### Monitoring and Auditing

CloudTrail Configuration for Root activities can help to identify usage of AWS root account credentials. It’s important to setup monitoring and alerting for root account actions.

**Create dedicated CloudTrail for root account monitoring**

```
aws cloudtrail create-trail \
--name root-activity-trail \
--s3-bucket-name security-audit-logs-bucket \
--include-global-service-events \
--is-multi-region-trail \
--enable-log-file-validation \
--kms-key-id arn:aws:kms:region:account:key/key-id
```

Create real-time Alerting for Root Usage as well to make sure you can maintain awareness of usage.

**CloudWatch metric filter for root account usage**

```
aws logs put-metric-filter \
--log-group-name CloudTrail/RootAccountActivity \
--filter-name RootAccountUsage \
--filter-pattern '{ $.userIdentity.type = "Root" && $.eventName != "ConsoleLogin" }' \
--metric-transformations \
metricName=RootAccountAPIUsage,metricNamespace=Security/RootAccount,metricValue=1
```

**CloudWatch alarm for root account API usage**

```
aws cloudwatch put-metric-alarm \
--alarm-name "Root-Account-API-Usage" \
--alarm-description "Alert on root account API usage" \
--metric-name RootAccountAPIUsage \
--namespace Security/RootAccount \
--statistic Sum \
--period 300 \
--threshold 1 \
--comparison-operator GreaterThanOrEqualToThreshold \
--alarm-actions arn:aws:sns:region:account:security-alerts
```

### Operational Procedures

#### Change Management Process

A formal change management process is helpful in reducing the likliehood of inadvertent usage of root credentials. Placing safeguards and checks in place to prevent usage of root credentials can be implemented with the following items.

- **Request Authorization**: Formal approval process for root account usage
- **Justification Documentation**: Business case and technical necessity
- **Witness Requirement**: Two-person integrity for sensitive operations
- **Time Limitation**: Specific time windows for root account access
- **Post-Action Review**: Verification and documentation of changes made

#### Emergency Access Procedures

In case of emergency use, consider proper steps to ensure process is still followed.

- **Emergency Access Process**: Documented emergency access procedures
- **Incident Response**: Integration with security incident response plans
- **Communication Plan**: Notification requirements for emergency root access
- **Recovery Validation**: Verification that emergency actions resolved the issue

#### Compliance and Governance

Using AWS Config Rules for Root Account Security are recommended for monitoring specific component of root usage.

**Config Rules for Root Account Security**

Deploy AWS Config rules for root account compliance. The two provided AWS Config rules monitor for account compliance in having MFA enabled for root accounts, and identification if a root account has access keys.

```
aws configservice put-config-rule \
--config-rule '{
  "ConfigRuleName": "root-mfa-enabled",
  "Description": "Checks whether MFA is enabled for root account",
  "Source": {
    "Owner": "AWS",
    "SourceIdentifier": "ROOT_MFA_ENABLED"
  }
}'
```

```
aws configservice put-config-rule \
--config-rule '{
  "ConfigRuleName": "root-access-key-check",
  "Description": "Checks whether root account has access keys",
  "Source": {
    "Owner": "AWS",
    "SourceIdentifier": "ROOT_ACCESS_KEY_CHECK"
  }
}'
```

**Summary and Recommendations**

###### Immediate Actions

- Implement AWS Organizations root access management for all multi-account environments, avoid usage of root logons
- Enable comprehensive monitoring for all root account activities
- Document emergency procedures for root-only operations
- Train security teams on new root access management capabilities

---

###### Long-term Strategy

- Implement automated compliance validation using AWS Config
- Establish regular security reviews of root account configurations and usage
- Integrate with enterprise identity systems for centralized access management
