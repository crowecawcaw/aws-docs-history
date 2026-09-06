

# Monitoring discovery status
<a name="next-gen-discovery-status"></a>

After you enable dependency discovery, the `DependencyDiscoveryConfig` object returned by the `GetService` and `ListServices` API operations includes fields that indicate whether eligible resources have been found and whether dependency analysis is still in progress.

The following table describes the fields that indicate the current state of dependency discovery.


| Field | Type | Description | 
| --- | --- | --- | 
| status | String | The current state of dependency discovery: INITIALIZING, ENABLED, or DISABLED. | 
| eligibleResourceCount | Integer | The number of compute resources eligible for dependency discovery. This value is null until the resource discovery process completes its first run, and is updated on each subsequent run. | 
| message | String | A message describing the current state of discovery. This value is null when discovery is complete and dependencies are ready to view. | 

The `message` field provides context about the current state of discovery based on the status and the number of eligible resources. The following table shows the possible messages.


| Status | Eligible resource count | Message | 
| --- | --- | --- | 
| INITIALIZING | Not yet available | "Discovering resources" | 
| INITIALIZING | 0 | "No eligible resources discovered" | 
| INITIALIZING | 1 or more | "Discovering dependencies" | 
| ENABLED | 0 | "No eligible resources discovered" | 
| ENABLED | 1 or more | None. Dependencies are ready to view. | 
| DISABLED | Any | "Enable dependency discovery to display dependencies." | 

The following example shows how to check discovery status using the AWS CLI.

```
aws resiliencehubv2 get-service \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/checkout:abc123"
```

The response includes the `dependencyDiscovery` object:

```
{
  "service": {
    ...
    "dependencyDiscovery": {
      "status": "INITIALIZING",
      "updatedAt": "2026-06-30T10:00:00Z",
      "eligibleResourceCount": 5,
      "message": "Discovering dependencies"
    }
  }
}
```

When the `message` field is `null` and `status` is `ENABLED`, dependency discovery is complete and results are available through the `ListDependencies` operation.

**Note**  
If `eligibleResourceCount` is 0 after discovery completes, make sure that your service's compute resources meet the prerequisites described in [Prerequisites for dependency discovery](next-gen-discovery-prerequisites.md).