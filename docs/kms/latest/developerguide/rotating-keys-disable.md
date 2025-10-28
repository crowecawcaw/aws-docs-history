# Disable automatic key rotation

After enabling automatic key rotation on a customer managed key, you can choose to disable
it at any time.

If you disable automatic key rotation, the KMS key
continues to use the version of the key material it was using when rotation was
disabled. If you enable automatic key rotation again, AWS KMS rotates the key material
based on the new rotation-enable date.

Disabling automatic rotation does not impact your ability to [perform on-demand rotations](rotating-keys-on-demand.md "rotating-keys-on-demand.md"), nor does it
cancel any in progress on-demand rotations.

You can disable automatic key rotation in the AWS KMS console or by using the [DisableKeyRotation](../APIReference/API_DisableKeyRotation.md "../APIReference/API_DisableKeyRotation.md") operation.
To disable automatic key rotation, you need `kms:DisableKeyRotation`
permissions. For more information about AWS KMS permissions, see the [Permissions reference](kms-api-permissions-reference.md "kms-api-permissions-reference.md").

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**. (You cannot enable or disable rotation of
   AWS managed keys. They are automatically rotated every year.)
4. Choose the alias or key ID of a KMS key.
5. Choose the **Key rotation** tab.

The **Key rotation** tab appears only on the detail
page of symmetric encryption KMS keys with key material that AWS KMS
generated (the **Origin** is
**AWS_KMS**), including [multi-Region](rotate-keys.md#multi-region-rotate "rotate-keys.md#multi-region-rotate") symmetric
encryption KMS keys.

You cannot automatically rotate asymmetric KMS keys, HMAC
KMS keys, KMS keys with [imported key
material](importing-keys.md "importing-keys.md"), or KMS keys in [custom key stores](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview").
However, you can [rotate them
manually](rotate-keys-manually.md "rotate-keys-manually.md"). 6. In the **Automatic key rotation** section, choose
**Edit**. 7. For **Key rotation**, select
**Disable**.

###### Note

If a KMS key is disabled or pending deletion, AWS KMS does not
rotate the key material and you cannot update the automatic key
rotation status or rotation period. Enable the KMS key or cancel
deletion to update the automatic key rotation configuration. For
details, see [How key rotation works](rotate-keys.md#rotate-keys-how-it-works "rotate-keys.md#rotate-keys-how-it-works") and [Key states of AWS KMS keys](key-state.md "key-state.md"). 8. Choose **Save**.
You can use the [AWS Key Management Service (AWS KMS) API](../APIReference.md "../APIReference.md") to
disable automatic key rotation and view the current rotation status of any
customer managed key. This example uses the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

The [DisableKeyRotation](../APIReference/API_DisableKeyRotation.md "../APIReference/API_DisableKeyRotation.md") operation disables automatic key rotation. To identify the KMS key
in this operation, use its [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") or [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN"). By default, key rotation is
disabled for customer managed keys.

The following example disables automatic key rotation on the specified
symmetric encryption KMS key and uses the [GetKeyRotationStatus](../APIReference/API_GetKeyRotationStatus.md "../APIReference/API_GetKeyRotationStatus.md") operation to see the result.

```
`$` `aws kms disable-key-rotation --key-id `1234abcd-12ab-34cd-56ef-1234567890ab``

`$` `aws kms get-key-rotation-status --key-id `1234abcd-12ab-34cd-56ef-1234567890ab``
`{
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "KeyRotationEnabled": false
}`

```
