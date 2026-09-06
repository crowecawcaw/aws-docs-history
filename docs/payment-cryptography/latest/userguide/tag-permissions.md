

# Controlling access to tags
<a name="tag-permissions"></a>

To add, view, and delete tags by using the API, principals need tagging permissions in IAM policies.

You can also limit these permissions by using AWS global condition keys for tags. In AWS Payment Cryptography, these conditions can control access to tagging operations, such as [TagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UntagResource.html).

For example policies and more information, see [Controlling Access Based on Tag Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-tag-keys) in the *IAM User Guide*.

Permissions to create and manage tags work as follows.

**payment-cryptography:TagResource**  
Allows principals to add or edit tags. To add tags while creating a key, the principal must have permission in an IAM policy that isn't restricted to particular keys.

**payment-cryptography:ListTagsForResource**  
Allows principals to view tags on keys.

**payment-cryptography:UntagResource**  
Allows principals to delete tags from keys.

## Tag permissions in policies
<a name="tag-permission-examples"></a>

You can provide tagging permissions in a key policy or IAM policy. For example, the following example key policy gives select users tagging permission on the key. It gives all users who can assume the example Administrator or Developer roles permission to view tags.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Id": "example-key-policy",
  "Statement": [
    { 
      "Sid": "EnableIAMUserPermissions",
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::{{111122223333}}:root"},
      "Action": "payment-cryptography:*",
      "Resource": "*"
    },
    {
      "Sid": "AllowAllTaggingPermissions",
      "Effect": "Allow",
      "Principal": {"AWS": [
        "arn:aws:iam::{{111122223333}}:user/LeadAdmin",
        "arn:aws:iam::{{111122223333}}:user/SupportLead"
      ]},
      "Action": [
        "payment-cryptography:TagResource",
        "payment-cryptography:ListTagsForResource",
        "payment-cryptography:UntagResource"
      ],
      "Resource": "*"
    },
    {
      "Sid": "Allow roles to view tags",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::{{111122223333}}:role/Administrator",
          "arn:aws:iam::{{111122223333}}:role/Developer"
        ]
      },
      "Action": "payment-cryptography:ListTagsForResource",
      "Resource": "*"
    }
  ]
}
```

------

To give principals tagging permission on multiple keys, you can use an IAM policy. For this policy to be effective, the key policy for each key must allow the account to use IAM policies to control access to the key.

For example, the following IAM policy allows the principals to create keys. It also allows them to create and manage tags on all keys in the specified account. This combination allows the principals to use the tags parameter of the [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) operation to add tags to a key while they are creating it. 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "IAMPolicyCreateKeys",
      "Effect": "Allow",
      "Action": "payment-cryptography:CreateKey",
      "Resource": "*"
    },
    {
      "Sid": "IAMPolicyTags",
      "Effect": "Allow",
      "Action": [
        "payment-cryptography:TagResource",
        "payment-cryptography:UntagResource",
        "payment-cryptography:ListTagsForResource"
      ],
      "Resource": "arn:aws:payment-cryptography:*:{{111122223333}}:key/*"
    }    
  ]
}
```

------

## Limiting tag permissions
<a name="tag-permissions-conditions"></a>

You can limit tagging permissions by using policy conditions. The following policy conditions can be applied to the `payment-cryptography:TagResource` and `payment-cryptography:UntagResource` permissions. For example, you can use the `aws:RequestTag/tag-key` condition to allow a principal to add only particular tags, or prevent a principal from adding tags with particular tag keys.
+ [aws:RequestTag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)
+ [aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (IAM policies only)
+ [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tag-keys)

As a best practice when you use tags to control access to keys, use the `aws:RequestTag/tag-key` or `aws:TagKeys` condition key to determine which tags (or tag keys) are allowed.

For example, the following IAM policy is similar to the previous one. However, this policy allows the principals to create tags (`TagResource`) and delete tags `UntagResource` only for tags with a `Project` tag key.

Because `TagResource` and `UntagResource` requests can include multiple tags, you must specify a `ForAllValues` or `ForAnyValue` set operator with the [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys) condition. The `ForAnyValue` operator requires that at least one of the tag keys in the request matches one of the tag keys in the policy. The `ForAllValues` operator requires that all of the tag keys in the request match one of the tag keys in the policy. The `ForAllValues` operator also returns `true` if there are no tags in the request, but TagResource and UntagResource fail when no tags are specified. For details about the set operators, see [Use multiple keys and values](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_multi-value-conditions.html#reference_policies_multi-key-or-value-conditions) in the *IAM User Guide*.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "IAMPolicyCreateKey",
      "Effect": "Allow",
      "Action": "payment-cryptography:CreateKey",
      "Resource": "*"
    },
    {
      "Sid": "IAMPolicyViewAllTags",
      "Effect": "Allow",
      "Action": "payment-cryptography:ListTagsForResource",
      "Resource": "arn:aws:payment-cryptography:*:{{111122223333}}:key/*"
    },
    {
      "Sid": "IAMPolicyManageTags",
      "Effect": "Allow",
      "Action": [
        "payment-cryptography:TagResource",
        "payment-cryptography:UntagResource"
      ],
      "Resource": "arn:aws:payment-cryptography:*:{{111122223333}}:key/*",
      "Condition": {
          "ForAllValues:StringEquals": {"aws:TagKeys": "Project"}
      }
    }
  ]
}
```

------