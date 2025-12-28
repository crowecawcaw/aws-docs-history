# Copying a DB cluster parameter group

You can copy custom DB cluster parameter groups that you create. Copying a parameter group is a convenient
solution when you have already created a DB cluster parameter group and you want to include most of the custom
parameters and values from that group in a new DB cluster parameter group. You can copy a DB cluster parameter group by
using the AWS CLI [copy-db-cluster-parameter-group](../../../cli/latest/reference/rds/copy-db-cluster-parameter-group.md "../../../cli/latest/reference/rds/copy-db-cluster-parameter-group.md") command or the RDS API
[CopyDBClusterParameterGroup](../APIReference/API_CopyDBParameterGroup.md "../APIReference/API_CopyDBParameterGroup.md") operation.

After you copy a DB cluster parameter group, wait at least 5 minutes
before creating a DB cluster that uses that DB cluster parameter group.
Doing this allows Amazon RDS to fully copy the parameter group before it
is used by the new DB cluster. You can use the **Parameter groups** page
in the [Amazon RDS console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") or the
[describe-db-cluster-parameters](../../../cli/latest/reference/rds/describe-db-cluster-parameters.md "../../../cli/latest/reference/rds/describe-db-cluster-parameters.md")
command to verify that your DB cluster parameter group is created.

###### Note

You can't copy a default parameter group. However, you can create a new parameter group that is based on a default
parameter group.

You can't copy a DB cluster parameter group to a different AWS account or AWS Region.

###### To copy a DB cluster parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.
3. In the list, choose the custom parameter group that you want to copy.
4. For **Parameter group actions**, choose
   **Copy**.
5. In **New DB parameter group identifier**, enter a name for the new
   parameter group.
6. In **Description**, enter a description for the new parameter
   group.
7. Choose **Copy**.
   To copy a DB cluster parameter group, use the AWS CLI [`copy-db-cluster-parameter-group`](../../../cli/latest/reference/rds/copy-db-cluster-parameter-group.md "../../../cli/latest/reference/rds/copy-db-cluster-parameter-group.md") command with the following required parameters:

- `--source-db-cluster-parameter-group-identifier`
- `--target-db-cluster-parameter-group-identifier`
- `--target-db-cluster-parameter-group-description`
  The following example creates a new DB cluster parameter group named `mygroup2`
  that is a copy of the DB cluster parameter group `mygroup1`.

###### Example

For Linux, macOS, or Unix:

```
aws rds copy-db-cluster-parameter-group \
    --source-db-cluster-parameter-group-identifier `mygroup1` \
    --target-db-cluster-parameter-group-identifier `mygroup2` \
    --target-db-cluster-parameter-group-description `"DB parameter group 2"`
```

For Windows:

```
aws rds copy-db-cluster-parameter-group ^
    --source-db-cluster-parameter-group-identifier `mygroup1` ^
    --target-db-cluster-parameter-group-identifier `mygroup2` ^
    --target-db-cluster-parameter-group-description `"DB parameter group 2"`
```

To copy a DB cluster parameter group, use the RDS API [`CopyDBClusterParameterGroup`](../APIReference/API_CopyDBClusterParameterGroup.md "../APIReference/API_CopyDBClusterParameterGroup.md")
operation with the following required parameters:

- `SourceDBClusterParameterGroupIdentifier`
- `TargetDBClusterParameterGroupIdentifier`
- `TargetDBClusterParameterGroupDescription`
