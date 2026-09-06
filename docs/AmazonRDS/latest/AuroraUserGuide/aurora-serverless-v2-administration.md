

# Managing Aurora serverless DB clusters
<a name="aurora-serverless-v2-administration"></a>

With Aurora serverless, your clusters are interchangeable with provisioned clusters. The Aurora serverless properties apply to one or more DB instances within a DB cluster. Thus, the procedures for creating clusters, modifying clusters, creating and restoring snapshots, and so on, are basically the same as for other kinds of Aurora clusters. For general procedures for managing Aurora clusters and DB instances, see [Managing an Amazon Aurora DB cluster](CHAP_Aurora.md).

In the following topics, you can learn about management considerations for clusters that contain Aurora serverless DB instances.

**Topics**
+ [Setting the Aurora serverless capacity range for a cluster](#aurora-serverless-v2-setting-acus)
+ [Checking the capacity range for Aurora serverless](#aurora-serverless-v2-checking-capacity)
+ [Checking the platform version for an existing Aurora serverless cluster](#aurora-serverless-v2-checking-platform-version)
+ [Adding an Aurora serverless reader](#aurora-serverless-v2-adding-reader)
+ [Converting a provisioned writer or reader to Aurora serverless](#aurora-serverless-v2-converting-from-provisioned)
+ [Converting an Aurora serverless writer or reader to provisioned](#aurora-serverless-v2-converting-to-provisioned)
+ [Pausing Aurora serverless DB instances](#pause-when-inactive)
+ [Choosing the promotion tier for an Aurora serverless reader](#aurora-serverless-v2-choosing-promotion-tier)
+ [Using TLS/SSL with Aurora serverless](#aurora-serverless-v2.tls)
+ [Viewing Aurora serverless writers and readers](#aurora-serverless-v2.viewing)
+ [Logging for Aurora serverless](#aurora-serverless-v2.logging)

## Setting the Aurora serverless capacity range for a cluster
<a name="aurora-serverless-v2-setting-acus"></a>

To modify configuration parameters or other settings for clusters containing Aurora serverless DB instances, or the DB instances themselves, follow the same general procedures as for provisioned clusters. For details, see [Modifying an Amazon Aurora DB cluster](Aurora.Modifying.md).

The most important setting that's unique to Aurora serverless is the capacity range. After you set the minimum and maximum Aurora capacity unit (ACU) values for an Aurora cluster, you don't need to actively adjust the capacity of the Aurora serverless DB instances in the cluster. Aurora does that for you. This setting is managed at the cluster level. The same minimum and maximum ACU values apply to each Aurora serverless DB instance in the cluster.

You can set the following specific values:
+ **Minimum ACUs** – The Aurora serverless DB instance can reduce capacity down to this number of ACUs.
+ **Maximum ACUs** – The Aurora serverless DB instance can increase capacity up to this number of ACUs.

The available capacity range for Aurora serverless is a function of both the DB engine version and the platform version. Newer DB engine versions allow a maximum capacity of 256 ACUs, a minimum capacity of 0 ACUs, or both. For the capacity ranges for various DB engine versions, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity). 

 For the auto-pause and resume capability that's enabled by setting the minimum capacity to 0 ACUs, see [Scaling to Zero ACUs with automatic pause and resume for Aurora serverless](aurora-serverless-v2-auto-pause.md). 

 For more information on making sure that your Aurora serverless DB clusters can scale up to 256 ACUs, see [Upgrading your Aurora serverless DB cluster to allow scaling to 256 ACUs](#setting-256-acus). 

**Note**  
When you modify the capacity range for an Aurora serverless DB cluster, the change takes place immediately, regardless of whether you choose to apply it immediately or during the next scheduled maintenance window.

In Aurora serverless, you can't directly set the current capacity without modifying the capacity range, as capacity dynamically adjusts based on the workload within the specified range. However, you can influence the capacity indirectly in the following ways:
+ **Adjust the minimum capacity** – Temporarily lower the minimum capacity to reduce the baseline capacity when workloads are light.
+ **Pause scaling temporarily** – To fix the capacity at a specific value, set the minimum and maximum capacity to the same level.
+ **Scale proactive for bursting usage** – If you anticipate bursting workloads, increase the minimum capacity beforehand to maintain a higher baseline during periods of high activity.

For details about the effects of the capacity range and how to monitor and fine-tune it, see [Important Amazon CloudWatch metrics for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.viewing.monitoring) and [Performance and scaling for Aurora serverless](aurora-serverless-v2.setting-capacity.md). Your goal is to make sure that the maximum capacity for the cluster is high enough to handle spikes in workload, and the minimum is low enough to minimize costs when the cluster isn't busy.

Suppose that you determine based on your monitoring that the ACU range for the cluster should be higher, lower, wider, or narrower. You can set the capacity of an Aurora cluster to a specific range of ACUs with the AWS Management Console, the AWS CLI, or the Amazon RDS API. This capacity range applies to every Aurora serverless DB instance in the cluster.

For example, suppose that your cluster has a capacity range of 1–16 ACUs and contains two Aurora serverless DB instances. Then the cluster as a whole consumes somewhere between 2 ACUs (when idle) and 32 ACUs (when fully utilized). If you change the capacity range from 8 to 40.5 ACUs, now the entire cluster consumes 16 ACUs when idle, and up to 81 ACUs when fully utilized.

Aurora automatically sets certain parameters for Aurora serverless DB instances to values that depend on the maximum ACU value in the capacity range. For the list of such parameters, see [Maximum connections for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.max-connections). For static parameters that rely on this type of calculation, the value is evaluated again when you reboot the DB instance. Thus, you can update the value of such parameters by rebooting the DB instance after changing the capacity range. To check whether you need to reboot your DB instance to pick up such parameter changes, check the `ParameterApplyStatus` attribute of the DB instance. A value of `pending-reboot` indicates that rebooting will apply changes to some parameter values.

### Console
<a name="aurora-serverless-v2.setting-capacity.console"></a>

You can set the capacity range of a cluster that contains Aurora serverless DB instances with the AWS Management Console.

When you use the console, you set the capacity range for the cluster at the time that you add the first Aurora serverless DB instance to that cluster. You might do so when you choose the **Serverless v2** DB instance class for the writer DB instance when you create the cluster. Or you might do so when you choose the **Serverless** DB instance class when you add an Aurora serverless reader DB instance to the cluster. Or you might do so when you convert an existing provisioned DB instance in the cluster to the **Serverless** DB instance class. For the full versions of those procedures, see [Creating an Aurora serverless writer DB instance](aurora-serverless-v2.create.md#aurora-serverless-v2-adding-writer), [Adding an Aurora serverless reader](#aurora-serverless-v2-adding-reader), and [Converting a provisioned writer or reader to Aurora serverless](#aurora-serverless-v2-converting-from-provisioned).

Whatever capacity range that you set at the cluster level applies to all Aurora serverless DB instances in your cluster. The following image shows a cluster with multiple Aurora serverless reader DB instances. Each has an identical capacity range of 2–64 ACUs.

![Cluster with multiple Aurora serverless reader DB instances.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_settings_identical_all_instances_in_tree_view.png)


**To modify the capacity range of an Aurora serverless cluster**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose the cluster containing your Aurora serverless DB instances from the list. The cluster must already contain at least one Aurora serverless DB instance. Otherwise, Aurora doesn't show the **Capacity range** section.

1. For **Actions**, choose **Modify**.

1. In the **Capacity range** section, choose the following:

   1. Enter a value for **Minimum ACUs**. The console shows the allowed range of values. You can choose a minimum capacity from 0 to 256 ACUs. You can choose a maximum capacity from 1 to 256 ACUs. You can adjust the capacity values in increments of 0.5 ACU. The available capacity range depends on both your DB engine version and the platform version.

   1. Enter a value for **Maximum ACUs**. This value must be greater than or equal to **Minimum ACUs**. The console shows the allowed range of values. The following figure shows that choice.  
![Modifying the DB cluster capacity.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/sv2_capacity_settings_256_acus.png)

1. Choose **Continue**. The **Summary of modifications** page appears.

1. Choose **Apply immediately**.

   The capacity modification takes place immediately, regardless of whether you choose to apply it immediately or during the next scheduled maintenance window.

1. Choose **Modify cluster** to accept the summary of modifications. You can also choose **Back** to modify your changes or **Cancel** to discard your changes.

### AWS CLI
<a name="aurora-serverless-v2.setting-capacity.cli"></a>

To set the capacity of a cluster where you intend to use Aurora serverless DB instances using the AWS CLI, run the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) AWS CLI command. Specify the `--serverless-v2-scaling-configuration` option. The cluster might already contain one or more Aurora serverless DB instances, or you can add the DB instances later. Valid values for the `MinCapacity` and `MaxCapacity` fields include the following:
+ `0`, `0.5`, `1`, `1.5`, `2`, and so on, in steps of 0.5, up to a maximum of 256. The minimum ACU value of 0 is only available for the Aurora versions that support the auto-pause feature. 

The maximum available capacity depends on both your DB engine version and the platform version.

In this example, you set the ACU range of an Aurora DB cluster named `sample-cluster` to a minimum of `48.5` and a maximum of 64.

```
aws rds modify-db-cluster --db-cluster-identifier sample-cluster \
  --serverless-v2-scaling-configuration MinCapacity=48.5,MaxCapacity=64
```

The capacity modification takes place immediately, regardless of whether you choose to apply it immediately or during the next scheduled maintenance window.

After doing so, you can add Aurora serverless DB instances to the cluster and each new DB instance can scale between 48.5 and 64 ACUs. The new capacity range also applies to any Aurora serverless DB instances that were already in the cluster. The DB instances scale up or down if necessary to fall within the new capacity range.

For additional examples of setting the capacity range using the CLI, see [Choosing the Aurora serverless capacity range for an Aurora cluster](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2-examples-setting-capacity-range-for-cluster). 

To modify the scaling configuration of an Aurora Serverless DB cluster using the AWS CLI, run the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) AWS CLI command. Specify the `--serverless-v2-scaling-configuration` option to configure the minimum capacity and maximum capacity. Valid capacity values include the following:
+ Aurora MySQL: `0`, `0.5`, `1`, `1.5`, `2`, and so on, in increments of 0.5 ACUs up to a maximum of `256`.
+ Aurora PostgreSQL: `0`, `0.5`, `1`, `1.5`, `2`, and so on, in increments of 0.5 ACUs up to a maximum of `256`.
+  The minimum ACU value of 0 is only available for the Aurora versions that support the auto-pause feature. 

In the following example, you modify the scaling configuration of an Aurora serverless DB instance named `sample-instance` that's part of a cluster named `sample-cluster`.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster --db-cluster-identifier sample-cluster \
--serverless-v2-scaling-configuration MinCapacity=8,MaxCapacity=64
```

For Windows:

```
aws rds modify-db-cluster --db-cluster-identifier sample-cluster ^
--serverless-v2-scaling-configuration MinCapacity=8,MaxCapacity=64
```

### RDS API
<a name="aurora-serverless-v2.setting-capacity.api"></a>

You can set the capacity of an Aurora DB instance with the [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) API operation. Specify the `ServerlessV2ScalingConfiguration` parameter. Valid values for the `MinCapacity` and `MaxCapacity` fields include the following:
+ `0`, `0.5`, `1`, `1.5`, `2`, and so on, in steps of 0.5, up to a maximum of 256. The minimum ACU value of 0 is only available for the Aurora versions that support the auto-pause feature. 

You can modify the scaling configuration of a cluster containing Aurora serverless DB instances with the [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) API operation. Specify the `ServerlessV2ScalingConfiguration` parameter to configure the minimum capacity and the maximum capacity. Valid capacity values include the following:
+ Aurora MySQL: `0`, `0.5`, `1`, `1.5`, `2`, and so on, in increments of 0.5 ACUs up to a maximum of `256`.
+ Aurora PostgreSQL: `0`, `0.5`, `1`, `1.5`, `2`, and so on, in increments of 0.5 ACUs up to a maximum of `256`.
+  The minimum ACU value of 0 is only available for the Aurora versions that support the auto-pause feature. 

The maximum available capacity depends on both your DB engine version and the platform version.

The capacity modification takes place immediately, regardless of whether you choose to apply it immediately or during the next scheduled maintenance window.

### Upgrading your Aurora serverless DB cluster to allow scaling to 256 ACUs
<a name="setting-256-acus"></a>

In some cases, when you try to scale your Aurora serverless DB cluster to capacities greater than 128 ACUs, you receive an error message. The error message tells you which instances are incompatible with the new scaling range. This highlights the important relationship between your capacity range, DB engine version, and platform version.

The inability to scale greater than 128 ACUs can happen for one of two reasons:
+ Older DB engine version – Upgrade the DB engine version to one that supports 256 ACUs. For more information, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity).
+ Older platform version – Upgrade the platform for your Aurora serverless DB cluster. You can do this in one of the following ways:
  + Stop and restart the DB cluster. When the cluster restarts, it will be on the latest platform version capable which may be capable of a higher ACU maximum.

    However, stopping and starting a DB cluster incurs some downtime, usually several minutes. For more information, see [Stopping and starting an Amazon Aurora DB cluster](aurora-cluster-stop-start.md).
  + Use a blue/green deployment. For more information, see [Overview of Amazon Aurora Blue/Green Deployments](blue-green-deployments-overview.md).

    1. Create a blue/green deployment. For more information, see [Creating a blue/green deployment in Amazon Aurora](blue-green-deployments-creating.md).

    1. Confirm that you can set the maximum capacity for the staging (green) environment to 256 ACUs.

    1. Switch over to the green environment. For more information, see [Switching a blue/green deployment in Amazon Aurora](blue-green-deployments-switching.md).

    1. Delete the original DB cluster.
**Note**  
If you maintain your database credentials in AWS Secrets Manager, you can't use blue/green deployments.
Aurora Global Database doesn't support blue/green deployments.
**Important:** Once you upgrade to a newer platform version, you cannot downgrade to a previous version.

## Checking the capacity range for Aurora serverless
<a name="aurora-serverless-v2-checking-capacity"></a>

 The procedure to check the capacity range for your Aurora serverless cluster requires that you first set a capacity range. If you haven't done so, follow the procedure in [Setting the Aurora serverless capacity range for a cluster](#aurora-serverless-v2-setting-acus). 

 Whatever capacity range you set at the cluster level applies to all Aurora serverless DB instances in your cluster. The following image shows a cluster with multiple Aurora serverless DB instances. Each has an identical capacity range. 

![Cluster details for multiple Aurora serverless DB instances.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_settings_identical_all_instances_in_tree_view.png)


 You can also view the details page for any Aurora serverless DB instance in the cluster. DB instances' capacity range appears on the **Configuration** tab. 

![Instance type section, part of DB instance configuration user interface.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_settings_shown_for_serverless_instance.png)


 You can also see the current capacity range for the cluster on the **Modify** page for the cluster. At that point, you can change the capacity range. For all the ways that you can set or change the capacity range, see [Setting the Aurora serverless capacity range for a cluster](#aurora-serverless-v2-setting-acus). 

### Checking the current capacity range for an Aurora cluster
<a name="aurora-serverless-v2-examples-checking-cluster-capacity-range"></a>

 You can check the capacity range that's configured for Aurora serverless DB instances in a cluster by examining the `ServerlessV2ScalingConfiguration` attribute for the cluster. The following AWS CLI example shows a cluster with a minimum capacity of 0.5 Aurora capacity units (ACUs) and a maximum capacity of 16 ACUs. 

```
$ aws rds describe-db-clusters --db-cluster-identifier serverless-v2-64-acu-cluster \
  --query 'DBClusters[*].[ServerlessV2ScalingConfiguration]'
[
    [
        {
            "MinCapacity": 0.5,
            "MaxCapacity": 16.0
        }
    ]
]
```

## Checking the platform version for an existing Aurora serverless cluster
<a name="aurora-serverless-v2-checking-platform-version"></a>

### Console
<a name="aurora-serverless-v2-checking-platform-version-con"></a>

The platform version is displayed in the Instance Configuration section of the instance.

![Platform version in the Instance Configuration section.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-serverless-v2-platform-version.png)


### AWS CLI
<a name="aurora-serverless-v2-checking-platform-version-cli"></a>

You can use the `describe-db-clusters` command to check the platform version for existing cluster(s).

**Example**  

```
1. aws rds describe-db-clusters \
2.     --db-cluster-identifier {{mydbcluster}}
```

### Checking the default platform version
<a name="aurora-serverless-v2-checking-default-platform-version"></a>

#### AWS CLI
<a name="aurora-serverless-v2-checking-default-platform-version-cli"></a>

You can use the `describe-serverless-v2-platform-versions` command to check the details of a platform version or to check the default platform version that you will get when you create a new cluster.

**Example**  

```
 1. $ aws rds describe-serverless-v2-platform-versions 
 2. {
 3.     "ServerlessV2PlatformVersions": [
 4.         {
 5.             "Engine": "aurora-postgresql",
 6.             "ServerlessV2PlatformVersion": "3",
 7.             "ServerlessV2PlatformVersionDescription": "Version 3 powered by Graviton 3 processors offering scaling up to 256 ACUs, and performance improvement up to 30% compared to version 2"
 8.             "ServerlessV2FeatureSupport": {
 9.                 "MinCapacity": 0
10.                 "MaxCapacity": 256
11.             },
12.             "Status": "available",
13.             "IsDefault": True
14.         },
15.         ...
16.     ]
17. }
18. 
19. # describing the default platform version for an engine
20. $ aws rds describe-serverless-v2-platform-versions --engine aurora-postgresql --default-only
21. {
22.     "ServerlessV2PlatformVersions": [
23.         {
24.             "Engine": "aurora-postgresql",
25.             "ServerlessV2PlatformVersion": "3",
26.             "ServerlessV2PlatformVersionDescription": "Version 3 powered by Graviton 3 processors offering scaling up to 256 ACUs, and performance improvement up to 30% compared to version 2"
27.             "ServerlessV2FeatureSupport": {
28.                 "MinCapacity": 0
29.                 "MaxCapacity": 256
30.             },
31.             "Status": "available",
32.             "IsDefault": True
33.         }
34.     ]
35. }
```

### Checking for pending platform version upgrades
<a name="aurora-serverless-v2-checking-pending-platform-version-upgrades"></a>

 You can use the `describe-pending-maintenance-actions` command to check whether there are any pending platform version upgrades for your Aurora serverless DB clusters. 

 To check for pending upgrades on a specific cluster, use the `--resource-identifier` parameter to specify the Amazon Resource Name (ARN) of your DB cluster: 

**Example**  

```
1. aws rds describe-pending-maintenance-actions \
2.     --resource-identifier arn:aws:rds:{{us-east-1}}:{{123456789012}}
3.     :cluster:{{my-serverless-cluster}}
```

#### Scheduling a platform version upgrade
<a name="aurora-serverless-v2-scheduling-platform-version-upgrade"></a>

 After you identify a pending platform version upgrade, you can use the `apply-pending-maintenance-action` command to schedule when the upgrade occurs. 

 To schedule a platform version upgrade, specify the following parameters: 
+ `--resource-identifier` – The ARN of your Aurora serverless DB cluster
+ `--apply-action` – Use `serverless-platform-version-update` to specify a platform version upgrade
+ `--opt-in-type` – Choose when to apply the upgrade:
  + `immediate` – Apply the upgrade immediately
  + `next-maintenance` – Apply the upgrade during your next schedule

## Adding an Aurora serverless reader
<a name="aurora-serverless-v2-adding-reader"></a>

 To add an Aurora serverless reader DB instance to your cluster, you follow the same general procedure as in [Adding Aurora Replicas to a DB cluster](aurora-replicas-adding.md). Choose the **Serverless v2** instance class for the new DB instance. 

 If the reader DB instance is the first Aurora serverless DB instance in the cluster, you also choose the capacity range. This setting applies to this reader DB instance and to any other Aurora serverless DB instances that you add to the cluster. Each Aurora serverless DB instance can scale between the minimum and maximum ACU values. 

 If any other Aurora serverless instances already exist in the cluster, the **Add reader** dialog shows the current capacity range for the cluster. In that case, you can't change the capacity. The following image shows the report of the current cluster capacity. 

![Instance configuration user interface for Aurora serverless.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_settings_settable_for_add_reader_modify_instance.png)


 If you already added any Aurora serverless DB instances to the cluster, adding another Aurora serverless reader DB instance shows you the current capacity range. The following image shows those read-only controls. 

![Capacity settings for Aurora serverless shown in Add reader interface.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_settings_fixed_for_add_reader_modify_instance.png)


 If you want to change the capacity range for the cluster, follow the procedure in [Setting the Aurora serverless capacity range for a cluster](#aurora-serverless-v2-setting-acus). 

 For clusters containing more than one reader DB instance, the failover priority of each Aurora serverless reader DB instance plays an important part in how that DB instance scales up and down. You can't specify the priority when you initially create the cluster. Keep this property in mind when you add a second reader or later DB instance to your cluster. For more information, see [Choosing the promotion tier for an Aurora serverless reader](#aurora-serverless-v2-choosing-promotion-tier). 

 For other ways that you can see the current capacity range for a cluster, see [Checking the capacity range for Aurora serverless](#aurora-serverless-v2-checking-capacity). 

## Converting a provisioned writer or reader to Aurora serverless
<a name="aurora-serverless-v2-converting-from-provisioned"></a>

 You can convert a provisioned DB instance to use Aurora serverless. To do so, you follow the procedure in [Modifying a DB instance in a DB cluster](Aurora.Modifying.md#Aurora.Modifying.Instance). The cluster must meet the requirements in [Requirements and limitations for Aurora serverless](aurora-serverless-v2.requirements.md). For example, Aurora serverless DB instances require that the cluster be running certain minimum engine versions. 

 Suppose that you are converting a running provisioned cluster to take advantage of Aurora serverless. In that case, you can minimize downtime by converting a DB instance to Aurora serverless as the first step in the switchover process. For the full procedure, see [Converting a provisioned writer or reader to Aurora serverless](#aurora-serverless-v2-converting-from-provisioned). 

 If the DB instance that you convert is the first Aurora serverless DB instance in the cluster, you choose the capacity range for the cluster as part of the **Modify** operation. This capacity range applies to each Aurora serverless DB instance that you add to the cluster. The following image shows the page where you specify the minimum and maximum Aurora capacity units (ACUs). 

![Instance configuration user interface.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_settings_settable_for_add_reader_modify_instance.png)


 For details about the significance of the capacity range, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity). 

 If the cluster already contains one or more Aurora serverless DB instances, you see the existing capacity range during the **Modify** operation. The following image shows an example of that information panel. 

![Capacity range information panel.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_settings_fixed_for_add_reader_modify_instance.png)


 If you want to change the capacity range for the cluster after you add more Aurora serverless DB instances, follow the procedure in [Setting the Aurora serverless capacity range for a cluster](#aurora-serverless-v2-setting-acus). 

## Converting an Aurora serverless writer or reader to provisioned
<a name="aurora-serverless-v2-converting-to-provisioned"></a>

 You can convert an Aurora serverless DB instance to a provisioned DB instance. To do so, you follow the procedure in [Modifying a DB instance in a DB cluster](Aurora.Modifying.md#Aurora.Modifying.Instance). Choose a DB instance class other than **Serverless**. 

 You might convert an Aurora serverless DB instance to provisioned if it needs a larger capacity than is available with the maximum Aurora capacity units (ACUs) of an Aurora serverless DB instance. For example, the largest db.r5 and db.r6g DB instance classes have a larger memory capacity than an Aurora serverless DB instance can scale to. 

**Tip**  
 Some of the older DB instance classes such as db.r3 and db.t2 aren't available for the Aurora versions that you use with Aurora serverless. To see which DB instance classes you can use when converting an Aurora serverless DB instance to a provisioned one, see [Supported DB engines for DB instance classes](Concepts.DBInstanceClass.SupportAurora.md). 

 If you are converting the writer DB instance of your cluster from Aurora serverless to provisioned, you can follow the procedure in [Converting a provisioned writer or reader to Aurora serverless](#aurora-serverless-v2-converting-from-provisioned) but in reverse. Switch one of the reader DB instances in the cluster from Aurora serverless to provisioned. Then perform a failover to make that provisioned DB instance into the writer. 

 Any capacity range that you previously specified for the cluster remains in place, even if all Aurora serverless DB instances are removed from the cluster. If you want to change the capacity range, you can modify the cluster, as explained in [Setting the Aurora serverless capacity range for a cluster](#aurora-serverless-v2-setting-acus). 

## Pausing Aurora serverless DB instances
<a name="pause-when-inactive"></a>

 You can configure Aurora clusters to automatically pause and resume their Aurora serverless DB instances. For more information, see [Scaling to Zero ACUs with automatic pause and resume for Aurora serverless](aurora-serverless-v2-auto-pause.md). 

## Choosing the promotion tier for an Aurora serverless reader
<a name="aurora-serverless-v2-choosing-promotion-tier"></a>

 For clusters containing multiple Aurora serverless DB instances or a mixture of provisioned and Aurora serverless DB instances, pay attention to the promotion tier setting for each Aurora serverless DB instance. This setting controls more behavior for Aurora serverless DB instances than for provisioned DB instances. 

 In the AWS Management Console, you specify this setting using the **Failover priority** choice under **Additional configuration** for the **Create database**, **Modify instance**, and **Add reader** pages. You see this property for existing DB instances in the optional **Priority tier** column on the **Databases** page. You can also see this property on the details page for a DB cluster or DB instance. 

 For provisioned DB instances, the choice of tier 0–15 determines only the order in which Aurora chooses which reader DB instance to promote to the writer during a failover operation. For Aurora serverless reader DB instances, the tier number also determines whether the DB instance scales up to match the capacity of the writer DB instance or scales independently based on its own workload. Aurora serverless reader DB instances in tier 0 or 1 are kept at a minimum capacity at least as high as the writer DB instance. That way, they are ready to take over from the writer DB instance in case of a failover. If the writer DB instance is a provisioned DB instance, Aurora estimates the equivalent Aurora serverless capacity. It uses that estimate as the minimum capacity for the Aurora serverless reader DB instance. 

 Aurora serverless reader DB instances in tiers 2–15 don't have the same constraint on their minimum capacity. When they are idle, they can scale down to the minimum Aurora capacity unit (ACU) value specified in the cluster's capacity range. 

 The following Linux AWS CLI example shows how to examine the promotion tiers of all the DB instances in your cluster. The final field includes a value of `True` for the writer DB instance and `False` for all the reader DB instances. 

```
$ aws rds describe-db-clusters --db-cluster-identifier promotion-tier-demo \
  --query 'DBClusters[*].DBClusterMembers[*].[PromotionTier,DBInstanceIdentifier,IsClusterWriter]' \
  --output text

1   instance-192  True
1   tier-01-4840  False
10  tier-10-7425  False
15  tier-15-6694  False
```

 The following Linux AWS CLI example shows how to change the promotion tier of a specific DB instance in your cluster. The commands first modify the DB instance with a new promotion tier. Then they wait for the DB instance to become available again and confirm the new promotion tier for the DB instance. 

```
$ aws rds modify-db-instance --db-instance-identifier instance-192 --promotion-tier 0
$ aws rds wait db-instance-available --db-instance-identifier instance-192
$ aws rds describe-db-instances --db-instance-identifier instance-192 \
  --query '*[].[PromotionTier]' --output text
0
```

 For more guidance about specifying promotion tiers for different use cases, see [Aurora serverless scaling](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.scaling). 

## Using TLS/SSL with Aurora serverless
<a name="aurora-serverless-v2.tls"></a>

 Aurora serverless can use the Transport Layer Security/Secure Sockets Layer (TLS/SSL) protocol to encrypt communications between clients and your Aurora serverless DB instances. It supports TLS/SSL versions 1.0, 1.1, and 1.2. For general information about using TLS/SSL with Aurora, see [TLS connections to Aurora MySQL DB clusters](AuroraMySQL.Security.md#AuroraMySQL.Security.SSL). 

 To learn more about connecting to Aurora MySQL database with the MySQL client, see [Connecting to a DB instance running the MySQL database engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html). 

 Aurora serverless supports all TLS/SSL modes available to the MySQL client (`mysql`) and PostgreSQL client (`psql`), including those listed in the following table. 


|  Description of TLS/SSL mode  |  mysql  |  psql  | 
| --- | --- | --- | 
|  Connect without using TLS/SSL.  |  DISABLED  |  disable  | 
|  Try the connection using TLS/SSL first, but fall back to non-SSL if necessary.  |  PREFERRED  |  prefer (default)  | 
|  Enforce using TLS/SSL.  |  REQUIRED  |  require  | 
|  Enforce TLS/SSL and verify the certificate authority (CA).  |  VERIFY\_CA  |  verify-ca  | 
|  Enforce TLS/SSL, verify the CA, and verify the CA hostname.  |  VERIFY\_IDENTITY  |  verify-full  | 

 Aurora serverless uses wildcard certificates. If you specify the "verify CA" or the "verify CA and CA hostname" option when using TLS/SSL, first download the [Amazon root CA 1 trust store](https://www.amazontrust.com/repository/AmazonRootCA1.pem) from Amazon Trust Services. After doing so, you can identify this PEM-formatted file in your client command. To do so using the PostgreSQL client, do the following. 

For Linux, macOS, or Unix:

```
psql 'host={{endpoint}} user={{user}} sslmode=require sslrootcert=amazon-root-CA-1.pem dbname={{db-name}}'
```

 To learn more about working with the Aurora PostgreSQL database using the Postgres client, see [Connecting to a DB instance running the PostgreSQL database engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html). 

 For more information about connecting to Aurora DB clusters in general, see [Connecting to an Amazon Aurora DB cluster](Aurora.Connecting.md). 

### Supported cipher suites for connections to Aurora serverless DB clusters
<a name="aurora-serverless-v2.tls.cipher-suites"></a>

By using configurable cipher suites, you can have more control over the security of your database connections. You can specify a list of cipher suites that you want to allow to secure client TLS/SSL connections to your database. With configurable cipher suites, you can control the connection encryption that your database server accepts. Doing this prevents the use of ciphers that aren't secure or that are no longer used.

Aurora serverless DB clusters that are based on Aurora MySQL support the same cipher suites as Aurora MySQL provisioned DB clusters. For information about these cipher suites, see [Configuring cipher suites for connections to Aurora MySQL DB clusters](AuroraMySQL.Security.md#AuroraMySQL.Security.SSL.ConfiguringCipherSuites).

Aurora serverless DB clusters that are based on Aurora PostgreSQL support the same cipher suites as Aurora PostgreSQL provisioned DB clusters. For information about these cipher suites, see [Configuring cipher suites for connections to Aurora PostgreSQL DB clusters](AuroraPostgreSQL.Security.md#AuroraPostgreSQL.Security.SSL.ConfiguringCipherSuites).

## Viewing Aurora serverless writers and readers
<a name="aurora-serverless-v2.viewing"></a>

 You can view the details of Aurora serverless DB instances in the same way that you do for provisioned DB instances. To do so, follow the general procedure from [Viewing an Amazon Aurora DB cluster](accessing-monitoring.md#Aurora.Viewing). A cluster might contain all Aurora serverless DB instances, all provisioned DB instances, or some of each. 

 After you create one or more Aurora serverless DB instances, you can view which DB instances are type **Serverless** and which are type **Instance**. You can also view the minimum and maximum Aurora capacity units (ACUs) that the Aurora serverless DB instance can use. Each ACU is a combination of processing (CPU) and memory (RAM) capacity. This capacity range applies to each Aurora serverless DB instance in the cluster. For the procedure to check the capacity range of a cluster or any Aurora serverless DB instance in the cluster, see [Checking the capacity range for Aurora serverless](#aurora-serverless-v2-checking-capacity). 

 In the AWS Management Console, Aurora serverless DB instances are marked under the **Size** column in the **Databases** page. Provisioned DB instances show the name of a DB instance class such as r6g.xlarge. The Aurora Serverless DB instances show **Serverless** for the DB instance class, along with the DB instance's minimum and maximum capacity. For example, you might see **Serverless v2 (4–64 ACUs)** or **Serverless v2 (1–40 ACUs)**. 

 You can find the same information on the **Configuration** tab for each Aurora serverless DB instance in the console. For example, you might see an **Instance type** section such as the following. Here, the **Instance type** value is **Serverless v2**, the **Minimum capacity** value is **2 ACUs (4 GiB)**, and the **Maximum capacity** value is **64 ACUs (128 GiB)**. 

![Instance type section, part of DB instance configuration user interface.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_settings_shown_for_serverless_instance.png)


 You can monitor the capacity of each Aurora serverless DB instance over time. That way, you can check the minimum, maximum, and average ACUs consumed by each DB instance. You can also check how close the DB instance came to its minimum or maximum capacity. To see such details in the AWS Management Console, examine the graphs of Amazon CloudWatch metrics on the **Monitoring** tab for the DB instance. For information about the metrics to watch and how to interpret them, see [Important Amazon CloudWatch metrics for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.viewing.monitoring). 

## Logging for Aurora serverless
<a name="aurora-serverless-v2.logging"></a>

 To turn on database logging, you specify the logs to enable using configuration parameters in your custom parameter group. 

 For Aurora MySQL, you can enable the following logs. 


|  Aurora MySQL  |  Description  | 
| --- | --- | 
|  `general_log`  |  Creates the general log. Set to 1 to turn on. Default is off (0).  | 
|  `log_queries_not_using_indexes`  |  Logs any queries to the slow query log that don't use an index. Default is off (0). Set to 1 to turn on this log.  | 
|  `long_query_time`  |  Prevents fast-running queries from being logged in the slow query log. Can be set to a float between 0 and 31536000. Default is 0 (not active).  | 
|  `server_audit_events`  |  The list of events to capture in the logs. Supported values are `CONNECT`, `QUERY`, `QUERY_DCL`, `QUERY_DDL`, `QUERY_DML`, and `TABLE`.  | 
|  `server_audit_logging`  |  Set to 1 to turn on server audit logging. If you turn this on, you can specify the audit events to send to CloudWatch by listing them in the `server_audit_events` parameter.  | 
|  `slow_query_log`  |  Creates a slow query log. Set to 1 to turn on the slow query log. Default is off (0).  | 

 For more information, see [Using Advanced Auditing with an Amazon Aurora MySQL DB cluster](AuroraMySQL.Auditing.md). 

 For Aurora PostgreSQL, you can enable the following logs on your Aurora serverless DB instances. 


|  Aurora PostgreSQL  |  Description  | 
| --- | --- | 
|  `log_connections`  |  Logs each successful connection.  | 
|  `log_disconnections`  |  Logs end of a session including duration.  | 
|  `log_lock_waits`  |  Default is 0 (off). Set to 1 to log lock waits.  | 
|  `log_min_duration_statement`  |  The minimum duration (in milliseconds) for a statement to run before it's logged.  | 
|  `log_min_messages`  |  Sets the message levels that are logged. Supported values are debug5, debug4, debug3, debug2, debug1, info, notice, warning, error, log, fatal, panic. To log performance data to the postgres log, set the value to debug1.  | 
|  `log_temp_files`  |  Logs the use of temporary files that are above the specified kilobytes (kB).  | 
|  `log_statement`  |  Controls the specific SQL statements that get logged. Supported values are `none`, `ddl`, `mod`, and `all`. Default is `none`.  | 

**Topics**
+ [Logging with Amazon CloudWatch](#aurora-serverless-v2.how-it-works.logging)
+ [Viewing Aurora serverless logs in Amazon CloudWatch](#aurora-serverless-v2.logging.monitoring)
+ [Monitoring capacity with Amazon CloudWatch](#aurora-serverless-v2.how-it-works.logging.monitoring)
+ [Monitoring Aurora serverless pause and resume activity](#autopause-logging-instance-log)

### Logging with Amazon CloudWatch
<a name="aurora-serverless-v2.how-it-works.logging"></a>

 After you use the procedure in [Logging for Aurora serverless](#aurora-serverless-v2.logging) to choose which database logs to turn on, you can choose which logs to upload ("publish") to Amazon CloudWatch. 

 You can use Amazon CloudWatch to analyze log data, create alarms, and view metrics. By default, error logs for Aurora serverless are enabled and automatically uploaded to CloudWatch. You can also upload other logs from Aurora serverless DB instances to CloudWatch. 

 Then you choose which of those logs to upload to CloudWatch, by using the **Log exports** settings in the AWS Management Console or the `--enable-cloudwatch-logs-exports` option in the AWS CLI. 

 You can choose which of your Aurora serverless logs to upload to CloudWatch. For more information, see [Using Advanced Auditing with an Amazon Aurora MySQL DB cluster](AuroraMySQL.Auditing.md). 

 As with any type of Aurora DB cluster, you can't modify the default DB cluster parameter group. Instead, create your own DB cluster parameter group based on a default parameter for your DB cluster and engine type. We recommend that you create your custom DB cluster parameter group before creating your Aurora serverless DB cluster, so that it's available to choose when you create a database on the console. 

**Note**  
 For Aurora serverless, you can create both DB cluster and DB parameter groups. 

### Viewing Aurora serverless logs in Amazon CloudWatch
<a name="aurora-serverless-v2.logging.monitoring"></a>

 After you use the procedure in [Logging with Amazon CloudWatch](#aurora-serverless-v2.how-it-works.logging) to choose which database logs to turn on, you can view the contents of the logs. 

 For more information on using CloudWatch with Aurora MySQL and Aurora PostgreSQL logs, see [Monitoring log events in Amazon CloudWatch](AuroraMySQL.Integrating.CloudWatch.md#AuroraMySQL.Integrating.CloudWatch.Monitor) and [Publishing Aurora PostgreSQL logs to Amazon CloudWatch Logs](AuroraPostgreSQL.CloudWatch.md). 

**To view logs for your Aurora serverless DB cluster**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1.  Choose your AWS Region. 

1.  Choose **Log groups**. 

1.  Choose your Aurora serverless DB cluster log from the list. The log naming pattern is as follows. 

   ```
   /aws/rds/cluster/{{cluster-name}}/{{log_type}}
   ```

**Note**  
 For Aurora MySQL–compatible Aurora serverless DB clusters, the error log includes buffer pool scaling events even when there are no errors. 

### Monitoring capacity with Amazon CloudWatch
<a name="aurora-serverless-v2.how-it-works.logging.monitoring"></a>

 With Aurora serverless, you can use CloudWatch to to monitor the capacity and utilization of all the Aurora serverless DB instances in your cluster. You can view instance-level metrics to check the capacity of each Aurora serverless DB instance as it scales up and down. You can also compare the capacity-related metrics to other metrics to see how changes in workloads affect resource consumption. For example, you can compare `ServerlessDatabaseCapacity` to `DatabaseUsedMemory`, `DatabaseConnections`, and `DMLThroughput` to assess how your DB cluster is responding during operations. For details about the capacity-related metrics that apply to Aurora serverless, see [Important Amazon CloudWatch metrics for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.viewing.monitoring). 

**To monitor your Aurora serverless DB cluster's capacity**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1.  Choose **Metrics**. All available metrics appear as cards in the console, grouped by service name. 

1.  Choose **RDS**. 

1.  (Optional) Use the **Search** box to find the metrics that are especially important for Aurora serverless: `ServerlessDatabaseCapacity`, `ACUUtilization`, `CPUUtilization`, and `FreeableMemory`. 

 We recommend that you set up a CloudWatch dashboard to monitor your Aurora serverless DB cluster capacity using the capacity-related metrics. To learn how, see [Building dashboards with CloudWatch](https://docs.aws.amazon.com/autoscaling/application/userguide/monitoring-cloudwatch.html). 

 To learn more about using Amazon CloudWatch with Amazon Aurora, see [Publishing Amazon Aurora MySQL logs to Amazon CloudWatch Logs](AuroraMySQL.Integrating.CloudWatch.md). 

### Monitoring Aurora serverless pause and resume activity
<a name="autopause-logging-instance-log"></a>

 Aurora writes a separate log file for Aurora serverless DB instances with auto-pause enabled. Aurora writes to the log for each 10-minute interval that the instance isn't paused. Aurora retains up to seven of these logs, rotated daily. The current log file is named `instance.log`, and older logs are named using the pattern `instance.{{YYYY-MM-DD}}.{{N}}.log`. 

 This log is enabled by default for Aurora serverless DB instances with auto-pause enabled. You can view the contents of this log in the AWS Management Console or by using the AWS CLI or RDSP API. Currently, you can't upload this log to CloudWatch. 

 The events listed in [DB instance events](USER_Events.Messages.md#USER_Events.Messages.instance) provide a high-level overview of pause and resume activity, such as the following: 
+  When the instance begins to pause, and when it finishes pausing. 
+  When the instance begins to resume, and when it finishes resuming. 
+  Cases where the instance attempted to pause, but some condition prevented it from pausing. 

 The `instance.log` provides more granular detail about the reasons why an Aurora serverless instance might or might not be able to pause. 

 The log might indicate that an instance resumed for different reasons: 
+  **user activity**: A database connection request. This could be from an interactive client session, an RDS Data API call, or a request to download logs from the instance. 
+  **background activity**: A broad category that includes all the reasons why Aurora resumes an instance. For example, when a connection request to a reader instance causes the writer instance to resume, the log for the reader indicates user activity, while the log for the writer classifies that resume request as background activity. For the reasons why Aurora might resume an instance other than a user connection request, see [Resuming an auto-paused Aurora serverless instance](aurora-serverless-v2-auto-pause.md#auto-pause-waking). 

 When Aurora isn't aware of any conditions that would prevent the instance from pausing when the auto-pause interval expires, it periodically writes an informational message to the log. For clusters with only a single DB instance, the log contains this message: 

```
[INFO] No auto-pause blockers registered since {{time}}
```

 For clusters with multiple DB instances, the message is slightly different. That's because a writer might be unable to pause due to activity on any of the reader instances. If the activity on the reader finishes before the auto-pause interval expires on the writer, the writer is able to pause at the expected time. 

```
[INFO] No auto-pause blockers registered since {{time}}.
Database might be required to maintain compute capacity for high availability.
```

 If a pause operation starts, but a new database connection request arrives before the instance finishes pausing, the log contains this message: 

```
[INFO] Unable to pause database due to a new database activity
```

 If Aurora becomes aware of any conditions that definitely prevent the instance from pausing, the log contains this message that lists all such conditions: 

```
[INFO] Auto-pause blockers registered since {{time}}: {{list_of_conditions}}
```

 That way, Aurora doesn't prevent you from turning on replication, zero-ETL integration, Aurora Global Database, and so on in combination with the auto-pause feature. The log informs you when the use of such features might prevent auto-pause from taking effect. 

 The following are reasons why an Aurora serverless instance might exceed the auto-pause timeout interval, but be prevented from pausing: 
+  **database activity before auto-pause timeout**: The DB instance received a connection request before the timeout interval expired. 
+  **member of global database**: If the DB cluster is part of an Aurora global database, the Aurora serverless instances in the cluster don't pause. A cluster can change from a standalone cluster to a global database cluster. Thus, instances that formerly auto-paused might stop pausing, and report this reason in the log. Once a cluster becomes a member of a global database, it doesn't revert to a standalone cluster until you explicitly detach it. The primary cluster is still considered part of the global database even if you detach all of the secondary clusters. 
+  **replication capability configured**: The writer DB instance has engine-specific replication enabled, either binlog replication for MySQL or logical replication for PostgreSQL. This condition could also be caused by using another Aurora feature that requires turning on replication, such as zero-ETL integrations or Database Activity Streams (DAS). 
+  **continuous backup lag**: If the Aurora storage system hasn't finished applying the storage changes up to the current point in time, the writer instance doesn't pause until it catches up. This condition only affects the writer instance, and is expected to be relatively brief. 
+  **service or customer maintenance action**: If a maintenance operation starts, the DB instance won't pause again until that operation finishes. This condition includes a wide variety of operations that might be started by you or by Aurora, such as upgrades, cloning, changing configuration settings, upgrades, downloading log files, and so on. This event also happens when you request to delete an instance, and Aurora briefly resumes the instance as part of the deletion mechanism. 
+  **transient communication issue**: If Aurora can't determine whether the scaling configuration currently has a minimum capacity setting of zero ACUs, it doesn't pause the instance. This is expected to be a very rare occurrence. 