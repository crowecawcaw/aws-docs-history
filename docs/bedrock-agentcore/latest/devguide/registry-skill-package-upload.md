

# Upload a skill package

You can upload a skill package when you create a skill record, and replace or remove it later. The registry validates the package after the request returns, stores it, and copies its SKILL.md into the record’s `skillMd.data`.

Before you upload a package, make sure of the following:
+ The package follows the rules in [Skill package format and validation](registry-skill-package-format.md) and is no larger than the maximum package size in [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits) (5 MiB of ZIP data, before base64 encoding).
+ You have `agent-registry:CreateRegistryRecord` on the registry, or `agent-registry:UpdateRegistryRecord` on the record. If the registry is encrypted with a customer managed key, you also need `kms:GenerateDataKey` and `kms:Decrypt` on the key. The registry checks that you can use the key before it accepts the package. For more information, see [Set customer managed key policy](registry-kms-key-policy.md) and [IAM Permissions](registry-iam-permissions.md).

## Create a skill record with a package
<a name="registry-skill-package-upload-create"></a>

### Console
<a name="registry-skill-package-upload-create-console"></a>

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. In the **Record source** section, choose **Define manually**.

1. In the **Record details** section, enter a **Name** for the record.

1. For **Type**, choose **Skills**. For **Descriptor**, choose **Agent skills definition**.

1. (Optional) Expand **Additional configuration**, and enter a **Display name**, a **Description**, and a **Record version**.

1. In the **Skill content** section, for **Skill content source**, choose **Upload a package**.

1. For **Additional content**, choose **Skill definition** to add a structured skill definition in JSON, or **None**. The package supplies SKILL.md, so the editor for it isn’t offered on this path.

1. For **Skill package**, choose your .zip file, or drag and drop it onto the page.

   The console accepts a single .zip file of up to 5 MiB. Before you submit, it checks that the file has the .zip extension, that it’s a readable ZIP archive, and that it’s within the size limit. If you choose another file, it replaces the one that you chose.

1. (Optional) For **SHA-256 checksum**, enter the package’s SHA-256 checksum as 64 hexadecimal characters. The registry rejects the package if it doesn’t match. If you leave it blank, the registry still computes and stores its own checksum.

1. (Optional) In the **Tags** section, add tags to the record.

1. Choose **Create as draft**, or **Create and submit for approval**.

The record is in `CREATING` status while the registry validates the package. When validation finishes, the record moves to `DRAFT`, or to `CREATE_FAILED`. To see the problems, choose the record’s **Status** in the **Record details** section of the record detail page. If you chose **Create and submit for approval**, the console submits the record if validation finishes within about 30 seconds. Otherwise, wait for the record to reach `DRAFT` status, and then submit it for approval.

### AWS CLI
<a name="registry-skill-package-upload-create-cli"></a>

In the AWS CLI, `artifact.content` is base64 text inside the request JSON. Pass the request with `--cli-input-json`, because a package is usually too large for a command-line argument. The optional `sha256` is the lowercase hexadecimal SHA-256 checksum of the ZIP file itself, not of its base64 text.

**Note**  
These examples use the AWS CLI version 2 default binary format, `base64`. If your CLI configuration sets `cli_binary_format` to `raw-in-base64-out`, add `--cli-binary-format base64` to the command, so that the CLI doesn’t encode the content a second time.

The following commands encode the package, write the request with `jq`, and create the record:

```bash
# Checksum of the ZIP file, as lowercase hexadecimal
SHA256=$(sha256sum my-skill.zip | cut -d ' ' -f 1)

# Base64-encode the ZIP file, without line breaks
base64 -w 0 my-skill.zip > my-skill.zip.b64

jq -n \
  --arg registryId "<registryId>" \
  --rawfile content my-skill.zip.b64 \
  --arg sha256 "$SHA256" \
  '{
     registryId: $registryId,
     name: "my-skill",
     recordType: "SKILL",
     recordVersion: "1.0",
     descriptors: {agentSkillsDefinition: {}},
     artifact: {content: $content, sha256: $sha256}
   }' > create-skill-record.json

aws agent-registry-control create-registry-record \
  --cli-input-json file://create-skill-record.json \
  --region us-east-1
```

