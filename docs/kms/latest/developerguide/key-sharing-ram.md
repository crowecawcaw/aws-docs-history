

# Sharing KMS keys with AWS RAM

AWS Key Management Service (AWS KMS) integrates with AWS Resource Access Manager (AWS RAM). With AWS RAM, you can share KMS keys across your AWS accounts, within your organization in AWS Organizations, and with specific IAM roles and users. You share resources that you own by creating a *resource share*. For AWS KMS, a resource share specifies the KMS keys that you want to share and the principals to share them with.

Sharing a KMS key through AWS RAM doesn't change its existing key policy, which is named `default`. Every KMS key has a `default` key policy, whether you wrote it or AWS KMS created it for you. AWS RAM generates a second key policy for the KMS key, named `AWS_RAM`, from the *managed permission* that you choose for the resource share. The KMS key stays in your account, and you continue to manage it and its `default` key policy. AWS KMS evaluates the `default` key policy and the `AWS_RAM` key policy together.

For more information about AWS RAM, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/).

This topic explains how to share KMS keys that you own, and how to use KMS keys that are shared with you.

**Topics**
+ [Terminology](#key-sharing-ram-terms)
+ [When to use AWS RAM](#key-sharing-ram-when)
+ [Prerequisites and supported KMS keys](#key-sharing-ram-supported)
+ [Managed permissions for KMS keys](#key-sharing-ram-permissions)
+ [How managed permissions are shown in KMS keys](#key-sharing-ram-policy)
+ [How permissions are evaluated](#key-sharing-ram-evaluation)
+ [Sharing a KMS key](#key-sharing-ram-share)
+ [Revoking access to a shared KMS key](#key-sharing-ram-unshare)
+ [Identifying a shared KMS key](#key-sharing-ram-identify)
+ [Security best practices for sharing KMS keys](#key-sharing-ram-security)
+ [Other considerations](#key-sharing-ram-considerations)

## Terminology
<a name="key-sharing-ram-terms"></a>

This topic uses the following terms.

**Owner**  
The AWS account that owns the KMS key and shares it by adding it to a resource share.

**Consumer**  
A principal that a resource share shares the KMS key with.

**Managed permission**  
The AWS RAM permission that determines what consumers can do with the shared KMS key. AWS RAM generates the `AWS_RAM` key policy from it.

## When to use AWS RAM
<a name="key-sharing-ram-when"></a>

You can give another principal permission to use a KMS key in two ways. You can add a statement to the `default` key policy, as described in [Allowing users in other accounts to use a KMS key](key-policy-modifying-external-accounts.md). Or, you can add the KMS key to a resource share in AWS RAM. You can use both methods for the same KMS key.

**Use AWS RAM**  
Use AWS RAM in the following cases:  
+ You want to share a KMS key together with related AWS resources in one resource share.
+ You want to share KMS keys consistently with many AWS accounts, with your organization, or with organizational units (OUs) in AWS Organizations, by using one managed permission instead of writing multiple key policy statements.
+ You want someone else that you trust, such as your central security team or a trusted third-party service provider, to author and manage the permissions on your KMS keys through an AWS RAM customer managed permission. For more information, see [Sharing and using customer managed permissions across accounts](https://docs.aws.amazon.com/ram/latest/userguide/sharing-customer-managed-permissions.html) in the *AWS RAM User Guide*.
AWS RAM creates and manages the `AWS_RAM` key policy for you. Consumers can find the KMS keys that are shared with them through AWS RAM on the **Keys shared with me** page of the AWS KMS console and by using the `ListKeys` operation with the `ResourceOwners` parameter.

**Use a key policy statement**  
Use a key policy statement when you need granular control, such as `Deny` statements or condition keys that managed permissions don't support. AWS RAM managed permissions support only `Allow` statements.

When a KMS key has both key policies, AWS KMS evaluates them together. A permission in either key policy can allow access to the KMS key. For more information about how AWS KMS evaluates the two key policies, see [How permissions are evaluated](#key-sharing-ram-evaluation).

## Prerequisites and supported KMS keys
<a name="key-sharing-ram-supported"></a>

Before you share a KMS key, review the following requirements.
+ You can share [customer managed keys](concepts.md#customer-mgn-key) through AWS RAM. You can't share [AWS managed keys](concepts.md#aws-managed-key).
+ To share a KMS key, you must own it in your AWS account. You can't share a KMS key that is shared with you.
+ To share a KMS key, you need the following permissions:
  + `ram:CreateResourceShare` to create a resource share, or `ram:AssociateResourceShare` to add the KMS key to an existing resource share.
  + `kms:PutKeyPolicy` on the KMS key. AWS RAM uses your permissions to create and update the `AWS_RAM` key policy.
+ The KMS key and the resource share must be in the same AWS Region. To add a KMS key to a resource share, specify its [key ARN](concepts.md#key-id-key-ARN).
+ You can't add a KMS key to a resource share by its alias ARN.

You can share the following types of KMS keys:
+ Symmetric encryption KMS keys
+ Asymmetric KMS keys
+ HMAC KMS keys
+ Multi-Region primary and replica keys
+ KMS keys with imported key material
+ KMS keys in custom key stores (AWS CloudHSM key stores and external key stores)

## Managed permissions for KMS keys
<a name="key-sharing-ram-permissions"></a>

When you create a resource share, you choose a *managed permission* for each resource type in the share. The managed permission determines the actions that consumers can perform on the shared KMS key. AWS RAM writes the statements that result from the managed permission into the key's `AWS_RAM` key policy. For more information about managed permissions, see [Managing permissions in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/security-ram-permissions.html) in the *AWS RAM User Guide*.

There are two types of managed permissions:
+ **AWS managed permissions** are defined by AWS KMS and managed by AWS RAM. There is one default managed permission for the KMS key resource type, `AWSRAMPermissionKMSKeySymmetricEncryption`. If you don't choose a managed permission, AWS RAM uses the default managed permission. Use an AWS managed permission when it allows the actions that your consumers need.
+ **Customer managed permissions** are managed permissions that you author and maintain. Use a customer managed permission when you want to allow a different set of actions, or add conditions. For more information about how managed permissions work, see [How managed permissions work](https://docs.aws.amazon.com/ram/latest/userguide/security-ram-permissions.html#permissions-work) in the *AWS RAM User Guide*.

  You can also share a customer managed permission with other AWS accounts through AWS RAM. The accounts that you share it with can use it in their own resource shares, but only you can change it. For example, a central security team can author a customer managed permission for KMS keys, share it, and other teams can use it when they share their KMS keys. For more information, see [Sharing and using customer managed permissions across accounts](https://docs.aws.amazon.com/ram/latest/userguide/sharing-customer-managed-permissions.html) in the *AWS RAM User Guide*.

AWS managed permissions don't have a description in AWS RAM. The following table describes the AWS managed permissions for KMS keys and when to use each one.


| AWS managed permissions | When to use it | 
| --- | --- | 
| `AWSRAMPermissionKMSKeySymmetricEncryption` (default)<br />**Actions included:** `kms:Encrypt`, `kms:Decrypt`, `kms:ReEncrypt*`, `kms:GenerateDataKey*`, `kms:DescribeKey`, and `kms:ListGrants`.<br />`kms:CreateGrant`, with a condition that requires `kms:GrantIsForAWSResource` to be `true`. Consumers can't create grants directly, but an AWS service that's integrated with AWS KMS can create grants for them when it calls AWS KMS on their behalf. | AWS RAM uses this managed permission when you don't choose one. It lets the consumers use the KMS key for symmetric encryption, view the KMS key and its grants, and let AWS services that are integrated with AWS KMS create grants on their behalf. | 
| `AWSRAMPermissionKMSKeyLockoutResistant`<br />**Actions included:** `kms:DescribeKey`, `kms:GetKeyPolicy`, `kms:List*`, and `kms:PutKeyPolicy`, only when the caller is the root user of the AWS account that owns the KMS key. | Use it to keep the AWS account that owns the KMS key able to view and replace the key policy of the shared KMS key, through the account's root user. | 

### Considerations for using managed permissions with KMS keys
<a name="key-sharing-ram-cmp"></a>

Keep the following in mind when you choose or create a managed permission for KMS keys:
+ The default managed permission allows the operations of symmetric encryption KMS keys. To share another kind of KMS key, such as a signing key or an HMAC key, use a customer managed permission that allows the operations that the key supports, such as `kms:Sign` and `kms:Verify`, or `kms:GenerateMac` and `kms:VerifyMac`.
+ Not every AWS KMS action can be in a customer managed permission. For example, a customer managed permission can't include `kms:PutKeyPolicy`, and a statement with `kms:CreateGrant` needs a condition. To find out which actions a customer managed permission can include, see the *AWS RAM customer managed permission* column in [AWS KMS permissions](kms-api-permissions-reference.md).
+ Managed permissions can only allow actions, and some condition keys aren't supported in customer managed permissions. For details, see [Considerations for using customer managed permissions](https://docs.aws.amazon.com/ram/latest/userguide/managed-permission-considerations.html) in the *AWS RAM User Guide*.
+ A managed permission can have versions. For more information, see [Managed permission version](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-terms-and-concepts.html#term-managed-permission-version) in the *AWS RAM User Guide*.

## How managed permissions are shown in KMS keys
<a name="key-sharing-ram-policy"></a>

A KMS key can have two key policies. The `default` key policy is the one that you create and manage. The `AWS_RAM` key policy is created and managed by AWS RAM when you share the KMS key.

AWS RAM combines the permissions from all resource shares that include the KMS key into the key's single `AWS_RAM` key policy. If the resource shares use different managed permissions, the `AWS_RAM` key policy has a separate statement for each managed permission. Each statement allows the actions in its managed permission. A principal that is named in more than one statement can use the actions in all of them.

You can't create, change, or delete the `AWS_RAM` key policy. AWS RAM manages it. To change who can use the KMS key through AWS RAM, change the resource share.

You can view the `AWS_RAM` key policy by using the AWS KMS console or the AWS KMS API. You need `kms:GetKeyPolicy` permission in the AWS account that owns the KMS key.

### Using the AWS KMS console
<a name="key-sharing-ram-policy-console"></a>

**To view the `AWS_RAM` key policy (AWS KMS console)**

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. In the navigation pane, choose **Customer managed keys**.

1. In the list of KMS keys, choose the alias or key ID of the shared KMS key.

1. Choose the **Resource shares** tab, and then choose **Policy view (JSON)**.

   The **Resource shares** tab shows the `AWS_RAM` key policy, but you can't edit it there. The `default` key policy is on the **Key policy** tab.

### Using the AWS KMS API
<a name="key-sharing-ram-policy-api"></a>

You can use the `ListKeyPolicies` operation to find out whether a KMS key has an `AWS_RAM` key policy. If it has one, the response includes `default` and `AWS_RAM`. You can use the `GetKeyPolicy` operation with `PolicyName` set to `AWS_RAM` to view the `AWS_RAM` key policy.

The following AWS CLI example uses the [list-key-policies](https://docs.aws.amazon.com/cli/latest/reference/kms/list-key-policies.html) command to get the names of the key policies of a shared KMS key. Replace `{{1234abcd-12ab-34cd-56ef-1234567890ab}}` with the key ID or key ARN of your KMS key.

```bash
$ aws kms list-key-policies --key-id {{1234abcd-12ab-34cd-56ef-1234567890ab}}
```

The output shows that the KMS key has a `default` key policy and an `AWS_RAM` key policy.

```json
{
    "PolicyNames": [
        "AWS_RAM",
        "default"
    ]
}
```

The following AWS CLI example uses the [get-key-policy](https://docs.aws.amazon.com/cli/latest/reference/kms/get-key-policy.html) command to get the `AWS_RAM` key policy of a KMS key that is shared with one AWS account by using the default managed permission. The `--query Policy` and `--output text` parameters return only the key policy document, rather than a JSON object that contains it.

```bash
$ aws kms get-key-policy --key-id {{1234abcd-12ab-34cd-56ef-1234567890ab}} --policy-name AWS_RAM --query Policy --output text
```

The output is similar to the following key policy document, which is formatted here for readability. AWS RAM sets the statement IDs (`Sid`), which are shown here as placeholders.

```json
{
  "Version": "2012-10-17",
  "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "Statement": [
    {
      "Sid": "{{managed-permission-statement-id}}",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::444455556666:root"
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey",
        "kms:ListGrants"
      ],
      "Resource": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    {
      "Sid": "{{managed-permission-statement-id}}",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::444455556666:root"
      },
      "Action": [
        "kms:CreateGrant"
      ],
      "Resource": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "Condition": {
        "Bool": {
          "kms:GrantIsForAWSResource": "true"
        }
      }
    }
  ]
}
```

## How permissions are evaluated
<a name="key-sharing-ram-evaluation"></a>

AWS KMS evaluates the `default` key policy and the `AWS_RAM` key policy together. A permission in either key policy can allow access to the KMS key.

An explicit `Deny` statement in the `default` key policy overrides an `Allow` statement in the `AWS_RAM` key policy. For example, if the `default` key policy denies `kms:Encrypt` to an account that the `AWS_RAM` key policy allows to use the KMS key, principals in that account can't use the KMS key to encrypt data. Managed permissions can only allow actions, so the `AWS_RAM` key policy can't contain `Deny` statements.

The following considerations also apply to a shared KMS key.

**IAM policies**  
As with any KMS key in another account, a consumer needs two permissions to use a shared KMS key. A key policy (`default` or `AWS_RAM`) must allow the action for the consumer account, and an IAM policy in the consumer account must allow the action for the user or role that makes the request. The key policy decides what the account can do. The IAM policy decides which users and roles in the account can do it. In the IAM policy, identify the KMS key by its key ARN in the `Resource` element. For more information about IAM policies for KMS keys in other accounts, see [Step 2: Add IAM policies in the external account](key-policy-modifying-external-accounts.md#cross-account-iam-policy).

**Grants**  
Sharing a KMS key through AWS RAM doesn't change its [grants](grants.md). Deleting a resource share doesn't remove access that a grant or the `default` key policy allows.

**Policy lockout safety check**  
When you change the `default` key policy, AWS KMS checks that the new key policy still allows the principal that makes the request to change the key policy later, so you don't lose control of the KMS key. This policy lockout safety check considers only the `default` key policy. The `BypassPolicyLockoutSafetyCheck` parameter of `PutKeyPolicy` has no effect on the `AWS_RAM` key policy, which AWS RAM creates and manages.

**Controlling access to each key policy**  
The `kms:PolicyName` condition key controls access to the `GetKeyPolicy` and `PutKeyPolicy` operations based on the value of the `PolicyName` parameter in the request. For example, you can use it to control which principals in your account can view the `AWS_RAM` key policy. For more information about this condition key, see [kms:PolicyName](conditions-kms.md#conditions-kms-policy-name).

Changes to key policies are eventually consistent. For more information, see [Other considerations](#key-sharing-ram-considerations).

## Sharing a KMS key
<a name="key-sharing-ram-share"></a>

When you share a KMS key that you own, AWS RAM creates the `AWS_RAM` key policy for the KMS key from the managed permission of the resource share. Then, the consumers can attach IAM policies that allow their users and roles to use the KMS key.

To share a KMS key, you add it to a resource share. A resource share is an AWS RAM resource that specifies the resources to share and the principals to share them with.

If you share a KMS key with accounts outside your organization, AWS RAM sends them an invitation. Each account must accept the resource share invitation before the resource share gives it access to the KMS key. For more information about invitations, see [Sharing your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html) in the *AWS RAM User Guide*.

You can share a KMS key that you own using the AWS KMS console, AWS RAM console, or the AWS CLI. The AWS KMS console can start a resource share only for a KMS key that isn't in a resource share yet. To add a KMS key to an existing resource share, or to add a KMS key that is already shared to another resource share, use the AWS RAM console or the AWS CLI. For instructions, see [Update a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) in the *AWS RAM User Guide*.

### Using the AWS KMS console
<a name="key-sharing-ram-share-console"></a>

Use the following procedure to start a resource share from the AWS KMS console for a KMS key that isn't shared yet.

**To share a KMS key (AWS KMS console)**

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. In the navigation pane, choose **Customer managed keys**.

1. In the list of KMS keys, choose the alias or key ID of the KMS key that you want to share.

1. On the details page of the KMS key, choose the **Resource shares** tab.

   If the tab shows **No resource shares** and a **Create resource share** button, the KMS key isn't in a resource share. If the tab lists resource shares instead, the KMS key is shared in each one with a **Resource status** of **Associated**. The tab also lists resource shares that the KMS key was removed from, with a **Resource status** of **Disassociated**. To add the KMS key to another resource share, use the AWS RAM console or the AWS CLI.

1. Choose **Create resource share**. The **Create resource share** page of the AWS RAM console opens in a new tab.

1. Complete the resource share. For instructions, see [Creating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html) in the *AWS RAM User Guide*.

### Using the AWS CLI
<a name="key-sharing-ram-share-cli"></a>

Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command. Use the `--permission-arns` parameter to specify the managed permission. To add the KMS key to an existing resource share, use the [associate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/associate-resource-share.html) command.

The following AWS CLI example shares a KMS key with the AWS account `444455556666`. Replace the following values with your own:
+ Replace `{{my-key-share}}` with a name for the resource share.
+ Replace `{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}` with the key ARN of the KMS key to share.
+ Replace `{{444455556666}}` with the principal to share the KMS key with.

The example uses the ARN of the default AWS managed permission for KMS keys. To use a different managed permission, replace the value of `--permission-arns` with the ARN of that managed permission.

```bash
$ aws ram create-resource-share \
    --name {{my-key-share}} \
    --resource-arns {{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}} \
    --principals {{444455556666}} \
    --permission-arns arn:aws:ram::aws:permission/AWSRAMPermissionKMSKeySymmetricEncryption
```

## Revoking access to a shared KMS key
<a name="key-sharing-ram-unshare"></a>

Revoke access to a shared KMS key when you no longer want the consumers of a resource share to use it. If a KMS key is in only one resource share, deleting that share also removes the key's `AWS_RAM` key policy. The consumers then no longer have the access that the share gave them. Access that they have through the key's `default` key policy or through grants isn't affected.

Disabling a shared KMS key, or scheduling its deletion, doesn't remove it from the resource share or change its `AWS_RAM` key policy. While the KMS key is disabled or pending deletion, the consumers can still view it and find it in `ListKeys` results for keys shared with them, but they can't use it to encrypt data. Before you schedule a shared KMS key for deletion, remove it from its resource shares.

When you remove a KMS key from its only resource share, AWS RAM deletes the `AWS_RAM` key policy, and the consumers lose the permissions that the resource share gave them. They can no longer find the KMS key in `ListKeys` results for keys shared with them. Permissions that the `default` key policy or grants give them aren't affected.

If a KMS key is in two resource shares that use different managed permissions, and you remove the KMS key from one of them, AWS RAM removes that resource share's statement from the `AWS_RAM` key policy. The statement for the other resource share doesn't change.

To revoke access to a shared KMS key that you own, remove it from the resource share or delete the resource share. Remove the KMS key when the resource share also shares other AWS resources that you want to keep sharing. Delete the resource share when you no longer want to share any of its resources. Use the AWS KMS console, AWS RAM console, or the AWS CLI to do either.

### Using the AWS KMS console
<a name="key-sharing-ram-unshare-console"></a>

**To revoke access to a shared KMS key (AWS KMS console)**

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. In the navigation pane, choose **Customer managed keys**.

1. In the list of KMS keys, choose the alias or key ID of the shared KMS key.

1. On the details page of the KMS key, choose the **Resource shares** tab.

1. In the **Resource share name** column, choose the name of the resource share. The resource share opens in the AWS RAM console in a new tab.

1. Remove the KMS key from the resource share or delete the resource share. For instructions on updating or deleting a resource share, see [Update a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) and [Deleting a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-delete.html) in the *AWS RAM User Guide*.

### Using the AWS CLI
<a name="key-sharing-ram-unshare-cli"></a>

Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command to remove the KMS key from a resource share, or the [delete-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/delete-resource-share.html) command to delete the resource share.

The following AWS CLI example uses the `disassociate-resource-share` command to remove a KMS key from a resource share. Replace `{{resource-share-arn}}` with the ARN of your resource share, and `{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}` with the key ARN of the KMS key.

```bash
$ aws ram disassociate-resource-share \
--resource-share-arn {{resource-share-arn}} \
--resource-arns {{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}
```

## Identifying a shared KMS key
<a name="key-sharing-ram-identify"></a>

Owners and consumers can identify shared KMS keys by using the AWS KMS console or the AWS CLI.

### Using the AWS KMS console
<a name="key-sharing-ram-identify-console"></a>

**To find the resource shares that include your KMS key (owners)**

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. In the navigation pane, choose **Customer managed keys**.

1. In the list of KMS keys, choose the alias or key ID of the KMS key.

1. Choose the **Resource shares** tab. The KMS key is in each resource share with a **Resource status** of **Associated**.

   To list the resource shares, you need `ram:GetResourceShareAssociations` permission. Without it, the tab shows **Not authorized**. You can still choose **Policy view (JSON)** to view the `AWS_RAM` key policy, which requires `kms:GetKeyPolicy` permission.

**To find the KMS keys that are shared with you (consumers)**

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. In the navigation pane, choose **Keys shared with me**.

   The page lists the KMS keys that other AWS accounts shared with you through AWS RAM, with the **Owner account ID** and **Key ARN** of each KMS key. To show the **Key ID** column, change the table preferences.

   To view this page, you need `kms:ListKeys` permission. You don't need AWS RAM permissions.

### Using the AWS CLI
<a name="key-sharing-ram-identify-api"></a>

As an owner, use the [list-key-policies](https://docs.aws.amazon.com/cli/latest/reference/kms/list-key-policies.html) command. If the KMS key is shared through AWS RAM, the response includes `AWS_RAM`. A KMS key that you share stays in your account, and `ListKeys` still returns it with your other KMS keys. It doesn't appear on the **Keys shared with me** page or in `ListKeys` results for `OTHER_ACCOUNTS_VIA_RAM`, which list only KMS keys that other AWS accounts shared with you.

As a consumer, use the [list-keys](https://docs.aws.amazon.com/cli/latest/reference/kms/list-keys.html) command with the `ResourceOwners` parameter. Set it to `OTHER_ACCOUNTS_VIA_RAM` to list the KMS keys that other accounts shared with you through AWS RAM, or to both `SELF` and `OTHER_ACCOUNTS_VIA_RAM` to list your own KMS keys and the keys shared with you. You need `kms:ListKeys` permission, the same permission that lists the KMS keys in your account. For more information about the `ResourceOwners` parameter, see the [AWS KMS API Reference](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html).

The following AWS CLI example lists the KMS keys that are shared with you.

```bash
$ aws kms list-keys --resource-owners OTHER_ACCOUNTS_VIA_RAM
```

The output lists two KMS keys that the AWS account `111122223333` shared with you. The key ARN of each KMS key contains the owner's account ID.

```json
{
    "Keys": [
        {
            "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
            "KeyArn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        },
        {
            "KeyId": "0987dcba-09fe-87dc-65ba-ab0987654321",
            "KeyArn": "arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321"
        }
    ],
    "Truncated": false
}
```

For an example of the CloudTrail log entry for a `PutKeyPolicy` request in which AWS RAM writes the `AWS_RAM` key policy, see [PutKeyPolicy](ct-put-key-policy.md).

## Security best practices for sharing KMS keys
<a name="key-sharing-ram-security"></a>

Consumers of a resource share can use your KMS key without being named in a key policy statement that you write.

Use the following practices to control who can share your KMS keys, limit what consumers can do, and detect changes. They're general guidelines, not a complete security solution, so adapt them to your environment.

### Preventative best practices
<a name="key-sharing-ram-security-preventative"></a>

Use the following preventative practices to avoid unintended sharing and access:

**Control who can share your KMS keys**  
When you create or change a resource share that includes a KMS key, AWS RAM writes the `AWS_RAM` key policy. It does this by calling `PutKeyPolicy` on your behalf. The principal that makes the AWS RAM request needs permission to call the AWS RAM operation, such as `ram:CreateResourceShare` or `ram:AssociateResourceShare`, and `kms:PutKeyPolicy` permission on the KMS key.  
To let a principal share a KMS key without letting it change the `default` key policy, allow `kms:PutKeyPolicy` only when the value of the [kms:PolicyName](conditions-kms.md#conditions-kms-policy-name) condition key is `AWS_RAM`. With the following key policy statement, the `kms-key-sharing-role` role can share the KMS key through AWS RAM. In a key policy, the `"*"` in the `Resource` element means this KMS key. To use this example, replace the account ID and role name with your own.  

```json
{
  "Sid": "AllowSharingThroughRAM",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::{{111122223333}}:role/{{kms-key-sharing-role}}"
  },
  "Action": "kms:PutKeyPolicy",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:PolicyName": "AWS_RAM"
    }
  }
}
```
Principals that have `kms:PutKeyPolicy` permission without a `kms:PolicyName` condition, such as key administrators, can also share the KMS key if they have permission to use AWS RAM.

**Restrict sharing across your organization**  
Use service control policies (SCPs) to limit which principals can share KMS keys. The `ram:RequestedResourceType` condition key identifies requests that share KMS keys, whose resource type is `kms:Key`.  
For example, the following SCP restricts sharing of KMS keys to the `kms-key-sharing-role` role in one account. It uses the `StringEqualsIfExists` operator, so it also applies to requests that don't specify a resource type, such as adding principals to an existing resource share. To use this example, replace the account ID and role name with your own.  

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RestrictKMSKeySharingToOneRole",
      "Effect": "Deny",
      "Action": [
        "ram:CreateResourceShare",
        "ram:AssociateResourceShare"
      ],
      "Resource": "*",
      "Condition": {
        "StringEqualsIfExists": {
          "ram:RequestedResourceType": "kms:Key"
        },
        "ArnNotEquals": {
          "aws:PrincipalArn": "arn:aws:iam::{{111122223333}}:role/{{kms-key-sharing-role}}"
        }
      }
    }
  ]
}
```
To prevent sharing with accounts outside your organization, deny `ram:CreateResourceShare` and `ram:UpdateResourceShare` when the value of the `ram:RequestedAllowsExternalPrincipals` condition key is `true`. For this and other examples, see [Example service control policies for AWS Organizations and AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/security-scp.html) in the *AWS RAM User Guide*.

**Give consumers only the permissions they need**  
Use the default managed permission only when consumers need all of its actions. Otherwise, create a customer managed permission that allows only the actions that the consumers need. Before you share a KMS key or accept a resource share, review the managed permission in the AWS RAM console, or by using the `get-permission` command in the AWS CLI. For more information about the actions that you can include, see [Considerations for using managed permissions with KMS keys](#key-sharing-ram-cmp).

**Keep guardrails in the `default` key policy**  
An explicit `Deny` statement in the `default` key policy overrides an `Allow` statement in the `AWS_RAM` key policy, so you can use the `default` key policy to deny actions that no consumer should have. You can also use [resource control policies](resource-control-policies.md) (RCPs) to set the maximum permissions for the KMS keys in your organization. For more information about how AWS KMS evaluates the two key policies, see [How permissions are evaluated](#key-sharing-ram-evaluation).

### Detective best practices
<a name="key-sharing-ram-security-detective"></a>

Use the following detective practices to find sharing and changes to shared KMS keys:

**Monitor sharing activity**  
CloudTrail records the AWS RAM operations that create and change resource shares, such as `CreateResourceShare`, `AssociateResourceShare`, and `DisassociateResourceShare`. AWS KMS also records a `PutKeyPolicy` entry in your account each time AWS RAM writes the `AWS_RAM` key policy of your KMS key. Create alerts for these events, for example by using an EventBridge rule. For an example of the `PutKeyPolicy` entry, see [PutKeyPolicy](ct-put-key-policy.md).

**Review shared KMS keys regularly**  
As the owner, review the resource shares that include your KMS keys and the `AWS_RAM` key policy of each shared KMS key. As a consumer, review the KMS keys that other AWS accounts shared with you. For more information about identifying shared KMS keys, see [Identifying a shared KMS key](#key-sharing-ram-identify).

### Grants after you stop sharing
<a name="key-sharing-ram-security-grants"></a>

When you remove a KMS key from a resource share, or delete the resource share, the consumers lose the permissions that the resource share gave them. Grants aren't affected. Grants that AWS services created for principals in a consumer account while the KMS key was shared stay in effect until they're retired or revoked.

To find these grants, use the `ListGrants` operation on the KMS key. The `IssuingAccount` field of each grant shows the AWS account that created it. To remove a grant, use the `RevokeGrant` operation. For more information about viewing and revoking grants, see [Viewing grants](grant-view.md) and [Retiring and revoking grants](grant-delete.md).

## Other considerations
<a name="key-sharing-ram-considerations"></a>

Keep the following in mind when you share KMS keys through AWS RAM.

**Quotas**  
The `AWS_RAM` key policy can be up to 32,768 characters, and it doesn't count toward the [key policy size quota](key-policy-overview.md#key-policy-format) for the `default` key policy. Because AWS RAM combines all resource shares that include the KMS key into this one key policy, adding resource shares or principals makes it larger, and splitting principals across resource shares doesn't avoid the limit. AWS KMS doesn't otherwise limit how many resource shares include a KMS key or how many principals they share it with. The policy template of a customer managed permission can be up to 20,480 bytes. AWS RAM quotas, such as the number of principals and resources in a resource share, also apply. For more information about AWS RAM quotas, see [AWS Resource Access Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ram.html) in the *AWS General Reference*.

**Regions**  
Sharing KMS keys through AWS RAM isn't available in the Middle East (UAE) and Middle East (Bahrain) Regions.

**Eventual consistency**  
Like other changes to AWS KMS resources, changes to a resource share, and the `AWS_RAM` key policy that AWS RAM writes, are eventually consistent. After you create, change, or delete a resource share, it might take a short time before `ListKeys` results and access to the shared KMS key reflect the change. For more information about eventual consistency, see [AWS KMS eventual consistency](accessing-kms.md#programming-eventual-consistency).