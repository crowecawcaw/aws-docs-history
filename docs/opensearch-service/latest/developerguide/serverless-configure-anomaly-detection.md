

# Configuring anomaly detection on Amazon OpenSearch Serverless
<a name="serverless-configure-anomaly-detection"></a>

Anomaly detection automatically detects anomalies in your OpenSearch data in near real time by using the Random Cut Forest (RCF) algorithm. RCF is an unsupervised machine learning algorithm that models a sketch of your incoming data stream. For each incoming data point, RCF computes an `anomaly grade` and a `confidence score`. For a conceptual overview of anomaly detection, see [Anomaly detection](https://docs.opensearch.org/latest/observing-your-data/ad/index/) on the OpenSearch website.

Serverless anomaly detection uses an Amazon OpenSearch Serverless collection as the data source for the detector. You create and manage detectors from OpenSearch UI. Each detector is a resource of the OpenSearch UI workspace that you create it in. This page describes the prerequisites, permissions, and considerations that are specific to serverless collections. It also documents the workspace-scoped API operations that you use to manage detectors programmatically.

**Important**  
Detectors are OpenSearch UI workspace resources. As a result, the anomaly detection API operations for serverless collections differ from the open source anomaly detection API operations under `_plugins/_anomaly_detection`. Use the workspace-scoped operations in [Anomaly detection API operations for serverless collections](#serverless-ad-api).

## Prerequisites
<a name="serverless-ad-prereqs"></a>
+ A collection that contains the index that you want to run anomaly detection on. We recommend a **time series** collection. For more information, see [Choosing a collection type for anomaly detection](#serverless-ad-collection-type).
+ An OpenSearch UI application with a workspace that has the collection attached as a data source. For more information, see [Using OpenSearch UI in Amazon OpenSearch Service](application.md).

## Choosing a collection type for anomaly detection
<a name="serverless-ad-collection-type"></a>

We recommend that you use anomaly detection together with a **time series** collection. A detector on a serverless collection monitors a *single* index. A time series collection automatically manages data retention for that index, so you don't have to build a custom retention process.

Keep the following considerations in mind:
+ **One index for each detector** – A detector monitors a single index. Index patterns, aliases, and comma-separated lists of multiple indexes aren't supported. If you need to detect anomalies across several indexes, create a separate detector for each index.
+ **Automatic data retention** – Time series collections manage the lifecycle of the data in the monitored index for you. This pairs well with the single-index requirement, because a single long-lived index would otherwise require you to manage retention yourself.
+ **Search collections** – Search collections are also accepted as a detector data source, but they don't manage data retention for you.

For more information about collection types, see [Choosing a collection type](serverless-overview.md#serverless-usecase).

## Configuring permissions for anomaly detection
<a name="serverless-ad-permissions"></a>

Detectors run as background jobs against your collection. The following collection data access policy grants the permissions that anomaly detection requires. Replace the {{placeholder values}} with your specific information. The ARN partition depends on the AWS Region. Standard AWS Regions use `aws`, and China Regions use `aws-cn`. For more information, see [Supported policy permissions](serverless-data-access.md#serverless-data-supported-permissions).

```
{
    "Rules": [
        {
            "Resource": [
                "collection/{{collection_name}}"
            ],
            "Permission": [
                "aoss:CreateCollectionItems",
                "aoss:DeleteCollectionItems",
                "aoss:UpdateCollectionItems",
                "aoss:DescribeCollectionItems"
            ],
            "ResourceType": "collection"
        },
        {
            "Resource": [
                "index/{{collection_name}}/*"
            ],
            "Permission": [
                "aoss:CreateIndex",
                "aoss:DeleteIndex",
                "aoss:UpdateIndex",
                "aoss:DescribeIndex",
                "aoss:ReadDocument",
                "aoss:WriteDocument",
                "aoss:DelegateAccess"
            ],
            "ResourceType": "index"
        }
    ],
    "Principal": [
        "arn:aws:iam::{{account_id}}:role/{{role_name}}"
    ],
    "Description": "Anomaly detection access policy for {{collection_name}}"
}
```
+ **Collection permissions** (`aoss:CreateCollectionItems`, `aoss:DeleteCollectionItems`, `aoss:UpdateCollectionItems`, `aoss:DescribeCollectionItems`) – Allow the anomaly detection job to resolve and operate on the collection.
+ **Index permissions** (`aoss:CreateIndex`, `aoss:DeleteIndex`, `aoss:UpdateIndex`, `aoss:DescribeIndex`, `aoss:ReadDocument`, `aoss:WriteDocument`) – Allow the detector to read the monitored index. They also allow the detector to create the custom result index and write results to it.
+ **Delegation permission** (`aoss:DelegateAccess`) – Allows the anomaly detection background job to access the collection on your behalf.

**Important**  
You can scope the index resource to specific indexes instead of `index/{{collection_name}}/*`. In that case, cover both the monitored index and the custom result index.

Within an OpenSearch UI workspace, access to anomaly detection features follows the workspace collaborator permissions (read-only, read/write, or admin). Read-only collaborators can view detectors and results, and read/write and admin collaborators can create, update, start, stop, and delete detectors.

## Custom result indexes
<a name="serverless-ad-result-index"></a>

Detectors on serverless collections must write their results to a *custom result index*. The default `.opendistro-anomaly-results*` index isn't available on serverless collections.

Specify the custom result index in the `resultIndex` field when you create a detector. The index name must begin with `opensearch-ad-plugin-result-`.

```
"resultIndex": "opensearch-ad-plugin-result-{{my-detector}}"
```

**Important**  
OpenSearch Serverless doesn't support the result index lifecycle settings that anomaly detection offers on provisioned domains, such as `resultIndexMinAge`, `resultIndexMinSize`, `resultIndexTtl`, and `flattenCustomResultIndex`. You are responsible for managing and rolling over the result index. Configure a data lifecycle policy that covers the result index. For more information, see [Using data lifecycle policies with Amazon OpenSearch Serverless](serverless-lifecycle.md).

Every detector writes to a custom result index. Make sure that the data access policy in [Configuring permissions for anomaly detection](#serverless-ad-permissions) covers the result index as well as the monitored index.

## Alerting on anomalies
<a name="serverless-ad-alerting"></a>

To receive a notification when a detector finds an anomaly, create an alerting monitor that queries the custom result index of the detector. The detector writes its results to a regular index in your collection. As a result, you can use a standard per query or per bucket monitor with a trigger on `anomaly_grade` and `confidence`.

Complete the following steps:

1. Set up the alerting prerequisites and permissions for your collection.

1. Create a monitor in OpenSearch UI against the custom result index of the detector (`opensearch-ad-plugin-result-{{my-detector}}`). For guidance on the trigger conditions to use for anomaly results, see [Managing anomaly detection](https://docs.opensearch.org/latest/observing-your-data/ad/managing-anomalies/) on the OpenSearch website.

1. Add a notification channel to the trigger so that the alert reaches your destination of choice.

**Note**  
The *anomaly detector* monitor type from the open source alerting plugin isn't available on serverless collections, because it reads from the default anomaly result index. Query the custom result index instead.

## Anomaly detection API operations for serverless collections
<a name="serverless-ad-api"></a>

Serverless collections support all of the operations in the open source [Anomaly detection API](https://docs.opensearch.org/latest/observing-your-data/ad/api/) on the OpenSearch website. However, you call them with workspace-style paths. Detectors are OpenSearch UI workspace resources, so you send requests to your OpenSearch UI application endpoint rather than to the collection endpoint. Each path includes a workspace and identifies the data source that represents your collection.

Use a SigV4-signing HTTP client such as [awscurl](https://github.com/okigan/awscurl) on the GitHub website to call the operations. The following sections describe the request format, list the operation paths, and show a few representative examples.

### Request format
<a name="serverless-ad-api-format"></a>

Requests use the following format:

```
https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/{{operation_path}}
```

The following table describes each part of the request.


| Component | Description | 
| --- | --- | 
| {{application\_endpoint}} | The endpoint of your OpenSearch UI application, in the format `application-{{application_name}}-{{application_id}}.{{region}}.opensearch.amazonaws.com`. | 
| {{workspace\_id}} | The ID of the OpenSearch UI workspace that contains the detector. You can find it in the `/w/` segment of the workspace URL in the OpenSearch UI console. | 
| {{data\_source\_id}} | The ID of the data source in the workspace that represents your collection. Depending on the operation, you pass this value either as the last segment of the path or as a `dataSourceId` query parameter. See [Operation paths](#serverless-ad-api-operations). | 
| {{detector\_id}} | The ID of a detector, returned in the `id` field when you create or search for detectors. | 

Sign every request with Signature Version 4 (SigV4), using `opensearch` as the service name. For more information, see [Signing HTTP requests with other clients](serverless-clients.md#serverless-signing). The examples in this section use [awscurl](https://github.com/okigan/awscurl) on the GitHub website, which signs requests with the credentials from your AWS profile. Include the following headers on every request:
+ `Content-Type: application/json` – Required on requests that send a body.
+ `osd-xsrf: osd-fetch` – Required cross-site request forgery header.
+ `osd-version: {{3.6.0}}` – The OpenSearch version of your OpenSearch UI application.

Each response uses an envelope. A successful response returns `{"ok": true, "response": {...}}`, and a failed response returns `{"ok": false, "error": "{{message}}"}`.

### Operation paths
<a name="serverless-ad-api-operations"></a>

The following table lists the anomaly detection operations and their workspace-style paths. All paths are relative to `https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors`.


| Operation | Method and path | 
| --- | --- | 
| Create a detector | `POST /detectors/{{data_source_id}}` | 
| Get a detector | `GET /detectors/{{detector_id}}/{{data_source_id}}` | 
| Update a detector | `PUT /detectors/{{detector_id}}/{{data_source_id}}` | 
| Delete a detector | `DELETE /detectors/{{detector_id}}/{{data_source_id}}` | 
| Validate a detector | `POST /detectors/_validate/{{validation_type}}/{{data_source_id}}` | 
| Preview a detector | `POST /detectors/preview/{{data_source_id}}` | 
| Suggest configuration values | `POST /detectors/_suggest/{{suggest_type}}/{{data_source_id}}` | 
| Start a detector | `POST /detectors/{{detector_id}}/start/{{data_source_id}}` | 
| Stop a detector | `POST /detectors/{{detector_id}}/stop/{{is_historical}}/{{data_source_id}}` | 
| Profile a detector | `GET /detectors/{{detector_id}}/_profile/{{data_source_id}}` | 
| Count detectors | `GET /detectors/_count/{{data_source_id}}` | 
| List detectors | `GET /detectors/_list?dataSourceId={{data_source_id}}` | 
| Match a detector name | `GET /detectors/{{detector_name}}/_match?dataSourceId={{data_source_id}}` | 
| Search detectors | `POST /detectors/_search?dataSourceId={{data_source_id}}` | 
| Search detector tasks | `POST /detectors/tasks/_search/{{data_source_id}}` | 
| Search anomaly results | `POST /detectors/results/_search/{{data_source_id}}` | 
| Get the results of a detector | `GET /detectors/{{detector_id}}/results/{{is_historical}}?dataSourceId={{data_source_id}}` | 
| Get top anomalies | `POST /detectors/{{detector_id}}/_topAnomalies/{{is_historical}}?dataSourceId={{data_source_id}}` | 
| Get statistics | `GET /stats/{{stats}}/{{data_source_id}}` | 

Note the following about the path parameters:
+ {{is\_historical}} is `false` for real-time detection or `true` for historical analysis.
+ {{validation\_type}} is `detector` to validate the configuration itself. Use `model` to also check whether the configuration is likely to produce a usable model against your data.
+ {{stats}} is a comma-separated list of statistics, such as `ad_execute_request_count,ad_execute_failure_count,anomaly_results_index_status`.

For the request and response bodies of each operation, see [Anomaly detection API](https://docs.opensearch.org/latest/observing-your-data/ad/api/) on the OpenSearch website.

**Note**  
You must stop a detector before you update or delete it. Anomaly results and task records can take a few minutes to appear after you start a detector.

### Example: Create a detector
<a name="serverless-ad-api-create"></a>

```
awscurl --service opensearch --region {{us-west-2}} \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0" \
  -d '{
    "name": "deny-anomalies",
    "description": "Detects anomalies in denied requests",
    "indices": ["server-metrics"],
    "resultIndex": "opensearch-ad-plugin-result-deny-anomalies",
    "filterQuery": {"match_all": {}},
    "timeField": "@timestamp",
    "featureAttributes": [
      {
        "featureName": "deny_sum",
        "featureEnabled": true,
        "importance": 1,
        "aggregationQuery": {"deny_sum": {"sum": {"field": "deny"}}}
      }
    ],
    "detectionInterval": {"period": {"interval": 2, "unit": "Minutes"}},
    "windowDelay": {"period": {"interval": 1, "unit": "Minutes"}},
    "shingleSize": 8,
    "history": 1000
  }'
```

The response returns the detector ID in the `id` field.

```
{"ok": true, "response": {"id": "2d67c887-9420-4078-8b2c-fb5ce4830487", "name": "deny-anomalies"}}
```

Note the following serverless-specific requirements:
+ `indices` must contain exactly one index. For more information, see [Choosing a collection type for anomaly detection](#serverless-ad-collection-type).
+ `resultIndex` is required and must begin with `opensearch-ad-plugin-result-`. For more information, see [Custom result indexes](#serverless-ad-result-index).
+ The operation creates the detector in a disabled state. To start it, see [Example: Start and stop a detector](#serverless-ad-api-start).

### Example: Start and stop a detector
<a name="serverless-ad-api-start"></a>

Send the start request without a body to begin real-time detection. The detector evaluates new data at each detection interval.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/{{detector_id}}/start/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

```
{"ok": true, "response": {"_id": "2d67c887-9420-4078-8b2c-fb5ce4830487"}}
```

To run a historical analysis over a past time range instead, include `startTime` and `endTime` in the request body, as epoch milliseconds. The response returns the ID of the historical analysis task.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/{{detector_id}}/start/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0" \
  -d '{"startTime": 1778363544000, "endTime": 1781041944000}'
```

```
{"ok": true, "response": {"_id": "e3d68a89-d50f-4d9f-8284-21865795f886"}}
```

To stop real-time detection, send a stop request with {{is\_historical}} set to `false`. Use `true` to stop a historical analysis.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/{{detector_id}}/stop/false/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

### Example: Profile a detector
<a name="serverless-ad-api-profile"></a>

Profiling returns the runtime state of a detector, such as whether it's initializing or running and how far model initialization has progressed.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X GET \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/{{detector_id}}/_profile/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

```
{"ok": true, "response": {"state": "RUNNING", "error": "", "init_progress": {"percentage": "100%"}}}
```

Use the `type` query parameter to request specific profile types as a comma-separated list. The following example requests entity counts for a high cardinality detector.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X GET \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/{{detector_id}}/_profile/{{data_source_id}}?type=total_entities,active_entities' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

```
{"ok": true, "response": {"total_entities": 10000, "active_entities": 28721}}
```

### Example: List, search, and count detectors
<a name="serverless-ad-api-list"></a>

The list operation returns the detectors in the workspace along with their anomaly counts, which is the view that the OpenSearch UI detector list uses.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X GET \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/_list?dataSourceId={{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

The search operation runs a query against the detector configurations.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/_search?dataSourceId={{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0" \
  -d '{"query": {"match_all": {}}, "size": 1}'
```

The following example shows a truncated search response.

```
{
  "ok": true,
  "response": {
    "totalDetectors": 11,
    "detectors": [
      {
        "id": "bf1e824f-2867-4a2d-8c6a-5388e5452061",
        "name": "deny-anomalies",
        "timeField": "@timestamp",
        "indices": ["server-metrics"],
        "resultIndex": "opensearch-ad-plugin-result-deny-anomalies",
        "detectionInterval": {"period": {"unit": "Minutes", "interval": 2}},
        "windowDelay": {"period": {"unit": "Minutes", "interval": 1}},
        "shingleSize": 8,
        "detectorType": "SINGLE_ENTITY",
        "history": 1000,
        "dataSourceId": "ef581a74-e4e6-3fab-a5b4-9bffd8d4af64",
        "lastUpdateTime": 1781030925933,
        "filterQuery": {"match_all": {"boost": 1}},
        "featureAttributes": [
          {
            "featureId": "QQe3rZ4BN4hgnuM8MSjG",
            "featureEnabled": true,
            "featureName": "deny_sum",
            "aggregationQuery": {"deny_sum": {"sum": {"field": "deny"}}}
          }
        ],
        "enabled": false
      }
    ]
  }
}
```

The count operation returns the number of detectors in the workspace. Use it to check your usage against the detector quota.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X GET \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/_count/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

```
{"ok": true, "response": {"count": 303}}
```

### Example: Search anomaly results and tasks
<a name="serverless-ad-api-results"></a>

The following example queries the anomaly results that the detector wrote to its custom result index.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/results/_search/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0" \
  -d '{
    "size": 5,
    "sort": [{"data_end_time": {"order": "desc"}}],
    "query": {
      "bool": {
        "filter": [
          {"term": {"detector_id": "{{detector_id}}"}},
          {"range": {"anomaly_grade": {"gt": 0}}}
        ]
      }
    }
  }'
```

Detector tasks track individual real-time and historical runs. Task documents include the task state, progress, execution times, and the detector configuration that the task ran with.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/tasks/_search/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0" \
  -d '{"query": {"match_all": {}}, "size": 1}'
```

The following example shows a truncated response.

```
{
  "ok": true,
  "response": {
    "hits": {
      "total": {"value": 26, "relation": "eq"},
      "hits": [
        {
          "_index": "opendistro-anomaly-detection-state",
          "_id": "916eed3b-8785-4cf0-8cb4-ab7191d2845e",
          "_source": {
            "detector_id": "c6eb3d92-371c-4e1b-8480-09dad082f3a0",
            "task_type": "HISTORICAL_HC_ENTITY",
            "state": "FINISHED",
            "task_progress": 1,
            "init_progress": 1,
            "is_latest": true,
            "detection_date_range": {
              "start_time": 1778426808849,
              "end_time": 1781018808849
            },
            "execution_start_time": 1781018874002,
            "execution_end_time": 1781018913066,
            "entity": [{"name": "service", "value": "app_3"}]
          }
        }
      ]
    },
    "took": 12,
    "timed_out": false
  }
}
```

### Example: Preview a detector
<a name="serverless-ad-api-preview"></a>

Preview runs a detector configuration over a past time range and returns sample anomaly results without creating the detector. The preview request body uses camelCase field names, and it nests the detector configuration under a `detector` field.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/preview/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0" \
  -d '{
    "periodStart": 1778363544000,
    "periodEnd": 1781041944000,
    "detector": {
      "name": "preview-test",
      "description": "preview",
      "indices": ["server-metrics"],
      "resultIndex": "opensearch-ad-plugin-result-preview",
      "filterQuery": {"match_all": {}},
      "timeField": "@timestamp",
      "featureAttributes": [
        {
          "featureName": "deny_sum",
          "featureEnabled": true,
          "importance": 1,
          "aggregationQuery": {"deny_sum": {"sum": {"field": "deny"}}}
        }
      ],
      "detectionInterval": {"period": {"interval": 2, "unit": "Minutes"}},
      "windowDelay": {"period": {"interval": 1, "unit": "Minutes"}},
      "shingleSize": 8
    }
  }'
```

### Example: Get anomaly detection statistics
<a name="serverless-ad-api-stats"></a>

```
awscurl --service opensearch --region {{us-west-2}} \
  -X GET \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/stats/ad_execute_request_count,ad_execute_failure_count,anomaly_results_index_status,anomaly_detectors_index_status,models_checkpoint_index_status/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

```
{
  "ok": true,
  "response": {
    "anomaly_detectors_index_status": "green",
    "models_checkpoint_index_status": "green",
    "anomaly_results_index_status": "green",
    "nodes": {
      "node-1": {"ad_execute_request_count": 341, "ad_execute_failure_count": 0},
      "node-2": {"ad_execute_request_count": 60, "ad_execute_failure_count": 0},
      "node-3": {"ad_execute_request_count": 744, "ad_execute_failure_count": 0},
      "node-4": {"ad_execute_request_count": 1336, "ad_execute_failure_count": 78}
    }
  }
}
```

### Example: Delete a detector
<a name="serverless-ad-api-delete"></a>

Stop the detector before you delete it. Deleting a detector doesn't delete its custom result index or the results in it.

```
awscurl --service opensearch --region {{us-west-2}} \
  -X DELETE \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/anomaly_detectors/detectors/{{detector_id}}/{{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```