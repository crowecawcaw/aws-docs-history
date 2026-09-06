

# RejectSharedDirectory
<a name="API_RejectSharedDirectory"></a>

Rejects a directory sharing request that was sent from the directory owner account.

## Request Syntax
<a name="API_RejectSharedDirectory_RequestSyntax"></a>

```
{
   "SharedDirectoryId": "{{string}}"
}
```

## Request Parameters
<a name="API_RejectSharedDirectory_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [SharedDirectoryId](#API_RejectSharedDirectory_RequestSyntax) **   <a name="DirectoryService-RejectSharedDirectory-request-SharedDirectoryId"></a>
Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_RejectSharedDirectory_ResponseSyntax"></a>

```
{
   "SharedDirectoryId": "string"
}
```

## Response Elements
<a name="API_RejectSharedDirectory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SharedDirectoryId](#API_RejectSharedDirectory_ResponseSyntax) **   <a name="DirectoryService-RejectSharedDirectory-response-SharedDirectoryId"></a>
Identifier of the shared directory in the directory consumer account.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$` 

## Errors
<a name="API_RejectSharedDirectory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryAlreadySharedException **   
The specified directory has already been shared with this AWS account.    
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
<a name="API_RejectSharedDirectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/RejectSharedDirectory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/RejectSharedDirectory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/RejectSharedDirectory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/RejectSharedDirectory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/RejectSharedDirectory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/RejectSharedDirectory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/RejectSharedDirectory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/RejectSharedDirectory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/RejectSharedDirectory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/RejectSharedDirectory) 