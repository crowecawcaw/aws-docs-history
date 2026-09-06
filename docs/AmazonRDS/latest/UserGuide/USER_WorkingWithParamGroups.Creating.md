

# Creating a DB parameter group in Amazon RDS
<a name="USER_WorkingWithParamGroups.Creating"></a>

You can create a new DB parameter group using the AWS Management Console, the AWS CLI, or the RDS API.

The following limitations apply to the DB parameter group name:
+ The name must be 1 to 255 letters, numbers, or hyphens.

  Default parameter group names can include a period, such as `default.mysql8.0`. However, custom parameter group names can't include a period.
+ The first character must be a letter.
+ The name can't end with a hyphen or contain two consecutive hyphens.

## Console
<a name="USER_WorkingWithParamGroups.Creating.CON"></a>

**To create a DB parameter group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

1. Choose **Create parameter group**.

1. For **Parameter group name**, enter the name of your new DB parameter group.

1. For **Description**, enter a description for your new DB parameter group. 

1. For **Engine type**, choose your DB engine. 

1. For **Parameter group family**, choose a DB parameter group family.

1. For **Type**, if applicable, choose **DB Parameter Group**.

1. Choose **Create**.

## AWS CLI
<a name="USER_WorkingWithParamGroups.Creating.CLI"></a>

To create a DB parameter group, use the AWS CLI [`create-db-parameter-group`](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-parameter-group.html) command. The following example creates a DB parameter group named *mydbparametergroup* for MySQL version 8.0 with a description of "*My new parameter group*."

Include the following required parameters:
+ `--db-parameter-group-name`
+ `--db-parameter-group-family`
+ `--description`

To list all of the available parameter group families, use the following command:

```
aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily"
```

**Note**  
The output contains duplicates.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds create-db-parameter-group \
    --db-parameter-group-name {{mydbparametergroup}} \
    --db-parameter-group-family {{MySQL8.0}} \
    --description {{"My new parameter group"}}
```
For Windows:  

```
aws rds create-db-parameter-group ^
    --db-parameter-group-name {{mydbparametergroup}} ^
    --db-parameter-group-family {{MySQL8.0}} ^
    --description {{"My new parameter group"}}
```
This command produces output similar to the following:  

```
DBPARAMETERGROUP  mydbparametergroup  mysql8.0  My new parameter group
```

## RDS API
<a name="USER_WorkingWithParamGroups.Creating.API"></a>

To create a DB parameter group, use the RDS API [`CreateDBParameterGroup`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBParameterGroup.html) operation.

Include the following required parameters:
+ `DBParameterGroupName`
+ `DBParameterGroupFamily`
+ `Description`