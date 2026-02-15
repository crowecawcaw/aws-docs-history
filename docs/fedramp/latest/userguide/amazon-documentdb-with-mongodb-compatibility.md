# Amazon Documentdb With Mongodb Compatibility

This guide provides security configuration requirements and implementation examples for Amazon Documentdb With Mongodb Compatibility in accordance with FedRAMP requirements.

## Document Information

|                   |                              |
| ----------------- | ---------------------------- |
| Version           | 1.0.0                        |
| Last Updated      | 2025-12-23                   |
| Documentation URL | https://docs.aws.amazon.com/ |

## Overview

Amazon DocumentDB security configuration involves implementing comprehensive security controls including encryption, access management, master user authentication, and monitoring to meet FedRAMP compliance requirements. This guidance covers master user account security, MongoDB-compatible administrative operations, and privileged access controls for document database operations.

**Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

**Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements

Amazon DocumentDB must comply with the following FedRAMP requirements:

- FRR-RSC-01
- FRR-RSC-02
- FRR-RSC-03
- FRR-RSC-04
- FRR-RSC-05
- FRR-RSC-06
- FRR-RSC-07

## Administrative Account Model

Amazon DocumentDB has an administrative account model through master user accounts and MongoDB-compatible administrative operations.

|                         |                                                                       |
| ----------------------- | --------------------------------------------------------------------- |
| Administrative Accounts | Yes                                                                   |
| Account Type            | Master user account with MongoDB-compatible administrative privileges |

## FRR-RSC-01: Administrative Accounts

**Applicable:** Yes

Amazon DocumentDB Administrative Account Security Configuration

### OVERVIEW

Amazon DocumentDB administrative access is managed through the master user account and AWS IAM roles for cluster management operations. This guidance provides comprehensive security recommendations for securing administrative access to DocumentDB clusters with MongoDB compatibility.

### MASTER USER ACCOUNT SECURITY

1. Master User Account Configuration:
   - Use strong, randomly generated passwords (minimum 20 characters)
   - Rotate master passwords regularly (every 90 days maximum)
   - Store passwords in AWS Secrets Manager with automatic rotation
   - Never use default or predictable usernames (avoid 'admin', 'root', 'mongodb')

2. Authentication Methods:
   - Configure master user with appropriate MongoDB-compatible privileges
   - Use AWS Secrets Manager for password management
   - Implement MongoDB-compatible authentication mechanisms
   - Configure client applications to use secure authentication

### MONGODB-COMPATIBLE ADMINISTRATIVE SECURITY

- DocumentDB-Specific Configuration \*\*
  - Master User: Create with dbAdminAnyDatabase and readWriteAnyDatabase roles
  - TLS Encryption: Enable TLS for all client connections (required)
  - Connection Security: Configure connection limits and timeouts
  - Database Roles: Implement MongoDB-compatible role-based access control
  - Audit Logging: Enable profiler for administrative operations
  - Network Security: Deploy in private subnets with restrictive security groups

### AWS IAM INTEGRATION

1. Cluster Management Access:
   - Create IAM policies with least privilege DocumentDB permissions
   - Use IAM roles for administrative operations
   - Implement MFA requirements for privileged operations
   - Example policy for cluster administration:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "docdb:CreateDBCluster",
           "docdb:ModifyDBCluster",
           "docdb:DescribeDBClusters"
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

2. Cross-Service Integration:
   - Use AWS Secrets Manager for credential rotation
   - Integrate with AWS CloudTrail for API call logging
   - Configure VPC security groups for network-level access control
   - Enable CloudWatch monitoring for performance insights

### NETWORK SECURITY

1. VPC Configuration:
   - Deploy DocumentDB in private subnets only
   - Configure DB subnet groups across multiple AZs
   - Use VPC security groups with least privilege rules
   - Implement network ACLs for additional security layers

2. Connection Security:
   - Enable TLS encryption for all connections (mandatory)
   - Use VPC endpoints for AWS service communications
   - Configure connection timeouts and limits
   - Monitor connection patterns for anomalies

### MONITORING AND AUDITING

1. Database-Level Monitoring:
   - Enable profiler for administrative operations
   - Configure log retention policies (minimum 90 days)
   - Monitor failed authentication attempts
   - Set up alerts for suspicious administrative activities

2. AWS-Level Monitoring:
   - Enable CloudTrail for all DocumentDB API calls
   - Configure CloudWatch alarms for administrative events
   - Use AWS Config rules for compliance monitoring
   - Implement AWS GuardDuty for threat detection

