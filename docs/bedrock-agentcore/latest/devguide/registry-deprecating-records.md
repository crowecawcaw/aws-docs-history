

# Deprecating registry records
<a name="registry-deprecating-records"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Overview
<a name="registry-deprecating-overview"></a>

When you deprecate a registry record, you remove it from the discoverable data-plane APIs (`SearchDiscoverableRegistryRecords`, `ListDiscoverableRegistryRecords`, `BatchGetDiscoverableRegistryRecord`) and from the registry’s MCP endpoint. Deprecated is a terminal state — after a record reaches this state, you cannot edit it or transition it to any other state. You can still find the record by using the `ListRegistryRecords` and `GetRegistryRecord` APIs for auditing purposes, but you cannot un-deprecate it.

Deprecate a record for reasons like you have decommissioned the resource, a newer version of the resource is published (with an independent record in the registry), the resource has known issues due to which you do not want other builders to discover the resource, or internal policy requires removal of the resource record.

## Deprecate a record
<a name="registry-deprecating-deprecate"></a>

### Console
<a name="registry-deprecating-console"></a>

1. Open the record detail page.

1. Choose the **Update status** dropdown, then choose **Deprecate**.

1. In the **Update status** dialog, enter a **Reason** for the deprecation.

1. Choose **Update**.

**Note**  
Deprecation is available from any record status.

### AWS CLI
<a name="registry-deprecating-cli"></a>

**Example**  

```
aws agent-registry-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status DEPRECATED \
  --status-reason "Replaced by v2" \
  --region us-east-1
```

```
aws bedrock-agentcore-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status DEPRECATED \
  --status-reason "Replaced by v2" \
  --region us-east-1
```

### AWS SDK
<a name="registry-deprecating-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.update_registry_record_status(
    registryId='<registryId>',
    recordId='<recordId>',
    status='DEPRECATED',
    statusReason='Replaced by v2'
)
print(f"Status: {response['status']}")  # DEPRECATED
print(f"StatusReason: {response['statusReason']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.update_registry_record_status(
    registryId='<registryId>',
    recordId='<recordId>',
    status='DEPRECATED',
    statusReason='Replaced by v2'
)
print(f"Status: {response['status']}")  # DEPRECATED
print(f"StatusReason: {response['statusReason']}")
```