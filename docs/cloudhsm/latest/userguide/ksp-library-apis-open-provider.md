

# NCryptOpenStorageProvider function with Key Storage Provider (KSP)
<a name="ksp-library-apis-open-provider"></a>

The `NCryptOpenStorageProvider` function loads and initializes the Key Storage Provider (KSP).

## Parameters
<a name="ksp-library-apis-open-provider-parameters"></a>

 `phProvider` [out]   
A pointer to a `NCRYPT_PROV_HANDLE` variable that stores the provider handle.

 `pszProviderName` [in]   
A pointer to a null-terminated Unicode string identifying the key storage provider. AWS CloudHSM Key Storage Provider (KSP) supports the following values:  



<table>
<thead>
  <tr><th>Value</th><th>Meaning</th></tr>
</thead>
<tbody>
  <tr><td>L"CloudHSM Key Storage Provider"</td><td>Identifies Client SDK 5 provider name. We recommend using this name by default.</td></tr>
  <tr><td>L"Cavium Key Storage Provider"</td><td>Identifies the Client SDK 3 provider name. Supported for backward compatibility.</td></tr>
</tbody>
</table>

Values are wide-character string literal, as indicated by L before the literal.

`dwFlags` [in]  
Flags that modify the behavior of the function. No flags are defined for this function.

## Return Value
<a name="ksp-library-apis-open-provider-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_FAIL | The operation couldn't complete. | 