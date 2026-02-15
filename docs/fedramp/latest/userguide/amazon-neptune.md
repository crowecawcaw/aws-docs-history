# Amazon Neptune

This guide provides security configuration requirements and implementation examples for Amazon Neptune in accordance with FedRAMP requirements.

## Document Information

|                   |                                                                       |
| ----------------- | --------------------------------------------------------------------- |
| Version           | 1.0.0                                                                 |
| Last Updated      | 2026-01-09                                                            |
| Documentation URL | https://docs.aws.amazon.com/neptune/latest/userguide/get-started.html |

## Overview

Amazon Neptune security configuration involves implementing comprehensive security controls including encryption, access management, master user authentication, and monitoring to meet FedRAMP compliance requirements. This guidance covers master user account security, graph database administrative operations, and privileged access controls for Neptune graph database operations.

**Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

**Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements

Amazon Neptune must comply with the following FedRAMP requirements:

- FRR-RSC-01
- FRR-RSC-02
- FRR-RSC-03
- FRR-RSC-04
- FRR-RSC-05
- FRR-RSC-06
- FRR-RSC-07

## Administrative Account Model

Amazon Neptune has an administrative account model through master user accounts and graph database administrative operations.

|                         |                                                                   |
| ----------------------- | ----------------------------------------------------------------- |
| Administrative Accounts | Yes                                                               |
| Account Type            | Master user account with graph database administrative privileges |

## FRR-RSC-01: Administrative Accounts

**Applicable:** Yes

Amazon Neptune Administrative Account Security Configuration

### OVERVIEW

Amazon Neptune administrative access is managed through the master user account and AWS IAM roles for cluster management operations. This guidance provides comprehensive security recommendations for securing administrative access to Neptune graph database clusters.

### MASTER USER ACCOUNT SECURITY

1. Master User Account Configuration:
   - Use strong, randomly generated passwords (minimum 20 characters)
   - Rotate master passwords regularly (every 90 days maximum)
   - Store passwords in AWS Secrets Manager with automatic rotation
   - Never use default or predictable usernames (avoid 'admin', 'root', 'neptune')

2. Authentication Methods:
   - Configure master user with appropriate graph database privileges
   - Use AWS Secrets Manager for password management
   - Enable IAM database authentication where supported
   - Configure client applications to use secure authentication

### NEPTUNE GRAPH DATABASE ADMINISTRATIVE SECURITY

- Neptune-Specific Configuration \*\*
  - Master User: Create with full administrative privileges for graph operations
  - TLS Encryption: Enable HTTPS/TLS for all client connections (required)
  - Connection Security: Configure connection limits and timeouts
  - Query Languages: Secure access for both Gremlin and SPARQL endpoints
  - Audit Logging: Enable audit logs for administrative operations
  - Network Security: Deploy in private subnets with restrictive security groups

### AWS IAM INTEGRATION

1. Cluster Management Access:
   - Create IAM policies with least privilege Neptune permissions
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
           "neptune:CreateDBCluster",
           "neptune:ModifyDBCluster",
           "neptune:DescribeDBClusters"
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

2. Graph Database Authentication:
   - Enable IAM database authentication for Neptune clusters
   - Use temporary credentials for graph database access
   - Implement fine-grained access controls for graph operations
   - Configure Neptune-specific IAM policies for data access

3. Cross-Service Integration:
   - Use AWS Secrets Manager for credential rotation
   - Integrate with AWS CloudTrail for API call logging
   - Configure VPC security groups for network-level access control
   - Enable CloudWatch monitoring for performance insights

## FRR-RSC-02: Administrative Settings

**Applicable:** Yes

### Security-Related Settings Restricted to Master User and IAM Policies

Amazon Neptune uses a dual-layer security model: AWS IAM for cluster management operations and database-level authentication for graph data access. The following operations and their security implications require elevated privileges:

#### 1. Cluster Management Operations (IAM-Controlled)

**Operations:**

