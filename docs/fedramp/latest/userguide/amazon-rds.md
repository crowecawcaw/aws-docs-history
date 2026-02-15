# Amazon RDS

This guide provides security configuration requirements and implementation examples for Amazon RDS in accordance with FedRAMP requirements.

## Document Information

|                   |                                                                                  |
| ----------------- | -------------------------------------------------------------------------------- |
| Version           | 1.0.0                                                                            |
| Last Updated      | 2026-01-09                                                                       |
| Documentation URL | https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP\_GettingStarted.html |

## Overview

Amazon RDS security configuration involves implementing comprehensive security controls including encryption, access management, logging, and monitoring to meet FedRAMP compliance requirements. This guidance covers master user account security across all supported database engines and privileged access controls for relational database operations.

**Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

**Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements

Amazon RDS must comply with the following FedRAMP requirements:

- FRR-RSC-01
- FRR-RSC-02
- FRR-RSC-03
- FRR-RSC-04
- FRR-RSC-05
- FRR-RSC-06
- FRR-RSC-07

## Administrative Account Model

Amazon RDS has an administrative account model.

|                         |                      |
| ----------------------- | -------------------- |
| Administrative Accounts | Yes                  |
| Account Type            | Master database user |

## FRR-RSC-01: Administrative Accounts

**Applicable:** Yes

**Implementation Overview:** Amazon RDS administrative access is managed through the Master database user account and AWS IAM roles. This guidance provides comprehensive security recommendations for securing administrative access to RDS instances across all supported database engines.

### Master Database User Security

**Master User Account Configuration:**

- Use strong, randomly generated passwords (minimum 20 characters)
- Rotate master passwords regularly (every 90 days maximum)
- Store passwords in AWS Secrets Manager with automatic rotation
- Never use default or predictable usernames (avoid 'admin', 'root', 'sa')

**Authentication Methods:**

- Enable IAM database authentication where supported
- Use AWS Secrets Manager for password management
- Implement database-specific authentication mechanisms

### Database Engine-Specific Configurations

**PostgreSQL Administrative Security**

- Master user: Create with CREATEDB and CREATEROLE privileges only
- Disable superuser privileges for application accounts
- Configure pg_hba.conf for strict connection controls:
  - Require SSL connections: `hostssl all all 0.0.0.0/0 md5`
  - Limit connections by IP range and database

- Enable logging: `log_statement = 'all'`, `log_connections = on`
- Set connection limits: `max_connections` appropriate for workload
- Configure password policies: `password_encryption = 'scram-sha-256'`

**MySQL Administrative Security**

- Master user: Limit to necessary privileges, avoid SUPER privilege
- Enable SSL/TLS: `require_secure_transport = ON`
- Configure strict authentication: `default_authentication_plugin = mysql_native_password`
- Enable audit logging: `audit_log_policy = ALL`
- Set connection limits: `max_connections`, `max_user_connections`
- Disable remote root access: `DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1')`

**SQL Server Administrative Security**

- Master user: Use Windows Authentication when possible
- Enable SQL Server Audit for administrative actions
- Configure login policies: `CHECK_POLICY = ON`, `CHECK_EXPIRATION = ON`
- Set connection encryption: `Encrypt = yes`, `TrustServerCertificate = no`
- Enable C2 audit mode for comprehensive logging
- Configure server roles with least privilege principles

**Oracle Administrative Security**

- Master user: Avoid using SYS/SYSTEM accounts for applications
- Enable Oracle Audit Vault and Database Firewall integration
- Configure strong authentication: `SQLNET.AUTHENTICATION_SERVICES = (NONE)`
- Enable SSL/TLS: `SQLNET.ENCRYPTION_SERVER = REQUIRED`
- Set password policies: `PASSWORD_VERIFY_FUNCTION`
- Configure connection pooling limits and timeouts

**MariaDB Administrative Security**

