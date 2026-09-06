

# Viewing and managing custom engine versions
<a name="sqlserver-dev-edition.managing"></a>

To view all your RDS for SQL Server Developer Edition CEVs, use the `describe-db-engine-versions` command with `--engine sqlserver-dev-ee` for Enterprise Edition capabilities, or `--engine sqlserver-dev-se` for Standard Edition capabilities (SQL Server 2025 only).

```
# Developer Edition (Enterprise Edition capabilities)
aws rds describe-db-engine-versions \
--engine sqlserver-dev-ee \
--include-all \
--region us-west-2

# Developer Edition (Standard Edition capabilities, SQL Server 2025 only)
aws rds describe-db-engine-versions \
--engine sqlserver-dev-se \
--include-all \
--region us-west-2
```

To view the details of a specific CEV, use the following command:

```
aws rds describe-db-engine-versions \
--engine sqlserver-dev-ee \
--engine-version {{17.00.4045.5.my-dev-cev}} \
--region us-west-2
```

**Note**  
This command only returns CEVs with an `available` status. To view CEVs in validating or other states, include the `--include-all` flag. Replace `sqlserver-dev-ee` with `sqlserver-dev-se` when viewing Standard Edition capabilities CEVs.

## Deleting custom engine versions
<a name="sqlserver-dev-deleting-cevs"></a>

Before deleting a CEV, make sure it isn't being used by any of the following:
+ An Amazon RDS DB instance
+ A snapshot of an Amazon RDS DB instance
+ An automated backup of an Amazon RDS DB instance

**Note**  
You can't delete a CEV if there are any resources associated with it.

To delete a custom engine version, use the [ delete-custom-db-engine-version](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-custom-db-engine-version.html) command.
+ `--engine`: Specify `sqlserver-dev-ee` (Enterprise Edition capabilities) or `sqlserver-dev-se` (Standard Edition capabilities, SQL Server 2025 only)
+ `--engine-version`: The exact CEV version identifier to delete
+ `--region`: AWS Region where the CEV exists

```
aws rds delete-custom-db-engine-version \
--engine sqlserver-dev-ee \
--engine-version {{17.00.4045.5.my-dev-cev}} \
--region us-west-2
```

To monitor the CEV deletion process, use the `describe-db-engine-versions` command and specify your RDS for SQL Server CEV engine version

```
aws rds describe-db-engine-versions \
--engine sqlserver-dev-ee \
--engine-version {{17.00.4045.5.my-dev-cev}} \
--region us-west-2
```

Status Values:
+ `deleting`: CEV deletion in progress
+ No results returned: CEV successfully deleted