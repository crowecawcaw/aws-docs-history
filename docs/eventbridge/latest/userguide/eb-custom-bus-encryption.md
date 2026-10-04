

# Encryption at Rest for Amazon EventBridge Custom Event Bus
<a name="eb-custom-bus-encryption"></a>

## Options for Encryption at Rest
<a name="eb-custom-bus-encryption-at-rest"></a>

Amazon EventBridge Custom Event Bus encrypts all of your data at rest by default, server side, before it is written to storage: event payloads, event metadata, subscriber filter patterns, and subscriber target configurations. You do not need to configure anything, create any keys, or grant any permissions to get encryption at rest, and there is no additional cost for this default encryption.

By default, your data is encrypted using 256-bit Advanced Encryption Standard (AES-256) under an **AWS owned key**, a KMS key that EventBridge owns and manages for you. You cannot view, manage, or use this key, and its use does not appear in your AWS CloudTrail logs. AWS owned keys are free of charge and do not count against the AWS KMS quotas in your account. AWS owned keys are automatically rotated monthly.

For more information, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) in the *AWS Key Management Service Developer Guide*.

Optionally, you can choose to encrypt an event bus with a symmetric **customer managed KMS key** that you create, own, and manage. A customer managed key gives you:
+ Full control over the key lifecycle: key policy, rotation, disabling, deletion.
+ CloudTrail visibility into how EventBridge uses your key.
+ The ability to scope access with KMS key policy conditions, per event bus.

