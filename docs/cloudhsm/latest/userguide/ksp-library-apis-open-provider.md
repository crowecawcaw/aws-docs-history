

# NCryptOpenStorageProvider function with Key Storage Provider (KSP)
<a name="ksp-library-apis-open-provider"></a>

The `NCryptOpenStorageProvider` function loads and initializes the Key Storage Provider (KSP).

## Parameters
<a name="ksp-library-apis-open-provider-parameters"></a>

 `phProvider` [out]   
A pointer to a `NCRYPT_PROV_HANDLE` variable that stores the provider handle.

 `pszProviderName` [in]   
A pointer to a null-terminated Unicode string identifying the key storage provider. AWS CloudHSM Key Storage Provider (KSP) supports the following values:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-open-provider.html)
Values are wide-character string literal, as indicated by L before the literal.

`dwFlags` [in]  
Flags that modify the behavior of the function. No flags are defined for this function.

## Return Value
<a name="ksp-library-apis-open-provider-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_FAIL | The operation couldn't complete. | 