On macOS, use `shasum -a 256 my-skill.zip` for the checksum and `base64 -i my-skill.zip -o my-skill.zip.b64` to encode the file.

The response returns the record’s ARN and its status:

```json
{
    "recordArn": "arn:aws:agent-registry:us-east-1:111122223333:registry/AbCdEfGh1234/record/Rec123456789",
    "status": "CREATING"
}
```

To add a skill definition, set `agentSkillsDefinition` to `{"data": "<skill definition JSON>", "dataSchemaVersion": "0.1.0"}` instead of `{}`. Don’t send `skillMd.data`, because the registry sets it from the package.

To see the result of validation, get the record until its status is no longer `CREATING`:

```bash
aws agent-registry-control get-registry-record \
  --registry-id <registryId> \
  --record-id <recordId> \
  --query '{status: status, statusReason: statusReason}' \
  --region us-east-1
```

### AWS SDK
<a name="registry-skill-package-upload-create-sdk"></a>

The AWS SDKs take the package as bytes and encode it for you. The following example uses the AWS SDK for Python (Boto3):

```python
import hashlib
import time

import boto3

client = boto3.client('agent-registry-control')

with open('my-skill.zip', 'rb') as f:
    package = f.read()

response = client.create_registry_record(
    registryId='<registryId>',
    name='my-skill',
    recordType='SKILL',
    recordVersion='1.0',
    descriptors={'agentSkillsDefinition': {}},
    artifact={
        'content': package,                              # the ZIP bytes
        'sha256': hashlib.sha256(package).hexdigest(),   # optional
    },
)
record_arn = response['recordArn']
print(f"Status: {response['status']}")  # CREATING

# Wait for validation to finish
while True:
    record = client.get_registry_record(registryId='<registryId>', recordId=record_arn)
    if record['status'] not in ('CREATING', 'UPDATING'):
        break
    time.sleep(5)

print(record['status'], record.get('statusReason', ''))
```

## What happens after you upload
<a name="registry-skill-package-upload-status"></a>

 `CreateRegistryRecord` and `UpdateRegistryRecord` return as soon as the registry receives the package. Validation runs after the request returns:
