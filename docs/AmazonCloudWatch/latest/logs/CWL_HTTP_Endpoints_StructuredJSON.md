

# Sending logs using the Structured JSON endpoint (Structured JSON Logs)
<a name="CWL_HTTP_Endpoints_StructuredJSON"></a>

The Structured JSON Logs endpoint (`/ingest/json`) accepts standard JSON – either a single JSON object or a JSON array of objects. This endpoint is designed for structured log data where each event is a JSON object.

If you are using bearer token authentication, complete the setup steps in [Setting up bearer token authentication](CWL_HTTP_Endpoints_BearerTokenAuth.md) before proceeding.

## Request format
<a name="CWL_StructuredJSON_Format"></a>

Only `application/json` is accepted as the Content-Type.

**Single JSON object:**

```
{"timestamp":1771007942000,"message":"single event","level":"INFO"}
```

**JSON array of objects:**

```
[
  {"timestamp":1771007942000,"message":"event one","level":"INFO"},
  {"timestamp":1771007943000,"message":"event two","level":"ERROR"}
]
```

## Accepted JSON value types
<a name="CWL_StructuredJSON_Accepted_Types"></a>

This endpoint is strict – only JSON objects are accepted as events.


| Input | Behavior | 
| --- | --- | 
| Single JSON object | Accepted as one event | 
| JSON array of objects | Each object becomes a separate event | 
| Empty array [] | Accepted, produces 0 events | 
| Non-object in array (string, number, etc.) | Skipped | 
| Top-level primitive ("hello", 42) | Skipped | 
| Concatenated objects {...}{...} | Only first object parsed | 

**Example – array with mixed types:**

```
[
  {"timestamp":1771007942000,"message":"valid object"},
  "just a string",
  42,
  {"timestamp":1771007943000,"message":"another valid object"}
]
```

Result: 2 events ingested (the objects), 2 skipped (the string and number).

## Timestamp field
<a name="CWL_StructuredJSON_Timestamp"></a>

The `"timestamp"` field is in epoch milliseconds, same as the NDJSON endpoint.


| Format | Example | Interpreted as | 
| --- | --- | --- | 
| Numeric (millis) | "timestamp":1771007942000 | 1771007942000 ms | 
| Missing | (no timestamp field) | Server current time | 
| Non-numeric | "timestamp":"invalid" | Server current time | 

## Example request
<a name="CWL_StructuredJSON_Example"></a>

```
curl -X POST "https://logs.<region>.amazonaws.com/ingest/json?logGroup=MyLogGroup&logStream=MyStream" \
  -H "Authorization: Bearer ACWL<token>" \
  -H "Content-Type: application/json" \
  -d '[{"timestamp":1771007942000,"message":"User logged in","user_id":"u-123"},{"timestamp":1771007943000,"message":"Order placed","order_id":"o-456"}]'
```

## Responses
<a name="CWL_StructuredJSON_Responses"></a>

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

The `rejectedLogRecords` field is the total number of rejected events. The `errorMessage` field contains a JSON-encoded breakdown by rejection reason:
+ `tooOldLogEventCount` – Events with timestamps older than the retention period
+ `tooNewLogEventCount` – Events with timestamps too far in the future
+ `expiredLogEventCount` – Events that expired during processing

## Best practices
<a name="CWL_StructuredJSON_Best_Practices"></a>

### Batching events
<a name="CWL_StructuredJSON_Batching"></a>

For better performance and efficiency:
+ Batch multiple events in a single request when possible
+ Recommended batch size: 10–100 events per request
+ Maximum request size: 1 MB

### Error handling
<a name="CWL_StructuredJSON_Error_Handling"></a>

Implement proper error handling in your application. Common HTTP status codes:
+ `200 OK` – Logs successfully ingested
+ `400 Bad Request` – Invalid request format or parameters
+ `401 Unauthorized` – Invalid or expired bearer token
+ `403 Forbidden` – Insufficient permissions
+ `404 Not Found` – Log group or stream doesn't exist
+ `429 Too Many Requests` – Rate limit exceeded
+ `500 Internal Server Error` – Service error (retry with exponential backoff)

## Limitations
<a name="CWL_StructuredJSON_Limitations"></a>
+ Maximum event size: 256 KB per event
+ Maximum request size: 1 MB
+ Maximum events per request: 10,000
+ Log group names must follow CloudWatch Logs naming conventions
+ Bearer token authentication must be enabled on the log group if bearer token authentication is used.