

# UpdateTrust
<a name="API_UpdateTrust"></a>

Updates the trust that has been set up between your AWS Managed Microsoft AD directory and an self-managed Active Directory.

## Request Syntax
<a name="API_UpdateTrust_RequestSyntax"></a>

```
{
   "SelectiveAuth": "{{string}}",
   "TrustId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTrust_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [SelectiveAuth](#API_UpdateTrust_RequestSyntax) **   <a name="DirectoryService-UpdateTrust-request-SelectiveAuth"></a>
Updates selective authentication for the trust.  
Type: String  
Valid Values: `Enabled | Disabled`   
Required: No

 ** [TrustId](#API_UpdateTrust_RequestSyntax) **   <a name="DirectoryService-UpdateTrust-request-TrustId"></a>
Identifier of the trust relationship.  
Type: String  
Pattern: `^t-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_UpdateTrust_ResponseSyntax"></a>

```
{
   "RequestId": "string",
   "TrustId": "string"
}
```

## Response Elements
<a name="API_UpdateTrust_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_UpdateTrust_ResponseSyntax) **   <a name="DirectoryService-UpdateTrust-response-RequestId"></a>
The AWS request identifier.  
Type: String  
Pattern: `^([A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12})$` 

 ** [TrustId](#API_UpdateTrust_ResponseSyntax) **   <a name="DirectoryService-UpdateTrust-response-TrustId"></a>
Identifier of the trust relationship.  
Type: String  
Pattern: `^t-[0-9a-f]{10}$` 

## Errors
<a name="API_UpdateTrust_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** EntityDoesNotExistException **   
The specified entity could not be found.    
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

## See Also
<a name="API_UpdateTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/UpdateTrust) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/UpdateTrust) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/UpdateTrust) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/UpdateTrust) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/UpdateTrust) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateTrust) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/UpdateTrust) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/UpdateTrust) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/UpdateTrust) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/UpdateTrust) 