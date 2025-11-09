# Certificate storage attributes

The following table lists the supported certificate object attributes and their values:

| Attribute                  | Default value                         | Description                                              |
| -------------------------- | ------------------------------------- | -------------------------------------------------------- |
| `CKA_CLASS`                | Required                              | Must be `CKO_CERTIFICATE`.                               |
| `CKA_TOKEN`                | True                                  | Must be `True`.                                          |
| `CKA_MODIFIABLE`           | True                                  | Must be `True`.                                          |
| `CKA_PRIVATE`              | False                                 | Must be `False`.                                         |
| `CKA_LABEL`                | Empty                                 | Limit 127 characters.                                    |
| `CKA_COPYABLE`             | False                                 | Must be `False`.                                         |
| `CKA_DESTROYABLE`          | True                                  | Must be `True`.                                          |
| `CKA_CERTIFICATE_TYPE`     | Required                              | Must be `CKC_X_509`.                                     |
| `CKA_TRUSTED`              | False                                 | Must be `False`.                                         |
| `CKA_CERTIFICATE_CATEGORY` | `CK_CERTIFICATE_CATEGORY_UNSPECIFIED` | Must be<br>`CK_CERTIFICATE_CATEGORY_UNSPECIFIED`.        |
| `CKA_CHECK_VALUE`          | Derived from `CKA_VALUE`              | Automatically set based on<br>`CKA_VALUE`.               |
| `CKA_START_DATE`           | Empty                                 | The certificate 'not before' date.                       |
| `CKA_END_DATE`             | Empty                                 | The certificate 'not after' date.                        |
| `CKA_PUBLIC_KEY_INFO`      | Empty                                 | Maximum size is 16 kilobytes.                            |
| `CKA_SUBJECT`              | Required                              | The certificate subject.                                 |
| `CKA_ID`                   | Empty                                 | Maximum size is 128 bytes. Uniqueness isn't<br>enforced. |
| `CKA_ISSUER`               | Empty                                 | The certificate issuer.                                  |
| `CKA_SERIAL_NUMBER`        | Empty                                 | The certificate serial number.                           |
| `CKA_VALUE`                | Required                              | Maximum size is 32 kilobytes.                            |
