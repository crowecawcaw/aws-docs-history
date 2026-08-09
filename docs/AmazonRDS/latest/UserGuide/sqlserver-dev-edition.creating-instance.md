# Creating an RDS for SQL Server Developer Edition DB instance

Launching Developer Edition instance on RDS for SQL Server follows a two-step process: first create a CEV with `create-custom-db-engine-version`, Once your custom engine version is in the available state, you can create Amazon RDS database instances using the CEV.

**Key differences for Developer Edition instance creation**

| Parameter          | Developer Edition                                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `--engine`         | `sqlserver-dev-ee` (Enterprise Edition capabilities) or `sqlserver-dev-se` (Standard Edition capabilities, SQL Server 2025 only) |
| `--engine-version` | Custom engine version (e.g., `17.00.4045.5.cev-dev-ss2025-cu5`)                                                                  |
| `--license-model`  | bring-your-own-license                                                                                                           |

To create a SQL Server Developer Edition DB instance using the AWS AWS Management Console:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") and open the Amazon RDS console.
2. In the navigation pane, choose **Databases**, then choose **Create database**.
3. For **Choose a database creation method**, choose **Full configuration**.
4. For **Engine options**, choose **Microsoft SQL Server**.
5. For **Edition**, choose one of the following:

   - **SQL Server Developer Edition** – Provides Enterprise Edition capabilities. Corresponds to the `sqlserver-dev-ee` engine.
   - **SQL Server Standard Developer Edition** – Provides Standard Edition capabilities. Corresponds to the `sqlserver-dev-se` engine. Available for SQL Server 2025 only.

6. For **License model**, note that when you choose a Developer Edition, the console automatically selects **License: Not applicable**. You cannot change this value.
7. For **Custom engine version**, choose the CEV that you created (for example, `17.00.4045.5.cev-dev-ss2025-cu5`).

###### Note

Only CEVs in the `available` state appear in the list. If your CEV is not listed, verify its status. For more information, see [Creating a custom engine version for RDS for SQL Server](sqlserver-dev-edition.creating-cev.md "sqlserver-dev-edition.creating-cev.md"). 8. For **DB instance identifier**, enter a unique name for your DB instance. 9. Configure **DB instance class**, **Storage**, **Connectivity**, **Database authentication**, and other settings as needed. For more information, see [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating"). 10. Choose **Create database**.
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
