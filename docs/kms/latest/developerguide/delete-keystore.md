# Delete an AWS CloudHSM key store

When you delete an AWS CloudHSM key store, AWS KMS deletes all metadata about the AWS CloudHSM key store
from KMS, including information about its association with an AWS CloudHSM cluster. This operation does
not affect the AWS CloudHSM cluster, its HSMs, or its users. You can create a new AWS CloudHSM key store that
is associated with the same AWS CloudHSM cluster, but you cannot undo the delete operation.

You can only delete an AWS CloudHSM key store that is disconnected from its AWS CloudHSM cluster and does
not contain any AWS KMS keys. Before you delete a custom key store, do the following.

- Verify that you will never need to use any of the KMS keys in the key store for any
  [cryptographic operations](manage-cmk-keystore.md#use-cmk-keystore "manage-cmk-keystore.md#use-cmk-keystore"). Then [schedule deletion](deleting-keys.md#delete-cmk-keystore "deleting-keys.md#delete-cmk-keystore") of all of the KMS keys from the
  key store. For help finding the KMS keys in an AWS CloudHSM key store, see [Find the KMS keys in an AWS CloudHSM key store](find-cmk-in-keystore.md "find-cmk-in-keystore.md").
- Confirm that all KMS keys have been deleted. To view the KMS keys in an AWS CloudHSM key
  store, see [Identify KMS keys in AWS CloudHSM key stores](identify-key-types.md#identify-key-hsm-keystore "identify-key-types.md#identify-key-hsm-keystore").
- [Disconnect the AWS CloudHSM key store](disconnect-keystore.md "disconnect-keystore.md") from its AWS CloudHSM
  cluster.
  Instead of deleting the AWS CloudHSM key store, consider [disconnecting it](disconnect-keystore.md "disconnect-keystore.md") from its associated AWS CloudHSM cluster. While an AWS CloudHSM key store is
  disconnected, you can manage the AWS CloudHSM key store and its AWS KMS keys. But you cannot create
  or use KMS keys in the AWS CloudHSM key store. You can reconnect the AWS CloudHSM key store at any
  time.

## Delete your AWS CloudHSM key store

You can delete your AWS CloudHSM key store in the AWS KMS console or by using the [DeleteCustomKeyStore](../APIReference/API_DeleteCustomKeyStore.md "../APIReference/API_DeleteCustomKeyStore.md") operation.

To delete an AWS CloudHSM key store in the AWS Management Console, begin by selecting the AWS CloudHSM key store from
the **Custom key stores** page.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Custom key stores**, **AWS CloudHSM key stores**.
4. Find the row that represents the AWS CloudHSM key store that you want to delete. If the
   **Connection state** of the AWS CloudHSM key store is not
   **Disconnected**, you must [disconnect the AWS CloudHSM key store](disconnect-keystore.md "disconnect-keystore.md") before you delete it.
5. From the **Key store actions** menu, choose
   **Delete**.
   When the operation completes, a success message appears and the AWS CloudHSM key store no longer
   appears in the key stores list. If the operation is unsuccessful, an error message appears
   that describes the problem and provides help on how to fix it. If you need more help, see
   [Troubleshooting a custom key store](fix-keystore.md "fix-keystore.md").

To delete an AWS CloudHSM key store, use the [DeleteCustomKeyStore](../APIReference/API_DeleteCustomKeyStore.md "../APIReference/API_DeleteCustomKeyStore.md") operation.
If the operation is successful, AWS KMS returns an HTTP 200 response and a JSON
object with no properties.

To begin, verify that the AWS CloudHSM key store does not contain any AWS KMS keys. You cannot
delete a custom key store that contains KMS keys. The first example command uses [ListKeys](../APIReference/API_ListKeys.md "../APIReference/API_ListKeys.md") and [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") to search for AWS KMS keys in
the AWS CloudHSM key store with the example `cks-1234567890abcdef0`
custom key store ID. In this case, the command does not return any KMS keys. If it does, use
the [ScheduleKeyDeletion](../APIReference/API_ScheduleKeyDeletion.md "../APIReference/API_ScheduleKeyDeletion.md")
operation to schedule deletion of each of the KMS keys.

Bash

```
`for key in $(aws kms list-keys --query 'Keys[*].KeyId' --output text) ;
do aws kms describe-key --key-id $key |
grep '"CustomKeyStoreId": "`cks-1234567890abcdef0`"' --context 100; done`
```

PowerShell

```
`PS C:\>` `Get-KMSKeyList | Get-KMSKey | where CustomKeyStoreId -eq '`cks-1234567890abcdef0`'`
```

Next, disconnect the AWS CloudHSM key store. This example command uses the [DisconnectCustomKeyStore](../APIReference/API_DisconnectCustomKeyStore.md "../APIReference/API_DisconnectCustomKeyStore.md")
operation to disconnect an AWS CloudHSM key store from its AWS CloudHSM cluster. Before running this
command, replace the example custom key store ID with a valid one.

Bash

```
`$` `aws kms disconnect-custom-key-store --custom-key-store-id `cks-1234567890abcdef0``
```

PowerShell

```
`PS C:\>` `Disconnect-KMSCustomKeyStore -CustomKeyStoreId `cks-1234567890abcdef0``
```

After the custom key store is disconnected, you can use the [DeleteCustomKeyStore](../APIReference/API_DeleteCustomKeyStore.md "../APIReference/API_DeleteCustomKeyStore.md") operation to
delete it.

Bash

```
`$` `aws kms delete-custom-key-store --custom-key-store-id `cks-1234567890abcdef0``
```

PowerShell

```
`PS C:\>` `Remove-KMSCustomKeyStore -CustomKeyStoreId `cks-1234567890abcdef0``
```
