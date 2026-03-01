# Amazon RDS for Db2 parameters

Amazon RDS for Db2 uses three types of parameters: database manager configuration parameters,
registry variables, and database configuration parameters. You can manage the first two
types through parameter groups and the last type through the [rdsadmin.update_db_param](db2-sp-managing-databases.md#db2-sp-update-db-param "db2-sp-managing-databases.md#db2-sp-update-db-param") stored
procedure.

By default, an RDS for Db2 DB instance uses a DB parameter group that is specific to a Db2
database and DB instance. This parameter group contains parameters for the IBM Db2 database
engine, specifically the database manager configuration parameters and registry variables.
For information about working with parameter groups, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

RDS for Db2 database configuration parameters are set to the default values of the storage
engine that you have selected. For more information about Db2 parameters, see the [Db2
database configuration parameters](https://www.ibm.com/docs/en/db2/11.5?topic=parameters-database-configuration "https://www.ibm.com/docs/en/db2/11.5?topic=parameters-database-configuration") in the IBM Db2 documentation.

###### Topics

- [Viewing the parameters in parameter groups](#db2-viewing-parameter-group-parameters "#db2-viewing-parameter-group-parameters")
- [Viewing all parameters with Db2 commands](#db2-viewing-parameters-db2-commands "#db2-viewing-parameters-db2-commands")
- [Modifying the parameters in parameter groups](#db2-modifying-parameter-group-parameters "#db2-modifying-parameter-group-parameters")
- [Modifying the database configuration parameters with Db2 commands](#db2-modifying-parameters-db2-commands "#db2-modifying-parameters-db2-commands")

## Viewing the parameters in parameter groups

The database manager configuration parameters and the registry variables are set in
parameter groups. You can view the database manager configuration parameters and the
registry variables for a specific Db2 version by using the AWS Management Console, the AWS CLI, or the
RDS API.

###### To view the parameter values for a DB parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.

The DB parameter groups appear in a list. 3. Choose the name of the parameter group to see its list of
parameters.
You can view the database manager configuration parameters and the registry
variables for a Db2 version by running the [describe-engine-default-parameters](../../../cli/latest/reference/rds/describe-engine-default-parameters.md "../../../cli/latest/reference/rds/describe-engine-default-parameters.md") command.
Specify one of the following values for the
`--db-parameter-group-family` option:

- `db2-ae-11.5`
- `db2-se-11.5`
  For example, to view the parameters for Db2 Standard Edition
  11.5, run the following command:

```
aws rds describe-engine-default-parameters --db-parameter-group-family db2-se-11.5
```

This command produces output similar to the following example:

```
{
    "EngineDefaults": {
        "Parameters": [
            {
                "ParameterName": "agent_stack_sz",
                "ParameterValue": "1024",
                "Description": "You can use this parameter to determine the amount of memory that is allocated by Db2 for each agent thread stack.",
                "Source": "engine-default",
                "ApplyType": "static",
                "DataType": "integer",
                "AllowedValues": "256-32768",
                "IsModifiable": false
            },
            {
                "ParameterName": "agentpri",
                "ParameterValue": "-1",
                "Description": "This parameter controls the priority given to all agents and to other database manager instance processes and threads by the operating system scheduler. This priority determines how CPU time is allocated to the database manager processes, agents, and threads relative to other processes and threads running on the machine.",
                "Source": "engine-default",
                "ApplyType": "static",
                "DataType": "integer",
                "AllowedValues": "1-99",
                "IsModifiable": false
            },
            ...
        ]
    }
}
```

To list only the modifiable parameters for Db2 Standard Edition
11.5, run the following command:

For Linux, macOS, or Unix:

```
aws rds describe-engine-default-parameters \
    --db-parameter-group-family db2-se-11.5 \
    --query 'EngineDefaults.Parameters[?IsModifiable==`true`].{ParameterName:ParameterName, DefaultValue:ParameterValue}'
```

For Windows:

```
aws rds describe-engine-default-parameters ^
    --db-parameter-group-family db2-se-11.5 ^
    --query 'EngineDefaults.Parameters[?IsModifiable==`true`].{ParameterName:ParameterName, DefaultValue:ParameterValue}'
```

To view the parameter values for a DB parameter group, use the [`DescribeDBParameters`](../APIReference/API_DescribeDBParameters.md "../APIReference/API_DescribeDBParameters.md") operation with the following
required parameter.

- `DBParameterGroupName`

## Viewing all parameters with Db2 commands

You can view the settings for database manager configuration parameters, database
configuration parameters, and registry variables by using Db2 commands.

###### To view the settings

1. Connect to your Db2 database. In the following example, replace
   `database_name`,
   `master_username`, and
   `master_password` with your information.

```
db2 "connect to `database_name` user `master_username` using `master_password`"
```

2. Find the supported Db2 version.

```
db2 "select service_level, fixpack_num from table(sysproc.env_get_inst_info()) as instanceinfo"
```

3. View the parameters for a specific Db2 version.
   - View database manager configuration parameters by running the
     following command:

   ```
   db2 "select cast(substr(name,1,24) as varchar(24)) as name, case
       when value_flags = 'NONE' then '' else value_flags end flags,
       cast(substr(value,1,64) as varchar(64)) as current_value
       from sysibmadm.dbmcfg
       order by name asc with UR"
   ```

   - View all of your database configuration parameters by running the
     following command:

   ```
   db2 "select cast(substr(name,1,24) as varchar(24)) as name, case
       when value_flags = 'NONE' then '' else value_flags end flags,
       cast(substr(value,1,64) as varchar(64)) as current_value
       from table(db_get_cfg(null)) order by name asc, member asc with UR"
   ```

   - View the currently set registry variables by running the following
     command:

   ```
   db2 "select cast(substr(reg_var_name,1,50) as varchar(50)) as reg_var_name,
       cast(substr(reg_var_value,1,50) as varchar(50)) as reg_var_value,
       level from table(env_get_reg_variables(null))
       order by reg_var_name,member with UR"
   ```

## Modifying the parameters in parameter groups

You can modify the database manager configuration parameters and the registry
variables in custom parameter groups by using the AWS Management Console, the AWS CLI, or the RDS API.
For more information, see [DB parameter groups for Amazon RDS DB instances](USER_WorkingWithDBInstanceParamGroups.md "USER_WorkingWithDBInstanceParamGroups.md").

###### To modify database manager configuration parameters and registry variables

1. Create a custom parameter group. For more information about creating a
   DB parameter group, see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
2. Modify the parameters in that custom parameter group. For more
   information about modifying a parameter group, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### To modify database manager configuration parameters and registry variables

1. Create a custom parameter group by running the [create-db-parameter-group](../../../cli/latest/reference/rds/create-db-parameter-group.md "../../../cli/latest/reference/rds/create-db-parameter-group.md") command.

Include the following required options:

    * `--db-parameter-group-name` – A name for the
     parameter group that you are creating.
    * `--db-parameter-group-family` – The Db2
     engine edition and major version. Valid values:
     `db2-se-11.5`, `db2-ae-11.5`.
    * `--description` – A description for this
     parameter group.

For more information about creating a DB parameter group, see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 2. Modify the parameters in the custom parameter group that you created
by running the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md")
command.

Include the following required options:

    * `--db-parameter-group-name` – The name of
     the parameter group that you created.
    * `--parameters` – An array of parameter
     names, values, and the application methods for the parameter
     update.

For more information about modifying a parameter group, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### To modify database manager configuration parameters and registry variables

1. Create a custom DB parameter group by using the [CreateDBParameterGroup](../APIReference/API_CreateDBParameterGroup.md "../APIReference/API_CreateDBParameterGroup.md") operation.

Include the following required parameters:

    * `DBParameterGroupName`
    * `DBParameterGroupFamily`
    * `Description`

For more information about creating a DB parameter group, see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 2. Modify the parameters in the custom parameter group that you created
by using the [ModifyDBParameterGroup](../APIReference/API_ModifyDBParameterGroup.md "../APIReference/API_ModifyDBParameterGroup.md") operation.

Include the following required parameters:

    * `DBParameterGroupName`
    * `Parameters`

For more information about modifying a parameter group, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Modifying the database configuration parameters with Db2 commands

You can modify the database configuration parameters with Db2 commands.

###### To modify the database configuration parameters

1. Connect to the `rdsadmin` database. In the following example,
   replace `master_username` and
   `master_password` with your information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Change the database configuration parameters by calling the
   `rdsadmin.update_db_param` stored procedure. For more
   information, see [rdsadmin.update_db_param](db2-sp-managing-databases.md#db2-sp-update-db-param "db2-sp-managing-databases.md#db2-sp-update-db-param").

```
db2 "call rdsadmin.update_db_param(
    '`database_name`',
    '`parameter_to_modify`',
    '`changed_value`',
    '`restart_database`')"
```
