

# Amazon Aurora MySQL
<a name="amazon-aurora-mysql"></a>

This guide provides security configuration requirements and implementation examples for Amazon Aurora MySQL in accordance with FedRAMP requirements.

## Document Information
<a name="amazon_aurora_mysql_document_information"></a>


|  |  | 
| --- |--- |
| Version | 1.0.2 | 
| Last Updated | 2026-03-26 | 
| Documentation URL | https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html | 

## Overview
<a name="amazon_aurora_mysql_overview"></a>

Amazon Aurora MySQL security configuration involves implementing comprehensive security controls including encryption, access management, logging, and monitoring to meet FedRAMP compliance requirements. This guidance covers top-level administrative user account security, MySQL-specific administrative operations, and privileged access controls for Aurora MySQL database operations.

 **Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

 **Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements
<a name="amazon_aurora_mysql_fedramp_requirements"></a>

Amazon Aurora MySQL must comply with the following FedRAMP requirements:
+ SCG-CSO-RSC
+ SCG-CSO-SDF
+ SCG-ENH-CMP
+ SCG-ENH-EXP
+ SCG-ENH-API

## Administrative Account Model
<a name="amazon_aurora_mysql_administrative_account_model"></a>

Amazon Aurora MySQL has an administrative account model.


|  |  | 
| --- |--- |
| Administrative Accounts | Yes | 
| Account Type | Database Master User Account | 

## SCG-CSO-RSC: Recommended Secure Configuration
<a name="amazon_aurora_mysql_scg_cso_rsc_recommended_secure_configuration"></a>

 **Applicable:** Yes

This requirement consolidates guidance for: 1. Instructions on how to securely access, configure, operate, and decommission top-level administrative accounts 2. Explanations of security-related settings that can be operated only by top-level administrative accounts 3. Explanations of security-related settings that can be operated only by privileged accounts

### Part 1: Administrative Accounts
<a name="amazon_aurora_mysql_part_1_administrative_accounts"></a>

 **Applicable:** Yes

Amazon Aurora MySQL Administrative Account Security Configuration is applicable as there is a default administrator account created at cluster creation for Amazon Aurora MySQL clusters. This account has full access for what’s allowed in the Auror service. You can read more about these privileges in the AWS Documentation.

 [RDS Master account documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html) 

### Overview
<a name="amazon_aurora_mysql_overview_2"></a>

Amazon Aurora MySQL administrative access is managed through the Master database user account and AWS IAM roles. This guidance provides comprehensive security recommendations for securing administrative access to Aurora MySQL clusters.

### Master Database User Security
<a name="amazon_aurora_mysql_master_database_user_security"></a>

1. Master User Account Configuration:
   + Use strong, randomly generated passwords (minimum 20 characters)
   + Rotate master passwords regularly (every 90 days maximum)
   + Store passwords in AWS Secrets Manager with automatic rotation
   + Never use default or predictable usernames (avoid 'admin', 'root', 'mysql')

1. Authentication Methods:
   + Enable IAM database authentication where supported
   + Use AWS Secrets Manager for password management
   + Implement MySQL-specific authentication mechanisms
   + Where possible integrate with existing IdP solutions using Kerberos authentication

### MySQL Administrative Security
<a name="amazon_aurora_mysql_mysql_administrative_security"></a>
+ MySQL-Specific Configuration \*\*
  + Master user: Limit to necessary privileges, avoid SUPER privilege, existing priviliged are already limited in RDS, ensure you follow least privilege in your creation
  + Use secure authentication methods = Avoid MySQL native, leverage IAM and Kerberos authentication where possible
  + Enable SSL/TLS: require\_secure\_transport = ON
  + Enable comprehensive audit logging:
    + server\_audit\_logging = ON
    + server\_audit\_events = 'CONNECT,QUERY,TABLE'
    + server\_audit\_incl\_users = 'admin,root' - This shoudl reflect your master user name.
  + Set connection limits:
    + max\_connections appropriate for workload
    + max\_user\_connections per user limits
  + Configure password validation if using MySQL native (avoid if possible):
    + validate\_password.policy = STRONG - Only if not using Kerberos or IAM
    + validate\_password.length = 20
    + validate\_password.mixed\_case\_count = 2

