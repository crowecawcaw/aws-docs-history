# Permit IAM users to change

their own passwords

###### Note

Users with federated identities will use the process defined by their identity provider to change their
passwords. As a [best practice](best-practices.md "best-practices.md"), require human users to use federation with an identity provider
to access AWS using temporary credentials.

You can grant IAM users the permission to change their own passwords for signing in to the
AWS Management Console. You can do this in one of two ways:

- [Allow all IAM users in the account to
  change their own passwords](#proc_letalluserschangepassword "#proc_letalluserschangepassword").
- [Allow only selected IAM users to
  change their own passwords](#proc_letselectuserschangepassword "#proc_letselectuserschangepassword"). In this scenario, you disable the option for all users
  to change their own passwords and you use an IAM policy to grant permissions to only some
  users. This approach allows those users to change their own passwords and optionally other
  credentials like their own access keys.

###### Important

We recommend that you [set a custom
password policy](id_credentials_passwords_account-policy.md "id_credentials_passwords_account-policy.md") that requires IAM users to create strong passwords.

## To allow all IAM users change their own passwords

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, click **Account settings**.
3. In the **Password policy** section, choose
   **Edit**.
4. Choose **Custom** to use a custom password policy.
5. Select **Allow users to change their own password**, and then choose
   **Save changes**. This allows all users in the account access to the
   `iam:ChangePassword` action for only their user and to the
   `iam:GetAccountPasswordPolicy` action.
6. Provide users with the following instructions for changing their passwords: [How an IAM user changes their own
   password](id_credentials_passwords_user-change-own.md "id_credentials_passwords_user-change-own.md").

AWS CLI
Run the following command:

- `aws
iam update-account-password-policy`

API
To create an alias for your AWS Management Console
sign-in page URL, call the following operation:

- `UpdateAccountPasswordPolicy`

## To allow selected IAM users change their own passwords

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, click **Account settings**.
3. In the **Password policy** section, make sure that **Allow
   users to change their own password** is not selected. If this checkbox is
   selected, all users can change their own passwords. (See the previous procedure.)
4. Create the users who should be allowed to change their own password, if they do not
   already exist. For details, see [Create an IAM user in your AWS account](id_users_create.md "id_users_create.md").
5. (Optional) Create an IAM group for the users who should be allowed to change their
   passwords, and then add the users from the previous step to the group. For details, see
   [IAM user groups](id_groups.md "id_groups.md").
6. Assign the following policy to the group. For more information, see [Manage IAM policies](access_policies_manage.md "access_policies_manage.md").

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:GetAccountPasswordPolicy",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:ChangePassword",
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 }
 ]
}`

```

This policy grants access to the [ChangePassword](../APIReference/API_ChangePassword.md "../APIReference/API_ChangePassword.md") action, which lets users change only their own passwords from the
console, the AWS CLI, Tools for Windows PowerShell, or the API. It also grants access to the [GetAccountPasswordPolicy](../APIReference/API_GetAccountPasswordPolicy.md "../APIReference/API_GetAccountPasswordPolicy.md")
action, which lets the user view the current password policy; this permission is required so
that the user can view the account password policy on the **Change
password** page. The user must be allowed to read the current password policy to
ensure that the changed password meets the requirements of the policy. 7. Provide users with the following instructions for changing their passwords: [How an IAM user changes their own
password](id_credentials_passwords_user-change-own.md "id_credentials_passwords_user-change-own.md").

### For more information

For more information on managing credentials, see the following topics:

- [Permit IAM users to change
  their own passwords](id_credentials_passwords_enable-user-change.md "id_credentials_passwords_enable-user-change.md")
- [User passwords in AWS](id_credentials_passwords.md "id_credentials_passwords.md")
- [Set an account password policy for
  IAM users](id_credentials_passwords_account-policy.md "id_credentials_passwords_account-policy.md")
- [Manage IAM policies](access_policies_manage.md "access_policies_manage.md")
- [How an IAM user changes their own
  password](id_credentials_passwords_user-change-own.md "id_credentials_passwords_user-change-own.md")
