# Viewing and managing custom engine versions

To view all your RDS for SQL Server Developer Edition CEVs, use the `describe-db-engine-versions`
command with the `--engine` input as `sqlserver-dev-ee`.

```
aws rds describe-db-engine-versions \
--engine sqlserver-dev-ee \
--include-all \
--region us-west-2
```

To view the details of a specific CEV, use the following command:

```

aws rds describe-db-engine-versions \
--engine sqlserver-dev-ee \
--engine-version `16.00.4215.2.cev-dev-ss2022-cu21` \
--region us-west-2
```

###### Note

This command only returns CEVs with an `available` status. To view CEVs in validating or other states, include the `--include-all` flag.

## Deleting custom engine versions

Before deleting a CEV, make sure it isn't being used by any of the following:

- An Amazon RDS DB instance
- A snapshot of an Amazon RDS DB instance
- An automated backup of an Amazon RDS DB instance

###### Note

You can't delete a CEV if there are any resources associated with it.

To delete a custom engine version, use the [delete-custom-db-engine-version](../../../cli/latest/reference/rds/delete-custom-db-engine-version.md "../../../cli/latest/reference/rds/delete-custom-db-engine-version.md") command.

- `--engine`: Specify `sqlserver-dev-ee` for Developer Edition
- `--engine-version`: The exact CEV version identifier to delete
- `--region`: AWS Region where the CEV exists

```
aws rds delete-custom-db-engine-version \
--engine sqlserver-dev-ee \
--engine-version `16.00.4215.2.my-dev-cev` \
--region us-west-2
```

To monitor the CEV deletion process, use the `describe-db-engine-versions` command
and specify your RDS for SQL Server CEV engine version

```
aws rds describe-db-engine-versions \
--engine sqlserver-dev-ee \
--engine-version `16.00.4215.2.my-dev-cev` \
--region us-west-2
```

Status Values:

- `deleting`: CEV deletion in progress
- No results returned: CEV successfully deleted