### Part 2: Administrative Settings
<a name="amazon_aurora_mysql_part_2_administrative_settings"></a>

 **Applicable:** Yes

### Security-Related Settings Restricted to Master User
<a name="amazon_aurora_mysql_security_related_settings_restricted_to_master_user"></a>

The master user account in Amazon Aurora MySQL has elevated privileges that cannot be delegated to regular database users. The following operations and their security implications are restricted to the master user:

#### 1. User and Privilege Management
<a name="amazon_aurora_mysql_1_user_and_privilege_management"></a>

 **Operations:** 
+ CREATE USER
+ DROP USER
+ RENAME USER
+ GRANT ALL PRIVILEGES
+ REVOKE privileges
+ SET PASSWORD for other users
+ CREATE ROLE / DROP ROLE (Aurora MySQL 3.x)
+ GRANT/REVOKE role memberships (Aurora MySQL 3.x)

 **Security Implications:** 
+ Controls database access and authentication
+ Determines privilege levels for all users
+ Manages password policies and authentication methods
+ Unauthorized user creation could lead to data breaches
+ Improper privilege grants violate least privilege principles
+ Role mismanagement could enable privilege escalation

#### 2. Database Creation and Management
<a name="amazon_aurora_mysql_2_database_creation_and_management"></a>

 **Operations:** 
+ CREATE DATABASE
+ DROP DATABASE
+ ALTER DATABASE

 **Security Implications:** 
+ Database owners have extensive privileges within their databases
+ Unauthorized database creation could consume resources
+ Database deletion could result in data loss
+ Database-level settings affect all objects and users

#### 3. Replication Configuration
<a name="amazon_aurora_mysql_3_replication_configuration"></a>

 **Operations:** 
+ REPLICATION CLIENT privilege
+ REPLICATION SLAVE privilege
+ Binary log access and configuration
+ Read replica management

 **Security Implications:** 
+ Replication access allows reading all database data
+ Binary logs contain all data modifications
+ Could be used for unauthorized data exfiltration
+ Improper replication configuration could expose sensitive data

#### 4. Global System Variables
<a name="amazon_aurora_mysql_4_global_system_variables"></a>

 **Operations:** 
+ SET GLOBAL for security-related variables
+ Modification of authentication plugins
+ SSL/TLS configuration changes
+ Connection limits and timeouts

 **Security Implications:** 
+ Global variables affect all database connections
+ Authentication changes could weaken security
+ SSL/TLS misconfiguration could expose data in transit
+ Connection limit changes could enable denial of service

#### 5. Stored Procedure and Function Management
<a name="amazon_aurora_mysql_5_stored_procedure_and_function_management"></a>

 **Operations:** 
+ CREATE ROUTINE
+ ALTER ROUTINE
+ DROP ROUTINE
+ EXECUTE on privileged routines
+ SET\_USER\_ID privilege (Aurora MySQL 3.x)

 **Security Implications:** 
+ Stored procedures can execute with elevated privileges
+ Definer-rights procedures can bypass access controls
+ Malicious procedures could compromise database security
+ SET\_USER\_ID allows impersonation of other users

#### 6. Event Scheduler Management
<a name="amazon_aurora_mysql_6_event_scheduler_management"></a>

 **Operations:** 
+ CREATE EVENT
+ ALTER EVENT
+ DROP EVENT
+ EVENT privilege

 **Security Implications:** 
+ Events execute automatically with creator’s privileges
+ Could be used to implement backdoors
+ Malicious events could modify or exfiltrate data
+ Event scheduler access requires careful auditing

#### 7. Audit Logging Configuration
<a name="amazon_aurora_mysql_7_audit_logging_configuration"></a>

 **Operations:** 
+ Enabling/disabling server\_audit plugin
+ Configuring audit log events and filters
+ Managing audit log retention

 **Security Implications:** 
