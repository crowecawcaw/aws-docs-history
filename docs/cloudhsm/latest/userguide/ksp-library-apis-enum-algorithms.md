

# NCryptEnumAlgorithms with Key storage provider (KSP)
<a name="ksp-library-apis-enum-algorithms"></a>

The `NCryptEnumAlgorithms` function retrieves the names of algorithms that the Key Storage Provider (KSP) supports.

## Parameters
<a name="ksp-library-apis-enum-algorithms-parameters"></a>

 `hProvider` [in]   
 The handle of the key storage provider for which to enumerate the algorithms. Use the [`NCryptOpenStorageProvider`](ksp-library-apis-open-provider.md) function to get this handle. 

 `dwAlgOperations` [in]   
A set of values that specify which algorithm classes to enumerate. You can use zero to enumerate all algorithms, or combine one or more of these values:   



<table>
<thead>
  <tr><th>Value</th><th>Meaning</th></tr>
</thead>
<tbody>
  <tr><td>NCRYPT_ASYMMETRIC_ENCRYPTION_OPERATION<br />0x00000004</td><td>List the asymmetric encryption algorithms.</td></tr>
  <tr><td>NCRYPT_SIGNATURE_OPERATION<br />0x00000010</td><td>List the digital signature algorithms.</td></tr>
</tbody>
</table>


`pdwAlgCount` [out]  
The address of a DWORD that stores the number of elements in the `ppAlgList` array.

`ppAlgList` [out]  
The address of an `NCryptAlgorithmName` structure pointer that stores an array of registered algorithm names. The `pdwAlgCount` parameter indicates the number of elements in this array.

`dwFlags` [in]  
Flags to modify the function's behavior. Use zero or the following value:  



<table>
<thead>
  <tr><th>Value</th><th>Meaning</th></tr>
</thead>
<tbody>
  <tr><td>NCRYPT_SILENT_FLAG</td><td>This flag has no effect.</td></tr>
</tbody>
</table>


## Return Value
<a name="ksp-library-apis-open-key-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_FAIL | The operation couldn't complete. | 
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. | 
| NTE\_NOT\_SUPPORTED | The `dwAlgOperations` parameter contains an unsupported value. | 