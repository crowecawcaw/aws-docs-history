# Replicating AWS Payment Cryptography keys

AWS Payment Cryptography supports Multi-Region key replication, allowing you to securely distribute key material and metadata
from any given AWS Payment Cryptography Key to one or more AWS Regions within the same AWS partition and
account.

The source key is known as the [Primary Region key (PRK)](terminology.md#term.prk "terminology.md#term.prk") and
remains the authoritative source for all key management activities while both the PRK
and the [Replica Region keys (RRK)](terminology.md#term.rrk "terminology.md#term.rrk") can be used for cryptographic
operations in their respective AWS Regions.

## Benefits of Multi-Region key replication

The following outlines some benefits of Multi-Region key replication.

- _Easier setup for highly available applications_ - AWS Payment Cryptography
  handles key distribution for you so you can use a key in multiple AWS Regions
  without needing to create decoupled copies of a given key.
- _High availability and low latency keys_ - With Multi-Region key replication, you
  can access your keys in multiple AWS Regions making them highly available,
  resulting in lower latency.
- _Key material durability_ - Replica Region keys are complete key
  replicas and can be used independently of their Primary Region key in cryptographic
  operations. A RRK provides a durable replica in the event of a
  catastrophic data loss of a PRK.

## How Multi-Region key replication works

When Multi-Region key replication is enabled, the AWS Payment Cryptography service uses secure key distribution mechanisms to
copy key material and metadata to the replica AWS Regions you specify. Changes to a
Primary Region key metadata, such as key attributes, state, and enablement, are automatically
replicated to the Replica Region keys.

## Limitations and considerations

The following are some Multi-Region key replication limitations and considerations.

- You must enable this feature for either an AWS Region or specific
  Payment Cryptography keys.
  - If this feature is enabled for an AWS Region, all AWS Payment Cryptography keys
    created after enablement will be replicate to the specified
    AWS Region. Keys created in this Region will become Primary Region keys. Existing
    keys in this Region will not be automatically replicated. You can enable
    Multi-Region key replication for existing keys within an AWS Region at the key level.
  - Each AWS Region can have unique Multi-Region key replication settings.
  - A key's Multi-Region replication settings takes precedence over the AWS Region Multi-Region key replication
    setting.

- A Replica Region key cannot be configured to replicate to other AWS Regions.
- Multi-Region key replication is available for symmetric Payment Cryptography keys like Triple Data
  Encryption Standard (3DES), Advanced Encryption Standard (AES), and Hash-based
  Message Authentication Code (HMAC).
- Asymmetric Payment Cryptography keys do not support Multi-Region key replication.
- Replica Region key are read-only keys. All changes to the Primary Region key will be applied to the
  Replica Region keys.
- Primary Region key changes are eventually consistent with Replica Region keys.
- Payment Cryptography keys can only be replicated with the same AWS partition and
  account.
- Replica Region key count towards your AWS account level AWS Payment Cryptography limit.
- The Primary Region key and Replica Region key use the same key identifier which allows you to reference
  both keys by the same ARN in IAM policies.

## Enabling Multi-Region key replication

There are two ways you can enable Multi-Region key replication for AWS Payment Cryptography keys.

1. **AWS Region**: Multi-Region key replication is applied to all new keys created
   in that AWS Region when enabled. This method provides consistent replication
   for all keys.
2. **Specific AWS Payment Cryptography keys**: You can manage Multi-Region key replication for
   individual keys allowing a more granular level of control.

Once Multi-Region key replication is enabled, your Payment Cryptography keys will replicate to the AWS Regions
you specify.

###### Important

Multi-Region key replication cannot be paused. Your keys are automatically replicated to the
AWS Regions you specify once replication is enabled. Multi-Region key replication can be [disabled](#disabling-mrr "#disabling-mrr") for a specific AWS Region or
Payment Cryptography keys. You must remove the AWS Region as a replication region from
the Primary Region key to delete the Replica Region key.

Alternatively, you can call the [`StopKeyUsage`](../APIReference/API_StopKeyUsage.md "../APIReference/API_StopKeyUsage.md") API or [**stop-key-usage**](../../../cli/latest/reference/payment-cryptography/stop-key-usage.md "../../../cli/latest/reference/payment-cryptography/stop-key-usage.md") CLI command on your PRK to
stop the usage of both the PRK and all associated RRKs. You'll be
unable to use these keys in cryptographic operations. Using
`StopKeyUsage` API or **stop-key-usage** CLI command
will not stop the ongoing Multi-Region key replication enabled for your PRK.

You can check Multi-Region key replication settings for AWS Payment Cryptography keys in a specific AWS Region
by calling the `GetDefaultKeyReplicationRegions` API or
**get-default-key-replication-regions** CLI
command. Keys in the AWS Region where you call this API action or
command will become your [PRK](terminology.md#term.prk "terminology.md#term.prk").

Use the following procedures to enable Multi-Region key replication.

For AWS Region

- Use the following command to enable Multi-Region key replication for an AWS Region you
  specify. In this example, Multi-Region key replication is enabled in US East (Ohio)
  and US West (Oregon). To use this command, replace the `italicized placeholder text` in the example command with your own information.

```
aws payment-cryptography enable-default-key-replication-regions \
    --replication-regions `us-east-2 us-west-2`
```

###### Note

Enabling Multi-Region key replication for an AWS Region will not change the replication
configuration of any existing AWS Payment Cryptography keys. You can enable this
feature for existing keys at the key level. Only keys created after
Multi-Region key replication is enabled for an AWS Region will use the region replication
settings.

For specific AWS Payment Cryptography keys

- Use the following command to enable Multi-Region key replication for specific
  Payment Cryptography keys. In this example, Multi-Region key replication is enabled in
  US East (Ohio). To use this command, replace the `italicized placeholder text` in the example command with your own information.

```
aws payment-cryptography add-key-replication-regions \
    --key-identifier arn:aws:payment-cryptography:`us-east-2`:`111122223333`:key/`kwapwa6qaifllw2h` \
    --replication-regions `us-east-2`
```

Alternatively, you can [create a new
Payment Cryptography key](create-keys.md "create-keys.md") with this feature enabled by including the
replication AWS Regions in your create key request.

###### Note

The key replication settings takes
precedence over the AWS Region replication setting.

## Disabling Multi-Region key replication

If you want to disable Multi-Region key replication, you can call either the
**disable-default-key-replication** or
**remove-key-replication-regions** CLI commands, depending on how
Multi-Region key replication is enabled. You'll need to specify the key's ARN and the AWS Region to disable
Multi-Region key replication.

###### Considerations

Replication region key deletions are eventually consistent.

You can check Multi-Region key replication settings for AWS Payment Cryptography keys in a specific AWS Region
by calling the `GetDefaultKeyReplicationRegions` API or
**get-default-key-replication-regions** CLI
command.

Use the following procedures to disable Multi-Region key replication.

For AWS Region

- Use the following command to disable Multi-Region key replication for an AWS Region
  you specify. In this example, Multi-Region key replication is disabled in
  US East (Ohio). To use this command, replace the `italicized placeholder text` in the example command with your own information.

```
aws payment-cryptography disable-default-key-replication-regions \
    --replication-regions `us-east-2`
```

For specific AWS Payment Cryptography keys

- Use the following command to disable Multi-Region key replication for a specific
  Payment Cryptography key. In this example, Multi-Region key replication is disabling in
  US East (Ohio). To use this command, replace the `italicized placeholder text` in the example command with your own information.

```
aws payment-cryptography remove-key-replication-regions \
    --key-identifier arn:aws:payment-cryptography:`us-east-2`:`111122223333`:key/`kwapwa6qaifllw2h` \
    --replication-regions `us-east-2`
```

## Security considerations

The following are security considerations when using Multi-Region key replication for your Payment Cryptography
keys. For more information, see [Security best practices for AWS Payment Cryptography](security-best-practices.md "security-best-practices.md").

- Limit sharing key materials.
- Follow the principal of least privileges permissions when creating IAM
  policies.
- You can't make changes to the Replica Region key as it is a read-only key.

## Best practices

The following are some best practices when using Multi-Region key replication with AWS Payment Cryptography keys.

- Ensure your application continues to work even if the Multi-Region key replication to the specified
  AWS Region is not immediate. If you need to know when Multi-Region key replication is complete, you
  can monitor with the [GetKey](../APIReference/API_GetKey.md "../APIReference/API_GetKey.md") API action. You can monitor key replication events with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").
- Test and implement automated deployment processes in case of fail-over from
  one AWS Region to another Region.

## Pricing

You're charged for Replica Region keys you create with AWS Payment Cryptography. These keys are charged per
AWS Region. For the latest Payment Cryptography pricing information, see the [AWS Payment Cryptography pricing
page](https://aws.amazon.com/payment-cryptography/pricing/ "https://aws.amazon.com/payment-cryptography/pricing/").