- Master user: Limit to necessary privileges, avoid SUPER privilege
- Enable SSL/TLS: `require_secure_transport = ON`
- Configure authentication plugins: Support for `mysql_native_password`, `ed25519`, and `pam` authentication
- Enable audit logging: Use MariaDB Audit Plugin via RDS option groups
- Set connection limits: `max_connections`, `max_user_connections`
- Configure password validation: Use `simple_password_check` or `cracklib_password_check` plugins
- Implement account resource limits: `MAX_QUERIES_PER_HOUR`, `MAX_UPDATES_PER_HOUR`, `MAX_CONNECTIONS_PER_HOUR`
- Enable password expiration policies: `default_password_lifetime` parameter
- Disable remote root access: `DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1')`
- Use roles for privilege management: `CREATE ROLE`, `GRANT role TO user`

**IBM DB2 Administrative Security**

- Master user: Has DBADM, SYSCTRL, SYSMAINT, and SYSMON authorities (not SYSADM)
- Use group-based access control: Users gain database access through group membership
- Enable SSL/TLS: Configure `DB2COMM = TCPIP,SSL` and `SSL_SVCENAME` parameters
- Configure authentication: Support for LDAP and Kerberos integration
- Enable audit logging: Use DB2_AUDIT option in RDS option groups with S3 integration
- Implement role-based access: Use RDS default roles (`ROLE_NULLID_PACKAGES`, `ROLE_TABLESPACES`, `ROLE_PROCEDURES`)
- Set connection limits: Configure workload management and connection limits
- Use rdsadmin procedures: `rdsadmin.add_user`, `rdsadmin.create_role`, `rdsadmin.grant_role`
- Configure password policies: Implement through group policies and authentication mechanisms
- Separate administrative duties: Create specific roles for different administrative functions
- Grant minimal database authorities: Use `CONNECT`, `BINDADD`, `CREATETAB`, `IMPLICIT_SCHEMA` as baseline

### AWS IAM Integration

**IAM Database Authentication (PostgreSQL/MySQL):**

