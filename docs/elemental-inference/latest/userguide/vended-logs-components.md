

# Components of a log
<a name="vended-logs-components"></a>

Each Elemental Inference application log record is a JSON object with the following fields:

`resource_arn`  
The ARN of the feed that generated the record.

`event_timestamp`  
The time the event occurred, in Unix epoch time (milliseconds).

`log_level`  
The severity of the record. Values are `INFO`, `WARN`, and `ERROR`.

`message`  
A readable description of the event.

`detail`  
Optional. Additional structured context for the event, such as a related resource or an error code. This field can be empty or absent.

The following example shows an `ERROR` record that Elemental Inference emitted for a feed.

```
{
  "resource_arn": "arn:aws:elemental-inference:us-west-2:111122223333:feed/abc123example",
  "event_timestamp": 1786646699596,
  "log_level": "ERROR",
  "message": "Access denied reading the template object. Verify that the access role has s3:GetObject on this URI. Continuing without templates.",
  "detail": {
    "template_uri": "s3://amzn-s3-demo-bucket/templates/example-template.json",
    "error_code": "TEMPLATE_READ_ACCESS_DENIED"
  }
}
```