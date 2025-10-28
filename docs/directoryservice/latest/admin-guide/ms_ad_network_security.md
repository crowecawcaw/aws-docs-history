# Enhancing your AWS Managed Microsoft AD network security

configuration

The AWS Security Group that is provisioned for the AWS Managed Microsoft AD directory is configured
with the minimum inbound network ports required to support all known use cases for your
AWS Managed Microsoft AD directory. For more information on the provisioned AWS Security Group, see [What gets created with your
AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md").

To further enhance the network security of your AWS Managed Microsoft AD directory, you can modify the
AWS Security Group based on the following common scenarios.

**Customer domain controllers CIDR** - This CIDR block is where your domain
on-premises domain controllers reside.

**Customer client CIDR** - This CIDR block is where your clients such as
computers or users authenticate to your AWS Managed Microsoft AD. Your AWS Managed Microsoft AD domain controllers also
reside in this CIDR block.

###### Scenarios

- [AWS applications only support](#aws_apps_support "#aws_apps_support")
- [AWS applications only with trust support](#aws_apps_trust_support "#aws_apps_trust_support")
- [AWS applications and native Active Directory
  workload support](#aws_apps_native_ad_support "#aws_apps_native_ad_support")
- [AWS applications and native Active
  Directory workload support with trust support](#aws_apps_native_ad_trust_support "#aws_apps_native_ad_trust_support")

## AWS applications only support

All user accounts are provisioned only in your AWS Managed Microsoft AD to be used with supported
AWS applications, such as the following:

- Amazon Chime
- Amazon Connect
- Quick Suite
- AWS IAM Identity Center
- WorkDocs
- Amazon WorkMail
- AWS Client VPN
- AWS Management Console

You can use the following AWS Security Group configuration to block all non-essential
traffic to your AWS Managed Microsoft AD domain controllers.

###### Note

- The following are not compatible with this AWS Security Group
  configuration:
  - Amazon EC2 instances
  - Amazon FSx
  - Amazon RDS for MySQL
  - Amazon RDS for Oracle
  - Amazon RDS for PostgreSQL
  - Amazon RDS for SQL Server
  - WorkSpaces
  - Active Directory trusts
  - Domain joined clients or servers

**Inbound Rules**

None.

**Outbound Rules**

None.

## AWS applications only with trust support

All user accounts are provisioned in your AWS Managed Microsoft AD or trusted Active Directory to be
used with supported AWS applications, such as the following:

- Amazon Chime
- Amazon Connect
- Quick Suite
- AWS IAM Identity Center
- WorkDocs
- Amazon WorkMail
- Amazon WorkSpaces
- AWS Client VPN
- AWS Management Console

You can modify the provisioned AWS Security Group configuration to block all
non-essential traffic to your AWS Managed Microsoft AD domain controllers.

###### Note

- The following are not compatible with this AWS Security Group
  configuration:
  - Amazon EC2 instances
  - Amazon FSx
  - Amazon RDS for MySQL
  - Amazon RDS for Oracle
  - Amazon RDS for PostgreSQL
  - Amazon RDS for SQL Server
  - WorkSpaces
  - Active Directory trusts
  - Domain joined clients or servers

- This configuration requires you to ensure the "customer domain controllers CIDR"
  network is secure.
- TCP 445 is used for trust creation only and can be removed after the trust has been
  established.
- TCP 636 is only required when LDAP over SSL is in use.

**Inbound Rules**

| Protocol  | Port range    | Source                           | Type of traffic                | Active Directory usage                                                        |
| --------- | ------------- | -------------------------------- | ------------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TCP & UDP | 53            | Customer domain controllers CIDR | DNS                            | User and computer authentication, name resolution, trusts                     |
| TCP & UDP | 88            | Customer domain controllers CIDR | Kerberos                       | User and computer authentication, forest level trusts                         |
| TCP & UDP | 389           | Customer domain controllers CIDR | LDAP                           | Directory, replication, user and computer authentication group policy, trusts |
| TCP & UDP | 464           | Customer domain controllers CIDR | Kerberos change / set password | Replication, user and computer authentication, trusts                         |
| TCP       | 445           | Customer domain controllers CIDR | SMB / CIFS                     | Replication, user and computer authentication, group policy trusts            |
| TCP       | 135           | Customer domain controllers CIDR | Replication                    | RPC, EPM                                                                      |
| TCP       | 636           | Customer domain controllers CIDR | LDAP SSL                       | Directory, replication, user and computer authentication group policy, trusts |
| TCP       | 49152 - 65535 | Customer domain controllers CIDR | RPC                            | Replication, user and computer authentication, group policy, trusts           |
| TCP       | 3268 - 3269   | Customer domain controllers CIDR | LDAP GC & LDAP GC SSL          | Directory, replication, user and computer authentication group policy, trusts |
| UDP       | 123           | Customer domain controllers CIDR | Windows Time                   | Windows Time, trusts                                                          | **Outbound Rules**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Protocol  | Port range    | Source                           | Type of traffic                | Active Directory usage                                                        |
| ---       | ---           | ---                              | ---                            | ---                                                                           |
| All       | All           | Customer domain controllers CIDR | All traffic                    |                                                                               | ## AWS applications and native Active Directory workload support User accounts are provisioned only in your AWS Managed Microsoft AD to be used with supported AWS applications, such as the following: <br>• Amazon Chime <br>• Amazon Connect <br>• Amazon EC2 instances <br>• Amazon FSx <br>• Quick Suite <br>• Amazon RDS for MySQL <br>• Amazon RDS for Oracle <br>• Amazon RDS for PostgreSQL <br>• Amazon RDS for SQL Server <br>• AWS IAM Identity Center <br>• WorkDocs <br>• Amazon WorkMail <br>• WorkSpaces <br>• AWS Client VPN <br>• AWS Management Console You can modify the provisioned AWS Security Group configuration to block all non-essential traffic to your AWS Managed Microsoft AD domain controllers. ###### Note <br>• Active Directory trusts cannot be created and maintained between your AWS Managed Microsoft AD directory and customer domain controllers CIDR. <br>• It requires you to ensure the "customer client CIDR" network is secure. <br>• TCP 636 is only required when LDAP over SSL is in use. <br>• If you want to use an Enterprise CA with this configuration you will need to create an outbound rule "TCP, 443, CA CIDR". **Inbound Rules**                                                                                                                                                                                                                                |
| Protocol  | Port range    | Source                           | Type of traffic                | Active Directory usage                                                        |
| ---       | ---           | ---                              | ---                            | ---                                                                           |
| TCP & UDP | 53            | Customer client CIDR             | DNS                            | User and computer authentication, name resolution, trusts                     |
| TCP & UDP | 88            | Customer client CIDR             | Kerberos                       | User and computer authentication, forest level trusts                         |
| TCP & UDP | 389           | Customer client CIDR             | LDAP                           | Directory, replication, user and computer authentication group policy, trusts |
| TCP & UDP | 445           | Customer client CIDR             | SMB / CIFS                     | Replication, user and computer authentication, group policy trusts            |
| TCP & UDP | 464           | Customer client CIDR             | Kerberos change / set password | Replication, user and computer authentication, trusts                         |
| TCP       | 135           | Customer client CIDR             | Replication                    | RPC, EPM                                                                      |
| TCP       | 636           | Customer client CIDR             | LDAP SSL                       | Directory, replication, user and computer authentication group policy, trusts |
| TCP       | 49152 - 65535 | Customer client CIDR             | RPC                            | Replication, user and computer authentication, group policy, trusts           |
| TCP       | 3268 - 3269   | Customer client CIDR             | LDAP GC & LDAP GC SSL          | Directory, replication, user and computer authentication group policy, trusts |
| TCP       | 9389          | Customer client CIDR             | SOAP                           | AD DS web services                                                            |
| UDP       | 123           | Customer client CIDR             | Windows Time                   | Windows Time, trusts                                                          |
| UDP       | 138           | Customer client CIDR             | DFSN & NetLogon                | DFS, group policy                                                             | **Outbound Rules** None. ## AWS applications and native Active Directory workload support with trust support All user accounts are provisioned in your AWS Managed Microsoft AD or trusted Active Directory to be used with supported AWS applications, such as the following: <br>• Amazon Chime <br>• Amazon Connect <br>• Amazon EC2 instances <br>• Amazon FSx <br>• Quick Suite <br>• Amazon RDS for MySQL <br>• Amazon RDS for Oracle <br>• Amazon RDS for PostgreSQL <br>• Amazon RDS for SQL Server <br>• AWS IAM Identity Center <br>• WorkDocs <br>• Amazon WorkMail <br>• WorkSpaces <br>• AWS Client VPN <br>• AWS Management Console You can modify the provisioned AWS Security Group configuration to block all non-essential traffic to your AWS Managed Microsoft AD domain controllers. ###### Note <br>• It requires you to ensure the "customer domain controllers CIDR" and "customer client CIDR" networks are secure. <br>• TCP 445 with the "customer domain controllers CIDR" is used for trust creation only and can be removed after the trust has been established. <br>• TCP 445 with the "customer client CIDR" should be left open as it is required for Group Policy processing. <br>• TCP 636 is only required when LDAP over SSL is in use. <br>• If you want to use an Enterprise CA with this configuration you will need to create an outbound rule "TCP, 443, CA CIDR". **Inbound Rules** |
| Protocol  | Port range    | Source                           | Type of traffic                | Active Directory usage                                                        |
| ---       | ---           | ---                              | ---                            | ---                                                                           |
| TCP & UDP | 53            | Customer domain controllers CIDR | DNS                            | User and computer authentication, name resolution, trusts                     |
| TCP & UDP | 88            | Customer domain controllers CIDR | Kerberos                       | User and computer authentication, forest level trusts                         |
| TCP & UDP | 389           | Customer domain controllers CIDR | LDAP                           | Directory, replication, user and computer authentication group policy, trusts |
| TCP & UDP | 464           | Customer domain controllers CIDR | Kerberos change / set password | Replication, user and computer authentication, trusts                         |
| TCP       | 445           | Customer domain controllers CIDR | SMB / CIFS                     | Replication, user and computer authentication, group policy trusts            |
| TCP       | 135           | Customer domain controllers CIDR | Replication                    | RPC, EPM                                                                      |
| TCP       | 636           | Customer domain controllers CIDR | LDAP SSL                       | Directory, replication, user and computer authentication group policy, trusts |
| TCP       | 49152 - 65535 | Customer domain controllers CIDR | RPC                            | Replication, user and computer authentication, group policy, trusts           |
| TCP       | 3268 - 3269   | Customer domain controllers CIDR | LDAP GC & LDAP GC SSL          | Directory, replication, user and computer authentication group policy, trusts |
| UDP       | 123           | Customer domain controllers CIDR | Windows Time                   | Windows Time, trusts                                                          |
| TCP & UDP | 53            | Customer domain controllers CIDR | DNS                            | User and computer authentication, name resolution, trusts                     |
| TCP & UDP | 88            | Customer domain controllers CIDR | Kerberos                       | User and computer authentication, forest level trusts                         |
| TCP & UDP | 389           | Customer domain controllers CIDR | LDAP                           | Directory, replication, user and computer authentication group policy, trusts |
| TCP & UDP | 445           | Customer domain controllers CIDR | SMB / CIFS                     | Replication, user and computer authentication, group policy trusts            |
| TCP & UDP | 464           | Customer domain controllers CIDR | Kerberos change / set password | Replication, user and computer authentication, trusts                         |
| TCP       | 135           | Customer domain controllers CIDR | Replication                    | RPC, EPM                                                                      |
| TCP       | 636           | Customer domain controllers CIDR | LDAP SSL                       | Directory, replication, user and computer authentication group policy, trusts |
| TCP       | 49152 - 65535 | Customer domain controllers CIDR | RPC                            | Replication, user and computer authentication, group policy, trusts           |
| TCP       | 3268 - 3269   | Customer domain controllers CIDR | LDAP GC & LDAP GC SSL          | Directory, replication, user and computer authentication group policy, trusts |
| TCP       | 9389          | Customer domain controllers CIDR | SOAP                           | AD DS web services                                                            |
| UDP       | 123           | Customer domain controllers CIDR | Windows Time                   | Windows Time, trusts                                                          |
| UDP       | 138           | Customer domain controllers CIDR | DFSN & NetLogon                | DFS, group policy                                                             | **Outbound Rules**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Protocol  | Port range    | Source                           | Type of traffic                | Active Directory usage                                                        |
| ---       | ---           | ---                              | ---                            | ---                                                                           |
| All       | All           | Customer domain controllers CIDR | All traffic                    |                                                                               |