+ Disabling audit logging could hide malicious activity
+ Improper audit configuration may miss security events
+ Audit log tampering could compromise investigations
+ Audit settings are critical for compliance requirements

#### 8. Process and Connection Management
<a name="amazon_aurora_mysql_8_process_and_connection_management"></a>

 **Operations:** 
+ PROCESS privilege (view all connections)
+ RELOAD privilege (flush privileges, logs)
+ CONNECTION\_ADMIN (Aurora MySQL 3.x)
+ KILL connections

 **Security Implications:** 
+ PROCESS privilege reveals all active queries and data
+ RELOAD can disrupt service or clear security settings
+ CONNECTION\_ADMIN allows bypassing connection limits
+ KILL privilege could be used for denial of service

### Best Practices for Master User Account Security
<a name="amazon_aurora_mysql_best_practices_for_master_user_account_security"></a>

1.  **Minimize Master User Usage** 
   + Never use master user directly in applications
   + Create application-specific users with minimal required privileges
   + Reserve master user for administrative tasks only

1.  **Secure Master User Credentials** 
   + Use AWS Secrets Manager for password management
   + Enable automatic password rotation (90 days maximum)
   + Use strong, randomly generated passwords (minimum 20 characters)
   + Never hardcode master credentials in application code

1.  **Enable Multi-Factor Authentication** 
   + Require MFA for AWS Console access to modify master password
   + Implement MFA for IAM users who can modify DB clusters
   + Use IAM database authentication where possible

1.  **Audit Master User Activity** 
   + Enable comprehensive database audit logging
   + Monitor all master user connections and operations
   + Set up CloudWatch alarms for master user activity
   + Review audit logs regularly for unauthorized access

1.  **Implement Least Privilege** 
   + Create role-based access with minimal required privileges
   + Grant privileges at the most granular level possible
   + Regularly review and revoke unnecessary privileges
   + Document all privilege grants and their justifications

1.  **Network Security** 
   + Deploy Aurora in private subnets only
   + Use VPC security groups to restrict database access
   + Never make Aurora clusters publicly accessible
   + Use VPC endpoints for AWS service communications

1.  **Compliance and Documentation** 
   + Document all master user operations
   + Maintain audit trail of privilege changes
   + Conduct quarterly access reviews
   + Implement change management for security settings

### Part 3: Privileged Settings
<a name="amazon_aurora_mysql_part_3_privileged_settings"></a>

 **Applicable:** Yes

Within Aurora you have two layers of privileged access. One layer is at the IAM layer, where you can limit what permissions a user has to operate within RDS. This section covers the priviliged settings for using the service itself and provides example IAM Policies that would allow for varying levels of access to the service. The second layer of privileged access is at the database engine layer itself which is covered in the other sections of this document.

## IAM Least Privilege Policies
<a name="amazon_aurora_mysql_iam_least_privilege_policies"></a>

Sample IAM policies for least privilege access to Amazon Aurora MySQL

### Policy Selection Guide
<a name="amazon_aurora_mysql_policy_selection_guide"></a>

Choose the appropriate policy based on your role:


| Policy | Use Case | MFA Required | 
| --- | --- | --- | 
| Read Only | Auditors, compliance reviewers, monitoring dashboards | No | 
| Operator | Day-to-day operators managing resources | Yes | 
| Administrator | Service administrators with full management access | Yes (1-hour max) | 

### Read Only Policy
<a name="amazon_aurora_mysql_read_only_policy"></a>

 **Use this for:** Auditors, compliance reviewers, monitoring dashboards

 **Grants access to:** 
+ View resource configurations
+ List resources
+ Describe resource details

 **Does NOT grant:** 
+ Create or modify resources
+ Delete resources
+ Change configurations

 **Testing this policy:** 

```
# Verify read access works
aws rds describe-db-instances
aws rds describe-db-clusters

# Verify write access is denied (should fail)
aws rds modify-db-instance --db-instance-identifier test-db
```

 **Policy JSON:** 

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

