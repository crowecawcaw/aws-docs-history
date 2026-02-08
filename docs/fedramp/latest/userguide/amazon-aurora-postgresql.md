# Amazon Aurora PostgreSQL

This guide provides security configuration requirements and implementation examples for Amazon Aurora PostgreSQL in accordance with FedRAMP requirements.

## Document Information

|                   |                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------- |
| Version           | 1.0.0                                                                                     |
| Last Updated      | 2026-01-09                                                                                |
| Documentation URL | https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html |

## Overview

Amazon Aurora PostgreSQL security configuration involves implementing comprehensive security controls including encryption, access management, logging, and monitoring to meet FedRAMP compliance requirements. This guidance covers master user account security, PostgreSQL-specific administrative operations, and privileged access controls for Aurora PostgreSQL database operations.

**Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

**Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements

Amazon Aurora PostgreSQL must comply with the following FedRAMP requirements:

- FRR-RSC-01
- FRR-RSC-02
- FRR-RSC-03
- FRR-RSC-04
- FRR-RSC-05
- FRR-RSC-06
- FRR-RSC-07

## Administrative Account Model

Amazon Aurora PostgreSQL has an administrative account model.

|                         |                              |
| ----------------------- | ---------------------------- |
| Administrative Accounts | Yes                          |
| Account Type            | Database Master User Account |

## FRR-RSC-01: Administrative Accounts

**Applicable:** Yes

Amazon Aurora PostgreSQL Administrative Account Security Configuration

### OVERVIEW

Amazon Aurora PostgreSQL administrative access is managed through the Master database user account and AWS IAM roles. This guidance provides comprehensive security recommendations for securing administrative access to Aurora PostgreSQL clusters.

### MASTER DATABASE USER SECURITY

1. Master User Account Configuration:
   - Use strong, randomly generated passwords (minimum 20 characters)
   - Rotate master passwords regularly (every 90 days maximum)
   - Store passwords in AWS Secrets Manager with automatic rotation
   - Never use default or predictable usernames (avoid 'admin', 'root', 'postgres')

2. Authentication Methods:
   - Enable IAM database authentication where supported
   - Use AWS Secrets Manager for password management
   - Implement PostgreSQL-specific authentication mechanisms

### POSTGRESQL ADMINISTRATIVE SECURITY

- PostgreSQL-Specific Configuration \*\*
  - Master user: Create with CREATEDB and CREATEROLE privileges only
  - Disable superuser privileges for application accounts
  - Enable comprehensive logging:
    - log_statement = 'all'
    - log_connections = on
    - log_disconnections = on
    - log_duration = on

  - Set connection limits: max_connections appropriate for workload
  - Configure password policies: password_encryption = 'scram-sha-256'
  - Enable pg_audit extension for detailed audit logging:
    - shared_preload_libraries = 'pg_audit'
    - pg_audit.log = 'all'
    - pg_audit.log_catalog = on

### AWS IAM INTEGRATION

