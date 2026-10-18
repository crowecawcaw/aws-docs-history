

# System log event schema for Lambda Web Functions
<a name="web-functions-logging-system-log-schema"></a>

Lambda writes the following system events to your Web Function's log group. Each event is a JSON object with the envelope fields described in [Event envelope](#web-functions-logging-system-log-schema-envelope) and a `record` object whose fields depend on the event type. The level of each event determines whether Lambda delivers it. For more information, see [System logs](web-functions-logging.md#web-functions-logging-system-logs).


| Event type | Record object | Description | 
| --- | --- | --- | 
| platform.initStart | PlatformInitStart | Environment initialization started. | 
| platform.initReport | PlatformInitReport | Report of environment initialization, whether it succeeded or failed. | 
| platform.invokeStart | PlatformInvokeStart | The environment started serving requests. | 
| platform.requestComplete | PlatformRequestComplete | One HTTP request completed. Logged at DEBUG only. | 
| platform.invokeSummary | PlatformInvokeSummary | Summary of the environment's activity, emitted about every 60 seconds. | 
| platform.invokeReport | PlatformInvokeReport | Report of the environment's whole serving period, emitted when it stops serving. | 
| platform.spinDownStart | PlatformSpinDownStart | Environment shutdown started. | 
| platform.spinDownReport | PlatformSpinDownReport | Report of environment shutdown. | 
| platform.logsDropped | PlatformLogsDropped | Log records were dropped because logs were produced faster than they could be delivered. | 

