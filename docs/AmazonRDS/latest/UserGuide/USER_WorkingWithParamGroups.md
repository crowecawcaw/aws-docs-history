# Copying a DB parameter group in Amazon RDS

You can copy custom DB parameter groups that you create. Copying a parameter group can be
convenient solution. An example is when you have created a DB parameter group and want to include
most of its custom parameters and values in a new DB parameter group. You can copy a
DB parameter group by using the AWS Management Console. You can also use the AWS CLI [copy-db-parameter-group](../../../cli/latest/reference/rds/copy-db-parameter-group.md "../../../cli/latest/reference/rds/copy-db-parameter-group.md")
command or the RDS API [CopyDBParameterGroup](../APIReference/API_CopyDBParameterGroup.md "../APIReference/API_CopyDBParameterGroup.md") operation.

After you copy a DB parameter group, wait at least 5 minutes before creating your first DB instance that
uses that DB parameter group as the default parameter group. Doing this allows Amazon RDS to fully
complete the copy action before the parameter group is used. This is especially
important for parameters that are critical when creating the default database for a
DB instance. An example is the character set for the default database defined by the
`character_set_database` parameter. Use the **Parameter
Groups** option of the [Amazon RDS
console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") or the [describe-db-parameters](../../../cli/latest/reference/rds/describe-db-parameters.md "../../../cli/latest/reference/rds/describe-db-parameters.md") command to verify that your DB parameter group is created.

###### Note

You can't copy a default parameter group. However, you can create a new parameter
group that is based on a default parameter group.

You can't copy a DB parameter group to a different AWS account or AWS Region.

###### To copy a DB parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.
3. In the list, choose the custom parameter group that you want to
   copy.
4. For **Parameter group actions**, choose
   **Copy**.
5. In **New DB parameter group identifier**, enter a name for the new
   parameter group.
6. In **Description**, enter a description for the new
   parameter group.
7. Choose **Copy**.
   To copy a DB parameter group, use the AWS CLI [`copy-db-parameter-group`](../../../cli/latest/reference/rds/copy-db-parameter-group.md "../../../cli/latest/reference/rds/copy-db-parameter-group.md") command with the following
   required options:

- `--source-db-parameter-group-identifier`
- `--target-db-parameter-group-identifier`
- `--target-db-parameter-group-description`
  The following example creates a new DB parameter group named `mygroup2` that is
  a copy of the DB parameter group `mygroup1`.

###### Example

For Linux, macOS, or Unix:

```
aws rds copy-db-parameter-group \
    --source-db-parameter-group-identifier `mygroup1` \
    --target-db-parameter-group-identifier `mygroup2` \
    --target-db-parameter-group-description `"DB parameter group 2"`
```

For Windows:

```
aws rds copy-db-parameter-group ^
    --source-db-parameter-group-identifier `mygroup1` ^
    --target-db-parameter-group-identifier `mygroup2` ^
    --target-db-parameter-group-description `"DB parameter group 2"`
```

To copy a DB parameter group, use the RDS API [`CopyDBParameterGroup`](../APIReference/API_CopyDBParameterGroup.md "../APIReference/API_CopyDBParameterGroup.md") operation with the following
required parameters:

- `SourceDBParameterGroupIdentifier`
- `TargetDBParameterGroupIdentifier`
- `TargetDBParameterGroupDescription`
