

# Configuring alerting for Amazon OpenSearch Serverless
<a name="serverless-configure-alerting"></a>

Alerting automatically monitors your OpenSearch data on a defined schedule and notifies you when trigger conditions are met. A monitor is a job that runs a query against your data, evaluates trigger conditions, and generates alerts. When a trigger fires, the monitor runs actions that send notifications through configured channels. For a conceptual overview of monitors, triggers, and actions, see [Alerting](https://docs.opensearch.org/latest/observing-your-data/alerting/index/) on the OpenSearch website.

Serverless alerting uses an Amazon OpenSearch Serverless collection as the monitor's data source. You create and manage monitors from OpenSearch UI. Each monitor is a resource of the OpenSearch UI workspace that you create it in. This page describes the prerequisites, permissions, and considerations that are specific to serverless collections. It also documents the workspace-scoped API operations that you use to manage monitors programmatically.

**Important**  
Monitors are OpenSearch UI workspace resources. As a result, the alerting API operations for serverless collections differ from the open source alerting API operations under `_plugins/_alerting`. Use the workspace-scoped operations in [Alerting API operations for serverless collections](#serverless-configure-alerting-api).

## Prerequisites
<a name="serverless-configure-alerting-prerequisites"></a>
+ A collection that contains the indexes you want to monitor. We recommend a time series collection. For more information, see [Choosing a collection type for alerting](#serverless-configure-alerting-collection-type).
+ An OpenSearch UI application with a workspace that has the collection attached as a data source. For more information, see [Using OpenSearch UI in Amazon OpenSearch Service](application.md).
+ Your user role must trust the OpenSearch UI service principal (`application.opensearchservice.amazonaws.com`). You configure this trust policy during application setup. For more information, see [Using OpenSearch UI in Amazon OpenSearch Service](application.md).

## Choosing a collection type for alerting
<a name="serverless-configure-alerting-collection-type"></a>

We recommend that you use alerting together with a time series collection. A monitor on a serverless collection must reference concrete index names – index patterns, aliases, and wildcard expressions aren't supported. A time series collection automatically manages data retention for the monitored indexes, so you don't have to build a custom retention process.

Keep the following considerations in mind:
+ **Concrete index names only** – A monitor must reference concrete index names. Index patterns (for example, `logs-*`), aliases, and comma-separated lists of multiple indexes aren't supported.
+ **Automatic data retention** – Time series collections manage the lifecycle of the data in the monitored indexes for you. This pairs well with alerting, because monitored indexes that grow without bounds would otherwise require you to manage retention yourself.
+ **Search collections** – Search collections are also accepted as a monitor data source, but they don't manage data retention for you.

For more information about collection types, see [Choosing a collection type](serverless-overview.md#serverless-usecase).

## Configuring permissions for alerting
<a name="serverless-configure-alerting-permissions"></a>

Monitors run as background jobs against your collection. The following collection data access policy grants the permissions that alerting requires. Replace the {{placeholder values}} with your specific information. For more information, see [Supported policy permissions](serverless-data-access.md#serverless-data-supported-permissions).

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
    "Description": "Alerting access policy for {{collection_name}}"
}
```
+ Collection permissions (`aoss:CreateCollectionItems`, `aoss:DeleteCollectionItems`, `aoss:UpdateCollectionItems`, `aoss:DescribeCollectionItems`) – Allow the alerting job to resolve and operate on the collection.
+ Index permissions (`aoss:CreateIndex`, `aoss:DeleteIndex`, `aoss:UpdateIndex`, `aoss:DescribeIndex`, `aoss:ReadDocument`, `aoss:WriteDocument`) – Allow the monitor to read the monitored indexes. They also allow the monitor to create and write to the internal alert history indexes that the alerting plugin manages.
+ `aoss:DelegateAccess` – Allows the alerting background job to access the collection on your behalf.

**Important**  
`aoss:DelegateAccess` lets the alerting background job run against the collection, and `aoss:ReadDocument` lets monitor executions query the monitored indexes. You can scope the index resource to specific indexes instead of `index/{{collection_name}}/*`. In that case, cover every index that a monitor references as well as the internal alert history indexes that the alerting plugin writes to.

Within an OpenSearch UI workspace, access to alerting features follows the workspace collaborator permissions (read-only, read/write, or admin). Read-only collaborators can view monitors, alerts, and notification channels. Read/write and admin collaborators can create, update, enable, disable, and delete monitors, and can acknowledge and mute alerts.

## Supported monitor types
<a name="serverless-configure-alerting-monitor-types"></a>

Serverless collections support the following monitor types:
+ **Per-query monitors** – Run a single query and evaluate trigger conditions against the aggregated result. Use a per-query monitor when you want to alert on a single aggregated metric, such as the average response latency exceeding a threshold.
+ **Per-bucket monitors** – Run a query with a composite aggregation and evaluate trigger conditions against each bucket. Use a per-bucket monitor when you want to alert on individual groups within your data, such as each host exceeding an error rate.
+ **PPL monitors** – Run a Piped Processing Language (PPL) query and evaluate trigger conditions against the result. Use a PPL monitor when you want to express complex filtering, transformation, or statistical logic in a piped query language. For PPL syntax, see [PPL](https://docs.opensearch.org/latest/sql-and-ppl/ppl/index/) on the OpenSearch website.

Other monitor types – including per-document monitors, composite monitors, and per-cluster-metrics monitors – aren't available for serverless collections.

## Using anomaly detection with alerting
<a name="serverless-configure-alerting-anomaly"></a>

To receive a notification when an anomaly detector finds an anomaly, create a monitor that queries the detector's custom result index. Anomaly detectors on serverless collections write results to a custom result index in the same collection, which means you can use a standard per-query or per-bucket monitor with a trigger on `anomaly_grade` and `confidence`.

Complete the following steps:

1. Set up anomaly detection and create a detector with a custom result index. For more information, see [Configuring anomaly detection on Amazon OpenSearch Serverless](serverless-configure-anomaly-detection.md).

1. Create a monitor in OpenSearch UI against the detector's custom result index (for example, `opensearch-ad-plugin-result-my-detector`). For guidance on the trigger conditions to use for anomaly results, see [Anomaly detection](https://docs.opensearch.org/latest/observing-your-data/ad/index/) on the OpenSearch website.

1. Add a notification channel to the trigger so that the alert reaches your destination of choice.

**Note**  
The anomaly detector monitor type from the open source alerting plugin isn't available on serverless collections, because it reads from the default anomaly result index. Query the custom result index with a per-query or per-bucket monitor instead.

## Considerations and limitations
<a name="serverless-configure-alerting-considerations"></a>

Alerting on OpenSearch Serverless has the following considerations and limitations:
+ Aliases aren't supported. Monitors must reference concrete index names.
+ Wildcard index patterns aren't supported. Monitors must reference concrete index names (for example, `logs-*` isn't allowed).
+ Per-bucket monitors support a single trigger.
+ Per-document monitors, composite monitors, and per-cluster-metrics monitors aren't available for serverless collections.
+ Alerting settings, such as alert history retention, are managed by the service and can't be modified.
+ You must disable a monitor before you update or delete it.

## Alerting API operations for serverless collections
<a name="serverless-configure-alerting-api"></a>

Serverless collections support all of the monitor and alert operations in the open source [Alerting API](https://docs.opensearch.org/latest/observing-your-data/alerting/api/) on the OpenSearch website. However, you call them with workspace-style paths. Monitors are OpenSearch UI workspace resources, so you send requests to your OpenSearch UI application endpoint rather than to the collection endpoint. Each path includes a workspace and identifies the data source that represents your collection.

Use a SigV4-signing HTTP client such as [awscurl](https://github.com/okigan/awscurl) on the GitHub website to call the operations. The following sections describe the request format, list the operation paths, and show representative examples.

### Request format
<a name="serverless-configure-alerting-api-request-format"></a>

Requests use the following format:

```
https://{{application_endpoint}}/w/{{workspace_id}}/api/alerting/{{operation_path}}
```

The following table describes each part of the request.


| Component | Description | 
| --- | --- | 
| application\_endpoint | The endpoint of your OpenSearch UI application, in the format application-{{application\_name}}-{{application\_id}}.{{region}}.opensearch.amazonaws.com. | 
| workspace\_id | The ID of the OpenSearch UI workspace that contains the monitor. You can find it in the /w/ segment of the workspace URL in the OpenSearch UI console. | 
| data\_source\_id | The ID of the data source in the workspace that represents your collection. Depending on the operation, you pass this value either as the last segment of the path or as a dataSourceId query parameter. | 
| monitor\_id | The ID of a monitor, returned in the id field when you create or search for monitors. | 

Sign every request with Signature Version 4 (SigV4), using `opensearch` as the service name. Include the following headers on every request:
+ `Content-Type: application/json` – Required on requests that send a body.
+ `osd-xsrf: osd-fetch` – Required cross-site request forgery header.
+ `osd-version: 3.6.0` – The OpenSearch version of your OpenSearch UI application.

Each response uses an envelope. A successful response returns `{"ok": true, "response": {...}}`, and a failed response returns `{"ok": false, "error": "message"}`.

### Operation paths
<a name="serverless-configure-alerting-api-operations"></a>

The following table lists the alerting operations and their workspace-style paths. All paths are relative to `https://{{application_endpoint}}/w/{{workspace_id}}/api/alerting`.


| Operation | Method | Path | 
| --- | --- | --- | 
| Create a monitor | POST | monitors?dataSourceId={{data\_source\_id}} | 
| Get a monitor | GET | monitors/{{monitor\_id}}?dataSourceId={{data\_source\_id}} | 
| Update a monitor | PUT | monitors/{{monitor\_id}}?dataSourceId={{data\_source\_id}} | 
| Delete a monitor | DELETE | monitors/{{monitor\_id}}?dataSourceId={{data\_source\_id}} | 
| Search monitors | POST | monitors/\_search?dataSourceId={{data\_source\_id}} | 
| Execute a monitor | POST | monitors/{{monitor\_id}}/\_execute?dataSourceId={{data\_source\_id}} | 
| Get alerts | GET | monitors/alerts?dataSourceId={{data\_source\_id}} | 
| Acknowledge alerts | POST | monitors/{{monitor\_id}}/\_acknowledge/alerts?dataSourceId={{data\_source\_id}} | 

**Note**  
You must disable a monitor before you update or delete it. Alerts can take a few minutes to appear after you enable a monitor.

### Example: Create a monitor
<a name="serverless-configure-alerting-api-example-create"></a>

The following example creates a per-query monitor that checks for error spikes in server logs every 5 minutes.

```
awscurl --service opensearch --region us-west-2 \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/alerting/monitors?dataSourceId={{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0" \
  -d '{
    "type": "monitor",
    "name": "error-spike-monitor",
    "monitor_type": "query_level_monitor",
    "enabled": false,
    "schedule": {
      "period": { "interval": 5, "unit": "MINUTES" }
    },
    "inputs": [{
      "search": {
        "indices": ["server-logs"],
        "query": {
          "size": 0,
          "query": {
            "bool": {
              "filter": [
                {"range": {"@timestamp": {"gte": "{{period_end}}||-5m", "lte": "{{period_end}}", "format": "epoch_millis"}}},
                {"term": {"level": "ERROR"}}
              ]
            }
          },
          "aggregations": {
            "error_count": {"value_count": {"field": "_id"}}
          }
        }
      }
    }],
    "triggers": [{
      "query_level_trigger": {
        "name": "High error count",
        "severity": "1",
        "condition": {
          "script": {
            "source": "ctx.results[0].aggregations.error_count.value > 100",
            "lang": "painless"
          }
        },
        "actions": []
      }
    }]
  }'
```

The response returns the monitor ID in the `id` field.

```
{"ok": true, "response": {"id": "a3f8c214-7b62-4e91-9d05-1c3b6f4e8a92", "name": "error-spike-monitor"}}
```

Note the following serverless-specific requirements:
+ `indices` must contain concrete index names. Wildcards and aliases aren't supported. For more information, see [Choosing a collection type for alerting](#serverless-configure-alerting-collection-type).
+ The operation creates the monitor in a disabled state. Enable it with the update operation by setting `"enabled": true`.

### Example: Execute a monitor
<a name="serverless-configure-alerting-api-example-execute"></a>

The execute operation runs the monitor's query immediately and returns the results without waiting for the next scheduled interval. Use this to test a monitor's query and triggers before enabling it.

```
awscurl --service opensearch --region us-west-2 \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/alerting/monitors/{{monitor_id}}/_execute?dataSourceId={{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

```
{
  "ok": true,
  "response": {
    "monitor_name": "error-spike-monitor",
    "period_start": 1781041644000,
    "period_end": 1781041944000,
    "error": null,
    "input_results": {
      "results": [{"aggregations": {"error_count": {"value": 42}}}]
    },
    "trigger_results": {
      "trigger-id": {
        "name": "High error count",
        "triggered": false,
        "action_results": {}
      }
    }
  }
}
```

### Example: Search monitors and get alerts
<a name="serverless-configure-alerting-api-example-search"></a>

The search operation runs a query against the monitor configurations in the workspace.

```
awscurl --service opensearch --region us-west-2 \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/alerting/monitors/_search?dataSourceId={{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0" \
  -d '{"query": {"match_all": {}}, "size": 1}'
```

```
{
  "ok": true,
  "response": {
    "totalMonitors": 8,
    "monitors": [{
      "id": "a3f8c214-7b62-4e91-9d05-1c3b6f4e8a92",
      "name": "error-spike-monitor",
      "monitor_type": "query_level_monitor",
      "enabled": true,
      "schedule": {"period": {"interval": 5, "unit": "MINUTES"}},
      "inputs": [{"search": {"indices": ["server-logs"], "query": {}}}],
      "triggers": [{"query_level_trigger": {"name": "High error count", "severity": "1"}}],
      "last_update_time": 1781030925933,
      "dataSourceId": "ef581a74-e4e6-3fab-a5b4-9bffd8d4af64"
    }]
  }
}
```

The get alerts operation returns all active alerts across the monitors in the workspace.

```
awscurl --service opensearch --region us-west-2 \
  -X GET \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/alerting/monitors/alerts?dataSourceId={{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

```
{
  "ok": true,
  "response": {
    "alerts": [{
      "id": "d7e5b324-1f93-4a2d-bc89-6e4f1d2c3a56",
      "monitor_id": "a3f8c214-7b62-4e91-9d05-1c3b6f4e8a92",
      "monitor_name": "error-spike-monitor",
      "trigger_name": "High error count",
      "state": "ACTIVE",
      "severity": "1",
      "start_time": 1781041944000,
      "last_notification_time": 1781041944000
    }],
    "totalAlerts": 1
  }
}
```

### Example: Acknowledge alerts
<a name="serverless-configure-alerting-api-example-acknowledge"></a>

Acknowledging an alert moves it from the `ACTIVE` state to the `ACKNOWLEDGED` state, which prevents further notification actions from firing for that alert until the trigger condition resets.

```
awscurl --service opensearch --region us-west-2 \
  -X POST \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/alerting/monitors/{{monitor_id}}/_acknowledge/alerts?dataSourceId={{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0" \
  -d '{"alerts": ["d7e5b324-1f93-4a2d-bc89-6e4f1d2c3a56"]}'
```

```
{"ok": true, "response": {"success": ["d7e5b324-1f93-4a2d-bc89-6e4f1d2c3a56"], "failed": []}}
```

### Example: Delete a monitor
<a name="serverless-configure-alerting-api-example-delete"></a>

Disable the monitor before you delete it. Deleting a monitor doesn't delete the alerts it previously generated.

```
awscurl --service opensearch --region us-west-2 \
  -X DELETE \
  'https://{{application_endpoint}}/w/{{workspace_id}}/api/alerting/monitors/{{monitor_id}}?dataSourceId={{data_source_id}}' \
  -H "Content-Type: application/json" \
  -H "osd-xsrf: osd-fetch" \
  -H "osd-version: 3.6.0"
```

```
{"ok": true, "response": {}}
```