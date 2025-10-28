# Best practices and requirements for managing

global tables

###### Important

This documentation is for version 2017.11.29 (Legacy) of global tables, which
should be avoided for new global tables. Customers should use [Global Tables version 2019.11.21 (Current)](GlobalTables.md "GlobalTables.md") when possible,
as it provides greater flexibility, higher efficiency and consumes less write capacity than
2017.11.29 (Legacy).

To determine which version you are using, see [Determining the version of a global
table](V2globaltables_versions.md#globaltables.DetermineVersion "V2globaltables_versions.md#globaltables.DetermineVersion").
To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see
[DynamoDB global tables versions](V2globaltables_versions.md "V2globaltables_versions.md").

Using Amazon DynamoDB global tables, you can replicate your table data across AWS Regions. It is
important that the replica tables and secondary indexes in your global table have identical
write capacity settings to ensure proper replication of data.

###### Topics

- [Global tables version](#globaltables_version.tables "#globaltables_version.tables")
- [Requirements for adding a new
  replica table](#globaltables_reqs_bestpractices.requirements "#globaltables_reqs_bestpractices.requirements")
- [Best practices and requirements for
  managing capacity](#globaltables_reqs_bestpractices.tables "#globaltables_reqs_bestpractices.tables")

## Global tables version

There are two versions of DynamoDB global tables available: [Global Tables version 2019.11.21 (Current)](GlobalTables.md "GlobalTables.md") and [Global tables version 2017.11.29 (Legacy)](globaltables.md "globaltables.md"). Customers should use Global Tables version 2019.11.21
(Current) when possible, as it provides greater flexibility, higher efficiency and consumes
less write capacity than 2017.11.29 (Legacy).

To determine which version you are using, see [Determining the version of a global
table](V2globaltables_versions.md#globaltables.DetermineVersion "V2globaltables_versions.md#globaltables.DetermineVersion"). To
update existing global tables from Version 2017.11.29 (Legacy) to Version 2019.11.21
(Current), see [Upgrading global
tables](V2globaltables_versions.md#upgrading-to-current-version "V2globaltables_versions.md#upgrading-to-current-version").

## Requirements for adding a new

replica table

If you want to add a new replica table to a global table, each of the following conditions
must be true:

- The table must have the same partition key as all of the other replicas.
- The table must have the same write capacity management settings specified.
- The table must have the same name as all of the other replicas.
- The table must have DynamoDB Streams enabled, with the stream containing both the new and the old
  images of the item.
- None of the new or existing replica tables in the global table can contain any
  data.

If global secondary indexes are specified, the following conditions must also be
met:

- The global secondary indexes must have the same name.
- The global secondary indexes must have the same partition key and sort key (if
  present).

###### Important

Write capacity settings should be set consistently across all of your global tables’
replica tables and matching secondary indexes. To update write capacity settings for your
global table, we strongly recommend using the DynamoDB console or the
`UpdateGlobalTableSettings` API operation.
`UpdateGlobalTableSettings` applies changes to write capacity settings to all
replica tables and matching secondary indexes in a global table automatically. If you use
the `UpdateTable`, `RegisterScalableTarget`, or
`PutScalingPolicy` operations, you should apply the change to each replica
table and matching secondary index individually. For more information, see [UpdateGlobalTableSettings](../APIReference/API_UpdateGlobalTableSettings.md "../APIReference/API_UpdateGlobalTableSettings.md") in
the [Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").

We strongly recommend that you enable auto scaling to manage provisioned write capacity
settings. If you prefer to manage write capacity settings manually, you should provision
equal replicated write capacity units to all of your replica tables. Also provision equal
replicated write capacity units to matching secondary indexes across your global table.

You must also have appropriate AWS Identity and Access Management (IAM) permissions. For more information, see
[Using IAM with global tables](gt_IAM.md "gt_IAM.md").

## Best practices and requirements for

managing capacity

Consider the following when managing capacity settings for replica tables in DynamoDB.

### Using DynamoDB auto

scaling

Using DynamoDB auto scaling is the recommended way to manage throughput capacity settings
for replica tables that use the provisioned mode. DynamoDB auto scaling automatically adjusts
read capacity units (RCUs) and write capacity units (WCUs) for each replica table based upon
your actual application workload. For more information, see [Managing throughput capacity automatically with DynamoDB auto
scaling](AutoScaling.md "AutoScaling.md").

If you create your replica tables using the AWS Management Console, auto scaling is enabled by
default for each replica table, with default auto scaling settings for managing read
capacity units and write capacity units.

Changes to auto scaling settings for a replica table or secondary index made through the
DynamoDB console or using the `UpdateGlobalTableSettings` call are applied to all of
the replica tables and matching secondary indexes in the global table automatically. These
changes overwrite any existing auto scaling settings. This ensures that provisioned write
capacity settings are consistent across the replica tables and secondary indexes in your
global table. If you use the `UpdateTable`, `RegisterScalableTarget`,
or `PutScalingPolicy` calls, you should apply the change to each replica table
and matching secondary index individually.

###### Note

If auto scaling doesn't satisfy your application's capacity changes (unpredictable
workload), or if you don't want to configure its settings (target settings for minimum,
maximum, or utilization threshold), you can use on-demand mode to manage capacity for your
global tables. For more information, see [On-demand mode](capacity-mode.md#capacity-mode-on-demand "capacity-mode.md#capacity-mode-on-demand").

If you enable on-demand mode on a global table, your consumption of replicated write
request units (rWCUs) will be consistent with how rWCUs are provisioned. For example, if
you perform 10 writes to a local table that is replicated in two additional Regions, you
will consume 60 write request units (10 + 10 + 10 = 30; 30 x 2 = 60). The consumed 60
write request units include the extra write consumed by global tables Version 2017.11.29
(Legacy) to update the `aws:rep:deleting`, `aws:rep:updatetime`, and
`aws:rep:updateregion` attributes.

### Managing

capacity manually

If you decide not to use DynamoDB auto scaling, you must manually set the read capacity and
write capacity settings on each replica table and secondary index.

The provisioned replicated write capacity units (rWCUs) on every replica table should be
set to the total number of rWCUs needed for application writes across all Regions multiplied
by two. This accommodates application writes that occur in the local Region and replicated
application writes coming from other Regions. For example, suppose that you expect 5 writes
per second to your replica table in Ohio and 5 writes per second to your replica table in N.
Virginia. In this case, you should provision 20 rWCUs to each replica table (5 + 5 = 10; 10
x 2 = 20).

To update write capacity settings for your global table, we strongly recommend using
the DynamoDB console or the `UpdateGlobalTableSettings` API operation.
`UpdateGlobalTableSettings` applies changes to write capacity settings to all
replica tables and matching secondary indexes in a global table automatically. If you use
the `UpdateTable`, `RegisterScalableTarget`, or
`PutScalingPolicy` operations, you should apply the change to each replica
table and matching secondary index individually. For more information, see [Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").

###### Note

To update the settings (`UpdateGlobalTableSettings`) for a global table in
DynamoDB, you must have the `dynamodb:UpdateGlobalTable`,
`dynamodb:DescribeLimits`,
`application-autoscaling:DeleteScalingPolicy`, and
`application-autoscaling:DeregisterScalableTarget` permissions. For more
information, see [Using IAM with global tables](gt_IAM.md "gt_IAM.md").
