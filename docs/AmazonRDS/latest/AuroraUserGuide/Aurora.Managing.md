# Cloning a volume for an Amazon Aurora DB cluster

By using Aurora cloning, you can create a new cluster that initially shares the same data pages as the original, but is a separate
and independent volume. The process is designed to be fast and cost-effective. The new cluster with its associated data volume is
known as a _clone_. Creating a clone is faster and more space-efficient than physically copying the data using
other techniques, such as restoring a snapshot.

###### Topics

- [Overview of Aurora cloning](#Aurora.Clone.Overview "#Aurora.Clone.Overview")
- [Limitations of Aurora cloning](#Aurora.Managing.Clone.Limitations "#Aurora.Managing.Clone.Limitations")
- [How Aurora cloning works](#Aurora.Managing.Clone.Protocol "#Aurora.Managing.Clone.Protocol")
- [Creating an Amazon Aurora clone](#Aurora.Managing.Clone.create "#Aurora.Managing.Clone.create")
- [Cross-VPC cloning with Amazon Aurora](Aurora.Managing.Clone.md "Aurora.Managing.Clone.md")
- [Cross-account cloning with AWS RAM and Amazon Aurora](Aurora.Managing.Clone.md "Aurora.Managing.Clone.md")

## Overview of Aurora cloning

Aurora uses a _copy-on-write protocol_ to create a clone. This mechanism uses minimal additional
space to create an initial clone. When the clone is first created, Aurora keeps a single copy of the data that is used by the
source Aurora DB cluster and the new (cloned) Aurora DB cluster. Additional storage is allocated only when changes are made to
data (on the Aurora storage volume) by the source Aurora DB cluster or the Aurora DB cluster clone. To learn more about the
copy-on-write protocol, see [How Aurora cloning works](#Aurora.Managing.Clone.Protocol "#Aurora.Managing.Clone.Protocol").

Aurora cloning is especially useful for quickly setting up test environments using your
production data, without risking data corruption. You can use clones for many types of
applications, such as the following:

- Experiment with potential changes (schema changes and parameter group changes, for example) to assess all impacts.
- Run workload-intensive operations, such as exporting data or running analytical queries on the clone.
- Create a copy of your production DB cluster for development, testing, or other purposes.

You can create more than one clone from the same Aurora DB cluster. You can also create multiple clones from another
clone.

After creating an Aurora clone, you can configure the Aurora DB instances differently from the source Aurora DB cluster. For example, you might not
need a clone for development purposes to meet the same high availability requirements as the source production Aurora DB cluster. In this case, you can configure the clone
with a single Aurora DB instance rather than the multiple DB instances used by the Aurora DB cluster.

When you create a clone using a different deployment configuration from the source, the clone is created using the latest minor
version of the source's Aurora DB engine.

When you create clones from your Aurora DB clusters, the clones are created in your AWS account—the same account that
owns the source Aurora DB cluster. However, you can also share Aurora Serverless v2 and provisioned Aurora DB clusters and clones
with other AWS accounts. For more information, see [Cross-account cloning with AWS RAM and Amazon Aurora](Aurora.Managing.Clone.md "Aurora.Managing.Clone.md").

When you finish using the clone for your testing, development, or other purposes, you can
delete it.

## Limitations of Aurora cloning

Aurora cloning currently has the following limitations:

- You can create as many clones as you want, up to the maximum number of DB clusters allowed in the AWS Region.
- You can create up to 15 clones with copy-on-write protocol. After you have 15 clones, the next clone that you create is a full copy. The full-copy protocol acts like a point-in-time recovery.
- You can't create a clone in a different AWS Region from the source Aurora DB cluster.
- You can't create a clone from an Aurora DB cluster without the parallel query feature to a cluster that uses parallel query.
  To bring data into a cluster that uses parallel query, create a snapshot of the original
  cluster and restore it to the cluster that's using the parallel query feature.
- You can't create a clone from an Aurora DB cluster that has no DB instances.
  You can only clone Aurora DB clusters that have at least one DB instance.
- You can create a clone in a different virtual private cloud (VPC) than that of
  the Aurora DB cluster. If you do, the subnets of the VPCs must map to the same Availability
  Zones.
- You can create an Aurora provisioned clone from a provisioned Aurora DB cluster.
- Clusters with Aurora Serverless v2 instances follow the same rules as provisioned clusters.
- For Aurora Serverless v1:
  - You can create a provisioned clone from an Aurora Serverless v1 DB cluster.
  - You can create an Aurora Serverless v1 clone from an Aurora Serverless v1 or provisioned DB cluster.
  - You can't create an Aurora Serverless v1 clone from an unencrypted, provisioned Aurora DB cluster.
  - Cross-account cloning currently doesn't support cloning Aurora Serverless v1 DB clusters. For more
    information, see [Limitations of cross-account cloning](Aurora.Managing.Clone.md#Aurora.Managing.Clone.CrossAccount.Limitations "Aurora.Managing.Clone.md#Aurora.Managing.Clone.CrossAccount.Limitations").
  - A cloned Aurora Serverless v1 DB cluster has the same behavior and limitations as any Aurora Serverless v1 DB
    cluster. For more information, see [Using Amazon Aurora Serverless v1](aurora-serverless.md "aurora-serverless.md").
  - Aurora Serverless v1 DB clusters are always encrypted. When you clone an Aurora Serverless v1 DB
    cluster into a provisioned Aurora DB cluster, the provisioned Aurora DB cluster is encrypted. You can choose the
    encryption key, but you can't disable the encryption. To clone from a provisioned Aurora DB cluster to an
    Aurora Serverless v1, you must start with an encrypted provisioned Aurora DB cluster.

## How Aurora cloning works

Aurora cloning works at the storage layer of an Aurora DB cluster. It uses a
_copy-on-write_ protocol that's both fast and space-efficient in
terms of the underlying durable media supporting the Aurora storage volume. You can learn more
about Aurora cluster volumes in the [Overview of Amazon Aurora storage](Aurora.Overview.md#Aurora.Overview.Storage "Aurora.Overview.md#Aurora.Overview.Storage").

###### Topics

- [Understanding the copy-on-write protocol](#Aurora.Managing.Clone.Protocol.Before "#Aurora.Managing.Clone.Protocol.Before")
- [Deleting a source cluster volume](#Aurora.Managing.Clone.Deleting "#Aurora.Managing.Clone.Deleting")

### Understanding the copy-on-write protocol

An Aurora DB cluster stores data in pages in the underlying Aurora storage volume.

For example, in the following diagram you can find an Aurora DB cluster (A) that has four
data pages, 1, 2, 3, and 4. Imagine that a clone, B, is created from the Aurora DB cluster.
When the clone is created, no data is copied. Rather, the clone points to the same set of
pages as the source Aurora DB cluster.

![Amazon Aurora cluster volume with 4 pages for source cluster, A, and clone, B](images/aurora-cloning-copy-on-write-protocol-1.png)

When the clone is created, no additional storage is usually needed. The copy-on-write protocol uses the same segment on the physical
storage media as the source segment. Additional storage is required only if the capacity of the source segment isn't sufficient for
the entire clone segment. If that's the case, the source segment is copied to another physical device.

In the following diagrams, you can find an example of the copy-on-write protocol in
action using the same cluster A and its clone, B, as shown preceding. Let's say that
you make a change to your Aurora DB cluster (A) that results in a change to data held on page

1.  Instead of writing to the original page 1, Aurora creates a new page 1[A]. The Aurora DB
    cluster volume for cluster (A) now points to page 1[A], 2, 3, and 4, while the clone (B)
    still references the original pages.

![Amazon Aurora source DB cluster volume and its clone, both with changes.](images/aurora-cloning-copy-on-write-protocol-2.png)

On the clone, a change is made to page 4 on the storage volume. Instead of writing to the original page 4, Aurora creates a new page, 4[B].
The clone now points to pages 1, 2, 3, and to page 4[B], while the cluster (A) continues pointing to 1[A], 2, 3, and 4.

![Amazon Aurora source DB cluster volume and its clone, both with changes.](images/aurora-cloning-copy-on-write-protocol-3.png)

As more changes occur over time in both the source Aurora DB cluster volume and the clone, more storage is needed to
capture and store the changes.

### Deleting a source cluster volume

Initially, the clone volume shares the same data pages as the original volume
from which the clone is created. As long as the original volume exists, the clone volume
is only considered the owner of the pages that the clone created or modified. Thus, the
`VolumeBytesUsed` metric for the clone volume starts out small and only grows
as the data diverges between the original cluster and the clone. For pages that are identical
between the source volume and the clone, the storage charges apply only to the original cluster.
For more information about the `VolumeBytesUsed` metric, see
[Cluster-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.clusters "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.clusters").

When you delete a source cluster volume that has one or more clones associated with
it, the data in the cluster volumes of the clones isn't changed. Aurora preserves the
pages that were previously owned by the source cluster volume. Aurora redistributes
the storage billing for the pages that were owned by the deleted cluster. For
example, suppose that an original cluster had two clones and then the original cluster
was deleted. Half of the data pages owned by the original cluster would now be owned by
one clone. The other half of the pages would be owned by the other clone.

If you delete the original cluster, then as you create or delete more clones, Aurora continues
to redistribute ownership of the data pages among all the clones that share the same pages. Thus,
you might find that the value of the `VolumeBytesUsed` metric changes for the cluster volume of a clone.
The metric value can decrease as more clones are created and page ownership is spread across more
clusters. The metric value can also increase as clones are deleted and page ownership is assigned
to a smaller number of clusters. For information about how write operations affect data pages on clone volumes, see
[Understanding the copy-on-write protocol](#Aurora.Managing.Clone.Protocol.Before "#Aurora.Managing.Clone.Protocol.Before").

When the original cluster and the clones are owned by the same AWS account, all the storage charges for those
clusters apply to that same AWS account. If some of the clusters are cross-account clones, deleting the original
cluster can result in additional storage charges to the AWS accounts that own the cross-account clones.

For example, suppose that a cluster volume has 1000 used data pages before you create any clones. When you clone
that cluster, initially the clone volume has zero used pages. If the clone makes modifications to
100 data pages, only those 100 pages are stored on the clone volume and marked as used. The
other 900 unchanged pages from the parent volume are shared by both clusters. In this case,
the parent cluster has storage charges for 1000 pages and the clone volume for 100 pages.

If you delete the source volume, the storage charges for the clone include the
100 pages that it changed, plus the 900 shared pages from the original volume, for a total
of 1000 pages.

## Creating an Amazon Aurora clone

You can create a clone in the same AWS account as the source Aurora DB cluster. To do so,
you can use the AWS Management Console or the AWS CLI and the procedures following.

To allow another AWS account to create a clone or to share a clone with another AWS account, use the
procedures in [Cross-account cloning with AWS RAM and Amazon Aurora](Aurora.Managing.Clone.md "Aurora.Managing.Clone.md").

The following procedure describes how to clone an Aurora DB cluster using the
AWS Management Console.

Creating a clone using the AWS Management Console results in an Aurora DB cluster with one Aurora DB
instance.

These instructions apply for DB clusters owned by the same AWS account that is creating the clone.
If the DB cluster is owned by a different AWS account, see
[Cross-account cloning with AWS RAM and Amazon Aurora](Aurora.Managing.Clone.md "Aurora.Managing.Clone.md")
instead.

###### To create a clone of a DB cluster owned by your AWS account using the AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose your Aurora DB cluster from the list, and for **Actions**, choose
   **Create clone**.

![Creating a clone starts by selecting your Aurora DB cluster.](images/aurora-cloning-create-clone-1.png)

The Create clone page opens, where you can configure **Settings**, **Connectivity**,
and other options for the Aurora DB cluster clone. 4. For **DB instance identifier**, enter the name that you want to give to your cloned Aurora DB
cluster. 5. For Aurora Serverless v1 DB clusters, choose **Provisioned** or **Serverless** for **Capacity
type**.

You can choose **Serverless** only if the source Aurora DB cluster is an Aurora
Serverless v1 DB cluster or is a provisioned Aurora DB cluster that is encrypted. 6. For Aurora Serverless v2 or provisioned DB clusters, choose either **Aurora I/O-Optimized** or
**Aurora Standard** for **Cluster storage configuration**.

For more information, see [Storage configurations for Amazon Aurora DB clusters](Aurora.Overview.md#aurora-storage-type "Aurora.Overview.md#aurora-storage-type"). 7. Choose the DB instance size or DB cluster capacity:

    * For a provisioned clone, choose a **DB instance class**.



    ![To create a provisioned clone, specify the DB instance size.](images/aurora-cloning-create-clone-3-provisioned.png)

    You can accept the provided setting, or you can use a different DB instance class for your
     clone.
    * For an Aurora Serverless v1 or Aurora Serverless v2 clone, choose the **Capacity
     settings**.



    ![To create a Serverless clone from an Aurora DB cluster, specify the capacity.](images/aurora-cloning-create-clone-3-serverless.png)

    You can accept the provided settings, or you can change them for your clone.

8. Choose other settings as needed for your clone. To learn more about Aurora DB cluster and instance settings,
   see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").
9. Choose **Create clone**.
   When the clone is created, it's listed with your other Aurora DB clusters in the
   console **Databases** section and displays its current state. Your clone
   is ready to use when its state is **Available**.

Using the AWS CLI for cloning your Aurora DB cluster involves separate steps for creating the clone cluster and
adding one or more DB instances to it.

The `restore-db-cluster-to-point-in-time` AWS CLI command that you use results in an Aurora DB cluster
with the same storage data as the original cluster, but no Aurora DB instances. You create the DB instances
separately after the clone is available. You can choose the number of DB instances and their instance classes to
give the clone more or less compute capacity than the original cluster. The steps in the process are as follows:

1. Create the clone by using the
   [restore-db-cluster-to-point-in-time](../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md")
   CLI command.
2. Create the writer DB instance for the clone by using the
   [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") CLI command.
3. (Optional) Run additional [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md")
   CLI commands to add one or more reader instances to the clone cluster. Using reader instances helps improve
   the high availability and read scalability aspects of the clone. You might skip this step if you only intend
   to use the clone for development and testing.

###### Topics

- [Creating the clone](#Aurora.Managing.Clone.CLI.create-empty-clone "#Aurora.Managing.Clone.CLI.create-empty-clone")
- [Checking the status and getting clone details](#Aurora.Managing.Clone.CLI.check-status-get-details "#Aurora.Managing.Clone.CLI.check-status-get-details")
- [Creating the Aurora DB instance for your clone](#Aurora.Managing.Clone.CLI.create-db-instance "#Aurora.Managing.Clone.CLI.create-db-instance")
- [Parameters to use for cloning](#Aurora.Managing.Clone.CLI.parameter-summary "#Aurora.Managing.Clone.CLI.parameter-summary")

#### Creating the clone

Use the
`restore-db-cluster-to-point-in-time`
CLI command to create the initial clone cluster.

###### To create a clone from a source Aurora DB cluster

- Use the
  `restore-db-cluster-to-point-in-time`
  CLI command. Specify values for the following parameters. In this typical case, the clone uses the same
  engine mode as the original cluster, either provisioned or Aurora Serverless v1.
  - `--db-cluster-identifier` – Choose a meaningful name for your clone. You name the
    clone when you use the
    [restore-db-cluster-to-point-in-time](../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md")
    CLI command. You then pass the name of the clone in the
    [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") CLI command.
  - `--restore-type` – Use `copy-on-write` to create a clone of the source DB
    cluster. Without this parameter, the `restore-db-cluster-to-point-in-time` restores the
    Aurora DB cluster rather than creating a clone.
  - `--source-db-cluster-identifier` – Use the name of the source Aurora DB cluster that
    you want to clone.
  - `--use-latest-restorable-time` – This value points to the latest restorable volume
    data for the source DB cluster. Use it to create clones.

The following example creates a clone named `my-clone` from a cluster named
`my-source-cluster`.

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-to-point-in-time \
    --source-db-cluster-identifier `my-source-cluster` \
    --db-cluster-identifier `my-clone` \
    --restore-type copy-on-write \
    --use-latest-restorable-time
```

For Windows:

```
aws rds restore-db-cluster-to-point-in-time ^
    --source-db-cluster-identifier `my-source-cluster` ^
    --db-cluster-identifier `my-clone` ^
    --restore-type copy-on-write ^
    --use-latest-restorable-time
```

The command returns the JSON object containing details of the clone. Check to make sure that your cloned DB
cluster is available before trying to create the DB instance for your clone. For more information, see
[Checking the status and getting clone details](#Aurora.Managing.Clone.CLI.check-status-get-details "#Aurora.Managing.Clone.CLI.check-status-get-details").

For example, suppose you have a cluster named `tpch100g` that you want to clone. The following
Linux example creates a cloned cluster named `tpch100g-clone`, an Aurora Serverless v2 writer
instance named `tpch100g-clone-instance`, and a provisioned reader instance named
`tpch100g-clone-instance-2` for the new cluster.

You don't need to supply some parameters, such as `--master-username` and
`--master-user-password`. Aurora automatically determines those from the original cluster. You do
need to specify the DB engine to use. Thus, the example tests the new cluster to determine the right value to
use for the `--engine` parameter.

This example also includes the `--serverless-v2-scaling-configuration` option when creating the
clone cluster. That way, you can add Aurora Serverless v2 instances to the clone even if the original cluster
didn't use Aurora Serverless v2.

```
`$` aws rds restore-db-cluster-to-point-in-time \
  --source-db-cluster-identifier tpch100g \
  --db-cluster-identifier tpch100g-clone \
  --serverless-v2-scaling-configuration MinCapacity=`0.5`,MaxCapacity=`16` \
  --restore-type copy-on-write \
  --use-latest-restorable-time

`$` aws rds describe-db-clusters \
  --db-cluster-identifier tpch100g-clone \
    --query '*[].[Engine]' \
    --output text
`aurora-mysql`

`$` aws rds create-db-instance \
  --db-instance-identifier tpch100g-clone-instance \
  --db-cluster-identifier tpch100g-clone \
  --db-instance-class db.serverless \
  --engine aurora-mysql

`$` aws rds create-db-instance \
  --db-instance-identifier tpch100g-clone-instance-2 \
  --db-cluster-identifier tpch100g-clone \
  --db-instance-class db.r6g.2xlarge \
  --engine aurora-mysql

```

###### To create a clone with a different engine mode from the source Aurora DB cluster

- This procedure only applies to older engine versions that support Aurora Serverless v1. Suppose that you
  have an Aurora Serverless v1 cluster and you want to create a clone that's a provisioned cluster. In
  that case, use the
  `restore-db-cluster-to-point-in-time`
  CLI command and specify values similar parameter values as in the previous example, plus these additional
  parameters:
  - `--engine-mode` – Use this parameter only to create clones that are of a different
    engine mode from the source Aurora DB cluster. This parameter only applies to the older engine versions
    that support Aurora Serverless v1. Choose the value to pass with `--engine-mode` as follows:
    - Use `--engine-mode provisioned` to create a provisioned Aurora DB cluster clone from an
      Aurora Serverless DB cluster.

    ###### Note

    If you intend to use Aurora Serverless v2 with a cluster that was cloned from Aurora Serverless v1,
    you still specify the engine mode for the clone as `provisioned`. Then you perform
    additional upgrade and migration steps afterward.
    - Use `--engine-mode serverless` to create an Aurora Serverless v1 clone from a provisioned
      Aurora DB cluster. When you specify the `serverless` engine mode, you can also choose
      the `--scaling-configuration`.

  - `--scaling-configuration` – (Optional) Use with `--engine-mode
serverless` to configure the minimum and maximum capacity for an Aurora Serverless v1 clone. If
    you don't use this parameter, Aurora creates an Aurora Serverless v1 clone using the default
    Aurora Serverless v1 capacity values for the DB engine.

The following example creates a provisioned clone named `my-clone`, from an Aurora Serverless v1 DB
cluster named `my-source-cluster`.

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-to-point-in-time \
    --source-db-cluster-identifier `my-source-cluster` \
    --db-cluster-identifier `my-clone` \
    --engine-mode provisioned \
    --restore-type copy-on-write \
    --use-latest-restorable-time

```

For Windows:

```
aws rds restore-db-cluster-to-point-in-time ^
    --source-db-cluster-identifier `my-source-cluster` ^
    --db-cluster-identifier `my-clone` ^
    --engine-mode provisioned ^
    --restore-type copy-on-write ^
    --use-latest-restorable-time

```

These commands return the JSON object containing details of the clone that you need to create the DB instance.
You can't do that until the status of the clone (the empty Aurora DB cluster) has the status
**Available**.

###### Note

The
[restore-db-cluster-to-point-in-time](../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md")
AWS CLI command only restores the DB cluster, not the DB instances for that DB cluster. You run the
[create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command to create DB
instances for the restored DB cluster. With that command, you specify the identifier of the restored DB
cluster as the `--db-cluster-identifier` parameter. You can create DB instances only after the
`restore-db-cluster-to-point-in-time` command has completed and the DB cluster is available.

Suppose that you start with an Aurora Serverless v1 cluster and intend to migrate it to an Aurora Serverless v2
cluster. You create a provisioned clone of the Aurora Serverless v1 cluster as the initial step in the
migration. For the full procedure, including any required version upgrades, see
[Upgrading from an Aurora Serverless v1 cluster to Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure "aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure").

#### Checking the status and getting clone details

You can use the following command to check the status of your newly created clone cluster.

```
`$` `aws rds describe-db-clusters --db-cluster-identifier `my-clone` --query '*[].[Status]' --output text`
```

Or you can obtain the status and the other values that you need to
[create the DB instance for your clone](#Aurora.Managing.Clone.CLI.create-db-instance "#Aurora.Managing.Clone.CLI.create-db-instance") by
using the following AWS CLI query.

For Linux, macOS, or Unix:

```
aws rds describe-db-clusters --db-cluster-identifier `my-clone` \
  --query '*[].{Status:Status,Engine:Engine,EngineVersion:EngineVersion,EngineMode:EngineMode}'
```

For Windows:

```
aws rds describe-db-clusters --db-cluster-identifier `my-clone` ^
  --query "*[].{Status:Status,Engine:Engine,EngineVersion:EngineVersion,EngineMode:EngineMode}"
```

This query returns output similar to the following.

```
[
  {
        "Status": "available",
        "Engine": "aurora-mysql",
        "EngineVersion": "8.0.mysql_aurora.3.04.1",
        "EngineMode": "provisioned"
    }
]
```

#### Creating the Aurora DB instance for your clone

Use the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") CLI command to create
the DB instance for your Aurora Serverless v2 or provisioned clone. You don't create a DB instance for an
Aurora Serverless v1 clone.

The DB instance inherits the `--master-username` and `--master-user-password` properties
from the source DB cluster.

The following example creates a DB instance for a provisioned clone.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `my-new-db` \
    --db-cluster-identifier `my-clone` \
    --db-instance-class `db.r6g.2xlarge` \
    --engine aurora-mysql

```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `my-new-db` ^
    --db-cluster-identifier `my-clone` ^
    --db-instance-class `db.r6g.2xlarge` ^
    --engine aurora-mysql

```

The following example creates an Aurora Serverless v2 DB instance, for a clone that uses an engine version that
supports Aurora Serverless v2.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `my-new-db` \
    --db-cluster-identifier `my-clone` \
    --db-instance-class db.serverless \
  --engine aurora-postgresql

```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `my-new-db` ^
    --db-cluster-identifier `my-clone` ^
    --db-instance-class db.serverless ^
    --engine aurora-mysql

```

#### Parameters to use for cloning

The following table summarizes the various parameters used with
`restore-db-cluster-to-point-in-time` to clone Aurora DB clusters.

| Parameter                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--source-db-cluster-identifier`        | Use the name of the source Aurora DB cluster that you want to clone.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `--db-cluster-identifier`               | Choose a meaningful name for your clone when you create it with the<br>`restore-db-cluster-to-point-in-time` command. Then you pass this name to the<br>`create-db-instance` command.                                                                                                                                                                                                                                                                                                                                             |
| `--restore-type`                        | Specify `copy-on-write` as the `--restore-type` to create a clone of the<br>source DB cluster rather than restoring the source Aurora DB cluster.                                                                                                                                                                                                                                                                                                                                                                                 |
| `--use-latest-restorable-time`          | This value points to the latest restorable volume data for the source DB cluster. Use it to create<br>clones.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--serverless-v2-scaling-configuration` | (Newer versions that support Aurora Serverless v2) Use this parameter to configure the minimum and<br>maximum capacity for an Aurora Serverless v2 clone. If you don't specify this parameter, you<br>can't create any Aurora Serverless v2 instances in the clone cluster until you modify the cluster<br>to add this attribute.                                                                                                                                                                                                 |
| `--engine-mode`                         | (Older versions that support Aurora Serverless v1 only) Use this parameter to create clones that are<br>of a different type from the source Aurora DB cluster, with one of the following values:<br>• Use `provisioned` to create a provisioned clone from an Aurora Serverless v1 DB<br>cluster.<br>• Use `serverless` to create an Aurora Serverless v1 clone from a provisioned or<br>Aurora Serverless v2 DB cluster.<br>When you specify the `serverless` engine mode, you can also choose the<br>`--scaling-configuration`. |
| `--scaling-configuration`               | (Older versions that support Aurora Serverless v1 only) Use this parameter to configure the minimum<br>and maximum capacity for an Aurora Serverless v1 clone. If you don't specify this parameter,<br>Aurora creates the clone using the default capacity values for the DB engine.                                                                                                                                                                                                                                              |

For information about cross-VPC and cross-account cloning, see the following sections.

###### Topics

- [Cross-VPC cloning with Amazon Aurora](Aurora.Managing.Clone.md "Aurora.Managing.Clone.md")
- [Cross-account cloning with AWS RAM and Amazon Aurora](Aurora.Managing.Clone.md "Aurora.Managing.Clone.md")
