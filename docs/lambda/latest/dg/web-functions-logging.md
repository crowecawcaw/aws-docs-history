

# Web Function logs in Amazon CloudWatch Logs
<a name="web-functions-logging"></a>

AWS Lambda captures everything your application writes to standard output and standard error and sends it to Amazon CloudWatch Logs, along with system logs that Lambda itself generates. In Node.js, output from every `console` method, such as `console.log`, `console.info`, and `console.error`, is captured automatically and filtered by the `applicationLogLevel` setting. Logging libraries that write to standard output or standard error are also captured. You do not need a logging agent or the Amazon CloudWatch Logs SDK.

Lambda writes `console` output as JSON log events and adds the `requestId`, `endpointName`, and `region` fields to each event. For an example, see [Writing structured logs](#web-functions-logging-structured).

Lambda collects logs in each AWS Region where your Web Function runs and then centralizes them into the function's home Region. A `HomeRegion` endpoint runs only in the home Region. A `MultiRegion` or `PerRegion` endpoint also runs in the other Regions that you specify, so Lambda centralizes logs from each of those Regions. For more information, see [Endpoint types](web-functions-endpoints.md#web-functions-endpoint-types).

## Log groups
<a name="web-functions-logging-log-groups"></a>

By default, Lambda sends your Web Function's logs to a log group named after the function:

```
/aws/lambda/web/{{function-name}}
```

Alongside the centralized log group, Lambda uses a companion log group to hold in-Region logs before they are centralized. The companion's name is the centralized log group's name followed by `.local`, for both the default log group and a custom log group. For the default log group, the companion is:

```
/aws/lambda/web/{{function-name}}.local
```

Lambda writes logs to the `.local` log group in every Region where requests run, including the home Region, and then centralizes them into the log group without the suffix in the home Region. Each `.local` log group holds only the logs from its own Region. Lambda does not remove events from the `.local` log group after centralization. The log group's retention setting determines how long they remain.

The log groups do not exist until your Web Function serves its first request. The centralized log group in the home Region might appear after the `.local` log group. For centralization timing, see [Centralization latency](web-functions-monitoring.md#web-functions-monitoring-delays).

Lambda creates the default log group and each `.local` log group with default Amazon CloudWatch Logs settings, so their events never expire unless you set a retention policy. You can change their retention, encryption, and resource policy after Lambda creates them. Set these on the `.local` log group in every Region where the endpoint runs and on the centralized log group in the home Region.

Because the `.local` log group does not wait for centralization, it is useful for debugging an issue in a specific Region. The centralized log group holds logs from every Region, so build shared queries, subscription filters, metric filters, and automation that must cover the whole application on the centralized log group. For how telemetry behaves in each Region, see [Telemetry in each Region](web-functions-monitoring.md#web-functions-monitoring-replica-telemetry).

## Using a custom log group
<a name="web-functions-logging-custom-group"></a>

You can send your Web Function's logs to a log group that you choose instead of the default. Use a custom log group when you want retention, encryption, or resource policies in place before the first log event arrives. A custom log group also lets you group logs from several functions together. To apply those settings from the start, create the log group and its `.local` companion yourself before you route traffic to the revision. If either log group does not exist, Lambda creates it on first use with default settings, and you can update its settings afterward. Lambda can create a log group only if the execution role has permission to create log groups. For the required permissions, see [Execution role](web-functions-permissions.md#web-functions-permissions-execution-role).

**To send logs to a custom log group (AWS CLI)**

1. In the home Region, create the log group and its `.local` companion, and set the retention you want on each. For a `MultiRegion` or `PerRegion` endpoint, also create the `.local` log group in each other Region that the endpoint serves, by running the `.local` commands with `--region` set to that Region.

   ```
   aws logs create-log-group --log-group-name {{/my-app/web-logs}}
   aws logs create-log-group --log-group-name {{/my-app/web-logs}}.local
   
   aws logs put-retention-policy \
       --log-group-name {{/my-app/web-logs}} \
       --retention-in-days 30
   
   aws logs put-retention-policy \
       --log-group-name {{/my-app/web-logs}}.local \
       --retention-in-days 30
   ```

1. Create a revision that specifies the log group in the `telemetryConfig` section of `serviceConfig`.

   ```
   aws lambda-web create-web-function-revision \
       --function-name {{my-web-app}} \
       --build-config '{
         "codeConfig": {
           "s3Object": { "bucket": "{{my-bucket}}", "key": "{{my-app.zip}}" }
         },
         "runtimeConfig": { "runtime": "nodejs24.x" }
       }' \
       --service-config '{
         "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}",
         "telemetryConfig": {
           "loggingConfig": {
             "logGroup": "{{/my-app/web-logs}}"
           }
         }
       }'
   ```

1. Route traffic to the new revision. For more information, see [Deployment patterns](web-functions-deployment.md).

Because logging configuration is part of the revision, it is immutable for that revision. To change the log group later, create another revision. For more information, see [Managing Web Function revisions](web-functions-revisions.md).

## Logging controls
<a name="web-functions-logging-format-levels"></a>

The `loggingConfig` section controls the destination and minimum severity of logs. These settings are part of the revision.


| Setting | Values | Default | Description | 
| --- | --- | --- | --- | 
| logGroup | Log group name | /aws/lambda/web/{{function-name}} | The Amazon CloudWatch Logs log group that receives your logs. | 
| applicationLogLevel | TRACE \| DEBUG \| INFO \| WARN \| ERROR \| FATAL | INFO | The minimum severity of your application's logs that Lambda sends to Amazon CloudWatch Logs. Logs below this level are dropped. Node.js has no FATAL console method, so a level of FATAL behaves as ERROR. | 
| systemLogLevel | DEBUG \| INFO \| WARN | INFO | The minimum severity of Lambda-generated system logs that Lambda sends to Amazon CloudWatch Logs. For the level of each system event, see [System logs](#web-functions-logging-system-logs). | 

The following example creates a revision that drops application logs below `WARN`:

```
aws lambda-web create-web-function-revision \
    --function-name {{my-web-app}} \
    --build-config '{
      "codeConfig": {
        "s3Object": { "bucket": "{{my-bucket}}", "key": "{{my-app.zip}}" }
      },
      "runtimeConfig": { "runtime": "nodejs24.x" }
    }' \
    --service-config '{
      "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}",
      "telemetryConfig": {
        "loggingConfig": {
          "applicationLogLevel": "WARN",
          "systemLogLevel": "INFO"
        }
      }
    }'
```

Raising `applicationLogLevel` in production reduces both log volume and cost. Lower it temporarily to `DEBUG` or `TRACE` when you are investigating an issue.

## System logs
<a name="web-functions-logging-system-logs"></a>

In addition to your application's output, your log group receives system logs that Lambda generates about the execution environment lifecycle, such as environment initialization and shutdown. Use `systemLogLevel` to control how much of this Lambda emits.

System logs are useful for correlating application behavior with platform events. For example, a latency spike that lines up with an environment initialization entry points to a cold start rather than to your application code. For the lifecycle these logs describe, see [Execution environment lifecycle](web-functions-env-lifecycle.md).

Web Functions emit the following system events. Set `systemLogLevel` to the lowest level that you need. For example, set it to `DEBUG` to receive `platform.requestComplete`, or to `WARN` to receive only failures and dropped-log warnings.


| Event type | Level | Notes | 
| --- | --- | --- | 
| platform.initStart | INFO | None | 
| platform.initReport | INFO on success, WARN on failure | A failure indicates an initialization error, such as an error importing your code. | 
| platform.invokeStart | INFO | None | 
| platform.requestComplete | DEBUG | Emitted once for every HTTP request, including failed requests. Because it is high volume, it is not emitted at the default system log level. | 
| platform.invokeSummary | INFO | Periodic. Emitted about every 60 seconds for each active execution environment. | 
| platform.invokeReport | INFO on success, WARN on failure |  | 
| platform.spinDownStart | INFO |  | 
| platform.spinDownReport | INFO on success, WARN on failure | A failure indicates that your application didn't exit within 1 second of receiving SIGTERM (Runtime.SpinDownTimeout) or exited with an error (Runtime.ExitError). | 
| platform.logsDropped | WARN | Indicates that Lambda dropped log events. | 

For the fields in each system event, see [System log event schema for Lambda Web Functions](web-functions-logging-system-log-schema.md).

The `lambda-web-request-id` response header identifies the request, and the `lambda-web-logstream` response header identifies the log stream for the environment that handled it. Use these values to correlate a client response with application and system logs. For more information, see [Response headers](web-functions-http.md#web-functions-http-response-headers).

To find the events from the identified log stream in the centralized log group in the home Region, filter by the stream name as a prefix. You can also read the stream by its exact name from the `.local` log group in the Region that served the request.

```
aws logs filter-log-events \
    --log-group-name /aws/lambda/web/{{my-web-app}} \
    --log-stream-name-prefix "{{LAMBDA_WEB_LOGSTREAM}}" \
    --region {{us-east-1}}
```

To follow recent logs while reproducing an issue, use:

```
aws logs tail /aws/lambda/web/{{my-web-app}} \
    --follow \
    --region {{us-east-1}}
```

## Writing structured logs
<a name="web-functions-logging-structured"></a>

Pass an object to a `console` method so that Lambda writes it as a JSON object in the `message` field. You can then query individual fields in Amazon CloudWatch Logs Insights rather than matching on substrings. Do not pass a string that you built with `JSON.stringify`. Lambda writes a string as an escaped string value, so its fields cannot be queried.

```
function logRequest(req, statusCode, durationMs) {
  console.info({
    method: req.method,
    path: req.url,
    statusCode: statusCode,
    durationMs: durationMs
  });
}
```

Lambda writes a log event similar to the following:

```
{
  "timestamp": "2026-09-25T11:29:02.711Z",
  "level": "INFO",
  "message": {
    "method": "GET",
    "path": "/hello-world",
    "statusCode": 200,
    "durationMs": 100
  },
  "requestId": "US3NHLM77IRXDFLBADYHGIZZNM",
  "endpointName": "prod",
  "region": "us-east-1"
}
```

You can then query the fields directly. For example, the following Amazon CloudWatch Logs Insights query returns the 20 most recent requests that returned a 5xx status:

```
fields @timestamp, message.method, message.path, message.statusCode, message.durationMs
| filter message.statusCode >= 500
| sort @timestamp desc
| limit 20
```

To publish custom metrics from your logs rather than only querying them, use the embedded metric format. For more information, see [Publishing custom metrics with the embedded metric format](web-functions-emf.md).

## Using Amazon CloudWatch Logs features with your logs
<a name="web-functions-logging-cwl-features"></a>

Because logs are centralized into the home Region, you can use the standard Amazon CloudWatch Logs features in that Region, including:
+ **Live Tail** – Stream log events as they arrive while you reproduce an issue. Events reach the centralized log group after centralization, so for the shortest delay, run Live Tail on the `.local` log group in the Region that serves your requests.
+ **Logs Insights** – Query fields in your JSON log events.
+ **Log centralization** – Forward your logs onward to another account or destination using the Amazon CloudWatch Logs centralization features, if you aggregate logs outside the function's account.
+ **Subscription filters and metric filters** – Trigger downstream processing or derive metrics from log patterns.

Apply features that must cover the whole application to the centralized log group in the home Region. A `.local` log group holds only the logs from its own Region. For more information, see [Telemetry in each Region](web-functions-monitoring.md#web-functions-monitoring-replica-telemetry).