# Using identity-based policies (IAM policies) for AWS Account Management

For a full discussion of AWS accounts and IAM users, see [What Is
IAM?](../../../IAM/latest/UserGuide/IAM_Introduction.md "../../../IAM/latest/UserGuide/IAM_Introduction.md") in the _IAM User Guide_.

For instructions on how you can update customer managed policies, see [Edit IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-managed-policy-console") in the _IAM User Guide_.

## AWS Account Management actions policies

This table summarizes the permissions that grant access to your account settings.
For examples of policies that use these permissions, see [Identity-based policy examples for AWS Account Management](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

###### Note

To grant IAM users write access to a specific account setting in the [**Account**](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account") page of the AWS Management Console, you must
allow the `GetAccountInformation` permission, in addition to the
permission (or permissions) that you want to use to modify that setting.

| Permission name                    | Access level | Description                                                                                                                                 |
| ---------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `account:ListRegions`              | List         | Grants permission to list the available Regions.                                                                                            |
| `account:GetAccountInformation`    | Read         | Grants permission to retrieve the account information for an<br>account.                                                                    |
| `account:GetAlternateContact`      | Read         | Grants permission to retrieve the alternate contacts for an<br>account.                                                                     |
| `account:GetContactInformation`    | Read         | Grants permission to retrieve the primary contact information<br>for an account.                                                            |
| `account:GetPrimaryEmail`          | Read         | Grants permission to retrieve the primary email address of an<br>account.                                                                   |
| `account:GetRegionOptStatus`       | Read         | Grants permission to get the opt-in status of a Region.                                                                                     |
| `account:AcceptPrimaryEmailUpdate` | Write        | Grants permission to accept the primary email address update<br>of the member account in an AWS organization.                               |
| `account:CloseAccount`             | Write        | Grants permission to close an account.<br>NoteThis is a permission for the console only. No API access<br>is available for this permission. |
| `account:DeleteAlternateContact`   | Write        | Grants permission to delete the alternate contacts for an<br>account.                                                                       |
| `account:DisableRegion`            | Write        | Grants permission to disable use of a Region.                                                                                               |
| `account:EnableRegion`             | Write        | Grants permission to enable use of a Region.                                                                                                |
| `account:PutAccountName`           | Write        | Grants permission to update the name for an account.                                                                                        |
| `account:PutAlternateContact`      | Write        | Grants permission to modify the alternate contacts for an<br>account.                                                                       |
| `account:PutContactInformation`    | Write        | Grants permission to update the primary contact information<br>for an account.                                                              |
| `account:StartPrimaryEmailUpdate`  | Write        | Grants permission to initiate the primary email address update<br>of the member account in an AWS organization.                             |
