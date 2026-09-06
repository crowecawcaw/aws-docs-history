

# DescribeSettings
<a name="API_DescribeSettings"></a>

Retrieves information about the configurable settings for the specified directory.

## Request Syntax
<a name="API_DescribeSettings_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "NextToken": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSettings_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeSettings_RequestSyntax) **   <a name="DirectoryService-DescribeSettings-request-DirectoryId"></a>
The identifier of the directory for which to retrieve information.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [NextToken](#API_DescribeSettings_RequestSyntax) **   <a name="DirectoryService-DescribeSettings-request-NextToken"></a>
The `DescribeSettingsResult.NextToken` value from a previous call to [DescribeSettings](#API_DescribeSettings). Pass null if this is the first call.  
Type: String  
Required: No

 ** [Status](#API_DescribeSettings_RequestSyntax) **   <a name="DirectoryService-DescribeSettings-request-Status"></a>
The status of the directory settings for which to retrieve information.  
Type: String  
Valid Values: `Requested | Updating | Updated | Failed | Default`   
Required: No

## Response Syntax
<a name="API_DescribeSettings_ResponseSyntax"></a>

```
{
   "DirectoryId": "string",
   "NextToken": "string",
   "SettingEntries": [ 
      { 
         "AllowedValues": "string",
         "AppliedValue": "string",
         "DataType": "string",
         "LastRequestedDateTime": number,
         "LastUpdatedDateTime": number,
         "Name": "string",
         "RequestDetailedStatus": { 
            "string" : "string" 
         },
         "RequestedValue": "string",
         "RequestStatus": "string",
         "RequestStatusMessage": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_DescribeSettings_ResponseSyntax) **   <a name="DirectoryService-DescribeSettings-response-DirectoryId"></a>
The identifier of the directory.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$` 

 ** [NextToken](#API_DescribeSettings_ResponseSyntax) **   <a name="DirectoryService-DescribeSettings-response-NextToken"></a>
If not null, token that indicates that more results are available. Pass this value for the `NextToken` parameter in a subsequent call to `DescribeSettings` to retrieve the next set of items.   
Type: String

 ** [SettingEntries](#API_DescribeSettings_ResponseSyntax) **   <a name="DirectoryService-DescribeSettings-response-SettingEntries"></a>
The list of [SettingEntry](API_SettingEntry.md) objects that were retrieved.  
It is possible that this list contains less than the number of items specified in the `Limit` member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.  
Type: Array of [SettingEntry](API_SettingEntry.md) objects

## Errors
<a name="API_DescribeSettings_Errors"></a>

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
<a name="API_DescribeSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeSettings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeSettings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeSettings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeSettings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeSettings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeSettings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeSettings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeSettings) 