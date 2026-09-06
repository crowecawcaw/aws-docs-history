

# Retrieving Amazon Verified Permissions policy store aliases
<a name="policy-store-aliases-retrieve"></a>

You can retrieve information about policy store aliases using the `GetPolicyStoreAlias` operation to get details about a specific policy store alias, or the `ListPolicyStoreAliases` operation to list all policy store aliases in your AWS account and Region.

## Getting a policy store alias
<a name="policy-store-aliases-get"></a>

Use the `GetPolicyStoreAlias` operation to retrieve details about a specific policy store alias, including the associated policy store ID.

------
#### [ AWS CLI ]

**To retrieve details about a policy store alias**  
You can retrieve a policy store alias by using the [GetPolicyStoreAlias](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStoreAlias.html) operation. The following example retrieves details for a policy store alias with the name `example-policy-store`.

```
$ aws verifiedpermissions get-policy-store-alias \
    --alias-name policy-store-alias/example-policy-store
{
    "aliasName": "policy-store-alias/example-policy-store",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "aliasArn": "arn:aws:verifiedpermissions:us-west-2:123456789012:policy-store-alias/example-policy-store",
    "createdAt": "2024-01-15T12:30:00.000000+00:00",
    "state": "Active"
}
```

------

## Listing policy store aliases
<a name="policy-store-aliases-list"></a>

Use the `ListPolicyStoreAliases` operation to list all policy store aliases in your AWS account and Region. You can use the `filter` parameter to list only policy store aliases associated with a specific policy store.

------
#### [ AWS CLI ]

**To list all policy store aliases**  
You can list policy store aliases by using the [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html) operation. The following example lists all policy store aliases owned by the 123456789012 AWS account in the us-west-2 Region.

```
$ aws verifiedpermissions list-policy-store-aliases
{
    "policyStoreAliases": [
        {
            "aliasName": "policy-store-alias/example-policy-store",
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "aliasArn": "arn:aws:verifiedpermissions:us-west-2:123456789012:policy-store-alias/example-policy-store",
            "createdAt": "2024-01-15T12:30:00.000000+00:00",
            "state": "Active"
        },
        {
            "aliasName": "policy-store-alias/example-policy-store-2",
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "aliasArn": "arn:aws:verifiedpermissions:us-west-2:123456789012:policy-store-alias/example-policy-store-2",
            "createdAt": "2024-01-16T09:15:00.000000+00:00",
            "state": "Active"
        },
        {
            "aliasName": "policy-store-alias/example-policy-store-3",
            "policyStoreId": "PSEXAMPLEabcdefg222222",
            "aliasArn": "arn:aws:verifiedpermissions:us-west-2:123456789012:policy-store-alias/example-policy-store-3",
            "createdAt": "2024-01-17T14:45:00.000000+00:00",
            "state": "Active"
        }
    ]
}
```

**To list policy store aliases for a specific policy store**  
Use the `filter` parameter to list only aliases associated with a specific policy store.

```
$ aws verifiedpermissions list-policy-store-aliases \
    --filter '{"policyStoreId": "PSEXAMPLEabcdefg111111"}'
{
    "policyStoreAliases": [
        {
            "aliasName": "policy-store-alias/example-policy-store",
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "aliasArn": "arn:aws:verifiedpermissions:us-west-2:123456789012:policy-store-alias/example-policy-store",
            "createdAt": "2024-01-15T12:30:00.000000+00:00",
            "state": "Active"
        },
        {
            "aliasName": "policy-store-alias/example-policy-store-2",
            "policyStoreId": "PSEXAMPLEabcdefg111111",
            "aliasArn": "arn:aws:verifiedpermissions:us-west-2:123456789012:policy-store-alias/example-policy-store-2",
            "createdAt": "2024-01-16T09:15:00.000000+00:00",
            "state": "Active"
        }
    ]
}
```

------