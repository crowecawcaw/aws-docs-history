# Creating an RDS for SQL Server Developer Edition DB instance

Launching Developer Edition instance on RDS for SQL Server follows a two-step process: first create a CEV with `create-custom-db-engine-version`, Once your custom engine version is in the available state, you can create Amazon RDS database instances using the CEV.

**Key differences for Developer Edition instance creation**

| Parameter          | Developer Edition                                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `--engine`         | `sqlserver-dev-ee` (Enterprise Edition capabilities) or `sqlserver-dev-se` (Standard Edition capabilities, SQL Server 2025 only) |
| `--engine-version` | Custom engine version (e.g., `17.00.4045.5.cev-dev-ss2025-cu5`)                                                                  |
| `--license-model`  | bring-your-own-license                                                                                                           |

To create a SQL Server Developer Edition DB instance, use the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command with the following parameters:

The following options are required:

- `--db-instance-identifier`
- `--db-instance-class`
- `--engine` – `sqlserver-dev-ee` (Enterprise Edition capabilities) or `sqlserver-dev-se` (Standard Edition capabilities, SQL Server 2025 only)
- `--region`
  **Examples:**

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
--db-instance-identifier my-dev-sqlserver \
--db-instance-class db.m6i.xlarge \
--engine sqlserver-dev-ee \
--engine-version `17.00.4045.5.cev-dev-ss2025-cu5` \
--allocated-storage 200 \
--master-username admin \
--master-user-password `changeThisPassword` \
--license-model bring-your-own-license \
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
--engine-version `17.00.4045.5.cev-dev-ss2025-cu5` ^
--allocated-storage 200 ^
--master-username admin ^
--master-user-password `master_user_password` ^
--license-model bring-your-own-license ^
--vpc-security-group-ids `sg-xxxxxxxxx` ^
--db-subnet-group-name `my-db-subnet-group` ^
--backup-retention-period 7 ^
--region us-west-2
```

###### Note

For Developer Edition (Standard Edition capabilities), use `--engine sqlserver-dev-se` with a `sqlserver-dev-se` CEV version.

Refer to [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating") to create using the AWS console.
