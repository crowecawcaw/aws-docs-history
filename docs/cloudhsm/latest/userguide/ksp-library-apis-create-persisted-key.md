# NCryptCreatePersistedKey with

Key storage provider (KSP)

The `NCryptCreatePersistedKey` function creates a new key and stores it in the Key Storage Provider (KSP). You can use the [NCryptSetProperty](ksp-library-apis-set-property.md "ksp-library-apis-set-property.md") function to set its
properties after creation. You must call [NCryptFinalizeKey](ksp-library-apis-finalize-key.md "ksp-library-apis-finalize-key.md") before you can use the key.

## Parameters

`hProvider` [in]

The handle of the key storage provider where you will create the key. Use [NCryptOpenStorageProvider](ksp-library-apis-open-provider.md "ksp-library-apis-open-provider.md") to get this handle.

`phKey` [out]

The address of an `NCRYPT_KEY_HANDLE` variable that stores
the key handle.

`pszAlgId` [in]

A pointer to a null-terminated Unicode string that specifies the
cryptographic algorithm identifier for creating the key.

AWS CloudHSM Key Storage Provider (KSP) supports the following algorithms:

| Constant/value                           | Description                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BCRYPT_RSA_ALGORITHM "RSA"               | The RSA public key algorithm.                                                                                             |
| BCRYPT_ECDSA_P256_ALGORITHM "ECDSA_P256" | The 256-bit prime elliptic curve digital signature algorithm (FIPS 186-2).                                                |
| BCRYPT_ECDSA_P384_ALGORITHM "ECDSA_P384" | The 384-bit prime elliptic curve digital signature algorithm (FIPS 186-2).                                                |
| BCRYPT_ECDSA_P521_ALGORITHM "ECDSA_P521" | The 521-bit prime elliptic curve digital signature algorithm (FIPS 186-2).                                                | `pszKeyName` [in, optional] A pointer to a null-terminated Unicode string that contains the name of the key. If this parameter is NULL, this function will create an ephemeral key that is not persisted. `dwLegacyKeySpec` [in, unused] AWS CloudHSM Key Storage Provider (KSP) doesn't use this parameter. `dwFlags` [in] Flags to modify the function's behavior. Use zero or more of the following values: |
| Value                                    | Meaning                                                                                                                   |
| ---                                      | ---                                                                                                                       |
| NCRYPT_MACHINE_KEY_FLAG                  | This flag has no effect.                                                                                                  |
| NCRYPT_SILENT_FLAG                       | This flag has no effect.                                                                                                  |
| NCRYPT_OVERWRITE_KEY_FLAG                | Specifying this flag overwrites any existing key with the same name in the HSM. Without this flag, the function returns . | ## Return Value The function returns a status code to indicate success or failure. Common return codes include:                                                                                                                                                                                                                                                                                                |
| Return code                              | Description                                                                                                               |
| ---                                      | ---                                                                                                                       |
| ERROR_SUCCESS                            | The function completed successfully.                                                                                      |
| NTE_INVALID_PARAMETER                    | One or more parameters are not valid.                                                                                     |
| NTE_FAIL                                 | The operation couldn't complete.                                                                                          |
| NTE_BAD_FLAGS                            | The `dwFlags` parameter contains an invalid value.                                                                        |
| NTE_NOT_SUPPORTED                        | The `pszAlgId` parameter contains an unsupported value.                                                                   |
| NTE_EXISTS                               | A key with the specified name already exists and operation didn't use `NCRYPT_OVERWRITE_KEY_FLAG`.                        |
