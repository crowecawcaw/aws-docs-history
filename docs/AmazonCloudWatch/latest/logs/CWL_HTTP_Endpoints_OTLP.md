

# Sending logs using the OTLP endpoint (OpenTelemetry Logs)
<a name="CWL_HTTP_Endpoints_OTLP"></a>

The OpenTelemetry Logs endpoint (`/v1/logs`) accepts OpenTelemetry Protocol (OTLP) log data in either JSON or Protobuf encoding. For detailed information about the OTLP endpoint, including configuration and usage, see [Send metrics and traces to CloudWatch with OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html).

If you are using bearer token authentication, complete the setup steps in [Setting up bearer token authentication](CWL_HTTP_Endpoints_BearerTokenAuth.md) before proceeding.

## Request format
<a name="CWL_OTLP_Format"></a>
+ Method: `POST`
+ Content-Type: `application/json` or `application/x-protobuf`
+ Log group: `x-aws-log-group` header only (query parameter not supported)
+ Log stream: `x-aws-log-stream` header

## Example request
<a name="CWL_OTLP_Example"></a>

```
curl -X POST "https://logs.<region>.amazonaws.com/v1/logs" \
  -H "Authorization: Bearer ACWL<token>" \
  -H "Content-Type: application/json" \
  -H "x-aws-log-group: MyLogGroup" \
  -H "x-aws-log-stream: MyLogStream" \
  -d '{
  "resourceLogs": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": { "stringValue": "my-service" }
          }
        ]
      },
      "scopeLogs": [
        {
          "scope": {
            "name": "my-library",
            "version": "1.0.0"
          },
          "logRecords": [
            {
              "timeUnixNano": "1741900000000000000",
              "severityNumber": 9,
              "severityText": "INFO",
              "body": {
                "stringValue": "User logged in successfully"
              },
              "attributes": [
                {
                  "key": "user.id",
                  "value": { "stringValue": "12345" }
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}'
```

## Responses
<a name="CWL_OTLP_Responses"></a>

**Success (all events accepted):**

```
HTTP 200 OK
{}
```

**Partial success (some events rejected):**

```
{
  "partialSuccess": {
    "rejectedLogRecords": 5,
    "errorMessage": "{\"tooOldLogEventCount\": 3, \"tooNewLogEventCount\": 1, \"expiredLogEventCount\": 1}"
  }
}
```

When the request Content-Type is `application/x-protobuf`, the response is returned as a serialized `ExportLogsServiceResponse` protobuf message with the same fields.

## OTLP-specific behaviors
<a name="CWL_OTLP_Specific_Behaviors"></a>

The following behaviors are specific to the OTLP endpoint and are not present on the other HTTP ingestion endpoints:
+ **Retry-After header** – Included on 503 and 429 responses to indicate when the client should retry.