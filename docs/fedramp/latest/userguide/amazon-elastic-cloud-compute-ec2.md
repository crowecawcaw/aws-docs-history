

# Amazon Elastic Compute Cloud (EC2)
<a name="amazon-elastic-cloud-compute-ec2"></a>

This guide provides security configuration requirements and implementation examples for Amazon Elastic Compute Cloud (EC2) in accordance with FedRAMP requirements.

## Document Information
<a name="amazon_elastic_compute_cloud_ec2_document_information"></a>


|  |  | 
| --- |--- |
| Version | 1.0.2 | 
| Last Updated | 2026-03-26 | 
| Documentation URL | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2\_GetStarted.html | 

## Overview
<a name="amazon_elastic_compute_cloud_ec2_overview"></a>

Amazon Elastic Cloud Compute (EC2) security configuration involves implementing comprehensive security controls including encryption, access management, logging, and monitoring to meet FedRAMP compliance requirements.

 **Important Disclaimer**: This document provides AWS recommended practices and guidance only. It does not constitute legal, compliance, or regulatory advice. Organizations are solely responsible for determining their compliance requirements and implementing appropriate controls. AWS makes no warranties or representations regarding FedRAMP compliance or the adequacy of these recommendations for any specific use case. AWS services and features evolve rapidly. Customers should verify current service capabilities and limitations through official AWS documentation before implementation.

 **Command and Configuration Disclaimer**: All AWS CLI commands, API calls, and configuration examples provided in this document are for illustrative purposes only. Organizations must validate all commands and configurations in non-production environments before implementation. AWS CLI commands may require specific IAM permissions, resource names, and parameter values that must be customized for each environment. Always refer to the latest AWS CLI documentation and service-specific guides for current syntax and available options.

## FedRAMP Requirements
<a name="amazon_elastic_compute_cloud_ec2_fedramp_requirements"></a>

Amazon Elastic Compute Cloud (EC2) must comply with the following FedRAMP requirements:
+ SCG-CSO-RSC
+ SCG-CSO-SDF
+ SCG-ENH-CMP
+ SCG-ENH-EXP
+ SCG-ENH-API

## Administrative Account Model
<a name="amazon_elastic_compute_cloud_ec2_administrative_account_model"></a>

Amazon Elastic Compute Cloud (EC2) does not have an administrative account model.


|  |  | 
| --- |--- |
| Administrative Accounts | No | 
| Account Type | N/A | 

## SCG-CSO-RSC: Recommended Secure Configuration
<a name="amazon_elastic_compute_cloud_ec2_scg_cso_rsc_recommended_secure_configuration"></a>

 **Applicable:** Yes

This requirement consolidates guidance for: 1. Instructions on how to securely access, configure, operate, and decommission top-level administrative accounts 2. Explanations of security-related settings that can be operated only by top-level administrative accounts 3. Explanations of security-related settings that can be operated only by privileged accounts

### Part 1: Administrative Accounts
<a name="amazon_elastic_compute_cloud_ec2_part_1_administrative_accounts"></a>

 **Applicable:** No

Not applicable - no administrative account model

### Part 2: Administrative Settings
<a name="amazon_elastic_compute_cloud_ec2_part_2_administrative_settings"></a>

 **Applicable:** Yes (OS-Level Administrative Accounts)

### Operating System Administrative Account Security
<a name="amazon_elastic_compute_cloud_ec2_operating_system_administrative_account_security"></a>

Amazon EC2 instances run customer-managed operating systems. Unlike database services, EC2 does not have a service-level "master user." Instead, security focuses on OS-level administrative accounts that vary by operating system. This section provides guidance for securing administrative access across different operating systems.

#### Linux-Based Operating Systems (Amazon Linux, Ubuntu, RHEL, etc.)
<a name="amazon_elastic_compute_cloud_ec2_linux_based_operating_systems_amazon_linux_ubuntu_rhel_etc"></a>

##### 1. Root Account Security
<a name="amazon_elastic_compute_cloud_ec2_1_root_account_security"></a>

 **Operations Restricted to root:** 
+ System-wide configuration changes
+ Installation and removal of system packages
+ Modification of system services and daemons
+ Network configuration changes
+ Firewall and iptables management
+ User and group management
+ File system mounting and unmounting
+ Kernel module loading
+ System logging configuration

 **Security Implications:** 
+ Root access provides complete system control
+ Compromised root account enables full system takeover
+ Root operations bypass most security controls
+ Improper root usage violates least privilege
+ Root access required for security patching

 **Best Practices:** 
