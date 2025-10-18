# NCryptSetProperty with Key storage provider (KSP)

The `NCryptSetProperty` function sets property values for a key storage
 object.


## Parameters





`hObject` [in] 

 The handle of the object whose property you want to set. You can use:



* A provider handle (`NCRYPT_PROV_HANDLE`)
* A key handle (`NCRYPT_KEY_HANDLE`)



`pszProperty`  [in] 

A pointer to a null-terminated Unicode string containing the property name
 to retrieve. 


When using `NCRYPT_PROV_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the
 following KSP identifiers:




| Identifier/Value | Description |
| --- | --- |
| NCRYPT\_USE\_CONTEXT\_PROPERTY L"Use Context" | A pointer to a null-terminated Unicode string describing the operation context. | When using `NCRYPT_KEY_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:
| Identifier/Value | Description |
| --- | --- |
| NCRYPT\_KEY\_USAGE\_PROPERTY L"Key Usage" | A DWORD containing a set of flags that define key usage details. This property only applies to keys. This can contain zero or a combination of one or more of the following values. NCRYPT\_ALLOW\_DECRYPT\_FLAG (0x00000001) NCRYPT\_ALLOW\_SIGNING\_FLAG (0x00000002) |
| NCRYPT\_LENGTH\_PROPERTY L"Length" | A DWORD containing the key length in bits. |
| NCRYPT\_EXPORT\_POLICY\_PROPERTY L"Export Policy" | A DWORD containing flags that specify the persisted key's export policy. This can contain zero or a combination of one or more of the following values. NCRYPT\_ALLOW\_EXPORT\_FLAG (0x00000001) | ###### Note Values are wide-character string literal, as indicated by L before the literal. `pbInput` [in] The address of a buffer that contains the new property value. `cbInput` contains the size of the buffer. `cbInput` [in] The size of the `pbInput` buffer in bytes. `dwFlags` [in] Flags that modify function's behavior. No flags are defined for this function. ## Return Value The function returns a status code to indicate success or failure. Common return codes include:
| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. |
| NTE\_FAIL | The operation couldn't complete. |
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. |
| NTE\_NOT\_SUPPORTED | The `pszProperty` parameter contains a value that is not supported. |
| NTE\_INVALID\_HANDLE | The handle in `hObject` is not valid. |
| NTE\_BAD\_DATA | The data pointed by `pbInput` and `cbInput` is not valid. |