- `neptune:CreateDBCluster` - Create new Neptune clusters
- `neptune:DeleteDBCluster` - Delete Neptune clusters
- `neptune:ModifyDBCluster` - Modify cluster configuration
- `neptune:CreateDBInstance` - Add instances to cluster
- `neptune:DeleteDBInstance` - Remove instances from cluster
- `neptune:ModifyDBInstance` - Modify instance configuration
- `neptune:CreateDBClusterSnapshot` - Create manual snapshots
- `neptune:RestoreDBClusterFromSnapshot` - Restore from snapshots

**Security Implications:**

- Cluster creation/deletion affects data availability and costs
- Cluster modifications can impact security settings (encryption, IAM auth)
- Instance management affects cluster capacity and performance
- Snapshot operations enable backup and potential data exfiltration
- These operations require AWS IAM permissions, not database credentials

#### 2. IAM Database Authentication Management

**Operations:**

- Enable/disable IAM database authentication on cluster
- Grant `neptune-db:connect` permissions via IAM policies
- Configure IAM roles for database access
- Manage temporary credentials for graph operations

**Security Implications:**

- IAM authentication provides fine-grained access control
- Temporary credentials reduce credential exposure risk
- IAM policies control who can access graph data
- Misconfigured IAM policies could grant excessive access
- IAM authentication bypasses traditional username/password

#### 3. Graph Data Access Operations (IAM Data Plane)

**Operations:**

- `neptune-db:ReadDataViaQuery` - Read graph data using Gremlin/SPARQL
- `neptune-db:WriteDataViaQuery` - Write graph data
- `neptune-db:DeleteDataViaQuery` - Delete graph data
- `neptune-db:GetEngineStatus` - View engine status
- `neptune-db:GetQueryStatus` - View query execution status
- `neptune-db:CancelQuery` - Cancel running queries
- `neptune-db:GetStatisticsStatus` - Access statistics

**Security Implications:**

- Read access allows viewing all graph data
- Write access enables data modification and potential corruption
- Delete access can result in permanent data loss
- Query cancellation could disrupt legitimate operations
- Statistics reveal graph structure and usage patterns

#### 4. Parameter Group Management

**Operations:**

- Create custom DB cluster parameter groups
- Modify parameter group settings
- Apply parameter groups to clusters
- Configure Neptune-specific parameters (query timeout, audit logging)

**Security Implications:**

- Parameter changes affect cluster behavior and security
- Query timeout settings impact denial-of-service protection
- Audit logging configuration affects compliance
- Parameter modifications require cluster reboot
- Incorrect parameters could impact availability

#### 5. Network and Encryption Configuration

**Operations:**

- Configure VPC security groups
- Modify subnet groups
- Enable/disable encryption at rest (at cluster creation only)
- Configure KMS key for encryption
- Enable/disable HTTPS/TLS enforcement

**Security Implications:**

- Security group changes affect network access control
- Encryption settings cannot be changed after cluster creation
- KMS key access controls data encryption
- TLS enforcement is mandatory for Neptune
- Network misconfiguration could expose cluster publicly

#### 6. Backup and Recovery Operations

**Operations:**

- Configure automated backup retention period
- Create manual cluster snapshots
- Delete cluster snapshots
- Copy snapshots to other regions (Use AWS Backups)
- Restore cluster from snapshot
- Perform point-in-time recovery

**Security Implications:**

- Backup retention affects recovery capabilities
- Snapshot access enables data exfiltration
- Cross-region copies may violate data residency requirements
- Restore operations can overwrite existing data
- Snapshot sharing requires careful access control

#### 7. Monitoring and Audit Logging

**Operations:**

- Enable/disable audit logging
- Configure CloudWatch Logs export
- Set up CloudWatch alarms
- Enable Enhanced Monitoring
- Configure Performance Insights

**Security Implications:**

- Disabling audit logs could hide malicious activity
- Log data contains sensitive query information
- CloudWatch access requires separate IAM permissions
- Performance Insights reveals query patterns
- Monitoring configuration affects compliance posture

#### 8. Maintenance and Upgrade Operations

**Operations:**

- Apply engine version upgrades
- Configure maintenance windows
- Apply security patches
- Modify cluster availability settings
- Enable/disable deletion protection