+ Disable direct root SSH login (`PermitRootLogin no` in sshd\_config)
+ Use sudo for privileged operations instead of su
+ Require individual user accounts with sudo access
+ Enable sudo logging and auditing
+ Use SSH key-based authentication only (disable password auth)
+ Implement multi-factor authentication for sudo operations
+ Regularly audit sudo access and usage

##### 2. Sudo-Enabled User Accounts
<a name="amazon_elastic_compute_cloud_ec2_2_sudo_enabled_user_accounts"></a>

 **Operations:** 
+ Execute commands with root privileges via sudo
+ Modify system configuration files
+ Install/update software packages
+ Manage system services
+ Access restricted log files
+ Modify security settings

 **Security Implications:** 
+ Sudo provides temporary privilege escalation
+ Sudo logs provide audit trail of privileged operations
+ Misconfigured sudoers file can grant excessive privileges
+ Sudo without password (NOPASSWD) increases risk

 **Best Practices:** 
+ Configure sudoers file with least privilege
+ Require password for sudo operations (avoid NOPASSWD)
+ Use sudo groups instead of individual user entries
+ Enable sudo logging to syslog
+ Implement command restrictions in sudoers
+ Regular review of sudoers configuration
+ Use `visudo` to prevent syntax errors

##### 3. SSH Key Management
<a name="amazon_elastic_compute_cloud_ec2_3_ssh_key_management"></a>

 **Operations:** 
+ Generate and distribute SSH key pairs
+ Manage authorized\_keys files
+ Configure SSH daemon settings
+ Implement SSH certificate authorities

 **Security Implications:** 
+ SSH keys provide passwordless authentication
+ Compromised private keys enable unauthorized access
+ Shared keys violate accountability principles
+ Unmanaged keys create security gaps

 **Best Practices:** 
+ Use EC2 key pairs or AWS Systems Manager Session Manager
+ Generate unique SSH keys per user
+ Implement SSH key rotation (90 days maximum)
+ Use SSH certificates instead of static keys where possible
+ Disable password authentication in sshd\_config
+ Implement SSH bastion hosts for access control
+ Use AWS Systems Manager Session Manager for auditable access

##### 4. System Service Management
<a name="amazon_elastic_compute_cloud_ec2_4_system_service_management"></a>

 **Operations:** 
+ Start, stop, restart system services
+ Enable/disable services at boot
+ Modify service configurations
+ View service status and logs

 **Security Implications:** 
+ Service management affects system availability
+ Malicious services can compromise system
+ Service misconfigurations create vulnerabilities
+ Service accounts may have elevated privileges

 **Best Practices:** 
+ Use systemd or init.d for service management
+ Implement service-specific user accounts (not root)
+ Enable SELinux or AppArmor for service confinement
+ Regular audit of running services
+ Disable unnecessary services
+ Monitor service logs for anomalies

#### Windows-Based Operating Systems
<a name="amazon_elastic_compute_cloud_ec2_windows_based_operating_systems"></a>

##### 1. Administrator Account Security
<a name="amazon_elastic_compute_cloud_ec2_1_administrator_account_security"></a>

 **Operations Restricted to Administrator:** 
+ System-wide configuration changes
+ Software installation and removal
+ User and group management
+ Security policy configuration
+ Service management
+ Registry modifications
+ Firewall configuration
+ Event log management

 **Security Implications:** 
+ Administrator access provides complete system control
+ Compromised Administrator account enables full takeover
+ Administrator operations bypass User Account Control (UAC)
+ Improper Administrator usage violates least privilege

 **Best Practices:** 
+ Rename default Administrator account
+ Disable built-in Administrator account when not needed
+ Use separate administrative accounts (not daily-use accounts)
+ Enable and configure User Account Control (UAC)
+ Implement Local Administrator Password Solution (LAPS)
+ Use RDP with Network Level Authentication (NLA)
+ Require strong passwords (minimum 20 characters)
+ Enable account lockout policies

##### 2. Domain Administrator Accounts (Active Directory)
<a name="amazon_elastic_compute_cloud_ec2_2_domain_administrator_accounts_active_directory"></a>

 **Operations:** 
+ Domain-wide user and computer management
+ Group Policy creation and modification
+ Domain controller management
+ Trust relationship configuration
+ Schema modifications
+ Forest and domain functional level changes

 **Security Implications:** 
