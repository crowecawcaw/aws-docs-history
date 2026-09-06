

# UpdateDirectorySetup
<a name="API_UpdateDirectorySetup"></a>

Updates directory configuration for the specified update type.

## Request Syntax
<a name="API_UpdateDirectorySetup_RequestSyntax"></a>

```
{
   "CreateSnapshotBeforeUpdate": {{boolean}},
   "DirectoryId": "{{string}}",
   "DirectorySizeUpdateSettings": { 
      "DirectorySize": "{{string}}"
   },
   "NetworkUpdateSettings": { 
      "CustomerDnsIpsV6": [ "{{string}}" ],
      "NetworkType": "{{string}}"
   },
   "OSUpdateSettings": { 
      "OSVersion": "{{string}}"
   },
   "UpdateType": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDirectorySetup_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [CreateSnapshotBeforeUpdate](#API_UpdateDirectorySetup_RequestSyntax) **   <a name="DirectoryService-UpdateDirectorySetup-request-CreateSnapshotBeforeUpdate"></a>
Specifies whether to create a directory snapshot before performing the update.  
Type: Boolean  
Required: No

 ** [DirectoryId](#API_UpdateDirectorySetup_RequestSyntax) **   <a name="DirectoryService-UpdateDirectorySetup-request-DirectoryId"></a>
The identifier of the directory to update.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [DirectorySizeUpdateSettings](#API_UpdateDirectorySetup_RequestSyntax) **   <a name="DirectoryService-UpdateDirectorySetup-request-DirectorySizeUpdateSettings"></a>
Directory size configuration to apply during the update operation.  
Type: [DirectorySizeUpdateSettings](API_DirectorySizeUpdateSettings.md) object  
Required: No

 ** [NetworkUpdateSettings](#API_UpdateDirectorySetup_RequestSyntax) **   <a name="DirectoryService-UpdateDirectorySetup-request-NetworkUpdateSettings"></a>
Network configuration to apply during the directory update operation.  
Type: [NetworkUpdateSettings](API_NetworkUpdateSettings.md) object  
Required: No

 ** [OSUpdateSettings](#API_UpdateDirectorySetup_RequestSyntax) **   <a name="DirectoryService-UpdateDirectorySetup-request-OSUpdateSettings"></a>
Operating system configuration to apply during the directory update operation.  
Type: [OSUpdateSettings](API_OSUpdateSettings.md) object  
Required: No

 ** [UpdateType](#API_UpdateDirectorySetup_RequestSyntax) **   <a name="DirectoryService-UpdateDirectorySetup-request-UpdateType"></a>
The type of update to perform on the directory.  
Type: String  
Valid Values: `OS | NETWORK | SIZE`   
Required: Yes

## Response Elements
<a name="API_UpdateDirectorySetup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDirectorySetup_Errors"></a>

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

 ** DirectoryInDesiredStateException **   
 The directory is already updated to desired update type settings.     
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

 ** SnapshotLimitExceededException **   
The maximum number of manual snapshots for the directory has been reached. You can use the [GetSnapshotLimits](API_GetSnapshotLimits.md) operation to determine the snapshot limits for a directory.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** UnsupportedOperationException **   
The operation is not supported.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDirectorySetup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/UpdateDirectorySetup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/UpdateDirectorySetup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/UpdateDirectorySetup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/UpdateDirectorySetup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/UpdateDirectorySetup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateDirectorySetup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/UpdateDirectorySetup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/UpdateDirectorySetup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/UpdateDirectorySetup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/UpdateDirectorySetup) 