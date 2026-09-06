

# Tables
<a name="cql.ddl.table"></a>

*Tables* are the primary data structures in Amazon Keyspaces. Data in a table is organized into rows and columns. A subset of those columns is used to determine partitioning (and ultimately data placement) through the specification of a partition key.

Another set of columns can be defined into clustering columns, which means that they can participate as predicates in query execution. 

By default, new tables are created with *on-demand* throughput capacity. You can change the capacity mode for new and existing tables. For more information about read/write capacity throughput modes, see [Configure read/write capacity modes in Amazon Keyspaces](ReadWriteCapacityMode.md). 

For tables in provisioned mode, you can configure optional `AUTOSCALING_SETTINGS`. For more information about Amazon Keyspaces auto scaling and the available options, see [Configure automatic scaling on an existing table](autoscaling.configureTable.md).

For information about quota limits and constraints for Amazon Keyspaces tables, see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md).

**Topics**
+ [CREATE TABLE](#cql.ddl.table.create)
+ [ALTER TABLE](#cql.ddl.table.alter)
+ [RESTORE TABLE](#cql.ddl.table.restore)
+ [DROP TABLE](#cql.ddl.table.drop)

## CREATE TABLE
<a name="cql.ddl.table.create"></a>

Use the `CREATE TABLE` statement to create a new table.

 **Syntax**

```
create_table_statement ::=  CREATE TABLE [ IF NOT EXISTS ] table_name
    '('
        column_definition 
        ( ',' column_definition )*
        [ ',' PRIMARY KEY '(' primary_key ')' ]
    ')' [ WITH table_options ]

column_definition      ::=  column_name cql_type [ FROZEN ][ STATIC ][ PRIMARY KEY]

primary_key            ::=  partition_key [ ',' clustering_columns ]

partition_key          ::=  column_name
                              | '(' column_name ( ',' column_name )* ')'

clustering_columns     ::=  column_name ( ',' column_name )*

table_options          ::=  [table_options]
                              | CLUSTERING ORDER BY '(' clustering_order ')' [ AND table_options ]
                              | cdc
                              | CUSTOM_PROPERTIES
                              | AUTOSCALING_SETTINGS
                              | default_time_to_live
                              | TAGS

clustering_order       ::=  column_name (ASC | DESC) ( ',' column_name (ASC | DESC) )*
```

Where:
+ `table_name` is the name of the table to be created. The fully qualified name includes the keyspace prefix. Alternatively, you can set the current keyspace with the `USE` keyspace statement.
+ `column_definition` consists of the following:
  +  *`column_name`* – The name of the column.
  + `cql_type` – An Amazon Keyspaces data type (see [Data types](cql.elements.md#cql.data-types)).
  + `FROZEN` – Designates this column that is user-defined or of type `collection` (for example, `LIST`, `SET`, or `MAP`) as frozen. A *frozen* collection is serialized into a single immutable value and treated like a `BLOB`. For more information, see [Collection types](cql.elements.md#cql.data-types.collection).
  + `STATIC` – Designates this column as static. Static columns store values that are shared by all rows in the same partition.
  + `PRIMARY KEY` – Designates this column as the table's primary key.
+ `primary_key` consists of the following:
  + `partition_key`
  + `clustering_columns`
+ `partition_key`:
  + The partition key can be a single column, or it can be a compound value composed of two or more columns. The partition key portion of the primary key is required and determines how Amazon Keyspaces stores your data. 
+ `clustering_columns`:
  + The optional clustering column portion of your primary key determines how the data is clustered and sorted within each partition. 
+ `table_options` consist of the following:
  + *`CLUSTERING ORDER BY`* – The default CLUSTERING ORDER on a table is composed of your clustering keys in the `ASC` (ascending) sort direction. Specify it to override the default sort behavior. 
  +  *`cdc`* – A boolean that specifies if Amazon Keyspaces creates a change data capture (CDC) stream for the table. The default is `false`. To specify the `view type` when enabling a stream, set the `cdc_specification` with `CUSTOM_PROPERTIES` . 
  +  *`CUSTOM_PROPERTIES`* – A map of settings that are specific to Amazon Keyspaces.
    +  `capacity_mode`: Specifies the read/write throughput capacity mode for the table. The options are `throughput_mode:PAY_PER_REQUEST` and `throughput_mode:PROVISIONED`. The provisioned capacity mode requires `read_capacity_units` and `write_capacity_units` as inputs. The default is `throughput_mode:PAY_PER_REQUEST`.
    +  `cdc_specification`: Specifies the `view_type` of the CDC stream. The options are:
      + `NEW_AND_OLD_IMAGES` – both versions of the row, before and after the change. This is the default.
      + `NEW_IMAGE` – the version of the row after the change.
      + `OLD_IMAGE` – the version of the row before the change.
      + `KEYS_ONLY` – the partition and clustering keys of the row that was changed.

      For more information about CDC streams, see [Working with change data capture (CDC) streams in Amazon Keyspaces](cdc.md). For code examples, see [Enable a CDC stream when creating a new table in Amazon Keyspaces](keyspaces-enable-cdc-new-table.md).
    +  `client_side_timestamps`: Specifies if client-side timestamps are enabled or disabled for the table. The options are `{'status': 'enabled'}` and `{'status': 'disabled'}`. If it's not specified, the default is `status:disabled`. After client-side timestamps are enabled for a table, this setting cannot be disabled. 
    +  `encryption_specification`: Specifies the encryption options for encryption at rest. If it's not specified, the default is `encryption_type:AWS_OWNED_KMS_KEY`. The encryption option customer managed key requires the AWS KMS key in Amazon Resource Name (ARN) format as input: `kms_key_identifier:ARN`: `kms_key_identifier:ARN`. 
    +  `point_in_time_recovery`: Specifies if point-in-time restore is enabled or disabled for the table. The options are `status:enabled` and `status:disabled`. If it's not specified, the default is `status:disabled`.
    + `replica_updates`: Specifies the settings of a multi-Region table that are specific to an AWS Region. For a multi-Region table, you can configure the table's read capacity differently per AWS Region. You can do this by configuring the following parameters. For more information and examples, see [Create a multi-Region table in provisioned mode with auto scaling in Amazon Keyspaces](tables-mrr-create-provisioned.md).
      + `region` – The AWS Region of the table replica with the following settings:
        + `read_capacity_units`
    +  `TTL`: Enables Time to Live custom settings for the table. To enable, use `status:enabled`. The default is `status:disabled`. After `TTL` is enabled, you can't disable it for the table.
  + `AUTOSCALING_SETTINGS` includes the following optional settings for tables in provisioned mode. For more information and examples, see [Create a new table with automatic scaling](autoscaling.createTable.md).
    + `provisioned_write_capacity_autoscaling_update`:
      + `autoscaling_disabled` – To enable auto scaling for write capacity, set the value to `false`. The default is `true`. (Optional)
      + `minimum_units` – The minimum level of write throughput that the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
      + `maximum_units` – The maximum level of write throughput that the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
      + `scaling_policy` – Amazon Keyspaces supports the target tracking policy. The auto scaling target is the provisioned write capacity of the table.
        + `target_tracking_scaling_policy_configuration` – To define the target tracking policy, you must define the target value. For more information about target tracking and cooldown periods, see [ Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*. 
          + `target_value` – The target utilization rate of the table. Amazon Keyspaces auto scaling ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `target_value` as a percentage. A double between 20 and 90. (Required)
          + `scale_in_cooldown` – A cooldown period in seconds between scaling activities that lets the table stabilize before another scale in activity starts. If no value is provided, the default is 0. (Optional)
          + `scale_out_cooldown` – A cooldown period in seconds between scaling activities that lets the table stabilize before another scale out activity starts. If no value is provided, the default is 0. (Optional)
          + `disable_scale_in`: A `boolean` that specifies if `scale-in` is disabled or enabled for the table. This parameter is disabled by default. To turn on `scale-in`, set the `boolean` value to `FALSE`. This means that capacity is automatically scaled down for a table on your behalf. (Optional) 
    + `provisioned_read_capacity_autoscaling_update`:
      + `autoscaling_disabled` – To enable auto scaling for read capacity, set the value to `false`. The default is `true`. (Optional)
      + `minimum_units` – The minimum level of throughput that the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
      + `maximum_units` – The maximum level of throughput that the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
      + `scaling_policy` – Amazon Keyspaces supports the target tracking policy. The auto scaling target is the provisioned read capacity of the table.
        + `target_tracking_scaling_policy_configuration` – To define the target tracking policy, you must define the target value. For more information about target tracking and cooldown periods, see [ Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*. 
          + `target_value` – The target utilization rate of the table. Amazon Keyspaces auto scaling ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `target_value` as a percentage. A double between 20 and 90. (Required)
          + `scale_in_cooldown` – A cooldown period in seconds between scaling activities that lets the table stabilize before another scale in activity starts. If no value is provided, the default is 0. (Optional)
          + `scale_out_cooldown` – A cooldown period in seconds between scaling activities that lets the table stabilize before another scale out activity starts. If no value is provided, the default is 0. (Optional)
          + `disable_scale_in`: A `boolean` that specifies if `scale-in` is disabled or enabled for the table. This parameter is disabled by default. To turn on `scale-in`, set the `boolean` value to `FALSE`. This means that capacity is automatically scaled down for a table on your behalf. (Optional) 
    + `replica_updates`: Specifies the AWS Region specific auto scaling settings of a multi-Region table. For a multi-Region table, you can configure the table's read capacity differently per AWS Region. You can do this by configuring the following parameters. For more information and examples, see [Update the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces](tables-mrr-autoscaling.md).
      + `region` – The AWS Region of the table replica with the following settings:
        + `provisioned_read_capacity_autoscaling_update`
          + `autoscaling_disabled` – To enable auto scaling for the table's read capacity, set the value to `false`. The default is `true`. (Optional) 
**Note**  
Auto scaling for a multi-Region table has to be either enabled or disabled for all replicas of the table.
          + `minimum_units` – The minimum level of read throughput that the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
          + `maximum_units` – The maximum level of read throughput that the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
          + `scaling_policy` – Amazon Keyspaces supports the target tracking policy. The auto scaling target is the provisioned read capacity of the table.
            + `target_tracking_scaling_policy_configuration` – To define the target tracking policy, you must define the target value. For more information about target tracking and cooldown periods, see [ Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*. 
              + `target_value` – The target utilization rate of the table. Amazon Keyspaces auto scaling ensures that the ratio of consumed read capacity to provisioned read capacity stays at or near this value. You define `target_value` as a percentage. A double between 20 and 90. (Required)
              + `scale_in_cooldown` – A cooldown period in seconds between scaling activities that lets the table stabilize before another scale in activity starts. If no value is provided, the default is 0. (Optional)
              + `scale_out_cooldown` – A cooldown period in seconds between scaling activities that lets the table stabilize before another scale out activity starts. If no value is provided, the default is 0. (Optional)
              + `disable_scale_in`: A `boolean` that specifies if `scale-in` is disabled or enabled for the table. This parameter is disabled by default. To turn on `scale-in`, set the `boolean` value to `FALSE`. This means that read capacity is automatically scaled down for a table on your behalf. (Optional) 
  + `default_time_to_live` – The default Time to Live setting in seconds for the table.
  + `TAGS` – A list of key-value pair tags to be attached to the resource when it's created. 
  + `clustering_order` consists of the following:
    +  *`column_name`* – The name of the column. 
    +  *`ASC | DESC`* – Sets the ascendant (`ASC`) or descendant (`DESC`) order modifier. If it's not specified, the default order is ASC. 

**Example**

```
CREATE TABLE IF NOT EXISTS {{my_keyspace.my_table}} (
                                            id text,
                                            name text,
                                            region text,
                                            division text,
                                            project text,
                                            role text,
                                            pay_scale int,
                                            vacation_hrs float,
                                            manager_id text,
                                            PRIMARY KEY (id,division))
                                            WITH CUSTOM_PROPERTIES={
                                                'capacity_mode':{
                                                        'throughput_mode': 'PROVISIONED', 'read_capacity_units': 10, 'write_capacity_units': 20
                                                    },
                                                'point_in_time_recovery':{'status': 'enabled'},
                                                'encryption_specification':{
                                                        'encryption_type': 'CUSTOMER_MANAGED_KMS_KEY', 
                                                        'kms_key_identifier':'{{arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111}}'
                                                    }
                                            }
                                            AND CLUSTERING ORDER BY (division ASC) 
                                            AND TAGS={'key1':'val1', 'key2':'val2'}
                                            AND default_time_to_live = 3024000;
```

In a table that uses clustering columns, non-clustering columns can be declared as static in the table definition. For more information about static columns, see [Estimate capacity consumption for static columns in Amazon Keyspaces](static-columns.md).

**Example**

```
CREATE TABLE {{my_keyspace.my_table}} (
                                            id int,
                                            name text,
                                            region text,
                                            division text,
                                            project text STATIC,
                                            PRIMARY KEY (id,division));
```

You can create a table with a column that uses a user-defined type (UDT). The first statement in the examples creates a type, the second statement creates a table with a column that uses the type.

**Example**

```
CREATE TYPE my_keyspace."udt""N@ME" (my_field int);
CREATE TABLE my_keyspace.my_table (my_col1 int pri key, my_col2 "udt""N@ME");
```

## ALTER TABLE
<a name="cql.ddl.table.alter"></a>

Use the `ALTER TABLE` statement to add new columns, add tags, or change the table's custom properties.

**Syntax**

```
alter_table_statement ::=  ALTER TABLE table_name    
 
        [ ADD ( column_definition | column_definition_list)  ] 
        [[ADD | DROP] TAGS {'key1':'val1', 'key2':'val2'}]            
        [ WITH table_options [ , ... ] ] ;
        
column_definition      ::=  column_name cql_type
```

Where:
+ `table_name` is the name of the table to be altered.
+ `column_definition` is the name of the column and data type to be added.
+ `column_definition_list` is a comma-separated list of columns placed inside parentheses.
+ `table_options` consist of the following:
  + `AUTOSCALING_SETTINGS` includes the optional auto scaling settings for provisioned tables. For syntax and detailed descriptions, see [CREATE TABLE](#cql.ddl.table.create). For examples, see [Configure automatic scaling on an existing table](autoscaling.configureTable.md).
  +  *`cdc`* – A boolean that specifies if Amazon Keyspaces creates a change data capture (CDC) stream for the table. The default is `false`. To specify the `view type` when enabling a stream, set the `cdc_specification` with `CUSTOM_PROPERTIES` . 
  +  *`CUSTOM_PROPERTIES`* – A map of settings specific to Amazon Keyspaces.
    +  `capacity_mode`: Specifies the read/write throughput capacity mode for the table. The options are `throughput_mode:PAY_PER_REQUEST` and `throughput_mode:PROVISIONED`. The provisioned capacity mode requires `read_capacity_units` and `write_capacity_units` as inputs. The default is `throughput_mode:PAY_PER_REQUEST`.
    +  `cdc_specification`: Specifies the `view_type` of the CDC stream. The options are:
      + `NEW_AND_OLD_IMAGES` – both versions of the row, before and after the change. This is the default.
      + `NEW_IMAGE` – the version of the row after the change.
      + `OLD_IMAGE` – the version of the row before the change.
      + `KEYS_ONLY` – the partition and clustering keys of the row that was changed.

      For more information about CDC streams, see [Working with change data capture (CDC) streams in Amazon Keyspaces](cdc.md). For code examples, see [Enable a CDC stream for an existing table in Amazon Keyspaces](keyspaces-enable-cdc-alter-table.md).
    +  `client_side_timestamps`: Specifies if client-side timestamps are enabled or disabled for the table. The options are `{'status': 'enabled'}` and `{'status': 'disabled'}`. If it's not specified, the default is `status:disabled`. After client-side timestamps are enabled for a table, this setting cannot be disabled. 
    +  `encryption_specification`: Specifies the encryption option for encryption at rest. The options are `encryption_type:AWS_OWNED_KMS_KEY` and `encryption_type:CUSTOMER_MANAGED_KMS_KEY`. The encryption option customer managed key requires the AWS KMS key in Amazon Resource Name (ARN) format as input: `kms_key_identifier:ARN`. 
    +  `point_in_time_recovery`: Specifies if point-in-time restore is enabled or disabled for the table. The options are `status:enabled` and `status:disabled`. The default is `status:disabled`.
    + `replica_updates`: Specifies the AWS Region specific settings of a multi-Region table. For a multi-Region table, you can configure the table's read capacity differently per AWS Region. You can do this by configuring the following parameters. For more information and examples, see [Update the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces](tables-mrr-autoscaling.md).
      + `region` – The AWS Region of the table replica with the following settings:
        + `read_capacity_units` 
    +  `ttl`: Enables Time to Live custom settings for the table. To enable, use `status:enabled`. The default is `status:disabled`. After `ttl`is enabled, you can't disable it for the table.
+ `default_time_to_live`: The default Time to Live setting in seconds for the table.
+ `TAGS` is a list of key-value pair tags to be attached to the resource.

**Note**  
With ALTER TABLE, you can only change a single custom property. You can't combine more than one ALTER TABLE command in the same statement.

**Examples**

The following statement shows how to add a column to an existing table.

```
ALTER TABLE {{mykeyspace.mytable}} ADD (ID int);
```

This statement shows how to add two collection columns to an existing table: 
+ A frozen collection column `col_frozen_list` that contains a nested frozen collection
+ A non-frozen collection column `col_map` that contains a nested frozen collection

```
ALTER TABLE {{my_Table}} ADD({{col_frozen_list}} FROZEN<LIST<FROZEN<SET<TEXT>>>>, {{col_map}} MAP<INT, FROZEN<SET<INT>>>);
```

The following example shows how to add a column that uses a user-defined type (UDT) to a table.

```
ALTER TABLE my_keyspace.my_table ADD (my_column, my_udt;);
```

To change a table's capacity mode and specify read and write capacity units, you can use the following statement.

```
ALTER TABLE {{mykeyspace.mytable}} WITH CUSTOM_PROPERTIES={'capacity_mode':{'throughput_mode': 'PROVISIONED', 'read_capacity_units': 10, 'write_capacity_units': 20}};
```

The following statement specifies a customer managed KMS key for the table.

```
ALTER TABLE {{mykeyspace.mytable}} WITH CUSTOM_PROPERTIES={     
              'encryption_specification':{ 
                      'encryption_type': 'CUSTOMER_MANAGED_KMS_KEY', 
                      'kms_key_identifier':'{{arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111}}'     
                  } 
         };
```

To enable point-in-time restore for a table, you can use the following statement.

```
ALTER TABLE mykeyspace.mytable WITH CUSTOM_PROPERTIES={'point_in_time_recovery': {'status': 'enabled'}};
```

To set a default Time to Live value in seconds for a table, you can use the following statement.

```
ALTER TABLE {{my_table}} WITH default_time_to_live = 2592000;
```

This statement enables custom Time to Live settings for a table.

```
ALTER TABLE {{mytable}} WITH CUSTOM_PROPERTIES={'ttl':{'status': 'enabled'}};
```

## RESTORE TABLE
<a name="cql.ddl.table.restore"></a>

Use the `RESTORE TABLE` statement to restore a table to a point in time. This statement requires point-in-time recovery to be enabled on a table. For more information, see [Backup and restore data with point-in-time recovery for Amazon Keyspaces](PointInTimeRecovery.md).

**Syntax**

```
restore_table_statement ::=  
    RESTORE TABLE restored_table_name FROM TABLE source_table_name 
                    [ WITH table_options [ , ... ] ];
```

Where:
+ `restored_table_name` is the name of the restored table.
+ `source_table_name` is the name of the source table.
+ `table_options` consists of the following:
  + `restore_timestamp` is the restore point time in ISO 8601 format. If it's not specified, the current timestamp is used.
  +  *`CUSTOM_PROPERTIES`* – A map of settings specific to Amazon Keyspaces.
    +  `capacity_mode`: Specifies the read/write throughput capacity mode for the table. The options are `throughput_mode:PAY_PER_REQUEST` and `throughput_mode:PROVISIONED`. The provisioned capacity mode requires `read_capacity_units` and `write_capacity_units` as inputs. The default is the current setting from the source table.
    +  `encryption_specification`: Specifies the encryption option for encryption at rest. The options are `encryption_type:AWS_OWNED_KMS_KEY` and `encryption_type:CUSTOMER_MANAGED_KMS_KEY`. The encryption option customer managed key requires the AWS KMS key in Amazon Resource Name (ARN) format as input: `kms_key_identifier:ARN`. To restore a table encrypted with a customer managed key to a table encrypted with an AWS owned key, Amazon Keyspaces requires access to the AWS KMS key of the source table.
    +  `point_in_time_recovery`: Specifies if point-in-time restore is enabled or disabled for the table. The options are `status:enabled` and `status:disabled`. Unlike when you create new tables, the default status for restored tables is `status:enabled` because the setting is inherited from the source table. To disable PITR for restored tables, you must set `status:disabled` explicitly.
    + `replica_updates`: Specifies the AWS Region specific settings of a multi-Region table. For a multi-Region table, you can configure the table's read capacity differently per AWS Region. You can do this by configuring the following parameters. 
      + `region` – The AWS Region of the table replica with the following settings:
        + `read_capacity_units` 
  + `AUTOSCALING_SETTINGS` includes the optional auto scaling settings for provisioned tables. For detailed syntax and descriptions, see [CREATE TABLE](#cql.ddl.table.create).
  + `TAGS` is a list of key-value pair tags to be attached to the resource.

**Note**  
Deleted tables can only be restored to the time of deletion.

**Example**

```
RESTORE TABLE mykeyspace.mytable_restored from table mykeyspace.my_table 
WITH restore_timestamp = '2020-06-30T04:05:00+0000'
AND custom_properties = {'point_in_time_recovery':{'status':'disabled'}, 'capacity_mode':{'throughput_mode': 'PROVISIONED', 'read_capacity_units': 10, 'write_capacity_units': 20}}
AND TAGS={'key1':'val1', 'key2':'val2'};
```

## DROP TABLE
<a name="cql.ddl.table.drop"></a>

Use the `DROP TABLE` statement to remove a table from the keyspace.

**Syntax**

```
drop_table_statement ::=  
    DROP TABLE [ IF EXISTS ] table_name
```

Where:
+ `IF EXISTS` prevents `DROP TABLE` from failing if the table doesn't exist. (Optional)
+ `table_name` is the name of the table to be dropped.

**Example**

```
DROP TABLE my_keyspace.my_table;
```