

# Reviewing registry records
<a name="registry-reviewing-records"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Overview
<a name="registry-reviewing-overview"></a>

As a curator, you review records in Pending Approval status against your organization’s standards for security, compliance, and metadata quality.

## View pending records
<a name="registry-reviewing-view-pending"></a>

As a curator, you can find records awaiting review from the registry detail page, AWS CLI, or AWS SDK.

### Console
<a name="registry-reviewing-view-pending-console"></a>

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry you want to review.

1. In the **Registry records** section, the **Pending approval** status summary counter shows how many records are awaiting review.

1. Filter the records table by **Status** to show only records in **Pending approval** status.

1. Choose a record’s name to open its detail page and review its content.

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry you want to review.

1. In the **Registry records** section, the **Pending approval** status summary counter shows how many records are awaiting review.

1. Filter the records table by **Status** to show only records in **Pending approval** status.

1. Choose a record’s name to open its detail page and review its content.

### AWS CLI
<a name="registry-reviewing-view-pending-cli"></a>

**Example**  

```
aws agent-registry-control list-registry-records \
  --registry-id "<registryId>" \
  --filters '[{"name": "status", "values": ["PENDING_APPROVAL"]}]' \
  --region us-east-1
```

```
aws bedrock-agentcore-control list-registry-records \
  --registry-id "<registryId>" \
  --status PENDING_APPROVAL \
  --region us-east-1
```

### AWS SDK
<a name="registry-reviewing-view-pending-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.list_registry_records(
    registryId='<registryId>',
    filters=[{'name': 'status', 'values': ['PENDING_APPROVAL']}]
)
for record in response['registryRecords']:
    print(f"{record['displayName']} ({record['name']}) - {record['recordType']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.list_registry_records(
    registryId='<registryId>',
    status='PENDING_APPROVAL'
)
for record in response['registryRecords']:
    print(f"{record['name']} - {record['descriptorType']}")
```

## Approve a record
<a name="registry-reviewing-approve"></a>

### Console
<a name="registry-reviewing-approve-console"></a>

1. Open the record detail page for a record in **Pending approval** status.

1. Choose the **Update status** dropdown, then choose **Approve**.

1. In the **Update status** dialog, enter a **Reason** for the status change.

1. Choose **Update**.

### AWS CLI
<a name="registry-reviewing-approve-cli"></a>

**Example**  

```
aws agent-registry-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status APPROVED \
  --status-reason "Reviewed and approved" \
  --region us-east-1
```

```
aws bedrock-agentcore-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status APPROVED \
  --status-reason "Reviewed and approved" \
  --region us-east-1
```

### AWS SDK
<a name="registry-reviewing-approve-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.update_registry_record_status(
    registryId='<registryId>',
    recordId='<recordId>',
    status='APPROVED',
    statusReason='Reviewed and approved'
)
print(f"Status: {response['status']}")  # APPROVED
print(f"StatusReason: {response['statusReason']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.update_registry_record_status(
    registryId='<registryId>',
    recordId='<recordId>',
    status='APPROVED',
    statusReason='Reviewed and approved'
)
print(f"Status: {response['status']}")  # APPROVED
print(f"StatusReason: {response['statusReason']}")
```

## Reject a record
<a name="registry-reviewing-reject"></a>

### Console
<a name="registry-reviewing-reject-console"></a>

1. Open the record detail page for a record in **Pending approval** status.

1. Choose the **Update status** dropdown, then choose **Reject**.

1. In the **Update status** dialog, enter a **Reason** for the rejection.

1. Choose **Update**.

### AWS CLI
<a name="registry-reviewing-reject-cli"></a>

**Example**  

```
aws agent-registry-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status REJECTED \
  --status-reason "Missing tool input schemas" \
  --region us-east-1
```

```
aws bedrock-agentcore-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status REJECTED \
  --status-reason "Missing tool input schemas" \
  --region us-east-1
```

### AWS SDK
<a name="registry-reviewing-reject-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.update_registry_record_status(
    registryId='<registryId>',
    recordId='<recordId>',
    status='REJECTED',
    statusReason='Missing tool input schemas'
)
print(f"Status: {response['status']}")  # REJECTED
print(f"StatusReason: {response['statusReason']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.update_registry_record_status(
    registryId='<registryId>',
    recordId='<recordId>',
    status='REJECTED',
    statusReason='Missing tool input schemas'
)
print(f"Status: {response['status']}")  # REJECTED
print(f"StatusReason: {response['statusReason']}")
```

**Note**  
Publisher can edit and resubmit, or curator can directly approve a rejected record.