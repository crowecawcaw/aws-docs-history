

# NCryptExportKey with Key storage provider (KSP)
<a name="ksp-library-apis-export-key"></a>

The `NCryptExportKey` function exports a KSP key to a memory BLOB. This function only supports exporting public keys.

## Parameters
<a name="ksp-library-apis-export-key-parameters"></a>

 `hKey` [in]  
The handle of the key to export.

 `hExportKey` [in, unused]  
 AWS CloudHSM Key Storage Provider (KSP) doesn't use this parameter. 

`pszBlobType` [in]  
A null-terminated Unicode string that specifies the BLOB type to export. AWS CloudHSM Key Storage Provider (KSP) supports the following values:  



<table>
<thead>
  <tr><th>Value</th><th>Meaning</th></tr>
</thead>
<tbody>
  <tr><td>BCRYPT_RSAPUBLIC_BLOB</td><td>Exports an RSA public key. The <code>pbOutput</code> buffer contains a <code>BCRYPT_RSAKEY_BLOB</code> structure followed by the key data.</td></tr>
  <tr><td>BCRYPT_ECCPUBLIC_BLOB</td><td>Exports an ECC public key. The <code>pbOutput</code> buffer contains a <code>BCRYPT_ECCKEY_BLOB</code> structure followed by the key data.</td></tr>
</tbody>
</table>


`pParameterList` [in, unused]  
AWS CloudHSM Key Storage Provider (KSP) doesn't use this parameter.

`pbOutput` [out, optional]  
A buffer address to store the key BLOB. Specify the buffer size using `cbOutput`. If set to NULL, the function stores the required size (in bytes) in the DWORD pointed to by `pcbResult`.

`cbOutput` [in]  
The size of the `pbOutput` buffer in bytes.

`pcbResult` [out]  
A DWORD variable address that stores the number of bytes copied to the `pbOutput` buffer. If `pbOutput` is NULL, the function stores the required buffer size in bytes.

`dwFlags` [in]  
Flags that modify how the function works. You can use zero or the following:  



<table>
<thead>
  <tr><th>Value</th><th>Meaning</th></tr>
</thead>
<tbody>
  <tr><td>NCRYPT_SILENT_FLAG</td><td>This flag has no effect.</td></tr>
</tbody>
</table>


## Return Value
<a name="ksp-library-apis-export-key-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_FAIL | The operation couldn't complete. | 
| NTE\_INVALID\_HANDLE | The handle in `hProvider` is not valid. | 
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. | 
| NTE\_BAD\_KEY\_STATE | The key state is not valid. | 
| NTE\_NOT\_SUPPORTED | The `pszBlobType` or `dwFlags` parameter contains an unsupported value. | 
| STATUS\_INTERNAL\_ERROR | An internal error happened during the operation. | 