Customer managed keys incur AWS KMS charges: a monthly fee for the key, and charges for the KMS API requests made to it. These requests also count against the AWS KMS request quotas in your account. Because EventBridge encrypts and decrypts events locally under a cached branch key (see [How Custom Event Bus uses a Customer Managed KMS Key for encryption at rest](#eb-custom-bus-encryption-branch-key)), its KMS request volume is a few calls per event bus per cache window plus key rotation — it does not grow with your event volume. For details, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/).

## Encrypting Data at Rest using Customer Managed KMS Keys for Custom Event Bus
<a name="eb-custom-bus-encryption-cmk"></a>

### How Custom Event Bus uses a Customer Managed KMS Key for encryption at rest
<a name="eb-custom-bus-encryption-branch-key"></a>

**What is encrypted with your key** (per event bus):
+ Event payloads and event metadata, stored for the bus's retention period (1-365 days) in the bus's event storage and in per-subscriber delivery storage.
+ Subscriber filter patterns and target configurations, stored with the bus's configuration.

**What is not encrypted with your key:**
+ Resource identifiers that EventBridge needs for routing and lookup: bus name, bus ARN, account ID.
+ The message group ID, which orders FIFO delivery. Avoid placing sensitive data in this field.
+ The message deduplication ID. EventBridge stores it as a one-way hash.
+ Internal service metadata: subscription match results, sequence numbers.

These items are still encrypted at rest by the underlying storage services, not by your key.

**How encryption works.** When you configure a customer managed key on an event bus, EventBridge creates a **branch key** for that bus. The branch key is an intermediate key. It is stored in a service-managed table, wrapped by your KMS key, following the AWS Encryption SDK [Hierarchical Keyring](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-hierarchical-keyring.html). EventBridge uses the branch key to derive per-event data encryption keys. So events are encrypted and decrypted locally, without a KMS call per event:
+ When you publish an event, EventBridge encrypts it under the bus's branch key before any write to storage.
+ When EventBridge delivers an event, it decrypts the event for filter evaluation and delivery.
+ **EventBridge sends the decrypted event to your target.** Encryption at rest at the destination is the destination service's responsibility.
+ The branch key is cached in service memory for up to **15 minutes**. On cache expiry, EventBridge calls `kms:Decrypt` against your key to unwrap the branch key again.
+ EventBridge rotates the branch key by creating a new version approximately every **30 days**. Older versions are retained so previously written events remain readable for the bus's retention period.

**Two access paths.** EventBridge accesses your key in exactly two ways. For synchronous operations and authorization checks, it uses **your credentials**, forwarded from your API call. For asynchronous work (event delivery, the branch-key lifecycle) it acts as the **`events.amazonaws.com` service principal**, because your API call has completed and your credentials are no longer available. Your key policy governs both paths, as described below.

### Configuring a Customer Managed KMS Key on an event bus
<a name="eb-custom-bus-encryption-configure"></a>

Supported key types:
+ **Symmetric encryption keys only** (`SYMMETRIC_DEFAULT`, key usage `ENCRYPT_DECRYPT`). Asymmetric keys and HMAC keys are rejected.
+ Multi-Region keys are supported as ordinary keys: use the replica in the event bus's Region. EventBridge does not replicate your data or your key material across Regions.
+ Keys with imported key material and keys in an external key store (XKS) are supported.

**Key identifier.** Specify the key by its **key ARN**.

#### Configuring permissions to use a Customer Managed KMS Key
<a name="eb-custom-bus-encryption-key-policy"></a>

Your key policy needs three statements for EventBridge Custom Event Bus. Replace the example account, Region, role, and bus name.

An [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) is a set of non-secret key-value pairs that AWS KMS cryptographically binds to a request, and that you can use as a condition for authorization in key policies. Every KMS request EventBridge makes for an event bus includes an **encryption context** that binds the request to that bus's ARN, so each statement below can be scoped to a single bus. The context key is `aws:events:event-busv2:arn` and its value is the bus ARN, on every request EventBridge makes — whether with your credentials or as the service principal. [Scoping down access to the Customer Managed KMS Key](#eb-custom-bus-encryption-scope) covers scoping in more detail. The trailing `/*` in the encryption-context values matches the bus ARN's suffix, which EventBridge generates at creation (`arn:aws:events:{{region}}:{{account}}:event-busv2/{{name}}/{{suffix}}`).

```
{
  "Version": "2012-10-17",
  "Id": "eventbridge-eventbus-v2-cmk-policy",
  "Statement": [
    {
      "Sid": "AllowKeyValidationThroughEventBridge",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/ExampleRole" },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": { "kms:ViaService": "events.us-east-1.amazonaws.com" }
      }
    },
    {
      "Sid": "AllowKeyUseThroughEventBridge",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/ExampleRole" },
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:ReEncryptFrom",
        "kms:ReEncryptTo"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": { "kms:ViaService": "events.us-east-1.amazonaws.com" },
        "StringLike": {
          "kms:EncryptionContext:aws:events:event-busv2:arn": "arn:aws:events:us-east-1:111122223333:event-busv2/my-bus/*"
        }
      }
    },
    {
      "Sid": "AllowEventBridgeServicePrincipal",
      "Effect": "Allow",
      "Principal": { "Service": "events.amazonaws.com" },
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:ReEncryptFrom",
        "kms:ReEncryptTo"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:events:event-busv2:arn": "arn:aws:events:us-east-1:111122223333:event-busv2/my-bus/*"
        }
      }
    }
  ]
}
```

**Purpose of each statement:**
+ **`AllowKeyValidationThroughEventBridge`** lets your principals validate the key when creating or updating an event bus. EventBridge calls `kms:DescribeKey` with your credentials to confirm the key exists, is symmetric, and is enabled. The `DescribeKey` API has no encryption-context parameter. So this statement has no encryption-context condition. The `kms:ViaService` condition limits this statement's grant to requests that come through EventBridge.
+ **`AllowKeyUseThroughEventBridge`** authorizes the access checks EventBridge runs **with your credentials**. EventBridge runs these checks before it accepts a key configuration and before it writes or reads encrypted data on your behalf. So you cannot configure a key that EventBridge's later, asynchronous processing cannot use. The checks are KMS *dry runs*: they authorize but do not encrypt or decrypt anything. Dry-run requests are billed as standard KMS API requests and count against your KMS request quotas; see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the *AWS Key Management Service Developer Guide*. Per operation:
  + `CreateEventBus` with a customer managed key checks `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptFrom`/`kms:ReEncryptTo`, and `kms:Decrypt`. These are the actions that branch-key creation and later reads perform.
  + An `UpdateEventBus` key change checks `kms:Decrypt` on the current key, plus `kms:Encrypt` and `kms:Decrypt` on the new key. These are the actions the key transition performs.
  + `PutEvents` / `PutRawEvents` on a bus with a customer managed key checks `kms:Decrypt`. A caller who cannot read the bus's events back may not write them either.
  + `CreateSubscriber` / `UpdateSubscriber` checks `kms:Decrypt`, because subscriber configuration is encrypted under the bus key.

  **Choosing principals for this statement.** You can list individual role or user ARNs in the `Principal`, or use the account root principal to delegate this access to IAM policies in your account.
+ **`AllowEventBridgeServicePrincipal`** authorizes the work EventBridge performs **as the service** after your API call completes, when your credentials are no longer available:
  + `kms:GenerateDataKeyWithoutPlaintext` and `kms:ReEncryptFrom`/`kms:ReEncryptTo`: EventBridge creates the bus's branch key, and creates new branch-key versions on rotation.
  + `kms:Decrypt`: EventBridge unwraps the branch key to deliver events, to load subscriber configuration, and to return decrypted configuration on describe calls.
  + `kms:Decrypt` and `kms:Encrypt`: EventBridge re-wraps the branch key when you change the bus's KMS key.

  This statement uses the same encryption-context condition as `AllowKeyUseThroughEventBridge`. Every request EventBridge makes for a bus, on either access path, carries `aws:events:event-busv2:arn` with the bus ARN, so both statements bind key use to the specific event bus.

**Cross-account keys:** the key can be in a different account than the event bus (for example, a central security account). In that case, put all three statements in that key's policy. The first two statements' `Principal` entries name the bus account's roles. The encryption-context values name the bus account's bus ARN. Cross-account KMS access requires permission on both sides: in addition to the key policy statements above, the bus account's roles need IAM identity policies that allow the same KMS actions on the key's ARN. Access the key by its full key ARN.

#### Creating a new event bus with a Customer Managed KMS Key
<a name="eb-custom-bus-encryption-create"></a>

Specify the key ARN in the `EncryptionConfiguration` parameter of [`CreateEventBus`](https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_CreateEventBus.html):

```
{
  "Name": "my-bus",
  "EncryptionConfiguration": {
    "KmsKeyIdentifier": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
  }
}
```

At creation time, EventBridge validates the key and your access with your credentials (the `DescribeKey` and dry-run checks above). EventBridge then provisions the bus's branch key asynchronously, as the service principal. If the service principal statement is missing from your key policy, the bus transitions to `CREATE_FAILED`, and `DescribeEventBus` returns a `StateReason` naming the KMS access failure.

`DescribeEventBus` on a bus with a customer managed key returns its `EncryptionConfiguration`. A bus using the default AWS owned key returns no `EncryptionConfiguration`: EventBridge never returns the AWS owned key.

#### Changing the encryption configuration on an existing event bus
<a name="eb-custom-bus-encryption-change"></a>

All transitions are supported, via [`UpdateEventBus`](https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_UpdateEventBus.html):
+ AWS owned key → customer managed key
+ Customer managed key → different customer managed key
+ Customer managed key → AWS owned key: send `EncryptionConfiguration` **present and empty** (`"EncryptionConfiguration": {}`). Omitting the member entirely means "leave the encryption configuration unchanged".

When you change the key, the bus enters `UPDATING`. EventBridge re-wraps the branch key under the new key. The bus then returns to `ACTIVE`. The branch key itself does not change, so the material protecting your data does not change. Only the wrapping key changes. Consequences:
+ **Previously written events remain readable** after the transition, regardless of the old key's state. Once the transition completes you can disable the old key immediately without losing access to existing events.
+ New events continue under the same branch key, now protected by the new KMS key.
+ No re-encryption of stored events takes place, so transitions complete quickly and do not depend on how much data the bus holds.

**Automatic KMS key rotation:** if you enable [automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) on your key, KMS rotates the backing material behind the same key ARN. The rotation does not immediately affect the branch key. The branch key stays wrapped by the material that wrapped it last. The next branch-key version, created approximately every 30 days, is protected by the current backing material. So KMS-side rotation takes effect on your bus within roughly a month.

**If your key becomes unavailable** (disabled, deleted, or access removed):
+ Publishing to the bus fails with a KMS access error once the cached branch key expires, within 15 minutes.
+ Event delivery pauses at the same point, for the same reason.
+ Events EventBridge already accepted are not dropped, and decrypt failures are not routed to dead-letter queues. EventBridge retries them. A key-access failure is a condition you can fix, so EventBridge holds and retries the affected events rather than diverting them. No event is lost unless the outage outlasts the bus's retention period.
+ After you restore access, processing resumes automatically, for as long as the events remain within the bus's retention period.

**Deleting your key is permanent.** Disabling a key or removing EventBridge's access is reversible: restore access, and processing resumes. Deleting the key is not. After AWS KMS deletes the key currently configured on a bus, EventBridge can no longer unwrap the bus's branch key, and every event still stored on the bus becomes permanently unreadable for the remainder of its retention period. As a best practice, disable the key first and confirm the impact before you schedule it for deletion. See [Deleting AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html) in the *AWS Key Management Service Developer Guide*.

**Deleting a bus does not require the key.** `DeleteEventBus` succeeds even if the key is disabled or deleted.

#### Scoping down access to the Customer Managed KMS Key
<a name="eb-custom-bus-encryption-scope"></a>
+ **Encryption context.** Every KMS request EventBridge makes for an event bus includes an encryption context binding the request to that bus's ARN. So you can scope each statement to a single bus, as in the example policy. The context key is `aws:events:event-busv2:arn` on every request, whether made with your credentials or as the service principal. Use `StringLike` with a trailing `/*`, because the bus ARN ends in a suffix generated at creation. On an existing bus you can match the exact ARN from `DescribeEventBus` with `StringEquals`.
+ **kms:ViaService.** All requests made with your credentials populate the `kms:ViaService` condition key with `events.{{region}}.amazonaws.com`. So you can restrict your principals' access to key use through EventBridge only.
+ **Propagation of key-policy changes.** Individual event operations use the cached branch key and do not re-validate against your key policy per event. A key-policy change — including removing EventBridge's access — takes effect for a bus's data handling when the cached branch key expires, within 15 minutes.
+ **Confused deputy protection.** Requests EventBridge makes as the service principal include the `aws:SourceArn` context (the bus ARN) and the `aws:SourceAccount` context. So you can add these conditions to the `AllowEventBridgeServicePrincipal` statement. They ensure EventBridge uses your key only on behalf of your own resources:

  ```
  "Condition": {
    "StringEquals": { "aws:SourceAccount": "111122223333" },
    "ArnLike": { "aws:SourceArn": "arn:aws:events:us-east-1:111122223333:event-busv2/my-bus/*" }
  }
  ```

## Monitoring EventBridge Custom Event Bus interaction with AWS KMS
<a name="eb-custom-bus-encryption-cloudtrail"></a>

EventBridge's use of your customer managed key appears in AWS CloudTrail. See [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct). Events to expect:


| CloudTrail `eventName` | When | Calling identity | 
| --- | --- | --- | 
| DescribeKey | Bus create/update key validation | Your principal, via EventBridge | 
| Decrypt, Encrypt, GenerateDataKeyWithoutPlaintext, ReEncrypt (dry run) | Authorization checks on bus create/update, publish, subscriber create/update | Your principal (via EventBridge) | 
| GenerateDataKeyWithoutPlaintext, ReEncrypt | Branch-key creation (bus create) and branch-key rotation (\~30 days) | events.amazonaws.com service principal | 
| Decrypt | Branch-key unwrap on cache expiry: event delivery, subscriber-configuration load, describe-time decryption | events.amazonaws.com service principal | 
| Decrypt \+ Encrypt | Branch-key re-wrap on UpdateEventBus key change | events.amazonaws.com service principal | 

CloudTrail records the `ReEncrypt` API call as one event. The `kms:ReEncryptFrom` and `kms:ReEncryptTo` permissions in your key policy both authorize that call.

The authorization checks are KMS dry-run requests. By design, a dry-run request returns `DryRunOperationException` instead of performing the operation: that response is the trace of a *passing* check, not an error in your configuration. A dry-run entry showing `AccessDeniedException` instead means the caller lacks the permission being checked. For details, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the *AWS Key Management Service Developer Guide*.

The `requestParameters.encryptionContext` of these entries includes `aws:events:event-busv2:arn` with your bus ARN. Entries for branch-key operations also include branch-key metadata added by the Hierarchical Keyring: `branch-key-id` (the bus ARN), `type`, `create-time`, `tablename`, `hierarchy-version`, and `kms-arn`.

Individual event encryption and decryption use data keys derived locally from the cached branch key. So per-event operations do not appear in CloudTrail. You see branch-key operations only.