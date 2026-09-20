

# NCryptGetProperty with Key storage provider (KSP)
<a name="ksp-library-apis-get-property"></a>

The `NCryptGetProperty` function retrieves property values for a key storage object.

## Parameters
<a name="ksp-library-apis-create-get-property-parameters"></a>

 `hObject` [in]   
 The handle of the object whose property you want to retrieve. You can use:  
+ A provider handle (`NCRYPT_PROV_HANDLE`)
+ A key handle (`NCRYPT_KEY_HANDLE`)

 `pszProperty ` [in]   
A pointer to a null-terminated Unicode string containing the property name to retrieve.   
When using `NCRYPT_PROV_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:  



<table>
<thead>
  <tr><th>Identifier/Value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>NCRYPT_IMPL_TYPE_PROPERTY<br />L"Impl Type"</td><td>A DWORD containing flags that define provider implementation details</td></tr>
  <tr><td>NCRYPT_MAX_NAME_LENGTH_PROPERTY<br />L"Max Name Length"</td><td>A DWORD containing the maximum length (in characters) for a persistent key name.</td></tr>
  <tr><td>NCRYPT_NAME_PROPERTY<br />L"Name"</td><td>A pointer to a null-terminated Unicode string containing the KSP name.</td></tr>
  <tr><td>NCRYPT_VERSION_PROPERTY<br />L"Version"</td><td>A DWORD containing the provider version (high word: major version, low word: minor version).</td></tr>
  <tr><td>NCRYPT_USE_CONTEXT_PROPERTY<br />L"Use Context"</td><td>A pointer to a null-terminated Unicode string describing the operation context.</td></tr>
  <tr><td>NCRYPT_SECURITY_DESCR_SUPPORT_PROPERTY<br />L"Security Descr Support"</td><td>Indicates if the provider supports security descriptors for keys.</td></tr>
</tbody>
</table>

When using `NCRYPT_KEY_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:  



<table>
<thead>
  <tr><th>Identifier/Value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>NCRYPT_ALGORITHM_PROPERTY<br />L"Algorithm Name"</td><td>A null-terminated Unicode string containing the key's algorithm name.</td></tr>
  <tr><td>NCRYPT_BLOCK_LENGTH_PROPERTY<br />L"Block Length"</td><td>A DWORD containing the encryption block length in bytes.</td></tr>
  <tr><td>NCRYPT_EXPORT_POLICY_PROPERTY<br />L"Export Policy"</td><td>A DWORD containing flags that specify the persisted key's export policy.</td></tr>
  <tr><td>NCRYPT_KEY_USAGE_PROPERTY<br />L"Key Usage"</td><td>A DWORD containing flags that define key usage details.</td></tr>
  <tr><td>NCRYPT_KEY_TYPE_PROPERTY<br />L"Key Type"</td><td>A DWORD containing flags that define the key type.</td></tr>
  <tr><td>NCRYPT_LENGTH_PROPERTY<br />L"Length"</td><td>A DWORD containing the key length in bits.</td></tr>
  <tr><td>NCRYPT_LENGTHS_PROPERTY<br />L"Lengths"</td><td>A pointer to an NCRYPT_SUPPORTED_LENGTHS structure containing supported key sizes.</td></tr>
  <tr><td>NCRYPT_NAME_PROPERTY<br />L"Name"</td><td>A pointer to a null-terminated Unicode string containing the key name.</td></tr>
  <tr><td>NCRYPT_SECURITY_DESCR_PROPERTY<br />L"Security Descr"</td><td>A pointer to a SECURITY_DESCRIPTOR structure containing key access control information.</td></tr>
  <tr><td>NCRYPT_ALGORITHM_GROUP_PROPERTY<br />L"Algorithm Group"</td><td>A null-terminated Unicode string containing the object's algorithm group name.</td></tr>
  <tr><td>NCRYPT_UNIQUE_NAME_PROPERTY<br />L"Unique Name"</td><td>A pointer to a null-terminated Unicode string containing the key's unique name.</td></tr>
</tbody>
</table>

Values are wide-character string literal, as indicated by L before the literal.

 `pbOutput` [out]   
The address of a buffer to store the property value. Specify the buffer size using `cbOutput`.  
To determine the required buffer size, set this parameter to NULL. The function stores the required size (in bytes) in the location pointed to by `pcbResult`.

 `cbOutput` [in]   
 The size of the `pbOutput` buffer in bytes.

`pcbResult` [out]  
A pointer to a DWORD variable that stores the number of bytes copied to the`pbOutput` buffer.  
If the `pbOutput` is NULL, this stores the required size (in bytes).

`dwFlags` [in]  
Flags to modify the function's behavior. You can use zero or:  



<table>
<thead>
  <tr><th>Value</th><th>Meaning</th></tr>
</thead>
<tbody>
  <tr><td>NCRYPT_SILENT_FLAG</td><td>This flag has no effect.</td></tr>
</tbody>
</table>

When pszProperty is `NCRYPT_SECURITY_DESCR_PROPERTY`, use one or a combination of:  



<table>
<thead>
  <tr><th>Value</th><th>Meaning</th></tr>
</thead>
<tbody>
  <tr><td>OWNER_SECURITY_INFORMATION</td><td>This flag has no effect.</td></tr>
  <tr><td>GROUP_SECURITY_INFORMATION</td><td>This flag has no effect.</td></tr>
  <tr><td>DACL_SECURITY_INFORMATION</td><td>This flag has no effect.</td></tr>
  <tr><td>LABEL_SECURITY_INFORMATION</td><td>This flag has no effect.</td></tr>
  <tr><td>SACL_SECURITY_INFORMATION</td><td>This flag has no effect.</td></tr>
</tbody>
</table>


## Return Value
<a name="ksp-library-apis-get-property-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_FAIL | The operation couldn't complete. | 
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. | 
| NTE\_NOT\_SUPPORTED | The `pszAlgId` parameter contains a value that is not supported. | 
| NTE\_INVALID\_HANDLE | The handle in `hObject` is not valid. | 
| NTE\_BUFFER\_TOO\_SMALL | The `cbOutput` parameter is too small for return values. | 