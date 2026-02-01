# Creating a DB cluster that uses Aurora Serverless v2

To create an Aurora cluster where you can add Aurora Serverless v2 DB instances, you follow the same procedure as
in [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md"). With Aurora Serverless v2, your
clusters are interchangeable with provisioned clusters. You can have clusters where some DB instances use Aurora Serverless v2 and some DB instances are provisioned.

###### Topics

- [Settings for Aurora Serverless v2 DB clusters](#aurora-serverless-v2.create-settings "#aurora-serverless-v2.create-settings")
- [Creating an Aurora Serverless v2 DB cluster](#aurora-serverless-v2.create-cluster "#aurora-serverless-v2.create-cluster")
- [Creating an Aurora Serverless v2 writer DB instance](#aurora-serverless-v2-adding-writer "#aurora-serverless-v2-adding-writer")

## Settings for Aurora Serverless v2 DB clusters

Make sure that the cluster's initial settings meet the requirements listed in [Requirements and limitations for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md"). Specify the following
settings to make sure that you can add Aurora Serverless v2 DB instances to the cluster:

**AWS Region**

Create the cluster in an AWS Region where Aurora Serverless v2 DB instances are available. For details about
available Regions, see [Supported
Regions and Aurora DB engines for Aurora Serverless v2](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

**DB engine version**

Choose an engine version that's compatible with Aurora Serverless v2. For information about the
Aurora Serverless v2 version requirements, see [Requirements and limitations for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

**DB instance class**

If you create a cluster using the AWS Management Console, you choose the DB instance class for the writer DB instance at the
same time. Choose the **Serverless** DB instance class. When you choose that DB instance class, you
also specify the capacity range for the writer DB instance. That same capacity range applies to all other
Aurora Serverless v2 DB instances that you add to that cluster.

If you don't see the **Serverless** choice for the DB instance class, make sure that you
chose a DB engine version that's supported for [Supported
Regions and Aurora DB engines for Aurora Serverless v2](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

When you use the AWS CLI or the Amazon RDS API, the parameter that you specify for the DB instance class is
`db.serverless`.

**Capacity range**

Fill in the minimum and maximum Aurora capacity unit (ACU) values that apply to all the DB instances in the
cluster. This option is available on both the **Create cluster** and **Add
reader** console pages when you choose **Serverless** for the DB instance
class.

For the allowed capacity ranges for various DB engine versions, see [Aurora Serverless v2 capacity](aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity "aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity").

If you don't see the minimum and maximum ACU fields, make sure that you chose the
**Serverless** DB instance class for the writer DB instance.

If you initially create the cluster with a provisioned DB instance, you don't specify the minimum and maximum ACUs. In
that case you can modify the cluster afterward to add that setting. You can also add an Aurora Serverless v2 reader DB instance to
the cluster. You specify the capacity range as part of that process.

Until you specify the capacity range for your cluster, you can't add any Aurora Serverless v2 DB instances to the cluster
using the AWS CLI or RDS API. If you try to add a Aurora Serverless v2 DB instance, you get an error. In the AWS CLI or the RDS API
procedures, the capacity range is represented by the `ServerlessV2ScalingConfiguration` attribute.

For clusters containing more than one reader DB instance, the failover priority of each Aurora Serverless v2 reader DB instance
plays an important part in how that DB instance scales up and down. You can't specify the priority when you initially
create the cluster. Keep this property in mind when you add a second or later reader DB instance to your cluster. For more
information, see [Choosing the promotion tier for an Aurora Serverless v2 reader](aurora-serverless-v2-administration.md#aurora-serverless-v2-choosing-promotion-tier "aurora-serverless-v2-administration.md#aurora-serverless-v2-choosing-promotion-tier").

## Creating an Aurora Serverless v2 DB cluster

You can use the AWS Management Console, AWS CLI, or RDS API to create an Aurora Serverless v2 DB cluster.

###### To create a cluster with an Aurora Serverless v2 writer

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose **Create database**. On the page that appears, choose the following options:
   - For **Engine type**, choose **Aurora (MySQL Compatible)** or
     **Aurora (PostgreSQL Compatible)**.
   - For **Version**, choose one of the supported versions for [Supported
     Regions and Aurora DB engines for Aurora Serverless v2](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

4. For **DB instance class**, select **Serverless v2**.
5. For **Capacity range**, you can accept the default range. Or you can choose other values for
   minimum and maximum capacity units. You can choose from 0 ACUs minimum through 256 ACUs maximum, in increments
   of 0.5 ACU.

For more information about Aurora Serverless v2 capacity units, see
[Aurora Serverless v2 capacity](aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity "aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity") and
[Performance and scaling for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

Depending on the engine and version that you choose, the upper limit might be 128 ACUs, the lower limit might
be 0.5 ACUs, or both. For details about the limit for each combination of Aurora engine and version, see
[Aurora Serverless v2 capacity](aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity "aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity").

![Instance configuration settings for Aurora Serverless v2.](images/serverless_v2_screencaps/serverless_v2_capacity_setting_incl_nonzero_minimum.png)

Choosing a minimum capacity of 0 ACUs enables the Aurora Serverless v2 automatic pause and resume capability.
In that case, you can make an additional choice of how long the Aurora Serverless v2 DB instances wait
with no database connections before automatically pausing. For information about the automatic pause
and resume capability, see
[Scaling to Zero ACUs with automatic pause and resume for Aurora Serverless v2](aurora-serverless-v2-auto-pause.md "aurora-serverless-v2-auto-pause.md").

![Capacity setting Aurora Serverless v2 when the lower limit is 0 ACUs.](images/serverless_v2_screencaps/serverless_v2_capacity_setting_incl_zero_minimum.png) 6. Choose any other DB cluster settings, as described in
[Settings for Aurora DB clusters](Aurora.md#Aurora.CreateInstance.Settings "Aurora.md#Aurora.CreateInstance.Settings"). 7. Choose **Create database** to create your Aurora DB cluster with an Aurora Serverless v2 DB
instance as the writer instance, also known as the primary DB instance.
To create a DB cluster that's compatible with Aurora Serverless v2 DB instances using the AWS CLI, you follow the CLI
procedure in [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md"). Include the following
parameters in your `create-db-cluster` command:

- --region `AWS_Region_where_Aurora Serverless v2_instances_are_available`
- --engine-version `serverless_v2_compatible_engine_version`
- --serverless-v2-scaling-configuration
  MinCapacity=`minimum_capacity`,MaxCapacity=`maximum_capacity`
  The following example shows the creation of an Aurora Serverless v2 DB cluster.

```
aws rds create-db-cluster \
    --db-cluster-identifier `my-serverless-v2-cluster` \
    --region `eu-central-1` \
    --engine `aurora-mysql` \
    --engine-version `8.0.mysql_aurora.3.04.1` \
    --serverless-v2-scaling-configuration MinCapacity=`1`,MaxCapacity=`4` \
    --master-username `myuser` \
    --manage-master-user-password
```

###### Note

When you create an Aurora Serverless v2 DB cluster using the AWS CLI, the engine mode appears in the output as
`provisioned` rather than `serverless`. The `serverless` engine mode refers to
Aurora Serverless v1.

This example specifies the `--manage-master-user-password` option to generate the administrative password and
manage it in Secrets Manager. For more information, see [Password management with
Amazon Aurora
and AWS Secrets Manager](rds-secrets-manager.md "rds-secrets-manager.md").
Alternatively, you can use the `--master-password` option to specify and manage the password yourself.

For information about the Aurora Serverless v2 version requirements, see
[Requirements and limitations for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").
For information about the allowed numbers for the capacity range and what those numbers represent, see
[Aurora Serverless v2 capacity](aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity "aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity")
and [Performance and scaling for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

To verify whether an existing cluster has the capacity settings specified, check the output of the
`describe-db-clusters` command for the `ServerlessV2ScalingConfiguration` attribute.
That attribute looks similar to the following.

```
"ServerlessV2ScalingConfiguration": {
    "MinCapacity": 1.5,
    "MaxCapacity": 24.0
}
```

###### Tip

If you don't specify the minimum and maximum ACUs when you create the cluster, you can use the
`modify-db-cluster` command afterward to add that setting. Until you do, you can't add any
Aurora Serverless v2 DB instances to the cluster. If you try to add a `db.serverless` DB instance,
you get an error.

To create a DB cluster that's compatible with Aurora Serverless v2 DB instances using the RDS API,
you follow the API procedure in [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").
Choose the following settings. Make sure that your `CreateDBCluster` operation includes
the following parameters:

```
EngineVersion `serverless_v2_compatible_engine_version`
ServerlessV2ScalingConfiguration with MinCapacity=`minimum_capacity` and MaxCapacity=`maximum_capacity`

```

For information about the Aurora Serverless v2 version requirements, see
[Requirements and limitations for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").
For information about the allowed numbers for the capacity range and what those numbers represent, see
[Aurora Serverless v2 capacity](aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity "aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity")
and [Performance and scaling for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

To check if an existing cluster has the capacity settings specified, check the output of the
`DescribeDBClusters` operation for the `ServerlessV2ScalingConfiguration` attribute. That
attribute looks similar to the following.

```
"ServerlessV2ScalingConfiguration": {
    "MinCapacity": 1.5,
    "MaxCapacity": 24.0
}
```

###### Tip

If you don't specify the minimum and maximum ACUs when you create the cluster, you can use the
`ModifyDBCluster` operation afterward to add that setting. Until you do, you can't add any
Aurora Serverless v2 DB instances to the cluster. If you try to add a `db.serverless` DB instance,
you get an error.

## Creating an Aurora Serverless v2 writer DB instance

Although you specify the Aurora Serverless v2 capacity range when you create an Aurora cluster, you can choose
whether to use Aurora Serverless v2 or provisioned for each DB instance in the cluster. To begin using
Aurora Serverless v2 immediately in your DB cluster, add a writer DB instance that uses the `db.serverless`
instance class. In the console, you typically make this choice as part of the workflow to create the DB cluster.
Therefore, this procedure applies mostly when you do the setup through the CLI.

When you create a DB cluster using the AWS Management Console, you specify the properties of the writer DB instance at the same time.
To make the writer DB instance use Aurora Serverless v2, choose the **Serverless** DB instance class.

Then you set the capacity range for the cluster by specifying the minimum and maximum Aurora capacity unit (ACU) values.
These minimum and maximum values apply to each Aurora Serverless v2 DB instance in the cluster.
For that procedure and the significance of the minimum and maximum capacity settings, see
[Creating an Aurora Serverless v2 DB cluster](#aurora-serverless-v2.create-cluster "#aurora-serverless-v2.create-cluster").

If you don't create an Aurora Serverless v2 DB instance when you first create the cluster, you can add
one or more Aurora Serverless v2 DB instances later. To do so, follow the procedures in
[Adding an Aurora Serverless v2 reader](aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader "aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader") and
[Converting a provisioned writer or reader to Aurora Serverless v2](aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned "aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned").
You specify the capacity range at the time that you add the first Aurora Serverless v2 DB instance to the cluster. You can change the capacity range later by following the
procedure in [Setting the Aurora Serverless v2 capacity range for a cluster](aurora-serverless-v2-administration.md#aurora-serverless-v2-setting-acus "aurora-serverless-v2-administration.md#aurora-serverless-v2-setting-acus").

When you create a Aurora Serverless v2 DB cluster using the AWS CLI, you explicitly add the writer DB instance using the
[create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command. Include the following parameter:

- `--db-instance-class db.serverless`
  The following example shows the creation of an Aurora Serverless v2 writer DB instance.

```
aws rds create-db-instance \
    --db-cluster-identifier my-serverless-v2-cluster \
    --db-instance-identifier `my-serverless-v2-instance` \
    --db-instance-class db.serverless \
    --engine aurora-mysql
```
