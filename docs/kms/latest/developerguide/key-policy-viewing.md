

# View a key policies

You can view the key policy for an AWS KMS [customer managed key](concepts.md#customer-mgn-key) or an [AWS managed key](concepts.md#aws-managed-key) in your account by using the AWS KMS console or the [GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html) operation in the AWS KMS API. You cannot use these techniques to view the key policy of a KMS key in a different AWS account. 

Every KMS key has a `default` key policy. A customer managed key that you share through AWS Resource Access Manager (AWS RAM) also has an `AWS_RAM` key policy, which AWS RAM creates and manages. You can view the `AWS_RAM` key policy, but you can't change it. For more information about the `AWS_RAM` key policy, see [How managed permissions are shown in KMS keys](key-sharing-ram.md#key-sharing-ram-policy).

To learn more about AWS KMS key policies, see [Key policies in AWS KMS](key-policies.md). To learn how to determine which users and roles have access to a KMS key, see [Determining access to AWS KMS keys](determining-access.md).

## Using the AWS KMS console
<a name="key-policy-viewing-console"></a>

Authorized users can view the key policy for an [AWS managed key](concepts.md#aws-managed-key) or a [customer managed key](concepts.md#customer-mgn-key) on the **Key policy** tab of the AWS Management Console. 

To view the key policy for a KMS key in the AWS Management Console, you must have [kms:ListAliases](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListAliases.html), [kms:DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html), and [kms:GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html) permissions.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. 

   To view the keys in your account that AWS creates and manages for you, in the navigation pane, choose **AWS managed keys**. To view the keys in your account that you create and manage, in the navigation pane choose **Customer managed keys**.

1. In the list of KMS keys, choose the alias or key ID of the KMS key that you want to examine.

1. Choose the **Key policy** tab.

   On the **Key policy** tab, you might see the key policy document. This is *policy view*. In the key policy statements, you can see the principals who have been given access to the KMS key by the key policy, and you can see the actions they can perform.

   The following example shows the policy view for the [default key policy](key-policy-default.md).   
![View of the default key policy in policy view in the AWS KMS console](https://docs.aws.amazon.com/kms/latest/developerguide/images/console-key-policy-view.png)

   Or, if you created the KMS key in the AWS Management Console, you will see the *default view* with sections for **Key administrators**, **Key deletion**, and **Key Users**. To see the key policy document, choose **Switch to policy view**. If the **Key policy** tab shows a **Default view** and **Policy view (JSON)** control instead, choose **Policy view (JSON)**.

   The following example shows the default view for the [default key policy](key-policy-default.md).   
![View of the default key policy in default view in the AWS KMS console](https://docs.aws.amazon.com/kms/latest/developerguide/images/console-key-policy-full-vsm.png)

1. (Optional) To view the `AWS_RAM` key policy of a customer managed key that you share through AWS RAM, choose the **Resource shares** tab, and then choose **Policy view (JSON)**.

   The **Key policy** tab shows only the `default` key policy. The **Resource shares** tab lists the resource shares for the KMS key, and its **Policy view (JSON)** shows the `AWS_RAM` key policy. The KMS key is in each resource share with a **Resource status** of **Associated**. You can't edit the `AWS_RAM` key policy in the console. If the **Resource shares** tab shows **No resource shares**, the KMS key isn't in a resource share.

   To list the resource shares, you also need `ram:GetResourceShareAssociations` permission. Without it, the **Resource shares** tab shows **Not authorized**, but you can still choose **Policy view (JSON)** to view the `AWS_RAM` key policy.

## Using the AWS KMS API
<a name="key-policy-viewing-api"></a>

To get the key policy for a KMS key in your AWS account, use the [GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html) operation in the AWS KMS API. You cannot use this operation to view a key policy in a different account.

The following example uses the [get-key-policy](https://docs.aws.amazon.com/cli/latest/reference/kms/get-key-policy.html) command in the AWS Command Line Interface (AWS CLI), but you can use any AWS SDK to make this request. 

The valid values of the `PolicyName` parameter are `default` and `AWS_RAM`. If you omit `PolicyName`, GetKeyPolicy returns the `default` key policy. The `--query Policy` and `--output text` parameters return only the key policy document, rather than a JSON object that contains it, to make it easier to view.

Before running this command, replace the example key ID with a valid one from your account.

```bash
$ aws kms get-key-policy --key-id {{1234abcd-12ab-34cd-56ef-1234567890ab}} --policy-name default --query Policy --output text
```

The response should be similar to the following one, which returns the [default key policy](key-policy-default.md).

------
#### [ JSON ]

****  

```json
{
  "Version":"2012-10-17",		 	 	 
  "Id" : "key-consolepolicy-3",
  "Statement" : [ {
  "Sid" : "EnableIAMUserPermissions",
    "Effect" : "Allow",
    "Principal" : {
      "AWS" : "arn:aws:iam::{{111122223333}}:root"
    },
    "Action" : "kms:*",
    "Resource" : "*"
  } ]
}
```

------

To find out whether a KMS key has an `AWS_RAM` key policy, use the [list-key-policies](https://docs.aws.amazon.com/cli/latest/reference/kms/list-key-policies.html) command. It returns `default` and, when the KMS key has one, `AWS_RAM`.

```bash
$ aws kms list-key-policies --key-id {{1234abcd-12ab-34cd-56ef-1234567890ab}}
```

Replace the following value:
+ `{{1234abcd-12ab-34cd-56ef-1234567890ab}}` – The key ID or key ARN of your KMS key.

For a KMS key that you share through AWS RAM, the output shows both key policies.

```json
{
    "PolicyNames": [
        "AWS_RAM",
        "default"
    ]
}
```

To view the `AWS_RAM` key policy, set the `--policy-name` parameter to `AWS_RAM`. If the KMS key doesn't have an `AWS_RAM` key policy, GetKeyPolicy returns a `NotFoundException` with the message `No such policy exists`. For an example of an `AWS_RAM` key policy, see [How managed permissions are shown in KMS keys](key-sharing-ram.md#key-sharing-ram-policy).

```bash
$ aws kms get-key-policy --key-id {{1234abcd-12ab-34cd-56ef-1234567890ab}} --policy-name AWS_RAM --query Policy --output text
```

Replace the following value:
+ `{{1234abcd-12ab-34cd-56ef-1234567890ab}}` – The key ID or key ARN of your KMS key.