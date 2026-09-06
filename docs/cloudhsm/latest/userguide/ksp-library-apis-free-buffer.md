

# NCryptFreeBuffer with Key storage provider (KSP)
<a name="ksp-library-apis-free-buffer"></a>

The `NCryptFreeBuffer` function releases a block of memory that was allocated by the Key Storage Provider (KSP).

## Parameters
<a name="ksp-library-apis-free-buffer-parameters"></a>

 `pvInput` [in]   
 The address of the memory to released. 

## Return Value
<a name="ksp-library-apis-free-buffer-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_FAIL | The operation couldn't complete. | 