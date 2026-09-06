

# Troubleshooting common ABAC errors for DynamoDB tables and indexes
<a name="abac-troubleshooting"></a>

This topic provides troubleshooting advice for common errors and issues that you might encounter while implementing ABAC in DynamoDB tables or indexes.

## Service-specific condition keys in policies result in an error
<a name="abac-troubleshooting-service-specific-keys"></a>

Service-specific condition keys aren't considered as valid condition keys. If you've used such keys in your policies, these will result in an error. To fix this issue, you must replace the service-specific condition keys with an appropriate [condition key to implement ABAC](attribute-based-access-control.md#condition-keys-implement-abac) in DynamoDB.

For example, say that you've used the `dynamodb:ResourceTag` condition key in an [inline policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#inline-policies) that performs the [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) request. Imagine that the request fails with an `AccessDeniedException`. The following example shows the erroneous inline policy with the `dynamodb:ResourceTag` condition key.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem"
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/*",
            "Condition": {
                "StringEquals": {
                    "dynamodb:ResourceTag/Owner": "John"
                }
            }
        }
    ]
}
```

------

To fix this issue, replace the `dynamodb:ResourceTag` condition key with `aws:ResourceTag`, as shown in the following example.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem"
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/Owner": "John"
                }
            }
        }
    ]
}
```

------

## Unable to opt out of ABAC
<a name="abac-troubleshooting-unable-opt-out"></a>

If ABAC was enabled for your account through Support, you won't be able to opt out of ABAC through the DynamoDB console. To opt out, contact [Support](https://console.aws.amazon.com/support).

You can opt out of ABAC yourself *only if* the following are true:
+ You used the self-service way of [opting in through the DynamoDB console](abac-enable-ddb.md#abac-enable-console).
+ You're opting out within seven calendar days of opting in.