In the field lists on this page, a question mark (`?`) after a field name means that the field might not be present. Types that are not JSON types, such as `InitType`, `Status`, or `InvokeSummaryMetrics`, are defined in [Shared object types](#web-functions-logging-system-log-schema-types), and each one links to its definition.

## `platform.initStart`
<a name="web-functions-logging-system-log-schema-initstart"></a>

The environment initialization phase started.

Level: `INFO`

The `record` object has the following fields:
+ `functionName` (`String`) – The name of the function.
+ `revisionId` (`String`) – The revision that the environment runs.
+ `instanceId` (`String`) – The identifier of the execution environment.
+ `initializationType` ([`InitType`](#web-functions-logging-system-log-schema-inittype)) – How Lambda initialized the environment.
+ `runtimeVersion` (`String`) – The runtime version that the environment runs.
+ `runtimeVersionArn` (`String`) – The Amazon Resource Name (ARN) of the runtime version.

```
{
  "timestamp": "2026-09-25T11:12:30.893Z",
  "level": "INFO",
  "type": "platform.initStart",
  "region": "us-east-1",
  "record": {
    "runtimeVersion": "nodejs24.x:nodejs.web24.v51",
    "runtimeVersionArn": "arn:aws:lambda:us-east-1::runtime/nodejs24.x/version/nodejs.web24.v51",
    "functionName": "my-web-app",
    "revisionId": "rev-fs0fq",
    "instanceId": "52754708-44f1-407a-a1fd-6d2a98175a45",
    "initializationType": "native-http"
  }
}
```

## `platform.initReport`
<a name="web-functions-logging-system-log-schema-initreport"></a>

Overall report of the initialization phase.

Level: `INFO` when status is success, `WARN` when failure.

The `record` object has the following fields:
+ `status` ([`Status`](#web-functions-logging-system-log-schema-status)) – The outcome of the initialization phase.
+ `errorType?` (`String`) – Present when status is failure. Values such as `Runtime.ImportCodeError`, `Application.InitCodeError`, and `Runtime.InitTimeout`.
+ `initializationType` ([`InitType`](#web-functions-logging-system-log-schema-inittype)) – How Lambda initialized the environment.
+ `metrics` ([`InitReportMetrics`](#web-functions-logging-system-log-schema-initreportmetrics)) – Metrics for the initialization phase.

Success example:

```
{
  "timestamp": "2026-09-25T11:12:31.143Z",
  "level": "INFO",
  "type": "platform.initReport",
  "region": "us-east-1",
  "record": {
    "status": "success",
    "initializationType": "native-http",
    "metrics": {
      "totalDurationMs": 304.000,
      "totalCpuTimeMs": 143.000,
      "maxMemoryUsageMb": 142
    }
  }
}
```

Failure example, where the handler module failed to load:

```
{
  "timestamp": "2026-09-25T11:16:04.164Z",
  "level": "WARN",
  "type": "platform.initReport",
  "region": "us-east-1",
  "record": {
    "status": "failure",
    "errorType": "Runtime.ImportCodeError",
    "initializationType": "native-http",
    "metrics": {
      "totalDurationMs": 320.000,
      "totalCpuTimeMs": 137.000,
      "maxMemoryUsageMb": 138
    }
  }
}
```

## `platform.invokeStart`
<a name="web-functions-logging-system-log-schema-invokestart"></a>

The environment finished initializing and started serving requests. Lambda emits this event once per environment, not once per request, and only when initialization succeeded.

Level: `INFO`

The `record` object has the following fields:
+ `functionName` (`String`) – The name of the function.
+ `revisionId` (`String`) – The revision that the environment runs.
+ `instanceId` (`String`) – The identifier of the execution environment.

```
{
  "timestamp": "2026-09-25T11:12:31.144Z",
  "level": "INFO",
  "type": "platform.invokeStart",
  "region": "us-east-1",
  "record": {
    "functionName": "my-web-app",
    "revisionId": "rev-fs0fq",
    "instanceId": "52754708-44f1-407a-a1fd-6d2a98175a45"
  }
}
```

## `platform.requestComplete`
<a name="web-functions-logging-system-log-schema-requestcomplete"></a>

One HTTP request finished, successfully or not.

Level: `DEBUG`, so Lambda delivers it only when `systemLogLevel` is `DEBUG`.

The `record` object has the following fields:
+ `requestId` (`String`) – The request ID.
+ `endpointName` (`String`) – The endpoint that served the request.
+ `result` (`Integer`) – The HTTP status code returned to the client.
+ `errorType?` (`String`) – Present when Lambda failed the request. Values such as `Runtime.RequestTimeout` and `Platform.InvalidRequest`.
+ `metrics` ([`RequestCompleteMetrics`](#web-functions-logging-system-log-schema-requestcompletemetrics)) – Metrics for the request.

Success example:

```
{
  "timestamp": "2026-09-25T11:12:31.154Z",
  "level": "DEBUG",
  "type": "platform.requestComplete",
  "region": "us-east-1",
  "record": {
    "requestId": "KXH25FBDZ33GP4TQ4ARAUYSTSA",
    "endpointName": "default",
    "result": 200,
    "metrics": {
      "durationMs": 4.484,
      "responseBytes": 40
    }
  }
}
```

Timeout example:

```
{
  "timestamp": "2026-09-25T11:12:34.926Z",
  "level": "DEBUG",
  "type": "platform.requestComplete",
  "region": "us-east-1",
  "record": {
    "requestId": "5SXHGVX2GD64ND6NQVEBAY235Q",
    "endpointName": "default",
    "result": 504,
    "errorType": "Runtime.RequestTimeout",
    "metrics": {
      "durationMs": 3001.229,
      "responseBytes": 0
    }
  }
}
```

## `platform.invokeSummary`
<a name="web-functions-logging-system-log-schema-invokesummary"></a>

Summarizes one window of about 60 seconds of an environment's activity. Lambda emits it for every live environment, including idle windows where `requests` is 0.

Level: `INFO`

The `record` object has the following fields:
+ `startTime` (`String`) – The start of the summary window (RFC 3339).
+ `instanceId` (`String`) – The identifier of the execution environment.
+ `metrics` ([`InvokeSummaryMetrics`](#web-functions-logging-system-log-schema-invokesummarymetrics)) – Metrics for the window.

```
{
  "timestamp": "2026-09-25T11:13:31.143Z",
  "level": "INFO",
  "type": "platform.invokeSummary",
  "region": "us-east-1",
  "record": {
    "startTime": "2026-09-25T11:12:31.144547426Z",
    "instanceId": "52754708-44f1-407a-a1fd-6d2a98175a45",
    "metrics": {
      "requests": 4,
      "concurrentRequests": 1,
      "cpuTimeMs": 420.000,
      "maxMemoryUsageMb": 154
    }
  }
}
```

## `platform.invokeReport`
<a name="web-functions-logging-system-log-schema-invokereport"></a>

Overall report of the environment's serving period, from invokeStart until it stops serving. Lambda emits it once per environment, at shutdown.

Level: `INFO` when status is success, `WARN` when failure.

The `record` object has the following fields:
+ `status` ([`Status`](#web-functions-logging-system-log-schema-status)) – The outcome of the serving period.
+ `errorType?` (`String`) – Present when status is failure. Values such as `Runtime.Exit`, `Runtime.ExitError`, and `Runtime.OutOfMemory`.
+ `instanceId` (`String`) – The identifier of the execution environment.
+ `metrics` ([`InvokeReportMetrics`](#web-functions-logging-system-log-schema-invokereportmetrics)) – Metrics for the serving period.

A request timeout does not fail the serving period. The `status` stays `success`.

Success example:

```
{
  "timestamp": "2026-09-25T11:19:11.858Z",
  "level": "INFO",
  "type": "platform.invokeReport",
  "region": "us-east-1",
  "record": {
    "status": "success",
    "instanceId": "52754708-44f1-407a-a1fd-6d2a98175a45",
    "metrics": {
      "totalCpuTimeMs": 973.000,
      "totalDurationMs": 400723.000,
      "totalRequests": 4,
      "concurrentRequests": 1,
      "maxMemoryUsageMb": 157
    }
  }
}
```

Failure example:

```
{
  "timestamp": "2026-09-25T11:19:11.858Z",
  "level": "WARN",
  "type": "platform.invokeReport",
  "region": "us-east-1",
  "record": {
    "status": "failure",
    "errorType": "Runtime.OutOfMemory",
    "instanceId": "52754708-44f1-407a-a1fd-6d2a98175a45",
    "metrics": {
      "totalCpuTimeMs": 973.000,
      "totalDurationMs": 400723.000,
      "totalRequests": 4,
      "concurrentRequests": 1,
      "maxMemoryUsageMb": 512
    }
  }
}
```

## `platform.spinDownStart`
<a name="web-functions-logging-system-log-schema-spindownstart"></a>

Environment shutdown started.

Level: `INFO`

The `record` object has the following fields:
+ `functionName` (`String`) – The name of the function.
+ `revisionId` (`String`) – The revision that the environment runs.
+ `instanceId` (`String`) – The identifier of the execution environment.

```
{
  "timestamp": "2026-09-25T11:19:11.858Z",
  "level": "INFO",
  "type": "platform.spinDownStart",
  "region": "us-east-1",
  "record": {
    "functionName": "my-web-app",
    "revisionId": "rev-fs0fq",
    "instanceId": "52754708-44f1-407a-a1fd-6d2a98175a45"
  }
}
```

## `platform.spinDownReport`
<a name="web-functions-logging-system-log-schema-spindownreport"></a>

Overall report of the shutdown.

Lambda sends `SIGTERM` to your application and waits up to 1 second for it to exit. If the application is still running, Lambda stops it with `SIGKILL` and reports a failure with the error type `Runtime.SpinDownTimeout`.

Level: `INFO` when status is success, `WARN` when failure.

The `record` object has the following fields:
+ `status` ([`Status`](#web-functions-logging-system-log-schema-status)) – The outcome of the shutdown phase.
+ `errorType?` (`String`) – Present when status is failure. Values such as `Runtime.SpinDownTimeout` and `Runtime.ExitError`.
+ `metrics` ([`SpinDownReportMetrics`](#web-functions-logging-system-log-schema-spindownreportmetrics)) – Metrics for the shutdown phase.

Success example:

```
{
  "timestamp": "2026-09-25T11:19:11.879Z",
  "level": "INFO",
  "type": "platform.spinDownReport",
  "region": "us-east-1",
  "record": {
    "status": "success",
    "metrics": {
      "totalDurationMs": 21.000,
      "totalCpuTimeMs": 8.000,
      "maxMemoryUsageMb": 157
    }
  }
}
```

Failure example:

```
{
  "timestamp": "2026-09-25T11:19:12.879Z",
  "level": "WARN",
  "type": "platform.spinDownReport",
  "region": "us-east-1",
  "record": {
    "status": "failure",
    "errorType": "Runtime.SpinDownTimeout",
    "metrics": {
      "totalDurationMs": 1021.000,
      "totalCpuTimeMs": 8.000,
      "maxMemoryUsageMb": 157
    }
  }
}
```

## `platform.logsDropped`
<a name="web-functions-logging-system-log-schema-logsdropped"></a>

Log records were dropped because logs were produced faster than they could be delivered.

Level: `WARN`

The `record` object has the following fields:
+ `reason` (`String`) – Why the records were dropped.
+ `droppedRecords` (`Integer`) – Records dropped since the last record that was delivered.
+ `droppedBytes` (`Integer`) – Bytes dropped since the last record that was delivered.

Both counts accumulate across consecutive drops and reset to 0 after a record is delivered.

```
{
  "timestamp": "2026-09-25T11:20:00.000Z",
  "level": "WARN",
  "type": "platform.logsDropped",
  "region": "us-east-1",
  "record": {
    "reason": "Some logs were dropped because the downstream consumer is slower than the logs production rate",
    "droppedRecords": 120,
    "droppedBytes": 48000
  }
}
```

## Shared object types
<a name="web-functions-logging-system-log-schema-types"></a>

The following types appear in the field lists of the events on this page.

### Event envelope
<a name="web-functions-logging-system-log-schema-envelope"></a>

Every system event has the following envelope fields:
+ `timestamp` (`String`) – RFC 3339 in UTC.
+ `level` (`Level`) – The level of the event.
+ `type` (`String`) – The event type (`platform.*`).
+ `region` (`String`) – The Region where the execution environment ran.
+ `record` (`Object`) – The event-specific fields.

### `InitType`
<a name="web-functions-logging-system-log-schema-inittype"></a>

String enum that describes how Lambda initialized the environment. Web Functions always use `native-http`.

### `Level`
<a name="web-functions-logging-system-log-schema-level"></a>

String enum for the level of a system event: `DEBUG`, `INFO`, or `WARN`. System events are never `ERROR` or `FATAL`. Report events are `INFO` when status is success and `WARN` when it is failure.

### `Status`
<a name="web-functions-logging-system-log-schema-status"></a>

String enum that describes the outcome of a phase: `success` or `failure`. When it is `failure`, the record also contains `errorType`.

### `InitReportMetrics`
<a name="web-functions-logging-system-log-schema-initreportmetrics"></a>
+ `totalDurationMs` (`Double`) – Wall-clock time of the initialization phase.
+ `totalCpuTimeMs` (`Double`) – CPU time consumed during initialization.
+ `maxMemoryUsageMb` (`Integer`) – Peak memory of the environment, in MiB.

### `RequestCompleteMetrics`
<a name="web-functions-logging-system-log-schema-requestcompletemetrics"></a>
+ `durationMs` (`Double`) – Wall-clock time of the request.
+ `responseBytes` (`Integer`) – Response body bytes sent.

### `InvokeSummaryMetrics`
<a name="web-functions-logging-system-log-schema-invokesummarymetrics"></a>
+ `requests` (`Integer`) – Requests completed in the window.
+ `concurrentRequests` (`Integer`) – Maximum concurrent requests in the window.
+ `cpuTimeMs` (`Double`) – CPU time consumed in the window.
+ `maxMemoryUsageMb` (`Integer`) – Peak memory of the environment, in MiB.

### `InvokeReportMetrics`
<a name="web-functions-logging-system-log-schema-invokereportmetrics"></a>
+ `totalCpuTimeMs` (`Double`) – CPU time over the serving period.
+ `totalDurationMs` (`Double`) – Wall-clock time from invokeStart until the environment stopped serving.
+ `totalRequests` (`Integer`) – Total requests served.
+ `concurrentRequests` (`Integer`) – Maximum concurrent requests over the period.
+ `maxMemoryUsageMb` (`Integer`) – Peak memory of the environment, in MiB.

### `SpinDownReportMetrics`
<a name="web-functions-logging-system-log-schema-spindownreportmetrics"></a>
+ `totalDurationMs` (`Double`) – Wall-clock time of the shutdown phase.
+ `totalCpuTimeMs` (`Double`) – CPU time consumed during shutdown.
+ `maxMemoryUsageMb` (`Integer`) – Peak memory of the environment, in MiB.