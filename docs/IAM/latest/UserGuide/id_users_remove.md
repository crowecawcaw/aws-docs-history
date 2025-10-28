# Remove or deactivate an IAM user

[Best practices](best-practices.md#remove-credentials "best-practices.md#remove-credentials") recommend that you remove unused
IAM users from your AWS account. If you want to retain the IAM users credentials for
future use, instead of deleting them from the account you can deactivate the user's access.
For more information, see [Deactivating an IAM user](#id_users_deactivating "#id_users_deactivating").

###### Warning

Once an IAM user and its access keys are deleted, they cannot be restored or recovered.

## Prerequisite – View IAM user

access

Before you remove a user, review their recent service-level activity. This helps
prevent removing access from a principal (person or application) who is using it. For
more information about viewing last accessed information, see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Removing an IAM user (console)

When you use the AWS Management Console to remove an IAM user, IAM automatically deletes
the following associated information:

- The IAM user identifier
- Any group memberships—that is, the IAM user is removed from any groups
  that the IAM user was a member of
- Any password associated with the IAM user
- All inline policies embedded in the IAM user (policies that were applied to
  the IAM user using user group permissions are not affected)

###### Note

IAM removes any managed policies attached to the IAM user when you
delete the user, but does not delete managed policies.

- Any associated MFA device

### To remove an IAM user (console)

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**, and
   then select the checkbox next to the IAM user name that you
   want to delete.
4. At the top of the page, choose
   **Delete**.

###### Note

If any of the users have active access keys, you must
deactivate the access keys before deleting the users. For
more information, see [To deactivate an access key for an
IAM user](access-keys-admin-managed.md#admin-deactivate-access-key "access-keys-admin-managed.md#admin-deactivate-access-key"). 5. In the confirmation dialog box, enter the username in the text
input field to confirm the deletion of the user. Choose
**Delete**.

The console displays a status notification that the IAM user was
deleted.

## Deleting an IAM user (AWS CLI)

Unlike the AWS Management Console, when you delete a IAM user with the AWS CLI, you must delete the
items attached to the IAM user manually. This procedure illustrates the process.

###### To delete an IAM user from your AWS account (AWS CLI)

1. Delete the user's password, if the user has one.

`aws iam
 delete-login-profile` 2. Delete the user's access keys, if the user has them.

`aws iam
 list-access-keys` (to list the user's access keys) and
`aws iam
 delete-access-key` 3. Delete the user's signing certificate. Note that when you delete a security
credential, it's gone forever and can't be retrieved.

`aws iam
 list-signing-certificates` (to list the user's signing
certificates) and `aws iam
 delete-signing-certificate` 4. Delete the user's SSH public key, if the user has them.

`aws iam
 list-ssh-public-keys` (to list the user's SSH public keys)
and `aws iam
 delete-ssh-public-key` 5. Delete the user's Git credentials.

`aws
 iam list-service-specific-credentials` (to list the user's
git credentials) and `aws iam
 delete-service-specific-credential` 6. Deactivate the user's multi-factor authentication (MFA) device, if the user
has one.

`aws iam
 list-mfa-devices` (to list the user's MFA devices),
`aws iam
 deactivate-mfa-device` (to deactivate the device), and
`aws
 iam delete-virtual-mfa-device` (to permanently delete a
virtual MFA device) 7. Delete the user's inline policies.

`aws iam
 list-user-policies` (to list the inline policies for the
user) and [`aws iam
 delete-user-policy`](../../../cli/latest/reference/iam/delete-user-policy.md "../../../cli/latest/reference/iam/delete-user-policy.md") (to delete the policy) 8. Detach any managed policies that are attached to the user.

`aws iam
 list-attached-user-policies` (to list the managed policies
attached to the user) and [`aws iam detach-user-policy`](../../../cli/latest/reference/iam/detach-user-policy.md "../../../cli/latest/reference/iam/detach-user-policy.md") (to detach the policy) 9. Remove the user from any IAM groups.

`aws iam
 list-groups-for-user` (to list the IAM groups to which
the user belongs) and `aws iam
 remove-user-from-group` 10. Delete the user.

`aws iam
 delete-user`

## Deactivating an IAM user

You might need to deactivate an IAM user while they are temporarily away from your
company. You can leave their IAM user credentials in place and still block their AWS
access.

To deactivate a user, create and attach a policy to deny the user access to AWS. You
can restore the user's access later.

Here are two examples of deny policies that you can attach to a user to deny their
access.

The following policy does not include a time limit. You must remove the policy to
restore the user's access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*"
 }
 ]
}`

```

The following policy includes a condition that starts the policy on December 24, 2024
at 11:59 PM (UTC) and ends it on February 28, 2025 at 11:59 PM (UTC).

JSON

```
`{
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
}`

```
