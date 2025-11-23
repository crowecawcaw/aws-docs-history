# Cross-cluster replication for Amazon OpenSearch Service

With cross-cluster replication in Amazon OpenSearch Service, you can replicate user indexes, mappings, and
metadata from one OpenSearch Service domain to another. Using cross-cluster replication helps to ensure
disaster recovery if there is an outage, and allows you to replicate data across
geographically distant data centers to reduce latency. You pay [standard AWS data transfer
charges](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/") for the data transferred between domains.

Cross-cluster replication follows an active-passive replication model where the
_local_ or _follower_ index pulls data from the
_remote_ or _leader_ index. The leader index
refers to the source of the data, or the index that you want to replicate data from. The
follower index refers to the target for the data, or the index that you want to replicate
data to.

Cross-cluster replication is available on domains running Elasticsearch 7.10 or
OpenSearch 1.1 or later.

###### Note

This documentation describes how to set up cross-cluster replication from an Amazon OpenSearch Service
perspective. This includes using the AWS Management Console to set up cross-cluster connections,
which is not possible on a self-managed OpenSearch cluster. For full documentation,
including a settings reference and a comprehensive API reference, see [Cross-cluster
replication](https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/index/ "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/index/") in the OpenSearch documentation.

###### Topics

- [Limitations](#replication-limitations "#replication-limitations")
- [Prerequisites](#replication-prereqs "#replication-prereqs")
- [Permissions requirements](#replication-permissions "#replication-permissions")
- [Set up a cross-cluster connection](#replication-connect "#replication-connect")
- [Start replication](#replication-start "#replication-start")
- [Confirm replication](#replication-confirm "#replication-confirm")
- [Pause and resume replication](#replication-pause-resume "#replication-pause-resume")
- [Stop replication](#replication-stop "#replication-stop")
- [Auto-follow](#replication-autofollow "#replication-autofollow")
- [Upgrading connected domains](#replication-upgrade "#replication-upgrade")

## Limitations

Cross-cluster replication has the following limitations:

- You can't replicate data between Amazon OpenSearch Service domains and self-managed
  OpenSearch or Elasticsearch clusters.
- You can't replicate an index from a follower domain to another follower
  domain. If you want to replicate an index to multiple follower domains, you can
  only replicate it from the single leader domain.
- A domain can be connected, through a combination of inbound and outbound
  connections, to a maximum of 20 other domains.
- When you initially set up a cross-cluster connection, the leader domain must
  be on the same or a higher version than the follower domain.
- You can't use CloudFormation to connect domains.
- You can't use cross-cluster replication on M3 or burstable (T2 and T3)
  instances.
- You can't replicate data between UltraWarm or cold indexes. Both indexes must
  be in hot storage.
- When you delete an index from the leader domain, the corresponding index on
  the follower domain isn't automatically deleted.

## Prerequisites

Before you set up cross-cluster replication, make sure that your domains meet the
following requirements:

- Elasticsearch 7.10 or OpenSearch 1.1 or later
- [Fine-grained access control](fgac.md "fgac.md") enabled
- [Node-to-node encryption](ntn.md "ntn.md") enabled

## Permissions requirements

In order to start replication, you must include the `es:ESCrossClusterGet`
permission on the remote (leader) domain. We recommend the following IAM policy on the
remote domain. This policy also lets you perform other operations, such as indexing
documents and performing standard searches:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "*"
 ]
 },
 "Action": [
 "es:ESHttp*"
 ],
 "Resource": "arn:aws:es:`us-east-1`:`111122223333`:domain/leader-domain/*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": "es:ESCrossClusterGet",
 "Resource": "arn:aws:es:`us-east-1`:`111122223333`:domain/leader-domain"
 }
 ]
}`

```

Make sure that the `es:ESCrossClusterGet` permission is applied for
`/leader-domain` and not `/leader-domain/*`.

In order for non-admin users to perform replication activities, they also need to be
mapped to the appropriate permissions. Most permissions correspond to specific [REST API
operations](https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/api/ "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/api/"). For example, the
`indices:admin/plugins/replication/index/_resume` permission lets you
resume replication of an index. For a full list of permissions, see [Replication permissions](https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/permissions/#replication-permissions "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/permissions/#replication-permissions") in the OpenSearch documentation.

###### Note

The commands to start replication and create a replication rule are special cases.
Because they invoke background processes on the leader and follower domains, you
must pass a `leader_cluster_role` and `follower_cluster_role`
in the request. OpenSearch Service uses these roles in all backend replication tasks. For
information about mapping and using these roles, see [Map the leader and follower cluster roles](https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/permissions/#map-the-leader-and-follower-cluster-roles "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/permissions/#map-the-leader-and-follower-cluster-roles") in the OpenSearch
documentation.

## Set up a cross-cluster connection

To replicate indexes from one domain to another, you need to set up a cross-cluster
connection between the domains. The easiest way to connect domains is through the
**Connections** tab of the domain dashboard. You can also use the
[configuration API](../APIReference/Welcome.md "../APIReference/Welcome.md")
or the [AWS CLI](../../../cli/latest/reference/opensearch/create-outbound-connection.md "../../../cli/latest/reference/opensearch/create-outbound-connection.md"). Because cross-cluster replication follows a "pull" model, you
initate connections from the follower domain.

###### Note

If you previously connected two domains to perform [cross-cluster searches](cross-cluster-search.md "cross-cluster-search.md"), you can't use that
same connection for replication. The connection is marked as
`SEARCH_ONLY` in the console. In order to perform replication between
two previously connected domains, you must delete the connection and recreate it.
When you've done this, the connection is available for both cross-cluster search and
cross-cluster replication.

###### To set up a connection

1. In the Amazon OpenSearch Service console, select the follower domain, go to the
   **Connections** tab, and choose
   **Request**.
2. For **Connection alias**, enter a name for your
   connection.
3. Choose between connecting to a domain in your AWS account and
   Region or in another account or Region.
   - To connect to a domain in your AWS account and
     Region, select the domain and choose
     **Request**.
   - To connect to a domain in another AWS account or
     Region, specify the ARN of the remote domain and choose
     **Request**.

OpenSearch Service validates the connection request. If the domains are incompatible, the connection
fails. If validation succeeds, it's sent to the destination domain for approval. When
the destination domain approves the request, you can begin replication.

Cross-cluster replication supports bidirectional replication. This means that you can
create an outbound connection from domain A to domain B, and another outbound connection
from domain B to domain A. You can then set up replication so that domain A follows an
index in domain B, and domain B follows an index in domain A.

## Start replication

After you establish a cross-cluster connection, you can begin to replicate data.
First, create an index on the leader domain to replicate:

```
PUT `leader-01`
```

To replicate that index, send this command to the follower domain:

```
PUT _plugins/_replication/`follower-01`/_start
{
   "leader_alias": "`connection-alias`",
   "leader_index": "`leader-01`",
   "use_roles":{
      "leader_cluster_role": "`all_access`",
      "follower_cluster_role": "`all_access`"
   }
}
```

You can find the connection alias on the **Connections** tab on your
domain dashboard.

This example assumes that an admin is issuing the request and uses
`all_access` for the `leader_cluster_role` and
`follower_cluster_role` for simplicity. In production environments,
however, we recommend that you create replication users on both the leader and follower
indexes, and map them accordingly. The usernames must be identical. For information
about these roles and how to map them, see [Map the leader and follower cluster roles](https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/permissions/#map-the-leader-and-follower-cluster-roles "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/permissions/#map-the-leader-and-follower-cluster-roles") in the OpenSearch
documentation.

## Confirm replication

To confirm that replication is happening, get the replication status:

```
GET _plugins/_replication/`follower-01`/_status

{
  "status" : "SYNCING",
  "reason" : "User initiated",
  "leader_alias" : "connection-alias",
  "leader_index" : "leader-01",
  "follower_index" : "follower-01",
  "syncing_details" : {
    "leader_checkpoint" : -5,
    "follower_checkpoint" : -5,
    "seq_no" : 0
  }
}
```

The leader and follower checkpoint values begin as negative integers and reflect the
number of shards you have (-1 for one shard, -5 for five shards, and so on). The values
increment to positive integers with each change that you make. If the values are the
same, it means that the indexes are fully synced. You can use these checkpoint values to
measure replication latency across your domains.

To further validate replication, add a document to the leader index:

```
PUT `leader-01`/_doc/1
{
   "Doctor Sleep":"Stephen King"
}
```

And confirm that it shows up on the follower index:

```
GET `follower-01`/_search

{
    ...
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "follower-01",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "Doctor Sleep" : "Stephen King"
        }
      }
    ]
  }
}
```

## Pause and resume replication

You can temporarily pause replication if you need to remediate issues or reduce load
on the leader domain. Send this request to the follower domain. Make sure to include an
empty request body:

```
POST _plugins/_replication/`follower-01`/_pause
{}
```

Then get the status to ensure that replication is paused:

```
GET _plugins/_replication/`follower-01`/_status

{
  "status" : "PAUSED",
  "reason" : "User initiated",
  "leader_alias" : "connection-alias",
  "leader_index" : "leader-01",
  "follower_index" : "follower-01"
}
```

When you're done making changes, resume replication. Send this request to the follower
domain. Make sure to include an empty request body:

```
POST _plugins/_replication/`follower-01`/_resume
{}
```

You can't resume replication after it's been paused for more than 12 hours. You must
stop replication, delete the follower index, and restart replication of the
leader.

## Stop replication

When you stop replication completely, the follower index unfollows the leader and
becomes a standard index. You can't restart replication after you stop it.

Stop replication from the follower domain. Make sure to include an empty request
body:

```
POST _plugins/_replication/`follower-01`/_stop
{}
```

## Auto-follow

You can define a set of replication rules against a single leader domain that
automatically replicate indexes that match a specified pattern. When an index on the
leader domain matches one of the patterns (for example, `books*`), a matching
follower index is created on the follower domain. OpenSearch Service replicates any existing indexes
that match the pattern, as well as new indexes that you create. It does not replicate
indexes that already exist on the follower domain.

To replicate all indexes (with the exception of system-created indexes, and those that
already exist on the follower domain), use a wildcard (`*`) pattern.

### Create a replication rule

Create a replication rule on the follower domain, and specify the name of the
cross-cluster connection:

```
POST _plugins/_replication/_autofollow
{
   "leader_alias" : "`connection-alias`",
   "name": "`rule-name`",
   "pattern": "`books*`",
   "use_roles":{
      "leader_cluster_role": "`all_access`",
      "follower_cluster_role": "`all_access`"
   }
}
```

You can find the connection alias on the **Connections** tab on
your domain dashboard.

This example assumes that an admin is issuing the request, and it uses
`all_access` as the leader and follower domain roles for simplicity.
In production environments, however, we recommend that you create replication users
on both the leader and follower indexes and map them accordingly. The usernames must
be identical. For information about these roles and how to map them, see [Map the leader and follower cluster roles](https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/permissions/#map-the-leader-and-follower-cluster-roles "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/permissions/#map-the-leader-and-follower-cluster-roles") in the OpenSearch
documentation.

To retrieve a list of existing replication rules on a domain, use the [auto-follow stats API operation](https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/api/#get-auto-follow-stats "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/api/#get-auto-follow-stats").

To test the rule, create an index that matches the pattern on the leader
domain:

```
PUT `books-are-fun`
```

And check that its replica appears on the follower domain:

```
GET _cat/indices

health status index          uuid                     pri rep docs.count docs.deleted store.size pri.store.size
green  open   books-are-fun  ldfHO78xYYdxRMULuiTvSQ     1   1          0            0       208b           208b
```

### Delete a replication rule

When you delete a replication rule, OpenSearch Service stops replicating
_new_ indices that match the pattern, but continues existing
replication activity until you [stop
replication](#replication-stop "#replication-stop") of those indexes.

Delete replication rules from the follower domain:

```
DELETE _plugins/_replication/_autofollow
{
   "leader_alias" : "`connection-alias`",
   "name": "`rule-name`"
}
```

## Upgrading connected domains

In order to upgrade the engine version of two domains that have a cross-cluster
connection, upgrade the follower domain first and then the leader domain. Do not delete
the connection between them, otherwise replication pauses and you won't be able to
resume it.
