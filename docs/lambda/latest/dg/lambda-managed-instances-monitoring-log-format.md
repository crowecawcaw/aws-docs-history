

# Capacity provider system log format
<a name="lambda-managed-instances-monitoring-log-format"></a>

Capacity provider system logs use structured JSON format. JSON structured logs provide enhanced searchability and enable automated analysis of your capacity provider operational events.

## JSON format for system logs
<a name="lambda-managed-instances-log-format-json-structure"></a>

Each system log entry is captured as a JSON object that contains key-value pairs with the following top-level fields:


| Field | Type | Description | 
| --- | --- | --- | 
| timestamp | String | The time the log event was generated, in ISO 8601 format. | 
| level | String | The log level of the event. | 
| message | String | A human-readable description of the event. | 
| metadata | Object | Structured metadata about the event. Contains fields that vary by event type. | 

## Metadata fields
<a name="lambda-managed-instances-log-format-metadata"></a>

The `metadata` object contains the following fields. Not all fields are present in every event.


| Field | Type | Description | 
| --- | --- | --- | 
| instanceId | String | The Amazon EC2 instance ID associated with the event. | 
| availabilityZones | Array of strings | The Availability Zone(s) associated with the event. | 
| instanceTypes | Array of strings | The Amazon EC2 instance type(s) associated with the event. | 
| capacityProviderArn | String | The ARN of the capacity provider. | 

## Example log entry
<a name="lambda-managed-instances-log-format-examples"></a>

The following example shows a system log entry for a successful instance launch:

```
{
  "timestamp": "2025-07-01T14:31:15.456Z",
  "level": "INFO",
  "message": "Successfully launched c7g.xlarge instance i-0abc123def456789 in us-east-1a",
  "metadata": {
    "instanceId": "i-0abc123def456789",
    "availabilityZones": ["us-east-1a"],
    "instanceTypes": ["c7g.xlarge"],
    "capacityProviderArn": "arn:aws:lambda:us-east-1:123456789012:capacity-provider:my-capacity-provider"
  }
}
```