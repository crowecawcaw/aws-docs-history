# NCryptExportKey with Key storage provider (KSP)

The `NCryptExportKey` function exports a KSP key to a memory BLOB. This function
only supports exporting public keys.

## Parameters

`hKey` [in]

The handle of the key to export.

`hExportKey` [in, unused]

AWS CloudHSM Key Storage Provider (KSP) doesn't use this parameter.

`pszBlobType` [in]

A null-terminated Unicode string that specifies the BLOB
type to export. AWS CloudHSM Key Storage Provider (KSP) supports the following values:

| Value                 | Meaning                                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| BCRYPT_RSAPUBLIC_BLOB | Exports an RSA public key. The `pbOutput`<br>buffer contains a `BCRYPT_RSAKEY_BLOB`<br>structure followed by the key data.    |
| BCRYPT_ECCPUBLIC_BLOB | Exports an ECC public key. The<br>`pbOutput` buffer contains a<br>`BCRYPT_ECCKEY_BLOB` structure followed<br>by the key data. |

`pParameterList` [in, unused]

AWS CloudHSM Key Storage Provider (KSP) doesn't use this parameter.

`pbOutput` [out, optional]

A buffer address to store the key BLOB. Specify the buffer size using
`cbOutput`. If set to NULL, the function stores the required
size (in bytes) in the DWORD pointed to by `pcbResult`.

`cbOutput` [in]

The size of the `pbOutput` buffer in bytes.

`pcbResult` [out]

A DWORD variable address that stores the number of bytes copied to the
`pbOutput` buffer. If `pbOutput` is NULL, the
function stores the required buffer size in bytes.

`dwFlags` [in]

Flags that modify how the function works. You can use zero or the
following:

| Value              | Meaning                  |
| ------------------ | ------------------------ |
| NCRYPT_SILENT_FLAG | This flag has no effect. |

## Return Value

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code           | Description                                                                |
| --------------------- | -------------------------------------------------------------------------- |
| ERROR_SUCCESS         | The operation completed successfully.                                      |
| NTE_INVALID_PARAMETER | One or more parameters are not valid.                                      |
| NTE_FAIL              | The operation couldn't complete.                                           |
| NTE_INVALID_HANDLE    | The handle in `hProvider` is not valid.                                    |
| NTE_BAD_FLAGS         | The `dwFlags` parameter contains an invalid<br>value.                      |
| NTE_BAD_KEY_STATE     | The key state is not valid.                                                |
| NTE_NOT_SUPPORTED     | The `pszBlobType` or `dwFlags` parameter<br>contains an unsupported value. |
| STATUS_INTERNAL_ERROR | An internal error happened during the operation.                           |
