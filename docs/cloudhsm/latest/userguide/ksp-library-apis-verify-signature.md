# NCryptVerifySignature with

Key storage provider (KSP)

The `NCryptVerifySignature` function confirms whether a signature
matches a specified hash.

## Parameters

`hKey` [in]

The handle of the key to use to decrypt the signature. You must use the
public key portion of the key pair that was used to sign the data with
the [NCryptSignHash](ksp-library-apis-sign-hash.md "ksp-library-apis-sign-hash.md").

`pPaddingInfo` [in, optional]

A pointer to a structure containing padding information. The structure
type depends on the `dwFlags` value. Use this parameter only with
asymmetric keys; set to NULL for other key types.

`pbHashValue` [in]

A pointer to a buffer containing the hash value to sign. Specify the
buffer size using `cbHashValue`.

`cbHashValue` [in]

The size of the `pbHashValue` buffer in bytes.

`pbSignature` [out]

The address of a buffer containing the signed hash of the data. Use [NCryptSignHash](ksp-library-apis-sign-hash.md "ksp-library-apis-sign-hash.md") to create
this signature. Specify the buffer size using
`cbSignature`.

`cbSignature` [in]

The size of the `pbSignature` buffer in bytes. Use [NCryptSignHash](ksp-library-apis-sign-hash.md "ksp-library-apis-sign-hash.md") to create the
signature.

`dwFlags` [in]

Flags to modify the function's behavior. The allowed flags depend on your
key type. Use one of these values:

| Value                 | Meaning                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NCRYPT_PAD_PKCS1_FLAG | Indicates the signature used PKCS1 padding. Set<br>`pPaddingInfo` to point to a<br>`BCRYPT_PKCS1_PADDING_INFO`<br>structure.                              |
| NCRYPT_PAD_PSS_FLAG   | Indicates the signature used Probabilistic Signature<br>Scheme (PSS) padding. Set `pPaddingInfo` to<br>point to a `BCRYPT_PSS_PADDING_INFO`<br>structure. |
| NCRYPT_SILENT_FLAG    | This flag has no effect.                                                                                                                                  |

## Return Value

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code           | Description                                               |
| --------------------- | --------------------------------------------------------- |
| ERROR_SUCCESS         | The operation completed successfully.                     |
| NTE_INVALID_PARAMETER | One or more parameters are not valid.                     |
| NTE_FAIL              | The operation couldn't complete.                          |
| NTE_INVALID_HANDLE    | The handle in `hKey` is not valid.                        |
| NTE_BAD_FLAGS         | The `dwFlags` parameter contains an invalid<br>value.     |
| NTE_BAD_SIGNATURE     | The signature was not verified.                           |
| NTE_BAD_KEY_STATE     | The key state is not valid.                               |
| NTE_INTERNAL_ERROR    | An internal error happened while verifying the signature. |