### BACKUP AND RECOVERY SECURITY

1. Automated Backups:
   - Enable automatic backups with encryption
   - Configure backup retention period (7-35 days)
   - Use cross-region backup replication for DR
   - Encrypt backup snapshots with customer-managed KMS keys

2. Manual Snapshots:
   - Encrypt all manual snapshots
   - Implement snapshot sharing controls
   - Regular testing of snapshot restoration procedures
   - Document recovery time objectives (RTO) and recovery point objectives (RPO)

### COMPLIANCE REQUIREMENTS

1. FedRAMP Controls Addressed:
   - AC-2: Account Management
   - AC-3: Access Enforcement
   - AC-6: Least Privilege
   - AU-2: Audit Events
   - AU-3: Content of Audit Records
   - IA-2: Identification and Authentication
   - SC-8: Transmission Confidentiality
   - SC-28: Protection of Information at Rest

2. Implementation Validation:
   - Regular access reviews (quarterly minimum)
   - Security assessments of cluster configurations
   - Compliance scanning and vulnerability assessments
   - Documentation of security configurations and procedures

### IMPLEMENTATION CHECKLIST

☐ Configure strong master user credentials
☐ Enable TLS encryption for all connections
☐ Configure MongoDB-compatible role-based access control
☐ Configure VPC and security group restrictions
☐ Enable comprehensive monitoring and logging
☐ Configure automated encrypted backups
☐ Implement IAM least privilege policies
☐ Document administrative procedures
☐ Conduct regular security reviews

This comprehensive guidance ensures that Amazon DocumentDB administrative accounts are configured according to security best practices and FedRAMP requirements.

## FRR-RSC-02: Administrative Settings

**Applicable:** Yes

### Security-Related Settings Restricted to Master User (Primary User with root role)

The master user account (primary user) in Amazon DocumentDB has the MongoDB-compatible `root` role, which provides elevated privileges that cannot be delegated to regular database users. The following operations and their security implications are restricted to accounts with the root role:

#### 1. User and Role Management

**Operations:**

- `db.createUser()` - Create new database users
- `db.dropUser()` - Remove database users
- `db.updateUser()` - Modify user attributes and passwords
- `db.grantRolesToUser()` - Assign roles to users
- `db.revokeRolesFromUser()` - Remove roles from users
- `db.createRole()` - Create custom roles (user-defined roles)
- `db.dropRole()` - Remove custom roles

**Security Implications:**

- Controls who can access the database cluster
- Determines authentication methods and password policies
- Manages privilege escalation through role assignments
- Unauthorized user creation could lead to security breaches
- Improper role grants could violate least privilege principles
- User management is always performed in the context of the admin database

#### 2. Database Creation and Management

**Operations:**

- Create new databases
- Drop databases
- Clone databases
- Modify database-level settings

**Security Implications:**

- Database owners have extensive privileges within their databases
- Unauthorized database creation could consume resources
- Database deletion could result in data loss
- Database-level settings affect all collections and users

#### 3. Collection and Index Management

**Operations:**

- Create and drop collections across all databases
- Create and drop indexes on any collection
- Modify collection options and validation rules
- Manage capped collections

**Security Implications:**

- Index management affects query performance and resource usage
- Collection deletion results in permanent data loss
- Validation rules enforce data integrity constraints
- Improper index management could impact cluster performance

#### 4. Profiler and Audit Configuration

**Operations:**

- Enable/disable profiler for query logging
- Configure profiler threshold and sampling rate
- Set profiler level (off, slowOp, all)
- Manage audit log settings

**Security Implications:**

- Disabling profiler could hide malicious activity
- Improper profiler configuration may miss security events
- Profiler data contains sensitive query information
- Audit settings are critical for compliance requirements

#### 5. Cluster-Wide Administrative Operations

**Operations:**

- `db.shutdownServer()` - Shutdown operations (restricted in DocumentDB)
- `db.fsyncLock()` / `db.fsyncUnlock()` - Filesystem operations
- `db.currentOp()` - View all running operations
- `db.killOp()` - Terminate operations
- Server status and diagnostic commands

**Security Implications:**

- Viewing current operations reveals all active queries and data
- Killing operations could disrupt legitimate workloads
- Administrative commands can impact cluster availability
- Diagnostic information may expose sensitive metadata

