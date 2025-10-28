# Modifying PKCS #11 library attributes for AWS CloudHSM Client SDK 3

Some attributes of an object can be modified after the object has been created, whereas
some cannot. To modify attributes, use the [setAttribute](cloudhsm_mgmt_util-setAttribute.md "cloudhsm_mgmt_util-setAttribute.md") command from cloudhsm_mgmt_util. You can also derive a list of attributes and the
constants that represent them by using the [listAttribute](cloudhsm_mgmt_util-listAttributes.md "cloudhsm_mgmt_util-listAttributes.md") command from cloudhsm_mgmt_util.

The following list displays attributes that are allowed for modification after object
creation:

- `CKA_LABEL`
- `CKA_TOKEN`

###### Note

Modification is allowed only for changing a session key to a token key. Use the
[setAttribute](key_mgmt_util-setAttribute.md "key_mgmt_util-setAttribute.md") command from key_mgmt_util to
change the attribute value.

- `CKA_ENCRYPT`
- `CKA_DECRYPT`
- `CKA_SIGN`
- `CKA_VERIFY`
- `CKA_WRAP`
- `CKA_UNWRAP`
- `CKA_LABEL`
- `CKA_SENSITIVE`
- `CKA_DERIVE`

###### Note

This attribute supports key derivation. It must be `False` for all
public keys and cannot be set to `True`. For secret and EC private keys, it
can be set to `True` or `False`.

- `CKA_TRUSTED`

###### Note

This attribute can be set to `True` or `False` by Crypto
Officer (CO) only.

- `CKA_WRAP_WITH_TRUSTED`

###### Note

Apply this attribute to an exportable data key to specify that you can only wrap this
key with keys marked as `CKA_TRUSTED`. Once you set `CKA_WRAP_WITH_TRUSTED`
to true, the attribute becomes read-only and you cannot change or remove the attribute.
