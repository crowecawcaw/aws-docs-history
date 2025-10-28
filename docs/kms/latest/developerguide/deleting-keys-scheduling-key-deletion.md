# Schedule key deletion

The following procedures describe how to schedule key deletion and cancel key deletion of
AWS KMS keys (KMS keys) in AWS KMS using the AWS Management Console and the AWS KMS API.

###### Warning

Deleting a KMS key is destructive and potentially dangerous. You should proceed only
when you are sure that you don't need to use the KMS key anymore and won't need to use it
in the future. If you are not sure, you should [disable the
KMS key](enabling-keys.md "enabling-keys.md") instead of deleting it.

Before you can delete a KMS key, you must have permission to do so. For information
about giving these permissions to key administrators, see [Control access to key deletion](deleting-keys-adding-permission.md "deleting-keys-adding-permission.md").
You can also use the [kms:ScheduleKeyDeletionPendingWindowInDays](conditions-kms.md#conditions-kms-schedule-key-deletion-pending-window-in-days "conditions-kms.md#conditions-kms-schedule-key-deletion-pending-window-in-days") condition key to further
constrain the waiting period, such as enforcing a minimum waiting period.

AWS KMS records an entry in your AWS CloudTrail log when you [schedule deletion](ct-schedule-key-deletion.md "ct-schedule-key-deletion.md") of the KMS key and when the
[KMS key is actually deleted](ct-delete-key.md "ct-delete-key.md").

In the AWS Management Console, you can schedule and cancel the deletion of multiple KMS keys at
one time.

###### To schedule key deletion

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.

You cannot schedule the deletion of [AWS managed keys](concepts.md#aws-managed-key "concepts.md#aws-managed-key") or [AWS owned keys](concepts.md#aws-owned-key "concepts.md#aws-owned-key"). 4. Choose the checkbox next to the KMS key that you want to delete. 5. Choose **Key actions**, **Schedule key
deletion**. 6. Read and consider the warning, and the information about canceling the deletion
during the waiting period. If you decide to cancel the deletion, at the bottom of
the page, choose **Cancel**. 7. For **Waiting period (in days)**, enter a number of days
between 7 and 30. 8. Review the KMS keys that you are deleting. 9. Choose the check box next to **Confirm you want to schedule this key for
deletion in `<number of days>`
days.**. 10. Choose **Schedule deletion**.
The KMS key status changes to **Pending deletion**.

Use the [`aws kms
 schedule-key-deletion`](../../../cli/latest/reference/kms/schedule-key-deletion.md "../../../cli/latest/reference/kms/schedule-key-deletion.md") command to schedule key deletion of a [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key"), as shown in the following example.

You cannot schedule the deletion of an AWS managed key or AWS owned key.

```
$ aws kms schedule-key-deletion --key-id `1234abcd-12ab-34cd-56ef-1234567890ab` --pending-window-in-days 10
```

When used successfully, the AWS CLI returns output like the output shown in the
following example:

```
{
    "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "DeletionDate": 1598304792.0,
    "KeyState": "PendingDeletion",
    "PendingWindowInDays": 10
}
```
