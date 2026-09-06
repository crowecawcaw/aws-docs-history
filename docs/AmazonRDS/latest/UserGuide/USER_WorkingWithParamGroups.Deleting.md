

# Deleting a DB parameter group in Amazon RDS
<a name="USER_WorkingWithParamGroups.Deleting"></a>

You can delete a DB parameter group using the AWS Management Console, AWS CLI, or RDS API. A parameter group is eligible for deletion only if it isn't associated with a DB instance.

## Console
<a name="USER_WorkingWithParamGroups.Deleting.CON"></a>

**To delete a DB parameter group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

   The DB parameter groups appear in a list.

1. Choose the name of the parameter groups to be deleted.

1. Choose **Actions** and then **Delete**.

1. Review the parameter group names and then choose **Delete**.

## AWS CLI
<a name="USER_WorkingWithParamGroups.Deleting.CLI"></a>

To delete a DB parameter group, use the AWS CLI [`delete-db-parameter-group`](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-parameter-group.html) command with the following required parameter.
+ `--db-parameter-group-name`

**Example**  
The following example deletes a DB parameter group named *mydbparametergroup.*  

```
aws rds delete-db-parameter-group --db-parameter-group-name {{mydbparametergroup}}
```

## RDS API
<a name="USER_WorkingWithParamGroups.Deleting.API"></a>

To delete a DB parameter group, use the RDS API [`DeleteDBParameterGroup`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBParameterGroup.html) command with the following required parameter.
+ `DBParameterGroupName`