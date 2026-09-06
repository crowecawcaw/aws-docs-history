

# Creating a DB cluster that uses Aurora serverless
<a name="aurora-serverless-v2.create"></a>

To create an Aurora cluster where you can add Aurora serverless DB instances, you follow the same procedure as in [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md). With Aurora serverless, your clusters are interchangeable with provisioned clusters. You can have clusters where some DB instances use Aurora serverless and some DB instances are provisioned.

**Topics**
+ [Settings for Aurora serverless DB clusters](#aurora-serverless-v2.create-settings)
+ [Creating an Aurora serverless DB cluster](#aurora-serverless-v2.create-cluster)
+ [Creating an Aurora serverless writer DB instance](#aurora-serverless-v2-adding-writer)

## Settings for Aurora serverless DB clusters
<a name="aurora-serverless-v2.create-settings"></a>

Make sure that the cluster's initial settings meet the requirements listed in [Requirements and limitations for Aurora serverless](aurora-serverless-v2.requirements.md). Specify the following settings to make sure that you can add Aurora serverless DB instances to the cluster:

**AWS Region**  
Create the cluster in an AWS Region where Aurora serverless DB instances are available. For details about available Regions, see [Supported Regions and Aurora DB engines for Aurora serverless](Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.md).

**DB engine version**  
Choose an engine version that's compatible with Aurora serverless. For information about the Aurora serverless version requirements, see [Requirements and limitations for Aurora serverless](aurora-serverless-v2.requirements.md).

**DB instance class**  
If you create a cluster using the AWS Management Console, you choose the DB instance class for the writer DB instance at the same time. Choose the **Serverless** DB instance class. When you choose that DB instance class, you also specify the capacity range for the writer DB instance. That same capacity range applies to all other Aurora serverless DB instances that you add to that cluster.  
If you don't see the **Serverless** choice for the DB instance class, make sure that you chose a DB engine version that's supported for [Supported Regions and Aurora DB engines for Aurora serverless](Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.md).  
When you use the AWS CLI or the Amazon RDS API, the parameter that you specify for the DB instance class is `db.serverless`.

**Capacity range**  
Fill in the minimum and maximum Aurora capacity unit (ACU) values that apply to all the DB instances in the cluster. This option is available on both the **Create cluster** and **Add reader** console pages when you choose **Serverless** for the DB instance class.  
For the allowed capacity ranges for various DB engine versions, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity).  
If you don't see the minimum and maximum ACU fields, make sure that you chose the **Serverless** DB instance class for the writer DB instance.

If you initially create the cluster with a provisioned DB instance, you don't specify the minimum and maximum ACUs. In that case you can modify the cluster afterward to add that setting. You can also add an Aurora serverless reader DB instance to the cluster. You specify the capacity range as part of that process.

Until you specify the capacity range for your cluster, you can't add any Aurora serverless DB instances to the cluster using the AWS CLI or RDS API. If you try to add a Aurora serverless DB instance, you get an error. In the AWS CLI or the RDS API procedures, the capacity range is represented by the `ServerlessV2ScalingConfiguration` attribute.

For clusters containing more than one reader DB instance, the failover priority of each Aurora serverless reader DB instance plays an important part in how that DB instance scales up and down. You can't specify the priority when you initially create the cluster. Keep this property in mind when you add a second or later reader DB instance to your cluster. For more information, see [Choosing the promotion tier for an Aurora serverless reader](aurora-serverless-v2-administration.md#aurora-serverless-v2-choosing-promotion-tier).

## Creating an Aurora serverless DB cluster
<a name="aurora-serverless-v2.create-cluster"></a>

You can use the AWS Management Console, AWS CLI, or RDS API to create an Aurora serverless DB cluster.

### Console
<a name="aurora-serverless-v2-create.console"></a>

**To create a cluster with an Aurora serverless writer**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose **Create database**. On the page that appears, choose the following options:
   + For **Engine type**, choose **Aurora (MySQL Compatible)** or **Aurora (PostgreSQL Compatible)**.
   + For **Version**, choose one of the supported versions for [Supported Regions and Aurora DB engines for Aurora serverless](Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.md).

1. For **DB instance class**, select **Serverless v2**.

1. For **Capacity range**, you can accept the default range. Or you can choose other values for minimum and maximum capacity units. You can choose from 0 ACUs minimum through 256 ACUs maximum, in increments of 0.5 ACU.

   For more information about Aurora serverless capacity units, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity) and [Performance and scaling for Aurora serverless](aurora-serverless-v2.setting-capacity.md). 

    Depending on the engine and version that you choose, the upper limit might be 128 ACUs, the lower limit might be 0.5 ACUs, or both. For details about the limit for each combination of Aurora engine and version, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity).   
