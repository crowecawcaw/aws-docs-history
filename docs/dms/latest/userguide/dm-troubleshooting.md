# Troubleshooting for homogeneous data migrations in AWS DMS

In the following list, you can find actions to take when you encounter issues with homogeneous data migrations in AWS DMS.

###### Topics

- [I can't create a homogeneous data migration in AWS DMS](#dm-troubleshooting-create "#dm-troubleshooting-create")
- [I can't start a homogeneous data migration in AWS DMS](#dm-troubleshooting-dm-fails "#dm-troubleshooting-dm-fails")
- [I can't connect to the target database when running a data migration in AWS DMS](#dm-troubleshooting-connect-target "#dm-troubleshooting-connect-target")
- [AWS DMS migrates views as tables in PostgreSQL](#dm-troubleshooting-views "#dm-troubleshooting-views")

## I can't create a homogeneous data migration in AWS DMS

If you get an error message that says that AWS DMS can't connect to your data providers after you
choose **Create data migration**, then make sure that you have configured the required
IAM role. For more information, see [Creating an IAM role](dm-iam-resources.md#dm-resources-iam-role "dm-iam-resources.md#dm-resources-iam-role").

If you have configured the IAM role and still get this error message, then add this IAM role
to your key user in the AWS KMS key configuration. For more information, see [Allows key users to use the KMS key](../../../kms/latest/developerguide/key-policy-default.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policy-default.md#key-policy-default-allow-users") in the _AWS Key Management Service Developer Guide_.

## I can't start a homogeneous data migration in AWS DMS

If you get the `Failed` status when you start a data migration in your migration project,
check the versions of your source and target data providers. To do so, run the `SELECT VERSION();`
query in your MySQL or PostgreSQL database. Make sure that you use the supported database version.

For the list of supported source databases, see [Sources for DMS homogeneous data migrations](CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations "CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations").

For the list of supported target databases, see [Targets for DMS homogeneous data migrations](CHAP_Introduction.md#CHAP_Introduction.Targets.HomogeneousDataMigrations "CHAP_Introduction.md#CHAP_Introduction.Targets.HomogeneousDataMigrations").

If you use an unsupported database version, then upgrade your source or target database, and try again.

Check the error message for your data migration in the AWS DMS console. To do so, open your migration project,
and choose your data migration. On the **Details** tab, check the **Last failure message**
under **General**.

Finally, analyze the CloudWatch log. To do so, open your migration project, and choose your data migration.
On the **Details** tab, choose **View CloudWatch logs**.

## I can't connect to the target database when running a data migration in AWS DMS

If you get the **Unable to connect to target** error message, then perform the following actions.

1. Make sure that the security group that is attached to your source and target databases
   contains a rule for any inbound and outbound traffic. For more information, see
   [Configuring ongoing data
   replication](vpc-peering.md#vpc-peering-ongoing-replication "vpc-peering.md#vpc-peering-ongoing-replication").
2. Verify the network access control list (ACL) and route table rules.
3. Your database must be accessible from the VPC that you created. Add public IP addresses in
   VPC security groups, and allow input connections in your firewall.
4. On the **Data migrations** tab of your migration project, choose
   your data migration. Take a note of the **public IP address** under
   **Connectivity and security** on the **Details** tab. Next,
   allow access from the public IP address of your data migration in your source and target databases.
5. For ongoing data replication, make sure that your source and target databases can communicate
   with each other.

For more information, see [Control traffic to resources using security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") in the _Amazon Virtual Private Cloud User Guide_.

## AWS DMS migrates views as tables in PostgreSQL

Homogeneous data migration doesn't support migrating views as views in PostgreSQL. For PostgreSQL, AWS DMS migrates views as tables.
