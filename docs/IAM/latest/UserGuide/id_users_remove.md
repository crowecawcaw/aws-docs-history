

# Remove or deactivate an IAM user
<a name="id_users_remove"></a>

[Best practices](best-practices.md#remove-credentials) recommend that you remove unused IAM users from your AWS account. If you want to retain the IAM users credentials for future use, instead of deleting them from the account you can deactivate the user's access. For more information, see [Deactivating an IAM user](#id_users_deactivating).

**Warning**  
Once an IAM user and its access keys are deleted, they cannot be restored or recovered.

## Prerequisite – View IAM user access
<a name="users-manage_prerequisites"></a>

Before you remove a user, review their recent service-level activity. This helps prevent removing access from a principal (person or application) who is using it. For more information about viewing last accessed information, see [Refine permissions in AWS using last accessed information](access_policies_last-accessed.md).

## Removing an IAM user (console)
<a name="id_users_deleting_console"></a>

When you use the AWS Management Console to remove an IAM user, IAM automatically deletes the following associated information: 
+ The IAM user identifier
+ Any group memberships—that is, the IAM user is removed from any groups that the IAM user was a member of
+ Any password associated with the IAM user 
+ All inline policies embedded in the IAM user (policies that were applied to the IAM user using user group permissions are not affected) 
**Note**  
IAM removes any managed policies attached to the IAM user when you delete the user, but does not delete managed policies. 
+ Any associated MFA device

### To remove an IAM user (console)
<a name="id_users_remove-section-1"></a>

------
#### [ Console ]

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

1. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.

1. In the navigation pane, choose **Users**, and then select the checkbox next to the IAM user name that you want to delete. 

1. At the top of the page, choose **Delete**.
**Note**  
If any of the users have active access keys, you must deactivate the access keys before deleting the users. For more information, see [To deactivate an access key for an IAM user](access-keys-admin-managed.md#admin-deactivate-access-key).

1. In the confirmation dialog box, enter the username in the text input field to confirm the deletion of the user. Choose **Delete**. 

The console displays a status notification that the IAM user was deleted.

------

## Deleting an IAM user (AWS CLI)
<a name="id_users_deleting_cli"></a>

Unlike the AWS Management Console, when you delete a IAM user with the AWS CLI, you must delete the items attached to the IAM user manually. This procedure illustrates the process. 

**To delete an IAM user from your AWS account (AWS CLI)**

1. Delete the user's password, if the user has one.

   `[aws iam delete-login-profile](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-login-profile.html)`

1. Delete the user's access keys, if the user has them.

   `[aws iam list-access-keys](https://docs.aws.amazon.com/cli/latest/reference/iam/list-access-keys.html)` (to list the user's access keys) and `[aws iam delete-access-key](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-access-key.html)`

1. Delete the user's signing certificate. Note that when you delete a security credential, it's gone forever and can't be retrieved.

   `[aws iam list-signing-certificates](https://docs.aws.amazon.com/cli/latest/reference/iam/list-signing-certificates.html)` (to list the user's signing certificates) and `[aws iam delete-signing-certificate](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-signing-certificate.html)`

1. Delete the user's SSH public key, if the user has them.

   `[aws iam list-ssh-public-keys](https://docs.aws.amazon.com/cli/latest/reference/iam/list-ssh-public-keys.html)` (to list the user's SSH public keys) and `[aws iam delete-ssh-public-key](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-ssh-public-key.html)`

1. Delete the user's Git credentials.

   `[aws iam list-service-specific-credentials](https://docs.aws.amazon.com/cli/latest/reference/iam/list-service-specific-credentials.html)` (to list the user's git credentials) and `[aws iam delete-service-specific-credential](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-service-specific-credential.html)`

1. Deactivate the user's multi-factor authentication (MFA) device, if the user has one.

   `[aws iam list-mfa-devices](https://docs.aws.amazon.com/cli/latest/reference/iam/list-mfa-devices.html)` (to list the user's MFA devices), `[aws iam deactivate-mfa-device](https://docs.aws.amazon.com/cli/latest/reference/iam/deactivate-mfa-device.html)` (to deactivate the device), and `[aws iam delete-virtual-mfa-device](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-virtual-mfa-device.html)` (to permanently delete a virtual MFA device) 

1. Delete the user's inline policies. 

   `[aws iam list-user-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-user-policies.html)` (to list the inline policies for the user) and [`aws iam delete-user-policy`](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-user-policy.html) (to delete the policy) 

1. Detach any managed policies that are attached to the user. 

   `[aws iam list-attached-user-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-attached-user-policies.html)` (to list the managed policies attached to the user) and [`aws iam detach-user-policy`](https://docs.aws.amazon.com/cli/latest/reference/iam/detach-user-policy.html) (to detach the policy) 

1. Remove the user from any IAM groups. 

   `[aws iam list-groups-for-user](https://docs.aws.amazon.com/cli/latest/reference/iam/list-groups-for-user.html)` (to list the IAM groups to which the user belongs) and `[aws iam remove-user-from-group](https://docs.aws.amazon.com/cli/latest/reference/iam/remove-user-from-group.html)` 

1. Delete the user.

   `[aws iam delete-user](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-user.html)` 

## Deactivating an IAM user
<a name="id_users_deactivating"></a>

You might need to deactivate an IAM user while they are temporarily away from your company. You can leave their IAM user credentials in place and still block their AWS access.

To deactivate a user, create and attach a policy to deny the user access to AWS. You can restore the user's access later.

Here are two examples of deny policies that you can attach to a user to deny their access.

The following policy does not include a time limit. You must remove the policy to restore the user's access.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [ 
      {
        "Effect": "Deny",
        "Action": "*",
        "Resource": "*"
      } 
   ]
}
```

------

The following policy includes a condition that starts the policy on December 24, 2024 at 11:59 PM (UTC) and ends it on February 28, 2025 at 11:59 PM (UTC).

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
      {
        "Effect": "Deny",
        "Action": "*",
        "Resource": "*",
        "Condition": {
          "DateGreaterThan": {"aws:CurrentTime": "2024-12-24T23:59:59Z"},
          "DateLessThan": {"aws:CurrentTime": "2025-02-28T23:59:59Z"}
          }
       }
   ]
}
```

------