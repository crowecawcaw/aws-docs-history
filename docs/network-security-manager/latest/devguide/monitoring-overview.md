

# Monitoring AWS Network Security Manager
<a name="monitoring-overview"></a>

Monitoring AWS Network Security Manager helps you understand whether your resources are protected as intended. AWS Network Security Manager provides the following monitoring capabilities:
+ **Synchronization status APIs** -- Query the protection state of individual resources across your deployments.
+ **AWS CloudTrail** -- Record all AWS Network Security Manager API calls for auditing, compliance, and operational troubleshooting.

## Monitoring synchronization status
<a name="monitoring-sync-status"></a>

The primary way to monitor whether your resources are protected is through the synchronization status APIs. AWS Network Security Manager evaluates each in-scope resource and records whether its actual firewall configuration matches the intended configuration.

### Synchronization status operations
<a name="monitoring-sync-operations"></a>

AWS Network Security Manager provides two operations for querying synchronization status:

ListResourceSynchronizationStatuses  
Returns per-resource status for a specific deployment. Requires a `deploymentIdentifier` parameter. Optionally filter by `synchronizationStatus` (IN\_SYNC, OUT\_OF\_SYNC, or NOT\_APPLICABLE).

ListAggregateResourceSynchronizationStatuses  
Returns per-resource aggregate status across all of your deployments. Optionally filter by `synchronizationStatus`. This operation shows the combined result of all policies that apply to each resource.

Both operations support pagination with `maxResults` (1 to 100) and `nextToken`.

### Understanding synchronization status values
<a name="monitoring-sync-values"></a>

IN\_SYNC  
The resource's actual firewall configuration matches the effective configuration computed from all applicable policies.

OUT\_OF\_SYNC  
The resource's actual configuration differs from the effective configuration. The `outOfSyncReasons` field provides per-setting details showing expected versus actual values.

NOT\_APPLICABLE  
The resource's account and resource type are in scope, but the resource itself does not match the scope filters (for example, a tag filter excludes it). No action is needed.

If a resource does not appear in the results at all, the account or resource type is not in scope for the deployment. Check your scope configuration.

### Understanding evaluation timestamps
<a name="monitoring-sync-timestamps"></a>

Each synchronization status entry includes two timestamps:
+ `evaluatedAt` -- When AWS Network Security Manager last evaluated the resource's configuration. A stale `evaluatedAt` value indicates that evaluation has not yet run for recent changes.
+ `updatedAt` -- When the synchronization status record itself last changed. If `updatedAt` is older than `evaluatedAt`, the status has been stable since the last evaluation.

### Cross-account visibility
<a name="monitoring-sync-cross-account"></a>

When multiple administrators protect the same resource, visibility into the aggregate synchronization status depends on the `enableCrossAccountVisibility` setting on each deployment.
+ If all deployments covering a resource have cross-account visibility enabled, any administrator can see the full aggregate status and out-of-sync reasons.
+ If any deployment has cross-account visibility disabled, other administrators see a `NOT_VISIBLE` marker instead of detailed reasons. This indicates that another administrator also protects the resource but has not shared visibility.

### Diagnosing out-of-sync resources
<a name="monitoring-sync-diagnosing"></a>

When a resource reports OUT\_OF\_SYNC, the `outOfSyncReasons` field identifies the specific configuration differences. The top-level reason is one of:
+ `missingFirewall` -- No firewall protection is associated with the resource.
+ `invalidFirewall` -- A firewall exists but its configuration does not match expectations. Specific differences are listed in categorized buckets.

If remediation is enabled but cannot fix the resource, the `remediationIssues` field provides a `correctiveAction` with guidance on how to resolve the issue manually. Remediation is a policy-level setting that is turned off by default. For more information, see [Synchronization and remediation](concepts.md#concepts-synchronization).

Multiple deployments with different configurations can target the same resource. In this case, the per-deployment synchronization status can be OUT\_OF\_SYNC while the aggregate synchronization status is IN\_SYNC. This is expected behavior, not a failure. A higher-priority policy's settings took precedence during merging. As a result, the resource matches the effective configuration, even though it does not match the configuration of the lower-priority deployment.