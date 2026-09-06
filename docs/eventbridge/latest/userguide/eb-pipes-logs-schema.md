

# EventBridge Pipes log schema reference
<a name="eb-pipes-logs-schema"></a>

The following reference details the schema for EventBridge Pipes log records.

Each log record represents a pipe execution step, and may contain up to 10,000 events if the pipe source and target have been configured for batching.

For more information, see [Logging Amazon EventBridge Pipes performance](eb-pipes-logs.md).

```
{
    "executionId": "{{guid}}",
    "timestamp": "{{date_time}}",
    "messageType": "{{execution_step}}",
    "resourceArn": "arn:aws:pipes:{{region}}:{{account}}:pipe/{{pipe-name}}",
    "logLevel": "{{TRACE}} | {{INFO}} | {{ERROR}}",
    "payload": "{}",
    "awsRequest": "{}"
    "awsResponse":"{}"
    "truncatedFields": [{{"awsRequest","awsResponse","payload"}}],
    "error": {
        "httpStatusCode": {{code}},
        "message": "{{error_message}}",
        "details": "",
        "awsService": "{{service_name}}",
        "requestId": "{{service_request_id}}"
    }
}
```

**executionId**  <a name="pipe-log-schema-execution-id"></a>
The ID of the pipe execution.  
A pipe execution is an event or batch of events received by a pipe that travel to an enrichment or target. For more information, see [How Amazon EventBridge Pipes logging works](eb-pipes-logs.md#eb-pipes-logs-overview).

**timestamp**  <a name="pipe-log-schema-timestamp"></a>
The date and time the log event was emitted.  
Unit: millisecond

**messageType**  <a name="pipe-log-schema-message-type"></a>
The pipe execution step for which the record was generated.  
For more information on pipe execution steps, see [EventBridge Pipes execution steps](eb-pipes-logs-execution-steps.md).

**resourceArn**  <a name="pipe-log-schema-resource-arn"></a>
The Amazon Resource Name (ARN) for the pipe.

**logLevel**  <a name="pipe-log-schema-loglevel"></a>
The level of detail specified for the pipe log.  
*Valid values*: `ERROR` \| `INFO` \| `TRACE`  
For more information, see [Specifying EventBridge Pipes log level](eb-pipes-logs.md#eb-pipes-logs-level).

**payload**  <a name="pipe-log-schema-payload"></a>
The contents of the event batch being processed by the pipe.  
EventBridge includes this field only if you have specified to include execution data in the logs for this pipe. For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data)  
These fields may contain sensitive information. EventBridge makes no attempt to redact the contents of these fields during logging.
For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data).

**awsRequest**  <a name="pipe-log-schema-aws-request"></a>
The request sent to the enrichment or target, in JSON format. For requests sent to an API destination, this represents the HTTP request sent to that endpoint.  
EventBridge includes this field only if you have specified to include execution data in the logs for this pipe. For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data)  
These fields may contain sensitive information. EventBridge makes no attempt to redact the contents of these fields during logging.
For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data).

**awsResponse**  <a name="pipe-log-schema-aws-response"></a>
The response returned by the enrichment or target, in JSON format. For requests sent to an API destination, this represents the HTTP response returned from that endpoint, and not the response returned by the API Destination service itself.  
EventBridge includes this field only if you have specified to include execution data in the logs for this pipe. For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data)  
These fields may contain sensitive information. EventBridge makes no attempt to redact the contents of these fields during logging.
For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data).

**truncatedFields**  <a name="pipe-log-schema-truncated-fields"></a>
A list of any execution data fields EventBridge has truncated to keep the record below the 256 KB size limitation.  
If EventBridge did not have to truncate any of the execution data fields, this field is present but `null`.  
For more information, see [Truncating execution data in EventBridge Pipes log records](eb-pipes-logs.md#eb-pipes-logs-execution-data-truncation).

**error**  <a name="pipe-log-schema-error"></a>
Contains information for any error generated during this pipe execution step.   
If no error was generated during this pipe execution step, this field is present but `null`.    
**httpStatusCode**  <a name="pipe-log-schema-http-status-code"></a>
The HTTP status code returned by the called service.  
**message**  <a name="pipe-log-schema-message"></a>
The error message returned by the called service.  
**details**  <a name="pipe-log-schema-details"></a>
Any detailed error information returned by the called service.  
**awsService**  <a name="pipe-log-schema-aws-service"></a>
The name of the service called.  
**requestId**  <a name="pipe-log-schema-request-id"></a>
The request ID for this request from the called service.