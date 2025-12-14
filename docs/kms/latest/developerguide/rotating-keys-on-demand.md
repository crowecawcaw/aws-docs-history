# Perform on-demand key

rotation

You can perform on-demand rotation of the key material in customer managed KMS keys,
regardless of whether or not automatic key rotation is enabled. Disabling automatic
rotation ([DisableKeyRotation](../APIReference/API_DisableKeyRotation.md "../APIReference/API_DisableKeyRotation.md")) does not impact your ability to perform on-demand
rotations, nor does it cancel any in progress on-demand rotations. On-demand rotations
do not change existing automatic rotation schedules. For example, consider a KMS key
that has automatic key rotation enabled with a rotation period of 730 days. If the key
is scheduled to automatically rotate on April 14, 2024, and you perform an on-demand
rotation on April 10, 2024, the key will automatically rotate, as scheduled, on April
14, 2024 and every 730 days thereafter.

You can perform on-demand key rotation a maximum of 10 times per KMS key. You can
use the AWS KMS console to view the number of remaining on-demand rotations available for
a KMS key.

On-demand key rotation is supported only on [symmetric
encryption KMS keys](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks"). You cannot perform on-demand rotation of [asymmetric KMS keys](symmetric-asymmetric.md "symmetric-asymmetric.md"), [HMAC KMS keys](hmac.md "hmac.md"), or KMS keys in a [custom
key store](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview"). To perform on-demand rotation of a set of related [multi-Region keys](rotate-keys.md#multi-region-rotate "rotate-keys.md#multi-region-rotate"), invoke the on-demand
rotation on the primary key.

Authorized users with `kms:RotateKeyOnDemand` and
`kms:GetKeyRotationStatus` permissions can use the AWS KMS console and the
AWS KMS API to initiate on-demand key rotation and view the key rotation status. Use
[ListKeyRotations](../APIReference/API_ListKeyRotations.md "../APIReference/API_ListKeyRotations.md") to view
completed rotations for a KMS key.

###### Topics

- [Initiating on-demand key rotation
  (console)](#rotate-on-demand-console "#rotate-on-demand-console")
- [Initiating on-demand key rotation
  (AWS KMS API)](#rotate-on-demand-api "#rotate-on-demand-api")

## Initiating on-demand key rotation

(console)

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**. (You cannot perform on-demand rotation of
   AWS managed keys. They are automatically rotated every year.)
4. Choose the alias or key ID of a KMS key.
5. Choose the **Key material and rotations** tab.

The **Key material and rotations** tab appears only on
the detail page of symmetric encryption KMS keys that support automatic or
on-demand rotation. This includes KMS keys with key material that AWS KMS
generated (**AWS_KMS** origin) and KMS keys with imported
key material (**EXTERNAL** origin)

You cannot perform on-demand rotation of asymmetric KMS keys, HMAC
KMS keys, or KMS keys in [custom key
stores](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview"). However, you can [rotate them manually](rotate-keys-manually.md "rotate-keys-manually.md"). 6. Choose **Rotate now**. For symmetric encryption keys with
imported key material, the **Rotate now** option is
available only if you have previously [imported new key material](importing-keys-import-key-material.md#import-new-key-material "importing-keys-import-key-material.md#import-new-key-material") and
it is in **Pending rotation** state.

###### Note

For multi-Region keys, only the primary Region key can be
rotated. 7. Read and consider the warning and the information about the number of
remaining on-demand rotations for the key. You will also see information
such as the ID, description, and expiration time of the key material that
will become current after rotation. If you decide that you do not want to
proceed with the on-demand rotation, choose
**Cancel**. 8. Choose **Rotate key** to confirm on-demand
rotation.

###### Note

On-demand rotation is subject to the same eventual consistency effects
as other AWS KMS management operations. There might be a slight delay
before the new key material is available throughout AWS KMS. The banner at
the top of the console notifies you when the on-demand rotation is
complete.

## Initiating on-demand key rotation

(AWS KMS API)

You can use the [AWS Key Management Service (AWS KMS) API](../APIReference.md "../APIReference.md") to
initiate on-demand key rotation, and view the current rotation status of any
customer managed key. This example uses the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

The [RotateKeyOnDemand](../APIReference/API_RotateKeyOnDemand.md "../APIReference/API_RotateKeyOnDemand.md")
operation immediately initiates on-demand key rotation for the specified KMS key.
To identify the KMS key in these operations, use its [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") or [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN").

The following example initiates on-demand key rotation on the specified symmetric
encryption KMS key and uses the [GetKeyRotationStatus](../APIReference/API_GetKeyRotationStatus.md "../APIReference/API_GetKeyRotationStatus.md")
operation to verify that the on-demand rotation is in progress. The
`OnDemandRotationStartDate` in the
`kms:GetKeyRotationStatus` response identifies the date and time that
an in progress on-demand rotation was initiated. In this example, the KMS key also
has automatic rotation enabled with a period of 365 days.

```
`$` `aws kms rotate-key-on-demand --key-id `1234abcd-12ab-34cd-56ef-1234567890ab``
`{
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"
}`

`$` `aws kms get-key-rotation-status --key-id `1234abcd-12ab-34cd-56ef-1234567890ab``
`{
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "KeyRotationEnabled": true,
 "NextRotationDate": "2024-03-14T18:14:33.587000+00:00",
 "OnDemandRotationStartDate": "2024-02-24T18:44:48.587000+00:00"
 "RotationPeriodInDays": 365
}`

```

If the KMS key does not support automatic rotation or does not have automatic
rotation enabled, the `kms:GetKeyRotationStatus` response would have
fewer fields as shown in the following example:

```
`$` `aws kms rotate-key-on-demand --key-id `1234abcd-12ab-34cd-56ef-1234567890ab``
`{
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"
}`

`$` `aws kms get-key-rotation-status --key-id `1234abcd-12ab-34cd-56ef-1234567890ab``
`{
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "KeyRotationEnabled": false,
 "OnDemandRotationStartDate": "2024-02-24T18:44:48.587000+00:00"
}`

```
