

# NCryptFreeObject with Key storage provider (KSP)
<a name="ksp-library-apis-free-object"></a>

The `NCryptFreeObject` function releases provider or key handle from the Key Storage Provider (KSP).

## Parameters
<a name="ksp-library-apis-free-object-parameters"></a>

 `hObject` [in]   
 The handle of the object to release. You can use:  
+ A provider handle (`NCRYPT_PROV_HANDLE`)
+ A key handle (`NCRYPT_KEY_HANDLE`)

## Return Value
<a name="ksp-library-apis-free-object-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_HANDLE | The handle in `hObject` is not valid. | 