# NCryptGetProperty with Key storage provider (KSP)

The `NCryptGetProperty` function retrieves property values for a key
 storage object.


## Parameters





`hObject` [in] 

 The handle of the object whose property you want to retrieve. You can
 use:



* A provider handle (`NCRYPT_PROV_HANDLE`)
* A key handle (`NCRYPT_KEY_HANDLE`)



`pszProperty`  [in] 

A pointer to a null-terminated Unicode string containing the property name
 to retrieve. 


When using `NCRYPT_PROV_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the
 following KSP identifiers:




| Identifier/Value | Description |
| --- | --- |
| NCRYPT\_IMPL\_TYPE\_PROPERTY L"Impl Type" | A DWORD containing flags that define provider implementation details |
| NCRYPT\_MAX\_NAME\_LENGTH\_PROPERTY L"Max Name Length" | A DWORD containing the maximum length (in characters) for a persistent key name. |
| NCRYPT\_NAME\_PROPERTY L"Name" | A pointer to a null-terminated Unicode string containing the KSP name. |
| NCRYPT\_VERSION\_PROPERTY L"Version" | A DWORD containing the provider version (high word: major version, low word: minor version). |
| NCRYPT\_USE\_CONTEXT\_PROPERTY L"Use Context" | A pointer to a null-terminated Unicode string describing the operation context. |
| NCRYPT\_SECURITY\_DESCR\_SUPPORT\_PROPERTY L"Security Descr Support" | Indicates if the provider supports security descriptors for keys. | When using `NCRYPT_KEY_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:
| Identifier/Value | Description |
| --- | --- |
| NCRYPT\_ALGORITHM\_PROPERTY L"Algorithm Name" | A null-terminated Unicode string containing the key's algorithm name. |
| NCRYPT\_BLOCK\_LENGTH\_PROPERTY L"Block Length" | A DWORD containing the encryption block length in bytes. |
| NCRYPT\_EXPORT\_POLICY\_PROPERTY L"Export Policy" | A DWORD containing flags that specify the persisted key's export policy. |
| NCRYPT\_KEY\_USAGE\_PROPERTY L"Key Usage" | A DWORD containing flags that define key usage details. |
| NCRYPT\_KEY\_TYPE\_PROPERTY L"Key Type" | A DWORD containing flags that define the key type. |
| NCRYPT\_LENGTH\_PROPERTY L"Length" | A DWORD containing the key length in bits. |
| NCRYPT\_LENGTHS\_PROPERTY L"Lengths" | A pointer to an NCRYPT\_SUPPORTED\_LENGTHS structure containing supported key sizes. |
| NCRYPT\_NAME\_PROPERTY L"Name" | A pointer to a null-terminated Unicode string containing the key name. |
| NCRYPT\_SECURITY\_DESCR\_PROPERTY L"Security Descr" | A pointer to a SECURITY\_DESCRIPTOR structure containing key access control information. |
| NCRYPT\_ALGORITHM\_GROUP\_PROPERTY L"Algorithm Group" | A null-terminated Unicode string containing the object's algorithm group name. |
| NCRYPT\_UNIQUE\_NAME\_PROPERTY L"Unique Name" | A pointer to a null-terminated Unicode string containing the key's unique name. | ###### Note Values are wide-character string literal, as indicated by L before the literal. `pbOutput` [out] The address of a buffer to store the property value. Specify the buffer size using `cbOutput`. To determine the required buffer size, set this parameter to NULL. The function stores the required size (in bytes) in the location pointed to by `pcbResult`. `cbOutput` [in] The size of the `pbOutput` buffer in bytes. `pcbResult` [out] A pointer to a DWORD variable that stores the number of bytes copied to the`pbOutput` buffer. If the `pbOutput` is NULL, this stores the required size (in bytes). `dwFlags` [in] Flags to modify the function's behavior. You can use zero or:
| Value | Meaning |
| --- | --- |
| NCRYPT\_SILENT\_FLAG | This flag has no effect. | When pszProperty is `NCRYPT_SECURITY_DESCR_PROPERTY`, use one or a combination of:
| Value | Meaning |
| --- | --- |
| OWNER\_SECURITY\_INFORMATION | This flag has no effect. |
| GROUP\_SECURITY\_INFORMATION | This flag has no effect. |
| DACL\_SECURITY\_INFORMATION | This flag has no effect. |
| LABEL\_SECURITY\_INFORMATION | This flag has no effect. |
| SACL\_SECURITY\_INFORMATION | This flag has no effect. | ## Return Value The function returns a status code to indicate success or failure. Common return codes include:
| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. |
| NTE\_FAIL | The operation couldn't complete. |
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. |
| NTE\_NOT\_SUPPORTED | The `pszAlgId` parameter contains a value that is not supported. |
| NTE\_INVALID\_HANDLE | The handle in `hObject` is not valid. |
| NTE\_BUFFER\_TOO\_SMALL | The `cbOutput` parameter is too small for return values. |
