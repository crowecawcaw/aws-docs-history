

# Log ingestion through HTTP endpoints
<a name="CWL_HTTP_Endpoints"></a>

Amazon CloudWatch Logs provides HTTP endpoints that allow you to send logs directly to CloudWatch Logs using simple HTTP POST requests. These endpoints support both SigV4 and bearer token authentication.

**Important**  
We recommend using SigV4 authentication for all production workloads where AWS SDK integration is possible. SigV4 uses short-term credentials and provides the strongest security posture. Bearer token (API key) authentication is intended for scenarios where SigV4 is not feasible, such as third-party log forwarders that do not support AWS SDK integration. For more information, see [Alternatives to long-term access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles) in the *IAM User Guide*.

CloudWatch Logs supports the following HTTP ingestion endpoints:


| Endpoint | Path | Content-Type | Format | 
| --- | --- | --- | --- | 
| [OpenTelemetry Logs](CWL_HTTP_Endpoints_OTLP.md) | /v1/logs | application/json or application/x-protobuf | OTLP JSON or Protobuf | 
| [HLC Logs](CWL_HLC_Endpoint.md) | /services/collector/event | application/json | HLC format | 
| [ND-JSON Logs](CWL_HTTP_Endpoints_NDJSON.md) | /ingest/bulk | application/json or application/x-ndjson | Newline-delimited JSON | 
| [Structured JSON Logs](CWL_HTTP_Endpoints_StructuredJSON.md) | /ingest/json | application/json | JSON object or array | 

## Common behavior
<a name="CWL_HTTP_Endpoints_Common"></a>

All HTTP ingestion endpoints share the following behavior:

**Authentication**

All endpoints support both SigV4 and bearer token authentication:
+ **SigV4 (recommended)** – Standard AWS Signature Version 4 signing. Use SigV4 whenever your application or infrastructure supports the AWS SDK or can sign requests. SigV4 uses short-term credentials and is the most secure authentication method.
+ **Bearer token** – Use the `Authorization: Bearer <ACWL token>` header.
  + Token must be a valid ACWL bearer token. For setup instructions, see [Setting up bearer token authentication](CWL_HTTP_Endpoints_BearerTokenAuth.md).
  + Requires the `logs:PutLogEvents` and `logs:CallWithBearerToken` IAM permissions.

**Log group and log stream**
+ Provided via headers: `x-aws-log-group` and `x-aws-log-stream`
+ Query parameters `?logGroup=<name>&logStream=<name>` are also supported on all endpoints except OTLP.
+ You cannot use both query parameters and headers for the same parameter.
+ Both log group and log stream are required.

**Response**
+ Success: `HTTP 200` with body `{}`
+ Validation errors: `HTTP 400`
+ Auth failures: `HTTP 401`

## Comparison of HTTP ingestion endpoints
<a name="CWL_HTTP_Endpoints_Comparison"></a>


| Feature | HLC Logs | ND-JSON Logs | Structured JSON Logs | OpenTelemetry Logs | 
| --- | --- | --- | --- | --- | 
| Path | /services/collector/event | /ingest/bulk | /ingest/json | /v1/logs | 
| Content-Type | application/json | application/json or application/x-ndjson | application/json | application/json or application/x-protobuf | 
| Timestamp field | "time" (seconds) | "timestamp" (milliseconds) | "timestamp" (milliseconds) | "timeUnixNano" (nanoseconds) | 
| Required fields | "event" | None | None | OTLP structure ("resourceLogs") | 
| Partial success response | No | Yes | Yes | Yes | 
| Query parameter support | Yes | Yes | Yes | No (headers only) | 
| Entity metadata | Yes | Yes | Yes | No | 
| Accepts primitives | No | Yes | No | No | 
| Line-based parsing | No | Yes | No | No | 
| Protobuf support | No | No | No | Yes | 
| Retry-After header | No | No | No | Yes | 

## Choosing an endpoint
<a name="CWL_HTTP_Endpoints_Choosing"></a>
+ **Using HLC format?** Use HLC Logs. Your existing HLC payloads work with minimal changes.
+ **Streaming line-by-line logs?** Use ND-JSON Logs. Best for log pipelines that emit one event per line. Most flexible – accepts any JSON value type.
+ **Sending structured JSON payloads?** Use Structured JSON Logs. Best for applications that produce well-formed JSON objects or arrays.
+ **Already using OpenTelemetry?** Use OpenTelemetry Logs. Accepts OTLP JSON or Protobuf format and supports partial success responses with retry semantics.