+ Domain Admin access affects entire AD environment
+ Compromised Domain Admin enables enterprise-wide attack
+ Domain Admin credentials are high-value targets
+ Improper Group Policy can weaken security

 **Best Practices:** 
+ Minimize Domain Admin account usage
+ Use separate accounts for domain administration
+ Implement Privileged Access Workstations (PAWs)
+ Enable Protected Users security group
+ Implement tiered administrative model
+ Use Just-In-Time (JIT) admin access
+ Monitor Domain Admin activity with SIEM
+ Regular audit of Domain Admin group membership

##### 3. Local Security Policy Management
<a name="amazon_elastic_compute_cloud_ec2_3_local_security_policy_management"></a>

 **Operations:** 
+ Password policy configuration
+ Account lockout policy settings
+ User rights assignment
+ Security options configuration
+ Audit policy settings

 **Security Implications:** 
+ Security policies enforce baseline security
+ Weak policies create vulnerabilities
+ Policy misconfigurations can lock out users
+ Audit policies affect compliance

 **Best Practices:** 
+ Implement CIS Benchmarks for Windows
+ Use Group Policy for centralized management
+ Enable comprehensive audit logging
+ Configure password complexity requirements
+ Implement account lockout policies
+ Regular review of security policy settings
+ Test policy changes in non-production first

##### 4. Remote Desktop Protocol (RDP) Security
<a name="amazon_elastic_compute_cloud_ec2_4_remote_desktop_protocol_rdp_security"></a>

 **Operations:** 
+ Enable/disable RDP access
+ Configure RDP security settings
+ Manage RDP user permissions
+ Configure Network Level Authentication

 **Security Implications:** 
+ RDP provides remote administrative access
+ Unsecured RDP is common attack vector
+ RDP credentials can be intercepted
+ RDP sessions may not be audited

 **Best Practices:** 
+ Use AWS Systems Manager Session Manager instead of RDP when possible
+ Enable Network Level Authentication (NLA)
+ Use RDP Gateway for centralized access
+ Implement multi-factor authentication for RDP
+ Restrict RDP access via security groups
+ Enable RDP session recording
+ Use strong encryption for RDP connections
+ Disable RDP when not needed

#### Cross-Platform Administrative Security Best Practices
<a name="amazon_elastic_compute_cloud_ec2_cross_platform_administrative_security_best_practices"></a>

##### 1. Access Management
<a name="amazon_elastic_compute_cloud_ec2_1_access_management"></a>
+ Use AWS Systems Manager Session Manager for secure, auditable access
+ Implement bastion hosts for SSH/RDP access
+ Use AWS IAM roles for EC2 instead of long-term credentials
+ Enable AWS CloudTrail for API logging
+ Implement just-in-time (JIT) administrative access
+ Use separate accounts for administrative tasks

##### 2. Credential Management
<a name="amazon_elastic_compute_cloud_ec2_2_credential_management"></a>
+ Store credentials in AWS Secrets Manager
+ Implement automatic credential rotation
+ Use SSH keys or certificates (not passwords)
+ Enable multi-factor authentication
+ Implement password complexity requirements
+ Regular credential audits and rotation

##### 3. Monitoring and Auditing
<a name="amazon_elastic_compute_cloud_ec2_3_monitoring_and_auditing"></a>
+ Enable CloudWatch Logs for system logs
+ Configure CloudWatch alarms for suspicious activity
+ Use AWS Config for configuration compliance
+ Implement centralized logging (SIEM)
+ Enable detailed audit logging
+ Regular review of administrative activity

##### 4. Patch Management
<a name="amazon_elastic_compute_cloud_ec2_4_patch_management"></a>
+ Use AWS Systems Manager Patch Manager
+ Implement automated patching schedules
+ Test patches in non-production first
+ Maintain patch compliance reporting
+ Enable automatic security updates where appropriate
+ Regular vulnerability scanning

##### 5. Network Security
<a name="amazon_elastic_compute_cloud_ec2_5_network_security"></a>
+ Deploy EC2 instances in private subnets
+ Use security groups with least privilege
+ Implement Network ACLs for additional protection
+ Use VPC endpoints for AWS service access
+ Enable VPC Flow Logs for network monitoring
+ Implement host-based firewalls (iptables, Windows Firewall)

