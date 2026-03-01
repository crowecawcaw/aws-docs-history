# Requirements for using Trusted Language Extensions for PostgreSQL

The following are requirements for setting up and using the TLE development kit.

- RDS for PostgreSQL versions – Trusted Language Extensions
  is supported on
  RDS for PostgreSQL versions 13.12 and higher 13 versions, 14.5 and higher 14 versions, and 15.2 and higher versions only.
  - If you need to upgrade your RDS for PostgreSQL instance,
    see
    [Upgrades of the RDS for PostgreSQL DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").
  - If you don't yet have an
    Amazon RDS DB instance running
    PostgreSQL, you can create one. For more information, see

  RDS for PostgreSQL DB instance, see [Creating and connecting to a PostgreSQL DB instance](CHAP_GettingStarted.CreatingConnecting.md "CHAP_GettingStarted.CreatingConnecting.md").

- Requires `rds_superuser` privileges – To set
  up and configure the `pg_tle` extension, your database user role must
  have the permissions of the `rds_superuser` role. By default, this
  role is granted to the `postgres` user that creates the
  RDS for PostgreSQL DB instance.
- Requires a custom DB
  parameter group – Your RDS for PostgreSQL DB instance must be
  configured with a custom DB parameter group.
  - If your
    RDS for PostgreSQL DB instance
    isn't configured with a custom DB parameter group, you should
    create one and associate it with your RDS for PostgreSQL DB instance. For a
    short summary of steps, see [Creating and applying a custom DB parameter group](#PostgreSQL_trusted_language_extension-requirements-create-custom-params "#PostgreSQL_trusted_language_extension-requirements-create-custom-params").
  - If your
    RDS for PostgreSQL DB instance is already
    configured using a custom DB parameter group, you can set up Trusted Language Extensions. For details,
    see [Setting up Trusted Language Extensions in your RDS for PostgreSQL DB instance](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md").

## Creating and applying a custom DB parameter group

Use the following steps to create a custom DB parameter group and configure your RDS for PostgreSQL DB
instance to use it.

###### To create a custom DB parameter group and use it with your RDS for PostgreSQL DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose Parameter groups from the Amazon RDS menu.
3. Choose **Create parameter group**.
4. In the **Parameter group details** page, enter the following information.
   - For **Parameter group family**, choose
     postgres14.
   - For **Type**, choose DB Parameter Group.
   - For **Group name**, give your parameter group a meaningful name in the
     context of your operations.
   - For **Description**, enter a useful description so that others on your team can easily find it.

5. Choose **Create**. Your custom DB parameter group is created in your
   AWS Region. You can now modify your RDS for PostgreSQL
   DB instance to use it by following the next steps.
6. Choose **Databases** from the Amazon RDS menu.
7. Choose the RDS for PostgreSQL DB instance that
   you want to use with TLE from among those listed, and then choose **Modify.**
8. In the Modify DB instance settings page, find
   **Database options** in the Additional
   configuration section and choose your custom DB parameter group
   from the selector.
9. Choose **Continue** to save the change.
10. Choose **Apply immediately** so that you can continue setting up the RDS for PostgreSQL DB instance to use TLE.
    To continue setting up your system for Trusted Language Extensions, see [Setting up Trusted Language Extensions in your RDS for PostgreSQL DB instance](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md").

For more information working with
DB parameter groups, see
[DB parameter groups for Amazon RDS DB instances](USER_WorkingWithDBInstanceParamGroups.md "USER_WorkingWithDBInstanceParamGroups.md").

You can avoid specifying the `--region` argument when you use CLI commands by configuring your AWS CLI
with your default AWS Region. For more information, see [Configuration
basics](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the _AWS Command Line Interface User Guide_.

###### To create a custom DB parameter group and use it with your RDS for PostgreSQL DB instance

1. Use the [create-db-parameter-group](../../../cli/latest/reference/rds/create-db-parameter-group.md "../../../cli/latest/reference/rds/create-db-parameter-group.md") AWS CLI
   command to create a custom DB parameter group based on
   postgres14 for your AWS Region.

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
  --region `aws-region` \
  --db-parameter-group-name `custom-params-for-pg-tle` \
  --db-parameter-group-family postgres14 \
  --description "My custom DB parameter group for Trusted Language Extensions"
```

For Windows:

```
aws rds create-db-parameter-group ^
  --region `aws-region` ^
  --db-parameter-group-name `custom-params-for-pg-tle` ^
  --db-parameter-group-family postgres14 ^
  --description "My custom DB parameter group for Trusted Language Extensions"
```

Your custom DB parameter group is available in your
AWS Region, so you can modify RDS for PostgreSQL
DB instance to use it. 2. Use the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") AWS CLI
command to apply your custom DB parameter group to your RDS for PostgreSQL DB instance. This
command immediately reboots the active instance.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
  --region `aws-region` \
  --db-instance-identifier `your-instance-name` \
  --db-parameter-group-name `custom-params-for-pg-tle` \
  --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
  --region `aws-region` ^
  --db-instance-identifier `your-instance-name` ^
  --db-parameter-group-name `custom-params-for-pg-tle` ^
  --apply-immediately
```

To continue setting up your system for Trusted Language Extensions, see [Setting up Trusted Language Extensions in your RDS for PostgreSQL DB instance](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md").

For more information, see
[Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
