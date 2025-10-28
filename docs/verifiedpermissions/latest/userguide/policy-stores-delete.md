# Deleting policy stores

You can delete Amazon Verified Permissions policy stores using the AWS Management Console or the AWS CLI. Deleting a
policy store permanently deletes the schema and any policies in the policy store.

Deletion protection prevents accidental deletion of a policy store. Deletion protection is
enabled on all new policy stores created through the AWS Management Console. By contrast, it is disabled
for all policy stores created through an API or SDK call.

You may want to delete policy stores for the following reasons:

- You have reached the quota of available policy stores in a given Region. For more
  information, see [Quotas for resources](quotas.md#quotas-resources "quotas.md#quotas-resources").
- You're no longer supporting a tenant in a multi-tenant application and, therefore,
  no longer need that policy store.

AWS Management Console

###### To delete a policy store

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose
   **Settings**.
3. Choose **Delete this policy store**.
4. Type `delete` in the text box and choose
   **Delete**.

###### Note

If deletion protection is enabled, you'll need to disable it
before you can choose **Delete**. To disable it, select
**Disable deletion protection**.

AWS CLI

###### To delete a policy store

You can delete a policy store by using the `delete-policy-store`
operation, replacing `PSEXAMPLEabcdefg111111` with the policy store ID you want to delete.

```
`$` `aws verifiedpermissions delete-policy-store \
 --policy-store-id `PSEXAMPLEabcdefg111111``
```

If successful, this command produces no output.

###### Note

If deletion protection is enabled for this policy store, you must first
run the `update-policy-store` operation and disable deletion
protection.

```
aws verifiedpermissions update-policy-store \
    --deletion-protection "DISABLED" \
    --policy-store-id PSEXAMPLEabcdefg111111
```
