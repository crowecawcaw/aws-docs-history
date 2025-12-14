#

Remediating exposures for Amazon RDS instances and clusters

AWS Security Hub can generate exposure findings for Amazon RDS instances and clusters.

On the Security Hub console, the Amazon RDS instance or cluster involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details.
Programmatically, you can retrieve resource details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it.
Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential,
follow these recommended remediation steps to help mitigate the risk. The remediation topics are
divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down
its severity level by addressing just one remediation topic. Your approach to risk remediation
depends on your organizational requirements and workloads.

###### Note

The remediation guidance provided in this topic might require additional consultation in other AWS resources.

###### Contents

- [Misconfiguration traits for Amazon RDS instances and clusters](exposure-rds.md#rds-instance-cluster-misconfiguration "exposure-rds.md#rds-instance-cluster-misconfiguration")
  - [The Amazon RDS DB instance is configured with public access](exposure-rds.md#public-access-configured "exposure-rds.md#public-access-configured")
  - [The Amazon RDS DB cluster has a snapshot that's shared publicly](exposure-rds.md#publicly-available-rds-cluster-snapshot "exposure-rds.md#publicly-available-rds-cluster-snapshot")
  - [The Amazon RDS DB instance has a snapshot that is not encrypted at rest](exposure-rds.md#unencrypted-rds-database-snapshot "exposure-rds.md#unencrypted-rds-database-snapshot")
  - [The Amazon RDS DB cluster has a snapshot that is not encrypted at rest](exposure-rds.md#unencrypted-rds-cluster-snapshot "exposure-rds.md#unencrypted-rds-cluster-snapshot")
  - [The Amazon RDS DB instance has an open security group](exposure-rds.md#open-security-group "exposure-rds.md#open-security-group")
  - [The Amazon RDS DB instance has IAM database authentication disabled](exposure-rds.md#rds-instance-iam-authentication-disabled "exposure-rds.md#rds-instance-iam-authentication-disabled")
  - [The Amazon RDS DB instance uses the default admin username](exposure-rds.md#rds-instance-default-admin-name-used "exposure-rds.md#rds-instance-default-admin-name-used")
  - [The Amazon RDS DB cluster uses the default admin username](exposure-rds.md#rds-cluster-misconfiguration-db-cluster-uses-default-admin-username "exposure-rds.md#rds-cluster-misconfiguration-db-cluster-uses-default-admin-username")
  - [The Amazon RDS DB instance has automatic minor version upgrades disabled](exposure-rds.md#rds-instance-minor-version-upgrades-disabled "exposure-rds.md#rds-instance-minor-version-upgrades-disabled")
  - [The Amazon RDS DB instance has automated backups disabled](exposure-rds.md#rds-instance-backups-disabled "exposure-rds.md#rds-instance-backups-disabled")
  - [The Amazon RDS DB instance has deletion protection disabled](exposure-rds.md#rds-instance-deletion-protection-disabled "exposure-rds.md#rds-instance-deletion-protection-disabled")
  - [The Amazon RDS DB cluster has deletion protection disabled](exposure-rds.md#rds-cluster-misconfiguration-db-cluster-deletion-protection-disabled "exposure-rds.md#rds-cluster-misconfiguration-db-cluster-deletion-protection-disabled")
  - [The Amazon RDS DB instance uses the default port for the database engine](exposure-rds.md#rds-instance-default-port-in-use "exposure-rds.md#rds-instance-default-port-in-use")
  - [The Amazon RDS DB instance is not covered by a backup plan](exposure-rds.md#rds-instance-not-in-backup-plan "exposure-rds.md#rds-instance-not-in-backup-plan")

## Misconfiguration traits for Amazon RDS instances and clusters

The following describes the misconfiguration traits and remediation steps for Amazon RDS instances and clusters.

### The Amazon RDS DB instance is configured with public access

Amazon RDS instances with public access are potentially accessible over the internet through their endpoints.
While public access is sometimes necessary for instance functionality, this configuration can be used as a potential attack vector for unauthorized users to attempt to access your database.
Publicly accessible databases can be exposed to port scanning, brute force attacks, and exploitation attempts.
Following standard security principles, we recommend that you limit public exposure of your database resources.

1. **Modify public access settings**

In the exposure finding, open the resource with the hyperlink.
This will open the affected DB instance.
Evaluate whether the DB instance requires public accessibility based on your application architecture.
For more information, see [Setting up public or private access in Amazon RDS](../../../AmazonRDS/latest/gettingstartedguide/security-public-private.md "../../../AmazonRDS/latest/gettingstartedguide/security-public-private.md").

### The Amazon RDS DB cluster has a snapshot that's shared publicly

Public snapshots can be accessed by any AWS account, potentially exposing sensitive data to unauthorized users.
Any AWS account has permission to copy these public snapshots and create DB instances from them, which could lead to data breaches or unauthorized data access.
Following security best practices, we recommend restricting access to your Amazon RDS snapshots to only trusted AWS accounts and organizations.

######

1.  Configure an Amazon RDS snapshot for private access

In the exposure finding, open the resource through the hyperlink.
For information about how to modify snapshot sharing settings, see [Sharing a snapshot](../../../AmazonRDS/latest/AuroraUserGuide/aurora-share-snapshot.md#aurora-share-snapshot.Sharing "../../../AmazonRDS/latest/AuroraUserGuide/aurora-share-snapshot.md#aurora-share-snapshot.Sharing") in the _Amazon Aurora User Guide._
For information about how to stop sharing snapshots, see [Stopping snapshot sharing](../../../AmazonRDS/latest/AuroraUserGuide/share-snapshot-stop.md "../../../AmazonRDS/latest/AuroraUserGuide/share-snapshot-stop.md") in the _Amazon Aurora User Guide._.

### The Amazon RDS DB instance has a snapshot that is not encrypted at rest

Unencrypted Amazon RDS DB instance snapshots may expose sensitive data if unauthorized access to the storage layer is obtained.
Without encryption, data in snapshots could potentially be exposed through unauthorized access.
This creates a risk of data breaches and compliance violations.
Following security best practices, we recommend encrypting all database resources and their backups to maintain data confidentiality.

######

In the exposure finding, open the resource with the hyperlink.
This will open the affected snapshot.
You cannot directly encrypt an existing unencrypted snapshot. Instead, create an encrypted copy of the unencrypted snapshot.
For detailed instructions, see [DB cluster snapshot copying and Encrypting Amazon RDS resources](../../../AmazonRDS/latest/AuroraUserGuide/aurora-copy-snapshot.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-copy-snapshot.md") in the _Amazon Aurora User Guide._..

### The Amazon RDS DB cluster has a snapshot that is not encrypted at rest

Unencrypted Amazon RDS DB cluster snapshots may expose sensitive data if unauthorized access to the storage layer is obtained.
Without encryption, data in snapshots could potentially be exposed through unauthorized access.
This creates a risk of data breaches and compliance violations.
Following security best practices, we recommend encrypting all database resources and their backups to maintain data confidentiality.

######

1.  Create an encrypted copy of the snapshot

In the exposure finding, open the resource with the hyperlink.
This will open the affected snapshot.
You cannot directly encrypt an existing unencrypted snapshot. Instead, create an encrypted copy of the unencrypted snapshot.
For detailed instructions, see [DB cluster snapshot copying and Encrypting Amazon RDS resources](../../../AmazonRDS/latest/AuroraUserGuide/aurora-copy-snapshot.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-copy-snapshot.md") in the _Amazon Aurora User Guide._..

### The Amazon RDS DB instance has an open security group

Security groups act as virtual firewalls for your Amazon RDS instances to control inbound and outbound traffic.
Open security groups, which allow unrestricted access from any IP address, may expose your database instances to unauthorized access and potential attacks.
Following standard security principles, we recommend restricting security group access to specific IP addresses and ports to maintain the principle of least privilege.

###### Review security group rules and assess current configuration

In the exposure finding, open the resource for the DB instance Security Group.
Evaluate which ports are open and accessible from broad IP ranges, such as `(0.0.0.0/0 or ::/0)`.
For information about viewing security group details, see [DescribeSecurityGroups](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md") in the _Amazon Elastic Compute Cloud API Reference_.

###### Modify security group rules

Modify your security group rules to restrict access to specific trusted IP addresses or ranges.
When updating your security group rules, consider separating access requirements for different network segments by creating rules for each required source IP range or restricting access to specific ports.
To modify security group rules, see [Configure security group rules](../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules "../../../AWSEC2/latest/UserGuide/changing-security-group.md#add-remove-security-group-rules") in the _Amazon EC2 User Guide_.
To modify the default port of an existing Amazon RDS database instance, see Modifying the DB cluster by using the console, CLI, and API in the _Amazon Aurora User Guide_.

### The Amazon RDS DB instance has IAM database authentication disabled

IAM database authentication allows you to authenticate to your Amazon RDS database using IAM credentials instead of database passwords.
This provides several security benefits, such as centralized access management, temporary credentials, and elimination of storing database passwords in application code.
IAM database authentication allows authentication to database instances with an authentication token instead of a password.
As a result, network traffic to and from the database instance is encrypted using SSL.
Without IAM authentication, databases typically rely on password-based authentication, which can lead to password reuse and weak passwords.
Following security best practices, we recommend enabling IAM database authentication.

###### Enable IAM database authentication

In the exposure finding, open the resource with the hyperlink.
This will open the affected DB instance.
You can enable IAM database authentication in the Database options.
For more information, see [Enabling and disabling IAM database authentication](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.md") in the _Amazon RDS User Guide_.
After enabling IAM authentication, update your DB instances to use IAM authentication instead of password based authentication.

### The Amazon RDS DB instance uses the default admin username

Using default usernames (e.g., “admin”, “root”) for DB instances increases security risk as these are widely known and commonly targeted in brute force attacks.
Default usernames are predictable and make it easier for unauthorized users to attempt to gain access to your database.
With default usernames, attackers only need to obtain passwords rather than needing both to gain access to your database.
Following security best practices, we recommend using unique administrator usernames for your database instance to enhance security through obscurity and reduce the risk of unauthorized access attempts.

###### Configure a unique administrator username

In the exposure finding, open the resource with the hyperlink.
This will open the affected DB instance.
Consider what backup frequency, retention period, and lifecycle rules are best for your applications.

### The Amazon RDS DB cluster uses the default admin username

Using default usernames (e.g., “admin”, “root”) for DB instances increases security risk as these are widely known and commonly targeted in brute force attacks.
Default usernames are predictable and make it easier for unauthorized users to attempt to gain access to your database. With default usernames, attackers only need to obtain passwords rather than needing both to gain access to your database.
Following security best practices, we recommend using unique administrator usernames for your database instance to enhance security through obscurity and reduce the risk of unauthorized access attempts.

###### Configure a unique administrator username

In the exposure finding, open the resource with the hyperlink.
This will open the affected DB instance.
You cannot change the administrator username of an existing Amazon RDS DB instance.
To create a unique administrator name, you need to create a new DB instance with a custom username and migrate your data.

### The Amazon RDS DB instance has automatic minor version upgrades disabled

Automatic minor version upgrades ensure that your Amazon RDS instances automatically receive minor engine version upgrades when they become available.
These upgrades often include important security patches and bug fixes that help maintain the security and stability of your database.
Your database is at risk of running with known security vulnerabilities that have been fixed in newer minor versions.
Without automatic updates, database instances can accumulate security vulnerabilities as new CVEs are discovered.
Following security best practices, we recommend enabling automatic minor version upgrades for all Amazon RDS instances.

###### Enable automatic minor version upgrades

In the exposure finding, open the resource with the hyperlink.
This will open the affected DB instance.
You can view automatic minor upgrade settings in the **Maintenance & backups** tab.
For more information, see [Automatic minor version upgrades for Amazon RDS for MySQL](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.md").
You can also configure your maintenance window to occur during periods of low database activity.

### The Amazon RDS DB instance has automated backups disabled

Automated backups provide point-in-time recovery for your Amazon RDS instances, allowing you to restore your database to any point within your retention period.
When automated backups are disabled, you risk losing data in case of malicious deletion, data corruption, or other data loss scenarios.
In the event of malicious activity like ransomware attacks, database table deletion, or corruption, the ability to restore to a point in time before the incident reduces the time required to recover from an incident.
Following security best practices, we recommend enabling automated backups with an appropriate retention period for all [production databases](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md").

### The Amazon RDS DB instance has deletion protection disabled

Database deletion protection is a feature that helps prevent the deletion of your database instances.
When deletion protection is disabled, your database can be deleted by any user with sufficient permissions, potentially resulting in data loss or application downtime.
Attackers can delete your database, leading to service disruption, data loss, and increased recovery time.
Following security best practices, we recommend enabling deletion protection for your RDS DB instances to prevent malicious deletion.

###### Enable delete protection for your Amazon RDS DB cluster

In the exposure finding, open the resource with the hyperlink.
This will open the affected DB cluster.

### The Amazon RDS DB cluster has deletion protection disabled

Database deletion protection is a feature that helps prevent the deletion of your database instances.
When deletion protection is disabled, your database can be deleted by any user with sufficient permissions, potentially resulting in data loss or application downtime.
Attackers can delete your database, leading to service disruption, data loss, and increased recovery time.
Following security best practices, we recommend enabling deletion protection for your RDS DB clusters to prevent malicious deletion.

###### Enable delete protection for your Amazon RDS DB cluster

In the exposure finding, open the resource with the hyperlink.
This will open the affected DB cluster.

### The Amazon RDS DB instance uses the default port for the database engine

Amazon RDS instances that use default ports for database engines may face increased security risks, as these default ports are widely known and are often targeted by automated scanning tools.
Modifying your DB instance to use non-default ports adds an additional layer of security through obscurity, making it more difficult for unauthorized users to perform automated or targeted attacks on your database.
Default ports are commonly scanned for by unauthorized persons, and may cause your DB instance to be targeted.
Following security best practices, we recommend changing the default port to a custom port to reduce the risk of automated or targeted attacks.

######

In the exposure finding, open the resource with the hyperlink.
This will open the affected DB instance.

###### Update application connection strings

After changing the port, update all applications and services that connect to your Amazon RDS instance to use the new port number.

### The Amazon RDS DB instance is not covered by a backup plan

AWS Backup is a fully managed backup service that centralizes and automates the backup of data across AWS services.
If your DB instance is not covered by a backup plan, you risk losing data in case of malicious deletion, data corruption, or other data loss scenarios.
In the event of malicious activity like ransomware attacks, database table deletion, or corruption, the ability to restore to a point in time before the incident reduces the time required to recover from an incident.
Following security best practices, we recommend including your Amazon RDS instances in a backup plan to ensure data protection.

###### Create and assign a backup plan for your DB instance

In the exposure finding, open the resource with the hyperlink.
This will open the affected DB instance.
Consider what backup frequency, retention period, and lifecycle rules are best for your applications.
