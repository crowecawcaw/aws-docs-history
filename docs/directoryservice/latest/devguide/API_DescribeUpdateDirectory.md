

# DescribeUpdateDirectory
<a name="API_DescribeUpdateDirectory"></a>

 Describes the updates of a directory for a particular update type. 

## Request Syntax
<a name="API_DescribeUpdateDirectory_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "NextToken": "{{string}}",
   "RegionName": "{{string}}",
   "UpdateType": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUpdateDirectory_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeUpdateDirectory_RequestSyntax) **   <a name="DirectoryService-DescribeUpdateDirectory-request-DirectoryId"></a>
 The unique identifier of the directory.   
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [NextToken](#API_DescribeUpdateDirectory_RequestSyntax) **   <a name="DirectoryService-DescribeUpdateDirectory-request-NextToken"></a>
 The `DescribeUpdateDirectoryResult`. NextToken value from a previous call to [DescribeUpdateDirectory](#API_DescribeUpdateDirectory). Pass null if this is the first call.   
Type: String  
Required: No

 ** [RegionName](#API_DescribeUpdateDirectory_RequestSyntax) **   <a name="DirectoryService-DescribeUpdateDirectory-request-RegionName"></a>
 The name of the Region.   
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 32.  
Required: No

 ** [UpdateType](#API_DescribeUpdateDirectory_RequestSyntax) **   <a name="DirectoryService-DescribeUpdateDirectory-request-UpdateType"></a>
 The type of updates you want to describe for the directory.   
Type: String  
Valid Values: `OS | NETWORK | SIZE`   
Required: Yes

## Response Syntax
<a name="API_DescribeUpdateDirectory_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "UpdateActivities": [ 
      { 
         "InitiatedBy": "string",
         "LastUpdatedDateTime": number,
         "NewValue": { 
            "OSUpdateSettings": { 
               "OSVersion": "string"
            }
         },
         "PreviousValue": { 
            "OSUpdateSettings": { 
               "OSVersion": "string"
            }
         },
         "Region": "string",
         "StartTime": number,
         "Status": "string",
         "StatusReason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeUpdateDirectory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeUpdateDirectory_ResponseSyntax) **   <a name="DirectoryService-DescribeUpdateDirectory-response-NextToken"></a>
 If not null, more results are available. Pass this value for the `NextToken` parameter.   
Type: String

 ** [UpdateActivities](#API_DescribeUpdateDirectory_ResponseSyntax) **   <a name="DirectoryService-DescribeUpdateDirectory-response-UpdateActivities"></a>
 The list of update activities on a directory for the requested update type.   
Type: Array of [UpdateInfoEntry](API_UpdateInfoEntry.md) objects

## Errors
<a name="API_DescribeUpdateDirectory_Errors"></a>

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

## See Also
<a name="API_DescribeUpdateDirectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeUpdateDirectory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeUpdateDirectory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeUpdateDirectory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeUpdateDirectory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeUpdateDirectory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeUpdateDirectory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeUpdateDirectory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeUpdateDirectory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeUpdateDirectory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeUpdateDirectory) 