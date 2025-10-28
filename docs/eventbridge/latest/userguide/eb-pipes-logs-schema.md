# EventBridge Pipes log schema reference

The following reference details the schema for EventBridge Pipes log records.

Each log record represents a pipe execution step, and may contain up to 10,000 events if
the pipe source and target have been configured for batching.

For more information, see [Logging Amazon EventBridge Pipes performance](eb-pipes-logs.md "eb-pipes-logs.md").

```
{
    "executionId": "`guid`",
    "timestamp": "`date_time`",
    "messageType": "`execution_step`",
    "resourceArn": "arn:aws:pipes:`region`:`account`:pipe/`pipe-name`",
    "logLevel": "`TRACE` | `INFO` | `ERROR`",
    "payload": "{}",
    "awsRequest": "{}"
    "awsResponse":"{}"
    "truncatedFields": [`"awsRequest","awsResponse","payload"`],
    "error": {
        "httpStatusCode": `code`,
        "message": "`error_message`",
        "details": "",
        "awsService": "`service_name`",
        "requestId": "`service_request_id`"
    }
}
```

**executionId**

The ID of the pipe execution.

A pipe execution is an event or batch of events received by a pipe that travel to an enrichment or target. For more information, see
[How Amazon EventBridge Pipes logging works](eb-pipes-logs.md#eb-pipes-logs-overview "eb-pipes-logs.md#eb-pipes-logs-overview").

**timestamp**

The date and time the log event was emitted.

Unit: millisecond

**messageType**

The pipe execution step for which the record was generated.

For more information on pipe execution steps, see [EventBridge Pipes execution steps](eb-pipes-logs-execution-steps.md "eb-pipes-logs-execution-steps.md").

**resourceArn**

The Amazon Resource Name (ARN) for the pipe.

**logLevel**

The level of detail specified for the pipe log.

_Valid values_: `ERROR` | `INFO` | `TRACE`

For more information, see [Specifying EventBridge Pipes log level](eb-pipes-logs.md#eb-pipes-logs-level "eb-pipes-logs.md#eb-pipes-logs-level").

**payload**

The contents of the event batch being processed by the pipe.

EventBridge includes this field only if you have specified to include execution data in the logs for this pipe. For more information, see
[Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data "eb-pipes-logs.md#eb-pipes-logs-execution-data")

###### Important

These fields may contain sensitive information. EventBridge makes no attempt to redact the contents
of these fields during logging.

For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data "eb-pipes-logs.md#eb-pipes-logs-execution-data").

**awsRequest**

The request sent to the enrichment or target, in JSON format. For requests sent to an API destination, this represents the HTTP request sent to that endpoint.

EventBridge includes this field only if you have specified to include execution data in the logs for this pipe. For more information, see
[Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data "eb-pipes-logs.md#eb-pipes-logs-execution-data")

###### Important

These fields may contain sensitive information. EventBridge makes no attempt to redact the contents
of these fields during logging.

For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data "eb-pipes-logs.md#eb-pipes-logs-execution-data").

**awsResponse**

The response returned by the enrichment or target, in JSON format. For requests sent to an API destination, this represents the HTTP response returned from that endpoint, and not the response returned by the API Destination service itself.

EventBridge includes this field only if you have specified to include execution data in the logs for this pipe. For more information, see
[Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data "eb-pipes-logs.md#eb-pipes-logs-execution-data")

###### Important

These fields may contain sensitive information. EventBridge makes no attempt to redact the contents
of these fields during logging.

For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data "eb-pipes-logs.md#eb-pipes-logs-execution-data").

**truncatedFields**

A list of any execution data fields EventBridge has truncated to keep the record below the 256 KB size limitation.

If EventBridge did not have to truncate any of the execution data fields, this field is present but `null`.

For more information, see [Truncating execution data in EventBridge
Pipes log records](eb-pipes-logs.md#eb-pipes-logs-execution-data-truncation "eb-pipes-logs.md#eb-pipes-logs-execution-data-truncation").

**error**

Contains information for any error generated during this pipe execution step.

If no error was generated during this pipe execution step, this field is present but `null`.

**httpStatusCode**

The HTTP status code returned by the called service.

**message**
The error message returned by the called service.

**details**
Any detailed error information returned by the called service.

**awsService**
The name of the service called.

**requestId**
The request ID for this request from the called service.
