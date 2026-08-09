# Deprecating registry records

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

## Overview

When you deprecate a registry record, you remove it from the discoverable data-plane APIs (`SearchDiscoverableRegistryRecords`, `ListDiscoverableRegistryRecords`, `BatchGetDiscoverableRegistryRecord`) and from the registry’s MCP endpoint. Deprecated is a terminal state — after a record reaches this state, you cannot edit it or transition it to any other state. You can still find the record by using the `ListRegistryRecords` and `GetRegistryRecord` APIs for auditing purposes, but you cannot un-deprecate it.

Deprecate a record for reasons like you have decommissioned the resource, a newer version of the resource is published (with an independent record in the registry), the resource has known issues due to which you do not want other builders to discover the resource, or internal policy requires removal of the resource record.

## Deprecate a record

### Console

1. Open the record detail page.
2. Choose the **Update status** dropdown, then choose **Deprecate**.
3. In the **Update status** dialog, enter a **Reason** for the deprecation.
4. Choose **Update**.

###### Note

Deprecation is available from any record status.

### AWS CLI

###### Example

AWS Agent Registry namespace

```
aws agent-registry-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status DEPRECATED \
  --status-reason "Replaced by v2" \
  --region us-east-1
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
aws bedrock-agentcore-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status DEPRECATED \
  --status-reason "Replaced by v2" \
  --region us-east-1
```

### AWS SDK

###### Example

AWS Agent Registry namespace

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

Amazon Bedrock AgentCore namespace (to be deprecated)

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
