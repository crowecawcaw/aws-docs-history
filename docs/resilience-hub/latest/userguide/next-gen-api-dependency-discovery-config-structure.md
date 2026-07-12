# DependencyDiscoveryConfig structure

```
{
  "status": "INITIALIZING | ENABLED | DISABLED",
  "updatedAt": "timestamp",
  "eligibleResourceCount": integer,
  "message": "string"
}
```

The following table describes the fields in the
`DependencyDiscoveryConfig` structure.

| Field                   | Required | Description                                                                                                                                                                                     |
| ----------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status`                | Yes      | The current state of dependency discovery. Valid values:<br>`INITIALIZING` (discovery is running),<br>`ENABLED` (discovery is complete and active), or<br>`DISABLED` (discovery is turned off). |
| `updatedAt`             | No       | The timestamp when the dependency discovery status was last updated.                                                                                                                            |
| `eligibleResourceCount` | No       | The number of compute resources eligible for dependency discovery. Returns<br>`null` until the resource discovery process completes its first<br>run.                                           |
| `message`               | No       | A message describing the current state of discovery. Returns<br>`null` when discovery is complete and dependencies are<br>available.                                                            |
