

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Access retained data
<a name="retained-data"></a>

## S3 bucket structure
<a name="bucket-structure"></a>

Retained data is organized in your encrypted retention bucket by UTC date. The bucket name begins with `wickr-drs-<network-id>-`, where `<network-id>` is your Wickr network ID.

```
s3:{{//your-retention-bucket/}}
└── wickr-drs-encrypted/
    └── YYYY/MM/DD/
        └── <vgroupid>/
            ├── message/
            ├── username/
            └── file/ (optional)
```

The `vgroupid` uniquely identifies a room, group, or one-on-one conversation.
+ `message/` contains one encrypted JSON object for each message.
+ The `username/` folder stores zero-byte marker objects. Each object name is a username hash that identifies a participant. These objects aren't message content.
+ The `file/` folder appears when the conversation contains retained file attachments for that UTC date.

## File naming conventions
<a name="file-naming"></a>

Encrypted message objects use the format `<message-sequence-number>-<message-id>.json`. Each retained attachment is stored as two objects in the `file/` folder: `<message-sequence-number>-<message-id>.json` holds the encrypted attachment metadata, and `<message-sequence-number>-<message-id>-attachment.bin` holds the encrypted attachment. Username marker objects are named with a username hash and contain no data.

## Triggering on-demand decryption
<a name="decryption"></a>

Messages in S3 are encrypted with your KMS key. Complete the following procedure to use the **Step Functions** state machine to decrypt them on-demand.

**In the AWS console**:

1. Navigate to **Step Functions** in the AWS console.

1. Select the `DecryptionStateMachine`.

1. Choose **Start execution**.

1. Provide input JSON:

   ```
   {
    "startDate": {{"2026-06-03",}}
    "endDate": {{"2026-06-04",}}
    "vgroupid": {{"ABC123"}}
   }
   ```

   The `vgroupid` field is optional. If you provide it, the system decrypts only messages for that room or conversation. If you omit it, the system decrypts messages for all rooms and conversations in the date range.

1.  Monitor execution progress in real-time.

1.  Once complete, decrypted files appear in the decrypted bucket.

**In the AWS CLI**:

```
aws stepfunctions start-execution \
 --state-machine-arn arn:aws:states:us-east-1:111122223333:stateMachine:DecryptionStateMachine \
 --input '{
    "startDate": {{"2026-06-03",}}
    "endDate": {{"2026-06-04",}}
    "vgroupid": {{"ABC123"}}
 }'
```

## Reading decrypted files:
<a name="decrypted-files"></a>

You can read decrypted files directly from your decrypted S3 bucket. Each execution writes its output under a prefix named for the time the execution started (`YYYY-MM-DDTHH-MM-SS`, in UTC), then the date and `vgroupid` of the retained data. The `wickr-drs-decrypted` folder is a fixed prefix in your decrypted bucket. The time in the prefix uses hyphens instead of colons.

```
s3:{{//amzn-s3-demo-bucket-decrypted/}}wickr-drs-decrypted/{{{requested-date-time}}}/YYYY/MM/DD/{{{vgroup-id}}}/message/chunk-NNNN.json
s3:{{//amzn-s3-demo-bucket-decrypted/}}wickr-drs-decrypted/{{{requested-date-time}}}/YYYY/MM/DD/{{{vgroup-id}}}/file/{{{base-name}}}-metadata.json
s3:{{//amzn-s3-demo-bucket-decrypted/}}wickr-drs-decrypted/{{{requested-date-time}}}/YYYY/MM/DD/{{{vgroup-id}}}/file/{{{base-name}}}-file-{{{file-name}}}
```

The following Python example reads a decrypted message file from the bucket:

```
import boto3
s3 = boto3.client({{'s3'}})
response = s3.get_object(
    Bucket={{'amzn-s3-demo-bucket-decrypted'}},
    Key={{'wickr-drs-decrypted/2026-06-05T14-30-00/2026/06/03/ABC123/message/chunk-0000.json'}}
)
content = response[{{'Body'}}].read().decode({{'utf-8'}})
print(content)
```

## Stored message cleanup
<a name="stored-message-cleanup"></a>

