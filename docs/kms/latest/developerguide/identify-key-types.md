# Identify different key types

The following topics explain how to identify different key types in the AWS KMS console and
[DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") responses.

For help navigating to the **Cryptographic configuration** tab on the
details page for a KMS key, see [Access and list KMS key details](finding-keys.md "finding-keys.md").

###### Topics

- [Identify asymmetric KMS keys](#identify-asymm-keys "#identify-asymm-keys")
- [Identify HMAC KMS keys](#hmac-view "#hmac-view")
- [Identify multi-Region KMS keys](#multi-region-keys-view "#multi-region-keys-view")
- [Identify KMS keys with imported key
  material](#identify-imported-keys "#identify-imported-keys")
- [Identify KMS keys in AWS CloudHSM key stores](#identify-key-hsm-keystore "#identify-key-hsm-keystore")
- [Identify KMS keys in external key stores](#view-xks-key "#view-xks-key")

## Identify asymmetric KMS keys

**In the AWS KMS console**

The **Key type** column of the **Customer managed
keys** table shows whether each KMS key is symmetric or asymmetric. You
can filter the table by the **Key type** value to display only
asymmetric KMS keys. For more information see [Sort and filter your KMS keys](viewing-console-customize.md#viewing-console-filter "viewing-console-customize.md#viewing-console-filter").

The **Cryptographic configuration** tab on the details page for a
KMS key displays the **Key Type**, which indicates whether the key
is symmetric or asymmetric. It also displays the **Key Usage**, which
indicates whether your asymmetric KMS key is used for encryption and decryption, signing
and verification, or deriving shared secrets.

**In DescribeKey responses**

When you call the `DescribeKey` operation on an asymmetric KMS key
the response includes the `KeySpec` and `KeyUsage` values, which
can be used to determine if a KMS key is symmetric or asymmetric.

If the `KeySpec` value is `SYMMETRIC_DEFAULT`, the key is a
symmetric encryption KMS key. For details on asymmetric key specs, see [Key spec reference](symm-asymm-choose-key-spec.md "symm-asymm-choose-key-spec.md").

If the `KeyUsage` value is `SIGN_VERIFY` or
`KEY_AGREEMENT`, the key is an asymmetric KMS key.

The `DescribeKey` operation also returns the following details for
asymmetric KMS keys.

- For asymmetric KMS keys with a `KeyUsage` value of
  `ENCRYPT_DECRYPT`, the operation returns the
  `EncryptionAlgorithms`, which lists the valid encryption algorithms
  for the key.
- For asymmetric KMS keys with a `KeyUsage` value of
  `SIGN_VERIFY`, the operation returns the
  `SigningAlgorithms`, which lists the valid signing algorithms for the
  key.
- For asymmetric KMS keys with a `KeyUsage` value of
  `KEY_AGREEMENT`, the operation returns the
  `KeyAgreementAlgorithms`, which lists the valid key agreement
  algorithms for the key.

For more information on asymmetric KMS keys, see [Asymmetric keys in AWS KMS](symmetric-asymmetric.md "symmetric-asymmetric.md").

## Identify HMAC KMS keys

**In the AWS KMS console**

HMAC KMS keys are included in the **Customer managed keys**
table, but you cannot sort or filter this table by the key spec or key usage values
that identify HMAC keys. To make it easier to find your HMAC keys, assign them a
distinctive alias or tag. Then you can sort or filter by the alias or tag.

The **Cryptographic configuration** tab on the details page for a
KMS key displays the **Key Type**, which indicates whether the key
is symmetric or asymmetric. HMAC KMS keys are symmetric. The **Cryptographic
configuration** tab also displays the **Key Usage**. For
HMAC KMS keys the key usage value is always **Generate and verify
MAC**.

**In DescribeKey responses**

When you call the `DescribeKey` operation on an HMAC KMS key the
response includes the `KeySpec` and `KeyUsage` values. For HMAC
KMS keys the key usage value is always `GENERATE_VERIFY_MAC` and the key
spec value always starts with `HMAC_`.

For more information on HMAC KMS keys, see [HMAC keys in AWS KMS](hmac.md "hmac.md").

## Identify multi-Region KMS keys

**In the AWS KMS console**

The **Customer managed keys** table only displays KMS keys in
the selected Region. You can view multi-Region primary and replica keys in the
selected Region. To change the AWS Region, use the Region selector in the
upper-right corner of the console.

To make it easier to identify multi-Region keys in the **Customer managed
keys** table, add the **Regionality** column to your
table. For help, see [Customize your KMS key tables](viewing-console-customize.md#console-customize-tables "viewing-console-customize.md#console-customize-tables").

The detail page for multi-Region KMS keys includes a
**Regionality** tab. The **Regionality** tab for a
primary key includes Change primary Region and Create new replica keys buttons. (The
Regionality tab for a replica key has neither button.) The **Related
multi-Region keys** section lists all multi-Region keys related to the
current one. If the current key is a replica key, this list includes the primary
key.

If you choose a related multi-Region key from the **Related multi-Region
keys** table, the AWS KMS console changes to the Region of the selected key
and it opens the detail page for the key. For example, if you choose the replica key
in the `sa-east-1` Region from the example **Related multi-Region
keys** section below, the AWS KMS console changes to the
`sa-east-1` Region to display the detail page for that replica key. You
might do this to view the alias or key policy for the replica key. To change the
Region again, use the Region selector at the top right corner of the page.

**In DescribeKey responses**

By default, AWS KMS API operations are Regional and only return the resources in the
current or specified Region. But, when you call the `DescribeKey` operation
on a multi-Region KMS key, the response includes all related multi-Region keys in
other AWS Regions in the `MultiRegionConfiguration` element.

For more information on multi-Region KMS keys, see [Multi-Region keys in AWS KMS](multi-region-keys-overview.md "multi-region-keys-overview.md").

## Identify KMS keys with imported key

material

**In the AWS KMS console**

To make it easier to identify KMS keys with imported key material in the
**Customer managed keys** table, add the
**Origin** column to your table. The **Origin**
column makes it easy to identify KMS keys with an **External (Import Key
material)** origin property value. For help, see [Customize your KMS key tables](viewing-console-customize.md#console-customize-tables "viewing-console-customize.md#console-customize-tables").

The **Cryptographic configuration** tab on the details page for a
KMS key displays the **Origin**, which identifies the source of the
key material for the KMS key. For KMS keys with imported key material, the origin
value is always **External (Import Key material)**. The details page
also includes a **Key material** tab that provides detailed
information about the imported key material. Symmetric encryption keys
with `EXTERNAL` origin support on-demand rotations and can have multiple key
materials associated with them. For such keys, the tab is labeled **Key material and
rotations**.

**In DescribeKey responses**

When you call the `DescribeKey` operation on a KMS key with imported
key material the response includes the `Origin`,
`ExpirationModel`, and `ValidTo` values. For KMS keys with
imported key material the origin value is always `EXTERNAL`. The
`ExpirationModel` value indicates whether or not the key material is set
to expire, and the `ValidTo` value indicates when the key material will
expire. When multiple key materials are associated with a key, the `ValidTo`
value indicates the earliest expiry time across all key materials (except for the one pending
rotation) and `ExpirationModel` is set to `DOES_NOT_EXPIRE` only if none
of these key materials are set to expire. For more information, see
[Setting an expiration time (optional)](importing-keys-import-key-material.md#importing-keys-expiration "importing-keys-import-key-material.md#importing-keys-expiration").

For more information on KMS keys with imported key material, see [Importing key material for AWS KMS keys](importing-keys.md "importing-keys.md").

## Identify KMS keys in AWS CloudHSM key stores

**In the AWS KMS console**

To make it easier to identify KMS keys in AWS CloudHSM key stores in the
**Customer managed keys** table, add the
**Origin** column to your table. The **Origin**
column makes it easy to identify KMS keys with an **AWS CloudHSM** origin
property value. For help, see [Customize your KMS key tables](viewing-console-customize.md#console-customize-tables "viewing-console-customize.md#console-customize-tables").

The **Cryptographic configuration** tab on the details page for a
KMS key displays the **Origin**, which identifies the source of the
key material for the KMS key. For KMS keys in AWS CloudHSM key stores, the origin value
is always **AWS CloudHSM**.

For a KMS key in an AWS CloudHSM key store, the **Cryptographic
configuration** tab includes an additional section, **Custom key
store**, that provides information about the AWS CloudHSM key store and AWS CloudHSM
cluster associated with the KMS key.

**In DescribeKey responses**

When you call the `DescribeKey` operation on a KMS key in an AWS CloudHSM
key store the response includes the `Origin`, which identifies the source
of the key material. For KMS keys in an AWS CloudHSM key store the origin value is always
`AWS_CLOUDHSM`. The operation also returns the following special fields
for KMS keys in AWS CloudHSM key stores:

- `CloudHsmClusterId`
- `CustomKeyStoreId`

For more information on AWS CloudHSM key stores, see [AWS CloudHSM key stores](keystore-cloudhsm.md "keystore-cloudhsm.md").

## Identify KMS keys in external key stores

**In the AWS KMS console**

To make it easier to identify KMS keys in external key stores in the
**Customer managed keys** table, add the
**Origin** column to your table. The **Origin**
column makes it easy to identify KMS keys with an **External key
store** origin property value. For help, see [Customize your KMS key tables](viewing-console-customize.md#console-customize-tables "viewing-console-customize.md#console-customize-tables").

The **Cryptographic configuration** tab on the details page for a
KMS key displays the **Origin**, which identifies the source of the
key material for the KMS key. For KMS keys in external key stores, the origin
value is always **External key store**.

For a KMS key in an external key store, the **Cryptographic
configuration** tab includes two additional sections, **Custom key
store** and **External key**. The **Custom key
store** table provides information about the external key store associated
with the KMS key. The **External key** table appears in the AWS KMS
console only for KMS keys in external key stores. It provides information about the
external key associated with the KMS key. The [external key](keystore-external.md#concept-external-key "keystore-external.md#concept-external-key") is a cryptographic key
outside of AWS that serves as the key material for the KMS key in the external key
store. When you encrypt or decrypt with the KMS key, the operation is performed by
your [external key manager](keystore-external.md#concept-ekm "keystore-external.md#concept-ekm") using the specified
external key.

The following values appear in the **External key**
section.

**External key ID**

The identifier for the external key in its external key manager. This is the
value that the external key store proxy uses to identify the external key. You
specify the ID of the external key when you create the KMS key and you cannot
change it. If the external key ID value that you used to create the KMS key
changes or becomes invalid, you must [schedule the
KMS key for deletion](deleting-keys.md "deleting-keys.md") and [create a new
KMS key](create-xks-keys.md "create-xks-keys.md") with the correct external key ID value.

**In DescribeKey responses**

When you call the `DescribeKey` operation on a KMS key in an external
key store the response includes the `Origin`, which identifies the source
of the key material. For KMS keys in an AWS CloudHSM key store the origin value is always
`EXTERNAL_KEY_STORE`. The operation also returns the
`CustomKeyStoreId` element, which identifies the external key store
associated with the KMS keys.

For more information on external key stores, see [External key stores](keystore-external.md "keystore-external.md").
