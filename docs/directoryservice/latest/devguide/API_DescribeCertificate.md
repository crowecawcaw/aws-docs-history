

# DescribeCertificate
<a name="API_DescribeCertificate"></a>

Displays information about the certificate registered for secure LDAP or client certificate authentication.

## Request Syntax
<a name="API_DescribeCertificate_RequestSyntax"></a>

```
{
   "CertificateId": "{{string}}",
   "DirectoryId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCertificate_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [CertificateId](#API_DescribeCertificate_RequestSyntax) **   <a name="DirectoryService-DescribeCertificate-request-CertificateId"></a>
The identifier of the certificate.  
Type: String  
Pattern: `^c-[0-9a-f]{10}$`   
Required: Yes

 ** [DirectoryId](#API_DescribeCertificate_RequestSyntax) **   <a name="DirectoryService-DescribeCertificate-request-DirectoryId"></a>
The identifier of the directory.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_DescribeCertificate_ResponseSyntax"></a>

```
{
   "Certificate": { 
      "CertificateId": "string",
      "ClientCertAuthSettings": { 
         "OCSPUrl": "string"
      },
      "CommonName": "string",
      "ExpiryDateTime": number,
      "RegisteredDateTime": number,
      "State": "string",
      "StateReason": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_DescribeCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificate](#API_DescribeCertificate_ResponseSyntax) **   <a name="DirectoryService-DescribeCertificate-response-Certificate"></a>
Information about the certificate, including registered date time, certificate state, the reason for the state, expiration date time, and certificate common name.  
Type: [Certificate](API_Certificate.md) object

## Errors
<a name="API_DescribeCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CertificateDoesNotExistException **   
The certificate is not present in the system for describe or deregister activities.    
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
<a name="API_DescribeCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeCertificate) 