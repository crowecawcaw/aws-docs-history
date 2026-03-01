# Known issues for Amazon RDS Custom for Oracle

When working with RDS Custom for Oracle, note the following issues for DB instances:

- Resizing the root or dbbin volumes isn't supported.

###### Warning

We strongly recommend that you don't resize the root or dbbin volumes
manually. We recommend that you store all configurations in the data volume,
which persists after patching, and that you resize the volume using only the RDS
scale storage API.

- Some RDS APIs can be blocked when a database instance is on an older AMI, for
  example, an AMI that uses Oracle Linux 7. To resolve this issue, patch your DB instance to
  the latest AMI using OS patching. For more information, see [CEV upgrade options](custom-upgrading.md#custom-upgrading.overview.cev-options "custom-upgrading.md#custom-upgrading.overview.cev-options").
- Before you perform RDS operations, make sure that your AWS account has enough
  quota for compute and storage.
- If the database is in the creation state, and you actively log in to the database
  or Amazon EC2 host and run commands, database creation might not complete.
- Control file multiplexing isn't currently supported because of a read replica
  issue. Before you create a read replica, make sure to specify only one file name in
  the `CONTROL_FILES` initialization parameter on the source
  database.
- You can't change the database mode from `PHYSICAL STANDBY` (mounted or
  read-only) to `SNAPSHOT STANDBY` (converting to read/write).
- If an AWS account is part of an AWS Organization with a service control policy
  (SCP), and the SCP contains a condition key, an RDS Custom for Oracle DB instance might fail to create
  with the following error:

```
You can't create the DB instance because of incompatible resources.
The IAM instance profile role [AWSRDSCustomInstanceRole1-us-east-1] is missing the following permissions:
EFFECT [Allow] on ACTION(S) [ssm:DescribeAssociation, ssm:DescribeDocument, ssm:GetConnectionStatus,
  ssm:GetDeployablePatchSnapshotForInstance, ssmmessages:OpenControlChannel, ssm:GetParameters,
  ssm:ListInstanceAssociations, ssm:PutConfigurePackageResult, ssmmessages:CreateControlChannel,
  ssm:GetParameter, ssm:UpdateAssociationStatus, ssm:GetManifest, ssmmessages:CreateDataChannel,
  ssm:PutInventory, ssm:UpdateInstanceInformation, ssm:DescribeInstanceInformation,
  ssmmessages:OpenDataChannel, ssm:GetDocument, ssm:ListAssociations, ssm:PutComplianceItems,
  ssm:UpdateInstanceAssociationStatus] for RESOURCE(S) [], EFFECT [Allow] on ACTION(S) [ec2messages:DeleteMessage,
  ec2messages:FailMessage, ec2messages:GetEndpoint, ec2messages:AcknowledgeMessage, ec2messages:GetMessages,
  ec2messages:SendReply] for RESOURCE(S) [], EFFECT [Allow] on ACTION(S) [logs:CreateLogStream,
  logs:DescribeLogStreams, logs:PutRetentionPolicy, logs:PutLogEvents]
```

To resolve this issue, create a ticket with Support.

## Known issues with database user accounts

Note the following issues:

- Don't remove database user accounts that begin with the string
  `RDS`, such as `RDSADMIN` and
  `RDS_DATAGUARD`. RDS Custom for Oracle uses the `RDS` account for
  automation. If you remove this user account, RDS Custom moves the instance to the
  unsupported configuration state.
- You can't change the master username for your RDS Custom for Oracle DB instance using the
  `ModifyDBInstance` API.
- RDS Custom for Oracle rotates user account credentials on all DB instances. For more
  information, see [Rotating RDS Custom for Oracle credentials for compliance programs](custom-security.md "custom-security.md"). If you use an on-premises
  primary/standby configuration, credential rotation might affect the following
  resources:
  - Manually created standby RDS Custom for Oracle instances

  To resolve this issue, drop the manual standby databases, and then
  create an Oracle read replica using an API call. Manage the secrets
  manually for the manual standby databases so that they match the source
  DB instance.
  - Manually created cross-Region read replicas

  To resolve this issue, manually keep the secrets so that they match
  the primary DB instance.

## Known issues with parameter and configuration files

- You must configure the `crontab` file after scale compute, OS
  upgrades, and other operations where RDS Custom replaces the root volume. We highly
  recommend that you keep a backup of `crontab`.
- Note the following guidelines when you configure the
  `listener.ora` file:
  - Make sure that every entry in the file is on a single line. This
    approach avoids issues with indentation during instance creation.
  - Make sure that `GLOBAL_DBNAME` is equal to the value of
    `SID_NAME`.
  - Make sure the value for `LISTENER` follows the naming
    convention `L_`dbname`_001`.
  - Make sure the `listener.ora` file maintains a connection to
    the database name. RDS Custom uses this connection to verify database
    startup. If you modify this file incorrectly, operations such as scale
    compute or patching might fail.

  The following example shows a `listener.ora` that is
  configured correctly:

  ```
  ADR_BASE_L_ORCL_001=/rdsdbdata/log/
  USE_SID_AS_SERVICE_L_ORCL_001=ON
  SID_LIST_L_ORCL_001=(SID_LIST = (SID_DESC = (SID_NAME = ORCL)(GLOBAL_DBNAME = ORCL) (ORACLE_HOME = /rdsdbbin/oracle.19.custom.r1.EE.1)))
  SUBSCRIBE_FOR_NODE_DOWN_EVENT_L_ORCL_001=OFF
  L_ORCL_001=(DESCRIPTION_LIST = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(PORT = XXXX)(HOST = x.x.x.x))) (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(PORT = XXXX)(HOST = 127.0.0.1))))
  ```

- Comments aren't supported in a server parameter file or initialization
  parameter file.
- You must declare the following initialization parameters in the server
  parameter file (`/rdsdbdata/config/oracle_pfile`):

      + `MEMORY_MAX_TARGET`
      + `MEMORY_TARGET`
      + `PGA_AGGREGATE_TARGET`
      + `PROCESSES`
      + `SGA_TARGET`
      + `USE_LARGE_PAGES`

  If the preceding parameters aren't declared in
  `/rdsdbdata/config/oracle_pfile`, read replica creation
  and scale compute might fail.

- You can't delete the symbolic links for configuration files such as the server
  parameter file, audit files, `listener.ora`,
  `tnsnames.ora`, or `sqlnet.ora`. You
  also can't modify the directory structure for these files. RDS Custom automation
  expects these files to exist in a specific directory structure.

To create a server parameter file from an initialization parameter file, use
the following syntax.

```
CREATE SPFILE='/rdsdbdata/admin/$ORACLE_SID/pfile/spfile$ORACLE_SID.ora'
    FROM PFILE='/rdsdbdata/config/oracle_pfile';
```
