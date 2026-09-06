

# NCryptSetProperty with Key storage provider (KSP)
<a name="ksp-library-apis-set-property"></a>

The `NCryptSetProperty` function sets property values for a key storage object.

## Parameters
<a name="ksp-library-apis-create-set-property-parameters"></a>

 `hObject` [in]   
 The handle of the object whose property you want to set. You can use:  
+ A provider handle (`NCRYPT_PROV_HANDLE`)
+ A key handle (`NCRYPT_KEY_HANDLE`)

 `pszProperty ` [in]   
A pointer to a null-terminated Unicode string containing the property name to retrieve.   
When using `NCRYPT_PROV_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-set-property.html)
When using `NCRYPT_KEY_HANDLE`, AWS CloudHSM Key Storage Provider (KSP) supports the following KSP identifiers:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-set-property.html)
Values are wide-character string literal, as indicated by L before the literal.

 `pbInput` [in]   
 The address of a buffer that contains the new property value. `cbInput` contains the size of the buffer. 

 `cbInput` [in]   
 The size of the `pbInput` buffer in bytes. 

`dwFlags` [in]  
Flags that modify function's behavior. No flags are defined for this function.

## Return Value
<a name="ksp-library-apis-set-property-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_FAIL | The operation couldn't complete. | 
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. | 
| NTE\_NOT\_SUPPORTED | The `pszProperty` parameter contains a value that is not supported. | 
| NTE\_INVALID\_HANDLE | The handle in `hObject` is not valid. | 
| NTE\_BAD\_DATA | The data pointed by `pbInput` and `cbInput` is not valid. | 