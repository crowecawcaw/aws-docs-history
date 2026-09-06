

# Resetting parameters in a DB cluster parameter group
<a name="USER_WorkingWithParamGroups.ResettingCluster"></a>

You can reset parameters to their default values in a customer-created DB cluster parameter group. Changes to parameters in a customer-created DB cluster parameter group are applied to all DB clusters that are associated with the DB cluster parameter group.

**Note**  
In a default DB cluster parameter group, parameters are always set to their default values.

## Console
<a name="USER_WorkingWithParamGroups.ResettingCluster.CON"></a>

**To reset parameters in a DB cluster parameter group to their default values**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

1. In the list, choose the parameter group.

1. For **Parameter group actions**, choose **Edit**.

1. Choose the parameters that you want to reset to their default values. You can scroll through the parameters using the pagination controls. 

   You can't reset values in a default parameter group.

1. Choose **Reset** and then confirm by choosing **Reset parameters**.

1. Reboot the DB cluster.

## AWS CLI
<a name="USER_WorkingWithParamGroups.ResettingCluster.CLI"></a>

To reset parameters in a DB cluster parameter group to their default values, use the AWS CLI [`reset-db-cluster-parameter-group`](https://docs.aws.amazon.com/cli/latest/reference/rds/reset-db-cluster-parameter-group.html) command with the following required option: `--db-cluster-parameter-group-name`.

To reset all of the parameters in the DB cluster parameter group, specify the `--reset-all-parameters` option. To reset specific parameters, specify the `--parameters` option.

The following example resets all of the parameters in the DB parameter group named *mydbparametergroup* to their default values.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds reset-db-cluster-parameter-group \
    --db-cluster-parameter-group-name {{mydbparametergroup}} \
    --reset-all-parameters
```
For Windows:  

```
aws rds reset-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name {{mydbparametergroup}} ^
    --reset-all-parameters
```

The following example resets the `server_audit_logging` and `server_audit_logs_upload` to their default values in the DB cluster parameter group named *mydbclusterparametergroup*.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds reset-db-cluster-parameter-group \
    --db-cluster-parameter-group-name {{mydbclusterparametergroup}} \
    --parameters "ParameterName={{server_audit_logging}},ApplyMethod={{immediate}}" \
                 "ParameterName={{server_audit_logs_upload}},ApplyMethod={{immediate}}"
```
For Windows:  

```
aws rds reset-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name {{mydbclusterparametergroup}} ^
    --parameters "ParameterName={{server_audit_logging}},ParameterValue={{1}},ApplyMethod={{immediate}}" ^
                 "ParameterName={{server_audit_logs_upload}},ParameterValue={{1}},ApplyMethod={{immediate}}"
```
The command produces output like the following:  

```
DBClusterParameterGroupName  mydbclusterparametergroup
```

## RDS API
<a name="USER_WorkingWithParamGroups.ResettingCluster.API"></a>

To reset parameters in a DB cluster parameter group to their default values, use the RDS API [`ResetDBClusterParameterGroup`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ResetDBClusterParameterGroup.html) command with the following required parameter: `DBClusterParameterGroupName`.

To reset all of the parameters in the DB cluster parameter group, set the `ResetAllParameters` parameter to `true`. To reset specific parameters, specify the `Parameters` parameter.