#### 6. Replication and Backup Operations

**Operations:**

- Access to oplog (operations log)
- Replication status and configuration
- Backup and restore operations
- Point-in-time recovery management

**Security Implications:**

- Oplog access allows reading all database changes
- Replication information reveals cluster topology
- Backup access could enable unauthorized data exfiltration
- Restore operations can overwrite existing data

#### 7. Role-Based Access Control (RBAC) Management

**Operations:**

- Grant database-wide roles (readAnyDatabase, readWriteAnyDatabase, dbAdminAnyDatabase)
- Manage built-in roles across all databases
- Create and manage user-defined roles
- View role privileges and inheritance

**Security Implications:**

- Database-wide roles provide access to all databases
- Role inheritance can create unexpected privilege escalation
- User-defined roles require careful privilege design
- Role misconfiguration could violate security policies

### Best Practices for Master User Account Security

1. **Minimize Master User Usage**
   - Never use master user directly in applications
   - Create application-specific users with minimal required privileges
   - Reserve master user for administrative tasks only
   - Use MongoDB-compatible RBAC for fine-grained access control

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
   - Enable profiler for comprehensive query logging
   - Monitor all master user connections and operations
   - Set up CloudWatch alarms for master user activity
   - Review profiler logs regularly for unauthorized access

5. **Implement Least Privilege**
   - Create role-based access with minimal required privileges
   - Use built-in roles (read, readWrite, dbAdmin) appropriately
   - Grant privileges at the most granular level possible
   - Document all privilege grants and their justifications

6. **Network Security**
   - Deploy DocumentDB in private subnets only
   - Use VPC security groups to restrict database access
   - Never make DocumentDB clusters publicly accessible
   - Enforce TLS for all client connections (mandatory)

7. **Compliance and Documentation**
   - Document all master user operations
   - Maintain audit trail of privilege changes
   - Conduct quarterly access reviews
   - Implement change management for security settings

## FRR-RSC-03: Privileged Settings

**Applicable:** Yes

Within DocumentDB you have two layers of privileged access. One layer is at the IAM layer, where you can limit what permissions a user has to operate within RDS. This section covers the priviliged settings for using the service itself and provides example IAM Policies that would allow for varying levels of access to the service. The second layer of privileged access is at the database engine layer itself which is covered in the other sections of this document.

## IAM Least Privilege Policies

Sample IAM policies for least privilege access to Amazon DocumentDB

### Policy Selection Guide

Choose the appropriate policy based on your role:

| Policy        | Use Case                                              | MFA Required     |
| ------------- | ----------------------------------------------------- | ---------------- |
| Read Only     | Auditors, compliance reviewers, monitoring dashboards | No               |
| Operator      | Day-to-day operators managing resources               | Yes              |
| Administrator | Service administrators with full management access    | Yes (1-hour max) |

### Read Only Policy

**Use this for:** Auditors, compliance reviewers, monitoring dashboards

**Grants access to:**

- View resource configurations
- List resources
- Describe resource details

**Does NOT grant:**

- Create or modify resources
- Delete resources
- Change configurations

**Testing this policy:**

```
# Verify access works
aws documentdb-with-mongodb-compatibility describe-* / list-*

# Verify restricted access is denied (should fail)
aws documentdb-with-mongodb-compatibility create-* / delete-*
```

**Policy JSON:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "docdb:Describe*",
        "docdb:List*"
      ],
      "Resource": "*"
    }
  ]
}
```

### Operator Policy

**Use this for:** Day-to-day operators managing resources

**Grants access to:**

- All read-only permissions
- Create and modify resources
- Perform operational tasks

**Does NOT grant:**

- Delete critical resources
- Change security configurations
- Manage access policies

**Testing this policy:**

```
# Verify access works
aws documentdb-with-mongodb-compatibility create-* / update-*

