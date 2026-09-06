

# Controlling access to policy store aliases
<a name="policy-store-aliases-control-access"></a>

Principals who manage policy store aliases must have permission to interact with those policy store aliases and, for some operations, the policy store that the policy store alias is associated with. You can provide these permissions using IAM policies.

The following sections describe the permissions required to create and manage policy store aliases.

## verifiedpermissions:CreatePolicyStoreAlias
<a name="alias-access-create"></a>

To create a policy store alias, the principal needs the following permissions for both the policy store alias and for the associated policy store.
+ `verifiedpermissions:CreatePolicyStoreAlias` for the policy store alias. Provide this permission in an IAM policy that is attached to the principal who is allowed to create the policy store alias.

  The following example policy statement specifies a particular policy store alias in a `Resource` element. But you can list multiple policy store alias ARNs or specify a policy store alias pattern, such as `"sample*"`. You can also specify a `Resource` value of `"*"` to allow the principal to create any policy store alias in the AWS account and Region.

  ```
  {
    "Sid": "IAMPolicyForCreateAlias",
    "Effect": "Allow",
    "Action": "verifiedpermissions:CreatePolicyStoreAlias",
    "Resource": "arn:aws:verifiedpermissions:us-east-1:123456789012:policy-store-alias/example-policy-store"
  }
  ```
+ `verifiedpermissions:CreatePolicyStoreAlias` for the associated policy store. This permission must be provided in an IAM policy.

  ```
  {
    "Sid": "PolicyStorePermissionForAlias",
    "Effect": "Allow",
    "Action": "verifiedpermissions:CreatePolicyStoreAlias",
    "Resource": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111"
  }
  ```

## verifiedpermissions:GetPolicyStoreAlias
<a name="alias-access-get"></a>

To get details about a specific policy store alias, the principal must have `verifiedpermissions:GetPolicyStoreAlias` permission for the policy store alias in an IAM policy.

The following example policy statement gives the principal permission to get a specific policy store alias.

```
{
  "Sid": "IAMPolicyForGetAlias",
  "Effect": "Allow",
  "Action": "verifiedpermissions:GetPolicyStoreAlias",
  "Resource": "arn:aws:verifiedpermissions:us-east-1:123456789012:policy-store-alias/example-policy-store"
}
```

## verifiedpermissions:ListPolicyStoreAliases
<a name="alias-access-view"></a>

To list policy store aliases in the AWS account and Region, the principal must have `verifiedpermissions:ListPolicyStoreAliases` permission in an IAM policy. Because this policy is not related to any particular policy store or policy store alias resource, the value of the resource element in the policy must be `"*"`.

For example, the following IAM policy statement gives the principal permission to list all policy store aliases in the AWS account.

```
{
  "Sid": "IAMPolicyForListingAliases",
  "Effect": "Allow",
  "Action": "verifiedpermissions:ListPolicyStoreAliases",
  "Resource": "*"
}
```

## verifiedpermissions:DeletePolicyStoreAlias
<a name="alias-access-delete"></a>

To delete a policy store alias, the principal needs permission for just the policy store alias.

**Note**  
Deleting a policy store alias has no effect on the associated policy store, although applications that reference the policy store alias will receive errors. If you mistakenly delete a policy store alias, you can recreate it after the 24-hour reservation period.

The principal needs `verifiedpermissions:DeletePolicyStoreAlias` permission for the policy store alias. Provide this permission in an IAM policy attached to the principal who is allowed to delete the policy store alias.

The following example policy statement specifies the policy store alias in a `Resource` element. But you can list multiple policy store alias ARNs or specify a policy store alias pattern, such as `"sample*"`. You can also specify a `Resource` value of `"*"` to allow the principal to delete any policy store alias in the AWS account and Region.

```
{
  "Sid": "IAMPolicyForDeleteAlias",
  "Effect": "Allow",
  "Action": "verifiedpermissions:DeletePolicyStoreAlias",
  "Resource": "arn:aws:verifiedpermissions:us-east-1:123456789012:policy-store-alias/example-policy-store"
}
```

## Limiting Policy store alias Permissions
<a name="alias-access-limiting"></a>

You can use a policy store alias to reference a policy store in any operation that accepts a `policyStoreId` field as input. When you do, Amazon Verified Permissions authorizes `verifiedpermissions:GetPolicyStoreAlias` against the policy store alias and the requested operation against the associated policy store.

For example, if the `IsAuthorized` operation is performed using a policy store alias, the principal needs both:
+ `verifiedpermissions:GetPolicyStoreAlias` permission for the policy store alias
+ `verifiedpermissions:IsAuthorized` permission for the associated policy store

The following example policy grants permission to call `IsAuthorized` using a specific policy store alias.

```
{
  "Sid": "IAMPolicyForAliasUsage",
  "Effect": "Allow",
  "Action": "verifiedpermissions:GetPolicyStoreAlias",
  "Resource": "arn:aws:verifiedpermissions:us-east-1:123456789012:policy-store-alias/example-policy-store"
},
{
  "Sid": "IAMPolicyForPolicyStoreOperation",
  "Effect": "Allow",
  "Action": "verifiedpermissions:IsAuthorized",
  "Resource": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111"
}
```

To limit which policy store aliases a principal can use, restrict the `verifiedpermissions:GetPolicyStoreAlias` permission. For example, the following policy allows the principal to use any policy store alias except those beginning with `Restricted`.

```
{
  "Sid": "IAMPolicyForAliasAllow",
  "Effect": "Allow",
  "Action": "verifiedpermissions:GetPolicyStoreAlias",
  "Resource": "arn:aws:verifiedpermissions:us-east-1:123456789012:policy-store-alias/*"
},
{
  "Sid": "IAMPolicyForAliasDeny",
  "Effect": "Deny",
  "Action": "verifiedpermissions:GetPolicyStoreAlias",
  "Resource": "arn:aws:verifiedpermissions:us-east-1:123456789012:policy-store-alias/Restricted*"
}
```