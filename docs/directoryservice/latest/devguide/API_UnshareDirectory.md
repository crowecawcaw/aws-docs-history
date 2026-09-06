

# UnshareDirectory
<a name="API_UnshareDirectory"></a>

Stops the directory sharing between the directory owner and consumer accounts. 

## Request Syntax
<a name="API_UnshareDirectory_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "UnshareTarget": { 
      "Id": "{{string}}",
      "Type": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UnshareDirectory_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_UnshareDirectory_RequestSyntax) **   <a name="DirectoryService-UnshareDirectory-request-DirectoryId"></a>
The identifier of the AWS Managed Microsoft AD directory that you want to stop sharing.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [UnshareTarget](#API_UnshareDirectory_RequestSyntax) **   <a name="DirectoryService-UnshareDirectory-request-UnshareTarget"></a>
Identifier for the directory consumer account with whom the directory has to be unshared.  
Type: [UnshareTarget](API_UnshareTarget.md) object  
Required: Yes

## Response Syntax
<a name="API_UnshareDirectory_ResponseSyntax"></a>

```
{
   "SharedDirectoryId": "string"
}
```

## Response Elements
<a name="API_UnshareDirectory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SharedDirectoryId](#API_UnshareDirectory_ResponseSyntax) **   <a name="DirectoryService-UnshareDirectory-response-SharedDirectoryId"></a>
Identifier of the directory stored in the directory consumer account that is to be unshared from the specified directory (`DirectoryId`).  
Type: String  
Pattern: `^d-[0-9a-f]{10}$` 

## Errors
<a name="API_UnshareDirectory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryNotSharedException **   
The specified directory has not been shared with this AWS account.    
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

 ** InvalidTargetException **   
The specified shared target is not valid.    
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
<a name="API_UnshareDirectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/UnshareDirectory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/UnshareDirectory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/UnshareDirectory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/UnshareDirectory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/UnshareDirectory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/UnshareDirectory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/UnshareDirectory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/UnshareDirectory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/UnshareDirectory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/UnshareDirectory) 