##### 6. Compliance and Documentation
<a name="amazon_elastic_compute_cloud_ec2_6_compliance_and_documentation"></a>
+ Document all administrative accounts and their purposes
+ Maintain inventory of administrative access
+ Conduct quarterly access reviews
+ Implement change management for system changes
+ Use infrastructure as code (CloudFormation, Terraform)
+ Regular security assessments and penetration testing

#### AWS-Specific Administrative Tools
<a name="amazon_elastic_compute_cloud_ec2_aws_specific_administrative_tools"></a>

##### 1. AWS Systems Manager Session Manager
<a name="amazon_elastic_compute_cloud_ec2_1_aws_systems_manager_session_manager"></a>

 **Benefits:** 
+ No need for SSH keys or RDP passwords
+ Fully auditable sessions via CloudTrail
+ No need for bastion hosts or open inbound ports
+ Integrated with IAM for access control
+ Session recording and logging capabilities

 **Security Implications:** 
+ Requires IAM permissions for access
+ Sessions are encrypted in transit
+ Provides centralized access management
+ Eliminates need for direct SSH/RDP access

##### 2. AWS Systems Manager Run Command
<a name="amazon_elastic_compute_cloud_ec2_2_aws_systems_manager_run_command"></a>

 **Operations:** 
+ Execute commands across multiple instances
+ Automate administrative tasks
+ Apply patches and updates
+ Collect system information

 **Security Implications:** 
+ Requires IAM permissions
+ Commands are logged in CloudTrail
+ Can execute with elevated privileges
+ Requires careful access control

##### 3. EC2 Instance Connect
<a name="amazon_elastic_compute_cloud_ec2_3_ec2_instance_connect"></a>

 **Operations:** 
+ Temporary SSH access via AWS Console
+ One-time SSH public key push
+ No permanent key management

 **Security Implications:** 
+ Requires IAM permissions
+ Keys are temporary (60 seconds)
+ Access is logged in CloudTrail
+ Eliminates long-term key management

#### Implementation Checklist
<a name="amazon_elastic_compute_cloud_ec2_implementation_checklist"></a>

☐ Disable direct root/Administrator login ☐ Implement individual user accounts with sudo/admin rights ☐ Enable SSH key-based authentication (disable passwords) ☐ Configure multi-factor authentication ☐ Use AWS Systems Manager Session Manager ☐ Enable comprehensive audit logging ☐ Implement automated patch management ☐ Configure host-based firewalls ☐ Deploy instances in private subnets ☐ Regular access reviews and audits ☐ Document administrative procedures ☐ Implement change management processes

This comprehensive guidance ensures that EC2 instance administrative accounts are configured according to security best practices and FedRAMP requirements across different operating systems.

### Part 3: Privileged Settings
<a name="amazon_elastic_compute_cloud_ec2_part_3_privileged_settings"></a>

 **Applicable:** Yes

Within EC2 you have two layers of privileged access. One layer is at the IAM layer, where you can limit what permissions a user has to operate within EC2. This section covers the privileged settings for using the service itself and provides example IAM Policies that would allow for varying levels of access to the service. The second layer of privileged access is at the OS layer itself which is covered in the other sections of this document.

## IAM Least Privilege Policies
<a name="amazon_elastic_compute_cloud_ec2_iam_least_privilege_policies"></a>

Sample IAM policies for least privilege access to Amazon Elastic Compute Cloud (EC2)

### Policy Selection Guide
<a name="amazon_elastic_compute_cloud_ec2_policy_selection_guide"></a>

Choose the appropriate policy based on your role:


| Policy | Use Case | MFA Required | 
| --- | --- | --- | 
| Read Only | Auditors, compliance reviewers, monitoring dashboards | No | 
| Operator | Day-to-day operators managing resources | Yes | 
| Administrator | Service administrators with full management access | Yes (1-hour max) | 

### Read Only Policy
<a name="amazon_elastic_compute_cloud_ec2_read_only_policy"></a>

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
# Verify access works
aws elastic-cloud-compute-ec2 describe-* / list-*

# Verify restricted access is denied (should fail)
aws elastic-cloud-compute-ec2 create-* / delete-*
```

 **Policy JSON:** 

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "ec2:List*",
        "ec2:Get*"
      ],
      "Resource": "*"
    }
  ]
}
```

### Operator Policy
<a name="amazon_elastic_compute_cloud_ec2_operator_policy"></a>

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
# Verify access works
aws elastic-cloud-compute-ec2 create-* / update-*

