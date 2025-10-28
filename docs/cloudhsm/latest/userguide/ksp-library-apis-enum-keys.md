# NCryptEnumKeys with Key storage provider (KSP)

NCryptEnumKeys function lists the keys stored in the Key Storage Provider (KSP).

## Parameters

`hProvider` [in]

The key storage provider handle. Use [NCryptOpenStorageProvider](ksp-library-apis-open-provider.md "ksp-library-apis-open-provider.md") to get this handle.

`pszScope` [in, unused]

Set this parameter to NULL.

`ppKeyName` [out]

A pointer address to an `NCryptKeyName` structure that stores
the key name. To free this memory after use, call `NCryptFreeBuffer`.

`ppEnumState` [in, out]

A VOID pointer address that tracks the enumeration progress. The key
storage provider uses this information internally to manage the enumeration
sequence. To start a new enumeration from the beginning, set this pointer to
NULL.

To free this memory after completing the enumeration, pass this pointer to
the `NCryptFreeBuffer`.

`dwFlags` [in]

Flags to modify the function's behavior. This function has no
flags.

## Return Value

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code           | Description                                    |
| --------------------- | ---------------------------------------------- |
| ERROR_SUCCESS         | The operation completed successfully.          |
| NTE_INVALID_PARAMETER | One or more parameters are not valid.          |
| NTE_FAIL              | The operation couldn't complete.               |
| NTE_INVALID_HANDLE    | The handle in `hProvider` is not valid.        |
| NTE_NO_MORE_ITEMS     | The enumeration has listed all available keys. |
