# NCryptDeleteKey with Key storage provider (KSP)

The `NCryptDeleteKey` function deletes a KSP key from the Key Storage Provider (KSP).


## Parameters





`hKey` [in] 

 The handle of the key to delete. 



`dwFlags` [in]

Flags to modify the function's behavior. You can use zero or more of the
 following values:




| Value | Meaning |
| --- | --- |
| NCRYPT\_SILENT\_FLAG | This flag has no effect. | ## Return Value The function returns a status code to indicate success or failure. Common return codes include:
| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The function was successful. |
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. |
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. |
| NTE\_FAIL | The operation couldn't complete. |
| NTE\_INVALID\_HANDLE | The handle in `hKey` is not valid. |
| NTE\_INTERNAL\_ERROR | A internal error happened when deleting key. |
