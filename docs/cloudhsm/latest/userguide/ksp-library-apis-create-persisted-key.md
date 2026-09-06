

# NCryptCreatePersistedKey with Key storage provider (KSP)
<a name="ksp-library-apis-create-persisted-key"></a>

The `NCryptCreatePersistedKey` function creates a new key and stores it in the Key Storage Provider (KSP). You can use the [`NCryptSetProperty`](ksp-library-apis-set-property.md) function to set its properties after creation. You must call [`NCryptFinalizeKey`](ksp-library-apis-finalize-key.md) before you can use the key.

## Parameters
<a name="ksp-library-apis-create-persisted-key-parameters"></a>

 `hProvider` [in]   
The handle of the key storage provider where you will create the key. Use [`NCryptOpenStorageProvider`](ksp-library-apis-open-provider.md) to get this handle.

 `phKey` [out]   
The address of an `NCRYPT_KEY_HANDLE` variable that stores the key handle. 

 `pszAlgId` [in]   
A pointer to a null-terminated Unicode string that specifies the cryptographic algorithm identifier for creating the key.  
AWS CloudHSM Key Storage Provider (KSP) supports the following algorithms:       
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-create-persisted-key.html)

`pszKeyName` [in, optional]  
A pointer to a null-terminated Unicode string that contains the name of the key. If this parameter is NULL, this function will create an ephemeral key that is not persisted.

`dwLegacyKeySpec` [in, unused]  
AWS CloudHSM Key Storage Provider (KSP) doesn't use this parameter.

`dwFlags` [in]  
Flags to modify the function's behavior. Use zero or more of the following values:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-create-persisted-key.html)

## Return Value
<a name="ksp-library-apis-create-persisted-key-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The function completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_FAIL | The operation couldn't complete. | 
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. | 
| NTE\_NOT\_SUPPORTED | The `pszAlgId` parameter contains an unsupported value. | 
| NTE\_EXISTS | A key with the specified name already exists and operation didn't use ` NCRYPT_OVERWRITE_KEY_FLAG`. | 