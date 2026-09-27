

# Encrypting events on a Custom Event Bus
<a name="eb-custom-bus-encryption"></a>

A bus encrypts everything it stores: event payloads, event metadata, subscriber filters, and subscriber target configuration. By default it uses a key that AWS owns, and you configure nothing. To encrypt a bus with your own AWS KMS key instead, set `EncryptionConfiguration.KmsKeyIdentifier` when you create or update the bus, for example `aws eventsv2 create-event-bus --name orders --encryption-configuration KmsKeyIdentifier=arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`, and add the three statements in [Writing the key policy](#eb-custom-bus-encryption-key-policy) to the key policy.

## Choosing the key that encrypts a bus
<a name="eb-custom-bus-encryption-at-rest"></a>

Omit `EncryptionConfiguration` and EventBridge encrypts the bus with 256-bit AES under an AWS owned key. You cannot view or manage that key, its use does not appear in your CloudTrail logs, it costs nothing, it does not count against your AWS KMS quotas, and AWS rotates it monthly. `DescribeEventBus` returns no `EncryptionConfiguration` for such a bus. For more information, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the *AWS KMS Developer Guide*.

Set `EncryptionConfiguration.KmsKeyIdentifier` and EventBridge encrypts the bus with your customer managed key. You then control the key policy, rotation, disabling, and deletion, and you see every use of the key in CloudTrail. The key incurs the AWS KMS monthly key fee and request charges. Because EventBridge encrypts and decrypts events locally under a cached branch key (see [How the bus uses your key](#eb-custom-bus-encryption-branch-key)), it makes a few AWS KMS requests per bus per cache window plus rotation; the request count does not grow with your event volume. For more information, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/).

`KmsKeyIdentifier` accepts a key ID, a key ARN, an alias name such as `alias/orders`, or an alias ARN. EventBridge qualifies a bare key ID or alias name in your account and Region, so a key in another account must be named by its full key ARN. An alias is resolved to its key when you create or update the bus, and the create and describe responses return that key ARN. Re-pointing the alias later does not change the key a bus uses. The key must be a symmetric encryption key (`SYMMETRIC_DEFAULT`, key usage `ENCRYPT_DECRYPT`); EventBridge rejects asymmetric and HMAC keys. A multi-Region key works as an ordinary key: name the replica in the bus's Region, because EventBridge replicates neither your data nor your key material across Regions. Keys with imported key material and keys in an external key store are supported.

```
aws eventsv2 create-event-bus \
    --name orders \
    --encryption-configuration KmsKeyIdentifier=arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
```

Your key encrypts the event payloads and metadata that the bus retains, the copies held for each subscriber during delivery, and the subscriber filters and target configuration. Four things are not encrypted with your key, because EventBridge needs them to route and look up events: the bus name, ARN, and account ID; the event group ID that orders FIFO delivery, so do not put sensitive data in it; the deduplication ID, which EventBridge stores as a one-way hash; and internal match results and sequence numbers. The storage services encrypt those at rest with their own keys.

## How the bus uses your key
<a name="eb-custom-bus-encryption-branch-key"></a>

When you configure a customer managed key, EventBridge creates a *branch key* for the bus: an intermediate key, stored in a service-managed table and wrapped by your AWS KMS key, following the AWS Encryption SDK [Hierarchical Keyring](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-hierarchical-keyring.html). EventBridge derives a data key from the branch key for each event, so it encrypts and decrypts events locally without a AWS KMS call per event.
+ When you publish an event, EventBridge encrypts it under the bus's branch key before writing it to storage.
+ When EventBridge delivers an event, it decrypts the event to evaluate filters and to deliver it. The target receives the decrypted event; encryption at the target is the target service's responsibility.
+ EventBridge caches the branch key in memory for up to 15 minutes. When the cache expires, it calls `kms:Decrypt` on your key to unwrap the branch key again.
+ EventBridge creates a new branch key version about every 30 days and keeps the older versions, so events written earlier stay readable for the bus's retention period.

EventBridge reaches your key on two paths, and the key policy must allow both. For the checks it runs while your API call is in progress, it uses your credentials, forwarded from the call. For the work it does after the call returns, such as delivering events and managing the branch key, it acts as the `events.amazonaws.com` service principal, because your credentials are no longer available.

## Writing the key policy
<a name="eb-custom-bus-encryption-key-policy"></a>

Add three statements to the key policy: one that lets your principals validate the key, one that lets them pass the access checks EventBridge runs with their credentials, and one for the `events.amazonaws.com` service principal. Every AWS KMS request EventBridge makes for a bus carries the encryption context key `aws:events:event-busv2:arn` with the bus ARN, on both access paths, so the second and third statements are scoped to one bus. A bus ARN ends in a suffix that EventBridge generates at creation, so match it with `StringLike` and a trailing `/*`. Keep your own key administration statements in the policy as well. Replace the account, Region, role, and bus name in the following example.

```
{
    "Version": "2012-10-17",
    "Id": "eventbridge-custom-event-bus-key-policy",
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
                    "kms:EncryptionContext:aws:events:event-busv2:arn": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/*"
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
                    "kms:EncryptionContext:aws:events:event-busv2:arn": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/*"
                }
            }
        }
    ]
}
```

`AllowKeyValidationThroughEventBridge` lets your principals validate the key when they create or update a bus. EventBridge calls `kms:DescribeKey` with your credentials to confirm that the key exists, is symmetric, and is enabled. `DescribeKey` takes no encryption context, so this statement has none; `kms:ViaService` limits it to requests that come through EventBridge.

`AllowKeyUseThroughEventBridge` authorizes the access checks that EventBridge runs with your credentials before it accepts a key configuration and before it writes or reads encrypted data for you, so that you cannot configure a key that the service's later, asynchronous work cannot use. The checks are AWS KMS dry runs: they authorize but encrypt and decrypt nothing. They are billed as standard AWS KMS requests and count against your AWS KMS request quotas; see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the *AWS KMS Developer Guide*. Each operation checks the actions that its later work performs:
+ `CreateEventBus` with a customer managed key checks `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptFrom`, `kms:ReEncryptTo`, and `kms:Decrypt`, the actions that branch key creation and later reads perform.
+ `UpdateEventBus` that changes the key checks `kms:Decrypt` on the current key, and `kms:Encrypt` and `kms:Decrypt` on the new key.
+ `PutEvents` and `PutRawEvents` on a bus with a customer managed key check `kms:Decrypt`. A producer that cannot read the bus's events back cannot write them either. Without it, the publish call fails with `AccessDeniedException` naming `KMS_ACCESS_DENIED`.
+ `CreateSubscriber` and `UpdateSubscriber` check `kms:Decrypt`, because subscriber configuration is encrypted under the bus key.

So the `Principal` of this statement must cover every role that creates or updates the bus, publishes to it, or creates subscribers on it. List the role ARNs, or name the account root principal to delegate the decision to the IAM policies in your account.

`AllowEventBridgeServicePrincipal` authorizes the work EventBridge performs as the service after your call completes. `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptFrom`, and `kms:ReEncryptTo` create the bus's branch key and its new versions on rotation. `kms:Decrypt` unwraps the branch key to deliver events, to load subscriber configuration, and to return decrypted configuration on describe calls. `kms:Decrypt` with `kms:Encrypt` re-wraps the branch key when you change the bus's key.

The key can live in another account, for example a central security account. Put all three statements in that key's policy, with the bus account's roles as the principals of the first two and the bus account's bus ARN in the encryption context values. The bus account's roles also need IAM identity policies that allow the same AWS KMS actions on the key ARN, because cross-account AWS KMS access requires permission on both sides. Name the key by its full key ARN.

## Scoping the key policy to one bus
<a name="eb-custom-bus-encryption-scope"></a>

To limit a statement to one bus, condition it on `kms:EncryptionContext:aws:events:event-busv2:arn`. Before the bus exists, use `StringLike` with a trailing `/*`, as in the preceding policy. For an existing bus, you can match the exact ARN that `DescribeEventBus` returns with `StringEquals`. Every request made with your credentials also populates `kms:ViaService` with `events.{{region}}.amazonaws.com`, so you can restrict your principals to using the key through EventBridge only.

Requests that EventBridge makes as the service principal carry `aws:SourceArn` with the bus ARN and `aws:SourceAccount` with the bus account. Add them to `AllowEventBridgeServicePrincipal` so that EventBridge can use your key only for your own buses.

```
"Condition": {
    "StringEquals": { "aws:SourceAccount": "111122223333" },
    "ArnLike": { "aws:SourceArn": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/*" }
}
```

Individual publish and delivery operations use the cached branch key and do not re-check the key policy per event. A key policy change, including one that removes EventBridge's access, takes effect on a bus's data handling when the cached branch key expires, within 15 minutes.

## Changing or removing the key on a bus
<a name="eb-custom-bus-encryption-change"></a>

Call `UpdateEventBus` to move a bus from the AWS owned key to a customer managed key, from one customer managed key to another, or back to the AWS owned key. To return to the AWS owned key, send `EncryptionConfiguration` present and empty, as `--encryption-configuration '{}'`. Omit `EncryptionConfiguration` entirely and the bus keeps its current key.

The bus enters `UPDATING` while EventBridge re-wraps the branch key under the new key, then returns to `ACTIVE`. The branch key itself does not change, so EventBridge re-encrypts no stored events, the change completes quickly whatever the bus holds, and previously written events stay readable whatever the state of the old key. Once `DescribeEventBus` shows the bus `ACTIVE` with the new key, you can disable the old key.

If EventBridge cannot use the new key, the bus settles in `UPDATE_FAILED` and keeps working with its previous key: it still accepts and delivers events, and `DescribeEventBus` keeps reporting the old key. The failed key never becomes the bus key. Call `UpdateEventBus` again with a usable key, or the same key after you fix its policy, and the bus returns to `ACTIVE`. A bus whose creation fails on the key settles in `CREATE_FAILED` with a `StateReason` naming the AWS KMS denial; that state accepts only `DeleteEventBus`, and `UpdateEventBus` is rejected with a message naming the states it does accept, `[ACTIVE, UPDATE_FAILED]`. Fix the key policy, delete the bus, and create it again. For the states, see [Bus states and what each allows](eb-custom-bus-create.md#eb-custom-bus-lifecycle-states).

If you enable [automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) on your key, AWS KMS rotates the backing material behind the same key ARN. The branch key stays wrapped by the material that wrapped it last, and the next branch key version, created about every 30 days, uses the current material. So a AWS KMS rotation reaches your bus within roughly a month.

## When the key becomes unusable
<a name="eb-custom-bus-encryption-key-unusable"></a>

If you disable the key, schedule it for deletion, or remove EventBridge's access to it, the bus keeps working until its cached branch key expires, within 15 minutes. Then publishing to the bus fails with a AWS KMS access error, and delivery pauses. EventBridge does not drop the events it has already accepted and does not send them to dead-letter queues; it holds and retries them, because a key access failure is a condition you can fix. When you restore access, publishing and delivery resume on their own. No event is lost unless the outage outlasts the bus's retention period.

Deleting the key is permanent. After AWS KMS deletes the key configured on a bus, EventBridge can no longer unwrap the bus's branch key, and every event still stored on the bus is unreadable for the rest of its retention period. Disable the key first, confirm the effect, and only then schedule deletion; see [Deleting AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html) in the *AWS KMS Developer Guide*. `DeleteEventBus` does not need the key: it succeeds when the key is disabled or deleted.

## Monitoring key use in CloudTrail
<a name="eb-custom-bus-encryption-cloudtrail"></a>

Every request EventBridge makes to your customer managed key is recorded in CloudTrail; see [Logging AWS KMS API calls with CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html). The following table lists the events to expect.


| `eventName` | When | Calling identity | 
| --- | --- | --- | 
| DescribeKey | Key validation on bus create and update | Your principal, through EventBridge | 
| Decrypt, Encrypt, GenerateDataKeyWithoutPlaintext, ReEncrypt (dry run) | Access checks on bus create and update, publish, and subscriber create and update | Your principal, through EventBridge | 
| GenerateDataKeyWithoutPlaintext, ReEncrypt | Branch key creation at bus create, and branch key rotation about every 30 days | events.amazonaws.com | 
| Decrypt | Branch key unwrap when the cache expires: event delivery, subscriber configuration load, describe calls | events.amazonaws.com | 
| Decrypt and Encrypt | Branch key re-wrap when UpdateEventBus changes the key | events.amazonaws.com | 

CloudTrail records a `ReEncrypt` call as one event; the `kms:ReEncryptFrom` and `kms:ReEncryptTo` permissions both authorize it. A dry-run entry that shows `DryRunOperationException` is a passing access check, not a fault in your configuration; one that shows `AccessDeniedException` means the caller lacks the permission being checked. The `requestParameters.encryptionContext` of every entry includes `aws:events:event-busv2:arn` with your bus ARN. Branch key entries also carry the Hierarchical Keyring's fields: `branch-key-id` (the bus ARN), `type`, `create-time`, `tablename`, `hierarchy-version`, and `kms-arn`. Per-event encryption and decryption use data keys derived locally from the cached branch key, so individual events do not appear in CloudTrail.

## Encryption in transit
<a name="eb-custom-bus-encryption-transit"></a>

All Custom Event Bus API calls go to an HTTPS endpoint, `eventsv2.{{region}}.amazonaws.com`, and every request must be signed with your credentials. A FIPS endpoint, `eventsv2-fips.{{region}}.amazonaws.com`, is available where you need it. For EventBridge data protection in general, see [Amazon EventBridge security](eb-security.md).