# Verify restricted access is denied (should fail)
aws elastic-cloud-compute-ec2 delete-* / put-*-policy
```

 **Policy JSON:** 

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "ec2:List*",
        "ec2:Get*",
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:RebootInstances"
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
<a name="amazon_elastic_compute_cloud_ec2_administrator_policy"></a>

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
# Verify access works
aws elastic-cloud-compute-ec2 * (all operations)
```

 **Policy JSON:** 

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:*",
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

### Instance Metadata Service
<a name="amazon_elastic_compute_cloud_ec2_instance_metadata_service"></a>

Configure EC2 Instance Metadata Service v2 (IMDSv2) for enhanced security and disable IMDSv1.

 **Implementation Overview:** IMDSv2 provides session-oriented access to instance metadata with enhanced security features including token-based authentication and hop limit controls to prevent SSRF attacks.

#### Implementation Examples
<a name="amazon_elastic_compute_cloud_ec2_implementation_examples"></a>

1.  **Launch Instance with IMDSv2 Required** 

   Create EC2 instance with IMDSv2 enforcement

   ```
   aws ec2 run-instances --image-id AMI-12345678 --instance-type t3.micro --metadata-options HttpTokens=required,HttpPutResponseHopLimit=1,HttpEndpoint=enabled,InstanceMetadataTags=enabled
   ```

1.  **Modify Existing Instance Metadata Options** 

   Update existing instances to require IMDSv2

   ```
   aws ec2 modify-instance-metadata-options --instance-id <instance-id> --http-tokens required --http-put-response-hop-limit 1
   ```

 **Control:** SC-7

### Security Groups
<a name="amazon_elastic_compute_cloud_ec2_security_groups"></a>

Configure EC2 security groups with least privilege access rules and comprehensive traffic control.

 **Implementation Overview:** Security groups act as virtual firewalls controlling inbound and outbound traffic at the instance level. They should follow least privilege principles with specific port and protocol restrictions.

#### Implementation Examples
<a name="amazon_elastic_compute_cloud_ec2_implementation_examples_2"></a>

1.  **Create Restrictive Security Group** 

   Create security group with minimal required access

   ```
   aws ec2 create-security-group --group-name web-tier-sg --description 'Web tier security group' --vpc-id vpc-12345678
   aws ec2 authorize-security-group-ingress --group-id sg-abcdef12 --protocol tcp --port 443 --source-group sg-alb-sg
   aws ec2 authorize-security-group-ingress --group-id sg-abcdef12 --protocol tcp --port 22 --cidr 10.0.0.0/8
   ```

 **Control:** AC-4

### Privileged Access Control
<a name="amazon_elastic_compute_cloud_ec2_privileged_access_control"></a>

Amazon Elastic Compute Cloud (EC2) requires implementation of privileged account security controls including least privilege access, multi-factor authentication for administrative operations, and comprehensive audit logging of privileged activities.

 **Implementation Overview:** Amazon Elastic Compute Cloud (EC2) privileged account security involves implementing strict access controls, monitoring privileged operations, and ensuring administrative activities are properly authenticated and logged.

#### Implementation Examples
<a name="amazon_elastic_compute_cloud_ec2_implementation_examples_3"></a>

