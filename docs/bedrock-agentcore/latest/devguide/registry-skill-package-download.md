

# Download a skill package

When a skill record has a package, uploaded or synchronized, AWS Agent Registry returns it as a short-lived download URL together with the package’s SHA-256 checksum. You download the package from the URL, check it against the checksum, and extract it.

## Operations that return a download URL
<a name="registry-skill-package-download-apis"></a>

The following operations return a download URL for a skill package.


| Operation | Returns a download URL for | Permission | 
| --- | --- | --- | 
|  `GetRegistryRecord` (control plane) | The package of the record’s latest revision. Publishers and curators can use it to check a package before they approve it. |  `agent-registry:GetRegistryRecord` on the record. | 
|  `BatchGetDiscoverableRegistryRecord` (data plane) | The package of each requested record’s latest approved revision. |  `agent-registry:GetDiscoverableRegistryRecord` on each requested record. | 
|  `batch_get_discoverable_registry_record` tool of the registry’s MCP endpoint | The package of each requested record’s latest approved revision. |  `agent-registry:InvokeRegistryMcp` on the registry, and `agent-registry:GetDiscoverableRegistryRecord` on each requested record. | 

Each of these operations returns an `artifact` member for a record that has a package. No other operation returns a download URL: `SearchDiscoverableRegistryRecords`, `ListDiscoverableRegistryRecords`, `ListRegistryRecords`, the search and list tools of the MCP endpoint, and the responses of `CreateRegistryRecord` and `UpdateRegistryRecord` don’t include `artifact`.

A record returns no `artifact` in these cases:
+ Its content is inline, or it synchronizes only SKILL.md through `skillMd.source`.
+ It has no package yet: its status is `CREATING`, `CREATE_PENDING_AUTH`, or `CREATE_FAILED`.
+ An update switches it between an uploaded package and a synchronized package, and the update is in progress or has failed. `GetRegistryRecord` returns no download URL until such an update succeeds.

