# NCryptOpenKey with Key storage provider (KSP)

The `NCryptOpenKey` function opens a key that exists in the
Key Storage Provider (KSP).

## Parameters

`hProvider` [in]

The KSP handle that contains the key. Use [NCryptOpenStorageProvider](ksp-library-apis-open-provider.md "ksp-library-apis-open-provider.md") to get the handle.

`phKey` [out]

A pointer to a `NCRYPT_KEY_HANDLE` variable that stores the key
handle.

`pszKeyName` [in]

A pointer to a null-terminated Unicode string containing the key
name.

`dwLegacyKeySpec` [in, unused]

AWS CloudHSM Key Storage Provider (KSP) doesn't use this parameter.

`dwFlags` [in]

Flags that modify function's behavior. No flags are defined for this
function.

## Return Value

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code           | Description                                         |
| --------------------- | --------------------------------------------------- |
| ERROR_SUCCESS         | The operation completed successfully.               |
| NTE_INVALID_PARAMETER | One or more parameters are not valid.               |
| NTE_FAIL              | The operation couldn't complete.                    |
| NTE_INVALID_HANDLE    | The handle in `hProvider` is not valid.             |
| NTE_BAD_KEYSET        | The key name provided did not return unique result. |