**Security Implications:**

- Engine upgrades may introduce breaking changes
- Maintenance windows affect availability
- Security patches address known vulnerabilities
- Deletion protection prevents accidental data loss
- Upgrade operations require careful planning

### Best Practices for Neptune Administrative Security

1. **Separate Cluster and Data Access**
   - Use IAM roles for cluster management operations
   - Use IAM database authentication for graph data access
   - Never use AWS root account for Neptune operations
   - Implement separate roles for different access levels

2. **Secure Credential Management**
   - Use AWS Secrets Manager for any password-based authentication
   - Enable automatic credential rotation
   - Use temporary credentials via IAM database authentication
   - Never hardcode credentials in application code

3. **Enable Multi-Factor Authentication**
   - Require MFA for AWS Console access
   - Implement MFA for IAM users with Neptune permissions
   - Use time-based session restrictions for administrative roles
   - Enforce MFA for all privileged operations

4. **Comprehensive Audit Logging**
   - Enable audit logging for all graph operations
   - Export logs to CloudWatch Logs for retention
   - Set up CloudWatch alarms for suspicious activity
   - Review audit logs regularly for unauthorized access
   - Maintain logs for minimum 90 days

5. **Implement Least Privilege**
   - Grant minimal required IAM permissions
   - Use resource-specific IAM policies where possible
   - Separate read and write permissions
   - Implement just-in-time access for administrative operations
   - Regularly review and audit IAM policies

6. **Network Security**
   - Deploy Neptune in private subnets only
   - Use VPC security groups with least privilege rules
   - Never make Neptune clusters publicly accessible
   - Use VPC endpoints for AWS service communications
   - Enforce HTTPS/TLS for all connections (mandatory)

7. **Compliance and Documentation**
   - Document all administrative operations
   - Maintain audit trail of configuration changes
   - Conduct quarterly access reviews
   - Implement change management for security settings
   - Use AWS Config for configuration compliance monitoring

### Neptune-Specific Security Considerations

**Gremlin and SPARQL Access:**

- Both query languages have full access to graph data
- IAM policies control access to both endpoints
- Query complexity can impact cluster performance
- Implement query timeouts to prevent resource exhaustion

**IAM Database Authentication:**

- Provides temporary, token-based access
- Tokens expire after 15 minutes
- Eliminates need for password management
- Integrates with AWS IAM for centralized access control

**Cluster vs Instance Operations:**

- Cluster-level settings affect all instances
- Instance-level settings affect individual nodes
- Some operations require cluster reboot
- Plan maintenance windows for configuration changes

## FRR-RSC-03: Privileged Settings

**Applicable:** Yes

Within Neptune you have two layers of privileged access. One layer is at the IAM layer, where you can limit what permissions a user has to operate within Neptune. This section covers the priviliged settings for using the service itself and provides example IAM Policies that would allow for varying levels of access to the service. The second layer of privileged access is at the database engine layer itself which is covered in the other sections of this document.

## IAM Least Privilege Policies

Sample IAM policies for least privilege access to Amazon Neptune

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
aws neptune describe-* / list-*

# Verify restricted access is denied (should fail)
aws neptune create-* / delete-*
```

**Policy JSON:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "neptune:Describe*",
        "neptune:List*",
        "neptune:Get*"
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
aws neptune create-* / update-*

# Verify restricted access is denied (should fail)
aws neptune delete-* / put-*-policy
```

**Policy JSON:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "neptune:Describe*",
        "neptune:List*",
        "neptune:Get*",
        "neptune:Update*",
        "neptune:Put*"
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
aws neptune * (all operations)
```

**Policy JSON:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "neptune:*",
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

### Master User Authentication and Graph Database Security

Amazon Neptune requires comprehensive master user security, HTTPS/TLS encryption, and graph database administrative controls for secure graph database operations.

**Implementation Overview:** Neptune security involves master user account management, HTTPS/TLS encryption, IAM database authentication, and comprehensive audit logging for graph database operations supporting both Gremlin and SPARQL query languages.

#### Implementation Examples

1. **Configure Encryption and Secure Cluster Creation**

Set up Amazon Neptune cluster with comprehensive encryption, authentication, and security configurations

```
# Create customer-managed KMS key for Neptune encryption
aws kms create-key \
  --description 'Amazon Neptune Cluster Encryption Key' \
  --key-usage ENCRYPT_DECRYPT \
  --key-spec SYMMETRIC_DEFAULT

