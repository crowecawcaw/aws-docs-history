# KMS keys in a CloudHSM key store

You can create, view, manage, use, and schedule deletion of the AWS KMS keys in an
AWS CloudHSM key store. The procedures that you use are very similar to those you use for other
KMS keys. The only difference is that you specify an AWS CloudHSM key store when you create the
KMS key. Then, AWS KMS creates non-extractable key material for the KMS key in the AWS CloudHSM
cluster that is associated with the AWS CloudHSM key store. When you use a KMS key in an AWS CloudHSM key
store, the [cryptographic operations](#use-cmk-keystore "#use-cmk-keystore") are performed in the
HSMs in the cluster.

**Supported features**

In addition to the procedures discussed in this section, you can do the following with
KMS keys in an AWS CloudHSM key store:

- Use key policies, IAM policies, and grants to [authorize access](control-access.md "control-access.md") to the KMS keys.
- [Enable and disable](enabling-keys.md "enabling-keys.md") the KMS keys.
- Assign [tags](tagging-keys.md "tagging-keys.md") and create [aliases](kms-alias.md "kms-alias.md"), and use attribute-based access control
  (ABAC) to authorize access to the KMS keys.
- Use the KMS keys to perform the following cryptographic operations:

      + [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md")
      + [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md")
      + [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md")
      + [GenerateDataKeyWithoutPlaintext](../APIReference/API_GenerateDataKeyWithoutPlaintext.md "../APIReference/API_GenerateDataKeyWithoutPlaintext.md")
      + [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md")

  The operations that generate asymmetric data key pairs, [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md") and [GenerateDataKeyPairWithoutPlaintext](../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md "../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md"), are _not_
  supported in custom key stores.

- Use the KMS keys with [AWS services that
  integrate with AWS KMS](service-integration.md "service-integration.md") and support customer managed keys.
- Track use of your KMS keys in [AWS CloudTrail
  logs](logging-using-cloudtrail.md "logging-using-cloudtrail.md") and [Amazon CloudWatch monitoring
  tools](monitoring-overview.md "monitoring-overview.md").

**Unsupported features**

- AWS CloudHSM key stores support only symmetric encryption KMS keys. You cannot create HMAC
  KMS keys, asymmetric KMS keys, or asymmetric data key pairs in an AWS CloudHSM key store.
- You cannot [import key material](importing-keys.md "importing-keys.md") into a KMS key in
  an AWS CloudHSM key store. AWS KMS generates the key material for the KMS key in the AWS CloudHSM
  cluster.
- You cannot enable or disable [automatic rotation](rotate-keys.md "rotate-keys.md") of
  the key material for a KMS key in an AWS CloudHSM key store.

**Using KMS keys in an AWS CloudHSM key store**

When you use your KMS key in a request, identify the KMS key by its ID or alias; you do
not need to specify the AWS CloudHSM key store or AWS CloudHSM cluster. The response includes the same fields
that are returned for any symmetric encryption KMS key.

However, when you use a KMS key in an AWS CloudHSM key store, the cryptographic operation is
performed entirely within the AWS CloudHSM cluster that is associated with the AWS CloudHSM key store. The
operation uses the key material in the cluster that is associated with the KMS key that you
chose.

To make this possible, the following conditions are required.

- The [key state](key-state.md "key-state.md") of the KMS key must be
  `Enabled`. To find the key state, use the **Status** field
  in the [AWS KMS console](finding-keys.md#viewing-console-details "finding-keys.md#viewing-console-details") or the `KeyState`
  field in the [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md")
  response.
- The AWS CloudHSM key store must be connected to its AWS CloudHSM cluster. Its
  **Status** in the [AWS KMS console](view-keystore.md "view-keystore.md") or
  `ConnectionState` in the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
  response must be `CONNECTED`.
- The AWS CloudHSM cluster that is associated with the custom key store must contain at least
  one active HSM. To find the number of active HSMs in the cluster, use the [AWS KMS console](view-keystore.md "view-keystore.md"), the AWS CloudHSM console, or the [DescribeClusters](../../../cloudhsm/latest/APIReference/API_DescribeClusters.md "../../../cloudhsm/latest/APIReference/API_DescribeClusters.md") operation.
- The AWS CloudHSM cluster must contain the key material for the KMS key. If the key material was
  deleted from the cluster, or an HSM was created from a backup that did not include the
  key material, the cryptographic operation will fail.

If these conditions are not met, the cryptographic operation fails, and AWS KMS returns a
`KMSInvalidStateException` exception. Typically, you just need to [reconnect the AWS CloudHSM key store](connect-keystore.md "connect-keystore.md"). For additional help, see
[How to fix a failing KMS key](fix-keystore.md#fix-cmk-failed "fix-keystore.md#fix-cmk-failed").

When using the KMS keys in an AWS CloudHSM key store, be aware that the KMS keys in each AWS CloudHSM
key store share a [custom key store request quota](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores") for
cryptographic operations. If you exceed the quota, AWS KMS returns a
`ThrottlingException`. If the AWS CloudHSM cluster that is associated with the AWS CloudHSM key
store is processing numerous commands, including those unrelated to the AWS CloudHSM key store, you
might get a `ThrottlingException` at an even lower rate. If you get a
`ThrottlingException` for any request, lower your request rate and try the commands
again. For details about the custom key store request quota, see [Custom key store request quotas](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores").

**Learn more**

- To learn more about AWS CloudHSM key stores, see [AWS CloudHSM key stores](keystore-cloudhsm.md "keystore-cloudhsm.md").
- To create KMS keys in an AWS CloudHSM key store, see [Create a KMS key in an AWS CloudHSM key store](create-cmk-keystore.md "create-cmk-keystore.md").
- To identify and view KMS keys in an AWS CloudHSM key store, see [Identify KMS keys in AWS CloudHSM key stores](identify-key-types.md#identify-key-hsm-keystore "identify-key-types.md#identify-key-hsm-keystore").
- To find KMS keys and key material in an AWS CloudHSM key store, see [Find KMS keys and key material in an AWS CloudHSM key
  store](find-key-material.md "find-key-material.md").
- To learn about special considerations for deleting KMS keys in an AWS CloudHSM key store, see
  [Deleting KMS keys from an AWS CloudHSM key store](deleting-keys.md#delete-cmk-keystore "deleting-keys.md#delete-cmk-keystore").
