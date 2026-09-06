

# Create a new table with automatic scaling
<a name="autoscaling.createTable"></a>

When you create a new Amazon Keyspaces table, you can automatically enable auto scaling for the table's write or read capacity. This allows Amazon Keyspaces to contact Application Auto Scaling on your behalf to register the table as a scalable target and adjust the provisioned write or read capacity. 

For more information on how to create a multi-Region table and configure different auto scaling settings for table replicas, see [Create a multi-Region table in provisioned mode with auto scaling in Amazon Keyspaces](tables-mrr-create-provisioned.md).

**Note**  
Amazon Keyspaces automatic scaling requires the presence of a service-linked role (`AWSServiceRoleForApplicationAutoScaling_CassandraTable`) that performs automatic scaling actions on your behalf. This role is created automatically for you. For more information, see [Using service-linked roles for Amazon Keyspaces](using-service-linked-roles.md).

------
#### [ Console ]

**Create a new table with automatic scaling enabled using the console**

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home).

1. In the navigation pane, choose **Tables**, and then choose **Create table**.

1. On the **Create table** page in the **Table details** section, select a keyspace and provide a name for the new table.

1. In the **Columns** section, create the schema for your table.

1. In the **Primary key** section, define the primary key of the table and select optional clustering columns.

1. In the **Table settings** section, choose **Customize settings**.

1. Continue to **Read/write capacity settings**.

1. For **Capacity mode**, choose **Provisioned**.

1. In the **Read capacity** section, confirm that **Scale automatically** is selected.

   In this step, you select the minimum and maximum read capacity units for the table, as well as the target utilization.
   + **Minimum capacity units** – Enter the value for the minimum level of throughput that the table should always be ready to support. The value must be between 1 and the maximum throughput per second quota for your account (40,000 by default).
   + **Maximum capacity units** – Enter the maximum amount of throughput you want to provision for the table. The value must be between 1 and the maximum throughput per second quota for your account (40,000 by default).
   + **Target utilization** – Enter a target utilization rate between 20% and 90%. When traffic exceeds the defined target utilization rate, capacity is automatically scaled up. When traffic falls below the defined target, it is automatically scaled down again.
**Note**  
To learn more about default quotas for your account and how to increase them, see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md).

1. In the **Write capacity** section, choose the same settings as defined in the previous step for read capacity, or configure capacity values manually.

1. Choose **Create table**. Your table is created with the specified automatic scaling parameters.

------
#### [ Cassandra Query Language (CQL) ]

**Create a new table with Amazon Keyspaces automatic scaling using CQL**

To configure auto scaling settings for a table programmatically, you use the `AUTOSCALING_SETTINGS` statement that contains the parameters for Amazon Keyspaces auto scaling. The parameters define the conditions that direct Amazon Keyspaces to adjust your table's provisioned throughput, and what additional optional actions to take. In this example, you define the auto scaling settings for *mytable*.

The policy contains the following elements:
+ `AUTOSCALING_SETTINGS` – Specifies if Amazon Keyspaces is allowed to adjust throughput capacity on your behalf. The following values are required:
  + `provisioned_write_capacity_autoscaling_update`:
    + `minimum_units`
    + `maximum_units`
  + `provisioned_read_capacity_autoscaling_update`:
    + `minimum_units`
    + `maximum_units`
  + `scaling_policy` – Amazon Keyspaces supports the target tracking policy. To define the target tracking policy, you configure the following parameters.
    + `target_value` – Amazon Keyspaces auto scaling ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `target_value` as a percentage.
    + `disableScaleIn`: (Optional) A `boolean` that specifies if `scale-in` is disabled or enabled for the table. This parameter is disabled by default. To turn on `scale-in`, set the `boolean` value to `FALSE`. This means that capacity is automatically scaled down for a table on your behalf. 
    + `scale_out_cooldown` – A scale-out activity increases the provisioned throughput of your table. To add a cooldown period for scale-out activities, specify a value, in seconds, for `scale_out_cooldown`. If you don't specify a value, the default value is 0. For more information about target tracking and cooldown periods, see [ Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*. 
    + `scale_in_cooldown` – A scale-in activity decreases the provisioned throughput of your table. To add a cooldown period for scale-in activities, specify a value, in seconds, for `scale_in_cooldown`. If you don't specify a value, the default value is 0. For more information about target tracking and cooldown periods, see [ Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*.

**Note**  
To further understand how `target_value` works, suppose that you have a table with a provisioned throughput setting of 200 write capacity units. You decide to create a scaling policy for this table, with a `target_value` of 70 percent.  
Now suppose that you begin driving write traffic to the table so that the actual write throughput is 150 capacity units. The consumed-to-provisioned ratio is now (150 / 200), or 75 percent. This ratio exceeds your target, so auto scaling increases the provisioned write capacity to 215 so that the ratio is (150 / 215), or 69.77 percent—as close to your `target_value` as possible, but not exceeding it.

