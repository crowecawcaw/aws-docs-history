

# DescribeClientAuthenticationSettings
<a name="API_DescribeClientAuthenticationSettings"></a>

Retrieves information about the type of client authentication for the specified directory, if the type is specified. If no type is specified, information about all client authentication types that are supported for the specified directory is retrieved. Currently, only `SmartCard` is supported. 

## Request Syntax
<a name="API_DescribeClientAuthenticationSettings_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeClientAuthenticationSettings_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeClientAuthenticationSettings_RequestSyntax) **   <a name="DirectoryService-DescribeClientAuthenticationSettings-request-DirectoryId"></a>
The identifier of the directory for which to retrieve information.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Limit](#API_DescribeClientAuthenticationSettings_RequestSyntax) **   <a name="DirectoryService-DescribeClientAuthenticationSettings-request-Limit"></a>
The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** [NextToken](#API_DescribeClientAuthenticationSettings_RequestSyntax) **   <a name="DirectoryService-DescribeClientAuthenticationSettings-request-NextToken"></a>
The *DescribeClientAuthenticationSettingsResult.NextToken* value from a previous call to [DescribeClientAuthenticationSettings](#API_DescribeClientAuthenticationSettings). Pass null if this is the first call.  
Type: String  
Required: No

 ** [Type](#API_DescribeClientAuthenticationSettings_RequestSyntax) **   <a name="DirectoryService-DescribeClientAuthenticationSettings-request-Type"></a>
The type of client authentication for which to retrieve information. If no type is specified, a list of all client authentication types that are supported for the specified directory is retrieved.  
Type: String  
Valid Values: `SmartCard | SmartCardOrPassword`   
Required: No

## Response Syntax
<a name="API_DescribeClientAuthenticationSettings_ResponseSyntax"></a>

```
{
   "ClientAuthenticationSettingsInfo": [ 
      { 
         "LastUpdatedDateTime": number,
         "Status": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeClientAuthenticationSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientAuthenticationSettingsInfo](#API_DescribeClientAuthenticationSettings_ResponseSyntax) **   <a name="DirectoryService-DescribeClientAuthenticationSettings-response-ClientAuthenticationSettingsInfo"></a>
Information about the type of client authentication for the specified directory. The following information is retrieved: The date and time when the status of the client authentication type was last updated, whether the client authentication type is enabled or disabled, and the type of client authentication.  
Type: Array of [ClientAuthenticationSettingInfo](API_ClientAuthenticationSettingInfo.md) objects

 ** [NextToken](#API_DescribeClientAuthenticationSettings_ResponseSyntax) **   <a name="DirectoryService-DescribeClientAuthenticationSettings-response-NextToken"></a>
The next token used to retrieve the client authentication settings if the number of setting types exceeds page limit and there is another page.  
Type: String

## Errors
<a name="API_DescribeClientAuthenticationSettings_Errors"></a>

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
<a name="API_DescribeClientAuthenticationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeClientAuthenticationSettings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeClientAuthenticationSettings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeClientAuthenticationSettings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeClientAuthenticationSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeClientAuthenticationSettings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeClientAuthenticationSettings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeClientAuthenticationSettings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeClientAuthenticationSettings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeClientAuthenticationSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeClientAuthenticationSettings) 