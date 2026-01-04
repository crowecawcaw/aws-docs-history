# Creating a DB cluster parameter group

You can create a new DB cluster parameter group using the AWS Management Console, the AWS CLI, or the RDS API.

After you create a DB cluster parameter group, wait at least 5 minutes
before creating a DB cluster that uses that DB cluster parameter group.
Doing this allows Amazon RDS to fully create the parameter group before it
is used by the new DB cluster. You can use the **Parameter groups** page
in the [Amazon RDS console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") or the
[describe-db-cluster-parameters](../../../cli/latest/reference/rds/describe-db-cluster-parameters.md "../../../cli/latest/reference/rds/describe-db-cluster-parameters.md")
command to verify that your DB cluster parameter group is created.

The following limitations apply to the DB cluster parameter group name:

- The name must be 1 to 255 letters, numbers, or hyphens.

Default parameter group names can include a period, such as
`default.mysql5.7`. However, custom parameter group
names can't include a period.

- The first character must be a letter.
- The name can't end with a hyphen or contain two consecutive hyphens.

###### To create a DB cluster parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.
3. Choose **Create parameter group**.
4. For **Parameter group name**, enter the name of the new
   DB cluster parameter group.
5. For **Description**, enter a description for the new DB cluster parameter group.
6. For **Engine type**, choose your database engine.
7. For **Parameter group family**, choose a DB parameter group family.
8. Choose **Create**.
   To create a DB cluster parameter group, use the AWS CLI [`create-db-cluster-parameter-group`](../../../cli/latest/reference/rds/create-db-cluster-parameter-group.md "../../../cli/latest/reference/rds/create-db-cluster-parameter-group.md") command.

The following example creates a DB cluster parameter group named _mydbclusterparametergroup_
for RDS for MySQL version 8.0 with a description of "_My new cluster parameter group_."

Include the following required parameters:

- `--db-cluster-parameter-group-name`
- `--db-parameter-group-family`
- `--description`
  To list all of the available parameter group families, use the following command:

```
aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily"
```

###### Note

The output contains duplicates.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-db-cluster-parameter-group \
    --db-cluster-parameter-group-name `mydbclusterparametergroup` \
    --db-parameter-group-family `mysql8.0` \
    --description `"My new cluster parameter group"`
```

For Windows:

```
aws rds create-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name `mydbclusterparametergroup` ^
    --db-parameter-group-family `mysql8.0` ^
    --description `"My new cluster parameter group"`
```

This command produces output similar to the following:

```
{
    "DBClusterParameterGroup": {
        "DBClusterParameterGroupName": "mydbclusterparametergroup",
        "DBParameterGroupFamily": "mysql8.0",
        "Description": "My new cluster parameter group",
        "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:mydbclusterparametergroup2"
    }
}
```

To create a DB cluster parameter group, use the RDS API [`CreateDBClusterParameterGroup`](../APIReference/API_CreateDBClusterParameterGroup.md "../APIReference/API_CreateDBClusterParameterGroup.md") action.

Include the following required parameters:

- `DBClusterParameterGroupName`
- `DBParameterGroupFamily`
- `Description`