### Operator Policy
<a name="amazon_aurora_mysql_operator_policy"></a>

 **Use this for:** Day-to-day operators managing resources

 **Grants access to:** 
+ All read-only permissions
+ Create and modify resources
+ Perform operational tasks

 **Does NOT grant:** 
+ Delete critical resources
+ Change security configurations
+ Manage access policies

 **Testing this policy:** 

```
# Verify operator access works (requires MFA)
aws rds modify-db-cluster --db-cluster-identifier <cluster-id> --apply-immediately

# Verify admin access is denied (should fail)
aws rds delete-db-cluster --db-cluster-identifier <cluster-id>
```

 **Policy JSON:** 

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

### Administrator Policy
<a name="amazon_aurora_mysql_administrator_policy"></a>

 **Use this for:** Service administrators with full management access

 **Grants access to:** 
+ All operator permissions
+ Delete resources
+ Manage access policies
+ Configure security settings

 **Requires:** 
+ MFA with maximum 1-hour session duration

 **Testing this policy:** 

```
# Verify full admin access works (requires MFA)
aws rds create-db-cluster --db-cluster-identifier new-cluster --engine aurora-mysql
aws rds delete-db-cluster --db-cluster-identifier old-cluster --skip-final-snapshot
```

 **Policy JSON:** 

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
<a name="amazon_aurora_mysql_database_encryption"></a>

Amazon Aurora MySQL requires encryption at rest using AWS KMS customer-managed keys and SSL/TLS encryption in transit for secure database operations.

 **Implementation Overview:** Aurora MySQL security involves encrypting data at rest and in transit, securing the master user account, implementing network access controls, and enabling comprehensive audit logging.

#### Implementation Examples
<a name="amazon_aurora_mysql_implementation_examples"></a>

The below are several items you should consider implementing.

1.  **Create KMS Key for Aurora Encryption** 

   Create dedicated KMS key for encrypting Aurora MySQL cluster

   ```
   # Create KMS key for Aurora encryption
   aws kms create-key --description 'Aurora MySQL Encryption Key' --key-usage ENCRYPT_DECRYPT
   # Create alias for the key
   aws kms create-alias --alias-name alias/aurora-mysql-key --target-key-id arn:aws:kms:region:account:key/key-id
   ```

1.  **Create Encrypted Aurora MySQL Cluster** 

   Create Aurora cluster with encryption enabled and secure master user configuration

   ```
   # Create encrypted Aurora MySQL cluster
   aws rds create-db-cluster \
     --db-cluster-identifier my-aurora-cluster \
     --engine aurora-mysql \
     --master-username admin \
     --manage-master-user-password \
     --master-user-secret-kms-key-id alias/aurora-mysql-key \
     --storage-encrypted \
     --kms-key-id alias/aurora-mysql-key \
     --vpc-security-group-ids sg-xxxxxxxxx \
     --db-subnet-group-name private-subnet-group
   ```

1.  **Configure SSL/TLS and Audit Logging** 

   Enable SSL enforcement and comprehensive audit logging

   ```
   # Create parameter group with SSL enforcement
   aws rds create-db-cluster-parameter-group \
     --db-cluster-parameter-group-name aurora-mysql-secure \
     --db-parameter-group-family aurora-mysql8.0 \
     --description 'Secure Aurora MySQL parameters'
   
   # Enable SSL enforcement and audit logging
   aws rds modify-db-cluster-parameter-group \
     --db-cluster-parameter-group-name aurora-mysql-secure \
     --parameters ParameterName=require_secure_transport,ParameterValue=ON \
     --parameters ParameterName=server_audit_logging,ParameterValue=1 \
     --parameters ParameterName=server_audit_events,ParameterValue=CONNECT,QUERY,TABLE
   ```

 **API:** `aws rds create-db-cluster --storage-encrypted --kms-key-id alias/aurora-mysql-key` 

 **Control:** SC-28

### Privileged Access Control
<a name="amazon_aurora_mysql_privileged_access_control"></a>