- Enable IAM database authentication on RDS instance
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
      "Resource": "arn:aws:rds-db:region:account:dbuser:db-instance-id/db-username"
    }
  ]
}
```

**Cross-Service Integration:**

- Use AWS Secrets Manager for credential rotation
- Integrate with AWS CloudTrail for API call logging
- Configure VPC security groups for network-level access control
- Enable Enhanced Monitoring for performance insights

### Network Security

**VPC Configuration:**

- Deploy RDS in private subnets only
- Configure DB subnet groups across multiple AZs
- Use VPC security groups instead of DB security groups
- Implement least-privilege security group rules

**Connection Security:**

- Enable SSL/TLS encryption in transit for all connections
- Use VPC endpoints for AWS service communications
- Configure connection timeouts and limits
- Monitor connection patterns for anomalies

### Monitoring and Auditing

**Database-Level Auditing:**

- Enable database audit logs for all administrative actions
- Configure log retention policies (minimum 90 days)
- Monitor failed login attempts and privilege escalations
- Set up alerts for suspicious administrative activities

**AWS-Level Monitoring:**

- Enable CloudTrail for all RDS API calls
- Configure CloudWatch alarms for administrative events
- Use AWS Config rules for compliance monitoring
- Implement AWS GuardDuty for threat detection

### Backup and Recovery Security

**Automated Backups:**

- Enable automated backups with encryption
- Configure backup retention period (7-35 days)
- Use cross-region backup replication for DR
- Encrypt backup snapshots with customer-managed KMS keys

**Manual Snapshots:**

- Encrypt all manual snapshots
- Implement snapshot sharing controls
- Regular testing of snapshot restoration procedures
- Document recovery time objectives (RTO) and recovery point objectives (RPO)

### Compliance Requirements

**FedRAMP Controls Addressed:**

- AC-2: Account Management
- AC-3: Access Enforcement
- AC-6: Least Privilege
- AU-2: Audit Events
- AU-3: Content of Audit Records
- IA-2: Identification and Authentication
- SC-8: Transmission Confidentiality
- SC-28: Protection of Information at Rest

**Implementation Validation:**

- Regular access reviews (quarterly minimum)
- Penetration testing of database security
- Compliance scanning and vulnerability assessments
- Documentation of security configurations and procedures

### Implementation Checklist

☐ Configure strong master user credentials
☐ Enable IAM database authentication where supported
☐ Implement engine-specific security configurations
☐ Configure VPC and security group restrictions
☐ Enable SSL/TLS encryption in transit
☐ Set up comprehensive audit logging
☐ Configure automated encrypted backups
☐ Implement monitoring and alerting
☐ Document administrative procedures
☐ Conduct regular security reviews

This comprehensive guidance ensures that Amazon RDS administrative accounts are configured according to security best practices and FedRAMP requirements across all supported database engines.

## FRR-RSC-02: Administrative Settings

**Applicable:** Yes

### Security-Related Settings Restricted to Master User

The master user account in Amazon RDS has elevated privileges specific to each database engine. The following operations and their security implications are restricted to the master user account. Note that RDS is a managed service, so some traditional database superuser operations are not available.

#### 1. User and Privilege Management (All Engines)

**Operations:**

- CREATE USER / CREATE ROLE
- DROP USER / DROP ROLE
- ALTER USER / ALTER ROLE
- GRANT and REVOKE privileges
- Password management for all database users
- Role membership management

**Security Implications:**

- Controls who can access the database instance
- Determines authentication methods and password policies
- Manages privilege escalation through role/privilege assignments
- Unauthorized user creation could lead to security breaches
- Improper privilege grants violate least privilege principles

#### 2. Database Creation and Management (All Engines)

**Operations:**

- CREATE DATABASE
- DROP DATABASE
- ALTER DATABASE
- Database ownership changes

**Security Implications:**

- Database owners have extensive privileges within their databases
- Unauthorized database creation could consume resources
- Database deletion results in permanent data loss
- Database-level settings affect all objects and users

#### 3. PostgreSQL-Specific Master User Operations

**Operations Restricted to rds_superuser Role:**

- CREATE EXTENSION / DROP EXTENSION (for supported extensions)
- ALTER EXTENSION
- CREATE EVENT TRIGGER / DROP EVENT TRIGGER
- Modify system catalogs (limited)
- Access to replication slots
- Logical replication configuration
- CREATE TABLESPACE (limited in RDS)

**Security Implications:**

- Extensions can introduce security vulnerabilities
- Event triggers execute with elevated privileges
- Replication access allows reading all database data
- System catalog access reveals database structure
- Tablespace management affects storage allocation

**Note:** RDS PostgreSQL master user has `rds_superuser` role, NOT full PostgreSQL superuser. Cannot access OS, modify pg_hba.conf, or perform certain system-level operations.

#### 4. MySQL-Specific Master User Operations

**Operations (Aurora MySQL Version 3):**

- CREATE ROLE / DROP ROLE
- GRANT/REVOKE role memberships
- SET_USER_ID privilege (impersonate users)
- ROLE_ADMIN privilege
- APPLICATION_PASSWORD_ADMIN
- CONNECTION_ADMIN
- REPLICATION CLIENT / REPLICATION SLAVE
- RELOAD privilege (flush operations)
- PROCESS privilege (view all connections)

**Security Implications:**

- Role management controls privilege inheritance
- SET_USER_ID allows user impersonation
- REPLICATION access enables data exfiltration
- PROCESS privilege reveals all active queries
- RELOAD can disrupt service or clear settings
- CONNECTION_ADMIN bypasses connection limits

**Note:** RDS MySQL master user does NOT have SUPER privilege. Cannot perform certain system-level operations or modify some global variables.

#### 5. SQL Server-Specific Master User Operations

**Operations:**

- CREATE LOGIN / DROP LOGIN
- ALTER LOGIN
- Server role management (limited)
- Database ownership changes
- SQL Server Agent job management
- Backup and restore operations
- Linked server configuration (limited)

**Security Implications:**

- Login management controls server-level access
- Server roles provide elevated privileges
- Database ownership affects object permissions
- Agent jobs execute with elevated privileges
- Backup access enables data exfiltration
- Linked servers can expose other systems

**Note:** RDS SQL Server master user is NOT a sysadmin. Cannot access OS, modify certain server configurations, or perform xp_cmdshell operations.

#### 6. Oracle-Specific Master User Operations

**Operations:**

- CREATE USER / DROP USER
- GRANT/REVOKE system privileges
- CREATE PROFILE / ALTER PROFILE
- Tablespace management
- Directory object management (limited)
- Scheduler job management
- Materialized view management

**Security Implications:**

- System privileges provide database-wide access
- Profiles enforce password and resource policies
- Tablespace management affects storage
- Directory objects enable file system access
- Scheduler jobs execute with elevated privileges
- Materialized views can expose sensitive data

**Note:** RDS Oracle master user is NOT SYS/SYSTEM. Cannot access OS, modify certain initialization parameters, or perform certain DBA operations.

#### 7. MariaDB-Specific Master User Operations

**Operations:**

- CREATE USER / DROP USER / ALTER USER
- CREATE ROLE / DROP ROLE
- GRANT/REVOKE privileges and role memberships
- SET PASSWORD for all users
- SHOW CREATE USER (version 11.4+)
- SHOW CREATE ROUTINE privilege (version 11.4+)
- CREATE TEMPORARY TABLES
- LOCK TABLES
- REPLICATION CLIENT / REPLICATION SLAVE
- PROCESS privilege (view all connections)
- RELOAD privilege (flush operations)
- EVENT privilege (create/modify scheduled events)
- TRIGGER privilege
- CREATE VIEW / SHOW VIEW

**Security Implications:**

- Role management enables hierarchical privilege structures
- PROCESS privilege reveals all active queries and connections
- REPLICATION access enables data exfiltration
- RELOAD can disrupt service or clear caches
- EVENT privilege allows scheduled task execution
- Trigger execution can bypass application logic
- View creation can expose or hide sensitive data
- Password management controls authentication security

**Note:** RDS MariaDB master user does NOT have SUPER privilege. Cannot perform certain system-level operations, modify some global variables, or access OS-level functions.

#### 8. IBM DB2-Specific Master User Operations

**Operations:**

- User and group management via rdsadmin procedures:
  - `rdsadmin.add_user` / `rdsadmin.remove_user`
  - `rdsadmin.add_groups` / `rdsadmin.remove_groups`
  - `rdsadmin.change_password`

- Role management:
  - `rdsadmin.create_role` / `rdsadmin.drop_role`
  - `rdsadmin.grant_role` / `rdsadmin.revoke_role`

- Database authorization grants:
  - `rdsadmin.dbadm_grant` / `rdsadmin.dbadm_revoke`
  - Grant DBADM, ACCESSCTRL, DATAACCESS authorities

- Schema and object creation
- Tablespace management (limited)
- Workload management configuration
- Audit policy configuration

**Security Implications:**

- Group-based access model requires careful group management
- DBADM authority provides extensive database control
- ACCESSCTRL authority manages security policies
- DATAACCESS authority enables reading all data
- Role grants can cascade privileges to multiple users
- Audit configuration affects compliance and forensics
- Workload management impacts resource allocation
- Schema ownership determines object access control

**Note:** RDS DB2 master user has DBADM, SYSCTRL, SYSMAINT, and SYSMON authorities but NOT SYSADM. Cannot access OS, modify certain database manager configuration parameters, or perform certain instance-level operations.

#### 9. Parameter Group Management (All Engines)

**Operations:**

- Create custom DB parameter groups
- Modify parameter group settings
- Apply parameter groups to instances
- Configure engine-specific security parameters

**Security Implications:**

- Parameter changes affect instance behavior and security
- Some parameters require instance reboot
- Security-related parameters (SSL, authentication, logging)
- Incorrect parameters could impact availability or security

#### 10. Backup and Recovery Operations (All Engines)

**Operations:**

- Configure automated backup retention
- Create manual snapshots
- Delete snapshots
- Copy snapshots to other regions
- Restore from snapshots
- Point-in-time recovery

**Security Implications:**

- Backup retention affects recovery capabilities
- Snapshot access enables data exfiltration
- Cross-region copies may violate data residency
- Restore operations can overwrite existing data
- Snapshot sharing requires careful access control

#### 11. Replication and High Availability (All Engines)

**Operations:**

- Configure read replicas
- Promote read replicas
- Enable Multi-AZ deployment
- Configure replication settings
- Manage replication lag

**Security Implications:**

- Replication provides access to all database data
- Read replicas may have different security settings
- Multi-AZ failover affects availability
- Replication lag can impact data consistency
- Replica promotion changes cluster topology

#### 12. Audit and Logging Configuration (All Engines)

**Operations:**

- Enable/disable database audit logging
- Configure log retention and export
- Set logging parameters (connections, statements, errors)
- Export logs to CloudWatch Logs

**Security Implications:**

- Disabling audit logs could hide malicious activity
- Log data contains sensitive query information
- Log retention affects compliance requirements
- CloudWatch export requires IAM permissions
- Audit settings are critical for forensics

### Best Practices for RDS Master User Account Security

1. **Minimize Master User Usage**
   - Never use master user directly in applications
   - Create application-specific users with minimal privileges
   - Reserve master user for administrative tasks only
   - Use engine-specific RBAC for fine-grained access

2. **Secure Master User Credentials**
   - Use AWS Secrets Manager for password management
   - Enable automatic password rotation (90 days maximum)
   - Use strong, randomly generated passwords (minimum 20 characters)
   - Never hardcode master credentials in application code

3. **Enable Multi-Factor Authentication**
   - Require MFA for AWS Console access to modify master password
   - Implement MFA for IAM users who can modify DB instances
   - Use IAM database authentication where supported (PostgreSQL/MySQL)

4. **Audit Master User Activity**
   - Enable comprehensive database audit logging
   - Monitor all master user connections and operations
   - Set up CloudWatch alarms for master user activity
   - Review audit logs regularly for unauthorized access

5. **Implement Least Privilege**
   - Create role-based access with minimal required privileges
   - Grant privileges at the most granular level possible
   - Use engine-specific roles appropriately
   - Document all privilege grants and their justifications

6. **Network Security**
   - Deploy RDS in private subnets only
   - Use VPC security groups to restrict database access
   - Never make RDS instances publicly accessible
   - Enforce SSL/TLS for all client connections

7. **Compliance and Documentation**
   - Document all master user operations
   - Maintain audit trail of privilege changes
   - Conduct quarterly access reviews
   - Implement change management for security settings

### Engine-Specific Limitations in RDS

**Important:** RDS is a managed service. The master user does NOT have full superuser/admin privileges:

**PostgreSQL:**

- Cannot access OS or modify pg_hba.conf
- Cannot install arbitrary extensions (only AWS-supported)
- Cannot modify certain system parameters
- Has `rds_superuser` role, not full superuser

**MySQL:**

- Cannot use SUPER privilege
- Cannot access mysql.user table directly for some operations
- Cannot modify certain global variables
- Cannot perform OS-level operations

**MariaDB:**

- Cannot use SUPER privilege
- Cannot access mysql.user table directly for some operations
- Cannot modify certain global variables
- Cannot perform OS-level operations
- Limited access to performance_schema and information_schema tables

**SQL Server:**

- Not a member of sysadmin role
- Cannot use xp_cmdshell
- Cannot access OS or file system directly
- Limited server-level configuration access

**Oracle:**

- Not SYS or SYSTEM user
- Cannot access OS or modify certain init parameters
- Limited DBA operations
- Cannot perform certain maintenance tasks

**IBM DB2:**

- Not SYSADM user (has DBADM, SYSCTRL, SYSMAINT, SYSMON)
- Cannot access OS or modify database manager configuration
- Cannot perform instance-level operations
- Limited tablespace and storage management
- Must use rdsadmin procedures for user and role management

## FRR-RSC-03: Privileged Settings

**Applicable:** Yes

Within RDS you have two layers of privileged access. One layer is at the IAM layer, where you can limit what permissions a user has to operate within RDS. This section covers the priviliged settings for using the service itself and provides example IAM Policies that would allow for varying levels of access to the service. The second layer of privileged access is at the database engine layer itself which is covered in the other sections of this document.

## IAM Least Privilege Policies

This section provides sample IAM policies for implementing least privilege access to Amazon RDS resources across different operational roles and responsibilities.

### Policy Selection Guide

Choose the appropriate policy based on your role:

| Policy               | Use Case                                               | MFA Required     |
| -------------------- | ------------------------------------------------------ | ---------------- |
| Read-Only Access     | Auditors, compliance reviewers, monitoring dashboards  | No               |
| Operator Access      | Database operators performing routine management tasks | Yes              |
| Administrator Access | Database administrators with full management access    | Yes (1-hour max) |

### Read-Only Access Policy

**Use this for:** Auditors, compliance reviewers, monitoring dashboards

**Grants access to:**

- View database instance configurations
- List all RDS resources
- Describe database parameters and options
- Monitor database metrics

**Does NOT grant:**

- Start, stop, or reboot instances
- Modify database configurations
- Create or delete databases

**Testing this policy:**

```
# Verify read access works
aws rds describe-db-instances

