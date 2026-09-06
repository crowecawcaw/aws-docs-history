

# CreateLogSubscription
<a name="API_CreateLogSubscription"></a>

Creates a subscription to forward real-time Directory Service domain controller security logs to the specified Amazon CloudWatch log group in your AWS account.

## Request Syntax
<a name="API_CreateLogSubscription_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "LogGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateLogSubscription_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_CreateLogSubscription_RequestSyntax) **   <a name="DirectoryService-CreateLogSubscription-request-DirectoryId"></a>
Identifier of the directory to which you want to subscribe and receive real-time logs to your specified CloudWatch log group.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [LogGroupName](#API_CreateLogSubscription_RequestSyntax) **   <a name="DirectoryService-CreateLogSubscription-request-LogGroupName"></a>
The name of the CloudWatch log group where the real-time domain controller logs are forwarded.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[-._/#A-Za-z0-9]+`   
Required: Yes

## Response Elements
<a name="API_CreateLogSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateLogSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** EntityAlreadyExistsException **   
The specified entity already exists.    
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

 ** InsufficientPermissionsException **   
The account does not have sufficient permission to perform the operation.    
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
<a name="API_CreateLogSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/CreateLogSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/CreateLogSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/CreateLogSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/CreateLogSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/CreateLogSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/CreateLogSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/CreateLogSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/CreateLogSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/CreateLogSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/CreateLogSubscription) 