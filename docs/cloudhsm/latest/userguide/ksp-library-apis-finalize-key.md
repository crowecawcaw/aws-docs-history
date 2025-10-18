# NCryptFinalizeKey with Key storage provider (KSP)

The `NCryptFinalizeKey` function completes a KSP key. You must call
 this function before you can use the key.


## Parameters





`hKey` [in] 

 The handle of the key to complete. Get this handle by calling the
 [NCryptCreatePersistedKey](ksp-library-apis-create-persisted-key.md "ksp-library-apis-create-persisted-key.md") function.



`dwFlags` [in]

Flags to modify the function's behavior. You can use zero or these values:




| Value | Meaning |
| --- | --- |
| NCRYPT\_SILENT\_FLAG | This flag has no effect. |
| NCRYPT\_NO\_KEY\_VALIDATION | This flag has no effect. | ## Return Value The function returns a status code to indicate success or failure. Common return codes include:
| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_FAIL | The operation couldn't complete. |
| NTE\_INVALID\_HANDLE | The handle in `hKey` is not valid. |
| NTE\_NOT\_SUPPORTED | The `dwFlags` parameter contains a value that is not supported. |
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. |
