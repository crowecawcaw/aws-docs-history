# Requirements for using Trusted Language Extensions for PostgreSQL

The following are requirements for setting up and using the TLE development kit.

- Aurora PostgreSQL versions
  – Trusted Language Extensions
  is supported on Aurora PostgreSQL version 14.5
  and higher versions only.
  - If you need to upgrade your Aurora PostgreSQL DB
    cluster,
    see [Upgrading Amazon Aurora PostgreSQL DB clusters](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").
  - If you don't yet have an Aurora DB cluster
    running
    PostgreSQL, you can create one. For more information, see
    [Creating and connecting to an Aurora PostgreSQL DB cluster](CHAP_GettingStartedAurora.CreatingConnecting.md "CHAP_GettingStartedAurora.CreatingConnecting.md").

- Requires `rds_superuser` privileges – To set
  up and configure the `pg_tle` extension, your database user role must
  have the permissions of the `rds_superuser` role. By default, this
  role is granted to the `postgres` user that creates the Aurora PostgreSQL DB cluster.
- Requires a custom DB
  parameter group – Your Aurora PostgreSQL DB cluster must be
  configured with a custom DB parameter group. You use the
  custom DB parameter group for the writer instance of your
  Aurora PostgreSQL DB cluster.
  - If your Aurora PostgreSQL DB cluster

  isn't configured with a custom DB parameter group, you should
  create one and associate it with the writer
  instance of your Aurora PostgreSQL DB cluster. For a
  short summary of steps, see [Creating and applying a custom DB parameter group](#PostgreSQL_trusted_language_extension-requirements-create-custom-params "#PostgreSQL_trusted_language_extension-requirements-create-custom-params").
  - If your Aurora PostgreSQL DB cluster
    is already
    configured using a custom DB parameter group, you can set up Trusted Language Extensions. For details,
    see [Setting up Trusted Language Extensions in your Aurora PostgreSQL DB cluster](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md").

## Creating and applying a custom DB parameter group

Use the following steps to create a custom DB parameter group and configure your Aurora PostgreSQL DB cluster to use it.

###### To create a custom DB parameter group and use it with your Aurora PostgreSQL DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose Parameter groups from the Amazon RDS menu.
3. Choose **Create parameter group**.
4. In the **Parameter group details** page, enter the following information.
   - For **Parameter group family**, choose aurora-postgresql14.
   - For **Type**, choose DB Parameter Group.
   - For **Group name**, give your parameter group a meaningful name in the
     context of your operations.
   - For **Description**, enter a useful description so that others on your team can easily find it.

5. Choose **Create**. Your custom DB parameter group is created in your
   AWS Region. You can now modify your Aurora PostgreSQL DB cluster to use it by following the next steps.
6. Choose **Databases** from the Amazon RDS menu.
7. Choose the Aurora PostgreSQL DB cluster that
   you want to use with TLE from among those listed, and then choose **Modify.**
8. In the Modify DB cluster settings page, find **Database
   options** and use the selector to choose your
   custom DB parameter group.
9. Choose **Continue** to save the change.
10. Choose **Apply immediately** so that you can continue setting up the Aurora PostgreSQL
    DB cluster to use TLE.
    To continue setting up your system for Trusted Language Extensions, see [Setting up Trusted Language Extensions in your Aurora PostgreSQL DB cluster](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md").

For more information working with DB cluster and DB parameter groups, see
[DB cluster parameter groups for Amazon Aurora DB clusters](USER_WorkingWithDBClusterParamGroups.md "USER_WorkingWithDBClusterParamGroups.md").

You can avoid specifying the `--region` argument when you use CLI commands by configuring your AWS CLI
with your default AWS Region. For more information, see [Configuration
basics](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the _AWS Command Line Interface User Guide_.

###### To create a custom DB parameter group and use it with your Aurora PostgreSQL DB cluster

1. Use the [create-db-parameter-group](../../../cli/latest/reference/rds/create-db-parameter-group.md "../../../cli/latest/reference/rds/create-db-parameter-group.md") AWS CLI
   command to create a custom DB parameter group based on aurora-postgresql14
   for your AWS Region. Note that in this
   step you create a DB parameter group to apply to the writer instance of your Aurora PostgreSQL DB cluster.

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
  --region `aws-region` \
  --db-parameter-group-name `custom-params-for-pg-tle` \
  --db-parameter-group-family aurora-postgresql14 \
  --description "My custom DB parameter group for Trusted Language Extensions"
```

For Windows:

```
aws rds create-db-parameter-group ^
  --region `aws-region` ^
  --db-parameter-group-name `custom-params-for-pg-tle` ^
  --db-parameter-group-family aurora-postgresql14 ^
  --description "My custom DB parameter group for Trusted Language Extensions"
```

Your custom DB parameter group is available in your
AWS Region, so you can modify the writer instance of your Aurora PostgreSQL DB
cluster to use it. 2. Use the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") AWS CLI
command to apply your custom DB parameter group to the writer instance of your Aurora PostgreSQL DB cluster. This
command immediately reboots the active instance.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
  --region `aws-region` \
  --db-instance-identifier `your-writer-instance-name` \
  --db-parameter-group-name `custom-params-for-pg-tle` \
  --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
  --region `aws-region` ^
  --db-instance-identifier `your-writer-instance-name` ^
  --db-parameter-group-name `custom-params-for-pg-tle` ^
  --apply-immediately
```

To continue setting up your system for Trusted Language Extensions, see [Setting up Trusted Language Extensions in your Aurora PostgreSQL DB cluster](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md").

For more information, see [DB parameter groups for Amazon Aurora DB instances](USER_WorkingWithDBInstanceParamGroups.md "USER_WorkingWithDBInstanceParamGroups.md")
.