# Verify restricted access is denied (should fail)
aws documentdb-with-mongodb-compatibility delete-* / put-*-policy
```

**Policy JSON:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "docdb:Describe*",
        "docdb:List*",
        "docdb:ModifyDBCluster",
        "docdb:ModifyDBInstance",
        "docdb:RebootDBInstance",
        "docdb:CreateDBClusterSnapshot",
        "docdb:DeleteDBClusterSnapshot"
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

### Administrator Policy

**Use this for:** Service administrators with full management access

**Grants access to:**

- All operator permissions
- Delete resources
- Manage access policies
- Configure security settings

**Requires:**

- MFA with maximum 1-hour session duration

**Testing this policy:**

```
# Verify access works
aws documentdb-with-mongodb-compatibility * (all operations)
```

**Policy JSON:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "docdb:*",
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

### Master User Authentication and Database Security

Amazon DocumentDB requires comprehensive master user security, TLS encryption, and MongoDB-compatible administrative controls for secure document database operations.

**Implementation Overview:** DocumentDB security involves master user account management, TLS encryption, MongoDB-compatible role-based access control, and comprehensive audit logging for document database operations.

#### Implementation Examples

1. **Create KMS Key and Secure Master User Configuration**

Create dedicated KMS key and configure secure master user for DocumentDB cluster

```
# Create KMS key for DocumentDB encryption
aws kms create-key \
  --description 'DocumentDB Encryption Key' \
  --key-usage ENCRYPT_DECRYPT \
  --key-spec SYMMETRIC_DEFAULT

# Create alias for the key
aws kms create-alias \
  --alias-name alias/documentdb-key \
  --target-key-id <key-id>

# Store master user password in Secrets Manager
aws secretsmanager create-secret \
  --name documentdb/master-user \
  --description 'DocumentDB master user credentials' \
  --secret-string '{"username":"docdbadmin","password":"'$(openssl rand -base64 32)'"}'
```

2. **Create Encrypted DocumentDB Cluster with Secure Configuration**

Create DocumentDB cluster with encryption enabled and secure master user configuration

```
# Retrieve master user credentials from Secrets Manager
MASTER_CREDS=$(aws secretsmanager get-secret-value \
  --secret-id documentdb/master-user \
  --query 'SecretString' --output text)

MASTER_USERNAME=$(echo $MASTER_CREDS | jq -r '.username')
MASTER_PASSWORD=$(echo $MASTER_CREDS | jq -r '.password')

# Create encrypted DocumentDB cluster
aws docdb create-db-cluster \
  --db-cluster-identifier secure-documentdb-cluster \
  --engine docdb \
  --engine-version 5.0.0 \
  --master-username "$MASTER_USERNAME" \
  --master-user-password "$MASTER_PASSWORD" \
  --storage-encrypted \
  --kms-key-id alias/documentdb-key \
  --vpc-security-group-ids sg-xxxxxxxxx \
  --db-subnet-group-name private-docdb-subnet-group \
  --backup-retention-period 7 \
  --preferred-backup-window "05:00-06:00" \
  --preferred-maintenance-window "sun:06:00-sun:07:00" \
  --deletion-protection \
  --tags Key=DataClassification,Value=Sensitive Key=BackupRequired,Value=true

# Create DocumentDB instances
aws docdb create-db-instance \
  --db-instance-identifier secure-documentdb-instance-1 \
  --db-instance-class db.r6g.large \
  --engine docdb \
  --db-cluster-identifier secure-documentdb-cluster \
  --monitoring-interval 60 \
  --monitoring-role-arn arn:aws:iam::account:role/rds-monitoring-role \
  --tags Key=Role,Value=Primary
```

3. **Configure TLS Encryption and MongoDB-Compatible Security**

Enable TLS for client connections and configure MongoDB-compatible security features

```
# Download DocumentDB CA certificate for TLS connections
wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem

# Create parameter group with secure settings
aws docdb create-db-cluster-parameter-group \
  --db-cluster-parameter-group-name secure-docdb-params \
  --db-parameter-group-family docdb5.0 \
  --description 'Secure DocumentDB parameter group'

# Configure profiler for audit logging
aws docdb modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name secure-docdb-params \
  --parameters ParameterName=profiler,ParameterValue=enabled \
  --parameters ParameterName=profiler_threshold_ms,ParameterValue=100 \
  --parameters ParameterName=profiler_sampling_rate,ParameterValue=1.0

# Apply parameter group to cluster
aws docdb modify-db-cluster \
  --db-cluster-identifier secure-documentdb-cluster \
  --db-cluster-parameter-group-name secure-docdb-params \
  --apply-immediately

# Enable CloudWatch logs export
aws docdb modify-db-cluster \
  --db-cluster-identifier secure-documentdb-cluster \
  --cloudwatch-logs-export-configuration LogTypesToEnable=profiler \
  --apply-immediately