1. IAM Database Authentication:
   - Enable IAM database authentication on Aurora cluster
   - Create IAM policies with rds-db:connect permissions
   - Use temporary credentials instead of passwords
   - Example policy for IAM database authentication:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "rds-db:connect",
         "Resource": "arn:aws:rds-db:region:account:dbuser:cluster-id/db-username"
       }
     ]
   }
   ```

2. Cross-Service Integration:
   - Use AWS Secrets Manager for credential rotation
   - Integrate with AWS CloudTrail for API call logging
   - Configure VPC security groups for network-level access control
   - Enable Enhanced Monitoring for performance insights

### NETWORK SECURITY

1. VPC Configuration:
   - Deploy Aurora in private subnets only
   - Configure DB subnet groups across multiple AZs
   - Use VPC security groups instead of DB security groups
   - Implement least-privilege security group rules

2. Connection Security:
   - Enable SSL/TLS encryption in transit for all connections
   - Use VPC endpoints for AWS service communications
   - Configure connection timeouts and limits
   - Monitor connection patterns for anomalies

### MONITORING AND AUDITING

1. Database-Level Auditing:
   - Enable pg_audit extension for all administrative actions
   - "Publish logs to CloudWatch Logs and configure retention period (minimum 90 days)
   - Monitor failed login attempts and privilege escalations
   - Set up alerts for suspicious administrative activities

2. AWS-Level Monitoring:
   - Enable CloudTrail for all Aurora API calls
   - Configure CloudWatch alarms for administrative events
   - Use AWS Config rules for compliance monitoring

### BACKUP AND RECOVERY SECURITY

1. Automated Backups:
   - Enable automated backups with encryption
   - Configure backup retention period (7-35 days)
   - Use cross-region backup replication for DR (Use AWS Backups)
   - Encrypt backup snapshots with customer-managed KMS keys

2. Manual Snapshots:
   - Encrypt all manual snapshots
   - Encrypted snapshots require customer-managed KMS keys (not default AWS-managed keys) for sharing
   - Regular testing of snapshot restoration procedures
   - Document recovery time objectives (RTO) and recovery point objectives (RPO)

## FRR-RSC-02: Administrative Settings

**Applicable:** Yes

### Security-Related Settings Restricted to Master User (rds_superuser role)

The master user account in Amazon Aurora PostgreSQL has the `rds_superuser` role, which provides elevated privileges that cannot be delegated to regular database users. The following operations and their security implications are restricted to accounts with the rds_superuser role:

#### 1. User and Role Management

**Operations:**

- CREATE USER / CREATE ROLE with LOGIN privilege
- ALTER USER / ALTER ROLE to modify user attributes
- DROP USER / DROP ROLE
- GRANT and REVOKE role memberships
- Password management for all database users (unless delegated via rds_password role)

**Security Implications:**

- Controls who can access the database
- Determines authentication methods and password policies
- Manages privilege escalation through role assignments
- Unauthorized user creation could lead to security breaches
- Improper role grants could violate least privilege principles

#### 2. Extension Management

**Operations:**

- CREATE EXTENSION (for most extensions)
- ALTER EXTENSION
- DROP EXTENSION
- Note: Can be delegated using `rds.allowed_extensions` parameter (Aurora PostgreSQL 13.4+)

**Security Implications:**

- Extensions can introduce security vulnerabilities if not properly vetted
- Some extensions provide access to system-level functions
- Malicious extensions could compromise database security
- Extensions may bypass row-level security or other access controls

#### 3. Database Creation and Ownership

**Operations:**

- CREATE DATABASE
- ALTER DATABASE (ownership and configuration)
- DROP DATABASE

**Security Implications:**

- Database owners have extensive privileges within their databases
- Improper database ownership can lead to privilege escalation
- Database-level settings affect all objects within the database
- Unauthorized database creation could consume resources or expose data

#### 4. Replication and Backup Operations

**Operations:**

- REPLICATION CLIENT and REPLICATION SLAVE privileges
- Access to replication slots
- Logical replication configuration

**Security Implications:**

- Replication access allows reading all database data
- Improper replication configuration could expose sensitive data
- Replication users can bypass row-level security
- Could be used for unauthorized data exfiltration

#### 5. System Catalog Modifications

**Operations:**

- Direct modifications to system catalogs (pg_catalog)
- Access to sensitive system views and functions
- Modification of system-level settings

**Security Implications:**

- System catalog corruption can compromise database integrity
- Unauthorized access to system catalogs reveals database structure
- Could be used to bypass security controls
- May expose sensitive metadata about users and permissions

#### 6. Event Triggers

**Operations:**

- CREATE EVENT TRIGGER
- ALTER EVENT TRIGGER
- DROP EVENT TRIGGER

**Security Implications:**

- Event triggers execute with elevated privileges
- Can intercept and modify DDL operations
- Could be used to implement backdoors or audit bypasses
- Malicious event triggers could compromise database security

#### 7. Audit and Logging Configuration

**Operations:**

- Enabling/disabling pg_audit extension
- Configuring audit log settings
- Modifying log retention and export settings

**Security Implications:**

- Disabling audit logging could hide malicious activity
- Improper log configuration may fail to capture security events
- Log tampering could compromise forensic investigations
- Audit settings are critical for compliance requirements

### Best Practices for Master User Account Security

1. **Minimize Master User Usage**
   - Never use master user directly in applications
   - Create application-specific users with minimal required privileges
   - Reserve master user for administrative tasks only

2. **Secure Master User Credentials**
   - Use AWS Secrets Manager for password management
   - Enable automatic password rotation (90 days maximum)
   - Use strong, randomly generated passwords (minimum 20 characters)
   - Never hardcode master credentials in application code

3. **Enable Multi-Factor Authentication**
   - Require MFA for AWS Console access to modify master password
   - Implement MFA for IAM users who can modify DB clusters
   - Use IAM database authentication where possible

4. **Audit Master User Activity**
   - Enable comprehensive database audit logging
   - Monitor all master user connections and operations
   - Set up CloudWatch alarms for master user activity
   - Review audit logs regularly for unauthorized access

5. **Implement Least Privilege**
   - Create role-based access with minimal required privileges
   - Grant privileges at the most granular level possible
   - Regularly review and revoke unnecessary privileges
   - Document all privilege grants and their justifications

6. **Network Security**
   - Deploy Aurora in private subnets only
   - Use VPC security groups to restrict database access
   - Never make Aurora clusters publicly accessible
   - Use VPC endpoints for AWS service communications

7. **Compliance and Documentation**
   - Document all master user operations
   - Maintain audit trail of privilege changes
   - Conduct quarterly access reviews
   - Implement change management for security settings

## FRR-RSC-03: Privileged Settings

**Applicable:** Yes

Within Aurora you have two layers of privileged access. One layer is at the IAM layer, where you can limit what permissions a user has to operate within RDS. This section covers the priviliged settings for using the service itself and provides example IAM Policies that would allow for varying levels of access to the service. The second layer of privileged access is at the database engine layer itself which is covered in the other sections of this document.

## IAM Least Privilege Policies

Sample IAM policies for least privilege access to Amazon Aurora PostgreSQL

**Read Only Policy:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:Describe*",
        "rds:List*",
        "rds:Get*"
      ],
      "Resource": "*"
    }
  ]
}
```

