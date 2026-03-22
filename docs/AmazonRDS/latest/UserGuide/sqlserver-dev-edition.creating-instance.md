# Creating an RDS for SQL Server Developer Edition DB instance

Launching Developer Edition instance on RDS for SQL Server follows a two-step process: first create a CEV with `create-custom-db-engine-version`, Once your custom engine version is in the available state, you can create Amazon RDS database instances using the CEV.

**Key differences for Developer Edition instance creation**

| Parameter          | Developer Edition                                              |
| ------------------ | -------------------------------------------------------------- |
| `--engine`         | sqlserver-dev-ee                                               |
| `--engine-version` | Custom engine version (e.g., 16.00.4215.2.cev-dev-ss2022-cu21) |
| `--license-model`  | bring-your-own-license                                         |

To create a SQL Server Developer Edition DB instance, use the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command with the following parameters:

The following options are required:

- `--db-instance-identifier`
- `--db-instance-class`
- `--engine` – `sqlserver-dev-ee`
- `--region`
  **Examples:**

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
--db-instance-identifier my-dev-sqlserver \
--db-instance-class db.m6i.xlarge \
--engine sqlserver-dev-ee \
--engine-version `16.00.4215.2.my-dev-cev` \
--allocated-storage 200 \
--master-username admin \
--master-user-password `changeThisPassword` \
--license-model bring-your-own-license \
--no-multi-az \
--vpc-security-group-ids `sg-xxxxxxxxx` \
--db-subnet-group-name `my-db-subnet-group` \
--backup-retention-period 7 \
--region `us-west-2`
```

For Windows:

```
aws rds create-db-instance ^
--db-instance-identifier my-dev-sqlserver ^
--db-instance-class db.m6i.xlarge ^
--engine sqlserver-dev-ee ^
--engine-version `16.00.4215.2.cev-dev-ss2022-cu21` ^
--allocated-storage 200 ^
--master-username admin ^
--master-user-password `master_user_password` ^
--license-model bring-your-own-license ^
--no-multi-az ^
--vpc-security-group-ids `sg-xxxxxxxxx` ^
--db-subnet-group-name `my-db-subnet-group` ^
--backup-retention-period 7 ^
--region us-west-2
```

Refer to [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating") to create using the AWS console.
