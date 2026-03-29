# Deleting Amazon Verified Permissions policy store aliases

You can delete a policy store alias when it is no longer needed. Deleting a policy store alias does not affect the associated policy store. Deleting a policy store deletes all policy store aliases associated with that policy store.

After you delete a policy store alias, the policy store alias name is reserved for 24 hours and cannot be reused during this period.

AWS CLI

###### To delete a policy store alias

You can delete a policy store alias by using the [DeletePolicyStoreAlias](../apireference/API_DeletePolicyStoreAlias.md "../apireference/API_DeletePolicyStoreAlias.md")
operation. The following example deletes a policy store alias with the name `example-policy-store`.

```
`$` `aws verifiedpermissions delete-policy-store-alias \
 --alias-name policy-store-alias/example-policy-store`
```