**Operator Policy:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:Describe*",
        "rds:List*",
        "rds:Get*",
        "rds:Update*",
        "rds:Put*",
        "rds:Create*"
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

**Administrator Policy:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "rds:*",
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

### Database Encryption

Amazon Aurora PostgreSQL requires encryption at rest using AWS KMS customer-managed keys and SSL/TLS encryption in transit for secure database operations.

**Implementation Overview:** Aurora PostgreSQL security involves encrypting data at rest and in transit, securing the master user account, implementing network access controls, and enabling comprehensive audit logging with pg_audit.

#### Implementation Examples

1. **Create KMS Key for Aurora Encryption**

Create dedicated KMS key for encrypting Aurora PostgreSQL cluster

```
# Create KMS key for Aurora encryption
aws kms create-key --description 'Aurora PostgreSQL Encryption Key' --key-usage ENCRYPT_DECRYPT
# Create alias for the key
aws kms create-alias --alias-name alias/aurora-postgresql-key --target-key-id arn:aws:kms:region:account:key/key-id
```

2. **Create Encrypted Aurora PostgreSQL Cluster**

Create Aurora cluster with encryption enabled and secure master user configuration

```
# Create encrypted Aurora PostgreSQL cluster
aws rds create-db-cluster \
  --db-cluster-identifier my-aurora-pg-cluster \
  --engine aurora-postgresql \
  --master-username postgres \
  --manage-master-user-password \
  --master-user-secret-kms-key-id alias/aurora-postgresql-key \
  --storage-encrypted \
  --kms-key-id alias/aurora-postgresql-key \
  --vpc-security-group-ids sg-xxxxxxxxx \
  --db-subnet-group-name private-subnet-group
```

3. **Configure SSL/TLS and pg_audit Logging**

Enable SSL enforcement and comprehensive audit logging with pg_audit

```
# Create parameter group with SSL enforcement and pg_audit
aws rds create-db-cluster-parameter-group \
  --db-cluster-parameter-group-name aurora-postgresql-secure \
  --db-parameter-group-family aurora-postgresql14 \
  --description 'Secure Aurora PostgreSQL parameters'

# Enable SSL enforcement and pg_audit logging
aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name aurora-postgresql-secure \
  --parameters ParameterName=rds.force_ssl,ParameterValue=1 \
  --parameters ParameterName=shared_preload_libraries,ParameterValue=pg_audit \
  --parameters ParameterName=pgaudit.log,ParameterValue=all
```