For *mytable*, you set `TargetValue` for both read and write capacity to 50 percent. Amazon Keyspaces auto scaling adjusts the table's provisioned throughput within the range of 5–10 capacity units so that the consumed-to-provisioned ratio remains at or near 50 percent. For read capacity, you set the values for `ScaleOutCooldown` and `ScaleInCooldown` to 60 seconds.

You can use the following statement to create a new Amazon Keyspaces table with auto scaling enabled. 

```
CREATE TABLE mykeyspace.mytable(pk int, ck int, PRIMARY KEY (pk, ck))
WITH CUSTOM_PROPERTIES = {  
    'capacity_mode': {  
        'throughput_mode': 'PROVISIONED',  
        'read_capacity_units': 1,  
        'write_capacity_units': 1  
    }
} AND AUTOSCALING_SETTINGS = {
    'provisioned_write_capacity_autoscaling_update': {
        'maximum_units': 10,  
        'minimum_units': 5,  
        'scaling_policy': {
            'target_tracking_scaling_policy_configuration': {
                'target_value': 50
            }  
        }  
    },  
    'provisioned_read_capacity_autoscaling_update': {  
        'maximum_units': 10,  
        'minimum_units': 5,  
        'scaling_policy': {  
            'target_tracking_scaling_policy_configuration': {  
                'target_value': 50,
                'scale_in_cooldown': 60,  
                'scale_out_cooldown': 60
            }  
        }  
    }
};
```

------
#### [ CLI ]

**Create a new table with Amazon Keyspaces automatic scaling using the AWS CLI**

To configure auto scaling settings for a table programmatically, you use the `autoScalingSpecification` action that defines the parameters for Amazon Keyspaces auto scaling. The parameters define the conditions that direct Amazon Keyspaces to adjust your table's provisioned throughput, and what additional optional actions to take. In this example, you define the auto scaling settings for *mytable*.

The policy contains the following elements:
+ `autoScalingSpecification` – Specifies if Amazon Keyspaces is allowed to adjust capacity throughput on your behalf. You can enable auto scaling for read and for write capacity separately. Then you must specify the following parameters for `autoScalingSpecification`:
  + `writeCapacityAutoScaling` – The maximum and minimum write capacity units.
  + `readCapacityAutoScaling` – The maximum and minimum read capacity units.
  + `scalingPolicy` – Amazon Keyspaces supports the target tracking policy. To define the target tracking policy, you configure the following parameters.
    + `targetValue` – Amazon Keyspaces auto scaling ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage.
    + `disableScaleIn`: (Optional) A `boolean` that specifies if `scale-in` is disabled or enabled for the table. This parameter is disabled by default. To turn on `scale-in`, set the `boolean` value to `FALSE`. This means that capacity is automatically scaled down for a table on your behalf. 
    + `scaleOutCooldown` – A scale-out activity increases the provisioned throughput of your table. To add a cooldown period for scale-out activities, specify a value, in seconds, for `ScaleOutCooldown`. The default value is 0. For more information about target tracking and cooldown periods, see [ Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*. 
    + `scaleInCooldown` – A scale-in activity decreases the provisioned throughput of your table. To add a cooldown period for scale-in activities, specify a value, in seconds, for `ScaleInCooldown`. The default value is 0. For more information about target tracking and cooldown periods, see [ Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*.

**Note**  
To further understand how `TargetValue` works, suppose that you have a table with a provisioned throughput setting of 200 write capacity units. You decide to create a scaling policy for this table, with a `TargetValue` of 70 percent.  
Now suppose that you begin driving write traffic to the table so that the actual write throughput is 150 capacity units. The consumed-to-provisioned ratio is now (150 / 200), or 75 percent. This ratio exceeds your target, so auto scaling increases the provisioned write capacity to 215 so that the ratio is (150 / 215), or 69.77 percent—as close to your `TargetValue` as possible, but not exceeding it.

For *mytable*, you set `TargetValue` for both read and write capacity to 50 percent. Amazon Keyspaces auto scaling adjusts the table's provisioned throughput within the range of 5–10 capacity units so that the consumed-to-provisioned ratio remains at or near 50 percent. For read capacity, you set the values for `ScaleOutCooldown` and `ScaleInCooldown` to 60 seconds.

When creating tables with complex auto scaling settings, it's helpful to load the auto scaling settings from a JSON file. For the following example, you can download the example JSON file from [auto-scaling.zip](samples/auto-scaling.zip) and extract `auto-scaling.json`, taking note of the path to the file. In this example, the JSON file is located in the current directory. For different file path options, see [ How to load parameters from a file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html#cli-usage-parameters-file-how).

```
aws keyspaces create-table --keyspace-name mykeyspace --table-name mytable 
            \ --schema-definition 'allColumns=[{name=pk,type=int},{name=ck,type=int}],partitionKeys=[{name=pk},{name=ck}]' 
            \ --capacity-specification throughputMode=PROVISIONED,readCapacityUnits=1,writeCapacityUnits=1 
            \ --auto-scaling-specification file://auto-scaling.json
```

------