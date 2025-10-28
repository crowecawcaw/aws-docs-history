# NCryptEnumAlgorithms with

Key storage provider (KSP)

The `NCryptEnumAlgorithms` function retrieves the names of algorithms that the Key Storage Provider (KSP)
supports.

## Parameters

`hProvider` [in]

The handle of the key storage provider for which to enumerate the
algorithms. Use the [NCryptOpenStorageProvider](ksp-library-apis-open-provider.md "ksp-library-apis-open-provider.md") function to get this handle.

`dwAlgOperations` [in]

A set of values that specify which algorithm classes to enumerate. You can
use zero to enumerate all algorithms, or combine one or more of these
values:

| Value                                             | Meaning                                                        |
| ------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| NCRYPT_ASYMMETRIC_ENCRYPTION_OPERATION 0x00000004 | List the asymmetric encryption algorithms.                     |
| NCRYPT_SIGNATURE_OPERATION 0x00000010             | List the digital signature algorithms.                         | `pdwAlgCount` [out] The address of a DWORD that stores the number of elements in the `ppAlgList` array. `ppAlgList` [out] The address of an `NCryptAlgorithmName` structure pointer that stores an array of registered algorithm names. The `pdwAlgCount` parameter indicates the number of elements in this array. `dwFlags` [in] Flags to modify the function's behavior. Use zero or the following value: |
| Value                                             | Meaning                                                        |
| ---                                               | ---                                                            |
| NCRYPT_SILENT_FLAG                                | This flag has no effect.                                       | ## Return Value The function returns a status code to indicate success or failure. Common return codes include:                                                                                                                                                                                                                                                                                              |
| Return code                                       | Description                                                    |
| ---                                               | ---                                                            |
| ERROR_SUCCESS                                     | The operation completed successfully.                          |
| NTE_INVALID_PARAMETER                             | One or more parameters are not valid.                          |
| NTE_FAIL                                          | The operation couldn't complete.                               |
| NTE_BAD_FLAGS                                     | The `dwFlags` parameter contains an invalid value.             |
| NTE_NOT_SUPPORTED                                 | The `dwAlgOperations` parameter contains an unsupported value. |
