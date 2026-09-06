

# Modifying parameters in a DB cluster parameter groupin Amazon Aurora
<a name="USER_WorkingWithParamGroups.ModifyingCluster"></a>

You can modify parameter values in a customer-created DB cluster parameter group. You can't change the parameter values in a default DB cluster parameter group. Changes to parameters in a customer-created DB cluster parameter group are applied to all DB clusters that are associated with the DB cluster parameter group.

## Console
<a name="USER_WorkingWithParamGroups.ModifyingCluster.CON"></a>

**To modify a DB cluster parameter group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

1. In the list, choose the parameter group that you want to modify.

1. For **Parameter group actions**, choose **Edit**.

1. Change the values of the parameters you want to modify. You can scroll through the parameters using the pagination controls. 

   You can't change values in a default parameter group.

1. Choose **Save changes**.

1. Reboot the primary (writer) DB instance in the cluster to apply the changes to it.

1. Then reboot the reader DB instances to apply the changes to them. 

   If you don't reboot the DB instances, then a failover operation could take longer than normal.

## AWS CLI
<a name="USER_WorkingWithParamGroups.ModifyingCluster.CLI"></a>

To modify a DB cluster parameter group, use the AWS CLI [`modify-db-cluster-parameter-group`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster-parameter-group.html) command with the following required parameters:
+ `--db-cluster-parameter-group-name`
+ `--parameters`

The following example modifies the `server_audit_logging` and `server_audit_logs_upload` values in the DB cluster parameter group named *mydbclusterparametergroup*.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-cluster-parameter-group \
    --db-cluster-parameter-group-name {{mydbclusterparametergroup}} \
    --parameters "ParameterName={{server_audit_logging}},ParameterValue={{1}},ApplyMethod={{immediate}}" \
                 "ParameterName={{server_audit_logs_upload}},ParameterValue={{1}},ApplyMethod={{immediate}}"
```
For Windows:  

```
aws rds modify-db-cluster-parameter-group ^
    --db-cluster-parameter-group-name {{mydbclusterparametergroup}} ^
    --parameters "ParameterName={{server_audit_logging}},ParameterValue={{1}},ApplyMethod={{immediate}}" ^
                 "ParameterName={{server_audit_logs_upload}},ParameterValue={{1}},ApplyMethod={{immediate}}"
```
The command produces output like the following:  

```
DBCLUSTERPARAMETERGROUP  mydbclusterparametergroup
```

## RDS API
<a name="USER_WorkingWithParamGroups.ModifyingCluster.API"></a>

To modify a DB cluster parameter group, use the RDS API [`ModifyDBClusterParameterGroup`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterParameterGroup.html) command with the following required parameters:
+ `DBClusterParameterGroupName`
+ `Parameters`