# Verify write access is denied (should fail)
aws rds create-db-instance --db-instance-identifier test-db
```

**Policy JSON:**

**Purpose:** Provides read-only access to RDS resources for monitoring and auditing purposes.

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

### Operator Access Policy

**Use this for:** Database operators performing routine management tasks

**Grants access to:**

- All read-only permissions
- Start, stop, and reboot database instances
- Modify database instance configurations
- Create and restore snapshots

**Does NOT grant:**

- Delete database instances
- Modify security groups
- Change master passwords without proper authorization

**Testing this policy:**

```
# Verify operator access works (requires MFA)
aws rds stop-db-instance --db-instance-identifier my-database

# Verify admin access is denied (should fail)
aws rds delete-db-instance --db-instance-identifier my-database
```

**Policy JSON:**

**Purpose:** Provides operational access for routine database management tasks with MFA requirement.

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
        "rds:StartDBInstance",
        "rds:StopDBInstance",
        "rds:RebootDBInstance",
        "rds:ModifyDBInstance"
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

**Use this for:** Database administrators with full management access

**Grants access to:**

- All operator permissions
- Create and delete database instances
- Modify security groups and parameter groups
- Manage master passwords and encryption keys
- Configure cross-region replication

**Requires:**

- MFA with maximum 1-hour session duration

**Testing this policy:**

```
# Verify full admin access works (requires MFA)
aws rds create-db-instance --db-instance-identifier new-database --db-instance-class db.t3.micro --engine postgres
aws rds delete-db-instance --db-instance-identifier old-database --skip-final-snapshot
```

**Policy JSON:**

**Purpose:** Provides full administrative access with MFA and session time restrictions.

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

### Database Security Configuration

Configure Amazon RDS with comprehensive database security including encryption at rest and in transit, secure authentication, parameter groups, automated backups, and network isolation for relational database operations.

**Implementation Overview:** Amazon RDS security involves implementing encryption, access controls, network isolation, and comprehensive monitoring to protect database resources and meet compliance requirements.

**API Reference:**
`aws rds create-db-instance --storage-encrypted --kms-key-id`

**Control Mapping:** SC-28 (Protection of Information at Rest)

### Privileged Access Control

Amazon RDS requires implementation of privileged account security controls including least privilege access, multi-factor authentication for administrative operations, and comprehensive audit logging of privileged activities.

**Implementation Overview:** Amazon RDS privileged account security involves implementing strict access controls, monitoring privileged operations, and ensuring administrative activities are properly authenticated and logged.

#### Implementation Examples

**Step 1: Implement Least Privilege Access**

Configure Amazon RDS with minimal required permissions for administrative accounts:

```
# Create least privilege IAM policy for Amazon RDS administration
aws iam create-policy \
  --policy-name RDSAdminPolicy \
  --policy-document file://rds-admin-policy.json

