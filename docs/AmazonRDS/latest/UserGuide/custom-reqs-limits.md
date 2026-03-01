# RDS Custom for Oracle requirements and limitations

In this topic, you can find a summary of the Amazon RDS Custom for Oracle feature availability and
requirements for quick reference.

###### Topics

- [General requirements for RDS Custom for Oracle](#custom-reqs-limits.reqs "#custom-reqs-limits.reqs")
- [General limitations for RDS Custom for Oracle](#custom-reqs-limits.limits "#custom-reqs-limits.limits")
- [CEV and AMI limitations for RDS Custom for Oracle](#custom-reqs-limits.cev-limits "#custom-reqs-limits.cev-limits")
- [Unsupported settings for create and modify workflows](#custom-reqs-limits.unsupported-settings "#custom-reqs-limits.unsupported-settings")
- [DB instance quotas for your AWS account](#custom-reqs-limits.quotas "#custom-reqs-limits.quotas")

## General requirements for RDS Custom for Oracle

Make sure to meet the following requirements for Amazon RDS Custom for Oracle:

- You have access to [My Oracle
  Support](https://support.oracle.com/portal/ "https://support.oracle.com/portal/") and [Oracle Software
  Delivery Cloud](https://edelivery.oracle.com/osdc/faces/Home.jspx "https://edelivery.oracle.com/osdc/faces/Home.jspx") to download the supported list of installation files
  and patches for RDS Custom for Oracle. If you use an unknown patch, custom engine version
  (CEV) creation fails. In this case, contact the RDS Custom support team and ask it
  to add the missing patch. For more information, see [Step 2: Download your database installation files and patches from Oracle Software Delivery Cloud](custom-cev.md#custom-cev.preparing.download "custom-cev.md#custom-cev.preparing.download").
- You have access to Amazon S3. You need this service for the following
  reasons:

      + You upload your Oracle installation files to S3 buckets. You use the
       uploaded installation files to create your RDS Custom CEV.
      + RDS Custom for Oracle uses scripts downloaded from internally defined S3 buckets
       to perform actions on your DB instances. These scripts are necessary for
       onboarding and RDS Custom automation.
      + RDS Custom for Oracle uploads certain files to S3 buckets located in your customer
       account. These buckets use the following naming format:
       `do-not-delete-rds-custom-``account_id`-`region`-`uuid`.
       For example, you might have a bucket named
       `do-not-delete-rds-custom-123456789012-us-east-1-12a3b4`.

  For more information, see [Step 3: Upload your installation files to Amazon S3](custom-cev.md#custom-cev.preparing.s3 "custom-cev.md#custom-cev.preparing.s3") and [Creating a CEV](custom-cev.md "custom-cev.md").

- You use the DB instance classes listed in [DB instance class support for RDS Custom for Oracle](custom-oracle-feature-support.md#custom-reqs-limits.instances "custom-oracle-feature-support.md#custom-reqs-limits.instances") to create your RDS Custom for Oracle DB instances.
- Your RDS Custom for Oracle DB instances run Oracle Linux 8 (recommended) or Oracle Linux 7. If
  you require Oracle Linux 7, contact Support. For more information, see [Considerations for RDS Custom for Oracle database upgrades](custom-upgrading-considerations.md "custom-upgrading-considerations.md").
- You specify the gp2, gp3, or io1 solid state drives for Amazon EBS storage. The
  maximum storage size is 64 TiB.
- You have an AWS KMS key to create an RDS Custom for Oracle DB instance. For more information, see
  [Step 1: Create or reuse a symmetric encryption AWS KMS key](custom-setup-orcl.md#custom-setup-orcl.cmk "custom-setup-orcl.md#custom-setup-orcl.cmk").
- You have the AWS Identity and Access Management (IAM) role and instance profile required for creating
  RDS Custom for Oracle DB instances. For more information, see [Step 4: Configure IAM for RDS Custom for Oracle](custom-setup-orcl.md#custom-setup-orcl.iam-vpc "custom-setup-orcl.md#custom-setup-orcl.iam-vpc").
- The AWS Identity and Access Management (IAM) user that creates a CEV or RDS Custom DB instance has the required
  permissions for IAM, CloudTrail, and Amazon S3.

For more information, see [Step 5: Grant required permissions to your IAM user or role](custom-setup-orcl.md#custom-setup-orcl.iam-user "custom-setup-orcl.md#custom-setup-orcl.iam-user").

- You supply your own virtual private cloud (VPC) and security group
  configuration. For more information, see [Step 6: Configure your VPC for RDS Custom for Oracle](custom-setup-orcl.md#custom-setup-orc.vpc-config "custom-setup-orcl.md#custom-setup-orc.vpc-config").
- You supply a networking configuration that RDS Custom for Oracle can use to access other
  AWS services. For specific requirements, see [Step 4: Configure IAM for RDS Custom for Oracle](custom-setup-orcl.md#custom-setup-orcl.iam-vpc "custom-setup-orcl.md#custom-setup-orcl.iam-vpc").

## General limitations for RDS Custom for Oracle

The following limitations apply to RDS Custom for Oracle:

- You can't modify the DB instance identifier of an existing RDS Custom for Oracle DB instance.
- You can't specify the Oracle multitenant architecture for any release except
  Oracle Database 19c.
- You can't create multiple Oracle databases on a single RDS Custom for Oracle
  DB instance.
- You can’t stop your RDS Custom for Oracle DB instance or its underlying Amazon EC2 instance. Billing
  for an RDS Custom for Oracle DB instance can't be stopped.
- You can't use automatic shared memory management because RDS Custom for Oracle supports
  automatic memory management only. For more information, see [Automatic Memory Management](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-memory.html#GUID-04EFED7D-D1F1-43C3-B78F-0FF9AFAC02B0 "https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-memory.html#GUID-04EFED7D-D1F1-43C3-B78F-0FF9AFAC02B0") in the _Oracle Database
  Administrator’s Guide_.
- Make sure not to change the `DB_UNIQUE_NAME` for the primary DB instance.
  Changing the name causes any restore operation to become stuck.
- You can't make more than 20 snapshot copies at the same time in the same
  Region.
- You can't use the `describe-reserved-db-instances` API for
  RDS Custom for Oracle DB instances.

For limitations specific to modifying an RDS Custom for Oracle DB instance, see [Modifying your RDS Custom for Oracle DB instance](custom-managing.md "custom-managing.md"). For
replication limitations, see [General limitations for RDS Custom for Oracle replication](custom-rr.md#custom-rr.limitations "custom-rr.md#custom-rr.limitations").

## CEV and AMI limitations for RDS Custom for Oracle

The following limitations apply to RDS Custom for Oracle CEVs and AMIs:

- You can't provide your own AMI for use in an RDS Custom for Oracle CEV. You can specify either the
  default AMI, which uses Oracle Linux 8, or an AMI that has been previously used by an
  RDS Custom for Oracle CEV.

###### Note

RDS Custom for Oracle releases a new default AMI when common vulnerabilities and exposures are
discovered. No fixed schedule is available or guaranteed. RDS Custom for Oracle tends to publish a
new default AMI every 30 days.

- You can't modify a CEV to use a different AMI.
- You can't create a CDB instance from a CEV that uses the
  `custom-oracle-ee` or `custom-oracle-se2` engine
  types. The CEV must use `custom-oracle-ee-cdb` or
  `custom-oracle-se2-cdb`.
- RDS Custom for Oracle doesn't currently allow you to upgrade the OS of your RDS Custom for Oracle DB instance
  with RDS API calls. As a workaround, you can update your OS manually with the following command:
  `sudo yum update --security`.

## Unsupported settings for create and modify workflows

When you create or modify an RDS Custom for Oracle DB instance, you can't do the following:

- Change the number of CPU cores and threads per core on the DB instance class.
- Turn on storage autoscaling.
- Set backup retention to `0`.
- Configure Kerberos authentication.
- Specify your own DB parameter group or option group.
- Turn on Performance Insights.
- Turn on automatic minor version upgrade.

## DB instance quotas for your AWS account

Make sure that the combined number of RDS Custom and Amazon RDS DB instances doesn't exceed your
quota limit. For example, if your quota for Amazon RDS is 40 DB instances, you can have 20
RDS Custom for Oracle DB instances and 20 Amazon RDS DB instances.
