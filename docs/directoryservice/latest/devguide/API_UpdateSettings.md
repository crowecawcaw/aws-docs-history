

# UpdateSettings
<a name="API_UpdateSettings"></a>

Updates the configurable settings for the specified directory.

## Request Syntax
<a name="API_UpdateSettings_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Settings": [ 
      { 
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateSettings_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_UpdateSettings_RequestSyntax) **   <a name="DirectoryService-UpdateSettings-request-DirectoryId"></a>
The identifier of the directory for which to update settings.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Settings](#API_UpdateSettings_RequestSyntax) **   <a name="DirectoryService-UpdateSettings-request-Settings"></a>
The list of [Setting](API_Setting.md) objects.  
Type: Array of [Setting](API_Setting.md) objects  
Required: Yes

## Response Syntax
<a name="API_UpdateSettings_ResponseSyntax"></a>

```
{
   "DirectoryId": "string"
}
```

## Response Elements
<a name="API_UpdateSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_UpdateSettings_ResponseSyntax) **   <a name="DirectoryService-UpdateSettings-response-DirectoryId"></a>
The identifier of the directory.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$` 

## Errors
<a name="API_UpdateSettings_Errors"></a>

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

 ** DirectoryUnavailableException **   
The specified directory is unavailable.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** IncompatibleSettingsException **   
The specified directory setting is not compatible with other settings.    
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

 ** UnsupportedSettingsException **   
The specified directory setting is not supported.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/UpdateSettings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/UpdateSettings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/UpdateSettings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/UpdateSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/UpdateSettings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateSettings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/UpdateSettings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/UpdateSettings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/UpdateSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/UpdateSettings) 