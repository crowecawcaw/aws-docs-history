

# Modifying parameters in a DB parameter group in Amazon Aurora
<a name="USER_WorkingWithParamGroups.Modifying"></a>

You can modify parameter values in a customer-created DB parameter group; you can't change the parameter values in a default DB parameter group. Changes to parameters in a customer-created DB parameter group are applied to all DB instances that are associated with the DB parameter group. 

There are two types of parameters: dynamic parameters and static parameters. Changes to dynamic parameters are applied to the DB instance immediately without a reboot. Changes to static parameters are applied only after the DB instance is rebooted.

The RDS console shows the status of the DB parameter group associated with a DB instance on the **Configuration** tab. For example, if the DB instance isn't using the latest changes to its associated DB parameter group, the RDS console shows the DB parameter group with a status of **pending-reboot**. To apply the latest parameter changes to that DB instance, manually reboot the DB instance.

![Parameter change pending reboot scenario.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/db-cluster-instance-param-group.png)


## Console
<a name="USER_WorkingWithParamGroups.Modifying.CON"></a>

**To modify the parameters in a DB parameter group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

1. In the list, choose the name of the parameter group that you want to modify.

1. For **Parameter group actions**, choose **Edit**.

1. Change the values of the parameters that you want to modify. You can scroll through the parameters using the pagination controls. 

   You can't change values in a default parameter group.

1. Choose **Save changes**.

## AWS CLI
<a name="USER_WorkingWithParamGroups.Modifying.CLI"></a>

To modify a DB parameter group, use the AWS CLI [`modify-db-parameter-group`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-parameter-group.html) command with the following required options:
+ `--db-parameter-group-name`
+ `--parameters`

The following example modifies the` max_connections` and `max_allowed_packet` values in the DB parameter group named *mydbparametergroup*.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name {{mydbparametergroup}} \
    --parameters "ParameterName={{max_connections}},ParameterValue={{250}},ApplyMethod={{immediate}}" \
                 "ParameterName={{max_allowed_packet}},ParameterValue={{1024}},ApplyMethod={{immediate}}"
```
For Windows:  

```
aws rds modify-db-parameter-group ^
    --db-parameter-group-name {{mydbparametergroup}} ^
    --parameters "ParameterName={{max_connections}},ParameterValue={{250}},ApplyMethod={{immediate}}" ^
                 "ParameterName={{max_allowed_packet}},ParameterValue={{1024}},ApplyMethod={{immediate}}"
```
The command produces output like the following:  

```
DBPARAMETERGROUP  mydbparametergroup
```

## RDS API
<a name="USER_WorkingWithParamGroups.Modifying.API"></a>

To modify a DB parameter group, use the RDS API [`ModifyDBParameterGroup`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBParameterGroup.html) operation with the following required parameters:
+ `DBParameterGroupName`
+ `Parameters`