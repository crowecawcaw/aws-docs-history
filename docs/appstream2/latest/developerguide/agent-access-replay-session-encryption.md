

# Encryption at rest for Replay Session

Replay Session encrypts your recordings at rest by default. While a session is recorded and processed, Replay Session holds the screen frames, their metadata, and the finished artifacts that are waiting for delivery in storage that AWS owns. By default, this content is encrypted at rest with Amazon S3 managed keys (SSE-S3). You don't need to take any action.

Optionally, you can provide a customer managed AWS Key Management Service (AWS KMS) key. When you do, Replay Session uses the AWS Encryption SDK to encrypt each frame, metadata object, tool response record, and artifact checkpoint under your key before it stores the object. You create, own, and manage the customer managed key, and you have full control over it. For more information, see [AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) in the *AWS Key Management Service Developer Guide*.

AWS KMS charges apply for customer managed keys. For more information, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/).

**Topics**
+ [How Replay Session uses a customer managed key](#agent-access-replay-session-encryption-how)
+ [Encrypting delivered artifacts in your bucket](#agent-access-replay-session-encryption-delivered)
+ [Configuring a customer managed key for Replay Session](#agent-access-replay-session-encryption-configure)
+ [Monitoring Replay Session interaction with AWS KMS](#agent-access-replay-session-encryption-monitoring)

## How Replay Session uses a customer managed key
<a name="agent-access-replay-session-encryption-how"></a>

Replay Session uses your customer managed key to encrypt the following content while a session is recorded and processed:
+ **Screen frames**. The frames captured during the session.
+ **Frame metadata**. The per-action metadata for each frame.
+ **Tool responses**. The result that each tool call returns.
+ **Artifact checkpoints**. The transcript, session video, and HTML report that Replay Session produces after the session, while they wait for delivery.

The customer managed key protects only this content in AWS-owned storage. It isn't used for the artifacts that Replay Session delivers to your bucket. For those artifacts, see [Encrypting delivered artifacts in your bucket](#agent-access-replay-session-encryption-delivered).

### Principals that use the key
<a name="agent-access-replay-session-encryption-principals"></a>

Every AWS KMS request that Replay Session makes runs as your own identity, with your own permissions. Two of your principals are involved:
+ **The principal that configures the stack**. The IAM identity that calls `CreateStack` or `UpdateStack`. It validates the key when you set or change it.
+ **The principal that uses the stack**. The IAM identity that starts the agent session, which is the identity that your agent uses to connect to the Model Context Protocol (MCP) service. It makes every other AWS KMS request. This principal isn't necessarily the person whose screen activity is recorded.

Replay Session doesn't use grants, service roles, service-linked roles, or roles that you provide, and you don't add a service principal to your key policy.

### AWS KMS operations
<a name="agent-access-replay-session-encryption-operations"></a>

Replay Session makes the following AWS KMS requests with your customer managed key. Each request arrives through one of two services, which you can use as the value of the `kms:ViaService` condition key:
+ **Stack configurer** requests come from the principal that configures the stack, through `appstream.{{region}}.amazonaws.com`.
+ **Stack user** requests come from the principal that uses the stack, through `agentaccess-mcp.{{region}}.amazonaws.com`.


**AWS KMS requests that Replay Session makes**  

| Operation | When | Caller | Purpose | 
| --- | --- | --- | --- | 
| DescribeKey | When you call CreateStack or UpdateStack with KmsKeyArn | Stack configurer | Validate the key | 
| Decrypt | Once per session, at the first recorded action | Stack user | Confirm at the start of the session that processing will be able to decrypt the recording. No data is decrypted. | 
| GenerateDataKey | During the session, three times for each action: once for the frame, once for the metadata object, and once for the tool response record | Stack user | Encrypt each object before it is stored | 
| Decrypt | After the session, three times for each action: once for the frame, once for the metadata object, and once for the tool response record | Stack user | Read the recording for processing | 
| GenerateDataKey | After the session, at least three times per session | Stack user | Encrypt the transcript, video, and report checkpoints | 
| Decrypt | After the session, once for each object, only if processing fails | Stack user | Deliver the raw frames, metadata, tool response records, and any completed artifact checkpoints to your bucket instead of the finished artifacts, so that no captured evidence is lost | 

Replay Session never calls `Encrypt`, `ReEncrypt*`, or `CreateGrant`. Replay Session doesn't cache data keys, so if you disable the key or remove access to it, the change takes effect at the next request.

AWS KMS requests continue for a few minutes after a session ends, while the recording is processed. As a result, you can see `Decrypt` and `GenerateDataKey` events in CloudTrail after the agent has disconnected.

### Request quotas and using a dedicated key
<a name="agent-access-replay-session-encryption-quotas"></a>

Each recorded action makes three `GenerateDataKey` requests during the session and three `Decrypt` requests after it: one each for the frame, the metadata object, and the tool response record. These requests count toward the AWS KMS request quotas for your AWS account, which all keys in the account and Region share. For more information, see [Request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html) in the *AWS Key Management Service Developer Guide*.

We recommend that you use a dedicated key for Replay Session. That way, key policy changes that you make for other workloads can't stop Replay Session from recording.

### When the key becomes unavailable
<a name="agent-access-replay-session-encryption-unavailable"></a>

If you disable the key, schedule it for deletion, or change its policy so that Replay Session can no longer use it, the following happens:
+ **During a session**. The next frame capture fails, and the agent's action fails with it. Every later action in that session also fails, because Replay Session doesn't let an agent act without recording the action. Changes to the key or its policy therefore control whether agents can act on stacks that use the key.
+ **After a session**. If the key becomes unavailable before processing finishes, the recording can't be processed or delivered, and it can't be recovered.

The principal that uses the stack must keep the `kms:Decrypt` and `kms:GenerateDataKey` permissions on the key, and the `s3:PutObject` permission on the destination bucket, for the whole session and until processing finishes. Keep the key enabled, and keep its permissions in place, until every session that used it has finished processing.

## Encrypting delivered artifacts in your bucket
<a name="agent-access-replay-session-encryption-delivered"></a>

Replay Session writes the delivered artifacts to your Amazon S3 bucket as the principal that uses the stack. The artifacts are encrypted with the default encryption of the bucket, which can be SSE-S3. The customer managed key that you set for Replay Session isn't used for these artifacts.

To encrypt the delivered artifacts with your own key, do the following:

1. Set SSE-KMS with an Amazon S3 Bucket Key as the default encryption for the bucket. For more information, see [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) and [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) in the *Amazon S3 User Guide*.

1. Give the principal that uses the stack the following permissions on the bucket's KMS key, through Amazon S3:
   + `kms:GenerateDataKey`, to write each artifact.
   + `kms:Decrypt`, to write artifacts larger than 8 MB. Larger artifacts are uploaded in multiple parts, and multipart uploads to an SSE-KMS bucket require `kms:Decrypt`.

## Configuring a customer managed key for Replay Session
<a name="agent-access-replay-session-encryption-configure"></a>

Replay Session supports a symmetric encryption KMS key that is enabled and is in the same Region as the stack. Keys in custom key stores and external key stores are supported. You can choose a Multi-Region key. The primary key or replica key that you choose must be in the same Region as the stack. Replay Session doesn't support the multi-Region features of the key.

**To encrypt Replay Session recordings with a customer managed key**

1. Create a symmetric encryption KMS key in the same Region as the stack, or choose an existing one. For more information, see [Create a symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-symmetric-cmk.html) in the *AWS Key Management Service Developer Guide*.

1. Add key policy statements that allow the principal that uses the stack to encrypt and read recordings, and allow the principal that configures the stack to validate the key. For details, see [Permissions for the customer managed key](#agent-access-replay-session-encryption-permissions).

1. Attach IAM policies to both principals.

1. Set `KmsKeyArn` in the `AgentAccessConfig` when you call `CreateStack` or `UpdateStack`. For details, see [Setting the key on a stack](#agent-access-replay-session-encryption-set-key).

1. Verify in CloudTrail that the expected `DescribeKey`, `GenerateDataKey`, and `Decrypt` events appear. For details, see [Monitoring Replay Session interaction with AWS KMS](#agent-access-replay-session-encryption-monitoring).

### Permissions for the customer managed key
<a name="agent-access-replay-session-encryption-permissions"></a>

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. For more information, see [KMS key access and permissions](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) in the *AWS Key Management Service Developer Guide*.

Which policies you need depends on where the key is:
+ If the key is in the same account as the stack, and its key policy includes the default statement that allows IAM policies to grant access to the key, the IAM policies in this section are enough.
+ If the key is in another account, or its key policy doesn't allow IAM policies to grant access, also add the key policy statements in this section.

**Key policy statements**

The following example statements give the principal that uses the stack (`ReplaySessionUserRole`) and the principal that configures the stack (`ReplaySessionAdminRole`) the permissions they need. Add these statements to your existing key policy. Don't replace the existing statements.

```json
{
    "Sid": "AllowAgentAccessDirectKMS",
    "Effect": "Allow",
    "Principal": { "AWS": "arn:aws:iam::111122223333:role/ReplaySessionUserRole" },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "agentaccess-mcp.us-east-1.amazonaws.com"
        },
        "StringLike": {
            "kms:EncryptionContext:aws:agentaccess-mcp:session_id": "*"
        }
    }
},
{
    "Sid": "AllowAppstreamToDescribeKey",
    "Effect": "Allow",
    "Principal": { "AWS": "arn:aws:iam::111122223333:role/ReplaySessionAdminRole" },
    "Action": "kms:DescribeKey",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "appstream.us-east-1.amazonaws.com"
        }
    }
}
```
+ `AllowAgentAccessDirectKMS` lets the principal that uses the stack encrypt and read the recording. The `kms:ViaService` condition limits these operations to requests that come through Replay Session. The `kms:EncryptionContext` condition requires the session encryption context to be present, with any value, because the value is a session ID that is assigned when the session starts.
+ `AllowAppstreamToDescribeKey` lets the principal that configures the stack validate the key when it creates or updates the stack. This statement has no encryption context condition, because `DescribeKey` doesn't take an encryption context.

Because each statement names a specific role as its principal, you don't need a `kms:CallerAccount` condition. If more than one role starts sessions or configures the stack, list each role in the matching statement.

**IAM policy for the principal that uses the stack**

Attach the following statement to the IAM identity that your agent uses to start sessions.

```json
{
    "Sid": "AllowReplaySessionFrameEncryption",
    "Effect": "Allow",
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "agentaccess-mcp.us-east-1.amazonaws.com"
        }
    }
}
```

**IAM policy for the principal that configures the stack**

Attach the following statements to the IAM identity that calls `CreateStack` or `UpdateStack`.

```json
{
    "Sid": "AllowReplaySessionKeyValidation",
    "Effect": "Allow",
    "Action": "kms:DescribeKey",
    "Resource": "arn:*:kms:*:*:key/*"
},
{
    "Sid": "AllowReplaySessionConsoleKeyListing",
    "Effect": "Allow",
    "Action": "kms:ListAliases",
    "Resource": "*"
}
```

These statements don't include a `kms:ViaService` condition, because the console lists your keys with `kms:ListAliases` and validates the key that you select with `kms:DescribeKey` directly, without a `kms:ViaService` value. If you configure stacks only through the API, you can remove the `AllowReplaySessionConsoleKeyListing` statement, limit `Resource` to your key, and add a `kms:ViaService` condition with the value `appstream.{{region}}.amazonaws.com`.

For more information, see [Specifying KMS keys in IAM policy statements](https://docs.aws.amazon.com/kms/latest/developerguide/cmks-in-iam-policies.html) and [Troubleshooting key access](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html) in the *AWS Key Management Service Developer Guide*.

**Using a key in another account**

To use a key in another account, configure the stack through the API. Both the key policy and the IAM policy of the principal that configures the stack must allow `kms:DescribeKey`.

### Setting the key on a stack
<a name="agent-access-replay-session-encryption-set-key"></a>

Set the key with the `KmsKeyArn` field in the `AgentAccessConfig` of the `CreateStack` and `UpdateStack` API operations. You can set `KmsKeyArn` whether or not `ReplaySessionEnabled` is `true`.

`KmsKeyArn` accepts a key ARN only. If you provide an alias ARN, an alias name, or a key ID, the request is rejected before Replay Session contacts AWS KMS.

When `KmsKeyArn` is present, the service calls `DescribeKey` as the principal that makes the request, to confirm that the key exists, is enabled, is a symmetric encryption KMS key, and is in the same Region as the stack.

The following example adds a customer managed key to an existing stack:

```bash
aws appstream update-stack \
    --name {{your-stack-name}} \
    --agent-access-config '{
        "S3BucketArn": "{{arn:aws:s3:::amzn-s3-demo-bucket}}",
        "ReplaySessionEnabled": true,
        "KmsKeyArn": "{{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}"
    }'
```

**Changing the key**

To change the key, call `UpdateStack` with a new `KmsKeyArn`. The service validates the new key the same way that it validates a key when you create a stack. Configuration is fixed for each session, so sessions that are already running keep the key that they started with, and new sessions use the new key. Replay Session doesn't re-encrypt content.

Content recorded under the previous key stays encrypted under that key. Keep the previous key enabled, and keep its key policy and IAM permissions in place, until every session that started under it has finished processing.

### Scoping down access to the key
<a name="agent-access-replay-session-encryption-scope"></a>

**Encryption context**

An [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) is an optional set of key-value pairs that contain additional contextual information about the data. AWS KMS uses the encryption context as additional authenticated data to support authenticated encryption. The encryption context also appears in CloudTrail logs, so you can use it to identify how your key is being used.

Every `GenerateDataKey` and `Decrypt` request that Replay Session makes includes the following encryption context pair. The key is `aws:agentaccess-mcp:session_id`, and the value is the ID of the session being recorded.

```json
"encryptionContext": {
    "aws:agentaccess-mcp:session_id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

The `aws:` prefix is part of the literal name of the encryption context key. It isn't a global IAM condition key.

Requests made through the AWS Encryption SDK, which are all requests except the `Decrypt` request at the start of the session, also include an `aws-crypto-public-key` encryption context pair that the AWS Encryption SDK adds.

When you write your own encryption context conditions, require the `aws:agentaccess-mcp:session_id` key and allow the `aws-crypto-public-key` key. Session IDs are assigned when each session starts, and every session on the stack uses the same key, so you can't name a specific session ID in a policy. Instead, require that the session ID key is present, as the `AllowAgentAccessDirectKMS` statement does with `"StringLike": { "kms:EncryptionContext:aws:agentaccess-mcp:session_id": "*" }`. Don't use a condition that requires the encryption context to contain only the session ID pair, or requests that the AWS Encryption SDK makes are denied.

**kms:ViaService**

The [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-via-service) condition key limits use of the key to requests that come from a specific AWS service. Replay Session uses the following values:
+ `agentaccess-mcp.{{region}}.amazonaws.com` for `GenerateDataKey` and `Decrypt` requests made to record, process, and deliver the recording.
+ `appstream.{{region}}.amazonaws.com` for `DescribeKey` requests made to validate the key.

**Confused deputy protection**

The `aws:SourceArn` and `aws:SourceAccount` condition keys don't apply to Replay Session. Every AWS KMS request runs as your own identity, and Replay Session doesn't use a service role, so there is no cross-service request for these keys to constrain. The key policy scopes access by naming the two roles.

## Monitoring Replay Session interaction with AWS KMS
<a name="agent-access-replay-session-encryption-monitoring"></a>

When you use a customer managed key with Replay Session, you can use CloudTrail to track the requests that Replay Session sends to AWS KMS. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html) in the *AWS Key Management Service Developer Guide*.

Look for the following events:
+ `DescribeKey`, made by the principal that configures the stack when the stack is created or updated, with the `kms:ViaService` value `appstream.{{region}}.amazonaws.com`.
+ `GenerateDataKey` and `Decrypt`, made by the principal that uses the stack, with the `kms:ViaService` value `agentaccess-mcp.{{region}}.amazonaws.com` and the `aws:agentaccess-mcp:session_id` encryption context. These events continue for a few minutes after the agent disconnects.

Events appear in the trail of the account that makes the request. For a key in another account, the events also appear in the account that owns the key.