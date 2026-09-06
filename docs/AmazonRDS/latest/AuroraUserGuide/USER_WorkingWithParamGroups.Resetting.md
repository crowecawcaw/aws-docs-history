

# Resetting parameters in a DB parameter group to their default values in Amazon Aurora
<a name="USER_WorkingWithParamGroups.Resetting"></a>

You can reset parameter values in a customer-created DB parameter group to their default values. Changes to parameters in a customer-created DB parameter group are applied to all DB instances that are associated with the DB parameter group.

When you use the console, you can reset specific parameters to their default values. However, you can't easily reset all of the parameters in the DB parameter group at once. When you use the AWS CLI or RDS API, you can reset specific parameters to their default values. You can also reset all of the parameters in the DB parameter group at once.

Changes to some parameters are applied to the DB instance immediately without a reboot. Changes to other parameters are applied only after the DB instance is rebooted. The RDS console shows the status of the DB parameter group associated with a DB instance on the **Configuration** tab. For example, suppose that the DB instance isn't using the latest changes to its associated DB parameter group. If so, the RDS console shows the DB parameter group with a status of **pending-reboot**. To apply the latest parameter changes to that DB instance, manually reboot the DB instance.

![Parameter change pending reboot scenario.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/db-cluster-instance-param-group.png)


**Note**  
In a default DB parameter group, parameters are always set to their default values.

## Console
<a name="USER_WorkingWithParamGroups.Resetting.CON"></a>

**To reset parameters in a DB parameter group to their default values**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

1. In the list, choose the parameter group.

1. For **Parameter group actions**, choose **Edit**.

1. Choose the parameters that you want to reset to their default values. You can scroll through the parameters using the pagination controls. 

   You can't reset values in a default parameter group.

1. Choose **Reset** and then confirm by choosing **Reset parameters**.

## AWS CLI
<a name="USER_WorkingWithParamGroups.Resetting.CLI"></a>

To reset some or all of the parameters in a DB parameter group, use the AWS CLI [`reset-db-parameter-group`](https://docs.aws.amazon.com/cli/latest/reference/rds/reset-db-parameter-group.html) command with the following required option: `--db-parameter-group-name`.

To reset all of the parameters in the DB parameter group, specify the `--reset-all-parameters` option. To reset specific parameters, specify the `--parameters` option.

The following example resets all of the parameters in the DB parameter group named *mydbparametergroup* to their default values.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds reset-db-parameter-group \
    --db-parameter-group-name {{mydbparametergroup}} \
    --reset-all-parameters
```
For Windows:  

```
aws rds reset-db-parameter-group ^
    --db-parameter-group-name {{mydbparametergroup}} ^
    --reset-all-parameters
```

The following example resets the `max_connections` and `max_allowed_packet` options to their default values in the DB parameter group named *mydbparametergroup*.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds reset-db-parameter-group \
    --db-parameter-group-name {{mydbparametergroup}} \
    --parameters "ParameterName={{max_connections}},ApplyMethod={{immediate}}" \
                 "ParameterName={{max_allowed_packet}},ApplyMethod={{immediate}}"
```
For Windows:  

```
aws rds reset-db-parameter-group ^
    --db-parameter-group-name {{mydbparametergroup}} ^
    --parameters "ParameterName={{max_connections}},ApplyMethod={{immediate}}" ^
                 "ParameterName={{max_allowed_packet}},ApplyMethod={{immediate}}"
```
The command produces output like the following:  

```
DBParameterGroupName  mydbparametergroup
```

## RDS API
<a name="USER_WorkingWithParamGroups.Resetting.API"></a>

To reset parameters in a DB parameter group to their default values, use the RDS API [`ResetDBParameterGroup`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ResetDBParameterGroup.html) command with the following required parameter: `DBParameterGroupName`.

To reset all of the parameters in the DB parameter group, set the `ResetAllParameters` parameter to `true`. To reset specific parameters, specify the `Parameters` parameter.