Amazon Aurora MySQL requires implementation of privileged account security controls including least privilege access, multi-factor authentication for administrative operations, and comprehensive audit logging of privileged activities.

 **Implementation Overview:** Amazon Aurora MySQL privileged account security involves implementing strict access controls, monitoring privileged operations, and ensuring administrative activities are properly authenticated and logged.

#### Implementation Examples
<a name="amazon_aurora_mysql_implementation_examples_2"></a>

1.  **Implement Least Privilege Access** 

   Configure Amazon Aurora MySQL with minimal required permissions for administrative accounts

   ```
   # Create least privilege IAM policy for Amazon Aurora MySQL administration
   aws iam create-policy --policy-name ServiceAdminPolicy --policy-document file://admin-policy.json
   # Attach policy to administrative role
   aws iam attach-role-policy --role-name ServiceAdminRole --policy-arn arn:aws:iam::account:policy/ServiceAdminPolicy
   ```

1.  **Enable Multi-Factor Authentication** 

   Require MFA for all privileged operations and administrative access

   ```
   # Create MFA-required policy condition
   # Add MFA condition to administrative policies
   # Verify MFA enforcement for privileged operations
   ```

1.  **Configure Privileged Activity Monitoring** 

   Enable comprehensive logging and monitoring of all privileged account activities

   ```
   # Enable CloudTrail for API logging
   aws cloudtrail create-trail --name ServicePrivilegedAccess --s3-bucket-name audit-logs
   # Configure CloudWatch alarms for privileged operations
   aws logs create-log-group --log-group-name /aws/service/privileged-access
   ```

 **API:** `Configure via IAM policies and amazon-aurora-mysql administrative APIs` 

 **Control:** AC-6

## SCG-CSO-SDF: Secure Defaults
<a name="amazon_aurora_mysql_scg_cso_sdf_secure_defaults"></a>

 **Applicable:** Yes

AWS services are designed with security in mind, providing multiple layers of security controls and encryption capabilities. However, AWS allows customers to define the security configuration of services and does not enforce a minimum security standard by default, enabling customers the flexibility to meet their specific business requirements and compliance needs.

### Implementation
<a name="amazon_aurora_mysql_implementation"></a>

Ensure Aurora MySQL clusters are created with security-first configurations including encryption, access controls, and monitoring

 **Best Practices:** 
+ Enable encryption at rest using customer-managed KMS keys
+ Use AWS Secrets Manager for master user password management
+ Enforce SSL/TLS connections for all database access
+ Enable comprehensive audit logging and monitoring
+ Deploy in private subnets with restrictive security groups
+ Implement automated backup encryption
+ Configure parameter groups with security-hardened settings

## SCG-ENH-CMP: Configuration Comparison
<a name="amazon_aurora_mysql_scg_enh_cmp_configuration_comparison"></a>

 **Applicable:** Yes

Use AWS Config rules and custom scripts to compare current Aurora MySQL configuration against security baselines.

## SCG-ENH-EXP: Configuration Export
<a name="amazon_aurora_mysql_scg_enh_exp_configuration_export"></a>

 **Applicable:** Yes

Export Aurora MySQL configuration using AWS CLI describe commands in JSON format.

## SCG-ENH-API: API Configuration
<a name="amazon_aurora_mysql_scg_enh_api_api_configuration"></a>

 **Applicable:** Yes

### Cluster Management
<a name="amazon_aurora_mysql_cluster_management"></a>

 **API Command:** 

```
Configure via AWS RDS APIs for Aurora MySQL cluster management
```

 **Control:** AC-6

 **Implementation Guidance:** 
+ Create separate roles for different access levels (read-only, operator, administrator)
+ Always require MFA for privileged operations
+ Use time-based conditions to limit session duration
+ Implement resource-based restrictions where possible
+ Regular review and rotation of access permissions

## Additional Resources
<a name="amazon_aurora_mysql_additional_resources"></a>

For more information about AWS security best practices, see the following resources:
+  [AWS Security Documentation](https://docs.aws.amazon.com/security/) 
+  [AWS FedRAMP Compliance](https://aws.amazon.com/compliance/fedramp/) 
+  [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) 