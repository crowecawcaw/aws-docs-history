

# NCryptDeleteKey with Key storage provider (KSP)
<a name="ksp-library-apis-delete-key"></a>

The `NCryptDeleteKey` function deletes a KSP key from the Key Storage Provider (KSP).

## Parameters
<a name="ksp-library-apis-delete-key-parameters"></a>

 `hKey` [in]   
 The handle of the key to delete. 

`dwFlags` [in]  
Flags to modify the function's behavior. You can use zero or more of the following values:  



<table>
<thead>
  <tr><th>Value</th><th>Meaning</th></tr>
</thead>
<tbody>
  <tr><td>NCRYPT_SILENT_FLAG</td><td>This flag has no effect.</td></tr>
</tbody>
</table>


## Return Value
<a name="ksp-library-apis-delete-key-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The function was successful. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. | 
| NTE\_FAIL | The operation couldn't complete. | 
| NTE\_INVALID\_HANDLE | The handle in `hKey` is not valid. | 
| NTE\_INTERNAL\_ERROR | A internal error happened when deleting key. | 