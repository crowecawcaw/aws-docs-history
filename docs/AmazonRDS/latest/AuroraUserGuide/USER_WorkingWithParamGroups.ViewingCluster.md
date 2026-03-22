# Viewing parameter values for a DB cluster parameter groupin Amazon Aurora

You can get a list of all parameters in a DB cluster parameter group and their values.

###### To view the parameter values for a DB cluster parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.

The DB cluster parameter groups appear in the list with **DB cluster parameter group** for **Type**. 3. Choose the name of the DB cluster parameter group to see its list of parameters.
To view the parameter values for a DB cluster parameter group, use the AWS CLI [`describe-db-cluster-parameters`](../../../cli/latest/reference/rds/describe-db-cluster-parameters.md "../../../cli/latest/reference/rds/describe-db-cluster-parameters.md") command with the following required parameter.

- `--db-cluster-parameter-group-name`

###### Example

The following example lists the parameters and parameter values for a DB cluster parameter group named
_mydbclusterparametergroup_, in JSON format.

The command returns a response like the following:

```
aws rds describe-db-cluster-parameters --db-cluster-parameter-group-name `mydbclusterparametergroup`
```

```
{
    "Parameters": [
        {
            "ParameterName": "allow-suspicious-udfs",
            "Description": "Controls whether user-defined functions that have only an xxx symbol for the main function can be loaded",
            "Source": "engine-default",
            "ApplyType": "static",
            "DataType": "boolean",
            "AllowedValues": "0,1",
            "IsModifiable": false,
            "ApplyMethod": "pending-reboot",
            "SupportedEngineModes": [
                "provisioned"
            ]
        },
        {
            "ParameterName": "aurora_binlog_read_buffer_size",
            "ParameterValue": "5242880",
            "Description": "Read buffer size used by master dump thread when the switch aurora_binlog_use_large_read_buffer is ON.",
            "Source": "engine-default",
            "ApplyType": "dynamic",
            "DataType": "integer",
            "AllowedValues": "8192-536870912",
            "IsModifiable": true,
            "ApplyMethod": "pending-reboot",
            "SupportedEngineModes": [
                "provisioned"
            ]
        },

...
```

To view the parameter values for a DB cluster parameter group, use the RDS API [`DescribeDBClusterParameters`](../APIReference/API_DescribeDBParameters.md "../APIReference/API_DescribeDBParameters.md") command with the following
required parameter.

- `DBClusterParameterGroupName`
  In some cases, the allowed values for a parameter aren't shown. These are always parameters where the source is the database
  engine default.

To view the values of these parameters, you can run the following SQL statements:

- MySQL:

```
-- Show the value of a particular parameter
mysql`$` SHOW VARIABLES LIKE '%`parameter_name`%';

-- Show the values of all parameters
mysql`$` SHOW VARIABLES;
```

- PostgreSQL:

```
-- Show the value of a particular parameter
postgresql=> SHOW `parameter_name`;

-- Show the values of all parameters
postgresql=> SHOW ALL;
```
