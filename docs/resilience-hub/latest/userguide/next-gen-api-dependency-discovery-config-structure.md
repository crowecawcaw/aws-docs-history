

# DependencyDiscoveryConfig structure

```json
{
  "status": "INITIALIZING | ENABLED | DISABLED",
  "updatedAt": "timestamp",
  "eligibleResourceCount": integer,
  "message": "string"
}
```

The following table describes the fields in the `DependencyDiscoveryConfig` structure.


| Field | Required | Description | 
| --- | --- | --- | 
| status | Yes | The current state of dependency discovery. Valid values: INITIALIZING (discovery is running), ENABLED (discovery is complete and active), or DISABLED (discovery is turned off). | 
| updatedAt | No | The timestamp when the dependency discovery status was last updated. | 
| eligibleResourceCount | No | The number of Amazon EC2 instances, Lambda functions, and VPC resources in the service that are eligible for dependency discovery. Returns null until the resource discovery process completes its first run. | 
| message | No | A message describing the current state of discovery. Returns null when discovery is complete and dependencies are available. | 