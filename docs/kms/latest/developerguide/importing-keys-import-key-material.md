# Step 4: Import the

key material

After you [encrypt your key
material](importing-keys-encrypt-key-material.md "importing-keys-encrypt-key-material.md"), you can import the key material to use with an AWS KMS key. To import key
material, you upload the encrypted key material from [Step 3: Encrypt the
key material](importing-keys-encrypt-key-material.md "importing-keys-encrypt-key-material.md") and the import token that you
downloaded at [Step 2:
Download the wrapping public key and import token](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md"). You must import key material
into the same KMS key that you specified when you [downloaded the public key and import
token](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md"). When key material is successfully imported, the [key
state](key-state.md "key-state.md") of the KMS key changes to `Enabled`, and you can use the KMS key
in cryptographic operations.

When you import key material, you can [set an
optional expiration time](#importing-keys-expiration "#importing-keys-expiration") for the key material. When the key material expires, AWS KMS
deletes the key material and the KMS key becomes unusable. After you import your key
material, you cannot set, change, or cancel the expiration date for the current import. To
change these values, you must [reimport](#reimport-key-material "#reimport-key-material") the same
key material.

For all KMS keys with `EXTERNAL` origin, the first key material imported into it becomes current and
permanently associated with it. Single-Region, symmetric encryption keys with `EXTERNAL` origin
support on-demand rotation. You can associate multiple key materials with imported keys that support on-demand
rotation. You must set the `importType` parameter to `NEW_KEY_MATERIAL` with the
[ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md") action to associate new key
material with a KMS key. This key material is not permanently associated with the key until you perform
the [RotateKeyOnDemand](../APIReference/API_RotateKeyOnDemand.md "../APIReference/API_RotateKeyOnDemand.md") action.
Until then, this key material is in `PENDING_ROTATION` state. The default value of the optional
`ImportType` parameter is `EXISTING_KEY_MATERIAL`. When you omit the
`ImportType` parameter or specify it as `EXISTING_KEY_MATERIAL`, you must import a
key material that is previously associated with the KMS key.

For asymmetric, HMAC or multi-Region KMS keys with `EXTERNAL` origin, only one key material can
ever be associated with the key. AWS KMS will reject [ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md") API requests with the `ImportType` parameter.

When all key materials permanently associated with a KMS key are imported, the KMS key is available
for use in cryptographic operations. If any one of these key materials is deleted or allowed to expire, the
KMS key state changes to `PendingImport` and the key is unusable for cryptographic operations.

To import key material, you can use the [AWS KMS
console](#importing-keys-import-key-material-console "#importing-keys-import-key-material-console") or the [ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md") API. You can use the
API directly by making HTTP requests, or by using an [AWS SDKs](https://aws.amazon.com/tools/#sdk "https://aws.amazon.com/tools/#sdk"),
[AWS Command Line Interface](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") or [AWS Tools for PowerShell](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md").

When you import the key material, an [ImportKeyMaterial
entry](ct-importkeymaterial.md "ct-importkeymaterial.md") is added to your AWS CloudTrail log to record the `ImportKeyMaterial`
operation. The CloudTrail entry is the same whether you use the AWS KMS console or the AWS KMS API.

## Setting an expiration time (optional)

When you import the key material for your KMS key, you can set an optional expiration
date and time for the key material of up to 365 days from the import date. When imported key
material expires, AWS KMS deletes it. This action changes the [key state](key-state.md#key-state-table "key-state.md#key-state-table") of the KMS key to `PendingImport`, which prevents it from
being used in any cryptographic operation. To use the KMS key, you must [reimport a copy of the original key material](#reimport-key-material "#reimport-key-material").

Ensuring that imported key material expires frequently can help you to satisfy regulatory
requirements, but it introduces an additional a risk to data encrypted under the KMS key.
Until you reimport a copy of the original key material, a KMS key with expired key material
is unusable, and any data encrypted under the KMS key is inaccessible. If you fail to
reimport the key material for any reason, including losing your copy of the original key
material, the KMS key is permanently unusable, and data encrypted under the KMS key is
unrecoverable.

To mitigate this risk, make sure that your copy of the imported key material is
accessible, and design a system to delete and reimport the key material before it expires and
interrupts your AWS workload. We recommend that you [set an alarm](imported-key-material-expiration-alarm.md "imported-key-material-expiration-alarm.md") for the expiration of
your imported key material that gives you plenty of time to reimport the key material before
it expires. You can also use your CloudTrail logs to audit operations that [import (and reimport) key material](ct-importkeymaterial.md "ct-importkeymaterial.md") and [delete imported key material](ct-deleteimportedkeymaterial.md "ct-deleteimportedkeymaterial.md"), and the AWS KMS
operation to [delete expired key
material](ct-deleteexpiredkeymaterial.md "ct-deleteexpiredkeymaterial.md").

AWS KMS cannot restore, recover, or reproduce the deleted key material. Instead of setting an expiration
time, you can programmatically [delete](importing-keys-delete-key-material.md "importing-keys-delete-key-material.md") and [reimport](#reimport-key-material "#reimport-key-material") the imported key material periodically, but
the requirements for retaining a copy of the original key material are the same.

You determine whether and when imported key material expires when you import the key
material. However you can turn expiration on and off, or set a new expiration time by
reimporting the key material. Use the `ExpirationModel` parameter of [ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md") to turn expiration
on (`KEY_MATERIAL_EXPIRES`) and off (`KEY_MATERIAL_DOES_NOT_EXPIRE`) and
the `ValidTo` parameter to set the expiration time. The maximum time is 365 days
from the import data; there is no minimum, but the time must be in the future.

## Set key material description

Single-Region, symmetric encryption keys with `EXTERNAL` origin can have multiple key materials
associated with them. You can specify an optional key material description when importing key material into
such keys. The description can be used to keep track of where the corresponding key
material is durably maintained outside AWS KMS.

## Reimport key material

If you manage a KMS key with imported key material, you might need to reimport the key
material. You might reimport key material to replace expiring or deleted key material, or to
change the expiration model or expiration date of the key material.

You can reimport key material at any time, on any schedule that meets your security
requirements. You do not have to wait until the key material is at or close to its expiration
time.

The procedure to reimport key material is the same procedure that you use to
import the key material the first time, with the following exceptions.

- Use an existing KMS key, instead of creating a new KMS key. You can skip [Step 1](importing-keys-create-cmk.md "importing-keys-create-cmk.md") of the import procedure.
- When you reimport key material, you can change the expiration model and expiration
  date.

Each time you import key material to a KMS key, you need to [download and use a new wrapping key and
import token](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md") for the KMS key. The wrapping procedure does not affect the content of
the key material, so you can use different wrapping public keys and different wrapping
algorithms to import the same key material.

## Import new key material

To perform on-demand rotation on a symmetric encryption KMS key with imported key material,
you'll first need to import new key material, not previously associated with the key. Use the
[ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md") operation with the
`ImportType` parameter set to `NEW_KEY_MATERIAL` to accomplish this task. Key material
imported in this manner will be in `PENDING_ROTATION` state until you perform the
[RotateKeyOnDemand](../APIReference/API_RotateKeyOnDemand.md "../APIReference/API_RotateKeyOnDemand.md") operation or rotate the key in
the AWS Management Console. A KMS key can have at most one key material in `PENDING_ROTATION` state at any time.

## Import key material

(console)

You can use the AWS Management Console to import key material.

1. If you are on the **Upload your wrapped key material** page, skip to
   [Step 8](#id-key-materials-step "#id-key-materials-step").
2. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
3. To change the AWS Region, use the Region selector in the upper-right corner of the page.
4. In the navigation pane, choose **Customer managed keys**.
5. Choose the key ID or alias of the KMS key for which you downloaded the public key
   and import token.
6. Choose the **Cryptographic configuration** tab and view its values.
   The tabs are on the detail page for a KMS key below the **General
   configuration** section.

You can only import key material into KMS keys with an **Origin**
of **External (Import key material)**. For information about
creating KMS keys with imported key material, see [Importing key material for AWS KMS keys](importing-keys.md "importing-keys.md"). 7. For asymmetric, HMAC and multi-Region keys, choose the **Key material** tab
and then choose **Import key material**. For single-Region, symmetric encryption keys,
choose the **Key material and rotations** tab. Then, choose either **Import
initial key material** or **Import new key material** or **Reimport
key material**. The **Reimport key material** option is available in the
`Actions` menu in the key materials table.

If you downloaded the key material, import token, and encrypted the key material,
choose **Next**. 8. In the **Encrypted key material and import token** section, do the
following.

    1. Under **Wrapped key material**, choose **Choose
     file**. Then upload the file that contains your wrapped (encrypted) key
     material.
    2. Under **Import token**, choose **Choose file**.
     Upload the file that contains the import token that you [downloaded](importing-keys-get-public-key-and-token.md#importing-keys-get-public-key-and-token-console "importing-keys-get-public-key-and-token.md#importing-keys-get-public-key-and-token-console").

9. In the **Expiration option** section, you determine whether the key
   material expires. To set an expiration date and time, choose **Key material
   expires**, and use the calendar to select a date and time. You can specify a
   date up to 365 days from the current date and time.
10. For symmetric encryption keys, you can optionally specify a description for the key material
    being imported.
11. Choose **Import key material**.

## Import key material

(AWS KMS API)

To import key material, use the [ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md") operation. The following example uses the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming
language.

To use this example:

1. Replace `1234abcd-12ab-34cd-56ef-1234567890ab` with a key ID of
   the KMS key that you specified when you downloaded the public key and import token. To
   identify the KMS key, use its [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") or [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN"). You cannot use an [alias name](concepts.md#key-id-alias-name "concepts.md#key-id-alias-name") or [alias
   ARN](concepts.md#key-id-alias-ARN "concepts.md#key-id-alias-ARN") for this operation.
2. Replace `EncryptedKeyMaterial.bin` with the name
   of the file that contains the encrypted key material.
3. Replace `ImportToken.bin` with the name of the
   file that contains the import token.
4. If you want the imported key material to expire, set the value of the
   `expiration-model` parameter to its default value,
   `KEY_MATERIAL_EXPIRES`, or omit the `expiration-model` parameter.
   Then, replace the value of the `valid-to` parameter with the date and time that
   you want the key material to expire. The date and time can be up to 365 days from the time
   of the request.

```
`$` `aws kms import-key-material --key-id `1234abcd-12ab-34cd-56ef-1234567890ab` \
 --encrypted-key-material fileb://`EncryptedKeyMaterial.bin` \
 --import-token fileb://`ImportToken.bin` \
 --expiration-model `KEY_MATERIAL_EXPIRES` \
 --valid-to `2023-06-17T12:00:00-08:00``
```

If you do not want the imported key material to expire, set the value of the
`expiration-model` parameter to `KEY_MATERIAL_DOES_NOT_EXPIRE` and
omit the `valid-to` parameter from the command.

```
`$` `aws kms import-key-material --key-id `1234abcd-12ab-34cd-56ef-1234567890ab` \
 --encrypted-key-material fileb://`EncryptedKeyMaterial.bin` \
 --import-token fileb://`ImportToken.bin` \
 --expiration-model `KEY_MATERIAL_DOES_NOT_EXPIRE``
```

5. If you want to import new key material, not previously associated with the KMS key, set the
   `ImportType` parameter to `NEW_KEY_MATERIAL`. This option can only be used
   with single-Region symmetric encryption keys. For these keys, you can also use the optional
   `KeyMaterialDescription` parameter to set a description for the imported key material
   in the following command line example:

```
`$` `aws kms import-key-material --key-id `1234abcd-12ab-34cd-56ef-1234567890ab` \
 --encrypted-key-material fileb://`EncryptedKeyMaterial.bin` \
 --import-token fileb://`ImportToken.bin` \
 --expiration-model `KEY_MATERIAL_EXPIRES` \
 --valid-to `2023-06-17T12:00:00-08:00` \
 --import-type NEW_KEY_MATERIAL \
 --key-material-description `"Q2 2025 Rotation"``
```

###### Tip

If the command does not succeed, you might see a `KMSInvalidStateException`
or a `NotFoundException`. You can retry the request.
