

# Creating Amazon Verified Permissions policy store aliases
<a name="policy-store-aliases-create"></a>

You can create a policy store alias to reference a policy store using a friendly name. The name of a policy store alias must be unique per AWS account and Region. Policy store aliases may only be associated with policy stores that are owned by the same AWS account and active in the same Region as the policy store alias. Policy store aliases are separate resources with their own ARNs and IAM authorization.

By default, only 10 policy store aliases can be associated with the same policy store.

**Note**  
`CreatePolicyStoreAlias` is idempotent. If you call the `CreatePolicyStoreAlias` operation with a policy store alias name and policy store ID that match an existing policy store alias, the `CreatePolicyStoreAlias` operation succeeds and returns the existing policy store alias. However, if you call the `CreatePolicyStoreAlias` operation with an existing policy store alias name but a different policy store ID, the operation returns a `ConflictException`.

------
#### [ AWS CLI ]

**To create a policy store alias**  
You can create a policy store alias by using the [CreatePolicyStoreAlias](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStoreAlias.html) operation. The following example creates a policy store alias with the name `example-policy-store`.

```
$ aws verifiedpermissions create-policy-store-alias \
    --alias-name policy-store-alias/example-policy-store \
    --policy-store-id PSEXAMPLEabcdefg111111
{
    "aliasName": "policy-store-alias/example-policy-store",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "aliasArn": "arn:aws:verifiedpermissions:us-west-2:123456789012:policy-store-alias/example-policy-store",
    "createdAt": "2024-01-15T12:30:00.000000+00:00"
}
```

------