# Create alias for the KMS key
aws kms create-alias \
  --alias-name alias/neptune-encryption \
  --target-key-id arn:aws:kms:region:account:key/key-id

# Store master user credentials in Secrets Manager
aws secretsmanager create-secret \
  --name neptune/master-user \
  --description 'Neptune master user credentials' \
  --secret-string '{"username":"neptuneadmin","password":"'$(openssl rand -base64 32)'"}'

# Create DB subnet group for Neptune cluster
aws neptune create-db-subnet-group \
  --db-subnet-group-name neptune-secure-subnet-group \
  --db-subnet-group-description 'Secure subnet group for Neptune cluster' \
  --subnet-ids subnet-12345678 subnet-87654321 subnet-11223344 \
  --tags Key=Environment,Value=Production Key=Compliance,Value=FedRAMP
```

2. **Create Secure Neptune Cluster with Master User**

Create Neptune cluster with encryption and secure master user configuration

```
# Retrieve master user credentials from Secrets Manager
MASTER_CREDS=$(aws secretsmanager get-secret-value \
  --secret-id neptune/master-user \
  --query 'SecretString' --output text)

MASTER_USERNAME=$(echo $MASTER_CREDS | jq -r '.username')
MASTER_PASSWORD=$(echo $MASTER_CREDS | jq -r '.password')

# Create secure Neptune cluster with encryption
aws neptune create-db-cluster \
  --db-cluster-identifier secure-neptune-cluster \
  --engine neptune \
  --engine-version 1.3.1.0 \
  --master-username "$MASTER_USERNAME" \
  --master-user-password "$MASTER_PASSWORD" \
  --storage-encrypted \
  --kms-key-id alias/neptune-encryption \
  --vpc-security-group-ids sg-12345678 \
  --db-subnet-group-name neptune-secure-subnet-group \
  --backup-retention-period 7 \
  --preferred-backup-window '05:00-06:00' \
  --preferred-maintenance-window 'sun:06:00-sun:07:00' \
  --enable-iam-database-authentication \
  --deletion-protection \
  --tags Key=DataClassification,Value=Sensitive Key=BackupRequired,Value=true

# Create Neptune DB instances in the cluster
aws neptune create-db-instance \
  --db-instance-identifier secure-neptune-instance-1 \
  --db-instance-class db.r6g.large \
  --engine neptune \
  --db-cluster-identifier secure-neptune-cluster \
  --monitoring-interval 60 \
  --monitoring-role-arn arn:aws:iam::account:role/rds-monitoring-role \
  --performance-insights-enabled \
  --performance-insights-kms-key-id alias/neptune-encryption \
  --tags Key=Role,Value=Primary
```

3. **Configure IAM Database Authentication and Monitoring**

Set up IAM database authentication and comprehensive monitoring for Neptune

```
# Create IAM policy for Neptune database access
cat > neptune-db-access-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "neptune-db:connect",
        "neptune-db:ReadDataViaQuery",
        "neptune-db:WriteDataViaQuery"
      ],
      "Resource": "arn:aws:neptune-db:*:*:cluster-resource/secure-neptune-cluster/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
EOF

aws iam create-policy \
  --policy-name NeptuneDBAccessPolicy \
  --policy-document file://neptune-db-access-policy.json

# Enable CloudTrail logging for Neptune API calls
aws cloudtrail create-trail \
  --name neptune-audit-trail \
  --s3-bucket-name neptune-audit-logs-bucket \
  --include-global-service-events \
  --is-multi-region-trail \
  --enable-log-file-validation

# Enable Neptune audit logging
aws neptune modify-db-cluster \
  --db-cluster-identifier secure-neptune-cluster \
  --cloudwatch-logs-export-configuration LogTypesToEnable=audit \
  --apply-immediately

