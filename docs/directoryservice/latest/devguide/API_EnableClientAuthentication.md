

# EnableClientAuthentication
<a name="API_EnableClientAuthentication"></a>

Enables alternative client authentication methods for the specified directory.

## Request Syntax
<a name="API_EnableClientAuthentication_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_EnableClientAuthentication_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_EnableClientAuthentication_RequestSyntax) **   <a name="DirectoryService-EnableClientAuthentication-request-DirectoryId"></a>
The identifier of the specified directory.   
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Type](#API_EnableClientAuthentication_RequestSyntax) **   <a name="DirectoryService-EnableClientAuthentication-request-Type"></a>
The type of client authentication to enable. Currently only the value `SmartCard` is supported. Smart card authentication in AD Connector requires that you enable Kerberos Constrained Delegation for the Service User to the LDAP service in your self-managed AD.   
Type: String  
Valid Values: `SmartCard | SmartCardOrPassword`   
Required: Yes

## Response Elements
<a name="API_EnableClientAuthentication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableClientAuthentication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.    
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

 ** InvalidClientAuthStatusException **   
Client authentication is already enabled.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** NoAvailableCertificateException **   
Client authentication setup could not be completed because at least one valid certificate must be registered in the system.    
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
<a name="API_EnableClientAuthentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/EnableClientAuthentication) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/EnableClientAuthentication) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/EnableClientAuthentication) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/EnableClientAuthentication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/EnableClientAuthentication) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/EnableClientAuthentication) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/EnableClientAuthentication) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/EnableClientAuthentication) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/EnableClientAuthentication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/EnableClientAuthentication) 