+ On create, the record moves from `CREATING` to `DRAFT`, or to `CREATE_FAILED`.
+ On update, the record moves from `UPDATING` to `DRAFT`, or to `UPDATE_FAILED`. If the update fails, `GetRegistryRecord` keeps returning a download URL for the last uploaded package that passed validation. If the upload replaced a synchronized package, `GetRegistryRecord` returns no download URL until an update succeeds. For more information, see [Packages during an update](registry-skill-packages.md#registry-skill-packages-update-in-progress).

If validation fails, `statusReason` lists the problems. For information about how to read it, see [How validation failures appear](registry-skill-package-format.md#registry-skill-package-format-failures). To fix a `CREATE_FAILED` or `UPDATE_FAILED` record, upload a corrected package with `UpdateRegistryRecord`.

While the record is in `CREATING` or `UPDATING` status, you can’t update or delete it. A request to do so fails with a `ConflictException`.

## Replace the package
<a name="registry-skill-package-upload-replace"></a>

When you replace the package of an `APPROVED` record, the update creates a new `DRAFT` revision, even if the new package has the same bytes. Discovery keeps returning the approved package until you submit the new revision and it’s approved. For more information, see [Change the content of an approved record](registry-skill-packages.md#registry-skill-packages-approved-changes).

### Console
<a name="registry-skill-package-upload-replace-console"></a>

1. On the record detail page, choose **Manage**, and then choose **Edit**.

1. In the **Skill content** section, keep **Upload a package** selected.

   The record keeps the package that you already uploaded unless you choose a new file. SKILL.md comes from the package, so upload a new package to change it.

1. Under **Skill package**, choose the new .zip file.

1. (Optional) For **SHA-256 checksum**, enter the checksum of the new file. On a record that already has a package, the checksum applies only to a file that you choose in this request. It doesn’t verify the stored package, so a checksum on its own, without a new file, has no effect.

1. Choose **Save changes**.

### AWS CLI
<a name="registry-skill-package-upload-replace-cli"></a>

On `UpdateRegistryRecord`, wrap the package in `optionalValue`:

```bash
SHA256=$(sha256sum my-skill.zip | cut -d ' ' -f 1)
base64 -w 0 my-skill.zip > my-skill.zip.b64

jq -n \
  --arg registryId "<registryId>" \
  --arg recordId "<recordId>" \
  --rawfile content my-skill.zip.b64 \
  --arg sha256 "$SHA256" \
  '{
     registryId: $registryId,
     recordId: $recordId,
     recordVersion: "1.1",
     artifact: {optionalValue: {content: $content, sha256: $sha256}}
   }' > update-skill-record.json

aws agent-registry-control update-registry-record \
  --cli-input-json file://update-skill-record.json \
  --region us-east-1
```

 `recordVersion` is optional. Omit it to keep the record’s version.

### AWS SDK
<a name="registry-skill-package-upload-replace-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to replace the package:

```python
import hashlib

import boto3

client = boto3.client('agent-registry-control')

with open('my-skill.zip', 'rb') as f:
    package = f.read()

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    recordVersion='1.1',
    artifact={
        'optionalValue': {
            'content': package,
            'sha256': hashlib.sha256(package).hexdigest(),
        }
    },
)
print(f"Status: {response['status']}")  # UPDATING
```

## Remove the package
<a name="registry-skill-package-upload-remove"></a>

To remove an uploaded package, call `UpdateRegistryRecord` with `artifact` set to `{}`. The record no longer has a package, and `GetRegistryRecord` stops returning `artifact`. For an `APPROVED` record, the removal creates a new `DRAFT` revision, and discovery keeps returning the approved package until the new revision is approved. The record keeps the SKILL.md text that it had from the package (`skillMd.data`). To change that text too, send new `skillMd.data` in the same request.

 `artifact: {}` removes only a package that you uploaded. It doesn’t change a record whose package comes from a synchronized source. To stop synchronizing a package, remove `skillPackage` from the record. For the request syntax, see [Synchronize again or change the source](registry-skill-sync-s3.md#registry-skill-sync-s3-resync).

### Console
<a name="registry-skill-package-upload-remove-console"></a>

1. On the record detail page, choose **Manage**, and then choose **Edit**.

1. In the **Skill content** section, for **Skill content source**, choose **Author inline**.

1. For **Content to include**, choose **Skill documentation only**, **Skill definition only**, or **Skill documentation and definition**.

1. Enter the skill’s content.

1. Choose **Save changes**.

A skill that you author inline must have skill markdown or a skill definition. Enter one of them so that the console can save your changes.

### AWS CLI
<a name="registry-skill-package-upload-remove-cli"></a>

The following command removes the record’s uploaded package:

```bash
aws agent-registry-control update-registry-record \
  --registry-id <registryId> \
  --record-id <recordId> \
  --artifact '{}' \
  --region us-east-1
```

### AWS SDK
<a name="registry-skill-package-upload-remove-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to remove the package:

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    artifact={},    # removes the uploaded package
)
print(f"Status: {response['status']}")  # UPDATING
```

## Change how a record gets its content
<a name="registry-skill-package-upload-switch"></a>

A record gets its content in one way at a time: SKILL.md that you write, an uploaded package, or a source that the registry synchronizes from. To change the way, do one of the following:
+  **From upload to synchronization** — Call `UpdateRegistryRecord` with a new `skillMd.source` or `skillPackage.source`, and without `artifact`. The registry reads the source, and its content replaces the uploaded package. For more information, see [Synchronize a skill from Amazon S3](registry-skill-sync-s3.md) and [Synchronize a skill from GitHub](registry-skill-sync-github.md).
+  **From synchronization to upload** — Send the new package in `artifact.optionalValue`. We recommend that you also remove the source in the same request. Otherwise, the source stays on the record. A later `triggerSynchronization` then reads the source again and replaces your upload.
+  **From a package or a source to SKILL.md that you write** — Call `UpdateRegistryRecord` with new `skillMd.data`, and without `artifact`, `triggerSynchronization`, or a new source. Your text replaces the package or the synchronized content, and the record no longer has a package. A source that the record had stays on the record, unused. If you later change that source or set `triggerSynchronization`, the registry reads the source again, and its content replaces your text.

### Console
<a name="registry-skill-package-upload-switch-console"></a>

1. On the record detail page, choose **Manage**, and then choose **Edit**.

1. In the **Skill content** section, for **Skill content source**, choose **Author inline**, **Upload a package**, or **Synchronize from source**.

1. Complete the fields for the source that you chose, and then save the record.

The console warns you that saving with a different source replaces the record’s content with the new source’s, and removes the previous source, including an uploaded package. For the fields of each source, see the following:
+  **Author inline** – [Remove the package](#registry-skill-package-upload-remove) 
+  **Upload a package** – [Replace the package in the console](#registry-skill-package-upload-replace-console) 
+  **Synchronize from source** – [Change an Amazon S3 source in the console](registry-skill-sync-s3.md#registry-skill-sync-s3-resync-console), or [Change a GitHub source in the console](registry-skill-sync-github.md#registry-skill-sync-github-resync-console) 

The **Synchronize from source** tile appears only when you edit a record. To create a record that synchronizes, choose **Synchronize from source** in the **Record source** section of the **Create record** page instead. For more information, see [Create a record that synchronizes from Amazon S3](registry-skill-sync-s3.md#registry-skill-sync-s3-create) and [Create a record that synchronizes from GitHub](registry-skill-sync-github.md#registry-skill-sync-github-create).

On a record whose content comes from a package or a synchronized source, the markdown editor appears only on the **Author inline** tile. The package or the source owns SKILL.md. Choosing **Author inline** makes the markdown the record’s content, so you can edit it there. Saving then replaces the package or the source with what you entered.

The label above the editors differs by tile, because the package or the source already supplies SKILL.md. **Author inline** shows **Content to include**, where you choose the markdown, the definition, or both. **Upload a package** and **Synchronize from source** show **Additional content**, where the only choice is whether to add a skill definition.

### AWS CLI
<a name="registry-skill-package-upload-switch-cli"></a>

The following request body moves a record from synchronization to upload. It removes a full-package source and uploads a package in its place. Pass it with `--cli-input-json`, as described in [AWS CLI](#registry-skill-package-upload-create-cli):

```json
{
    "registryId": "<registryId>",
    "recordId": "<recordId>",
    "descriptors": {
        "optionalValue": {
            "agentSkillsDefinition": {
                "optionalValue": {
                    "additionalData": {
                        "optionalValue": {
                            "skillPackage": {}
                        }
                    }
                }
            }
        }
    },
    "artifact": {
        "optionalValue": {
            "content": "<base64 of the ZIP file>",
            "sha256": "<SHA-256 of the ZIP file>"
        }
    }
}
```

### AWS SDK
<a name="registry-skill-package-upload-switch-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to move a record from synchronization to upload:

```python
import hashlib

import boto3

client = boto3.client('agent-registry-control')

with open('my-skill.zip', 'rb') as f:
    package = f.read()

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    descriptors={
        'optionalValue': {
            'agentSkillsDefinition': {
                'optionalValue': {
                    'additionalData': {
                        'optionalValue': {
                            'skillPackage': {}    # removes the source
                        }
                    }
                }
            }
        }
    },
    artifact={
        'optionalValue': {
            'content': package,
            'sha256': hashlib.sha256(package).hexdigest(),
        }
    },
)
print(f"Status: {response['status']}")  # UPDATING
```

## Request rules
<a name="registry-skill-package-upload-rules"></a>

The registry rejects an upload with a `ValidationException` in the following cases:
+ The record’s `recordType` isn’t `SKILL`, or the record has no `agentSkillsDefinition` descriptor.
+ The record was created by auto-detection.
+ The request also sets `triggerSynchronization` or a new skill source, or sets `skillMd.source`.
+ The request also sends new `skillMd.data`. The registry takes SKILL.md from the package.
+ The content is empty, isn’t a ZIP archive, is larger than the maximum package size, or doesn’t match `sha256`.