Use this procedure to permanently remove retained content for one room, group, or one-on-one conversation for one UTC day. You identify the content by exact UTC date and exact `vgroupid`, and then delete only the object keys that you reviewed.

**Permanent deletion of stored content**  
This action permanently removes all retained messages, associated retained files, username markers, and every stored content version for the selected group or conversation for that UTC day—not only a selected message. You can't undo this action.

**Prerequisites**  
Use an administrator role with AWS Identity and Access Management (IAM) permissions to list and delete objects and object versions in the encrypted retention bucket. The required actions include `s3:ListBucket`, `s3:ListBucketVersions`, `s3:DeleteObject`, and `s3:DeleteObjectVersion`. Confirm that you have these permissions before you begin.  
Apply least-privilege permissions. Scope `s3:ListBucket` and `s3:ListBucketVersions` to the encrypted retention bucket. Scope `s3:DeleteObject` and `s3:DeleteObjectVersion` to the exact `wickr-drs-encrypted/YYYY/MM/DD/<vgroupid>/` object prefix in that bucket.  
Before you begin, identify your Wickr network ID, the exact `vgroupid`, and each applicable UTC date. For more information about the object path, see [Amazon S3 bucket structure](#bucket-structure).

**To identify the stored content**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the bucket list, select the encrypted retention bucket. Its name begins with `wickr-drs-<network-id>-`, where `<network-id>` is your Wickr network ID.

1. Browse to `wickr-drs-encrypted/YYYY/MM/DD/<vgroupid>/`. Replace `YYYY/MM/DD` with the exact UTC date, and replace `<vgroupid>` with the exact conversation ID.

1. Confirm that the folder contains `message/`, `username/`, and, when the conversation has retained attachments, `file/`.

**In the AWS CLI**:

The following examples use Bash syntax and require the AWS CLI to be installed and configured. Replace `<your-encrypted-retention-bucket>` with the bucket name from the Amazon S3 console. Replace `YYYY/MM/DD` with the exact UTC date. Replace `<vgroupid>` with the exact conversation ID:

```
bucket_name={{<your-encrypted-retention-bucket>}}
prefix=wickr-drs-encrypted/{{YYYY/MM/DD}}/{{<vgroupid>}}/
```

**To create the candidate key list**
+ List all object keys under the exact `vgroupid` prefix. The result includes message objects, zero-byte username markers, and retained file objects when they exist:

  ```
  aws s3api list-object-versions \
      --bucket "$bucket_name" \
      --prefix "$prefix" \
      --query 'Versions[].Key' \
      --output text | tr '\t' '\n' |
      grep -v '^None$' |
      sort -u > candidate_keys.txt
  
  cat candidate_keys.txt
  ```

**To review, delete, and verify candidate keys**

1. Review `candidate_keys.txt`. Confirm that every key belongs to the conversation and UTC date that you intend to clean up.

1. Copy the candidate list to `keys_to_delete.txt`. Remove any key that you don't want to delete:

   ```
   cp candidate_keys.txt keys_to_delete.txt
   # Edit keys_to_delete.txt before continuing.
   cat keys_to_delete.txt
   ```

1. For each reviewed key, list and delete every stored content version.

   ```
   while IFS= read -r object_key; do
       [ -z "$object_key" ] && continue
       aws s3api list-object-versions \
           --bucket "$bucket_name" \
           --prefix "$object_key" \
           --query "Versions[?Key=='$object_key'].VersionId" \
           --output text | tr '\t' '\n' |
       while IFS= read -r version_id; do
           [ -z "$version_id" ] && continue
           [ "$version_id" = "None" ] && continue
           aws s3api delete-object \
               --bucket "$bucket_name" \
               --key "$object_key" \
               --version-id "$version_id"
       done
   done < keys_to_delete.txt
   ```

1. Verify that no stored content versions remain for the reviewed keys. The command prints no rows when the cleanup is complete.

   ```
   while IFS= read -r object_key; do
       [ -z "$object_key" ] && continue
       aws s3api list-object-versions \
           --bucket "$bucket_name" \
           --prefix "$object_key" \
           --query "Versions[?Key=='$object_key'].[Key,VersionId]" \
           --output text
   done < keys_to_delete.txt
   ```

1. Repeat the applicable steps for each UTC date that you need to clean up.