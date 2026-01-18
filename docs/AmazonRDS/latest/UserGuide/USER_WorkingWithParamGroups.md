# Deleting a DB parameter group in

Amazon RDS

You can delete a DB parameter group using the AWS Management Console, AWS CLI, or RDS API. A parameter group is
eligible for deletion only if it isn't associated with a DB instance.

###### To delete a DB parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.

The DB parameter groups appear in a list. 3. Choose the name of the parameter groups to be deleted. 4. Choose **Actions** and then
**Delete**. 5. Review the parameter group names and then choose
**Delete**.
To delete a DB parameter group, use the AWS CLI [`delete-db-parameter-group`](../../../cli/latest/reference/rds/delete-db-parameter-group.md "../../../cli/latest/reference/rds/delete-db-parameter-group.md") command with the
following required parameter.

- `--db-parameter-group-name`

###### Example

The following example deletes a DB parameter group named
_mydbparametergroup._

```
aws rds delete-db-parameter-group --db-parameter-group-name `mydbparametergroup`
```

To delete a DB parameter group, use the RDS API [`DeleteDBParameterGroup`](../APIReference/API_DeleteDBParameterGroup.md "../APIReference/API_DeleteDBParameterGroup.md") command with the following
required parameter.

- `DBParameterGroupName`
