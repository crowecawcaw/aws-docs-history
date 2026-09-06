

# RegisterCertificate
<a name="API_RegisterCertificate"></a>

Registers a certificate for a secure LDAP or client certificate authentication.

## Request Syntax
<a name="API_RegisterCertificate_RequestSyntax"></a>

```
{
   "CertificateData": "{{string}}",
   "ClientCertAuthSettings": { 
      "OCSPUrl": "{{string}}"
   },
   "DirectoryId": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterCertificate_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [CertificateData](#API_RegisterCertificate_RequestSyntax) **   <a name="DirectoryService-RegisterCertificate-request-CertificateData"></a>
The certificate PEM string that needs to be registered.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: Yes

 ** [ClientCertAuthSettings](#API_RegisterCertificate_RequestSyntax) **   <a name="DirectoryService-RegisterCertificate-request-ClientCertAuthSettings"></a>
A `ClientCertAuthSettings` object that contains client certificate authentication settings.  
Type: [ClientCertAuthSettings](API_ClientCertAuthSettings.md) object  
Required: No

 ** [DirectoryId](#API_RegisterCertificate_RequestSyntax) **   <a name="DirectoryService-RegisterCertificate-request-DirectoryId"></a>
The identifier of the directory.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Type](#API_RegisterCertificate_RequestSyntax) **   <a name="DirectoryService-RegisterCertificate-request-Type"></a>
The function that the registered certificate performs. Valid values include `ClientLDAPS` or `ClientCertAuth`. The default value is `ClientLDAPS`.  
Type: String  
Valid Values: `ClientCertAuth | ClientLDAPS`   
Required: No

## Response Syntax
<a name="API_RegisterCertificate_ResponseSyntax"></a>

```
{
   "CertificateId": "string"
}
```

## Response Elements
<a name="API_RegisterCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificateId](#API_RegisterCertificate_ResponseSyntax) **   <a name="DirectoryService-RegisterCertificate-response-CertificateId"></a>
The identifier of the certificate.  
Type: String  
Pattern: `^c-[0-9a-f]{10}$` 

## Errors
<a name="API_RegisterCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CertificateAlreadyExistsException **   
The certificate has already been registered into the system.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** CertificateLimitExceededException **   
The certificate could not be added because the certificate limit has been reached.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryDoesNotExistException **   
The specified directory does not exist in the system.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryUnavailableException **   
The specified directory is unavailable.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InvalidCertificateException **   
The certificate PEM that was provided has incorrect encoding.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InvalidParameterException **   
One or more parameters are not valid.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** ServiceException **   
An exception has occurred in AWS Directory Service.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 500

 ** UnsupportedOperationException **   
The operation is not supported.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## See Also
<a name="API_RegisterCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/RegisterCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/RegisterCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/RegisterCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/RegisterCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/RegisterCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/RegisterCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/RegisterCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/RegisterCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/RegisterCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/RegisterCertificate) 