![Instance configuration settings for Aurora serverless.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_setting_incl_nonzero_minimum.png)

    Choosing a minimum capacity of 0 ACUs enables the Aurora serverless automatic pause and resume capability. In that case, you can make an additional choice of how long the Aurora serverless DB instances wait with no database connections before automatically pausing. For information about the automatic pause and resume capability, see [Scaling to Zero ACUs with automatic pause and resume for Aurora serverless](aurora-serverless-v2-auto-pause.md).   
![Capacity setting Aurora serverless when the lower limit is 0 ACUs.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/serverless_v2_screencaps/serverless_v2_capacity_setting_incl_zero_minimum.png)

1. Choose any other DB cluster settings, as described in [Settings for Aurora DB clusters](Aurora.CreateInstance.md#Aurora.CreateInstance.Settings).

1. Choose **Create database** to create your Aurora DB cluster with an Aurora serverless DB instance as the writer instance, also known as the primary DB instance.

### CLI
<a name="aurora-serverless-v2-create.cli"></a>

To create a DB cluster that's compatible with Aurora serverless DB instances using the AWS CLI, you follow the CLI procedure in [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md). Include the following parameters in your `create-db-cluster` command:
+ --region {{AWS\_Region\_where\_Aurora serverless\_instances\_are\_available}}
+ --engine-version {{serverless\_v2\_compatible\_engine\_version}}
+ --serverless-v2-scaling-configuration MinCapacity={{minimum\_capacity}},MaxCapacity={{maximum\_capacity}} 

The following example shows the creation of an Aurora serverless DB cluster.

```
aws rds create-db-cluster \
    --db-cluster-identifier {{my-serverless-v2-cluster}} \
    --region {{eu-central-1}} \
    --engine {{aurora-mysql}} \
    --engine-version {{8.0.mysql_aurora.3.04.1}} \
    --serverless-v2-scaling-configuration MinCapacity={{1}},MaxCapacity={{4}} \
    --master-username {{myuser}} \
    --manage-master-user-password
```

**Note**  
When you create an Aurora serverless DB cluster using the AWS CLI, the engine mode appears in the output as `provisioned` rather than `serverless`. 

This example specifies the `--manage-master-user-password` option to generate the administrative password and manage it in Secrets Manager. For more information, see [Password management with Amazon Aurora and AWS Secrets Manager](rds-secrets-manager.md). Alternatively, you can use the `--master-password` option to specify and manage the password yourself.

For information about the Aurora serverless version requirements, see [Requirements and limitations for Aurora serverless](aurora-serverless-v2.requirements.md). For information about the allowed numbers for the capacity range and what those numbers represent, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity) and [Performance and scaling for Aurora serverless](aurora-serverless-v2.setting-capacity.md). 

To verify whether an existing cluster has the capacity settings specified, check the output of the `describe-db-clusters` command for the `ServerlessV2ScalingConfiguration` attribute. That attribute looks similar to the following.

```
"ServerlessV2ScalingConfiguration": {
    "MinCapacity": 1.5,
    "MaxCapacity": 24.0
}
```

