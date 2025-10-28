# DescribeUpdateDirectory

Describes the updates of a directory for a particular update type.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "NextToken": "`string`",
   "RegionName": "`string`",
   "UpdateType": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_DescribeUpdateDirectory_RequestSyntax "#API_DescribeUpdateDirectory_RequestSyntax")**

The unique identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[NextToken](#API_DescribeUpdateDirectory_RequestSyntax "#API_DescribeUpdateDirectory_RequestSyntax")**

The `DescribeUpdateDirectoryResult`. NextToken value from a previous call to
[DescribeUpdateDirectory](API_DescribeUpdateDirectory.md "API_DescribeUpdateDirectory.md"). Pass null if this is the first call.

Type: String

Required: No

**[RegionName](#API_DescribeUpdateDirectory_RequestSyntax "#API_DescribeUpdateDirectory_RequestSyntax")**

The name of the Region.

Type: String

Length Constraints: Minimum length of 8. Maximum length of 32.

Required: No

**[UpdateType](#API_DescribeUpdateDirectory_RequestSyntax "#API_DescribeUpdateDirectory_RequestSyntax")**

The type of updates you want to describe for the directory.

Type: String

Valid Values: `OS | NETWORK | SIZE`

Required: Yes

## Response Syntax

```
{
   "NextToken": "***string***",
   "UpdateActivities": [
      {
         "InitiatedBy": "***string***",
         "LastUpdatedDateTime": ***number***,
         "NewValue": {
            "OSUpdateSettings": {
               "OSVersion": "***string***"
            }
         },
         "PreviousValue": {
            "OSUpdateSettings": {
               "OSVersion": "***string***"
            }
         },
         "Region": "***string***",
         "StartTime": ***number***,
         "Status": "***string***",
         "StatusReason": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_DescribeUpdateDirectory_ResponseSyntax "#API_DescribeUpdateDirectory_ResponseSyntax")**

If not null, more results are available. Pass this value for the `NextToken`
parameter.

Type: String

**[UpdateActivities](#API_DescribeUpdateDirectory_ResponseSyntax "#API_DescribeUpdateDirectory_ResponseSyntax")**

The list of update activities on a directory for the requested update type.

Type: Array of [UpdateInfoEntry](API_UpdateInfoEntry.md "API_UpdateInfoEntry.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have sufficient access to perform this action.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryDoesNotExistException**

The specified directory does not exist in the system.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidNextTokenException**

The `NextToken` value is not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidParameterException**

One or more parameters are not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/cli2/ds-2015-04-16/DescribeUpdateDirectory.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/DotNetSDKV3/ds-2015-04-16/DescribeUpdateDirectory.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/SdkForCpp/ds-2015-04-16/DescribeUpdateDirectory.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/SdkForGoV2/ds-2015-04-16/DescribeUpdateDirectory.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeUpdateDirectory.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeUpdateDirectory.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/SdkForKotlin/ds-2015-04-16/DescribeUpdateDirectory.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeUpdateDirectory.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/boto3/ds-2015-04-16/DescribeUpdateDirectory.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeUpdateDirectory.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeUpdateDirectory.md")