**API:**
`aws rds create-db-cluster --storage-encrypted --kms-key-id alias/aurora-postgresql-key`

**Control:** SC-28

### Privileged Access Control

Amazon Aurora PostgreSQL requires implementation of privileged account security controls including least privilege access, multi-factor authentication for administrative operations, and comprehensive audit logging of privileged activities.

**Implementation Overview:** Amazon Aurora PostgreSQL privileged account security involves implementing strict access controls, monitoring privileged operations, and ensuring administrative activities are properly authenticated and logged.

#### Implementation Examples

1. **Implement Least Privilege Access**

Configure Amazon Aurora PostgreSQL with minimal required permissions for administrative accounts

```
# Create least privilege IAM policy for Amazon Aurora PostgreSQL administration
aws iam create-policy --policy-name ServiceAdminPolicy --policy-document file://admin-policy.json
# Attach policy to administrative role
aws iam attach-role-policy --role-name ServiceAdminRole --policy-arn arn:aws:iam::account:policy/ServiceAdminPolicy
```

2. **Enable Multi-Factor Authentication**

Require MFA for all privileged operations and administrative access

```
# Create MFA-required policy condition
# Add MFA condition to administrative policies
# Verify MFA enforcement for privileged operations
```

3. **Configure Privileged Activity Monitoring**

Enable comprehensive logging and monitoring of all privileged account activities

```
# Enable CloudTrail for API logging
aws cloudtrail create-trail --name ServicePrivilegedAccess --s3-bucket-name audit-logs
# Configure CloudWatch alarms for privileged operations
aws logs create-log-group --log-group-name /aws/service/privileged-access
```

**API:**
`Configure via IAM policies and amazon-aurora-postgresql administrative APIs`

**Control:** AC-6

## FRR-RSC-04: Secure Defaults

**Applicable:** Yes

AWS services are designed with security in mind, providing multiple layers of security controls and encryption capabilities. However, AWS allows customers to define the security configuration of services and does not enforce a minimum security standard by default, enabling customers the flexibility to meet their specific business requirements and compliance needs.

Amazon Aurora PostgreSQL should be configured with encryption enabled, strong master user credentials, SSL enforcement, and comprehensive audit logging by default.

### Implementation

Ensure Aurora PostgreSQL clusters are created with security-first configurations including encryption, access controls, and monitoring

**Best Practices:**

- Enable encryption at rest using customer-managed KMS keys
- Use AWS Secrets Manager for master user password management
- Enforce SSL/TLS connections for all database access
- Enable pg_audit extension for comprehensive audit logging
- Deploy in private subnets with restrictive security groups
- Implement automated backup encryption
- Configure parameter groups with security-hardened settings
- Use row-level security (RLS) for fine-grained access control

## FRR-RSC-05: Configuration Comparison

**Applicable:** Yes

Use AWS Config rules and custom scripts to compare current Aurora PostgreSQL configuration against security baselines.

## FRR-RSC-06: Configuration Export

**Applicable:** Yes

Export Aurora PostgreSQL configuration using AWS CLI describe commands in JSON format.

## FRR-RSC-07: API Configuration

**Applicable:** Yes

### Cluster Management

**API Command:**

```
Configure via AWS RDS APIs for Aurora PostgreSQL cluster management
```

**Control:** AC-6

**Implementation Guidance:**

- Create separate roles for different access levels (read-only, operator, administrator)
- Always require MFA for privileged operations
- Use time-based conditions to limit session duration
- Implement resource-based restrictions where possible
- Regular review and rotation of access permissions

## Additional Resources

For more information about AWS security best practices, see the following resources:

- [AWS Security Documentation](../../../security.md "../../../security.md")
- [AWS FedRAMP Compliance](https://aws.amazon.com/compliance/fedramp/ "https://aws.amazon.com/compliance/fedramp/")
- [AWS Well-Architected Security Pillar](../../../wellarchitected/latest/security-pillar/welcome.md "../../../wellarchitected/latest/security-pillar/welcome.md")
