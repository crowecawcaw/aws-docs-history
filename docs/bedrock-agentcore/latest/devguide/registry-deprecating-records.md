# Deprecating registry records

## Overview

Deprecation of a Registry Record removes the record from being discoverable in the Search Results (via SearchRegistryRecords API) as well as the Registry’s MCP endpoint. Deprecated is a Terminal State and once a record is in this state, it cannot be edited or transitioned to any other state. The Record can still be found via ListRegistryRecords and GetRegistryRecord APIs for auditing purposes, but cannot be un-deprecated.

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

```
aws bedrock-agentcore-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status DEPRECATED \
  --status-reason "Replaced by v2" \
  --region us-east-1
```

### AWS SDK

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
