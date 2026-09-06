

# Payload Requirements For Ingesting APM Alerts with EventBridge
<a name="idr-gs-apm-payload-requirements"></a>

**Where does Incident Detection and Response ingest APM alerts from?**

AWS Incident Detection and Response installs a managed rule on the event bus that you send your final transformed payload to. It's a best practice to create a custom event bus for this purpose.

**What format must payloads be in?**

The following minimum JSON key:value pairs are required in event bus events ingested by AWS Incident Detection and Response:

```
{  
    "detail-type": "ams.monitoring/generic-apm",  
    "source": "GenericAPMEvent"  
    "detail": {  
        "incident-detection-response-identifier": "Your alarm name from your APM",  
    }  
}
```

The following examples show an event from a partner event bus before and after it is transformed.

**Before transformation:**

```
{  
    "version": "0",  
    "id": "a6150a80-601d-be41-1a1f-2c5527a99199",  
    "detail-type": "Datadog Alert Notification",  
    "source": "aws.partner/datadog.com/Datadog-aaa111bbbc",  
    "account": "123456789012",  
    "time": "2023-10-25T14:42:25Z",  
    "region": "us-east-1",  
    "resources": [],  
    "detail": {  
        "alert_type": "error",  
        "event_type": "query_alert_monitor",  
        "meta": {  
            "monitor": {  
                "id": 222222,  
                "org_id": 3333333333,  
                "type": "query alert",  
                "name": "UnHealthyHostCount",  
                "message": "@awseventbridge-Datadog-aaa111bbbc",  
                "query": "max(last_5m):avg:aws.applicationelb.un_healthy_host_count{aws_account:123456789012} <= 1",  
                "created_at": 1686884769000,  
                "modified": 1698244915000,  
                "options": {  
                    "thresholds": {  
                        "critical": 1.0  
                    }  
                },  
            },  
            "result": {  
                "result_id": 7281010972796602670,  
                "result_ts": 1698244878,  
                "evaluation_ts": 1698244868,  
                "scheduled_ts": 1698244938,  
                "metadata": {  
                    "monitor_id": 222222,  
                    "metric": "aws.applicationelb.un_healthy_host_count"  
                }  
            },  
            "transition": {  
                "trans_name": "Triggered",  
                "trans_type": "alert"  
            },  
            "states": {  
                "source_state": "OK",  
                "dest_state": "Alert"  
            },  
            "duration": 0  
        },  
        "priority": "normal",  
        "source_type_name": "Monitor Alert",  
        "tags": [  
            "aws_account:123456789012",  
            "monitor"  
        ]  
    }  
}
```

Note that before the event is transformed, `detail-type` and `source` indicates the APM details where the alert originated. These must be modified before ingestion. The `incident-detection-response-identifier` key is not yet present and must also be added before ingestion.

An Lambda Function transforms the above event and puts it in to the target custom or default event bus. The transformed payload must include the required key:value pairs.

**After transformation:**

```
{  
    "version": "0",  
    "id": "7f5e0fc1-e917-2b5d-a299-50f4735f1283",  
    "detail-type": "ams.monitoring/generic-apm",  
    "source": "GenericAPMEvent",  
    "account": "123456789012",  
    "time": "2023-10-25T14:42:25Z",  
    "region": "us-east-1",  
    "resources": [],  
    "detail": {  
        "incident-detection-response-identifier": "UnHealthyHostCount",  
        "alert_type": "error",  
        "event_type": "query_alert_monitor",  
        "meta": {  
            "monitor": {  
                "id": 222222,  
                "org_id": 3333333333,  
                "type": "query alert",  
                "name": "UnHealthyHostCount",  
                "message": "@awseventbridge-Datadog-aaa111bbbc",  
                "query": "max(last_5m):avg:aws.applicationelb.un_healthy_host_count{aws_account:123456789012} <= 1",  
                "created_at": 1686884769000,  
                "modified": 1698244915000,  
                "options": {  
                    "thresholds": {  
                        "critical": 1.0  
                    }  
                },  
            },  
            "result": {  
                "result_id": 7281010972796602670,  
                "result_ts": 1698244878,  
                "evaluation_ts": 1698244868,  
                "scheduled_ts": 1698244938,  
                "metadata": {  
                    "monitor_id": 222222,  
                    "metric": "aws.applicationelb.un_healthy_host_count"  
                }  
            },  
            "transition": {  
                "trans_name": "Triggered",  
                "trans_type": "alert"  
            },  
            "states": {  
                "source_state": "OK",  
                "dest_state": "Alert"  
            },  
            "duration": 0  
        },  
        "priority": "normal",  
        "source_type_name": "Monitor Alert",  
        "tags": [  
            "aws_account:123456789012",  
            "monitor"  
        ]  
    }  
}
```

Note that `detail-type` is now `ams.monitoring/generic-apm`, source is now `GenericAPMEvent`, and under detail there is new key:value pair: `incident-detection-response-identifier`.

The `incident-detection-response-identifier` value is taken from the alert name based on whatever payload your APM sends. APM alert name paths are different from one APM to another. An Lambda function must be set up to take the alarm name from the correct path in the APM JSON payload received by Lambda and use it for the `incident-detection-response-identifier` value.

`incident-detection-response-identifier` values must be unique per alarm type sent to AWS Incident Detection and Response. Each unique name that is set on the `incident-detection-response-identifier` must be provided to the AWS Incident Detection and Response team during on-boarding. Events that have an unknown or missing value for the `incident-detection-response-identifier` key are not processed.