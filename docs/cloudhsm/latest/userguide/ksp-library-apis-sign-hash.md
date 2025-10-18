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




| Value | Meaning |
| --- | --- |
| BCRYPT\_PAD\_PKCS1 | Uses the PKCS1 padding scheme. Set `pPaddingInfo` to point to a `BCRYPT_PKCS1_PADDING_INFO` structure. |
| BCRYPT\_PAD\_PSS |  Uses the Probabilistic Signature Scheme (PSS) padding scheme. Set `pPaddingInfo` parameter to point to a `BCRYPT_PSS_PADDING_INFO` structure.  |
| NCRYPT\_SILENT\_FLAG | This flag has no effect. | ## Return Value The function returns a status code to indicate success or failure. Common return codes include:
| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. |
| NTE\_FAIL | The operation couldn't complete. |
| NTE\_INVALID\_HANDLE | The handle in `hKey` is not valid. |
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. |
| NTE\_BUFFER\_TOO\_SMALL | The `pcbOutput` parameter is too small for return values. |
| NTE\_BAD\_KEY\_STATE | The key state is not valid. |
| NTE\_INTERNAL\_ERROR | An internal error happened when signing the hash. |
