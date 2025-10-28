# Troubleshoot workflow issues

This section describes possible solutions for issues with managed workflows.

###### Topics

- [Troubleshoot managed workflows issues](#workflow-errors "#workflow-errors")
- [Troubleshoot workflow decryption
  issues](#workflows-decrypt-issues "#workflows-decrypt-issues")

## Troubleshoot managed workflows issues

This section describes possible solutions for the following workflow issues.

###### Topics

- [Troubleshoot workflow-related errors
  using Amazon CloudWatch](#workflows-cloudwatch-errors "#workflows-cloudwatch-errors")
- [Troubleshoot workflow copy errors](#source-bucket-region "#source-bucket-region")

### Troubleshoot workflow-related errors

using Amazon CloudWatch

Description

If you are having issues with your workflows, you can use Amazon CloudWatch to investigate
the cause.

Cause

There can be several causes. Use Amazon CloudWatch Logs to investigate.

Solution

Transfer Family emits workflow execution status into CloudWatch Logs. The following types of workflow
errors can appear in CloudWatch Logs:

- `"type": "StepErrored"`
- `"type": "ExecutionErrored"`
- `"type": "ExecutionThrottled"`
- `"Service failure on starting workflow"`

You can filter your workflow's execution logs using different filter and pattern
syntax. For example, you can create a log filter in your CloudWatch logs to capture
workflow execution logs that contain the **ExecutionErrored**
message. For details, see [Real-time processing of
log data with subscriptions](../../../AmazonCloudWatch/latest/logs/Subscriptions.md "../../../AmazonCloudWatch/latest/logs/Subscriptions.md") and [Filter and
pattern syntax](../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md "../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md") in the _Amazon CloudWatch Logs User Guide_.

_StepErrored_

```
2021-10-29T12:57:26.272-05:00
            {"type":"StepErrored","details":{"errorType":"BAD_REQUEST","errorMessage":"Cannot
            tag Efs file","stepType":"TAG","stepName":"successful_tag_step"},
            "workflowId":"w-abcdef01234567890","executionId":"1234abcd-56ef-78gh-90ij-1234klmno567",
            "transferDetails":{"serverId":"s-1234567890abcdef0","username":"lhr","sessionId":"1234567890abcdef0"}
```

Here, `StepErrored` indicates that a step within the workflow has
generated an error. In a single workflow, you can have multiple steps configured.
This error tells you in which step the error occurred and provides an error message.
In this particular example, the step was configured to tag a file; however, tagging
a file in an Amazon EFS file system is not supported, so the step generated an
error.

_ExecutionErrored_

```
2021-10-29T12:57:26.618-05:00
            {"type":"ExecutionErrored","details":{},"workflowId":"w-w-abcdef01234567890",
            "executionId":"1234abcd-56ef-78gh-90ij-1234klmno567","transferDetails":{"serverId":"s-1234567890abcdef0",
            "username":"lhr","sessionId":"1234567890abcdef0"}}
```

When a workflow is not able to execute any step, it generates an
`ExecutionErrored` message. For example, if you have configured a
single step in a given workflow, and if the step is not able to execute, the overall
workflow fails.

_Executionthrottled_

Execution is throttled if a workflow is getting triggered at a rate that is faster
than the system can support. This log message indicates that you must slow down your
execution rate for workflows. If you are not able to scale down your
workflow-execution rate, contact AWS Support at [Contact AWS](https://aws.amazon.com/contact-us "https://aws.amazon.com/contact-us").

_Service failure on starting workflow_

Anytime you remove a workflow from a server and replace it with a new one, or
update server configuration (which impacts a workflow's execution role),
you must wait approximately 10 minutes before executing the new workflow. The
Transfer Family server caches the workflow details, and it takes 10 minutes for the server
to refresh its cache.

Additionally, you must log out of any active SFTP sessions, and then log back in after the 10-minute waiting period to see the changes.

### Troubleshoot workflow copy errors

Description

If you're executing a workflow that contains a step to copy the uploaded file,
you could encounter the following error:

```
{
  "type": "StepErrored", "details": {
    "errorType": "BAD_REQUEST", "errorMessage": "Bad Request (Service: Amazon S3; Status Code: 400; Error Code: 400 Bad Request;
    Request ID: `request-ID`; S3 Extended Request ID: `request-ID` Proxy: null)", "stepType": "COPY", "stepName": "`copy-step-name`" },
  "workflowId": "`workflow-ID`",
  "executionId": "`execution-ID`",
  "transferDetails": {
     "serverId": "`server-ID`",
     "username": "`user-name`",
     "sessionId": "`session-ID`"
  }
}
```

Cause

The source file is in an Amazon S3 bucket that is in a different AWS Region than the
destination bucket.

Solution

If you're executing a workflow that includes a copy step, make sure that the
source and destination buckets are in the same AWS Region.

## Troubleshoot workflow decryption

issues

This section describes possible solutions for the following issues with encrypted
workflows.

###### Topics

- [Troubleshoot anonymous recipient
  encryption issues](#workflows-decrypt-anonymous "#workflows-decrypt-anonymous")
- [Troubleshoot error for signed encryption
  file](#workflows-decrypt-signed "#workflows-decrypt-signed")
- [Troubleshoot error for a FIPS
  algorithm](#workflows-decrypt-fips "#workflows-decrypt-fips")

### Troubleshoot anonymous recipient

encryption issues

Description

Your decrypt workflow fails when processing certain encrypted files, but works
with others.

Cause

Files may have been encrypted without specifying a recipient (anonymous
encryption), making it difficult for the workflow to determine which key to use for
decryption.

Solution

Always encrypt files with a non-anonymous recipient using the `-r`
parameter. For example:

```
gpg -e -r `user@example.com` --openpgp file.txt
```

To check if a file was encrypted with a specific recipient or anonymously, use the
`--list-packets` command:

```
gpg --list-packets file.txt.gpg
```

This command displays the packet structure of the GPG-encrypted file without
decrypting its contents. Look for output that includes recipient information, such
as:

```
:pubkey enc packet: version 3, algo 1, keyid 1A2B3C4D5E6F7G8H
```

If you see keyid information, the file was encrypted for a specific recipient. If
this information is missing, the file may have been encrypted anonymously, which can
cause decryption failures in Transfer Family workflows.

You can also use this command to verify:

- Which encryption algorithms were used
- Compression methods (if any)
- Creation timestamps

To view the list of supported cipher algorithms for your GPG installation,
use:

```
gpg --version
```

This information can help you ensure that you're using encryption algorithms
compatible with Transfer Family workflows, especially when FIPS compliance is required.

### Troubleshoot error for signed encryption

file

Description

Your decrypt workflow fails and you receive the following error:

```
"Encrypted file with signed message unsupported"
```

Cause

Transfer Family does not currently support signing for encrypted files.

Solution

In your PGP client, if there is an option to sign the encrypted file, make sure to
clear the selection, as Transfer Family does not currently support signing for encrypted
files.

### Troubleshoot error for a FIPS

algorithm

Description

Your decrypt workflow fails, and the log message resembles the following:

```
{
   "type": "StepErrored",
   "details": {
      "errorType": "BAD_REQUEST",
      "errorMessage": "File encryption algorithm not supported with FIPS mode enabled.",
      "stepType": "DECRYPT",
      "stepName": "`step-name`"
   },
   "workflowId": "`workflow-ID`",
   "executionId": "`execution-ID`",
   "transferDetails": {
      "serverId": "`server-ID`",
      "username": "`user-name`",
      "sessionId": "`session-ID`"
   }
}
```

Cause

Your Transfer Family server has FIPS mode enabled and an associated Decrypt workflow step.
When encrypting the files before uploading to your Transfer Family server, the encryption
client might generate encrypted files that use non-FIPS approved symmetric
encryption algorithms. In such a scenario, the workflow is unable to decrypt files.
In the following example, **GnuPG** version 2.4.0 is using OCB (a
non-FIPS block cipher mode) to encrypt files: this causes the workflow to
fail.

Solution

You must edit the GPG key that you used to encrypt your files, and then re-encrypt
them. The following procedure describes the steps you must take.

###### To edit your PGP keys

1. Identify the key that you must edit by running `gpg
‐‐list-keys`

This returns a list of keys. Each key has details similar to the
following:

```
pub   ed25519 2022-07-07 [SC]
      wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
uid           [ultimate] Mary Major <marymajor@example.com>
sub   cv25519 2022-07-07 [E]
```

2. Identify the key that you want to edit. In the example shown in the
   previous step, the ID is `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.
3. Run `gpg ‐‐edit-key wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.

The system responds with details about the **GnuPG**
program and the specified key. 4. At the `gpg>` prompt, enter `showpref`. The
following details are returned:

```
[ultimate] (1). Mary Major <marymajor@example.com>
   Cipher: AES256, AES192, AES, 3DES
   AEAD: OCB
   Digest: SHA512, SHA384, SHA256, SHA224, SHA1
   Compression: ZLIB, BZIP2, ZIP, Uncompressed
   Features: MDC, AEAD, Keyserver no-modify
```

Note that the preferred algorithms that are stored on the key are
listed. 5. We want to edit the key to retain all algorithms except for
**OCB**. Run the `setpref` command,
specifying all the algorithms to retain:

```
gpg> setpref AES256, AES192,AES,3DES,SHA512, SHA384, SHA256, SHA224, SHA1,ZLIB, BZIP2, ZIP, Uncompressed
```

This returns the following details:

```
Set preference list to:
     Cipher: AES256, AES192, AES, 3DES
     AEAD:
     Digest: SHA512, SHA384, SHA256, SHA224, SHA1
     Compression: ZLIB, BZIP2, ZIP, Uncompressed
     Features: MDC, Keyserver no-modify
Really update the preferences? (y/N)
```

6. Enter `y` to update, then enter your password when prompted to
   confirm the change.
7. Save the changes.

```
gpg> save
```

Before re-running your decrypt workflow, you must re-encrypt your files, using the
edited key.
