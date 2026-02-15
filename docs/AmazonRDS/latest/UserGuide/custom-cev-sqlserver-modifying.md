# Modifying a CEV for RDS Custom for SQL Server

You can modify a CEV using the AWS Management Console or the AWS CLI. You can modify the CEV description or its availability status. Your CEV
has one of the following status values:

- `available` – You can use this CEV to create a new RDS Custom DB
  instance or upgrade a DB instance. This is the default status for a newly created
  CEV.
- `inactive` – You can't create or upgrade an RDS Custom DB
  instance with this CEV. You can't restore a DB snapshot to create a new RDS Custom DB
  instance with this CEV.
  You can change the CEV status from `available` to `inactive` or from
  `inactive` to `available`. You might change the status to
  `INACTIVE` to prevent the accidental use of a CEV or to make a discontinued
  CEV eligible for use again.

###### To modify a CEV

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Custom engine versions**.
3. Choose a CEV whose description or status you want to modify.
4. For **Actions**, choose
   **Modify**.
5. Make any of the following changes:
   - For **CEV status settings**, choose a new
     availability status.
   - For **Version description**, enter a new
     description.

6. Choose **Modify CEV**.

If the CEV is in use, the console displays **You can't modify
the CEV status**. Fix the problems, then try again.
The **Custom engine versions** page appears.

To modify a CEV by using the AWS CLI, run the [modify-custom-db-engine-version](../../../cli/latest/reference/rds/modify-custom-db-engine-version.md "../../../cli/latest/reference/rds/modify-custom-db-engine-version.md") command. You can find CEVs to modify by running the [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") command.

The following options are required:

- `--engine`
- `--engine-version
  `cev```, where
`cev`` is the name of the
  custom engine version that you want to modify
- `--status````status```, where
 ``status`` is the
 availability status that you want to assign to the CEV
The following example changes a CEV named `15.00.4249.2.my_cevtest`from its current status to
`inactive`.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-custom-db-engine-version \
    --engine custom-sqlserver-ee \
    --engine-version `15.00.4249.2.my_cevtest` \
    --status inactive
```

For Windows:

```
aws rds modify-custom-db-engine-version ^
    --engine custom-sqlserver-ee ^
    --engine-version `15.00.4249.2.my_cevtest` ^
    --status inactive
```

To modify an RDS Custom for SQL Server DB instance to use a new CEV, see [Modifying an RDS Custom for SQL Server DB instance to use a new CEV](custom-cev-sqlserver-modifying-dbinstance.md "custom-cev-sqlserver-modifying-dbinstance.md").
