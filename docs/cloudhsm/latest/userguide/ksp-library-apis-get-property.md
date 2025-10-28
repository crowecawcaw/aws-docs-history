# NCryptGetProperty with Key storage provider (KSP)

The `NCryptGetProperty` function retrieves property values for a key
storage object.

## Parameters

`hObject` [in]

The handle of the object whose property you want to retrieve. You can
use:

- A provider handle (`NCRYPT_PROV_HANDLE`)
- A key handle (`NCRYPT_KEY_HANDLE`)

`pszProperty` [in]

A pointer to a null-terminated Unicode string containing the property name
to retrieve.

When using `NCRYPT_PROV_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the
following KSP identifiers:

| Identifier/Value                                                 | Description                                                                                  |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NCRYPT_IMPL_TYPE_PROPERTY L"Impl Type"                           | A DWORD containing flags that define provider implementation details                         |
| NCRYPT_MAX_NAME_LENGTH_PROPERTY L"Max Name Length"               | A DWORD containing the maximum length (in characters) for a persistent key name.             |
| NCRYPT_NAME_PROPERTY L"Name"                                     | A pointer to a null-terminated Unicode string containing the KSP name.                       |
| NCRYPT_VERSION_PROPERTY L"Version"                               | A DWORD containing the provider version (high word: major version, low word: minor version). |
| NCRYPT_USE_CONTEXT_PROPERTY L"Use Context"                       | A pointer to a null-terminated Unicode string describing the operation context.              |
| NCRYPT_SECURITY_DESCR_SUPPORT_PROPERTY L"Security Descr Support" | Indicates if the provider supports security descriptors for keys.                            | When using `NCRYPT_KEY_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Identifier/Value                                                 | Description                                                                                  |
| ---                                                              | ---                                                                                          |
| NCRYPT_ALGORITHM_PROPERTY L"Algorithm Name"                      | A null-terminated Unicode string containing the key's algorithm name.                        |
| NCRYPT_BLOCK_LENGTH_PROPERTY L"Block Length"                     | A DWORD containing the encryption block length in bytes.                                     |
| NCRYPT_EXPORT_POLICY_PROPERTY L"Export Policy"                   | A DWORD containing flags that specify the persisted key's export policy.                     |
| NCRYPT_KEY_USAGE_PROPERTY L"Key Usage"                           | A DWORD containing flags that define key usage details.                                      |
| NCRYPT_KEY_TYPE_PROPERTY L"Key Type"                             | A DWORD containing flags that define the key type.                                           |
| NCRYPT_LENGTH_PROPERTY L"Length"                                 | A DWORD containing the key length in bits.                                                   |
| NCRYPT_LENGTHS_PROPERTY L"Lengths"                               | A pointer to an NCRYPT_SUPPORTED_LENGTHS structure containing supported key sizes.           |
| NCRYPT_NAME_PROPERTY L"Name"                                     | A pointer to a null-terminated Unicode string containing the key name.                       |
| NCRYPT_SECURITY_DESCR_PROPERTY L"Security Descr"                 | A pointer to a SECURITY_DESCRIPTOR structure containing key access control information.      |
| NCRYPT_ALGORITHM_GROUP_PROPERTY L"Algorithm Group"               | A null-terminated Unicode string containing the object's algorithm group name.               |
| NCRYPT_UNIQUE_NAME_PROPERTY L"Unique Name"                       | A pointer to a null-terminated Unicode string containing the key's unique name.              | ###### Note Values are wide-character string literal, as indicated by L before the literal. `pbOutput` [out] The address of a buffer to store the property value. Specify the buffer size using `cbOutput`. To determine the required buffer size, set this parameter to NULL. The function stores the required size (in bytes) in the location pointed to by `pcbResult`. `cbOutput` [in] The size of the `pbOutput` buffer in bytes. `pcbResult` [out] A pointer to a DWORD variable that stores the number of bytes copied to the`pbOutput` buffer. If the `pbOutput` is NULL, this stores the required size (in bytes). `dwFlags` [in] Flags to modify the function's behavior. You can use zero or: |
| Value                                                            | Meaning                                                                                      |
| ---                                                              | ---                                                                                          |
| NCRYPT_SILENT_FLAG                                               | This flag has no effect.                                                                     | When pszProperty is `NCRYPT_SECURITY_DESCR_PROPERTY`, use one or a combination of:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Value                                                            | Meaning                                                                                      |
| ---                                                              | ---                                                                                          |
| OWNER_SECURITY_INFORMATION                                       | This flag has no effect.                                                                     |
| GROUP_SECURITY_INFORMATION                                       | This flag has no effect.                                                                     |
| DACL_SECURITY_INFORMATION                                        | This flag has no effect.                                                                     |
| LABEL_SECURITY_INFORMATION                                       | This flag has no effect.                                                                     |
| SACL_SECURITY_INFORMATION                                        | This flag has no effect.                                                                     | ## Return Value The function returns a status code to indicate success or failure. Common return codes include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Return code                                                      | Description                                                                                  |
| ---                                                              | ---                                                                                          |
| ERROR_SUCCESS                                                    | The operation completed successfully.                                                        |
| NTE_INVALID_PARAMETER                                            | One or more parameters are not valid.                                                        |
| NTE_FAIL                                                         | The operation couldn't complete.                                                             |
| NTE_BAD_FLAGS                                                    | The `dwFlags` parameter contains an invalid value.                                           |
| NTE_NOT_SUPPORTED                                                | The `pszAlgId` parameter contains a value that is not supported.                             |
| NTE_INVALID_HANDLE                                               | The handle in `hObject` is not valid.                                                        |
| NTE_BUFFER_TOO_SMALL                                             | The `cbOutput` parameter is too small for return values.                                     |
