# UltraWarm storage for Amazon OpenSearch Service

UltraWarm provides a cost-effective way to store large amounts of read-only data on
Amazon OpenSearch Service. Standard data nodes use "hot" storage, which takes the form of instance stores or
Amazon EBS volumes attached to each node. Hot storage provides the fastest possible performance
for indexing and searching new data.

Rather than attached storage, UltraWarm nodes use Amazon S3 and a sophisticated caching
solution to improve performance. For indexes that you are not actively writing to, query
less frequently, and don't need the same performance from, UltraWarm offers significantly
lower costs per GiB of data. Because warm indexes are read-only unless you return them to
hot storage, UltraWarm is best-suited to immutable data, such as logs.

In OpenSearch, warm indexes behave just like any other index. You can query them using the
same APIs or use them to create visualizations in OpenSearch Dashboards.

###### Topics

- [Prerequisites](#ultrawarm-pp "#ultrawarm-pp")
- [UltraWarm storage requirements and performance
  considerations](#ultrawarm-calc "#ultrawarm-calc")
- [UltraWarm pricing](#ultrawarm-pricing "#ultrawarm-pricing")
- [Enabling UltraWarm](#ultrawarm-enable "#ultrawarm-enable")
- [Migrating indexes to UltraWarm storage](#ultrawarm-migrating "#ultrawarm-migrating")
- [Automating migrations](#ultrawarm-ism "#ultrawarm-ism")
- [Migration tuning](#ultrawarm-settings "#ultrawarm-settings")
- [Cancelling migrations](#ultrawarm-cancel "#ultrawarm-cancel")
- [Listing hot and warm indexes](#ultrawarm-api "#ultrawarm-api")
- [Returning warm indexes to hot storage](#ultrawarm-migrating-back "#ultrawarm-migrating-back")
- [Restoring warm indexes from snapshots](#ultrawarm-snapshot "#ultrawarm-snapshot")
- [Manual snapshots of warm indexes](#ultrawarm-manual-snapshot "#ultrawarm-manual-snapshot")
- [Migrating warm indexes to cold storage](#ultrawarm-cold "#ultrawarm-cold")
- [Best practices for KNN indexes](#ultrawarm-recommendations "#ultrawarm-recommendations")
- [Disabling UltraWarm](#ultrawarm-disable "#ultrawarm-disable")

## Prerequisites

UltraWarm has a few important prerequisites:

- UltraWarm requires OpenSearch or Elasticsearch 6.8 or higher.
- To use warm storage, domains must have [dedicated master
  nodes](managedomains-dedicatedmasternodes.md "managedomains-dedicatedmasternodes.md").
- When using a [Multi-AZ with
  Standby](managedomains-multiaz.md#managedomains-za-standby "managedomains-multiaz.md#managedomains-za-standby") domain, the number of warm nodes must be a multiple of the
  number of Availability Zones being used.
- If your domain uses a T2 or T3 instance type for your data nodes, you can't
  use warm storage.
- If your index uses approximate k-NN (`"index.knn":true`), you can
  move it to warm storage from version 2.17 and later. Domains on versions earlier
  than 2.17 can upgrade to 2.17 to use this functionality, but KNN indices created
  on versions earlier than 2.x can't migrate to UltraWarm.
- If the domain uses [fine-grained access control](fgac.md "fgac.md"),
  users must be mapped to the `ultrawarm_manager` role in
  OpenSearch Dashboards to make UltraWarm API calls.

###### Note

The `ultrawarm_manager` role might not be defined on some preexisting
OpenSearch Service domains. If you don't see the role in Dashboards, you need to [manually create it](#ultrawarm-create-role "#ultrawarm-create-role").

### Configure permissions

If you enable UltraWarm on a preexisting OpenSearch Service domain, the
`ultrawarm_manager` role might not be defined on the domain.
Non-admin users must be mapped to this role in order to manage warm indexes on
domains using fine-grained access control. To manually create the
`ultrawarm_manager` role, perform the following steps:

1. In OpenSearch Dashboards, go to **Security** and choose
   **Permissions**.
2. Choose **Create action group** and configure the
   following groups:

| Group name              | Permissions                                                                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ultrawarm_cluster`     | • `cluster:admin/ultrawarm/migration/list`<br>• `cluster:monitor/nodes/stats`                                                                                        |
| `ultrawarm_index_read`  | • `indices:admin/ultrawarm/migration/get`<br>• `indices:admin/get`                                                                                                   |
| `ultrawarm_index_write` | • `indices:admin/ultrawarm/migration/warm`<br>• `indices:admin/ultrawarm/migration/hot`<br>• `indices:monitor/stats`<br>• `indices:admin/ultrawarm/migration/cancel` |

3. Choose **Roles** and **Create
   role**.
4. Name the role **ultrawarm_manager**.
5. For **Cluster permissions,** select
   `ultrawarm_cluster` and `cluster_monitor`.
6. For **Index**, type `*`.
7. For **Index permissions**, select
   `ultrawarm_index_read`, `ultrawarm_index_write`,
   and `indices_monitor`.
8. Choose **Create**.
9. After you create the role, [map it](fgac.md#fgac-mapping "fgac.md#fgac-mapping") to
   any user or backend role that will manage UltraWarm indexes.

## UltraWarm storage requirements and performance

considerations

As covered in [Calculating storage requirements](bp-storage.md "bp-storage.md"), data in hot storage incurs significant
overhead: replicas, Linux reserved space, and OpenSearch Service reserved space. For example, a 20 GiB
primary shard with one replica shard requires roughly 58 GiB of hot storage.

Because it uses Amazon S3, UltraWarm incurs none of this overhead. When calculating
UltraWarm storage requirements, you consider only the size of the primary shards. The
durability of data in S3 removes the need for replicas, and S3 abstracts away any
operating system or service considerations. That same 20 GiB shard requires 20 GiB of
warm storage. If you provision an `ultrawarm1.large.search` instance, you can
use all 20 TiB of its maximum storage for primary shards. See [UltraWarm storage quotas](limits.md#limits-ultrawarm "limits.md#limits-ultrawarm") for a summary of instance types and the maximum amount
of storage that each can address.

With UltraWarm, we still recommend a maximum shard size of 50 GiB. The [number of CPU cores and amount of RAM allocated to each
UltraWarm instance type](#ultrawarm-pricing "#ultrawarm-pricing") gives you an idea of the number of shards they can
simultaneously search. Note that while only primary shards count toward UltraWarm
storage in S3, OpenSearch Dashboards and `_cat/indices` still report
UltraWarm index size as the _total_ of all primary and replica
shards.

For example, each `ultrawarm1.medium.search` instance has two CPU cores and
can address up to 1.5 TiB of storage on S3. Two of these instances have a combined 3 TiB
of storage, which works out to approximately 62 shards if each shard is 50 GiB. If a
request to the cluster only searches four of these shards, performance might be
excellent. If the request is broad and searches all 62 of them, the four CPU cores might
struggle to perform the operation. Monitor the `WarmCPUUtilization` and
`WarmJVMMemoryPressure`
[UltraWarm metrics](managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-uw "managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-uw") to
understand how the instances handle your workloads.

If your searches are broad or frequent, consider leaving the indexes in hot storage.
Just like any other OpenSearch workload, the most important step to determining if
UltraWarm meets your needs is to perform representative client testing using a realistic
dataset.

## UltraWarm pricing

With hot storage, you pay for what you provision. Some instances require an attached
Amazon EBS volume, while others include an instance store. Whether that storage is empty or
full, you pay the same price.

With UltraWarm storage, you pay for what you use. An
`ultrawarm1.large.search` instance can address up to 20 TiB of storage on
S3, but if you store only 1 TiB of data, you're only billed for 1 TiB of data. Like all
other node types, you also pay an hourly rate for each UltraWarm node. For more
information, see [Pricing for Amazon OpenSearch Service](what-is.md#pricing "what-is.md#pricing").

## Enabling UltraWarm

The console is the simplest way to create a domain that uses warm storage. While
creating the domain, choose **Enable warm data nodes** and the number
of warm nodes that you want. The same basic process works on existing domains, provided
they meet the [prerequisites](#ultrawarm-pp "#ultrawarm-pp"). Even after the domain
state changes from **Processing** to **Active**,
UltraWarm might not be available to use for several hours.

When using a Multi-AZ with Standby domain, the number of warm nodes must be a multiple
of the number of Availability Zones. For more information, see [Multi-AZ with Standby](managedomains-multiaz.md#managedomains-za-standby "managedomains-multiaz.md#managedomains-za-standby").

You can also use the [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html") or [configuration API](../APIReference/Welcome.md "../APIReference/Welcome.md")
to enable UltraWarm, specifically the `WarmEnabled`, `WarmCount`,
and `WarmType` options in `ClusterConfig`.

###### Note

Domains support a maximum number of warm nodes. For details, see [Amazon OpenSearch Service quotas](limits.md "limits.md").

### Sample CLI command

The following AWS CLI command creates a domain with three data nodes, three
dedicated master nodes, six warm nodes, and fine-grained access control
enabled:

```
aws opensearch create-domain \
  --domain-name `my-domain` \
  --engine-version Opensearch_1.0 \
  --cluster-config InstanceCount=3,InstanceType=r6g.large.search,DedicatedMasterEnabled=true,DedicatedMasterType=r6g.large.search,DedicatedMasterCount=3,ZoneAwarenessEnabled=true,ZoneAwarenessConfig={AvailabilityZoneCount=3},WarmEnabled=true,WarmCount=6,WarmType=ultrawarm1.medium.search \
  --ebs-options EBSEnabled=true,VolumeType=gp2,VolumeSize=11 \
  --node-to-node-encryption-options Enabled=true \
  --encryption-at-rest-options Enabled=true \
  --domain-endpoint-options EnforceHTTPS=true,TLSSecurityPolicy=Policy-Min-TLS-1-2-2019-07 \
  --advanced-security-options Enabled=true,InternalUserDatabaseEnabled=true,MasterUserOptions='{MasterUserName=`master-user`,MasterUserPassword=`master-password`}' \
  --access-policies '{"Version": "2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":{"AWS":["`123456789012`"]},"Action":["es:*"],"Resource":"arn:aws:es:`us-west-1`:`123456789012`:domain/`my-domain`/*"}]}' \
  --region `us-east-1`
```

For detailed information, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

### Sample configuration API

request

The following request to the configuration API creates a domain with three data
nodes, three dedicated master nodes, and six warm nodes with fine-grained access
control enabled and a restrictive access policy:

```
POST https://es.us-east-2.amazonaws.com/2021-01-01/opensearch/domain
{
  "ClusterConfig": {
    "InstanceCount": 3,
    "InstanceType": "r6g.large.search",
    "DedicatedMasterEnabled": true,
    "DedicatedMasterType": "r6g.large.search",
    "DedicatedMasterCount": 3,
    "ZoneAwarenessEnabled": true,
    "ZoneAwarenessConfig": {
      "AvailabilityZoneCount": 3
    },
    "WarmEnabled": true,
    "WarmCount": 6,
    "WarmType": "ultrawarm1.medium.search"
  },
  "EBSOptions": {
    "EBSEnabled": true,
    "VolumeType": "gp2",
    "VolumeSize": 11
  },
  "EncryptionAtRestOptions": {
    "Enabled": true
  },
  "NodeToNodeEncryptionOptions": {
    "Enabled": true
  },
  "DomainEndpointOptions": {
    "EnforceHTTPS": true,
    "TLSSecurityPolicy": "Policy-Min-TLS-1-2-2019-07"
  },
   "AdvancedSecurityOptions": {
    "Enabled": true,
    "InternalUserDatabaseEnabled": true,
    "MasterUserOptions": {
      "MasterUserName": "`master-user`",
      "MasterUserPassword": "`master-password`"
    }
  },
  "EngineVersion": "Opensearch_1.0",
  "DomainName": "`my-domain`",
  "AccessPolicies": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":[\"`123456789012`\"]},\"Action\":[\"es:*\"],\"Resource\":\"arn:aws:es:`us-east-1`:`123456789012`:domain/`my-domain`/*\"}]}"
}
```

For detailed information, see the [Amazon OpenSearch Service API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

## Migrating indexes to UltraWarm storage

If you finished writing to an index and no longer need the fastest possible search
performance, migrate it from hot to UltraWarm:

```
POST _ultrawarm/migration/`my-index`/_warm
```

Then check the status of the migration:

```
GET _ultrawarm/migration/`my-index`/_status

{
  "migration_status": {
    "index": "`my-index`",
    "state": "RUNNING_SHARD_RELOCATION",
    "migration_type": "HOT_TO_WARM",
    "shard_level_status": {
      "running": 0,
      "total": 5,
      "pending": 3,
      "failed": 0,
      "succeeded": 2
    }
  }
}
```

Index health must be green to perform a migration. If you migrate several indexes in
quick succession, you can get a summary of all migrations in plaintext, similar to the
`_cat` API:

```
GET _ultrawarm/migration/_status?v

index    migration_type state
`my-index` HOT_TO_WARM    RUNNING_SHARD_RELOCATION
```

OpenSearch Service migrates one index at a time to UltraWarm. You can have up to 200 migrations in
the queue. Any request that exceeds the limit will be rejected. To check the current
number of migrations in the queue, monitor the `HotToWarmMigrationQueueSize`
[metric](managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-uw "managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-uw"). Indexes remain
available throughout the migration process—no downtime.

The migration process has the following states:

```
PENDING_INCREMENTAL_SNAPSHOT
RUNNING_INCREMENTAL_SNAPSHOT
FAILED_INCREMENTAL_SNAPSHOT
PENDING_FORCE_MERGE
RUNNING_FORCE_MERGE
FAILED_FORCE_MERGE
PENDING_FULL_SNAPSHOT
RUNNING_FULL_SNAPSHOT
FAILED_FULL_SNAPSHOT
PENDING_SHARD_RELOCATION
RUNNING_SHARD_RELOCATION
FINISHED_SHARD_RELOCATION
```

As these states indicate, migrations might fail during snapshots, shard relocations,
or force merges. Failures during snapshots or shard relocation are typically due to node
failures or S3 connectivity issues. Lack of disk space is usually the underlying cause
of force merge failures.

After a migration finishes, the same `_status` request returns an error. If
you check the index at that time, you can see some settings that are unique to warm
indexes:

```
GET `my-index`/_settings

{
  "`my-index`": {
    "settings": {
      "index": {
        "refresh_interval": "-1",
        "auto_expand_replicas": "false",
        "provided_name": "`my-index`",
        "creation_date": "1599241458998",
        "unassigned": {
          "node_left": {
            "delayed_timeout": "5m"
          }
        },
        "number_of_replicas": "1",
        "uuid": "GswyCdR0RSq0SJYmzsIpiw",
        "version": {
          "created": "7070099"
        },
        "routing": {
          "allocation": {
            "require": {
              "box_type": "warm"
            }
          }
        },
        "number_of_shards": "5",
        "merge": {
          "policy": {
            "max_merge_at_once_explicit": "50"
          }
        }
      }
    }
  }
}
```

- `number_of_replicas`, in this case, is the number of passive
  replicas, which don't consume disk space.
- `routing.allocation.require.box_type` specifies that the index
  should use warm nodes rather than standard data nodes.
- `merge.policy.max_merge_at_once_explicit` specifies the number of
  segments to simultaneously merge during the migration.

Indexes in warm storage are read-only unless you [return them to hot storage](#ultrawarm-migrating-back "#ultrawarm-migrating-back"), which makes
UltraWarm best-suited to immutable data, such as logs. You can query the indexes and
delete them, but you can't add, update, or delete individual documents. If you try, you
might encounter the following error:

```
{
  "error" : {
    "root_cause" : [
      {
        "type" : "cluster_block_exception",
        "reason" : "index [indexname] blocked by: [TOO_MANY_REQUESTS/12/disk usage exceeded flood-stage watermark, index has read-only-allow-delete block];"
      }
    ],
    "type" : "cluster_block_exception",
    "reason" : "index [indexname] blocked by: [TOO_MANY_REQUESTS/12/disk usage exceeded flood-stage watermark, index has read-only-allow-delete block];"
  },
  "status" : 429
}
```

## Automating migrations

We recommend using [Index State Management in Amazon OpenSearch Service](ism.md "ism.md") to automate the migration process after an
index reaches a certain age or meets other conditions. See the [sample policy](ism.md#ism-example-cold "ism.md#ism-example-cold") that demonstrates this
workflow.

## Migration tuning

Index migrations to UltraWarm storage require a force merge. Each OpenSearch index
is composed of some number of shards, and each shard is composed of some number of
Lucene segments. The force merge operation purges documents that were marked for
deletion and conserves disk space. By default, UltraWarm merges indexes into one
segment, except for kNN indices, where a default value of 20 is used.

You can change this value up to 1,000 segments using the
`index.ultrawarm.migration.force_merge.max_num_segments` setting. Higher
values speed up the migration process, but increase query latency for the warm index
after the migration finishes. To change the setting, make the following request:

```
PUT `my-index`/_settings
{
  "index": {
    "ultrawarm": {
      "migration": {
        "force_merge": {
          "max_num_segments": `1`
        }
      }
    }
  }
}
```

To check how long this stage of the migration process takes, monitor the
`HotToWarmMigrationForceMergeLatency`
[metric](managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-uw "managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-uw").

## Cancelling migrations

UltraWarm handles migrations sequentially, in a queue. If a migration is in the queue,
but has not yet started, you can remove it from the queue using the following
request:

```
POST _ultrawarm/migration/_cancel/`my-index`
```

If your domain uses fine-grained access control, you must have the
`indices:admin/ultrawarm/migration/cancel` permission to make this
request.

## Listing hot and warm indexes

UltraWarm adds two additional options, similar to `_all`, to help manage
hot and warm indexes. For a list of all warm or hot indexes, make the following
requests:

```
GET _warm
GET _hot
```

You can use these options in other requests that specify indexes, such as:

```
_cat/indices/_warm
_cluster/state/_all/_hot
```

## Returning warm indexes to hot storage

If you need to write to an index again, migrate it back to hot storage:

```
POST _ultrawarm/migration/`my-index`/_hot
```

You can have up to 10 queued migrations from warm to hot storage at a time. OpenSearch Service
processes migration requests one at a time, in the order that they were queued. To check
the current number, monitor the `WarmToHotMigrationQueueSize`
[metric](managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-uw "managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-uw").

After the migration finishes, check the index settings to make sure they meet your
needs. Indexes return to hot storage with one replica.

## Restoring warm indexes from snapshots

In addition to the standard repository for automated snapshots, UltraWarm adds a
second repository for warm indexes, `cs-ultrawarm`. Each snapshot in this
repository contains only one index. If you delete a warm index, its snapshot remains in
the `cs-ultrawarm` repository for 14 days, just like any other automated
snapshot.

When you restore a snapshot from `cs-ultrawarm`, it restores to warm
storage, not hot storage. Snapshots in the `cs-automated` and
`cs-automated-enc` repositories restore to hot storage.

###### To restore an UltraWarm snapshot to warm storage

1. Identify the latest snapshot that contains the index you want to
   restore:

```
GET _snapshot/cs-ultrawarm/_all?verbose=false

{
  "snapshots": [{
    "snapshot": "`snapshot-name`",
    "version": "1.0",
    "indices": [
      "`my-index`"
    ]
  }]
}
```

###### Note

By default, the `GET _snapshot/<repo>` operation displays
verbose data information such as start time, end time, and duration for each
snapshot within a repository. The `GET _snapshot/<repo>`
operation retrieves information from the files of each snapshot contained in
a repository. If you do not need the start time, end time, and duration and
require only the name and index information of a snapshot, we recommend
using the `verbose=false` parameter when listing snapshots to
minimize processing time and prevent timing out. 2. If the index already exists, delete it:

```
DELETE `my-index`
```

If you don't want to delete the index, [return it to hot storage](#ultrawarm-migrating-back "#ultrawarm-migrating-back") and
[reindex](https://docs.opensearch.org/latest/opensearch/reindex-data/ "https://docs.opensearch.org/latest/opensearch/reindex-data/") it. 3. Restore the snapshot:

```
POST _snapshot/cs-ultrawarm/`snapshot-name`/_restore
```

UltraWarm ignores any index settings you specify in this restore request, but
you can specify options like `rename_pattern` and
`rename_replacement`. For a summary of OpenSearch snapshot restore
options, see the [OpenSearch documentation](https://docs.opensearch.org/latest/opensearch/snapshot-restore/#restore-snapshots "https://docs.opensearch.org/latest/opensearch/snapshot-restore/#restore-snapshots").

## Manual snapshots of warm indexes

You _can_ take manual snapshots of warm indexes, but
we don't recommend it. The automated `cs-ultrawarm` repository already
contains a snapshot for each warm index, taken during the migration, at no additional
charge.

By default, OpenSearch Service does not include warm indexes in manual snapshots. For example, the
following call only includes hot indexes:

```
PUT _snapshot/`my-repository`/`my-snapshot`
```

If you choose to take manual snapshots of warm indexes, several important
considerations apply.

- You can't mix hot and warm indexes. For example, the following request
  fails:

```
PUT _snapshot/`my-repository`/`my-snapshot`
{
  "indices": "`warm-index-1`,`hot-index-1`",
  "include_global_state": false
}
```

If they include a mix of hot and warm indexes, wildcard (`*`)
statements fail, as well.

- You can only include one warm index per snapshot. For example, the following
  request fails:

```
PUT _snapshot/`my-repository`/`my-snapshot`
{
  "indices": "`warm-index-1`,`warm-index-2`,`other-warm-indices-*`",
  "include_global_state": false
}
```

This request succeeds:

```
PUT _snapshot/`my-repository`/`my-snapshot`
{
  "indices": "`warm-index-1`",
  "include_global_state": false
}
```

- Manual snapshots always restore to hot storage, even if they originally
  included a warm index.

## Migrating warm indexes to cold storage

If you have data in UltraWarm that you query infrequently, consider migrating it to
cold storage. Cold storage is meant for data you only access occasionally or is no
longer in active use. You can't read from or write to cold indexes, but you can migrate
them back to warm storage at no cost whenever you need to query them. For instructions,
see [Migrating indexes to cold storage](cold-storage.md#coldstorage-migrating "cold-storage.md#coldstorage-migrating").

## Best practices for KNN indexes

- Ultrawarm/Cold tier is available for all KNN index engine types. We recommend
  it for KNN indexes using Lucene engine and Disk-optimized vector search, which
  does not require to fully load the graph data in off-heap memory. While using it
  with native in-memory engines like FAISS and NMSLIB, you must account for the
  shards graph size that will be actively searched on, and provision the UltraWarm
  instances, preferably of the `uw.large` instance type, accordingly.
  For example, if customers have 2 `uw.large` instances configured,
  then they each will have approximately `knn.memory.circuit_breaker.limit *
61` GiB available off-heap memory. You get optimal performance if all
  your warm queries are targeting shards whose cumulative graph size does not
  exceed available off-heap memory. Latency is impacted if the available memory is
  lower than needed to load the graph because of evictions and waiting on off-heap
  memory to become available. That's why we don’t recommend using
  `uw.medium` instances for use cases where in-memory engines are
  being used or for higher search throughput cases, irrespective of
  engines.
- KNN indexes migrating to UltraWarm will not be force-merged to single segment.
  This avoids any impact on the hot and warm nodes running into OOM issues because
  of graph size becoming too big for in-memory engines. Due to the increase in
  number of segments per shard, this might result in consuming more local cache
  space and allowing fewer indices to migrate to the warm tier. You can choose to
  force-merge indexes to single segment by using the existing setting, and
  overriding it before migrating indexes to the warm tier. For more information,
  see [Migration tuning](#ultrawarm-settings "#ultrawarm-settings").
- If you have a use case where indexes are searched infrequently and do not
  serve a latency sensitive workload, you can choose to migrate those indexes to
  the UltraWarm tier. This will help you to scale down the hot tier compute
  instances and let the UltraWarm tier compute handle the query on such low
  priority indexes. This can also help to provide isolation of resources consumed
  between the queries of low and high priority indexes so they don't impact each
  other.

## Disabling UltraWarm

The console is the simplest way to disable UltraWarm. Choose the domain,
**Actions**, and **Edit cluster configuration**.
Deselect **Enable warm data nodes** and choose **Save
changes**. You can also use the `WarmEnabled` option in the
AWS CLI and configuration API.

Before you disable UltraWarm, you must either [delete](https://opensearch.org/docs/latest/opensearch/rest-api/index-apis/delete-index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index-apis/delete-index/") all warm indexes or [migrate
them back to hot storage](#ultrawarm-migrating-back "#ultrawarm-migrating-back"). After warm storage is empty, wait five minutes
before attempting to disable UltraWarm.
