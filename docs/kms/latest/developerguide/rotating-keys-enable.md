# Enable automatic key rotation

By default, when you enable _automatic key rotation_
for a KMS key, AWS KMS generates new cryptographic material for the KMS key every
year. You can also specify a custom [rotation-period](rotate-keys.md#rotation-period "rotate-keys.md#rotation-period") to define the
number of days after you enable automatic key rotation that AWS KMS will rotate your key
material, and the number of days between each automatic rotation thereafter.

Automatic key rotation has the following benefits:

- The properties of the KMS key, including its [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id"), [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN"), region,
  policies, and permissions, do not change when the key is rotated.
- You do not need to change applications or aliases that refer to the key ID or
  key ARN of the KMS key.
- Rotating key material does not affect the use of the KMS key in any
  AWS service.
- After you enable key rotation, AWS KMS rotates the KMS key automatically on
  the next rotation date defined by your rotation period. You don't need to
  remember or schedule the update.
  You can enable automatic key rotation in the AWS KMS console or by using the [EnableKeyRotation](../APIReference/API_EnableKeyRotation.md "../APIReference/API_EnableKeyRotation.md") operation.
  To enable automatic key rotation, you need `kms:EnableKeyRotation`
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
**Enable**.

###### Note

If a KMS key is disabled or pending deletion, AWS KMS does not
rotate the key material and you cannot update the automatic key
rotation status or rotation period. Enable the KMS key or cancel
deletion to update the automatic key rotation configuration. For
details, see [How key rotation works](rotate-keys.md#rotate-keys-how-it-works "rotate-keys.md#rotate-keys-how-it-works") and [Key states of AWS KMS keys](key-state.md "key-state.md"). 8. (Optional) Type a rotation period between 90 and 2560 days. The
default value is 365 days. If you do not specify a custom rotation
period, AWS KMS will rotate the key material every year.

You can use the [kms:RotationPeriodInDays](conditions-kms.md#conditions-kms-rotation-period-in-days "conditions-kms.md#conditions-kms-rotation-period-in-days") condition key to limit the values
that principals can specify for the rotation period. 9. Choose **Save**.
You can use the [AWS Key Management Service (AWS KMS) API](../APIReference.md "../APIReference.md") to
enable automatic key rotation and view the current rotation status of any
customer managed key. These examples use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

The [EnableKeyRotation](../APIReference/API_EnableKeyRotation.md "../APIReference/API_EnableKeyRotation.md") operation enables automatic key rotation for the
specified KMS key. To identify the KMS key in this operation, use its [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") or [key
ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN"). By default, key rotation is disabled for customer managed keys.

You can use the [kms:RotationPeriodInDays](conditions-kms.md#conditions-kms-rotation-period-in-days "conditions-kms.md#conditions-kms-rotation-period-in-days") condition key to limit the values that
principals can specify for the `RotationPeriodInDays` parameter of an
`EnableKeyRotation` request.

The following example enables key rotation with a rotation period of 180 days
on the specified symmetric encryption KMS key and uses the [GetKeyRotationStatus](../APIReference/API_GetKeyRotationStatus.md "../APIReference/API_GetKeyRotationStatus.md") operation to see the result.

```
`$` `aws kms enable-key-rotation \
 --key-id `1234abcd-12ab-34cd-56ef-1234567890ab` \
 --rotation-period-in-days `180``

`$` `aws kms get-key-rotation-status --key-id `1234abcd-12ab-34cd-56ef-1234567890ab``
`{
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "KeyRotationEnabled": true,
 "RotationPeriodInDays": 180,
 "NextRotationDate": "2024-02-14T18:14:33.587000+00:00"
}`

```
