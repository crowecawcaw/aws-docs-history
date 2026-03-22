# Deleting a DB cluster parameter group

You can delete a DB cluster parameter group using the AWS Management Console, AWS CLI, or RDS API. A DB cluster parameter group parameter group
is eligible for deletion only if it isn't associated with a DB cluster.

###### To delete parameter groups

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.

The parameter groups appear in a list. 3. Choose the name of the DB cluster parameter groups to be deleted. 4. Choose **Actions** and then
**Delete**. 5. Review the parameter group names and then choose
**Delete**.
To delete a DB cluster parameter group, use the AWS CLI [`delete-db-cluster-parameter-group`](../../../cli/latest/reference/rds/delete-db-cluster-parameter-group.md "../../../cli/latest/reference/rds/delete-db-cluster-parameter-group.md") command with the
following required parameter.

- `--db-parameter-group-name`

###### Example

The following example deletes a DB cluster parameter group named
_mydbparametergroup._

```
aws rds delete-db-cluster-parameter-group --db-parameter-group-name `mydbparametergroup`
```

To delete a DB cluster parameter group, use the RDS API [`DeleteDBClusterParameterGroup`](../APIReference/API_DeleteDBClusterParameterGroup.md "../APIReference/API_DeleteDBClusterParameterGroup.md") command with the
following required parameter.

- `DBParameterGroupName`
