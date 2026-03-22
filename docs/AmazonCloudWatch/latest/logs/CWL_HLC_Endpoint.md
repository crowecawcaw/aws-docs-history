# Sending logs using the HLC endpoint (HLC Logs)

The HLC Logs endpoint (`/services/collector/event`) is based on the
HTTP Log Collector (HLC) format.

If you are using bearer token authentication, complete the setup steps in
[Setting up bearer token authentication](CWL_HTTP_Endpoints_BearerTokenAuth.md "CWL_HTTP_Endpoints_BearerTokenAuth.md") before proceeding.

## Input modes

Each event is a JSON object with a required `"event"` field. Optional
metadata fields: `"time"`, `"host"`, `"source"`,
`"sourcetype"`, `"index"`.

**Single event:**

```
{"event":"Hello world!","time":1486683865.0}
```

**JSON array of events:**

```
[
  {"event":"msg1","time":1486683865.0},
  {"event":"msg2","time":1486683866.0}
]
```

**Concatenated/batched events (no array wrapper):**

```
{"event":"msg1","time":1486683865.0}{"event":"msg2","time":1486683866.0}
```

## Event field (required)

The `"event"` field is mandatory. Its value can be any JSON type:

```
{"event":"a string message"}
{"event":{"message":"structured data","severity":"INFO"}}
{"event":42}
{"event":true}
```

Objects without an `"event"` field are silently skipped:

```
{"message":"this is skipped — no event field"}
```

## Time field (optional)

The `"time"` field is in epoch seconds (not milliseconds), with optional
decimal for sub-second precision.

| Format           | Example                   | Interpreted as      |
| ---------------- | ------------------------- | ------------------- |
| Float            | `"time":1486683865.500`   | 1486683865500 ms    |
| Integer          | `"time":1486683865`       | 1486683865000 ms    |
| String (float)   | `"time":"1486683865.500"` | 1486683865500 ms    |
| String (integer) | `"time":"1486683865"`     | 1486683865000 ms    |
| Missing          | (no time field)           | Server current time |
| Invalid          | `"time":"invalid"`        | Server current time |

## Content-Type

Only `application/json` is accepted.

## Accepted JSON value types

| Top-level type                            | Behavior                            |
| ----------------------------------------- | ----------------------------------- |
| Object with `"event"`                     | Accepted                            |
| Object without `"event"`                  | Skipped                             |
| Array of objects                          | Each element processed individually |
| Concatenated objects                      | Each object processed individually  |
| Primitive (string, number, boolean, null) | Skipped                             |

## Endpoint format

The HLC endpoint URL follows this format:

```
https://logs.<region>.amazonaws.com/services/collector/event?logGroup=<name>&logStream=<name>[&entityName=<name>&entityEnvironment=<environment>]
```

**Required parameters:**

- `<region>` – AWS Region (for example, `us-east-1`, `eu-west-1`)
- `logGroup` – URL-encoded log group name
- `logStream` – URL-encoded log stream name

**Optional parameters:**

You can optionally associate your log events with a `Service` entity by
including the following query parameters. Because logs sent through the HLC endpoint
are custom telemetry, they are not automatically associated with an entity. By
providing these parameters, CloudWatch Logs creates an entity with
`KeyAttributes.Type` set to `Service` and associates it with
your log events. This enables the **Explore related**
feature in CloudWatch to correlate these logs with other telemetry (metrics, traces,
and logs) from the same service, making it easier to troubleshoot and monitor your
applications across different signal types. For more information about entities and
related telemetry, see [Adding related information to custom telemetry](../monitoring/adding-your-own-related-telemetry.md "../monitoring/adding-your-own-related-telemetry.md").

- `entityName` – The name of the service entity to associate with the log events. This value is stored as the entity `KeyAttributes.Name` (for example, `my-application` or `api.myservice.com`).
- `entityEnvironment` – The environment where the service is hosted or what it belongs to. This value is stored as the entity `KeyAttributes.Environment` (for example, `production`, `ec2:default`, or `eks:my-cluster/default`).

## Request format

Send logs using HTTP POST with the following headers and body:

**Headers:**

- `Authorization: Bearer <your-bearer-token>`
- `Content-Type: application/json`

**Body format:**

The request body should be in JSON format with an array of events:

```
{
    "event": [
        {
            "time": 1730141374.001,
            "event": "Application started successfully",
            "host": "web-server-1",
            "source": "application.log",
            "severity": "info"
        },
        {
            "time": 1730141374.457,
            "event": "User login successful",
            "host": "web-server-1",
            "source": "auth.log",
            "user": "john.doe"
        }
    ]
}
```

**Field descriptions:**

- `time` – Unix epoch timestamp in seconds, with optional decimal for sub-second precision (optional)
- `event` – The log message or event data (required)
- `host` – Source hostname or identifier (optional)
- `source` – Log source identifier (optional)

Additional custom fields can be included as needed.

## Example request

```
curl -X POST "https://logs.<region>.amazonaws.com/services/collector/event?logGroup=MyLogGroup&logStream=MyStream" \
  -H "Authorization: Bearer ACWL<token>" \
  -H "Content-Type: application/json" \
  -d '{"event":{"message":"User logged in","user_id":"u-123"},"time":1486683865.0,"host":"web-01","source":"auth-service"}'
```

## Best practices

### Batching events

For better performance and efficiency:

- Batch multiple events in a single request when possible
- Recommended batch size: 10–100 events per request
- Maximum request size: 1 MB

### Error handling

Implement proper error handling in your application. Common HTTP status codes:

- `200 OK` – Logs successfully ingested
- `400 Bad Request` – Invalid request format or parameters
- `401 Unauthorized` – Invalid or expired bearer token
- `403 Forbidden` – Insufficient permissions
- `404 Not Found` – Log group or stream doesn't exist
- `429 Too Many Requests` – Rate limit exceeded
- `500 Internal Server Error` – Service error (retry with exponential backoff)

## Limitations

- Maximum event size: 256 KB per event
- Maximum request size: 1 MB
- Maximum events per request: 10,000
- Log group names must follow CloudWatch Logs naming conventions
- Bearer token authentication must be enabled on the log group if bearer token authentication is used.
