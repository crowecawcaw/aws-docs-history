# Control access to key deletion

If you use IAM policies to allow AWS KMS permissions, IAM identities that have AWS
administrator access (`"Action": "*"`) or AWS KMS full access (`"Action":
 "kms:*"`) are already allowed to schedule and cancel key the deletion of KMS keys.
To allow key administrators to schedule and cancel key deletion in the key policy, use the
AWS KMS console or the AWS KMS API.

Typically, only key administrators have permission to schedule or cancel key deletion.
However, you can give these permissions to other IAM identities by adding the
`kms:ScheduleKeyDeletion` and `kms:CancelKeyDeletion` permission to
the key policy or an IAM policy. You can also use the [kms:ScheduleKeyDeletionPendingWindowInDays](conditions-kms.md#conditions-kms-schedule-key-deletion-pending-window-in-days "conditions-kms.md#conditions-kms-schedule-key-deletion-pending-window-in-days") condition key to further
constrain the values that principals can specify in the `PendingWindowInDays`
parameter of a [ScheduleKeyDeletion](../APIReference/API_ScheduleKeyDeletion.md "../APIReference/API_ScheduleKeyDeletion.md") request.

## Allow key administrators to schedule and cancel key

deletion

To give key administrators permission to schedule and cancel key deletion.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Choose the alias or key ID of the KMS key whose permissions you want to
   change.
5. Choose the **key policy** tab.
6. The next step differs for the _default view_
   and _policy view_ of your key policy. Default view
   is available only if you are using the default console key policy. Otherwise, only
   policy view is available.

When default view is available, a **Switch to policy view** or
**Switch to default view** button appears on the **Key
policy** tab.

    * In default view:


    	1. Under **Key deletion**, choose **Allow key
    	 administrators to delete this key**.
    * In policy view:


    	1. Choose **Edit**.
    	2. In the policy statement for key administrators, add the
    	 `kms:ScheduleKeyDeletion` and
    	 `kms:CancelKeyDeletion` permissions to the `Action`
    	 element.



    	```
    	{
    	  "Sid": "Allow access for Key Administrators",
    	  "Effect": "Allow",
    	  "Principal": {"AWS": "arn:aws:iam::111122223333:user/KMSKeyAdmin"},
    	  "Action": [
    	    "kms:Create*",
    	    "kms:Describe*",
    	    "kms:Enable*",
    	    "kms:List*",
    	    "kms:Put*",
    	    "kms:Update*",
    	    "kms:Revoke*",
    	    "kms:Disable*",
    	    "kms:Get*",
    	    "kms:Delete*",
    	    **"kms:ScheduleKeyDeletion",
    	 "kms:CancelKeyDeletion"**
    	  ],
    	  "Resource": "*"
    	}
    	```
    	3. Choose **Save changes**.

You can use the AWS Command Line Interface to add permissions for scheduling and canceling key
deletion.

###### To add permission to schedule and cancel key deletion

1. Use the [`aws kms
get-key-policy`](../../../cli/latest/reference/kms/get-key-policy.md "../../../cli/latest/reference/kms/get-key-policy.md") command to retrieve the existing key policy, and
   then save the policy document to a file.
2. Open the policy document in your preferred text editor. In the policy statement
   for key administrators, add the `kms:ScheduleKeyDeletion` and
   `kms:CancelKeyDeletion` permissions. The following example shows a
   policy statement with these two permissions:

```
{
  "Sid": "Allow access for Key Administrators",
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::111122223333:user/KMSKeyAdmin"},
  "Action": [
    "kms:Create*",
    "kms:Describe*",
    "kms:Enable*",
    "kms:List*",
    "kms:Put*",
    "kms:Update*",
    "kms:Revoke*",
    "kms:Disable*",
    "kms:Get*",
    "kms:Delete*",
    **"kms:ScheduleKeyDeletion",
 "kms:CancelKeyDeletion"**
  ],
  "Resource": "*"
}
```

3. Use the [`aws kms
put-key-policy`](../../../cli/latest/reference/kms/put-key-policy.md "../../../cli/latest/reference/kms/put-key-policy.md") command to apply the key policy to the
   KMS key.
