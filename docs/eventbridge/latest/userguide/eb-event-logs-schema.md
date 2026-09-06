

# Amazon EventBridge event bus log schema
<a name="eb-event-logs-schema"></a>

The following reference details the schema for EventBridge event bus log records. Each record represent a step EventBridge performs processing a specific event.

For more information, see [Logging event buses ](eb-event-bus-logs.md).

```
{    
    "resource\_arn": "arn:aws:events:{{region}}:{{account}}:event-bus/{{bus-name}}",
    "request\_id": "{{guid}}", 
    "event\_id": "{{guid}}", 
    "invocation\_id": "{{guid}}",
    "message\_timestamp\_ms": "{{date_time}}",    
    "message\_type": "{{step}}",  
    "log\_level": "{{TRACE}} | {{INFO}} | {{ERROR}}",
    "details": {
      },
    "error": {  
        "http\_status\_code": {{code}},  
        "error\_message": "{{error_message}}",  
        "aws\_service": "{{service_name}}",  
        "request\_id": "{{service_request_id}}"  
    }  
}
```

**resource\_arn**  <a name="event-log-schema-resource-arn"></a>
The Amazon Resource Name (ARN) for the event bus.

**request\_id**  <a name="event-log-schema-request-id"></a>
The ID of the request.

**event\_id**  <a name="event-log-schema-event-id"></a>
The ID of the event being processed.

**invocation\_id**  <a name="event-log-schema-invocation-id"></a>
The ID of the invocation for the event.

**message\_timestamp\_ms**  <a name="event-log-schema-timestamp"></a>
The date and time the log event was emitted.  
Unit: millisecond

**message\_type**  <a name="event-log-schema-message-type"></a>
The event processing step for which the log record was generated.  
For more information on the steps EventBridge performs when processing an event, see [What Amazon EventBridge logs for event buses](eb-event-logs-execution-steps.md).  
*Valid values:*  
+ `EVENT_INGEST_FAILURE`
+ `EVENT_INGEST_SUCCESS`
+ `EVENT_RECEIPT`
+ `INVOCATION_ATTEMPT_PERMANENT_FAILURE`
+ `INVOCATION_ATTEMPT_RETRYABLE_FAILURE`
+ `INVOCATION_ATTEMPT_START`
+ `INVOCATION_ATTEMPT_SUCCESS`
+ `INVOCATION_ATTEMPT_THROTTLE`
+ `INVOCATION_DLQ`
+ `INVOCATION_FAILURE`
+ `INVOCATION_START`
+ `INVOCATION_SUCCESS`
+ `INVOCATION_THROTTLE_START`
+ `NO_STANDARD_RULES_MATCHED`
+ `RULE_MATCH`
+ `RULE_MATCH_START`

**log\_level**  <a name="event-log-schema-loglevel"></a>
The level of detail specified for the event bus log.  
*Valid values*: `ERROR` \| `INFO` \| `TRACE`  
For more information, see [Specifying event bus log level](eb-event-bus-logs.md#eb-event-bus-logs-level).

**details**  <a name="event-log-schema-details"></a>
Contains step details, based on the step detail type.  
The fields listed below are returned for the following message types:  
+ `EVENT_INGEST_SUCCESS`
+ `EVENT_INGEST_FAILURE`
+ `EVENT_RECEIPT`
+ `RULE_MATCH_START`

```
{
  "caller_account_id": "{{account_id}}",
  "source_time_ms": {{date_time}},
  "source": "{{source}}",
  "detail_type": " {{type}}",
  "resources": [],
  "event_detail": "{}"
}
```
The fields listed below are returned for the following message type:  
+ `RULE_MATCH`

```
{
  "rule_arn": "{{ARN}}",
  "target_arns": [
    "{{ARN}}"
  ],
  "invocation_ids": [
    "{{guid}}"
  ]
}
```
The fields listed below are returned for the following message types:  
+ `INVOCATION_ATTEMPT_START`
+ `INVOCATION_START`
+ `INVOCATION_THROTTLE_START`

```
{
  "rule_arn": "{{ARN}}",
  "role_arn": "{{ARN}}",
  "target_arn": "{{ARN}}",
  "attempt_count": {{Integer}},
  "target_input": "{{string}}",
  "target_properties": "{{string}}"
}
```
The fields listed below are returned for the following message types:  
+ `INVOCATION_DLQ`
+ `INVOCATION_FAILURE`
+ `INVOCATION_SUCCESS`

```
{
  "rule_arn": "{{ARN}}",
  "role_arn": "{{ARN}}",
  "target_arn": "{{ARN}}",
  "target_input": "{{string}}",
  "target_properties": "{{string}}",
  "total_attempts": {{Integer}},
  "final_invocation_status": "{{status}}",
  "ingestion_to_start_latency_ms": {{Integer}},
  "ingestion_to_complete_latency_ms": {{Integer}},
  "ingestion_to_success_latency_ms": {{Integer}},
  "target_duration_ms": {{Integer}},
  "target_response_body": "{{string}}"
}
```
The `ingestion_to_start_latency_ms` and `ingestion_to_complete_latency_ms` are only included in the first invocation attempt. The `ingestion_to_success_latency_ms` field is only included for successful invocations.  
The fields listed below are returned for the following message types:  
+ `INVOCATION_ATTEMPT_PERMANENT_FAILURE`
+ `INVOCATION_ATTEMPT_RETRYABLE_FAILURE`
+ `INVOCATION_ATTEMPT_SUCCESS`
+ `INVOCATION_ATTEMPT_THROTTLE`

```
{
  "rule_arn": "{{ARN}}",
  "role_arn": "{{ARN}}",
  "target_arn": "{{ARN}}",
  "attempt_type": "{{FIRST}} | {{THROTTLE}} | {{RETRY}}",
  "attempt_count": {{Integer}},
  "invocation_status": "{{status}}",
  "target_duration_ms": {{Integer}},
  "target_response_body": "{{string}}"
}
```

**dropped\_fields**  <a name="event-log-schema-dropped_fields"></a>
A list of any data fields EventBridge has truncated to keep the record below the 1 MB size limitation.  
EventBridge does not include this field if it has truncated any detail fields.  
For more information, see [Truncating data in event bus logs](eb-event-bus-logs.md#eb-event-logs-data-truncation).

**error**  <a name="event-log-schema-error"></a>
Contains information for any error generated during this step. For errors, EV always includes the following fields:  
+ `error_message`
+ `aws_service`
And the following fields if available:  
+ `request_id`
+ `http_status_code`
If no error was generated during this step, EventBridge does not include this field in the log record.    
**http\_status\_code**  <a name="event-log-schema-http-status-code"></a>
The HTTP status code returned by the called service.  
**error\_message**  <a name="event-log-schema-message"></a>
The error message returned by the called service.  
**aws\_service**  <a name="event-log-schema-aws-service"></a>
The name of the service called.  
**request\_id**  <a name="event-log-schema-error-request-id"></a>
The request ID for this request from the called service.