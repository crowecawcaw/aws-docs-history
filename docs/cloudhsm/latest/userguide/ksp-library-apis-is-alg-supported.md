# NCryptIsAlgSupported with

Key storage provider (KSP)

NCryptIsAlgSupported function determines if Key Storage Provider (KSP) supports a specific cryptographic
algorithm.

## Parameters

`hProvider` [in]

The handle of the key storage provider. Use
[NCryptOpenStorageProvider](ksp-library-apis-open-provider.md "ksp-library-apis-open-provider.md") to get the handle.

`pszAlgId` [in]

A pointer to a null-terminated Unicode string that contains the
identifier of the cryptographic algorithm to create the key. AWS CloudHSM
Key Storage Provider (KSP) supports the following algorithms:

| Constant/value                           | Description                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| BCRYPT_RSA_ALGORITHM "RSA"               | The RSA public key algorithm.                                              |
| BCRYPT_ECDSA_P256_ALGORITHM "ECDSA_P256" | The 256-bit prime elliptic curve digital signature algorithm (FIPS 186-2). |
| BCRYPT_ECDSA_P384_ALGORITHM "ECDSA_P384" | The 384-bit prime elliptic curve digital signature algorithm (FIPS 186-2). |
| BCRYPT_ECDSA_P521_ALGORITHM "ECDSA_P521" | The 521-bit prime elliptic curve digital signature algorithm (FIPS 186-2). | `dwFlags` [in] Flags that modify function behavior. This can be zero or the following value:                    |
| Value                                    | Meaning                                                                    |
| ---                                      | ---                                                                        |
| NCRYPT_SILENT_FLAG                       | This flag has no effect.                                                   | ## Return Value The function returns a status code to indicate success or failure. Common return codes include: |
| Return code                              | Description                                                                |
| ---                                      | ---                                                                        |
| ERROR_SUCCESS                            | The operation completed successfully.                                      |
| NTE_INVALID_PARAMETER                    | One or more parameters are not valid.                                      |
| NTE_BAD_FLAGS                            | The `dwFlags` parameter contains an invalid value.                         |
| NTE_NOT_SUPPORTED                        | The `pszAlgId` parameter contains an unsupported value.                    |
| NTE_INVALID_HANDLE                       | The handle in `hProvider` is not valid.                                    |
