# Change a key policy

You can change the key policy for a KMS key in your AWS account by using
the AWS Management Console or the [PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md") operation. You cannot use these techniques to change the key policy of a KMS key in a different AWS account.

When changing a key policy, keep in mind the following rules:

- You can view the key policy for an [AWS managed key](concepts.md#aws-managed-key "concepts.md#aws-managed-key") or a [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key"), but you can
  only change the key policy for a customer managed key. The policies of AWS managed keys
  are created and managed by the AWS service that created the KMS key in your account. You
  cannot view or change the key policy for an [AWS owned key](concepts.md#aws-owned-key "concepts.md#aws-owned-key").
- You can add or remove IAM users, IAM roles, and AWS accounts in the key policy,
  and change the actions that are allowed or denied for those principals. For more information
  about the ways to specify principals and permissions in a key policy, see [Key policies](key-policies.md "key-policies.md").
- You cannot add IAM groups to a key policy, but you can add multiple IAM users and
  IAM roles. For more information, see [Allowing multiple IAM principals
  to access a KMS key](iam-policies.md#key-policy-modifying-multiple-iam-users "iam-policies.md#key-policy-modifying-multiple-iam-users").
- If you add external AWS accounts to a key policy, you must also use IAM policies in
  the external accounts to give permissions to IAM users, groups, or roles in those
  accounts. For more information, see [Allowing users in other accounts to
  use a KMS key](key-policy-modifying-external-accounts.md "key-policy-modifying-external-accounts.md").
- The resulting key policy document cannot exceed 32 KB (32,768 bytes).

## How to change a key policy

You can change a key policy in three different ways as explained in the
following sections.

###### Topics

- [Using the AWS Management Console
  default view](#key-policy-modifying-how-to-console-default-view "#key-policy-modifying-how-to-console-default-view")
- [Using the AWS Management Console policy
  view](#key-policy-modifying-how-to-console-policy-view "#key-policy-modifying-how-to-console-policy-view")
- [Using the AWS KMS API](#key-policy-modifying-how-to-api "#key-policy-modifying-how-to-api")

### Using the AWS Management Console

default view

You can use the console to change a key policy with a graphical interface called the
_default view_.

If the following steps don't match what you see in the console, it might mean that this
key policy was not created by the console. Or it might mean that the key policy has been
modified in a way that the console's default view does not support. In that case, follow the
steps at [Using the AWS Management Console policy
view](#key-policy-modifying-how-to-console-policy-view "#key-policy-modifying-how-to-console-policy-view") or [Using the AWS KMS API](#key-policy-modifying-how-to-api "#key-policy-modifying-how-to-api").

1. View the key policy for a customer managed key as described in [Using the AWS KMS console](key-policy-viewing.md#key-policy-viewing-console "key-policy-viewing.md#key-policy-viewing-console"). (You cannot change the key policies of AWS managed keys.)
2. Decide what to change.
   - To add or remove [key
     administrators](key-policy-default.md#key-policy-default-allow-administrators "key-policy-default.md#key-policy-default-allow-administrators"), and to allow or prevent key administrators from [deleting the KMS key](deleting-keys.md "deleting-keys.md"), use the controls in the
     **Key administrators** section of the page. Key administrators
     manage the KMS key, including enabling and disabling it, setting key policy, and [enabling key rotation](rotate-keys.md "rotate-keys.md").
   - To add or remove [key
     users](key-policy-default.md#key-policy-default-allow-users "key-policy-default.md#key-policy-default-allow-users"), and to allow or disallow external AWS accounts to use the KMS key, use
     the controls in the **Key users** section of the page. Key users
     can use the KMS key in [cryptographic
     operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations"), such as encrypting, decrypting, re-encrypting, and generating
     data keys.

### Using the AWS Management Console policy

view

You can use the console to change a key policy document with the console's
_policy view_.

1. View the key policy for a customer managed key as described in [Using the AWS KMS console](key-policy-viewing.md#key-policy-viewing-console "key-policy-viewing.md#key-policy-viewing-console"). (You cannot change the key policies of AWS managed keys.)
2. In the **Key Policy** section, choose **Switch to policy
   view**.
3. Choose **Edit**.
4. Decide what to change.
   - To add a new statement, choose **Add new statement**. Then,
     you can select the actions, principals, and conditions for your new key policy
     statement from the options listed in the statement builder panel, or manually
     enter the policy statement elements.
   - To remove a statement from your key policy, select the statement and then choose
     **Remove**. Review the selected policy statement and confirm that
     you want to remove it. If you decide that you do not want to proceed with removing
     the statement, choose **Cancel**.
   - To edit an existing key policy statement, select the statement. Then,
     you can use the statement builder panel to choose specific elements
     that you want to modify, or manually edit the statement.

5. Choose **Save changes**.

### Using the AWS KMS API

You can use the [PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md")
operation to change the key policy of a KMS key in your AWS account. You cannot use this API
on a KMS key in a different AWS account.

1. Use the [GetKeyPolicy](../APIReference/API_GetKeyPolicy.md "../APIReference/API_GetKeyPolicy.md")
   operation to get the existing key policy document, and then save the key policy document
   to a file. For sample code in multiple programming languages, see [Use GetKeyPolicy with an AWS SDK or CLI](example_kms_GetKeyPolicy_section.md "example_kms_GetKeyPolicy_section.md").
2. Open the key policy document in your preferred text editor, edit the key policy
   document, and then save the file.
3. Use the [PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md")
   operation to apply the updated key policy document to the KMS key. For sample code in
   multiple programming languages, see [Use PutKeyPolicy with an AWS SDK or CLI](example_kms_PutKeyPolicy_section.md "example_kms_PutKeyPolicy_section.md").

For an example of copying a key policy from one KMS key to another, see the [GetKeyPolicy example](../../../cli/latest/reference/kms/get-key-policy.md#examples "../../../cli/latest/reference/kms/get-key-policy.md#examples") in the
AWS CLI Command Reference.
