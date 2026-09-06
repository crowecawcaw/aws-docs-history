

# NCryptGetProperty with Key storage provider (KSP)
<a name="ksp-library-apis-get-property"></a>

The `NCryptGetProperty` function retrieves property values for a key storage object.

## Parameters
<a name="ksp-library-apis-create-get-property-parameters"></a>

 `hObject` [in]   
 The handle of the object whose property you want to retrieve. You can use:  
+ A provider handle (`NCRYPT_PROV_HANDLE`)
+ A key handle (`NCRYPT_KEY_HANDLE`)

 `pszProperty ` [in]   
A pointer to a null-terminated Unicode string containing the property name to retrieve.   
When using `NCRYPT_PROV_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-get-property.html)
When using `NCRYPT_KEY_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-get-property.html)
Values are wide-character string literal, as indicated by L before the literal.

 `pbOutput` [out]   
The address of a buffer to store the property value. Specify the buffer size using `cbOutput`.  
To determine the required buffer size, set this parameter to NULL. The function stores the required size (in bytes) in the location pointed to by `pcbResult`.

 `cbOutput` [in]   
 The size of the `pbOutput` buffer in bytes.

`pcbResult` [out]  
A pointer to a DWORD variable that stores the number of bytes copied to the`pbOutput` buffer.  
If the `pbOutput` is NULL, this stores the required size (in bytes).

`dwFlags` [in]  
Flags to modify the function's behavior. You can use zero or:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-get-property.html)
When pszProperty is `NCRYPT_SECURITY_DESCR_PROPERTY`, use one or a combination of:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-get-property.html)

## Return Value
<a name="ksp-library-apis-get-property-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_FAIL | The operation couldn't complete. | 
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. | 
| NTE\_NOT\_SUPPORTED | The `pszAlgId` parameter contains a value that is not supported. | 
| NTE\_INVALID\_HANDLE | The handle in `hObject` is not valid. | 
| NTE\_BUFFER\_TOO\_SMALL | The `cbOutput` parameter is too small for return values. | 