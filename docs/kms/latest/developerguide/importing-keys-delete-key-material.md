# Delete imported key material

You can delete the imported key material from a KMS key at any time. Also, when imported
key material with an expiration date expires, AWS KMS deletes the key material. In either case,
when the key material is deleted, the [key state](key-state.md "key-state.md") of the
KMS key changes to _Pending import_, and the KMS key can't be used in any
cryptographic operations.

Symmetric encryption keys can have multiple key materials associated with them and the
deletion or expiration of any key material in a state other than `PENDING_ROTATION`
changes the key state to _Pending import_. For these keys, KMS assigns a
unique identifier to each key material. You can use the [ListKeyRotations](../APIReference/API_ListKeyRotations.md "../APIReference/API_ListKeyRotations.md") API to view these key
material identifiers. You can delete a specific key material by specifying its identifier using
the `key-material-id` parameter in the [DeleteImportedKeyMaterial](../APIReference/API_DeleteImportedKeyMaterial.md "../APIReference/API_DeleteImportedKeyMaterial.md")
API.

###### Considerations for multi-Region keys

- When you delete the key material of a primary Region key that is in
  `PENDING_ROTATION` or `PENDING_MULTI_REGION_IMPORT_AND_ROTATION`
  state, you'll also be deleting the key materials for the replica Region keys.
- If you delete the key material of a replica Region key, the primary Region key and
  other replica Region keys remain unchanged.

###### Warning

The `key-material-id` parameter is optional and if you do not specify it, AWS KMS
will delete the current key material.

Along with disabling the KMS key and withdrawing permissions, deleting key material can be
used as a strategy to quickly, but temporarily, halt the use of the KMS key. In contrast,
scheduling the deletion of a KMS key with imported key material also quickly halts the use of
the KMS key. However, if the deletion is not canceled during the waiting period, the
KMS key, associated key materials, and all key metadata are permanently deleted. For details,
see [Deleting KMS keys with imported key material](deleting-keys.md#import-delete-key "deleting-keys.md#import-delete-key").

To delete key material, you can use the AWS KMS console or the [DeleteImportedKeyMaterial](../APIReference/API_DeleteImportedKeyMaterial.md "../APIReference/API_DeleteImportedKeyMaterial.md") API
operation. AWS KMS records an entry in your AWS CloudTrail log when you [delete imported key material](ct-deleteimportedkeymaterial.md "ct-deleteimportedkeymaterial.md") and when [AWS KMS deletes expired key material](ct-deleteexpiredkeymaterial.md "ct-deleteexpiredkeymaterial.md").

**How deleting key material
affects AWS services**

When you delete any key material, the KMS key becomes unusable right away (subject
to eventual consistency). However, resources encrypted with [data
keys](data-keys.md "data-keys.md") protected by the KMS key are not affected until the KMS key is used
again, such as to decrypt the data key. This issue affects AWS services, many of which
use data keys to protect your resources. For details, see [How unusable KMS keys affect data keys](unusable-kms-keys.md "unusable-kms-keys.md").

You can use the AWS KMS console to delete key material.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Do one of the following:
   - Select the check box for a KMS key with imported key material. Choose
     **Key actions**, **Delete key material**. For
     symmetric encryption keys that have multiple key materials associated with them,
     this will delete the current key material.
   - For symmetric encryption KMS keys with imported key material,
     choose the alias or key ID of a KMS key. Choose the **Key material and
     rotations** tab. The key material table will list all of the key
     materials associated with the key. Choose **Delete key material**
     from the **Actions** menu in the row corresponding to the key
     material you want to delete.

5. Confirm that you want to delete the key material and then choose **Delete
   key material**. The KMS key's status, which corresponds to its [key state](key-state.md "key-state.md"), changes to **Pending import**.
   If the deleted key material was in `PENDING_ROTATION` state, there is no
   change to the KMS key's status.
   To use the [AWS KMS API](../APIReference.md "../APIReference.md") to delete key material, send a
   [DeleteImportedKeyMaterial](../APIReference/API_DeleteImportedKeyMaterial.md "../APIReference/API_DeleteImportedKeyMaterial.md") request. The following example shows how to do this
   with the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").

Replace `1234abcd-12ab-34cd-56ef-1234567890ab` with the key ID of
the KMS key whose key material you want to delete. You can use the KMS key's key ID or
ARN but you cannot use an alias for this operation. The following command deletes the
current key material which may be the only key material associated with the key.

```
`$` `aws kms delete-imported-key-material --key-id `1234abcd-12ab-34cd-56ef-1234567890ab``
```

To delete a specific key material, specify the key material identified using the
`key-material-id` parameter. Replace
`123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0` with the identifier
of the key material you want to delete.

```
`$` `aws kms delete-imported-key-material --key-id `1234abcd-12ab-34cd-56ef-1234567890ab` \
 --key-material-id `123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0``

```
