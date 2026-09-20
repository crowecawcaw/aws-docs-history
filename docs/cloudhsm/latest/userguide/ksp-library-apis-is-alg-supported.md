

# NCryptIsAlgSupported with Key storage provider (KSP)
<a name="ksp-library-apis-is-alg-supported"></a>

NCryptIsAlgSupported function determines if Key Storage Provider (KSP) supports a specific cryptographic algorithm.

## Parameters
<a name="ksp-library-apis-is-alg-supported-parameters"></a>

 `hProvider` [in]   
 The handle of the key storage provider. Use [`NCryptOpenStorageProvider`](ksp-library-apis-open-provider.md) to get the handle. 

 `pszAlgId` [in]   
 A pointer to a null-terminated Unicode string that contains the identifier of the cryptographic algorithm to create the key. AWS CloudHSM Key Storage Provider (KSP) supports the following algorithms:   



<table>
<thead>
  <tr><th>Constant/value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>BCRYPT_RSA_ALGORITHM<br />"RSA"</td><td>The RSA public key algorithm. </td></tr>
  <tr><td>BCRYPT_ECDSA_P256_ALGORITHM<br />"ECDSA_P256"</td><td>The 256-bit prime elliptic curve digital signature algorithm (FIPS 186-2).</td></tr>
  <tr><td>BCRYPT_ECDSA_P384_ALGORITHM<br />"ECDSA_P384"</td><td>The 384-bit prime elliptic curve digital signature algorithm (FIPS 186-2).</td></tr>
  <tr><td>BCRYPT_ECDSA_P521_ALGORITHM<br />"ECDSA_P521"</td><td>The 521-bit prime elliptic curve digital signature algorithm (FIPS 186-2).</td></tr>
</tbody>
</table>


`dwFlags` [in]  
Flags that modify function behavior. This can be zero or the following value:  



<table>
<thead>
  <tr><th>Value</th><th>Meaning</th></tr>
</thead>
<tbody>
  <tr><td>NCRYPT_SILENT_FLAG</td><td>This flag has no effect.</td></tr>
</tbody>
</table>


## Return Value
<a name="ksp-library-apis-is-alg-supported-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:



| Return code | Description | 
| --- | --- | 
| ERROR\_SUCCESS | The operation completed successfully. | 
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. | 
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. | 
| NTE\_NOT\_SUPPORTED | The `pszAlgId` parameter contains an unsupported value. | 
| NTE\_INVALID\_HANDLE | The handle in `hProvider` is not valid. | 