# Attach policy to administrative role
aws iam attach-role-policy \
  --role-name RDSAdminRole \
  --policy-arn arn:aws:iam::account:policy/RDSAdminPolicy
```

**Step 2: Enable Multi-Factor Authentication**

Require MFA for all privileged operations and administrative access:

```
# MFA enforcement is configured through IAM policy conditions
# Verify MFA enforcement for privileged operations
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::account:role/RDSAdminRole \
  --action-names rds:CreateDBInstance \
  --context-entries ContextKeyName=aws:MultiFactorAuthPresent,ContextKeyValues=false,ContextKeyType=boolean
```

**Step 3: Configure Privileged Activity Monitoring**

Enable comprehensive logging and monitoring of all privileged account activities:

```
# Enable CloudTrail for API logging
aws cloudtrail create-trail \
  --name RDSPrivilegedAccess \
  --s3-bucket-name rds-audit-logs \
  --include-global-service-events \
  --is-multi-region-trail

# Configure CloudWatch alarms for privileged operations
aws logs create-log-group \
  --log-group-name /aws/rds/privileged-access \
  --retention-in-days 365
```

**API Reference:** Configure via IAM policies and Amazon RDS administrative APIs

**Control Mapping:** AC-6 (Least Privilege)

## FRR-RSC-04: Secure Defaults

**Applicable:** Yes

AWS services are designed with security in mind, providing multiple layers of security controls and encryption capabilities. However, AWS allows customers to define the security configuration of services and does not enforce a minimum security standard by default, enabling customers the flexibility to meet their specific business requirements and compliance needs.

Amazon RDS should be configured using the above AWS Security Best Practice recommendations. AWS allows customers to define the security of services, and does not enforce a minimum security standard by default.

### Implementation Guidelines

Ensure Amazon RDS resources are created with security-first configurations that align with AWS security best practices and organizational compliance requirements.

**Security Configuration Best Practices:**

- Enable encryption at rest using customer-managed KMS keys
- Apply least privilege access policies for all database operations
- Enable comprehensive logging and monitoring for security events
- Use secure network configurations with private subnets and security groups
- Implement automated backup encryption with appropriate retention policies
- Configure SSL/TLS encryption for all database connections
- Enable Enhanced Monitoring for performance and security insights

## FRR-RSC-05: Configuration Comparison

**Applicable:** Yes

**Implementation Overview:** Use AWS Config rules, custom scripts, or third-party tools to compare current Amazon RDS configuration against established security baselines and compliance requirements.

### AWS Config Implementation

Deploy AWS Config rules to continuously monitor Amazon RDS compliance with organizational security standards:

**Configuration Monitoring Commands:**

```
# Describe RDS instances and compare against baseline
aws rds describe-db-instances \
  --query 'DBInstances[*].{InstanceId:DBInstanceIdentifier,Encrypted:StorageEncrypted,Engine:Engine}' \
  --output table

