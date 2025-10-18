# NCryptFreeBuffer with Key storage provider (KSP)

The `NCryptFreeBuffer` function releases a block of memory that was allocated by the Key Storage Provider (KSP).


## Parameters





`pvInput` [in] 

 The address of the memory to released. 




## Return Value


The function returns a status code to indicate success or failure.


Common return codes include:




| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_FAIL | The operation couldn't complete. |
