

# Creating a DB cluster parameter groupin Amazon Aurora
<a name="USER_WorkingWithParamGroups.CreatingCluster"></a>

You can create a new DB cluster parameter group using the AWS Management Console, the AWS CLI, or the RDS API.

After you create a DB cluster parameter group, wait at least 5 minutes before creating a DB cluster that uses that DB cluster parameter group. Doing this allows Amazon RDS to fully create the parameter group before it is used by the new DB cluster. You can use the **Parameter groups** page in the [Amazon RDS console](https://console.aws.amazon.com/rds/) or the [describe-db-cluster-parameters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html) command to verify that your DB cluster parameter group is created.

The following limitations apply to the DB cluster parameter group name:
+ The name must be 1 to 255 letters, numbers, or hyphens.

  Default parameter group names can include a period, such as `default.aurora-mysql5.7`. However, custom parameter group names can't include a period.
+ The first character must be a letter.
+ The name can't end with a hyphen or contain two consecutive hyphens.

## Console
<a name="USER_WorkingWithParamGroups.CreatingCluster.CON"></a>

**To create a DB cluster parameter group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

1. Choose **Create parameter group**.

1. For **Parameter group name**, enter the name of the new DB cluster parameter group.

1. For **Description**, enter a description for the new DB cluster parameter group.

1. For **Engine type**, choose your database engine.

1. For **Parameter group family**, choose a DB parameter group family.

1. Choose **Create**.

## AWS CLI
<a name="USER_WorkingWithParamGroups.CreatingCluster.CLI"></a>

To create a DB cluster parameter group, use the AWS CLI [`create-db-cluster-parameter-group`](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster-parameter-group.html) command.

The following example creates a DB cluster parameter group named *mydbclusterparametergroup* for Aurora MySQL version 5.7 with a description of "*My new cluster parameter group*."

Include the following required parameters:
+ `--db-cluster-parameter-group-name`
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
aws rds create-db-cluster-parameter-group \
    --db-cluster-parameter-group-name {{mydbclusterparametergroup}} \
    --db-parameter-group-family {{aurora-mysql5.7}} \
    --description {{"My new cluster parameter group"}}
```
For Windows:  

```
aws rds create-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name {{mydbclusterparametergroup}} ^
    --db-parameter-group-family {{aurora-mysql5.7}} ^
    --description {{"My new cluster parameter group"}}
```
This command produces output similar to the following:  

```
{
    "DBClusterParameterGroup": {
        "DBClusterParameterGroupName": "mydbclusterparametergroup",
        "DBParameterGroupFamily": "aurora-mysql5.7",
        "Description": "My new cluster parameter group",
        "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:mydbclusterparametergroup"
    }
}
```

## RDS API
<a name="USER_WorkingWithParamGroups.CreatingCluster.API"></a>

To create a DB cluster parameter group, use the RDS API [`CreateDBClusterParameterGroup`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBClusterParameterGroup.html) action.

Include the following required parameters:
+ `DBClusterParameterGroupName`
+ `DBParameterGroupFamily`
+ `Description`