```

**API:**
`aws docdb create-db-cluster --storage-encrypted --kms-key-id alias/documentdb-key`

**Control:** SC-28, IA-2

### Privileged Access Control

Amazon DocumentDB requires implementation of privileged account security controls including least privilege access, multi-factor authentication for administrative operations, and comprehensive audit logging of privileged activities.

**Implementation Overview:** Amazon DocumentDB privileged account security involves implementing strict access controls for cluster administration, monitoring privileged operations, and ensuring administrative activities are properly authenticated and logged.

#### Implementation Examples

1. **Implement Least Privilege Access**

Configure Amazon DocumentDB with minimal required permissions for administrative accounts

```
# Create least privilege IAM policy for DocumentDB administration
cat > documentdb-admin-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "docdb:CreateDBCluster",
        "docdb:ModifyDBCluster",
        "docdb:DescribeDBClusters",
        "docdb:CreateDBInstance",
        "docdb:ModifyDBInstance",
        "docdb:DescribeDBInstances",
        "docdb:CreateDBClusterSnapshot",
        "docdb:DescribeDBClusterSnapshots"
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
EOF

aws iam create-policy \
  --policy-name DocumentDBAdminPolicy \
  --policy-document file://documentdb-admin-policy.json

# Attach policy to administrative role
aws iam attach-role-policy \
  --role-name DocumentDBAdminRole \
  --policy-arn arn:aws:iam::account:policy/DocumentDBAdminPolicy
```

2. **Enable Multi-Factor Authentication**

Require MFA for all privileged operations and administrative access

```
# MFA enforcement is configured through IAM policy conditions
# Verify MFA enforcement for privileged operations
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::account:role/DocumentDBAdminRole \
  --action-names docdb:CreateDBCluster \
  --context-entries ContextKeyName=aws:MultiFactorAuthPresent,ContextKeyValues=false,ContextKeyType=boolean
```

3. **Configure Privileged Activity Monitoring**

Enable comprehensive logging and monitoring of all privileged account activities

```
# Enable CloudTrail for API logging
aws cloudtrail create-trail \
  --name DocumentDBPrivilegedAccess \
  --s3-bucket-name documentdb-audit-logs \
  --include-global-service-events \
  --is-multi-region-trail \
  --enable-log-file-validation

# Configure CloudWatch alarms for privileged operations
aws logs create-log-group \
  --log-group-name /aws/documentdb/privileged-access \
  --retention-in-days 365

# Create metric filter for privileged operations
aws logs put-metric-filter \
  --log-group-name CloudTrail/DocumentDBPrivilegedAccess \
  --filter-name DocumentDBPrivilegedOperations \
  --filter-pattern '{ $.eventSource = "docdb.amazonaws.com" && $.userIdentity.type = "AssumedRole" }' \
  --metric-transformations \
    metricName=DocumentDBPrivilegedOperations,metricNamespace=Security/DocumentDB,metricValue=1
```

**API:**
`Configure via IAM policies and DocumentDB administrative APIs`

**Control:** AC-6

## FRR-RSC-04: Secure Defaults

**Applicable:** Yes

AWS services are designed with security in mind, providing multiple layers of security controls and encryption capabilities. However, AWS allows customers to define the security configuration of services and does not enforce a minimum security standard by default, enabling customers the flexibility to meet their specific business requirements and compliance needs.

Amazon DocumentDB should be configured with encryption enabled, strong master user credentials, TLS enforcement, and comprehensive audit logging by default.

### Implementation

Ensure DocumentDB clusters are created with security-first configurations including encryption, authentication, and monitoring

**Best Practices:**

- Enable encryption at rest using customer-managed KMS keys
- Use AWS Secrets Manager for master user password management
- Enforce TLS connections for all database access (mandatory)
- Enable profiler for comprehensive audit logging
- Deploy in private subnets with restrictive security groups
- Implement automated backup encryption
- Configure parameter groups with security-hardened settings
- Use MongoDB-compatible role-based access control for fine-grained permissions

## FRR-RSC-05: Configuration Comparison

**Applicable:** Yes

Use AWS Config rules or custom scripts to compare current Amazon Documentdb With Mongodb Compatibility configuration against baselines.

## FRR-RSC-06: Configuration Export

**Applicable:** Yes

Export Amazon Documentdb With Mongodb Compatibility configuration using AWS CLI describe/get commands in JSON format.

## FRR-RSC-07: API Configuration

**Applicable:** Yes

### Iam Permissions

**API Command:**

```
Configure via IAM policies for Amazon Documentdb With Mongodb Compatibility
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
