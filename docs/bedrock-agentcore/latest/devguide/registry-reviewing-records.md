

# Reviewing registry records

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

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

```bash
aws agent-registry-control list-registry-records \
  --registry-id "<registryId>" \
  --filters '[{"name": "status", "values": ["PENDING_APPROVAL"]}]' \
  --region us-east-1
```

```bash
aws bedrock-agentcore-control list-registry-records \
  --registry-id "<registryId>" \
  --status PENDING_APPROVAL \
  --region us-east-1
```

### AWS SDK
<a name="registry-reviewing-view-pending-sdk"></a>

**Example**  

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.list_registry_records(
    registryId='<registryId>',
    filters=[{'name': 'status', 'values': ['PENDING_APPROVAL']}]
)
for record in response['registryRecords']:
    print(f"{record['displayName']} ({record['name']}) - {record['recordType']}")
```

```python
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.list_registry_records(
    registryId='<registryId>',
    status='PENDING_APPROVAL'
)
for record in response['registryRecords']:
    print(f"{record['name']} - {record['descriptorType']}")
```

## Review a skill package
<a name="registry-reviewing-skill-package"></a>

When a skill record has a skill package, you can download the package of the revision under review and inspect its files before you approve it. `GetRegistryRecord` returns the latest revision, so for a record in `PENDING_APPROVAL` status it returns the package that you’re reviewing, not the package of an earlier approved revision.

**Important**  
When the registry validates a skill package, it checks the archive structure and the SKILL.md format. It doesn’t check what the scripts and other files in the package do. Review them against your organization’s standards before you approve the record. For more information, see [Validate record metadata before you act on it](registry-data-protection.md#registry-consumer-validation).

### Console
<a name="registry-reviewing-skill-package-console"></a>

1. Open the record detail page for a Skills record in **Pending approval** status.

1. In the **Skill content** section, under **Skill package files**, browse the files in the package, and view or download each file.

1. To inspect the whole package locally, in the **Skill package** section, choose **Download**. Then choose **View checksum**, and compare the **SHA-256** value with the checksum of the downloaded file.

### AWS CLI
<a name="registry-reviewing-skill-package-cli"></a>

 `GetRegistryRecord` returns `artifact.downloadUrl`, a presigned URL that is valid for up to 5 minutes, and `artifact.sha256`. If the URL expires, call `GetRegistryRecord` again for a new one.

```bash
read -r URL SHA256 < <(aws agent-registry-control get-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --query '[artifact.downloadUrl, artifact.sha256]' \
  --output text \
  --region us-east-1)

curl -fsS -o skill-package.zip "$URL"
echo "$SHA256  skill-package.zip" | sha256sum -c -
```

### AWS SDK
<a name="registry-reviewing-skill-package-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to download the package under review and verify its checksum:

```python
import hashlib
import urllib.request

import boto3

client = boto3.client('agent-registry-control')

record = client.get_registry_record(
    registryId='<registryId>',
    recordId='<recordId>'
)
artifact = record['artifact']

with urllib.request.urlopen(artifact['downloadUrl']) as response:
    package = response.read()

if hashlib.sha256(package).hexdigest() != artifact['sha256']:
    raise ValueError('The downloaded package does not match its SHA-256 checksum')

with open('skill-package.zip', 'wb') as f:
    f.write(package)
```

If the registry is encrypted with a customer managed key, you need permission to use the key to get the download URL. For more information, see [Set customer managed key policy](registry-kms-key-policy.md). For more information about downloading packages, see [Download a skill package](registry-skill-package-download.md).

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

```bash
aws agent-registry-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status APPROVED \
  --status-reason "Reviewed and approved" \
  --region us-east-1
```

```bash
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

```python
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

```python
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

```bash
aws agent-registry-control update-registry-record-status \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --status REJECTED \
  --status-reason "Missing tool input schemas" \
  --region us-east-1
```

```bash
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

```python
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

```python
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