# Modifying parameters in a DB cluster parameter group

You can modify parameter values in a customer-created DB cluster parameter group. You can't change
the parameter values in a default DB cluster parameter group. Changes to parameters in a
customer-created DB cluster parameter group are applied to all DB clusters that are associated
with the DB cluster parameter group.

###### To modify a DB cluster parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.
3. In the list, choose the parameter group that you want to modify.
4. For **Parameter group actions**, choose
   **Edit**.
5. Change the values of the parameters you want to modify. You can scroll through the
   parameters using the arrow keys at the top right of the dialog box.

You can't change values in a default parameter group. 6. Choose **Save changes**. 7. Reboot the cluster to apply
the changes to it.

If you don't reboot the cluster, then a failover operation
could take longer than normal.
To modify a DB cluster parameter group, use the AWS CLI [`modify-db-cluster-parameter-group`](../../../cli/latest/reference/rds/modify-db-cluster-parameter-group.md "../../../cli/latest/reference/rds/modify-db-cluster-parameter-group.md") command with the following
required parameters:

- `--db-cluster-parameter-group-name`
- `--parameters`
  The following example modifies the `server_audit_logging` and
  `server_audit_logs_upload` values in the DB cluster parameter group named
  _mydbclusterparametergroup_.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-parameter-group \
    --db-cluster-parameter-group-name `mydbclusterparametergroup` \
    --parameters "ParameterName=`server_audit_logging`,ParameterValue=`1`,ApplyMethod=`immediate`" \
                 "ParameterName=`server_audit_logs_upload`,ParameterValue=`1`,ApplyMethod=`immediate`"
```

For Windows:

```
aws rds modify-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name `mydbclusterparametergroup` ^
    --parameters "ParameterName=`server_audit_logging`,ParameterValue=`1`,ApplyMethod=`immediate`" ^
                 "ParameterName=`server_audit_logs_upload`,ParameterValue=`1`,ApplyMethod=`immediate`"
```

The command produces output like the following:

```
DBCLUSTERPARAMETERGROUP  mydbclusterparametergroup
```

To modify a DB cluster parameter group, use the RDS API [`ModifyDBClusterParameterGroup`](../APIReference/API_ModifyDBClusterParameterGroup.md "../APIReference/API_ModifyDBClusterParameterGroup.md") command with the following
required parameters:

- `DBClusterParameterGroupName`
- `Parameters`
