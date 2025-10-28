# NCryptFreeObject with Key storage provider (KSP)

The `NCryptFreeObject` function releases provider or key handle from
the Key Storage Provider (KSP).

## Parameters

`hObject` [in]

The handle of the object to release. You can use:

- A provider handle (`NCRYPT_PROV_HANDLE`)
- A key handle (`NCRYPT_KEY_HANDLE`)

## Return Value

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code        | Description                           |
| ------------------ | ------------------------------------- |
| ERROR_SUCCESS      | The operation completed successfully. |
| NTE_INVALID_HANDLE | The handle in `hObject` is not valid. |
