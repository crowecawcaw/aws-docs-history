# DescribeSharedDirectories

Returns the shared directories in your account.

## Request Syntax

```
{
   "Limit": `number`,
   "NextToken": "`string`",
   "OwnerDirectoryId": "`string`",
   "SharedDirectoryIds": [ "`string`" ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Limit](#API_DescribeSharedDirectories_RequestSyntax "#API_DescribeSharedDirectories_RequestSyntax")**

The number of shared directories to return in the response object.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**[NextToken](#API_DescribeSharedDirectories_RequestSyntax "#API_DescribeSharedDirectories_RequestSyntax")**

The `DescribeSharedDirectoriesResult.NextToken` value from a previous call to
[DescribeSharedDirectories](API_DescribeSharedDirectories.md "API_DescribeSharedDirectories.md"). Pass null if this is the first call.

Type: String

Required: No

**[OwnerDirectoryId](#API_DescribeSharedDirectories_RequestSyntax "#API_DescribeSharedDirectories_RequestSyntax")**

Returns the identifier of the directory in the directory owner account.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[SharedDirectoryIds](#API_DescribeSharedDirectories_RequestSyntax "#API_DescribeSharedDirectories_RequestSyntax")**

A list of identifiers of all shared directories in your account.

Type: Array of strings

Pattern: `^d-[0-9a-f]{10}$`

Required: No

## Response Syntax

```
{
   "NextToken": "***string***",
   "SharedDirectories": [
      {
         "CreatedDateTime": ***number***,
         "LastUpdatedDateTime": ***number***,
         "OwnerAccountId": "***string***",
         "OwnerDirectoryId": "***string***",
         "SharedAccountId": "***string***",
         "SharedDirectoryId": "***string***",
         "ShareMethod": "***string***",
         "ShareNotes": "***string***",
         "ShareStatus": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_DescribeSharedDirectories_ResponseSyntax "#API_DescribeSharedDirectories_ResponseSyntax")**

If not null, token that indicates that more results are available. Pass this value for the
`NextToken` parameter in a subsequent call to [DescribeSharedDirectories](API_DescribeSharedDirectories.md "API_DescribeSharedDirectories.md") to retrieve the next set of items.

Type: String

**[SharedDirectories](#API_DescribeSharedDirectories_ResponseSyntax "#API_DescribeSharedDirectories_ResponseSyntax")**

A list of all shared directories in your account.

Type: Array of [SharedDirectory](API_SharedDirectory.md "API_SharedDirectory.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

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

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/cli2/ds-2015-04-16/DescribeSharedDirectories.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeSharedDirectories.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/SdkForCpp/ds-2015-04-16/DescribeSharedDirectories.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/SdkForGoV2/ds-2015-04-16/DescribeSharedDirectories.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeSharedDirectories.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeSharedDirectories.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/SdkForKotlin/ds-2015-04-16/DescribeSharedDirectories.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeSharedDirectories.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/boto3/ds-2015-04-16/DescribeSharedDirectories.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeSharedDirectories.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeSharedDirectories.md")
