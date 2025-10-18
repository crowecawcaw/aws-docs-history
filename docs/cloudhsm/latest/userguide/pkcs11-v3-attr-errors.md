# Interpreting PKCS #11 library error codes for AWS CloudHSM Client SDK 3

Specifying in the template a PKCS #11 library attribute that is not supported by a specific key results
 in an error. The following table contains error codes that are generated when you violate
 specifications:



| **Error Code** | **Description** |
| --- | --- |
| `CKR_TEMPLATE_INCONSISTENT` | You receive this error when you specify an attribute in the attribute template, where the attribute complies with the PKCS #11 specification, but is not supported by CloudHSM. |
| `CKR_ATTRIBUTE_TYPE_INVALID` | You receive this error when you retrieve value for an attribute, which complies with the PKCS #11 specification, but is not supported by CloudHSM. |
| `CKR_ATTRIBUTE_INCOMPLETE` | You receive this error when you do not specify the mandatory attribute in the attribute template. |
| `CKR_ATTRIBUTE_READ_ONLY` | You receive this error when you specify a read-only attribute in the attribute template. |
