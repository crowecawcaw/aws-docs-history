# Disconnect an AWS CloudHSM key store

When you disconnect an AWS CloudHSM key store, AWS KMS logs out of the AWS CloudHSM client, disconnects
from the associated AWS CloudHSM cluster, and removes the network infrastructure that it created to
support the connection.

While an AWS CloudHSM key store is disconnected, you can manage the AWS CloudHSM key store and its
KMS keys, but you cannot create or use KMS keys in the AWS CloudHSM key store. The connection
state of the key store is `DISCONNECTED` and the [key
state](key-state.md "key-state.md") of KMS keys in the custom key store is `Unavailable`, unless
they are `PendingDeletion`. You can reconnect the AWS CloudHSM key
store at any time.

###### Note

AWS CloudHSM key stores have a `DISCONNECTED` connection state only when the key store has never been connected or you explicitly disconnect it. If your AWS CloudHSM key store connection state
is `CONNECTED` but you are having trouble using it, make sure that its
associated AWS CloudHSM cluster is active and contains at least one active HSMs. For help with
connection failures, see [Troubleshooting a custom key store](fix-keystore.md "fix-keystore.md").

When you disconnect a custom key store, the KMS keys in the key store become unusable
right away (subject to eventual consistency). However, resources encrypted with [data keys](data-keys.md "data-keys.md") protected by the KMS key are not affected until
the KMS key is used again, such as to decrypt the data key. This issue affects
AWS services, many of which use data keys to protect your resources. For details, see
[How unusable KMS keys affect data keys](unusable-kms-keys.md "unusable-kms-keys.md").

###### Note

While a custom key store is disconnected, all attempts to create KMS keys in the custom key store or to use existing KMS keys in cryptographic operations will
fail. This action can prevent users from storing and accessing sensitive data.

To better estimate the effect of disconnecting your custom key store, [identify the KMS keys](find-cmk-in-keystore.md "find-cmk-in-keystore.md") in the custom key store
and [determine their past use](deleting-keys-determining-usage.md "deleting-keys-determining-usage.md").

You might disconnect an AWS CloudHSM key store for reasons such as the following:

- **To rotate of the `kmsuser` password.**
  AWS KMS changes the `kmsuser` password each time that it connects to the
  AWS CloudHSM cluster. To force a password rotation, just disconnect and reconnect.
- **To audit the key material** for the KMS keys in
  the AWS CloudHSM cluster. When you disconnect the custom key store, AWS KMS logs out of the
  [kmsuser crypto user](keystore-cloudhsm.md#concept-kmsuser "keystore-cloudhsm.md#concept-kmsuser") account
  in the AWS CloudHSM client. This allows you to log into the cluster as the
  `kmsuser` CU and audit and manage the key material for the
  KMS key.
- **To immediately disable all KMS keys** in the
  AWS CloudHSM key store. You can [disable and re-enable
  KMS keys](enabling-keys.md "enabling-keys.md") in an AWS CloudHSM key store by using the AWS Management Console or the [DisableKey](../APIReference/API_DisableKey.md "../APIReference/API_DisableKey.md") operation. These
  operations complete quickly, but they act on one KMS key at a time. Disconnecting
  the AWS CloudHSM key store immediately changes the key state of all KMS keys in the AWS CloudHSM
  key store to `Unavailable`, which prevents them from being used in any
  cryptographic operation.
- **To repair a failed connection attempt**. If an
  attempt to connect an AWS CloudHSM key store fails (the connection state of the custom key
  store is `FAILED`), you must disconnect the AWS CloudHSM key store before you
  try to connect it again.

## Disconnect your AWS CloudHSM key store

You can disconnect your AWS CloudHSM key store in the AWS KMS console or by using the [DisconnectCustomKeyStore](../APIReference/API_DisconnectCustomKeyStore.md "../APIReference/API_DisconnectCustomKeyStore.md") operation.

To disconnect a connected AWS CloudHSM key store in the AWS KMS console, begin by
choosing the AWS CloudHSM key store from the **Custom Key Stores**
page.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Custom key stores**, **AWS CloudHSM key stores**.
4. Choose the row of the external key store you want to disconnect.
5. From the **Key store actions** menu, choose
   **Disconnect**.
   When the operation completes, the connection state changes from
   **Disconnecting** to **Disconnected**. If
   the operation fails, an error message appears that describes the problem and
   provides help on how to fix it. If you need more help, see [Troubleshooting a custom key store](fix-keystore.md "fix-keystore.md").

To disconnect a connected AWS CloudHSM key store, use the [DisconnectCustomKeyStore](../APIReference/API_DisconnectCustomKeyStore.md "../APIReference/API_DisconnectCustomKeyStore.md") operation. If the operation is successful, AWS KMS returns an HTTP 200 response and a JSON
object with no properties.

The examples in this section use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

This example disconnects an AWS CloudHSM key store. Before running this example,
replace the example ID with a valid one.

```
`$` `aws kms disconnect-custom-key-store --custom-key-store-id `cks-1234567890abcdef0``
```

To verify that the AWS CloudHSM key store is disconnected, use the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md") operation. By default, this operation
returns all custom keys stores in your account and Region. But you can use
either the `CustomKeyStoreId` and `CustomKeyStoreName`
parameter (but not both) to limit the response to particular custom key stores.
The `ConnectionState` value of `DISCONNECTED` indicates
that this example AWS CloudHSM key store is not connected to its AWS CloudHSM cluster.

```
`$` `aws kms describe-custom-key-stores --custom-key-store-id `cks-1234567890abcdef0``
`{
 "CustomKeyStores": [
 "CloudHsmClusterId": "cluster-1a23b4cdefg",
 **"ConnectionState": "DISCONNECTED"**,
 "CreationDate": "1.499288695918E9",
 "CustomKeyStoreId": "cks-1234567890abcdef0",
 "CustomKeyStoreName": "ExampleKeyStore",
 "CustomKeyStoreType": "AWS_CLOUDHSM",
 "TrustAnchorCertificate": "`<certificate string appears here>`"
 ],
}`
```
