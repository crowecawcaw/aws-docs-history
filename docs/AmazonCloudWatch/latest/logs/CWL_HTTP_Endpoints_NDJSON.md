

# Sending logs using the NDJSON endpoint (ND-JSON Logs)
<a name="CWL_HTTP_Endpoints_NDJSON"></a>

The ND-JSON Logs endpoint (`/ingest/bulk`) accepts logs in [NDJSON (Newline Delimited JSON)](https://github.com/ndjson/ndjson-spec) format. Each line contains exactly one JSON value, separated by newline characters.

If you are using bearer token authentication, complete the setup steps in [Setting up bearer token authentication](CWL_HTTP_Endpoints_BearerTokenAuth.md) before proceeding.

## Request format
<a name="CWL_NDJSON_Format"></a>

Send one JSON value per line, separated by `\n` (LF) or `\r\n` (CRLF). Empty lines are silently ignored.

```
{"timestamp":1771007942000,"message":"event one","level":"INFO"}
{"timestamp":1771007943000,"message":"event two","level":"ERROR"}
{"timestamp":1771007944000,"message":"event three","level":"DEBUG"}
```

Both `application/json` and `application/x-ndjson` are accepted as the Content-Type.

## Accepted JSON value types
<a name="CWL_NDJSON_Accepted_Types"></a>

Per the NDJSON spec (RFC 8259), any valid JSON value is accepted on each line.

**JSON objects (most common):**

```
{"timestamp":1771007942000,"message":"User logged in","service":"auth"}
{"timestamp":1771007943000,"error":"Connection timeout","service":"api"}
```

**JSON arrays (flattened into individual events):**

```
[{"timestamp":1000,"message":"a"},{"timestamp":2000,"message":"b"}]
```

This single line produces 2 events. Each array element becomes a separate log event.

**Primitive values:**

```
"a plain string log message"
42
true
null
```

Each primitive becomes its own event with the server's current timestamp.

**Mixed types:**

```
{"timestamp":1771007942000,"message":"structured event"}
"unstructured string message"
42
{"timestamp":1771007943000,"error":"something failed"}
```

All 4 lines are accepted as valid events.


| Line content | Behavior | 
| --- | --- | 
| JSON object | Accepted, timestamp extracted if present | 
| JSON array | Flattened – each element becomes a separate event | 
| Empty array [] | Accepted, produces 0 events | 
| JSON string | Accepted as event message | 
| JSON number | Accepted as event message | 
| JSON boolean | Accepted as event message | 
| JSON null | Accepted as event message | 
| Invalid JSON | Skipped (counted, processing continues) | 
| Empty line | Ignored (not counted as skipped) | 

## Timestamp field
<a name="CWL_NDJSON_Timestamp"></a>

The `"timestamp"` field is in epoch milliseconds (not seconds).


| Format | Example | Interpreted as | 
| --- | --- | --- | 
| Numeric (millis) | "timestamp":1771007942000 | 1771007942000 ms | 
| Missing | (no timestamp field) | Server current time | 
| Non-numeric | "timestamp":"invalid" | Server current time | 
| Non-object line | "hello", 42, true | Server current time | 

## Invalid lines
<a name="CWL_NDJSON_Invalid_Lines"></a>

Lines that are not valid JSON are silently skipped and counted. Processing continues with the next line.

```
{"message":"valid event"}
this is not valid json
{"message":"another valid event"}
```

Result: 2 events ingested, 1 skipped. Returns `HTTP 200`.

If all lines are invalid, returns `HTTP 400` with `"All events were invalid"`.

## Example request
<a name="CWL_NDJSON_Example"></a>

```
curl -X POST "https://logs.<region>.amazonaws.com/ingest/bulk?logGroup=MyLogGroup&logStream=MyStream" \
  -H "Authorization: Bearer ACWL<token>" \
  -H "Content-Type: application/x-ndjson" \
  -d '{"timestamp":1771007942000,"message":"User logged in","level":"INFO"}
{"timestamp":1771007943000,"message":"Query took 42ms","level":"DEBUG"}
{"timestamp":1771007944000,"error":"Connection refused","level":"ERROR"}'
```

## Responses
<a name="CWL_NDJSON_Responses"></a>

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
<a name="CWL_NDJSON_Best_Practices"></a>

### Batching events
<a name="CWL_NDJSON_Batching"></a>

For better performance and efficiency:
+ Batch multiple events in a single request when possible
+ Recommended batch size: 10–100 events per request
+ Maximum request size: 1 MB

### Error handling
<a name="CWL_NDJSON_Error_Handling"></a>

Implement proper error handling in your application. Common HTTP status codes:
+ `200 OK` – Logs successfully ingested
+ `400 Bad Request` – Invalid request format or parameters
+ `401 Unauthorized` – Invalid or expired bearer token
+ `403 Forbidden` – Insufficient permissions
+ `404 Not Found` – Log group or stream doesn't exist
+ `429 Too Many Requests` – Rate limit exceeded
+ `500 Internal Server Error` – Service error (retry with exponential backoff)

## Limitations
<a name="CWL_NDJSON_Limitations"></a>
+ Maximum event size: 256 KB per event
+ Maximum request size: 1 MB
+ Maximum events per request: 10,000
+ Log group names must follow CloudWatch Logs naming conventions
+ Bearer token authentication must be enabled on the log group if bearer token authentication is used.