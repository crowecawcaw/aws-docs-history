# Simple AD

Simple AD is a standalone managed directory that is powered by a Samba 4 Active Directory
Compatible Server. It is available in two sizes.

- Small - Supports up to 500 users (approximately 2,000 objects including users, groups,
  and computers).
- Large - Supports up to 5,000 users (approximately 20,000 objects including users,
  groups, and computers).
  Simple AD provides a subset of the features offered by AWS Managed Microsoft AD, including the ability
  to manage user accounts and group memberships, create and apply group policies, securely connect
  to Amazon EC2 instances, and provide Kerberos-based single sign-on (SSO). However, note that
  Simple AD does not support features such as multi-factor authentication (MFA), trust
  relationships with other domains, Active Directory Administrative Center, PowerShell support,
  Active Directory recycle bin, group managed service accounts, and schema extensions for POSIX
  and Microsoft applications.

Simple AD offers many advantages:

- Simple AD makes it easier to [manage amazon EC2 instances running Linux and Windows](simple_ad_join_instance.md "simple_ad_join_instance.md") and deploy Windows
  applications in the AWS Cloud.
- Many of the applications and tools that you use today that require Microsoft Active
  Directory support can be used with Simple AD.
- User accounts in Simple AD allow access to AWS applications such as WorkSpaces, WorkDocs, or
  Amazon WorkMail.
- You can manage AWS resources through IAM role–based access to the
  AWS Management Console.
- Daily automated snapshots enable point-in-time recovery.
  Simple AD does not support any of the following:

- Amazon AppStream 2.0
- Amazon Chime
- Amazon FSx
- Amazon RDS for SQL Server
- Amazon RDS for Oracle
- AWS IAM Identity Center
- Trust relationships with other domains
- Active Directory Administrative Center
- PowerShell
- Active Directory recycle bin
- Group managed service accounts
- Schema extensions for POSIX and Microsoft applications
  Continue reading the topics in this section to learn how to create your own
  Simple AD.

###### Topics

- [Getting started with Simple AD](simple_ad_getting_started.md "simple_ad_getting_started.md")
- [Best practices for Simple AD](simple_ad_best_practices.md "simple_ad_best_practices.md")
- [Maintain your Simple AD directory](simple_ad_maintain.md "simple_ad_maintain.md")
- [Secure your Simple AD directory](simple_ad_security.md "simple_ad_security.md")
- [Monitor your Simple AD directory](simple_ad_monitor.md "simple_ad_monitor.md")
- [Access to AWS applications and services
  from your Simple AD](simple_ad_manage_apps_services.md "simple_ad_manage_apps_services.md")
- [Ways to join an Amazon EC2 instance to your
  Simple AD](simple_ad_join_instance.md "simple_ad_join_instance.md")
- [Users and groups management in Simple AD](simple_ad_manage_users_groups.md "simple_ad_manage_users_groups.md")
- [Simple AD quotas](simple_ad_limits.md "simple_ad_limits.md")
- [Troubleshooting Simple AD](simple_ad_troubleshooting.md "simple_ad_troubleshooting.md")
