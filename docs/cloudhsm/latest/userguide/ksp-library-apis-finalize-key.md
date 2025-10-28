# NCryptFinalizeKey with Key storage provider (KSP)

The `NCryptFinalizeKey` function completes a KSP key. You must call
this function before you can use the key.

## Parameters

`hKey` [in]

The handle of the key to complete. Get this handle by calling the
[NCryptCreatePersistedKey](ksp-library-apis-create-persisted-key.md "ksp-library-apis-create-persisted-key.md") function.

`dwFlags` [in]

Flags to modify the function's behavior. You can use zero or these values:

| Value                    | Meaning                                                         |
| ------------------------ | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| NCRYPT_SILENT_FLAG       | This flag has no effect.                                        |
| NCRYPT_NO_KEY_VALIDATION | This flag has no effect.                                        | ## Return Value The function returns a status code to indicate success or failure. Common return codes include: |
| Return code              | Description                                                     |
| ---                      | ---                                                             |
| ERROR_SUCCESS            | The operation completed successfully.                           |
| NTE_FAIL                 | The operation couldn't complete.                                |
| NTE_INVALID_HANDLE       | The handle in `hKey` is not valid.                              |
| NTE_NOT_SUPPORTED        | The `dwFlags` parameter contains a value that is not supported. |
| NTE_BAD_FLAGS            | The `dwFlags` parameter contains an invalid value.              |
