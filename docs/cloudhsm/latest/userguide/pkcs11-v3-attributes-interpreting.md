# PKCS #11 library attributes table for AWS CloudHSM Client SDK 3

The PKCS #11 library table for AWS CloudHSM Client SDK 3 contains a list of attributes that differ by key types. It indicates
 whether a given attribute is supported for a particular key type when using a specific
 cryptographic function with AWS CloudHSM.

**Legend:**


* ✔ indicates that CloudHSM supports the attribute for the specific key
 type.
* ✖ indicates that CloudHSM does not support the attribute for the specific key
 type.
* R indicates that the attribute value is set to read-only for the specific key type.
* S indicates that the attribute cannot be read by the `GetAttributeValue`
 as it is sensitive.
* An empty cell in the Default Value column indicates that there is no specific
 default value assigned to the attribute.


| Attribute | Key Type | **Default Value** |
| --- | --- | --- |
|   | **EC private** | **EC public** | **RSA private** | **RSA public** |   |
| `CKA_CLASS` | ✔ | ✔ | ✔ | ✔ |  |
| `CKA_KEY_TYPE` | ✔ | ✔ | ✔ | ✔ |  |
| `CKA_LABEL` | ✔ | ✔ | ✔ | ✔ |  |
| `CKA_ID` | ✔ | ✔ | ✔ | ✔ |  |
| `CKA_LOCAL` | R | R | R | R | True |
| `CKA_TOKEN` | ✔ | ✔ | ✔ | ✔ | False |
| `CKA_PRIVATE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True |
| `CKA_ENCRYPT` | ✖ | ✔ | ✖ | ✔ | False |
| `CKA_DECRYPT` | ✔ | ✖ | ✔ | ✖ | False |
| `CKA_DERIVE` | ✔ | ✔ | ✔ | ✔ | False |
| `CKA_MODIFIABLE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True |
| `CKA_DESTROYABLE` | ✔ | ✔ | ✔ | ✔ | True |
| `CKA_SIGN` | ✔ | ✖ | ✔ | ✖ | False |
| `CKA_SIGN_RECOVER` | ✖ | ✖ | ✔[3](#pkcs11-v3-f10 "#pkcs11-v3-f10") | ✖ |   |
| `CKA_VERIFY` | ✖ | ✔ | ✖ | ✔ | False |
| `CKA_VERIFY_RECOVER` | ✖ | ✖ | ✖ | ✔[4](#pkcs11-v3-f11 "#pkcs11-v3-f11") |   |
| `CKA_WRAP` | ✖ | ✔ | ✖ | ✔ | False |
| `CKA_WRAP_TEMPLATE` | ✖ | ✔ | ✖ | ✔ |   |
| `CKA_TRUSTED` | ✖ | ✔ | ✖ | ✔ | False |
| `CKA_WRAP_WITH_TRUSTED` | ✔ | ✖ | ✔ | ✖ | False |
| `CKA_UNWRAP` | ✔ | ✖ | ✔ | ✖ | False |
| `CKA_UNWRAP_TEMPLATE` | ✔ | ✖ | ✔ | ✖ |   |
| `CKA_SENSITIVE` | ✔ | ✖ | ✔ | ✖ | True |
| `CKA_ALWAYS_SENSITIVE` | R | ✖ | R | ✖ |  |
| `CKA_EXTRACTABLE` | ✔ | ✖ | ✔ | ✖ | True |
| `CKA_NEVER_EXTRACTABLE` | R | ✖ | R | ✖ |  |
| `CKA_MODULUS` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_MODULUS_BITS` | ✖ | ✖ | ✖ |  ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |   |
| `CKA_PRIME_1` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_PRIME_2` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_COEFFICIENT` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_EXPONENT_1` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_EXPONENT_2` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_PRIVATE_EXPONENT` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_PUBLIC_EXPONENT` | ✖ | ✖ | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |   |
| `CKA_EC_PARAMS` | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✖ | ✖ |   |
| `CKA_EC_POINT` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_VALUE` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_VALUE_LEN` | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_CHECK_VALUE` | R | R | R | R |   |
| Attribute | Key Type | **Default Value** | | --- | --- | --- |
|   | **AES** | **DES3** | **Generic Secret** |   | | `CKA_CLASS` | ✔  | ✔ | ✔ |  |
| `CKA_KEY_TYPE` | ✔  | ✔ | ✔ |  | | `CKA_LABEL` | ✔  | ✔ | ✔ |  |
| `CKA_ID` | ✔ | ✔ | ✔ |  | | `CKA_LOCAL` | R  | R | R | True |
| `CKA_TOKEN` | ✔ | ✔ | ✔ | False | | `CKA_PRIVATE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True |
| `CKA_ENCRYPT` | ✔ | ✔ | ✖ | False | | `CKA_DECRYPT` | ✔  | ✔ | ✖ | False |
| `CKA_DERIVE` | ✔  | ✔ | ✔ | False | | `CKA_MODIFIABLE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True |
| `CKA_DESTROYABLE` | ✔  | ✔ | ✔ | True | | `CKA_SIGN` | ✔  | ✔ | ✔ | True  |
| `CKA_SIGN_RECOVER` | ✖ | ✖ | ✖ |   | | `CKA_VERIFY` | ✔  | ✔ | ✔ | True  |
| `CKA_VERIFY_RECOVER` | ✖ | ✖ | ✖ |   | | `CKA_WRAP` | ✔  | ✔ | ✖ | False |
| `CKA_WRAP_TEMPLATE` | ✔  | ✔ | ✖ |   | | `CKA_TRUSTED` | ✔  | ✔ | ✖ | False |
| `CKA_WRAP_WITH_TRUSTED` | ✔  | ✔ | ✔ | False | | `CKA_UNWRAP` | ✔  | ✔ | ✖ | False |
| `CKA_UNWRAP_TEMPLATE` | ✔  | ✔ | ✖ |   | | `CKA_SENSITIVE` | ✔  | ✔ | ✔ | True |
| `CKA_ALWAYS_SENSITIVE` | ✖ | ✖ | ✖ |  | | `CKA_EXTRACTABLE` | ✔  | ✔ | ✔ | True |
| `CKA_NEVER_EXTRACTABLE` | R | R | R |  | | `CKA_MODULUS` | ✖ | ✖ | ✖ |   |
| `CKA_MODULUS_BITS` | ✖ | ✖ | ✖ |   | | `CKA_PRIME_1` | ✖ | ✖ | ✖ |   |
| `CKA_PRIME_2` | ✖ | ✖ | ✖ |   | | `CKA_COEFFICIENT` | ✖ | ✖ | ✖ |   |
| `CKA_EXPONENT_1` | ✖ | ✖ | ✖ |   | | `CKA_EXPONENT_2` | ✖ | ✖ | ✖ |   |
| `CKA_PRIVATE_EXPONENT` | ✖ | ✖ | ✖ |   | | `CKA_PUBLIC_EXPONENT` | ✖ | ✖ | ✖ |   |
| `CKA_EC_PARAMS` | ✖ | ✖ | ✖ |   | | `CKA_EC_POINT` | ✖ | ✖ | ✖ |   |
| `CKA_VALUE` | ✖ | ✖ | ✖ |   | | `CKA_VALUE_LEN` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |   |
| `CKA_CHECK_VALUE` | R  | R | R |   | | Attribute | Key Type | **Default Value** |
| --- | --- | --- |
|   | **EC private** | **EC public** | **RSA private** | **RSA public** | **AES** | **DES3** | **Generic Secret** |   |
| `CKA_CLASS` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |  |
| `CKA_KEY_TYPE` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |  |
| `CKA_LABEL` | ✔ | ✔ | ✔ | ✔ | ✔  | ✔ | ✔ |  |
| `CKA_ID` | ✔ | ✔ | ✔ | ✔ | ✔  | ✔ | ✔ |  |
| `CKA_LOCAL` | R | R | R | R | R | R | R | False |
| `CKA_TOKEN` | ✔ | ✔ | ✔ | ✔ | ✔  | ✔ | ✔ | False |
| `CKA_PRIVATE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True |
| `CKA_ENCRYPT` | ✖ | ✖ | ✖ | ✔ | ✔  | ✔ | ✖ | False |
| `CKA_DECRYPT` | ✖ | ✖ | ✔ | ✖ | ✔  | ✔ | ✖ | False |
| `CKA_DERIVE` | ✔ | ✔ | ✔ | ✔ | ✔  | ✔ | ✔ | False |
| `CKA_MODIFIABLE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True |
| `CKA_DESTROYABLE` | ✔ | ✔ | ✔ | ✔ | ✔  | ✔ | ✔ | True |
| `CKA_SIGN` | ✔ | ✖ | ✔ | ✖ | ✔  | ✔ | ✔ | False |
| `CKA_SIGN_RECOVER` | ✖ | ✖ | ✔[3](#pkcs11-v3-f10 "#pkcs11-v3-f10") | ✖ | ✖ | ✖ | ✖ | False |
| `CKA_VERIFY` | ✖ | ✔ | ✖ | ✔ | ✔  | ✔ | ✔ | False |
| `CKA_VERIFY_RECOVER` | ✖ | ✖ | ✖ | ✔[4](#pkcs11-v3-f11 "#pkcs11-v3-f11") | ✖ | ✖ | ✖ |   |
| `CKA_WRAP` | ✖ | ✖ | ✖ | ✔ | ✔  | ✔ | ✖ | False |
| `CKA_WRAP_TEMPLATE` | ✖ | ✔ | ✖ | ✔ | ✔  | ✔ | ✖ |   |
| `CKA_TRUSTED` | ✖ | ✔ | ✖ | ✔ | ✔  | ✔ | ✖ | False |
| `CKA_WRAP_WITH_TRUSTED` | ✔ | ✖ | ✔ | ✖ | ✔  | ✔ | ✔ | False |
| `CKA_UNWRAP` | ✖ | ✖ | ✔ | ✖ | ✔  | ✔ | ✖ | False |
| `CKA_UNWRAP_TEMPLATE` | ✔ | ✖ | ✔ | ✖ | ✔  | ✔ | ✖ |   |
| `CKA_SENSITIVE` | ✔ | ✖ | ✔ | ✖ | ✔  | ✔ | ✔ | True |
| `CKA_ALWAYS_SENSITIVE` | R | ✖ | R | ✖ | R | R | R |  |
| `CKA_EXTRACTABLE` | ✔ | ✖ | ✔ | ✖ | ✔  | ✔ | ✔ | True |
| `CKA_NEVER_EXTRACTABLE` | R | ✖ | R | ✖ | R | R | R |  |
| `CKA_MODULUS` | ✖ | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✖ | ✖ | ✖ |   |
| `CKA_MODULUS_BITS` | ✖ | ✖ | ✖ |  ✖ | ✖ | ✖ | ✖ |   |
| `CKA_PRIME_1` | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_PRIME_2` | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_COEFFICIENT` | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_EXPONENT_1` | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_EXPONENT_2` | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_PRIVATE_EXPONENT` | ✖ | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_PUBLIC_EXPONENT` | ✖ | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✖ | ✖ | ✖ |   |
| `CKA_EC_PARAMS` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_EC_POINT` | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_VALUE` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✖ | ✖ | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |   |
| `CKA_VALUE_LEN` | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_CHECK_VALUE` | R | R | R | R | R | R | R |   |
| Attribute | Key Type | **Default Value** | | --- | --- | --- | |   | **EC private** | **RSA private** | **AES** | **DES3** | **Generic Secret** |   |
| `CKA_CLASS` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |  | | `CKA_KEY_TYPE` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |  |
| `CKA_LABEL` | ✔ | ✔ | ✔ | ✔ | ✔ |  | | `CKA_ID` | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| `CKA_LOCAL` | R | R | R | R | R | False | | `CKA_TOKEN` | ✔ | ✔ | ✔ | ✔ | ✔ | False |
| `CKA_PRIVATE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True | | `CKA_ENCRYPT` | ✖ | ✖ | ✔ | ✔ | ✖ | False |
| `CKA_DECRYPT` | ✖ | ✔ | ✔ | ✔ | ✖ | False | | `CKA_DERIVE` | ✔ | ✔ | ✔ | ✔ | ✔ | False |
| `CKA_MODIFIABLE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True | | `CKA_DESTROYABLE` | ✔ | ✔ | ✔ | ✔ | ✔ | True |
| `CKA_SIGN` | ✔ | ✔ | ✔ | ✔ | ✔ | False | | `CKA_SIGN_RECOVER` | ✖ | ✔[3](#pkcs11-v3-f10 "#pkcs11-v3-f10") | ✖ | ✖ | ✖ | False |
| `CKA_VERIFY` | ✖ | ✖ | ✔ | ✔ | ✔ | False | | `CKA_VERIFY_RECOVER` | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_WRAP` | ✖ | ✖ | ✔ | ✔ | ✖ | False | | `CKA_UNWRAP` | ✖ | ✔ | ✔ | ✔ | ✖ | False |
| `CKA_SENSITIVE` | ✔ | ✔ | ✔ | ✔ | ✔ | True | | `CKA_EXTRACTABLE` | ✔ | ✔ | ✔ | ✔ | ✔ | True |
| `CKA_NEVER_EXTRACTABLE` | R | R | R | R | R |  | | `CKA_ALWAYS_SENSITIVE` | R | R | R | R | R |  |
| `CKA_MODULUS` | ✖ | ✖ | ✖ | ✖ | ✖ |   | | `CKA_MODULUS_BITS` | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_PRIME_1` | ✖ | ✖ | ✖ | ✖ | ✖ |   | | `CKA_PRIME_2` | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_COEFFICIENT` | ✖ | ✖ | ✖ | ✖ | ✖ |   | | `CKA_EXPONENT_1` | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_EXPONENT_2` | ✖ | ✖ | ✖ | ✖ | ✖ |   | | `CKA_PRIVATE_EXPONENT` | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_PUBLIC_EXPONENT` | ✖ | ✖ | ✖ | ✖ | ✖ |   | | `CKA_EC_PARAMS` | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_EC_POINT` | ✖ | ✖ | ✖ | ✖ | ✖ |   | | `CKA_VALUE` | ✖ | ✖ | ✖ | ✖ | ✖ |   |
| `CKA_VALUE_LEN` | ✖ | ✖ | ✖ | ✖ | ✖ |   | | `CKA_CHECK_VALUE` | R | R | R | R | R |   |
| Attribute | Key Type | **Default Value** | | --- | --- | --- | |   | **AES** | **DES3** | **Generic Secret** |   |
| `CKA_CLASS` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |  | | `CKA_KEY_TYPE` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |  |
| `CKA_LABEL` | ✔ | ✔ | ✔ |  | | `CKA_ID` | ✔ | ✔ | ✔ |  |
| `CKA_LOCAL` | R | R | R | True | | `CKA_TOKEN` | ✔ | ✔ | ✔ | False |
| `CKA_PRIVATE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True | | `CKA_ENCRYPT` | ✔ | ✔ | ✖ | False |
| `CKA_DECRYPT` | ✔ | ✔ | ✖ | False | | `CKA_DERIVE` | ✔ | ✔ | ✔ | False |
| `CKA_MODIFIABLE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True | | `CKA_DESTROYABLE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | True |
| `CKA_SIGN` | ✔ | ✔ | ✔ | False | | `CKA_SIGN_RECOVER` | ✖ | ✖ | ✖ |   |
| `CKA_VERIFY` | ✔ | ✔ | ✔ | False | | `CKA_VERIFY_RECOVER` | ✖ | ✖ | ✖ |   |
| `CKA_WRAP` | ✔ | ✔ | ✖ | False | | `CKA_UNWRAP` | ✔ | ✔ | ✖ | False |
| `CKA_SENSITIVE` | ✔ | ✔ | ✔ | True | | `CKA_EXTRACTABLE` | ✔ | ✔ | ✔ | True |
| `CKA_NEVER_EXTRACTABLE` | R | R | R |  | | `CKA_ALWAYS_SENSITIVE` | R | R | R |  |
| `CKA_MODULUS` | ✖ | ✖ | ✖ |   | | `CKA_MODULUS_BITS` | ✖ | ✖ | ✖ |   |
| `CKA_PRIME_1` | ✖ | ✖ | ✖ |   | | `CKA_PRIME_2` | ✖ | ✖ | ✖ |   |
| `CKA_COEFFICIENT` | ✖ | ✖ | ✖ |   | | `CKA_EXPONENT_1` | ✖ | ✖ | ✖ |   |
| `CKA_EXPONENT_2` | ✖ | ✖ | ✖ |   | | `CKA_PRIVATE_EXPONENT` | ✖ | ✖ | ✖ |   |
| `CKA_PUBLIC_EXPONENT` | ✖ | ✖ | ✖ |   | | `CKA_EC_PARAMS` | ✖ | ✖ | ✖ |   |
| `CKA_EC_POINT` | ✖ | ✖ | ✖ |   | | `CKA_VALUE` | ✖ | ✖ | ✖ |   |
| `CKA_VALUE_LEN` | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |   | | `CKA_CHECK_VALUE` | R | R | R |   |
| Attribute | Key Type | | --- | --- | |   | **EC private** | **EC public** | **RSA private** | **RSA public** | **AES** | **DES3** | **Generic Secret** |
| `CKA_CLASS` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | | `CKA_KEY_TYPE` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| `CKA_LABEL` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | | `CKA_ID` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| `CKA_LOCAL` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | | `CKA_TOKEN` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| `CKA_PRIVATE` | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | ✔[1](#pkcs11-v3-f8 "#pkcs11-v3-f8") | | `CKA_ENCRYPT` | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ | ✖ |
| `CKA_DECRYPT` | ✖ | ✖ | ✔ | ✖ | ✔ | ✔ | ✖ | | `CKA_DERIVE` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| `CKA_MODIFIABLE` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | | `CKA_DESTROYABLE` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| `CKA_SIGN` | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | | `CKA_SIGN_RECOVER` | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |
| `CKA_VERIFY` | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | ✔ | | `CKA_VERIFY_RECOVER` | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ |
| `CKA_WRAP` | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ | ✖ | | `CKA_WRAP_TEMPLATE` | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | ✖ |
| `CKA_TRUSTED` | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | ✔ | | `CKA_WRAP_WITH_TRUSTED` | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ |
| `CKA_UNWRAP` | ✖ | ✖ | ✔ | ✖ | ✔ | ✔ | ✖ | | `CKA_UNWRAP_TEMPLATE` | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✖ |
| `CKA_SENSITIVE` | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | | `CKA_EXTRACTABLE` | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ |
| `CKA_NEVER_EXTRACTABLE` | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | | `CKA_ALWAYS_SENSITIVE` | R | R; | R | R | R | R | R |
| `CKA_MODULUS` | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | | `CKA_MODULUS_BITS` | ✖ | ✖ | ✖ |  ✔ | ✖ | ✖ | ✖ |
| `CKA_PRIME_1` | ✖ | ✖ | S | ✖ | ✖ | ✖ | ✖ | | `CKA_PRIME_2` | ✖ | ✖ | S | ✖ | ✖ | ✖ | ✖ |
| `CKA_COEFFICIENT` | ✖ | ✖ | S | ✖ | ✖ | ✖ | ✖ | | `CKA_EXPONENT_1` | ✖ | ✖ | S | ✖ | ✖ | ✖ | ✖ |
| `CKA_EXPONENT_2` | ✖ | ✖ | S | ✖ | ✖ | ✖ | ✖ | | `CKA_PRIVATE_EXPONENT` | ✖ | ✖ | S | ✖ | ✖ | ✖ | ✖ |
| `CKA_PUBLIC_EXPONENT` | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | | `CKA_EC_PARAMS` | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ |
| `CKA_EC_POINT` | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | | `CKA_VALUE` | S | ✖ | ✖ | ✖ | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") | ✔[2](#pkcs11-v3-f9 "#pkcs11-v3-f9") |
| `CKA_VALUE_LEN` | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | | `CKA_CHECK_VALUE` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | **Attribute annotations** <br>• [1] This attribute is partially supported by the firmware and must be explicitly set only to the default value. <br>• [2] Mandatory attribute. <br>• [3] **Client SDK 3 only**. The `CKA_SIGN_RECOVER` attribute is derived from the `CKA_SIGN` attribute. If being set, it can only be set to the same value that is set for `CKA_SIGN`. If not set, it derives the default value of `CKA_SIGN`. Since CloudHSM only supports RSA-based recoverable signature mechanisms, this attribute is currently applicable to RSA public keys only. <br>• [4] **Client SDK 3 only**. The `CKA_VERIFY_RECOVER` attribute is derived from the `CKA_VERIFY` attribute. If being set, it can only be set to the same value that is set for `CKA_VERIFY`. If not set, it derives the default value of `CKA_VERIFY`. Since CloudHSM only supports RSA-based recoverable signature mechanisms, this attribute is currently applicable to RSA public keys only.
