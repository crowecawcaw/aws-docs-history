# Edit AWS CloudHSM key store settings

You can change the settings of an existing AWS CloudHSM key store. The custom key store must be
disconnected its AWS CloudHSM cluster.

To edit AWS CloudHSM key store settings:

1. [Disconnect the custom key store](disconnect-keystore.md "disconnect-keystore.md") from its
   AWS CloudHSM cluster.

While the custom key store is disconnected, you cannot create AWS KMS keys (KMS keys) in the custom key store and you
cannot use the KMS keys it contains for [cryptographic
operations](manage-cmk-keystore.md#use-cmk-keystore "manage-cmk-keystore.md#use-cmk-keystore"). 2. Edit one or more of the AWS CloudHSM key store settings.

You can edit the following settings in a custom key store:

The friendly name of the custom key store.

Enter a new friendly name. The new name must be unique among all custom key stores in
your AWS account.

###### Important

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

The cluster ID of the associated AWS CloudHSM cluster.

Edit this value to substitute a related AWS CloudHSM cluster for the original one. You
can use this feature to repair a custom key store if its AWS CloudHSM cluster becomes
corrupted or is deleted.

Specify an AWS CloudHSM cluster that shares a backup history with the original cluster
and [fulfills the requirements](create-keystore.md#before-keystore "create-keystore.md#before-keystore") for association
with a custom key store, including two active HSMs in different Availability Zones.
Clusters that share a backup history have the same cluster certificate. To view the
cluster certificate of a cluster, use the [DescribeClusters](../../../cloudhsm/latest/APIReference/API_DescribeClusters.md "../../../cloudhsm/latest/APIReference/API_DescribeClusters.md") operation. You
cannot use the edit feature to associate the custom key store with an unrelated AWS CloudHSM
cluster.

The current password of the [kmsuser
crypto user](keystore-cloudhsm.md#concept-kmsuser "keystore-cloudhsm.md#concept-kmsuser") (CU).

Tells AWS KMS the current password of the `kmsuser` CU in the AWS CloudHSM
cluster. This action does not change the password of the `kmsuser` CU in
the AWS CloudHSM cluster.

If you change the password of the `kmsuser` CU in the AWS CloudHSM cluster,
use this feature to tell AWS KMS the new `kmsuser` password. Otherwise, AWS KMS
cannot log into the cluster and all attempts to connect the custom key store to the
cluster fail. 3. [Reconnect the custom key store](connect-keystore.md "connect-keystore.md") to its
AWS CloudHSM cluster.

## Edit your key store settings

You can edit your AWS CloudHSM key store settings in the AWS KMS console or by using the [UpdateCustomKeyStore](../APIReference/API_UpdateCustomKeyStore.md "../APIReference/API_UpdateCustomKeyStore.md") operation.

When you edit an AWS CloudHSM key store, you can change any or of the configurable values.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Custom key stores**, **AWS CloudHSM key stores**.
4. Choose the row of the AWS CloudHSM key store you want to edit.

If the value in the **Connection state** column is not
**Disconnected**, you must disconnect the custom key store before you
can edit it. (From the **Key store actions** menu, choose
**Disconnect**.)

While an AWS CloudHSM key store is disconnected, you can manage the AWS CloudHSM key store and its
KMS keys, but you cannot create or use KMS keys in the AWS CloudHSM key store. 5. From the **Key store actions** menu, choose
**Edit**. 6. Do one or more of the following actions.

    * Type a new friendly name for the custom key store.
    * Type the cluster ID of a related AWS CloudHSM cluster.
    * Type the current password of the `kmsuser` crypto user in the
     associated AWS CloudHSM cluster.

7. Choose **Save**.

When the procedure is successful, a message describes the settings that you
edited. When it is unsuccessful, an error message appears that describes the problem
and provides help on how to fix it. If you need more help, see [Troubleshooting a custom key store](fix-keystore.md "fix-keystore.md"). 8. [Reconnect the custom key store.](connect-keystore.md "connect-keystore.md")

To use the AWS CloudHSM key store, you must reconnect it after editing. You can leave the
AWS CloudHSM key store disconnected. But while it is disconnected, you cannot create KMS keys
in the AWS CloudHSM key store or use the KMS keys in the AWS CloudHSM key store in [cryptographic operations](manage-cmk-keystore.md#use-cmk-keystore "manage-cmk-keystore.md#use-cmk-keystore").
To change the properties of an AWS CloudHSM key store, use the [UpdateCustomKeyStore](../APIReference/API_UpdateCustomKeyStore.md "../APIReference/API_UpdateCustomKeyStore.md") operation. You
can change multiple properties of a custom key store in the same command. If the operation is successful, AWS KMS returns an HTTP 200 response and a JSON
object with no properties. To
verify that the changes are effective, use the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
operation.

The examples in this section use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

Begin by using [DisconnectCustomKeyStore](../APIReference/API_DisconnectCustomKeyStore.md "../APIReference/API_DisconnectCustomKeyStore.md") to [disconnect the
custom key store](disconnect-keystore.md "disconnect-keystore.md") from its AWS CloudHSM cluster. Replace the example custom key store ID,
cks-1234567890abcdef0, with an actual ID.

```
`$` `aws kms disconnect-custom-key-store --custom-key-store-id `cks-1234567890abcdef0``
```

The first example uses [UpdateCustomKeyStore](../APIReference/API_UpdateCustomKeyStore.md "../APIReference/API_UpdateCustomKeyStore.md") to change the friendly name of the AWS CloudHSM key store to
`DevelopmentKeys`. The command uses the `CustomKeyStoreId` parameter
to identify the AWS CloudHSM key store and the `CustomKeyStoreName` to specify the new
name for the custom key store.

```
`$` `aws kms update-custom-key-store --custom-key-store-id `cks-1234567890abcdef0` --new-custom-key-store-name `DevelopmentKeys``
```

The following example changes the cluster that is associated with an AWS CloudHSM key store to
another backup of the same cluster. The command uses the `CustomKeyStoreId`
parameter to identify the AWS CloudHSM key store and the `CloudHsmClusterId` parameter to
specify the new cluster ID.

```
`$` `aws kms update-custom-key-store --custom-key-store-id `cks-1234567890abcdef0` --cloud-hsm-cluster-id `cluster-1a23b4cdefg``
```

The following example tells AWS KMS that the current `kmsuser` password is
`ExamplePassword`. The command uses the `CustomKeyStoreId` parameter
to identify the AWS CloudHSM key store and the `KeyStorePassword` parameter to specify the
current password.

```
`$` `aws kms update-custom-key-store --custom-key-store-id `cks-1234567890abcdef0` --key-store-password `ExamplePassword``
```

The final command reconnects the AWS CloudHSM key store to its AWS CloudHSM cluster. You can leave the
custom key store in the disconnected state, but you must connect it before you can create new
KMS keys or use existing KMS keys for [cryptographic
operations](manage-cmk-keystore.md#use-cmk-keystore "manage-cmk-keystore.md#use-cmk-keystore"). Replace the example custom key store ID with an actual ID.

```
`$` `aws kms connect-custom-key-store --custom-key-store-id `cks-1234567890abcdef0``
```