# Set up CloudWatch alarms for Neptune monitoring
aws cloudwatch put-metric-alarm \
  --alarm-name 'Neptune-High-CPU-Utilization' \
  --alarm-description 'Neptune instance CPU utilization is high' \
  --metric-name CPUUtilization \
  --namespace AWS/Neptune \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --dimensions Name=DBInstanceIdentifier,Value=secure-neptune-instance-1
```

**API:**
`aws neptune create-db-cluster --storage-encrypted --kms-key-id alias/neptune-encryption --enable-iam-database-authentication`

**Control:** SC-28, IA-2

### Privileged Access Control

Amazon Neptune requires implementation of privileged account security controls including least privilege access, multi-factor authentication for administrative operations, and comprehensive audit logging of privileged activities.

**Implementation Overview:** Amazon Neptune privileged account security involves implementing strict access controls for cluster administration, monitoring privileged operations, and ensuring administrative activities are properly authenticated and logged.

#### Implementation Examples

1. **Implement Least Privilege Access**

Configure Amazon Neptune with minimal required permissions for administrative accounts

```
# Create least privilege IAM policy for Neptune administration
cat > neptune-admin-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "neptune:CreateDBCluster",
        "neptune:ModifyDBCluster",
        "neptune:DescribeDBClusters",
        "neptune:CreateDBInstance",
        "neptune:ModifyDBInstance",
        "neptune:DescribeDBInstances",
        "neptune:CreateDBClusterSnapshot",
        "neptune:DescribeDBClusterSnapshots"
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
  --policy-name NeptuneAdminPolicy \
  --policy-document file://neptune-admin-policy.json

# Attach policy to administrative role
aws iam attach-role-policy \
  --role-name NeptuneAdminRole \
  --policy-arn arn:aws:iam::account:policy/NeptuneAdminPolicy
```

2. **Enable Multi-Factor Authentication**

Require MFA for all privileged operations and administrative access

```
# MFA enforcement is configured through IAM policy conditions
# Verify MFA enforcement for privileged operations
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::account:role/NeptuneAdminRole \
  --action-names neptune:CreateDBCluster \
  --context-entries ContextKeyName=aws:MultiFactorAuthPresent,ContextKeyValues=false,ContextKeyType=boolean
```

3. **Configure Privileged Activity Monitoring**

Enable comprehensive logging and monitoring of all privileged account activities

```
# Enable CloudTrail for API logging
aws cloudtrail create-trail \
  --name NeptunePrivilegedAccess \
  --s3-bucket-name neptune-audit-logs \
  --include-global-service-events \
  --is-multi-region-trail \
  --enable-log-file-validation

# Configure CloudWatch alarms for privileged operations
aws logs create-log-group \
  --log-group-name /aws/neptune/privileged-access \
  --retention-in-days 365

# Create metric filter for privileged operations
aws logs put-metric-filter \
  --log-group-name CloudTrail/NeptunePrivilegedAccess \
  --filter-name NeptunePrivilegedOperations \
  --filter-pattern '{ $.eventSource = "neptune.amazonaws.com" && $.userIdentity.type = "AssumedRole" }' \
  --metric-transformations \
    metricName=NeptunePrivilegedOperations,metricNamespace=Security/Neptune,metricValue=1
