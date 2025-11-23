# KMS keys in external key

stores

To create, view, manage, use, and schedule deletion of the KMS keys in an external key
store, you use procedures that are very similar to those you use for other KMS keys.
However, when you create a KMS key in an external key store, you specify an [external key store](keystore-external.md#concept-external-key-store "keystore-external.md#concept-external-key-store") and an [external key](keystore-external.md#concept-external-key "keystore-external.md#concept-external-key"). When you use a KMS key in an
external key store, [encryption and decryption
operations](keystore-external.md#xks-how-it-works "keystore-external.md#xks-how-it-works") are performed by your external key manager using the specified
external key.

AWS KMS cannot create, view, update, or delete any cryptographic keys in your
external key manager. AWS KMS never directly accesses your external key manager or any
external key. All requests for cryptographic operations are mediated by your [external key store proxy](keystore-external.md#concept-xks-proxy "keystore-external.md#concept-xks-proxy"). To use a KMS key in an
external key store, the external key store that hosts the KMS key must be [connected](xks-connect-disconnect.md "xks-connect-disconnect.md") to its external key store
proxy.

**Supported features**

In addition to the procedures discussed in this section, you can do the following with KMS
keys in an external key store:

- Use [key policies](key-policies.md "key-policies.md"), [IAM policies](iam-policies.md "iam-policies.md"), and [grants](grants.md "grants.md") to control access
  to the KMS keys.
- [Enable and disable](enabling-keys.md "enabling-keys.md") the KMS keys. These
  actions do not affect the external key in your external key manager.
- Assign [tags](tagging-keys.md "tagging-keys.md") and create [aliases](kms-alias.md "kms-alias.md"), and use [attribute-based
  access control](abac.md "abac.md") (ABAC) to authorize access to the KMS keys.
- Use the KMS keys to perform the following cryptographic operations:

      + [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md")
      + [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md")
      + [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md")
      + [GenerateDataKeyWithoutPlaintext](../APIReference/API_GenerateDataKeyWithoutPlaintext.md "../APIReference/API_GenerateDataKeyWithoutPlaintext.md")
      + [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md")

  The operations that generate asymmetric data key pairs, [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md") and [GenerateDataKeyPairWithoutPlaintext](../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md "../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md"), are _not_
  supported in custom key stores.

- Use the KMS keys with [AWS services that integrate with AWS KMS](https://aws.amazon.com/kms/features/#AWS_Service_Integration "https://aws.amazon.com/kms/features/#AWS_Service_Integration") and support [customer managed keys](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key").

**Unsupported features**

- External key stores support only [symmetric
  encryption KMS keys](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks"). You cannot create HMAC KMS keys or asymmetric
  KMS keys in an external key store.
- [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md")
  and [GenerateDataKeyPairWithoutPlaintext](../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md "../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md") are not supported on KMS keys in
  an external key store.
- You cannot use an [AWS::KMS::Key
  CloudFormation template](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.md") to create an external key store or a KMS key in an external
  key store.
- [Multi-Region keys](multi-region-keys-overview.md "multi-region-keys-overview.md") are not
  supported in an external key store.
- KMS keys with [imported key material](importing-keys.md "importing-keys.md") are
  not supported in an external key store.
- [Automatic key rotation](rotate-keys.md "rotate-keys.md") is not supported for
  KMS keys in an external key store.

**Using KMS keys in an external key store**

When you use your KMS key in a request, identify the KMS key by its [key ID, key ARN, alias, or alias ARN](concepts.md#key-id "concepts.md#key-id"). You do not need to specify
the external key store. The response includes the same fields that are returned for any
symmetric encryption KMS key. However, when you use a KMS key in an external key store,
encryption and decryption operations are performed by your external key manager using the external
key that is associated with the KMS key.

To ensure that ciphertext encrypted by a KMS key in an external key store is at least as
secure as any ciphertext encrypted by a standard KMS key, AWS KMS uses [double encryption](keystore-external.md#concept-double-encryption "keystore-external.md#concept-double-encryption"). Data is first encrypted in
AWS KMS using AWS KMS key material. Then it is encrypted by your external key manager using the
external key for the KMS key. To decrypt double-encrypted ciphertext, the ciphertext is
first decrypted by your external key manager using the external key for the KMS key. Then
it is decrypted in AWS KMS using the AWS KMS key material for the KMS key.

To make this possible, the following conditions are required.

- The [key state](key-state.md "key-state.md") of the KMS key must be
  `Enabled`. To find the key state, see the **Status**
  field for customer managed keys the [AWS KMS
  console](finding-keys.md#viewing-console-details "finding-keys.md#viewing-console-details") or the `KeyState` field in the [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") response.
- The external key store that hosts the KMS key must be connected to its [external key store proxy](keystore-external.md#concept-xks-proxy "keystore-external.md#concept-xks-proxy"), that is, the [connection state](xks-connect-disconnect.md#xks-connection-state "xks-connect-disconnect.md#xks-connection-state") of the external key store
  must be `CONNECTED`.

You can view the connection state on the **External key stores**
page in the AWS KMS console or in the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md") response. The connection state of the external
key store is also displayed on the detail page for the KMS key in the AWS KMS
console. On the detail page, choose the **Cryptographic
configuration** tab and see the **Connection state**
field in the **Custom key store** section.

If the connection state is `DISCONNECTED`, you must first connect it.
If the connection state is `FAILED`, you must resolve the problem,
disconnect the external key store, and then connect it. For instructions, see [Connect and disconnect external key
stores](xks-connect-disconnect.md "xks-connect-disconnect.md").

- The external key store proxy must be able to find the external key.
- The external key must be enabled and it must perform encryption and decryption.

The status of the external key is independent of and not affected by changes in
the [key state](key-state.md "key-state.md") of the KMS key, including enabling
and disabling the KMS key. Similarly, disabling or deleting the external key
doesn't change the key state of the KMS key, but cryptographic operations using
the associated KMS key will fail.

If these conditions are not met, the cryptographic operation fails, and AWS KMS returns a
`KMSInvalidStateException` exception. You might need to [reconnect the external key store](xks-connect-disconnect.md "xks-connect-disconnect.md") or use your
external key manager tools to reconfigure or repair your external key. For additional help,
see [Troubleshooting external key stores](xks-troubleshooting.md "xks-troubleshooting.md").

When using the KMS keys in an external key store, be aware that the KMS keys in each
external key store share a [custom key store request
quota](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores") for cryptographic operations. If you exceed the quota, AWS KMS returns a
`ThrottlingException`. For details about the custom key store request quota,
see [Custom key store request quotas](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores").

**Learn more**

- To learn more about external key stores, see [External key stores](keystore-external.md "keystore-external.md").
- To learn more about key material in external key stores, see [External key](keystore-external.md#concept-external-key "keystore-external.md#concept-external-key").
- To create KMS keys in an external key store, see [Create a KMS key in external key stores](create-xks-keys.md "create-xks-keys.md").
- To identify and view KMS keys in an external key store, see [Identify KMS keys in external key stores](identify-key-types.md#view-xks-key "identify-key-types.md#view-xks-key").
- To learn about special considerations for deleting KMS keys in an external key store, see
  [Deleting KMS keys from an external key store](deleting-keys.md#delete-xks-key "deleting-keys.md#delete-xks-key").