# Export configuration for comparison
aws rds describe-db-instances --output json > current-rds-config.json
```

### Automation Framework

- Use AWS Config conformance packs for automated compliance checking
- Implement custom Lambda functions for configuration drift detection
- Deploy AWS Systems Manager for configuration management
- Integrate with AWS Security Hub for centralized compliance reporting

## FRR-RSC-06: Configuration Export

**Applicable:** Yes

**Implementation Overview:** Export Amazon RDS configuration using AWS CLI describe commands in machine-readable JSON format for backup, audit, and Infrastructure as Code purposes.

### Export Procedures

**Export Format:** JSON via AWS CLI

**Primary Export Commands:**

```
# Export complete RDS configuration
aws rds describe-db-instances --output json > rds-instances.json
aws rds describe-db-parameter-groups --output json > rds-parameter-groups.json
aws rds describe-db-subnet-groups --output json > rds-subnet-groups.json
aws rds describe-db-security-groups --output json > rds-security-groups.json
```

**Configuration Export Use Cases:**

- Backup current configuration state
- Compare configurations across environments (dev, staging, production)
- Audit and compliance reporting requirements
- Infrastructure as Code template generation
- Disaster recovery planning and documentation

## FRR-RSC-07: API Configuration

**Applicable:** Yes

**Implementation Overview:** Amazon RDS security configurations are manageable through AWS APIs, CLI commands, and Infrastructure as Code tools, enabling automated and repeatable security implementations.

### Encryption Configuration

**API Command:**

```
# Create encrypted RDS instance
aws rds create-db-instance \
  --db-instance-identifier secure-database \
  --storage-encrypted \
  --kms-key-id alias/rds-encryption-key \
  --engine mysql \
  --db-instance-class db.t3.micro
