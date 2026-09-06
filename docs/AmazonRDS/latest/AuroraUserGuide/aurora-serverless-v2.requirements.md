

# Requirements and limitations for Aurora serverless
<a name="aurora-serverless-v2.requirements"></a>

When you create a cluster where you intend to use Aurora serverless DB instances, pay attention to the following requirements and limitations.

**Topics**
+ [Region and version availability](#aurora-serverless-v2-Availability)
+ [Clusters that use Aurora serverless must have a capacity range specified](#aurora-serverless-v2.requirements.capacity-range)
+ [Incompatible scaling configuration](#aurora-serverless-v2.requirements.incompatible-scaling-config)
+ [Some provisioned features aren't supported in Aurora serverless](#aurora-serverless-v2.limitations)

## Region and version availability
<a name="aurora-serverless-v2-Availability"></a>

Feature availability and support varies across specific versions of each Aurora database engine, and across AWS Regions. For more information on version and Region availability with Aurora and Aurora serverless, see [Supported Regions and Aurora DB engines for Aurora serverless](Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.md). 

The following example shows the AWS CLI commands to confirm the exact DB engine values you can use with Aurora serverless for a specific AWS Region. The `--db-instance-class` parameter for Aurora serverless is always `db.serverless`. The `--engine` parameter can be `aurora-mysql` or `aurora-postgresql`. Substitute the appropriate `--region` and `--engine` values to confirm the `--engine-version` values that you can use. If the command doesn't produce any output, Aurora serverless isn't available for that combination of AWS Region and DB engine.

```
aws rds describe-orderable-db-instance-options --engine aurora-mysql --db-instance-class db.serverless \
  --region {{my_region}} --query 'OrderableDBInstanceOptions[].[EngineVersion]' --output text

aws rds describe-orderable-db-instance-options --engine aurora-postgresql --db-instance-class db.serverless \
  --region {{my_region}} --query 'OrderableDBInstanceOptions[].[EngineVersion]' --output text
```

## Clusters that use Aurora serverless must have a capacity range specified
<a name="aurora-serverless-v2.requirements.capacity-range"></a>

An Aurora cluster must have a `ServerlessV2ScalingConfiguration` attribute before you can add any DB instances that use the `db.serverless` DB instance class. This attribute specifies the capacity range. Aurora serverless capacity ranges from a minimum of 0 Aurora capacity units (ACU) to a maximum of 256 ACUs, in increments of 0.5 ACU. The allowed minimum value depends on the Aurora version. Each ACU provides the equivalent of approximately 2 gibibytes (GiB) of RAM and associated CPU and networking. For details about how Aurora serverless uses the capacity range settings, see [How Aurora serverless works](aurora-serverless-v2.how-it-works.md).

For the allowed capacity ranges for various DB engine versions and platform versions, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity). The available scaling range for a given cluster is influenced by both engine version and hardware (platform version).

You can specify the minimum and maximum ACU values in the AWS Management Console when you create a cluster and associated Aurora serverless DB instance. You can also specify the `--serverless-v2-scaling-configuration` option in the AWS CLI. Or you can specify the `ServerlessV2ScalingConfiguration` parameter with the Amazon RDS API. You can specify this attribute when you create a cluster or modify an existing cluster. For the procedures to set the capacity range, see [Setting the Aurora serverless capacity range for a cluster](aurora-serverless-v2-administration.md#aurora-serverless-v2-setting-acus). For a detailed discussion of how to pick minimum and maximum capacity values and how those settings affect some database parameters, see [Choosing the Aurora serverless capacity range for an Aurora cluster](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2-examples-setting-capacity-range-for-cluster).

## Incompatible scaling configuration
<a name="aurora-serverless-v2.requirements.incompatible-scaling-config"></a>

When you modify your Aurora PostgreSQL cluster with a lower maximum capacity, each instance will be scaled down to match the new configuration. If Aurora detects that any of your instances are having trouble scaling down, it may cancel and roll back the scaling configuration update. As a result, the instances will scale back up to their previous configuration. This issue may occur if the new maximum capacity is insufficient to handle the current workload or if the custom parameters applied to the cluster's or instances' database parameter group are set too high. 

When the rollback starts, you will be notified via an Amazon RDS event containing information about instances that could not apply your desired scaling configuration. After the rollback completes, the scaling configuration's maximum capacity will return to its original higher value. Due to the roll back, you may observe that the Aurora Serverless database capacity across all of your cluster's instances may also increase, leading to higher costs.

For example, you have an Aurora PostgreSQL Aurora Serverless cluster with a single instance and the scaling configuration is set to `minCapacity=0.5`, `maxCapacity=128`, and `secondsUntilAutopause=null`. In addition, the database parameter `track_activity_query_size` is set to a custom value of 40960. If you then modify the cluster's scaling configuration to have a maximum capacity of 1 ACU, you may notice that after a couple of hours, the modification has not completed. The high value of the `track_activity_query_size` parameter requires more resources than the new maximum capacity can provide. As a result, even with no workload, the instance's `ServerlessDatabaseCapacity` cannot scale down to match the new maximum capacity of 1 ACU. Aurora serverless will then cancel the scaling configuration modification and will reapply the previous scaling configuration of `minCapacity=0.5`, `maxCapacity=128`, `secondsUntilAutopause=null`. The instance will then scale up to match the previous scaling configuration, ending the cluster's modification. An Amazon RDS event is published notifying you that an incompatible scaling configuration update was detected, canceled, and rolled back to the previous configuration.

### Issues and Remediations
<a name="aurora-serverless-v2.requirements.incompatible-scaling-config.issues"></a>

**New scaling configuration is incompatible with workload**  <a name="aurora-serverless-v2.requirements.incompatible-scaling-config.workload"></a>
The new Aurora serverless scaling configuration's maximum capacity is too low to handle the current workload.  
Recommendations:  
+ Reduce your workload before reapplying the lower maximum capacity.
+ If reducing the workload is not an option, reevaluate the desired maximum capacity. To pick an appropriate maximum capacity, check the maximum `ServerlessDatabaseCapacity` CloudWatch metric for your Aurora PostgreSQL cluster before the scaling configuration update was cancelled and rolled back. Then set your new scaling configuration's maximum capacity to be at least the observed ServerlessDatabaseCapacity value. For more guidance on choosing a maximum capacity, see [Choosing the Aurora serverless capacity range for an Aurora cluster](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2-examples-setting-capacity-range-for-cluster).

**New scaling configuration is incompatible with custom database parameters**  
Your cluster's or instances' custom database parameter groups require additional resources that exceed the new scaling configuration's maximum capacity.  
Potential incompatible Aurora PostgreSQL database parameters:  
+ max\_connections
+ track\_activity\_query\_size
+ min\_dynamic\_shared\_memory
Recommendations:  
+ To pick an appropriate database parameter value, check the default parameter values for each of the parameters listed above. If your configured value exceeds the default values, reduce the parameters to their default values before modifying the scaling configuration with the same reduced maximum capacity.
+ If reducing the database parameters is not an option, follow the same steps to pick an appropriate maximum capacity outlined above in: [New scaling configuration is incompatible with workload](#aurora-serverless-v2.requirements.incompatible-scaling-config.workload).

## Some provisioned features aren't supported in Aurora serverless
<a name="aurora-serverless-v2.limitations"></a>

The following features from Aurora provisioned DB instances currently aren't available for Amazon Aurora serverless:
+ Database activity streams (DAS).
+ Cluster cache management for Aurora PostgreSQL. The `apg_ccm_enabled` configuration parameter doesn't apply to Aurora serverless DB instances.

Some Aurora features work with Aurora serverless, but might cause issues if your capacity range is lower than needed for the memory requirements for those features with your specific workload. In that case, your database might not perform as well as usual, or might encounter out-of-memory errors. For recommendations about setting the appropriate capacity range, see [Choosing the Aurora serverless capacity range for an Aurora cluster](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2-examples-setting-capacity-range-for-cluster). For troubleshooting information if your database encounters out-of-memory errors due to a misconfigured capacity range, see [Avoiding out-of-memory errors](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.setting-capacity.incompatible_parameters).

Aurora Auto Scaling isn't supported. This type of scaling adds new readers to handle additional read-intensive workload, based on CPU usage. However, scaling based on CPU usage isn't meaningful for Aurora serverless. As an alternative, you can create Aurora serverless reader DB instances in advance and leave them scaled down to low capacity. That's a faster and less disruptive way to scale a cluster's read capacity than adding new DB instances dynamically.