

# Amazon Verified Permissions policy store aliases
<a name="policy-store-aliases"></a>

A policy store alias is a friendly name for a policy store. For example, policy store aliases let you refer to a policy store using `policy-store-alias/example-policy-store` instead of `PSEXAMPLEabcdefg111111`. Policy store aliases can be used in any Verified Permissions operation that accepts a `policyStoreId` input parameter.

You can create a policy store alias for a policy store by using the `CreatePolicyStoreAlias` API or by using the `AWS::VerifiedPermissions::PolicyStoreAlias` CloudFormation resource.

The Amazon Verified Permissions API provides full control of policy store aliases in each AWS account and Region. The API includes operations to create a policy store alias (`CreatePolicyStoreAlias`), view policy store alias names and policy store alias ARNs (`GetPolicyStoreAlias`, `ListPolicyStoreAliases`), and delete a policy store alias (`DeletePolicyStoreAlias`).

**Topics**
+ [Properties of policy store aliases](#alias-properties)
+ [Creating Amazon Verified Permissions policy store aliases](policy-store-aliases-create.md)
+ [Retrieving Amazon Verified Permissions policy store aliases](policy-store-aliases-retrieve.md)
+ [Deleting Amazon Verified Permissions policy store aliases](policy-store-aliases-delete.md)
+ [Using Amazon Verified Permissions policy store aliases in API operations](policy-store-aliases-using.md)
+ [Controlling access to policy store aliases](policy-store-aliases-control-access.md)

## Properties of policy store aliases
<a name="alias-properties"></a>

How policy store aliases work in Amazon Verified Permissions.

**A policy store alias is an independent AWS resource**  
A policy store alias is not a property of a policy store. The actions that you take on the policy store alias don't affect its associated policy store. You can delete the policy store alias without any effect on the associated policy store. If you delete a policy store, all policy store aliases associated with that policy store are also deleted.

Each policy store alias has an Amazon Resource Name (ARN) that uniquely identifies the policy store alias. If you specify a policy store alias as the resource in an IAM policy, the policy refers to the policy store alias, not to the associated policy store.

**Each policy store alias has two formats**  
When you create a policy store alias, you specify the policy store alias name. Amazon Verified Permissions creates the policy store alias ARN for you.
+ A policy store alias ARN is an Amazon Resource Name (ARN) that uniquely identifies the policy store alias.

  ```
  # Alias ARN
  arn:aws:verifiedpermissions:us-east-1:123456789012:policy-store-alias/example-policy-store
  ```
+ A policy store alias name that is unique in the AWS account and Region. In the Amazon Verified Permissions API, the policy store alias name is always prefixed by `policy-store-alias/`.

  ```
  # Alias name
  policy-store-alias/example-policy-store
  ```

**Policy store aliases are not secret**  
Policy store aliases may be displayed in plaintext in CloudTrail logs and other output. Do not include confidential or sensitive information in the policy store alias name.

**Each policy store alias is associated with one policy store at a time**  
The policy store alias and its associated policy store must belong to the same AWS account and Region. You can associate a policy store alias with any policy store in the same AWS account and Region.

For example, this `ListPolicyStoreAliases` output shows that the `example-policy-store` policy store alias is associated with exactly one target policy store, which is represented by the `policyStoreId` property.

```
{
    "aliasName": "policy-store-alias/example-policy-store",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "aliasArn": "arn:aws:verifiedpermissions:us-west-2:123456789012:policy-store-alias/example-policy-store",
    "createdAt": "2024-01-15T12:30:00.000000+00:00",
    "state": "Active"
}
```

**Multiple aliases can be associated with the same policy store**  
For example, you can associate the `example-policy-store` and `example-policy-store-2` aliases with the same policy store.

```
[
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
```

**A policy store alias must be unique in an AWS account and Region**  
For example, you can have only one policy store alias with the name `example-policy-store` in each AWS account and Region. Policy store aliases are case-sensitive. You cannot change a policy store alias name. However, you can delete the policy store alias and create a new policy store alias with the desired name after the 24-hour reservation period expires.

You can create policy store aliases with the same name in different Regions. Each policy store alias will have a unique ARN. If your code refers to a policy store alias name like `policy-store-alias/example-policy-store`, you can run it in multiple Regions. In each Region, it uses a different policy store.

**Policy store aliases support soft deletes and hard deletes**  
By default, when a policy store alias is deleted, it is soft deleted. The policy store alias name is reserved for a period of 24 hours. If you attempt to create a policy store alias with the same name during this period, the request will be rejected. During this period, `GetPolicyStoreAlias` returns the policy store alias with the `PendingDeletion` state. You can also hard delete a policy store alias by specifying `HardDelete` as the `deletionMode`. A hard-deleted policy store alias is immediately deleted and the policy store alias name becomes available for reuse immediately. For more information, see [Deleting Amazon Verified Permissions policy store aliases](policy-store-aliases-delete.md).

**You can use aliases to identify policy stores**  
You can use a policy store alias to identify a policy store in all operations that accept a `policyStoreId` (for example, `IsAuthorized`). In such cases, the policy store alias name must be prefixed with `policy-store-alias/`. Policy store aliases cannot be used to identify a policy store for the `DeletePolicyStore` operation.

You cannot use a policy store alias name or policy store alias ARN to identify a policy store in the `Resource` element of an IAM policy. To control access to a policy store when it is referenced through a policy store alias, see [Controlling access to policy store aliases](policy-store-aliases-control-access.md).