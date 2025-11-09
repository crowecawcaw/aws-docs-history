# NCryptOpenStorageProvider function with

Key Storage Provider (KSP)

The `NCryptOpenStorageProvider` function loads and initializes the Key Storage Provider (KSP).

## Parameters

`phProvider` [out]

A pointer to a `NCRYPT_PROV_HANDLE` variable that stores the
provider handle.

`pszProviderName` [in]

A pointer to a null-terminated Unicode string identifying the key
storage provider. AWS CloudHSM Key Storage Provider (KSP) supports the following
values:

| Value                            | Meaning                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| L"CloudHSM Key Storage Provider" | Identifies Client SDK 5 provider name. We<br>recommend using this name by default.  |
| L"Cavium Key Storage Provider"   | Identifies the Client SDK 3 provider name. Supported for<br>backward compatibility. |

###### Note

Values are wide-character string literal, as indicated by L before the
literal.

`dwFlags` [in]

Flags that modify the behavior of the function. No flags are defined for
this function.

## Return Value

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code           | Description                           |
| --------------------- | ------------------------------------- |
| ERROR_SUCCESS         | The operation completed successfully. |
| NTE_INVALID_PARAMETER | One or more parameters are not valid. |
| NTE_FAIL              | The operation couldn't complete.      |
