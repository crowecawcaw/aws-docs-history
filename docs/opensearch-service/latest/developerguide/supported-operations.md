# Supported operations in Amazon OpenSearch Service

OpenSearch Service supports many versions of OpenSearch and legacy Elasticsearch OSS. The following
sections show the operations that OpenSearch Service supports for each version.

###### Topics

- [Notable API differences](#version_api_notes "#version_api_notes")

## Notable API differences

### New List APIs

To support large clusters with large number of indexes and shards, we have
introduced new List APIs with pagination support, such as \_list/indices and
\_list/shards. The List API retrieves statistics about indexes and shards in a
paginated format. This streamlines the task of processing responses that include
many indexes.

- `_list/indices`: [\_list/indices](https://opensearch.org/docs/latest/api-reference/list/list-indices/ "https://opensearch.org/docs/latest/api-reference/list/list-indices/")
- `_list/shards`: [\_list/shards](https://opensearch.org/docs/latest/api-reference/list/list-shards/ "https://opensearch.org/docs/latest/api-reference/list/list-shards/")

### Changes to existing APIs

To support large clusters, we have added support in the
`_cluster/stats` API to add additional metric filters to support
retrieving only relevant stats responses, for example
`_cluster/stats/<metric>/nodes/<node-filters>` and
`_cluster/stats/<metric>/<index_metric>/nodes/<node-filters>`.
For details, see [\_cluster/stats](https://opensearch.org/docs/latest/api-reference/cluster-api/cluster-stats/ "https://opensearch.org/docs/latest/api-reference/cluster-api/cluster-stats/").

We have added support in `_cat/shards` API for task cancellation by
specifying a `cancel_after_time_interval` request parameter. For
details, see [\_cat/shards](https://opensearch.org/docs/latest/api-reference/cat/cat-shards/ "https://opensearch.org/docs/latest/api-reference/cat/cat-shards/").

**Limiting the response size for \_cat API**

To support large clusters with total instance count of more than 200 across
data and warm nodes, we have a 10K limit on the number of indexes returned by
the `_cat/segments API`. If the number of indexes in the response
exceeds this limit, the API returns a 429 error. To avoid this, you can specify
an index pattern filter in your query, such as
`_cat/segments/<index-pattern>`.

### Settings and statistics

OpenSearch Service only accepts PUT requests to the `_cluster/settings` API that
use the "flat" settings form. It rejects requests that use the expanded settings
form.

```
// Accepted
PUT _cluster/settings
{
  "persistent" : {
    "action.auto_create_index" : false
  }
}

// Rejected
PUT _cluster/settings
{
  "persistent": {
    "action": {
      "auto_create_index": false
    }
  }
}
```

The high-level Java REST client uses the expanded form, so if you need to send
settings requests, use the low-level client.

Prior to Elasticsearch 5.3, the `_cluster/settings` API on OpenSearch Service
domains supported only the HTTP `PUT` method, not the
`GET` method. OpenSearch and later versions of Elasticsearch
support the `GET` method, as shown in the following example:

```
GET https://`domain-name`.`region`.es.amazonaws.com/_cluster/settings?pretty
```

Here is a return example:

```
{
  "persistent": {
    "cluster": {
      "routing": {
        "allocation": {
          "cluster_concurrent_rebalance": "2",
          "node_concurrent_recoveries": "2",
          "disk": {
            "watermark": {
              "low": "1.35gb",
              "flood_stage": "0.45gb",
              "high": "0.9gb"
            }
          },
          "node_initial_primarirecoveries": "4"
        }
      }
    },
    "indices": {
      "recovery": {
        "max_bytper_sec": "40mb"
      }
    }
  }
}
```

If you compare responses from an open source OpenSearch cluster and OpenSearch Service for
certain settings and statistics APIs, you might notice missing fields. OpenSearch Service
redacts certain information that exposes service internals, such as the file
system data path from `_nodes/stats` or the operating system name and
version from `_nodes`.

### Shrink

The `_shrink` API can cause upgrades, configuration changes, and
domain deletions to fail. We don't recommend using it on domains that run
Elasticsearch versions 5.3 or 5.1. These versions have a bug that can cause
snapshot restoration of shrunken indices to fail.

If you use the `_shrink` API on other Elasticsearch or OpenSearch
versions, make the following request before starting the shrink
operation:

```
PUT https://`domain-name`.`region`.es.amazonaws.com/`source-index`/_settings
{
  "settings": {
    "index.routing.allocation.require._name": "`name-of-the-node-to-shrink-to`",
    "index.blocks.read_only": true
  }
}
```

Then make the following requests after completing the shrink operation:

```
PUT https://`domain-name`.`region`.es.amazonaws.com/`source-index`/_settings
{
  "settings": {
    "index.routing.allocation.require._name": null,
    "index.blocks.read_only": false
  }
}

PUT https://`domain-name`.`region`.es.amazonaws.com/`shrunken-index`/_settings
{
  "settings": {
    "index.routing.allocation.require._name": null,
    "index.blocks.read_only": false
  }
}
```

### New list APIs

To support large clusters with huge number of indexes and shards, we have
introduced new list APIs with pagination support i.e. `_list/indices`
and `_list/shards`. The List API retrieves statistics about indexes
and shards in a paginated format. This streamlines the task of processing
responses that include many indexes. For more information on
`_list/indices`, see [List indices](https://opensearch.org/docs/latest/api-reference/list/list-indices/ "https://opensearch.org/docs/latest/api-reference/list/list-indices/"). For more information on `_list/shards`,
see [List shards](https://opensearch.org/docs/latest/api-reference/list/list-shards/ "https://opensearch.org/docs/latest/api-reference/list/list-shards/").

### Changes to existing APIs

To support large clusters, we have added support in
`_cluster/stats/<metric>/nodes/<node-filters>` and
`_cluster/stats/<metric>/<index_metric>/nodes/<node-filters>`.
For more information on `_cluster/stats`, see [Cluster stats](https://opensearch.org/docs/latest/api-reference/cluster-api/cluster-stats/ "https://opensearch.org/docs/latest/api-reference/cluster-api/cluster-stats/").

### Limiting the response size for \_cat

APIs

To support large clusters with total instance count more than 200 across data
and warm nodes, we have a 10,000 limit on the number of indexes returned by
\_cat/segments API. If the number of indexes in the response exceeds this limit,
the API returns a `429` error. To avoid this, you can specify an
index pattern filter in your query (for example,
`_cat/segments/<index-pattern>` ).

Additionally, support for task cancellation has is now available for
`_cat/shards` API for task cancellation by specifying
`cancel_after_time_interval` request parameter. For more
information on this, see [CAT shards](https://opensearch.org/docs/latest/api-reference/cluster-api/cluster-stats/ "https://opensearch.org/docs/latest/api-reference/cluster-api/cluster-stats/").

### Choosing the instance types for dedicated

master nodes

The following table provides recommendations for choosing the appropriate
instance types for dedicdated master nodes:

| RAM    | Maximum node supported | Maximum shard supported |
| ------ | ---------------------- | ----------------------- |
| 2 GB   | 10                     | 1,000                   |
| 4 GB   | 10                     | 5,000                   |
| 8 GB   | 30                     | 15,000                  |
| 16 GB  | 60                     | 30,000                  |
| 32 GB  | 120                    | 60,000                  |
| 64 GB  | 240                    | 120,000                 |
| 128 GB | 480                    | 240,000                 |
| 256 GB | 1002                   | 500,000                 |

### OpenSearch version 2.19

For information about OpenSearch 2.19 operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin. For more details about changes in this release, see the [2.19 release notes](https://github.com/opensearch-project/opensearch-build/blob/main/release-notes/opensearch-release-notes-2.19.0.md "https://github.com/opensearch-project/opensearch-build/blob/main/release-notes/opensearch-release-notes-2.19.0.md").

### OpenSearch version 2.17

For OpenSearch 2.17, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

###### Note

Starting with OpenSearch 2.17, the `cluster.max_shards_per_node`
setting can't be modified. For OpenSearch 2.17 and later, OpenSearch Service supports 1000
shards for every 16GB of JVM heap memory up to a maximum of 4000 shards per
node.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.search.request.slowlog.level`<br>+ `cluster.search.request.slowlog.threshold.warn`<br>+ `cluster.search.request.slowlog.threshold.info`<br>+ `cluster.search.request.slowlog.threshold.debug`<br>+ `cluster.search.request.slowlog.threshold.trace`<br>+ `search.phase_took_enabled`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_list`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ml`<br>• `/_plugins/_notifications`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_security_analytics`<br>• `/_plugins/_sm`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search/pipeline`<br>• `/_search/point_in_time`<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refer to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and others.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

###### Note

Currently, changing the `cluster.max_shards_per_node`
setting functionality is not enabled for customers with Multi-AZ
(Availability Zone) with standby.

### OpenSearch version 2.15

For OpenSearch 2.15, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>+ `cluster.search.request.slowlog.level`<br>+ `cluster.search.request.slowlog.threshold.warn`<br>+ `cluster.search.request.slowlog.threshold.info`<br>+ `cluster.search.request.slowlog.threshold.debug`<br>+ `cluster.search.request.slowlog.threshold.trace`<br>+ `search.phase_took_enabled`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ml`<br>• `/_plugins/_notifications`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_security_analytics`<br>• `/_plugins/_sm`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search/pipeline`<br>• `/_search/point_in_time`<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 2.13

For OpenSearch 2.13, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>+ `cluster.search.request.slowlog.level`<br>+ `cluster.search.request.slowlog.threshold.warn`<br>+ `cluster.search.request.slowlog.threshold.info`<br>+ `cluster.search.request.slowlog.threshold.debug`<br>+ `cluster.search.request.slowlog.threshold.trace`<br>+ `search.phase_took_enabled`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ml`<br>• `/_plugins/_notifications`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_security_analytics`<br>• `/_plugins/_sm`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search/pipeline`<br>• `/_search/point_in_time`<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 2.11

For OpenSearch 2.11, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ml`<br>• `/_plugins/_notifications`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_security_analytics`<br>• `/_plugins/_sm`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search/pipeline`<br>• `/_search/point_in_time`<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 2.9

For OpenSearch 2.9, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ml`<br>• `/_plugins/_notifications`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_security_analytics`<br>• `/_plugins/_sm`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search/pipeline`<br>• `/_search/point_in_time`<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 2.7

For OpenSearch 2.7, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ml`<br>• `/_plugins/_notifications`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_security_analytics`<br>• `/_plugins/_sm`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search/point_in_time`<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 2.5

For OpenSearch 2.5, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ml`<br>• `/_plugins/_notifications`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_security_analytics`<br>• `/_plugins/_sm`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search/point_in_time`<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 2.3

For OpenSearch 2.3, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ml`<br>• `_plugins/_notifications`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 1.3

For OpenSearch 1.3, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ml`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 1.2

For OpenSearch 1.2, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_sql`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 1.1

For OpenSearch 1.1, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_sql`<br>• `/_plugins/_transforms`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### OpenSearch version 1.0

For OpenSearch 1.0, OpenSearch Service supports the following operations. For information
about most of the operations, see the [OpenSearch REST API reference](https://opensearch.org/docs/latest/opensearch/rest-api/index/ "https://opensearch.org/docs/latest/opensearch/rest-api/index/"), or the API reference for the
specific plugin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count`<br>• `/\_dashboards` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_plugins/_asynchronous_search`<br>• `/_plugins/_alerting`<br>• `/_plugins/_anomaly_detection`<br>• `/_plugins/_ism`<br>• `/_plugins/_ppl`<br>• `/_plugins/_security`<br>• `/_plugins/_sql`<br>• `/_plugins/_transforms`<br>• `/_percolate`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 7.10

For Elasticsearch 7.10, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_index_template`6<br>• `/_ingest/pipeline`<br>• `/_index_template`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_opendistro/_asynchronous_search`<br>• `/_opendistro/_anomaly_detection`<br>• `/_opendistro/_ism`<br>• `/_opendistro/_ppl`<br>• `/_opendistro/_security`<br>• `/_opendistro/_sql`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_plugins/_replication`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`6<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").
6. Legacy index templates (`_template`) were replaced by
   composable templates (`_index_template`) starting with
   Elasticsearch 7.8. Composable templates take precedence over legacy
   templates. If no composable template matches a given index, a legacy
   template can still match and be applied. The `_template`
   operation still works on OpenSearch and later versions of
   Elasticsearch OSS, but GET calls to the two template types return
   different results.

### Elasticsearch version 7.9

For Elasticsearch 7.9, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>• `/\_cluster/state`<br>• `/\_cluster/stats`<br>• `/\_count` | • `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_index_template`6<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_opendistro/_anomaly_detection`<br>• `/_opendistro/_ism`<br>• `/_opendistro/_ppl`<br>• `/_opendistro/_security`<br>• `/_opendistro/_sql`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_resolve/index`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`6<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic OpenSearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").
6. Legacy index templates (`_template`) were replaced by
   composable templates (`_index_template`) starting with
   Elasticsearch 7.8. Composable templates take precedence over legacy
   templates. If no composable template matches a given index, a legacy
   template can still match and be applied. The `_template`
   operation still works on OpenSearch and later versions of
   Elasticsearch OSS, but GET calls to the two template types return
   different results.

### Elasticsearch version 7.8

For Elasticsearch 7.8, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_index_template`6<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_opendistro/_anomaly_detection`<br>• `/_opendistro/_ism`<br>• `/_opendistro/_security`<br>• `/_opendistro/_sql`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`6<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").
6. Legacy index templates (`_template`) were replaced by
   composable templates (`_index_template`) starting with
   Elasticsearch 7.8. Composable templates take precedence over legacy
   templates. If no composable template matches a given index, a legacy
   template can still match and be applied. The `_template`
   operation still works on OpenSearch and later versions of
   Elasticsearch OSS, but GET calls to the two template types return
   different results.

### Elasticsearch version 7.7

For Elasticsearch 7.7, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_ltr`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_opendistro/_anomaly_detection`<br>• `/_opendistro/_ism`<br>• `/_opendistro/_security`<br>• `/_opendistro/_sql`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 7.4

For Elasticsearch 7.4, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`,<br>`/`index-name`/update/`id``,<br>and<br>`/`index-name`/\_close`)<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_opendistro/_anomaly_detection`<br>• `/_opendistro/_ism`<br>• `/_opendistro/_security`<br>• `/_opendistro/_sql`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 7.1

For Elasticsearch 7.1, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_opendistro/_ism`<br>• `/_opendistro/_security`<br>• `/_opendistro/_sql`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 6.8

For Elasticsearch 6.8, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node`<br>+ `cluster.blocks.read_only` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_opendistro/_ism`<br>• `/_opendistro/_security`<br>• `/_opendistro/_sql`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 6.7

For Elasticsearch 6.7, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `cluster.max_shards_per_node` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_opendistro/_security`<br>• `/_opendistro/_sql`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 6.5

For Elasticsearch 6.5, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_opendistro/_sql`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 6.4

For Elasticsearch 6.4, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 6.3

For Elasticsearch 6.3, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 6.2

For Elasticsearch 6.2, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_opendistro/_alerting`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_rank_eval` | • `/_refresh`<br>• `/_reindex`1<br>• `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_split`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 6.0

For Elasticsearch 6.0, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_refresh`<br>• `/_reindex`1 | • `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 5.6

For Elasticsearch 5.6, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_refresh`<br>• `/_reindex`1 | • `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 5.5

For Elasticsearch 5.5, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties4:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_refresh`<br>• `/_reindex`1 | • `/_render`<br>• `/_rollover`<br>• `/_scripts`3<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`5<br>• `/_snapshot`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. For considerations about using scripts, see [Other supported resources in Amazon OpenSearch Service](supported-resources.md "supported-resources.md").
4. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
5. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 5.3

For Elasticsearch 5.3, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties3:<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_refresh`<br>• `/_reindex`1 | • `/_render`<br>• `/_rollover`<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`4<br>• `/_snapshot`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. Refers to the `PUT` method. For information about the
   `GET` method, see [Notable API differences](#version_api_notes "#version_api_notes").
   This list only refers to the generic Elasticsearch operations that OpenSearch Service
   supports and does not include plugin-specific supported operations for
   anomaly detection, ISM, and so on.
4. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 5.1

For Elasticsearch 5.1, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/update/`id``)<br>**except**<br>`/`index-name`/\_close`<br>• `/\_alias`<br>• `/\_aliases`<br>• `/\_all`<br>• `/\_analyze`<br>• `/\_bulk`<br>• `/\_cat` (except<br>`/\_cat/nodeattrs`)<br>• `/\_cluster/allocation/explain`<br>• `/\_cluster/health`<br>• `/\_cluster/pending_tasks`<br>• `/\_cluster/settings`for several<br>properties (PUT only):<br>+`action.auto_create_index`<br>+ `action.search.shard_count.limit`<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit` | • `/_cluster/state`<br>• `/_cluster/stats`<br>• `/_count`<br>• `/_delete_by_query`1<br>• `/_explain`<br>• `/_field_caps`<br>• `/_field_stats`<br>• `/_flush`<br>• `/_ingest/pipeline`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_mtermvectors`<br>• `/_nodes`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_refresh`<br>• `/_reindex`1 | • `/_render`<br>• `/_rollover`<br>• `/_search`2<br>• `/_search profile`<br>• `/_shard_stores`<br>• `/_shrink`3<br>• `/_snapshot`<br>• `/_stats`<br>• `/_status`<br>• `/_tasks`<br>• `/_template`<br>• `/_update_by_query`1<br>• `/_validate` |

1. Cluster configuration changes might interrupt these operations before
   completion. We recommend that you use the `/_tasks` operation
   along with these operations to verify that the requests completed
   successfully.
2. DELETE requests to `/_search/scroll` with a message body
   must specify `"Content-Length"` in the HTTP header. Most
   clients add this header by default. To avoid a problem with
   `=` characters in `scroll_id` values, use the
   request body, not the query string, to pass `scroll_id`
   values to OpenSearch Service.
3. See [Shrink](#version_api_notes-shrink "#version_api_notes-shrink").

### Elasticsearch version 2.3

For Elasticsearch 2.3, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| • All operations in the index path (such as<br>`/`index-name`/_forcemerge`<br>and<br>`/`index-name`/_recovery`)<br>**except**<br>`/`index-name`/_close`<br>• `/_alias`<br>• `/_aliases`<br>• `/_all`<br>• `/_analyze`<br>• `/_bulk`<br>• `/_cache/clear` (index only)<br>• `/_cat` (except<br>`/_cat/nodeattrs`)<br>• `/_cluster/health`<br>• `/_cluster/settings` for several<br>properties (PUT only):<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `threadpool.get.queue_size`<br>+ `threadpool.bulk.queue_size`<br>+ `threadpool.index.queue_size`<br>+ `threadpool.percolate.queue_size`<br>+ `threadpool.search.queue_size`<br>+ `threadpool.suggest.queue_size` | • `/_cluster/stats`<br>• `/_count`<br>• `/_flush`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_nodes`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_refresh`<br>• `/_render`<br>• `/_search`<br>• `/_snapshot`<br>• `/_stats`<br>• `/_status`<br>• `/_template` |

### Elasticsearch version 1.5

For Elasticsearch 1.5, OpenSearch Service supports the following operations.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • All operations in the index path, such as<br>`/`index-name`/_optimize`<br>and<br>`/`index-name`/_warmer`,<br>**except**<br>`/`index-name`/_close`<br>• `/_alias`<br>• `/_aliases`<br>• `/_all`<br>• `/_analyze`<br>• `/_bulk`<br>• `/_cat`<br>• `/_cluster/health`<br>• `/_cluster/settings` for several<br>properties (PUT only):<br>+ `indices.breaker.fielddata.limit`<br>+ `indices.breaker.request.limit`<br>+ `indices.breaker.total.limit`<br>+ `threadpool.get.queue_size`<br>+ `threadpool.bulk.queue_size`<br>+ `threadpool.index.queue_size`<br>+ `threadpool.percolate.queue_size`<br>+ `threadpool.search.queue_size`<br>+ `threadpool.suggest.queue_size` | • `/_cluster/stats`<br>• `/_count`<br>• `/_flush`<br>• `/_mapping`<br>• `/_mget`<br>• `/_msearch`<br>• `/_nodes`<br>• `/_percolate`<br>• `/_plugin/kibana`<br>• `/_plugin/kibana3`<br>• `/_plugin/migration`<br>• `/_refresh`<br>• `/_search`<br>• `/_snapshot`<br>• `/_stats`<br>• `/_status`<br>• `/_template` |
