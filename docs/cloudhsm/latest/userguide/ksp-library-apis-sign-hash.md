# NCryptSignHash with Key storage provider (KSP)

The `NCryptSignHash` function creates a signature of a hash
value.

## Parameters

`hKey` [in]

The handle of the key to use to sign the hash.

`pPaddingInfo` [in, optional]

A pointer to a structure containing padding information. The structure
type depends on the `dwFlags` value. Use this parameter only with
asymmetric keys; set to NULL for other key types.

`pbHashValue` [in]

A pointer to a buffer containing the hash value to sign. Specify the
buffer size using `cbHashValue`.

`cbHashValue` [in]

The size, in bytes, of the `pbHashValue` buffer to sign.

`pbSignature` [out]

The address of a buffer to store the signature. Specify the buffer size
using `cbSignature`.

To determine the required buffer size, set this parameter to NULL. The
function stores the required size (in bytes) in the location pointed to by
`pcbResult`.

`cbSignature` [in]

The size of the `pbSignature` buffer in bytes. The function
ignores this parameter if `pbSignature` is NULL.

`pcbResult` [out]

A pointer to a DWORD variable that stores the number of bytes copied to
the `pbSignature` buffer.

If `pbSignature` is NULL, this stores the required buffer size,
in bytes.

`dwFlags` [in]

Flags to modify the function's behavior. The allowed flags depend on your
key type. Use one of these values:

| Value              | Meaning                                                                                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| BCRYPT_PAD_PKCS1   | Uses the PKCS1 padding scheme. Set<br>`pPaddingInfo` to point to<br>a `BCRYPT_PKCS1_PADDING_INFO`<br>structure.                                     |
| BCRYPT_PAD_PSS     | Uses the Probabilistic Signature Scheme (PSS) padding<br>scheme. Set `pPaddingInfo` parameter to point<br>to a `BCRYPT_PSS_PADDING_INFO` structure. |
| NCRYPT_SILENT_FLAG | This flag has no effect.                                                                                                                            |

## Return Value

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code           | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| ERROR_SUCCESS         | The operation completed successfully.                        |
| NTE_INVALID_PARAMETER | One or more parameters are not valid.                        |
| NTE_FAIL              | The operation couldn't complete.                             |
| NTE_INVALID_HANDLE    | The handle in `hKey` is not valid.                           |
| NTE_BAD_FLAGS         | The `dwFlags` parameter contains an invalid<br>value.        |
| NTE_BUFFER_TOO_SMALL  | The `pcbOutput` parameter is too small for return<br>values. |
| NTE_BAD_KEY_STATE     | The key state is not valid.                                  |
| NTE_INTERNAL_ERROR    | An internal error happened when signing the hash.            |
