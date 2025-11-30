# Creating a DB parameter group in Amazon RDS

You can create a new DB parameter group using the AWS Management Console, the AWS CLI, or the RDS API.

The following limitations apply to the DB parameter group name:

- The name must be 1 to 255 letters, numbers, or hyphens.

Default parameter group names can include a period, such as
`default.mysql8.0`. However, custom parameter group names can't
include a period.

- The first character must be a letter.
- The name can't end with a hyphen or contain two consecutive hyphens.

###### To create a DB parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.
3. Choose **Create parameter group**.
4. For **Parameter group name**, enter the name of your
   new DB parameter group.
5. For **Description**, enter a description for your new
   DB parameter group.
6. For **Engine type**, choose your DB engine.
7. For **Parameter group family**, choose a DB parameter group
   family.
8. For **Type**, if applicable, choose **DB
   Parameter Group**.
9. Choose **Create**.
   To create a DB parameter group, use the AWS CLI [`create-db-parameter-group`](../../../cli/latest/reference/rds/create-db-parameter-group.md "../../../cli/latest/reference/rds/create-db-parameter-group.md") command. The following
   example creates a DB parameter group named _mydbparametergroup_ for MySQL
   version 8.0 with a description of "_My new parameter
   group_."

Include the following required parameters:

- `--db-parameter-group-name`
- `--db-parameter-group-family`
- `--description`
  To list all of the available parameter group families, use the following
  command:

```
aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily"
```

###### Note

The output contains duplicates.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
    --db-parameter-group-name `mydbparametergroup` \
    --db-parameter-group-family `MySQL8.0` \
    --description `"My new parameter group"`
```

For Windows:

```
aws rds create-db-parameter-group ^
    --db-parameter-group-name `mydbparametergroup` ^
    --db-parameter-group-family `MySQL8.0` ^
    --description `"My new parameter group"`
```

This command produces output similar to the following:

```
DBPARAMETERGROUP  mydbparametergroup  mysql8.0  My new parameter group
```

To create a DB parameter group, use the RDS API [`CreateDBParameterGroup`](../APIReference/API_CreateDBParameterGroup.md "../APIReference/API_CreateDBParameterGroup.md") operation.

Include the following required parameters:

- `DBParameterGroupName`
- `DBParameterGroupFamily`
- `Description`
