# Cancel key deletion

After you [schedule a KMS key for
deletion](deleting-keys-scheduling-key-deletion.md "deleting-keys-scheduling-key-deletion.md"), you can cancel the key deletion while it is still in the [pending deletion](key-state.md "key-state.md") state. You can cancel key deletion in the AWS KMS
console or by using the [CancelKeyDeletion](../APIReference/API_CancelKeyDeletion.md "../APIReference/API_CancelKeyDeletion.md") operation. After you cancel the pending deletion of a KMS key,
the key state of the KMS key is `Disabled`. For more information on enabling the
KMS key, see [Enable and disable keys](enabling-keys.md "enabling-keys.md").

###### To cancel key deletion

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Choose the check box next to the KMS key that you want to recover.
5. Choose **Key actions**, **Cancel key
   deletion**.
   The KMS key status changes from **Pending deletion** to
   **Disabled**. To use the KMS key, you must [enable it](enabling-keys.md "enabling-keys.md").

Use the [`aws kms
 cancel-key-deletion`](../../../cli/latest/reference/kms/cancel-key-deletion.md "../../../cli/latest/reference/kms/cancel-key-deletion.md") command to cancel key deletion from the AWS CLI as
shown in the following example.

```
$ aws kms cancel-key-deletion --key-id `1234abcd-12ab-34cd-56ef-1234567890ab`
```

When used successfully, the AWS CLI returns output like the output shown in the
following example:

```
{
    "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

The status of the KMS key changes from **Pending Deletion** to
**Disabled**. To use the KMS key, you must [enable it](enabling-keys.md "enabling-keys.md").
