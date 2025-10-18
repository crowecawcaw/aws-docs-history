# Key attributes in the PKCS #11 library for AWS CloudHSM
 Client SDK 3

A key object can be a public, private, or secret key. Actions permitted on a key object
 are specified through attributes. Attributes are defined when the key object is created. When
 you use the PKCS #11 library for AWS CloudHSM, we assign default values as specified by the PKCS #11
 standard.

AWS CloudHSM does not support all attributes listed in the PKCS #11 specification. We are
 compliant with the specification for all attributes we support. These attributes are listed in
 the respective tables.

Cryptographic functions such as `C_CreateObject`, `C_GenerateKey`,
 `C_GenerateKeyPair`, `C_UnwrapKey`, and `C_DeriveKey` that
 create, modify, or copy objects take an attribute template as one of their parameters. For
 more information about passing an attribute template during object creation, see [Generate keys through PKCS #11 library](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/generate "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/generate") sample.

The following topics provide more information about AWS CloudHSM key attributes for
 Client SDK 3.

###### Topics

* [Attributes table](pkcs11-v3-attributes-interpreting.md "pkcs11-v3-attributes-interpreting.md")
* [Modifying attributes](pkcs11-v3-modify-attr.md "pkcs11-v3-modify-attr.md")
* [Interpreting PKCS #11 library error codes for AWS CloudHSM Client SDK 3](pkcs11-v3-attr-errors.md "pkcs11-v3-attr-errors.md")
