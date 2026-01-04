# Resetting parameters in a DB cluster parameter group in Amazon Aurora

You can reset parameters to their default values in a customer-created DB cluster parameter group. Changes to parameters in a
customer-created DB cluster parameter group are applied to all DB clusters that are associated
with the DB cluster parameter group.

###### Note

In a default DB cluster parameter group, parameters are always set to their default values.

###### To reset parameters in a DB cluster parameter group to their default values

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.
3. In the list, choose the parameter group.
4. For **Parameter group actions**, choose
   **Edit**.
5. Choose the parameters that you want to reset to their default values.
   You can scroll through the parameters using the arrow keys at the top right of the dialog box.

You can't reset values in a default parameter group. 6. Choose **Reset** and then confirm by choosing **Reset parameters**. 7. Reboot the primary DB instance in the DB cluster to apply the changes to
all of the DB instances in the DB cluster.
To reset parameters in a DB cluster parameter group to their default values,
use the AWS CLI [`reset-db-cluster-parameter-group`](../../../cli/latest/reference/rds/reset-db-cluster-parameter-group.md "../../../cli/latest/reference/rds/reset-db-cluster-parameter-group.md") command with the following
required option: `--db-cluster-parameter-group-name`.

To reset all of the parameters in the DB cluster parameter group, specify the `--reset-all-parameters` option.
To reset specific parameters, specify the `--parameters` option.

The following example resets all of the parameters in the DB parameter group named
_mydbparametergroup_ to their default values.

###### Example

For Linux, macOS, or Unix:

```
aws rds reset-db-cluster-parameter-group \
    --db-cluster-parameter-group-name `mydbparametergroup` \
    --reset-all-parameters
```

For Windows:

```
aws rds reset-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name `mydbparametergroup` ^
    --reset-all-parameters
```

The following example resets the `server_audit_logging` and
`server_audit_logs_upload` to their default values in the DB cluster parameter group named
_mydbclusterparametergroup_.

###### Example

For Linux, macOS, or Unix:

```
aws rds reset-db-cluster-parameter-group \
    --db-cluster-parameter-group-name `mydbclusterparametergroup` \
    --parameters "ParameterName=`server_audit_logging`,ApplyMethod=`immediate`" \
                 "ParameterName=`server_audit_logs_upload`,ApplyMethod=`immediate`"
```

For Windows:

```
aws rds reset-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name `mydbclusterparametergroup` ^
    --parameters "ParameterName=`server_audit_logging`,ParameterValue=`1`,ApplyMethod=`immediate`" ^
                 "ParameterName=`server_audit_logs_upload`,ParameterValue=`1`,ApplyMethod=`immediate`"
```

The command produces output like the following:

```
DBClusterParameterGroupName  mydbclusterparametergroup
```

To reset parameters in a DB cluster parameter group to their default values, use the RDS API
[`ResetDBClusterParameterGroup`](../APIReference/API_ResetDBClusterParameterGroup.md "../APIReference/API_ResetDBClusterParameterGroup.md") command with the following
required parameter: `DBClusterParameterGroupName`.

To reset all of the parameters in the DB cluster parameter group, set the `ResetAllParameters` parameter to `true`.
To reset specific parameters, specify the `Parameters` parameter.