```

**API:**
`Configure via IAM policies and Neptune administrative APIs`

**Control:** AC-6

## FRR-RSC-04: Secure Defaults

**Applicable:** Yes

AWS allows customers to define Amazon Neptune security configurations, and does not enforce a minimum security standard by default. AWS services are designed with security in mind, but do not enforce a minimum security standard to allow customers freedom to meet their needed business requirements.

Amazon Neptune should be configured with encryption enabled, strong master user credentials, HTTPS/TLS enforcement, and comprehensive audit logging by default.

### Implementation

Ensure Neptune clusters are created with security-first configurations including encryption, authentication, and monitoring

**Best Practices:**

- Enable encryption at rest using customer-managed KMS keys
- Use AWS Secrets Manager for master user password management
- Enforce HTTPS/TLS connections for all database access (mandatory)
- Enable IAM database authentication for fine-grained access control
- Deploy in private subnets with restrictive security groups
- Implement automated backup encryption
- Configure comprehensive audit logging for graph operations
- Use least privilege IAM policies for both cluster and database access

## FRR-RSC-05: Configuration Comparison

**Applicable:** Yes

Use AWS Config rules or custom scripts to compare current Amazon Neptune configuration against baselines.

### AWS Config Implementation

Deploy AWS Config rules to continuously monitor Amazon Neptune compliance

**Comparison Commands:**

```
# List all Neptune DB clusters
aws neptune describe-db-clusters --output json
# List all Neptune DB instances
aws neptune describe-db-instances --output json
# List all Neptune DB cluster parameter groups
aws neptune describe-db-cluster-parameter-groups --output json
# List all Neptune DB parameter groups
aws neptune describe-db-parameter-groups --output json
# List all Neptune DB subnet groups
aws neptune describe-db-subnet-groups --output json
# Compare output against baseline configuration files
```

### Automation

Use AWS Config conformance packs or custom Lambda functions for automated comparison

## FRR-RSC-06: Configuration Export

**Applicable:** Yes

Export Amazon Neptune configuration using AWS CLI describe/get commands in JSON format.

### Export Format

JSON via AWS CLI

**Export Commands:**

```
# Export all Neptune DB clusters
aws neptune describe-db-clusters --output json > amazon_neptune_clusters.json
# Export all Neptune DB instances
aws neptune describe-db-instances --output json > amazon_neptune_instances.json
# Export all Neptune DB cluster parameter groups
aws neptune describe-db-cluster-parameter-groups --output json > amazon_neptune_cluster_parameter_groups.json
# Export all Neptune DB parameter groups
aws neptune describe-db-parameter-groups --output json > amazon_neptune_parameter_groups.json
# Export all Neptune DB subnet groups
aws neptune describe-db-subnet-groups --output json > amazon_neptune_subnet_groups.json
# Export all Neptune event subscriptions
aws neptune describe-event-subscriptions --output json > amazon_neptune_event_subscriptions.json
```

**Use Cases:**

- Backup current configuration
- Compare configurations across environments
- Audit and compliance reporting
- Infrastructure as Code generation

## FRR-RSC-07: API Configuration

**Applicable:** Yes

### Create Neptune Cluster

**API Command:**

```
aws neptune create-db-cluster \
  --db-cluster-identifier <cluster-name> \
  --storage-encrypted \
  --kms-key-id <kms-key-id>
```

**Control:** AC-6

### Create Neptune Instance

**API Command:**

```
aws neptune create-db-instance \
  --db-instance-identifier <instance-name> \
  --db-cluster-identifier <cluster-name> \
  --db-instance-class <instance-class>
```

**Control:** AC-6

### Enable IAM Database Authentication

**API Command:**

```
aws neptune modify-db-cluster \
  --db-cluster-identifier <cluster-name> \
  --enable-iam-database-authentication
```

**Control:** AC-6

**Implementation Guidance:**

- Create separate roles for different access levels (read-only, operator, administrator)
- Always require MFA for privileged operations
- Use time-based conditions to limit session duration
- Apply resource-specific restrictions where possible
- Regularly review and audit policy assignments
- Use AWS Access Analyzer to validate least privilege

**Best Practices:**

- Start with read-only access and add permissions as needed
- Use AWS managed policies as a baseline when available
- Implement just-in-time access for administrative operations
- Monitor policy usage with CloudTrail and Access Analyzer
- Document business justification for each permission

## Additional Resources

For more information about AWS security best practices, see the following resources:

- [AWS Security Documentation](../../../security.md "../../../security.md")
- [AWS FedRAMP Compliance](https://aws.amazon.com/compliance/fedramp/ "https://aws.amazon.com/compliance/fedramp/")
- [AWS Well-Architected Security Pillar](../../../wellarchitected/latest/security-pillar/welcome.md "../../../wellarchitected/latest/security-pillar/welcome.md")
