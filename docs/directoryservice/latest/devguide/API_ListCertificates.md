

# ListCertificates
<a name="API_ListCertificates"></a>

For the specified directory, lists all the certificates registered for a secure LDAP or client certificate authentication.

## Request Syntax
<a name="API_ListCertificates_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCertificates_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_ListCertificates_RequestSyntax) **   <a name="DirectoryService-ListCertificates-request-DirectoryId"></a>
The identifier of the directory.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Limit](#API_ListCertificates_RequestSyntax) **   <a name="DirectoryService-ListCertificates-request-Limit"></a>
The number of items that should show up on one page  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** [NextToken](#API_ListCertificates_RequestSyntax) **   <a name="DirectoryService-ListCertificates-request-NextToken"></a>
A token for requesting another page of certificates if the `NextToken` response element indicates that more certificates are available. Use the value of the returned `NextToken` element in your request until the token comes back as `null`. Pass `null` if this is the first call.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListCertificates_ResponseSyntax"></a>

```
{
   "CertificatesInfo": [ 
      { 
         "CertificateId": "string",
         "CommonName": "string",
         "ExpiryDateTime": number,
         "State": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCertificates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificatesInfo](#API_ListCertificates_ResponseSyntax) **   <a name="DirectoryService-ListCertificates-response-CertificatesInfo"></a>
A list of certificates with basic details including certificate ID, certificate common name, certificate state.  
Type: Array of [CertificateInfo](API_CertificateInfo.md) objects

 ** [NextToken](#API_ListCertificates_ResponseSyntax) **   <a name="DirectoryService-ListCertificates-response-NextToken"></a>
Indicates whether another page of certificates is available when the number of available certificates exceeds the page limit.  
Type: String

## Errors
<a name="API_ListCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidNextTokenException **   
The `NextToken` value is not valid.    
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
<a name="API_ListCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/ListCertificates) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/ListCertificates) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/ListCertificates) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/ListCertificates) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/ListCertificates) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/ListCertificates) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/ListCertificates) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/ListCertificates) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/ListCertificates) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/ListCertificates) 