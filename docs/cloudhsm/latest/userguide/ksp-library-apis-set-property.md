

# NCryptSetProperty with Key storage provider (KSP)
<a name="ksp-library-apis-set-property"></a>

The `NCryptSetProperty` function sets property values for a key storage object.

## Parameters
<a name="ksp-library-apis-create-set-property-parameters"></a>

 `hObject` [in]   
 The handle of the object whose property you want to set. You can use:  
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
  <tr><td>NCRYPT_USE_CONTEXT_PROPERTY<br />L"Use Context"</td><td>A pointer to a null-terminated Unicode string describing the operation context.</td></tr>
</tbody>
</table>

When using `NCRYPT_KEY_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:  



<table>
<thead>
  <tr><th>Identifier/Value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>NCRYPT_KEY_USAGE_PROPERTY<br />L"Key Usage"</td><td>A DWORD containing a set of flags that define key usage details. This property only applies to keys. This can contain zero or a combination of one or more of the following values.<br />NCRYPT_ALLOW_DECRYPT_FLAG (0x00000001)<br />NCRYPT_ALLOW_SIGNING_FLAG (0x00000002)</td></tr>
  <tr><td>NCRYPT_LENGTH_PROPERTY<br />L"Length"</td><td>A DWORD containing the key length in bits.</td></tr>
  <tr><td>NCRYPT_EXPORT_POLICY_PROPERTY<br />L"Export Policy"</td><td>A DWORD containing flags that specify the persisted key's export policy. This can contain zero or a combination of one or more of the following values.<br />NCRYPT_ALLOW_EXPORT_FLAG (0x00000001)</td></tr>
</tbody>
</table>

Values are wide-character string literal, as indicated by L before the literal.

 `pbInput` [in]   
 The address of a buffer that contains the new property value. `cbInput` contains the size of the buffer. 

 `cbInput` [in]   
 The size of the `pbInput` buffer in bytes. 

`dwFlags` [in]  
Flags that modify function's behavior. No flags are defined for this function.

## Return Value
<a name="ksp-library-apis-set-property-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_FAIL | The operation couldn't complete. | 
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. | 
| NTE\_NOT\_SUPPORTED | The `pszProperty` parameter contains a value that is not supported. | 
| NTE\_INVALID\_HANDLE | The handle in `hObject` is not valid. | 
| NTE\_BAD\_DATA | The data pointed by `pbInput` and `cbInput` is not valid. | 