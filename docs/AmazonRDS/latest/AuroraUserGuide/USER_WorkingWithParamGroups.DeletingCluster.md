

# Deleting a DB cluster parameter groupin Amazon Aurora
<a name="USER_WorkingWithParamGroups.DeletingCluster"></a>

You can delete a DB cluster parameter group using the AWS Management Console, AWS CLI, or RDS API. A DB cluster parameter group parameter group is eligible for deletion only if it isn't associated with a DB cluster.

## Console
<a name="USER_WorkingWithParamGroups.DeletingCluster.CON"></a>

**To delete parameter groups**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

   The parameter groups appear in a list.

1. Choose the name of the DB cluster parameter groups to be deleted.

1. Choose **Actions** and then **Delete**.

1. Review the parameter group names and then choose **Delete**.

## AWS CLI
<a name="USER_WorkingWithParamGroups.DeletingCluster.CLI"></a>

To delete a DB cluster parameter group, use the AWS CLI [`delete-db-cluster-parameter-group`](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-cluster-parameter-group.html) command with the following required parameter.
+ `--db-parameter-group-name`

**Example**  
The following example deletes a DB cluster parameter group named *mydbparametergroup.*  

```
aws rds delete-db-cluster-parameter-group --db-parameter-group-name {{mydbparametergroup}}
```

## RDS API
<a name="USER_WorkingWithParamGroups.DeletingCluster.API"></a>

To delete a DB cluster parameter group, use the RDS API [`DeleteDBClusterParameterGroup`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterParameterGroup.html) command with the following required parameter.
+ `DBParameterGroupName`