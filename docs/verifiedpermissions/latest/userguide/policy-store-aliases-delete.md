

# Deleting Amazon Verified Permissions policy store aliases
<a name="policy-store-aliases-delete"></a>

You can delete a policy store alias when it is no longer needed. Deleting a policy store alias does not affect the associated policy store. Deleting a policy store deletes all policy store aliases associated with that policy store.

Amazon Verified Permissions supports two deletion modes for policy store aliases:
+ **Soft delete** (default): The policy store alias enters a `PendingDeletion` state. The policy store alias name is reserved for 24 hours and cannot be reused during this period. During this period, `GetPolicyStoreAlias` returns the policy store alias with the `PendingDeletion` state. This is the default behavior when you don't specify a `deletionMode`, or when you specify `SoftDelete`.
+ **Hard delete**: The policy store alias is immediately deleted. The policy store alias name becomes available for reuse immediately. To perform a hard delete, specify `HardDelete` as the `deletionMode`.

## Soft deleting a policy store alias
<a name="policy-store-aliases-soft-delete"></a>

By default, deleting a policy store alias performs a soft delete. The policy store alias enters the `PendingDeletion` state and the policy store alias name is reserved for 24 hours.

------
#### [ AWS CLI ]

**To soft delete a policy store alias**  
You can soft delete a policy store alias by using the [DeletePolicyStoreAlias](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyStoreAlias.html) operation. The following example soft deletes a policy store alias with the name `example-policy-store`.

```
$ aws verifiedpermissions delete-policy-store-alias \
    --alias-name policy-store-alias/example-policy-store
```

You can also explicitly specify the soft delete mode.

```
$ aws verifiedpermissions delete-policy-store-alias \
    --alias-name policy-store-alias/example-policy-store \
    --deletion-mode SoftDelete
```

------

## Hard deleting a policy store alias
<a name="policy-store-aliases-hard-delete"></a>

To immediately delete a policy store alias, specify `HardDelete` as the `deletionMode`. A hard-deleted policy store alias does not enter the `PendingDeletion` state and the policy store alias name becomes available for reuse immediately.

If you hard delete a policy store alias that was previously soft deleted, the policy store alias is immediately deleted.

**Important**  
Amazon Verified Permissions is eventually consistent. If you hard delete a policy store alias and immediately recreate it to point to a different policy store, requests that reference the policy store alias may continue to resolve to the previously associated policy store for a short period of time. To avoid unexpected authorization results, allow time for the deletion to propagate before recreating a policy store alias with the same name.

------
#### [ AWS CLI ]

**To hard delete a policy store alias**  
You can hard delete a policy store alias by using the [DeletePolicyStoreAlias](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyStoreAlias.html) operation with the `deletion-mode` parameter set to `HardDelete`. The following example immediately deletes a policy store alias with the name `example-policy-store`.

```
$ aws verifiedpermissions delete-policy-store-alias \
    --alias-name policy-store-alias/example-policy-store \
    --deletion-mode HardDelete
```

------