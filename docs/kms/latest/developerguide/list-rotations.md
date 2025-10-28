# List rotations and key materials

KMS keys that support automatic or on-demand key rotation can have multiple key materials
associated with them. These keys have an initial key material and one additional key material
for each automatic or on-demand rotation.

Authorized users with `kms:ListKeyRotations` permission can use the AWS KMS console
and the [ListKeyRotations](../APIReference/API_ListKeyRotations.md "../APIReference/API_ListKeyRotations.md") API to list
all key materials associated with a KMS key, including those from completed automatic and on-demand
rotations.

###### Topics

- [List rotations and key materials
  (console)](#list-rotations-console "#list-rotations-console")
- [List rotations and key materials
  (AWS KMS API)](#list-rotations-api "#list-rotations-api")

## List rotations and key materials

(console)

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Choose the alias or key ID of a KMS key.
5. Choose the **Key material and rotations** tab.
   - The **Key material and rotations** tab appears only on the detail
     page of symmetric encryption KMS keys that support automatic or on-demand rotation.
     This includes KMS keys with key material that AWS KMS generated (`AWS_KMS`
     origin) and single-Region KMS keys with imported key material (`EXTERNAL`
     origin).
   - The **Key materials** table in the **Key material and
     rotations** tab lists all the key materials associated with the KMS key. For
     each key material, the corresponding entry displays its unique identifier assigned by
     AWS KMS, the rotation date, and key material state. The rotation date identifies when the
     key material became current after an automatic or on-demand key rotation. There is no
     rotation date associated with the first or `Pending rotation` key material.
     The key material state determines how AWS KMS uses the key material. Current key material
     is used for both encryption and decryption. Non-current key material is only used for
     decryption. A key material state of `Pending rotation` indicates the key
     material is staged for rotation. This key material is not used for any cryptographic
     operation until an on-demand key rotation makes it the current key material. Additional
     information displayed for the key material depends on type of KMS key.
   - For symmetric encryption KMS keys with `AWS_KMS` origin, each row also
     displays the rotation type — `On-demand` or `Automatic`.
   - Single-Region, symmetric encryption KMS keys with imported key material
     (`EXTERNAL` origin) only support `On-demand` rotation, so there
     is no rotation type column. Instead, each row displays an import state, a user-specified
     description, expiration information, and an **Actions** menu. The
     import state is either **Imported** indicating the key material is
     available inside AWS KMS or **Pending import** indicating the key material
     is not available inside AWS KMS. The **Actions** menu can be used to
     delete imported key material or reimport key material. The **Delete key
     material** action is disabled if the import state of the key material is
     **Pending import**. The **Reimport key material**
     action is always available. You do not need to wait for a key material to expire or
     be deleted before reimporting it.

## List rotations and key materials

(AWS KMS API)

You can use the [AWS Key Management Service (AWS KMS) API](../APIReference.md "../APIReference.md") to
initiate on-demand key rotation and view the current rotation status of any
customer managed key. This example uses the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

The [ListKeyRotations](../APIReference/API_ListKeyRotations.md "../APIReference/API_ListKeyRotations.md")
operation lists all rotations and key materials for the specified KMS key.
To identify the KMS key in these operations, use its [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") or [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN").

This operation supports an optional `IncludeKeyMaterial` parameter. The default value
of this parameter is `ROTATIONS_ONLY`. If you omit this parameter, AWS KMS returns information
on the key materials created by automatic or on-demand key rotation. When you specify a value of
`ALL_KEY_MATERIAL`, AWS KMS adds the first key material and any imported key material
pending rotation to the response. This parameter can only be used with KMS keys that support
automatic or on-demand key rotation.

```
`$` `aws kms list-key-rotations --key-id `1234abcd-12ab-34cd-56ef-1234567890ab` \
 --inlcude-key-material ALL_KEY_MATERIAL`
`{
 "Rotations": [
 {
 "KeyId": 1234abcd-12ab-34cd-56ef-1234567890ab,
 "KeyMaterialId": 123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0,
 "KeyMaterialDescription": "KeyMaterialA",
 "ImportState": "PENDING_IMPORT",
 "KeyMaterialState": "NON_CURRENT"
 },
 {
 "KeyId": 1234abcd-12ab-34cd-56ef-1234567890ab,
 "KeyMaterialId": 96083e4fb6dbc41d77578a213a6b6669c044dd4c143e96755396d2bf11fd6068,
 "ImportState": "IMPORTED",
 "KeyMaterialState": "CURRENT",
 "ExpirationModel": "KEY_MATERIAL_DOES_NOT_EXPIRE",
 "RotationDate": "2025-05-01T15:50:51.045000-07:00",
 "RotationType": "ON_DEMAND"
 }
 ],
 "Truncated": false
}`

```
