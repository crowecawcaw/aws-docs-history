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




| Value | Meaning |
| --- | --- |
| NCRYPT\_PAD\_PKCS1\_FLAG |  Indicates the signature used PKCS1 padding. Set `pPaddingInfo` to point to a `BCRYPT_PKCS1_PADDING_INFO` structure. |
| NCRYPT\_PAD\_PSS\_FLAG | Indicates the signature used Probabilistic Signature Scheme (PSS) padding. Set  `pPaddingInfo` to point to a `BCRYPT_PSS_PADDING_INFO` structure. |
| NCRYPT\_SILENT\_FLAG | This flag has no effect. | ## Return Value The function returns a status code to indicate success or failure. Common return codes include:
| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. |
| NTE\_FAIL | The operation couldn't complete. |
| NTE\_INVALID\_HANDLE | The handle in `hKey` is not valid. |
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. |
| NTE\_BAD\_SIGNATURE | The signature was not verified. |
| NTE\_BAD\_KEY\_STATE | The key state is not valid. |
| NTE\_INTERNAL\_ERROR | An internal error happened while verifying the signature. |
