This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Access retained data

## S3 bucket structure

Retained data is organized in your S3 bucket using a date-based hierarchy:

```
s3:`//your-retention-bucket/`
wickr-drs-encrypted/YYYY/MM/DD/<vgroupid>/{file | message | username}


```

## File naming conventions

All files are: `{message sequence number}-{message id}.json` in the
encrypted bucket. Files are `{message sequence number}-{message
 id}.bin`.

## Triggering on-demand decryption

Messages in S3 are encrypted with your KMS key. Complete the following procedure
to use the **Step Functions** state machine to decrypt them
on-demand.

**In the AWS console**:

1. Navigate to **Step Functions** in the AWS
   console.
2. Select the `DecryptionStateMachine`.
3. Choose **Start execution**.
4. Provide input JSON:

```
{
 "startDate": `"2026-06-03",`
 "endDate": `"2026-06-04",`
 "vgroupid": `"ABC123",`
}

```

5. Monitor execution progress in real-time.
6. Once complete, decrypted files appear in the decrypted bucket.

**In the AWS CLI**:

```
aws stepfunctions start-execution \
 —state-machine-arn arn:aws:states:us-east-1:123456789012:stateMachine:DecryptionStateMachine \
 —input '{
    "startDate": `"2026-06-03",`
    "endDate": `"2026-06-04",`
    "vgroupid": `"ABC123",`

```

## Reading decrypted files:

You can read decrypted files directly from your decrypted S3 bucket.

```
import boto3
s3 = boto3.client(`'s3'`)
response = s3.get_object(
    Bucket=`'your-retention-bucket-decrypted'`,
    Key=`'wickr-drs/2026/03/20/vgroupid_ABC123/message1.txt'`
)
content = response[`'Body'`].read().decode(`'utf-8'`)
print(content)

```
