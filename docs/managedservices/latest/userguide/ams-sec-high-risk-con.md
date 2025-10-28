# Changes that introduce high or very high security risks in your environment

The following changes introduce high or very high security risk in your environment:

**AWS Identity and Access Management**

- High_Risk-IAM-001: Create access keys for root account
- High_Risk-IAM-002: SCP policy modification to allow additional access
- High_Risk-IAM-003: SCP policy modification that could break AMS infrastructure
- High_Risk-IAM-004: Creation of a role/user with infrastructure mutating permissions (write, permission management or tagging) in customer account
- High_Risk-IAM-005: IAM roles trust policies between AMS accounts and third-party accounts (not owned by the customer)
- High_Risk-IAM-006: Cross-account policies to access any KMS key from an AMS account by a third-party account)
- High_Risk-IAM-007: Cross-account policies from third-party accounts to access an AMS customer S3 bucket or resources where data can be stored (such as Amazon RDS, Amazon DynamoDB, or Amazon Redshift)
- High_Risk-IAM-008: Assign the IAM permissions with any infrastructure mutating permission in customer account
- High_Risk-IAM-009: Allow listing and reading on all the S3 buckets in the account
- High_Risk-IAM-010: Automated IAM Provisioning with read/write permissions
  **Network security**

- High_Risk-NET-001: Open OS management ports SSH/22 or SSH/2222 (Not SFTP/2222), TELNET/23, RDP/3389, WinRM/5985-5986, VNC/ 5900-5901 TS/CITRIX/1494 or 1604, LDAP/389 or 636 and NETBIOS/137-139 from the internet
- High_Risk-NET-002: Open database management ports MySQL/3306, PostgreSQL/5432, Oracle/1521, MSSQL/1433 or any management customer port from the internet
- High_Risk-NET-003: Open application ports HTTP/80, HTTPS/8443 and HTTPS/443 on any compute resources directly. For example, EC2 instances, ECS/EKS/Fargate containers, and so on from the internet
- High_Risk-NET-004: Any changes to the security groups which controls the access to the AMS infrastructure
- High_Risk-NET-006: VPC peering with the third-party account (not owned by the customer)
- High_Risk-NET-007: Adding customer firewall as egress point for all the AMS traffic
- High_Risk-NET-008: Transit Gateway attachment with the third-party account is not allowed
- High_Risk-S3-001: Provision or enable public access in the S3 bucket
  **Logging**

- High_Risk-LOG-001: Disable CloudTrail. (Ops Site Manager Approval Required)
- High_Risk-LOG-002: Disable VPC Flow Logs. (Ops Site Manager Approval Required)
- High_Risk-LOG-003: Log forwarding through any method (S3 event notification, SIEM agent pull, SIEM agent push etc) from an AMS managed account to third party account (not owned by customer)
- High_Risk-LOG-004: Use non-AMS trail for CloudTrail
  **Host Security**

- High_Risk-HOST-001: Disable End Point Security in the account for any reason.(Ops Site Manager Approval Required)
- High_Risk-HOST-002: Disable patching in a resource or at account level.
- High_Risk-HOST-003: Deploying an unmanaged EC2 instance in the account.
- High_Risk-HOST-004: Running a custom script provided by the customer.
- High_Risk-HOST-005: Creation of Local Administrator accounts on instances.
- High_Risk-HOST-006: Trend Micro EPS file type / extension scan exclusions or disabling malware protection on endpoints.

###### Note

Risk acceptance isn't required for EPS anti-malware exclusions or GuardDuty Suppression rules related to penetration tests or vulnerability scans or service impacting events/known performance issues warranting proactive actions. A risk notification is enough in these situations.

- High_Risk-HOST-007: Create KeyPair for EC2
- High_Risk-HOST-008: Disable End Point Security in the EC2
- High_Risk-HOST-009: Accounts using End of Life(EOL) OS
  **Miscellaneous**

- High_Risk-ENC-001: Disable encryption in any resource if it is enabled
  **Managed Active Directory**

- High_Risk-AD-001: Provide admin rights to active director user or group
- High_Risk-AD-002: GPO Policies capable of reducing security posture of the account
