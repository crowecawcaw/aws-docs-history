

# Viewing parameter values for a DB parameter group in Amazon Aurora
<a name="USER_WorkingWithParamGroups.Viewing"></a>

You can get a list of all parameters in a DB parameter group and their values.

## Console
<a name="USER_WorkingWithParamGroups.Viewing.CON"></a>

**To view the parameter values for a DB parameter group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

   The DB parameter groups appear in a list.

1. Choose the name of the parameter group to see its list of parameters.

## AWS CLI
<a name="USER_WorkingWithParamGroups.Viewing.CLI"></a>

To view the parameter values for a DB parameter group, use the AWS CLI [`describe-db-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) command with the following required parameter.
+ `--db-parameter-group-name`

**Example**  
The following example lists the parameters and parameter values for a DB parameter group named *mydbparametergroup.*  

```
aws rds describe-db-parameters --db-parameter-group-name {{mydbparametergroup}}
```
The command returns a response like the following:  

```
DBPARAMETER  Parameter Name            Parameter Value  Source           Data Type  Apply Type  Is Modifiable
DBPARAMETER  allow-suspicious-udfs                      engine-default   boolean    static      false
DBPARAMETER  auto_increment_increment                   engine-default   integer    dynamic     true
DBPARAMETER  auto_increment_offset                      engine-default   integer    dynamic     true
DBPARAMETER  binlog_cache_size         32768            system           integer    dynamic     true
DBPARAMETER  socket                    /tmp/mysql.sock  system           string     static      false
```

## RDS API
<a name="USER_WorkingWithParamGroups.Viewing.API"></a>

To view the parameter values for a DB parameter group, use the RDS API [`DescribeDBParameters`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBParameters.html) command with the following required parameter.
+ `DBParameterGroupName`