While any other update of the record is in progress or has failed (`UPDATING`, `UPDATE_PENDING_AUTH`, or `UPDATE_FAILED`), `GetRegistryRecord` returns a download URL for the record’s last package that passed validation. Discovery returns a download URL for the approved revision’s package. For more information, see [Packages during an update](registry-skill-packages.md#registry-skill-packages-update-in-progress).

## The artifact member
<a name="registry-skill-package-download-artifact"></a>

 `artifact` has the following members:

 `downloadUrl`   
A presigned Amazon S3 URL for the package. The URL is valid for up to 5 minutes, and no expiry time is returned with it. Download it over HTTPS with TLS 1.2 or later. To get a new URL, call the operation again. When you download it, Amazon S3 names the file after the record, as `<record name>.zip`, with each character other than a letter, digit, period, hyphen, or underscore replaced by an underscore. Browsers and tools that use the `Content-Disposition` header, such as `curl -OJ`, save the package under that name.

 `sha256`   
The SHA-256 checksum of the package, as 64 lowercase hexadecimal characters. The download response has no signature that you can check, so compare the checksum of the file that you download with this value before you use the package.

```json
"artifact": {
    "downloadUrl": "https://<bucket>.s3.us-east-1.amazonaws.com/...?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=300&...",
    "sha256": "3f2c7d9e0b4a61c8f5e2d7a9b1c3e5f708192a3b4c5d6e7f8091a2b3c4d5e6f7"
}
```

The download URL is a bearer credential. Anyone who has it can download the package until the URL expires, without AWS credentials or permissions. Don’t log, store, or share it. Removing a caller’s permissions doesn’t revoke URLs that the caller already received.

## Permissions
<a name="registry-skill-package-download-permissions"></a>

The registry checks the caller’s permissions on the operation that returns the URL, record by record:
+ Record-level `Allow` and `Deny` statements on `agent-registry:GetRegistryRecord` and `agent-registry:GetDiscoverableRegistryRecord` also decide who gets a record’s package. `BatchGetDiscoverableRegistryRecord` returns a record that the caller can’t read as an `ACCESS_DENIED` error, with no package. For more information, see [IAM Permissions](registry-iam-permissions.md).
+ Downloading from the URL itself needs no IAM or KMS permission.
+ If the registry is encrypted with a customer managed key, a caller that signs requests with IAM credentials also needs `kms:Decrypt` on the key, with the registry’s encryption context, to receive a download URL. This is the same permission that the caller needs to read the record’s descriptors. For the key policy statement, see [Set customer managed key policy](registry-kms-key-policy.md).
+ If the registry’s customer managed key is disabled, or the key policy or the registry’s grant doesn’t allow AWS Agent Registry to use the key, the read fails with an error and returns no download URL.

## Console
<a name="registry-skill-package-download-console"></a>

1. Open the record detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Skill package** section, choose **Download**. The console gets a fresh download URL each time you choose it, and opens the download in a new tab. The file is named `artifact.zip`.

1. To see the checksum, choose **View checksum**. Use the **SHA-256** value to verify the file that you downloaded.

The **Skill package files** section lists the files in the package, with the package’s uncompressed size. In the **Skill package files** section, you can do the following:
+ To find a file, use **Find files**. To show the whole tree again, clear the filter.
+ To expand or collapse the whole tree, choose **Expand all** or **Collapse all**.
+ To view a file’s contents, choose the file. For a Markdown file, choose **Rendered** or **Source**.
+ To download the open file, choose **Download file**.

The console limits how it previews some files:
+ It shows only the beginning of a very large file.
+ It shows a code file that is too large to highlight as plain text.
+ It previews only UTF-8 text files.

To see a file in full, download it.

Because the package includes SKILL.md, it appears in the package file browser rather than in the **Skill content** section.

For a record with a browsable package, **Skill content** shows only the skill definition. The console leaves out the section when the record has none.

If the package doesn’t match its SHA-256 checksum, the console doesn’t show its files. If the package can’t be downloaded or read, the console reports the error and offers **Retry**. If the record’s package is replaced or removed while you have the package file browser open, the console tells you to refresh the page.

When you browse a registry’s approved records in the console and open a record from the record list, the console shows the package of the record’s approved revision. A record that you open from search results shows no package.

## AWS CLI
<a name="registry-skill-package-download-cli"></a>

To install a skill directly into your AI coding agents in one command, see [Install skills with the AWS CLI](registry-skill-install-cli.md).

The following commands get the latest revision’s package with `GetRegistryRecord`, download it, verify its checksum, and extract it:

```bash
read -r DOWNLOAD_URL SHA256 <<< "$(aws agent-registry-control get-registry-record \
  --registry-id <registryId> \
  --record-id <recordId> \
  --query '[artifact.downloadUrl, artifact.sha256]' \
  --output text \
  --region us-east-1)"

curl --fail --silent --show-error --proto '=https' --tlsv1.2 \
  --output my-skill.zip "$DOWNLOAD_URL"

echo "$SHA256  my-skill.zip" | sha256sum --check

unzip -d my-skill my-skill.zip
```

To get the approved revision’s package as a consumer, use `BatchGetDiscoverableRegistryRecord`:

```bash
read -r DOWNLOAD_URL SHA256 <<< "$(aws agent-registry batch-get-discoverable-registry-record \
  --entries '[{"registryId": "<registryARN>", "recordIds": ["<recordId>"]}]' \
  --query 'registryRecords[0].artifact.[downloadUrl, sha256]' \
  --output text \
  --region us-east-1)"
```

On macOS, verify the checksum with `echo "$SHA256 my-skill.zip" | shasum -a 256 --check`.

For a registry that uses JSON Web Token (JWT) authorization, call `BatchGetDiscoverableRegistryRecord` with an HTTP client and a bearer token, as described in [Browse approved records](registry-browse-records.md). Each record in the response has the same `artifact` member.

## AWS SDK
<a name="registry-skill-package-download-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to get the approved packages of several records, verify each one, and extract it:

```python
import hashlib
import io
import urllib.request
import zipfile

import boto3

client = boto3.client('agent-registry')

response = client.batch_get_discoverable_registry_record(
    entries=[{'registryId': '<registryARN>', 'recordIds': ['<recordId1>', '<recordId2>']}]
)

for error in response['errors']:
    print(f"Not returned: {error['recordId']} ({error['errorCode']})")

for record in response['registryRecords']:
    artifact = record.get('artifact')
    if artifact is None:
        print(f"{record['recordId']} has no skill package")
        continue

    with urllib.request.urlopen(artifact['downloadUrl']) as download:
        package = download.read()

    if hashlib.sha256(package).hexdigest() != artifact['sha256']:
        raise ValueError(f"Checksum mismatch for {record['recordId']}")

    with zipfile.ZipFile(io.BytesIO(package)) as archive:
        archive.extractall(f"skills/{record['recordId']}")
```

To get the latest revision’s package as a publisher, call `get_registry_record` on the `agent-registry-control` client and read `response['artifact']` in the same way.

**Important**  
The checksum proves that you received the package that the registry stored. It doesn’t prove that the package is safe. AWS Agent Registry checks the structure of a package but doesn’t scan it for malware or check what its scripts do. Before an agent installs or runs a skill, validate it in the same way as any other content from an external source. For more information, see [Validate record metadata before you act on it](registry-data-protection.md#registry-consumer-validation).