```

**Control Mapping:** SC-28 (Protection of Information at Rest)

### Backup Configuration

**API Command:**

```
# Configure automated backups with retention
aws rds modify-db-instance \
  --db-instance-identifier secure-database \
  --backup-retention-period 7 \
  --preferred-backup-window "05:00-06:00"
```

**Control Mapping:** CP-9 (Information System Backup)

### Multi-AZ Configuration

**API Command:**

```
# Enable Multi-AZ deployment for high availability
aws rds modify-db-instance \
  --db-instance-identifier secure-database \
  --multi-az \
  --apply-immediately
```

**Control Mapping:** CP-6 (Alternate Processing Site)

### Implementation Guidance

**Role-Based Access Control:**

- Create separate IAM roles for different access levels (read-only, operator, administrator)
- Always require MFA for privileged operations and administrative access
- Use time-based conditions to limit session duration for administrative roles
- Apply resource-specific restrictions where possible to limit blast radius
- Regularly review and audit policy assignments and usage patterns
- Use AWS Access Analyzer to validate least privilege implementations

**Security Best Practices:**

- Start with read-only access and incrementally add permissions as needed
- Use AWS managed policies as a baseline when available and appropriate
- Implement just-in-time access for administrative operations
- Monitor policy usage with CloudTrail and Access Analyzer
- Document business justification for each permission granted
- Implement automated policy compliance checking and drift detection

## Additional Resources

For more information about AWS security best practices, see the following resources:

**AWS Security Documentation:**

- [AWS Security Documentation](../../../security.md "../../../security.md") - Comprehensive security guidance across all AWS services
- [AWS FedRAMP Compliance](../../../compliance/fedramp.md "../../../compliance/fedramp.md") - FedRAMP-specific compliance information and resources
- [AWS Well-Architected Security Pillar](../../../wellarchitected/latest/security-pillar/welcome.md "../../../wellarchitected/latest/security-pillar/welcome.md") - Security design principles and best practices

**Amazon RDS-Specific Resources:**

- [Amazon RDS Security Best Practices](../../../AmazonRDS/latest/UserGuide/CHAP_BestPractices.md "../../../AmazonRDS/latest/UserGuide/CHAP_BestPractices.md") - Service-specific security recommendations
- [IAM Database Authentication](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md") - Implementation guide for IAM-based database authentication
- [Amazon RDS Encryption](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md") - Encryption at rest and in transit configuration guidance

**Compliance and Governance:**

- [AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") - Automated compliance monitoring and evaluation
- [AWS CloudTrail User Guide](../../../cloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../cloudtrail/latest/userguide/cloudtrail-user-guide.md") - API logging and audit trail management
- [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") - Credential management and rotation automation