**Tip**  
If you don't specify the minimum and maximum ACUs when you create the cluster, you can use the `modify-db-cluster` command afterward to add that setting. Until you do, you can't add any Aurora serverless DB instances to the cluster. If you try to add a `db.serverless` DB instance, you get an error.

### API
<a name="aurora-serverless-v2-create.api"></a>

To create a DB cluster that's compatible with Aurora serverless DB instances using the RDS API, you follow the API procedure in [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md). Choose the following settings. Make sure that your `CreateDBCluster` operation includes the following parameters:

```
EngineVersion {{serverless_v2_compatible_engine_version}}
ServerlessV2ScalingConfiguration with MinCapacity={{minimum_capacity}} and MaxCapacity={{maximum_capacity}}
```

For information about the Aurora serverless version requirements, see [Requirements and limitations for Aurora serverless](aurora-serverless-v2.requirements.md). For information about the allowed numbers for the capacity range and what those numbers represent, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity) and [Performance and scaling for Aurora serverless](aurora-serverless-v2.setting-capacity.md). 

To check if an existing cluster has the capacity settings specified, check the output of the `DescribeDBClusters` operation for the `ServerlessV2ScalingConfiguration` attribute. That attribute looks similar to the following.

```
"ServerlessV2ScalingConfiguration": {
    "MinCapacity": 1.5,
    "MaxCapacity": 24.0
}
```

**Tip**  
If you don't specify the minimum and maximum ACUs when you create the cluster, you can use the `ModifyDBCluster` operation afterward to add that setting. Until you do, you can't add any Aurora serverless DB instances to the cluster. If you try to add a `db.serverless` DB instance, you get an error.

## Creating an Aurora serverless writer DB instance
<a name="aurora-serverless-v2-adding-writer"></a>

 Although you specify the Aurora serverless capacity range when you create an Aurora cluster, you can choose whether to use Aurora serverless or provisioned for each DB instance in the cluster. To begin using Aurora serverless immediately in your DB cluster, add a writer DB instance that uses the `db.serverless` instance class. In the console, you typically make this choice as part of the workflow to create the DB cluster. Therefore, this procedure applies mostly when you do the setup through the CLI. 

### Console
<a name="aurora-serverless-v2-adding-writer.CON"></a>

When you create a DB cluster using the AWS Management Console, you specify the properties of the writer DB instance at the same time. To make the writer DB instance use Aurora serverless, choose the **Serverless** DB instance class.

Then you set the capacity range for the cluster by specifying the minimum and maximum Aurora capacity unit (ACU) values. These minimum and maximum values apply to each Aurora serverless DB instance in the cluster. For that procedure and the significance of the minimum and maximum capacity settings, see [Creating an Aurora serverless DB cluster](#aurora-serverless-v2.create-cluster). 

If you don't create an Aurora serverless DB instance when you first create the cluster, you can add one or more Aurora serverless DB instances later. To do so, follow the procedures in [Adding an Aurora serverless reader](aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader) and [Converting a provisioned writer or reader to Aurora serverless](aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned). You specify the capacity range at the time that you add the first Aurora serverless DB instance to the cluster. You can change the capacity range later by following the procedure in [Setting the Aurora serverless capacity range for a cluster](aurora-serverless-v2-administration.md#aurora-serverless-v2-setting-acus).

### CLI
<a name="aurora-serverless-v2-adding-writer.CLI"></a>

When you create a Aurora serverless DB cluster using the AWS CLI, you explicitly add the writer DB instance using the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) command. Include the following parameter:
+ `--db-instance-class db.serverless`

The following example shows the creation of an Aurora serverless writer DB instance.

```
aws rds create-db-instance \
    --db-cluster-identifier my-serverless-v2-cluster \
    --db-instance-identifier {{my-serverless-v2-instance}} \
    --db-instance-class db.serverless \
    --engine aurora-mysql
```