1.  **Implement Least Privilege Access** 

   Configure Amazon Elastic Compute Cloud (EC2) with minimal required permissions for administrative accounts

   ```
   # Create least privilege IAM policy for Amazon Elastic Compute Cloud (EC2) administration
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

 **API:** `Configure via IAM policies and amazon-elastic-compute-cloud-(ec2) administrative APIs` 

 **Control:** AC-6

## SCG-CSO-SDF: Secure Defaults
<a name="amazon_elastic_compute_cloud_ec2_scg_cso_sdf_secure_defaults"></a>

 **Applicable:** Yes

Amazon Elastic Compute Cloud (EC2) should be configured using AWS Security Best Practice recommendations. AWS allows customers to define the security of services, and does not enforce a minimum security standard by default. AWS services are designed with security in mind, but do not enforce a minimum security standard to allow customers freedom to meet their needed business requirements.

### Implementation
<a name="amazon_elastic_compute_cloud_ec2_implementation"></a>

Ensure Amazon Elastic Compute Cloud (EC2) resources are created with security-first configurations following AWS security design philosophy

 **Best Practices:** 
+ Enable encryption by default for EBS volumes using customer-managed KMS keys
+ Apply least privilege access policies through IAM roles and security groups
+ Enable comprehensive logging and monitoring with CloudTrail, VPC Flow Logs, and CloudWatch
+ Use secure network configurations with VPCs, private subnets, and NACLs
+ Implement Instance Metadata Service v2 (IMDSv2) to prevent SSRF attacks
+ Configure security groups with minimal required access and specific port restrictions
+ Use Systems Manager Session Manager for secure, auditable instance access
+ Enable detailed monitoring and automated patching through Systems Manager
+ Implement proper key pair management and rotate access credentials regularly
+ Use dedicated tenancy or Nitro-based instances for enhanced security isolation

## SCG-ENH-CMP: Configuration Comparison
<a name="amazon_elastic_compute_cloud_ec2_scg_enh_cmp_configuration_comparison"></a>

 **Applicable:** Yes

Use AWS Config rules or custom scripts to compare current Amazon Elastic Compute Cloud (EC2) configuration against baselines.

### AWS Config Implementation
<a name="amazon_elastic_compute_cloud_ec2_aws_config_implementation"></a>

Deploy AWS Config rules to continuously monitor Amazon Elastic Compute Cloud (EC2) compliance

 **Comparison Commands:** 

```
# List all EC2 instances
aws ec2 describe-instances --output json
# List all security groups
aws ec2 describe-security-groups --output json
# List all volumes
aws ec2 describe-volumes --output json
# List all snapshots owned by self
aws ec2 describe-snapshots --owner-ids self --output json
# List all VPCs
aws ec2 describe-vpcs --output json
# List all subnets
aws ec2 describe-subnets --output json
# Compare output against baseline configuration files
```

### Automation
<a name="amazon_elastic_compute_cloud_ec2_automation"></a>

Use AWS Config conformance packs or custom Lambda functions for automated comparison

## SCG-ENH-EXP: Configuration Export
<a name="amazon_elastic_compute_cloud_ec2_scg_enh_exp_configuration_export"></a>

 **Applicable:** Yes

Export Amazon Elastic Compute Cloud (EC2) configuration using AWS CLI describe/get commands in JSON format.

### Export Format
<a name="amazon_elastic_compute_cloud_ec2_export_format"></a>

JSON via AWS CLI

 **Export Commands:** 

```
# Export all EC2 instances
aws ec2 describe-instances --output json > amazon_ec2_instances.json
# Export all security groups
aws ec2 describe-security-groups --output json > amazon_ec2_security_groups.json
# Export all volumes
aws ec2 describe-volumes --output json > amazon_ec2_volumes.json
# Export all snapshots
aws ec2 describe-snapshots --owner-ids self --output json > amazon_ec2_snapshots.json
# Export all AMIs
aws ec2 describe-images --owners self --output json > amazon_ec2_amis.json
# Export all key pairs
aws ec2 describe-key-pairs --output json > amazon_ec2_key_pairs.json
# Export all VPCs
aws ec2 describe-vpcs --output json > amazon_ec2_vpcs.json
```

 **Use Cases:** 
+ Backup current configuration
+ Compare configurations across environments
+ Audit and compliance reporting
+ Infrastructure as Code generation

## SCG-ENH-API: API Configuration
<a name="amazon_elastic_compute_cloud_ec2_scg_enh_api_api_configuration"></a>

 **Applicable:** Yes

### Instance Management
<a name="amazon_elastic_compute_cloud_ec2_instance_management"></a>

 **API Command:** 

```
aws ec2 run-instances --image-id <AMI-id> --instance-type <type> --key-name <key-pair> --security-group-ids <sg-id> --encrypted
```

 **Control:** AC-6

 **Implementation Guidance:** 
+ Create separate roles for different access levels (read-only, operator, administrator)
+ Always require MFA for privileged operations
+ Use time-based conditions to limit session duration
+ Apply resource-specific restrictions where possible
+ Regularly review and audit policy assignments
+ Use AWS Access Analyzer to validate least privilege

 **Best Practices:** 
+ Start with read-only access and add permissions as needed
+ Use AWS managed policies as a baseline when available
+ Implement just-in-time access for administrative operations
+ Monitor policy usage with CloudTrail and Access Analyzer
+ Document business justification for each permission

## Additional Resources
<a name="amazon_elastic_compute_cloud_ec2_additional_resources"></a>

For more information about AWS security best practices, see the following resources:
+  [AWS Security Documentation](https://docs.aws.amazon.com/security/) 
+  [AWS FedRAMP Compliance](https://aws.amazon.com/compliance/fedramp/) 
+  [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) 