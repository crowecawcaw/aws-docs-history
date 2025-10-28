# DescribeGlobalSettings

Describes whether the AWS account is opted in to cross-account backup.
Returns an error if the account is not a member of an Organizations organization.
Example: `describe-global-settings --region us-west-2`

## Request Syntax

```
GET /global-settings HTTP/1.1

```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "GlobalSettings": {
      "***string***" : "***string***"
   },
   "LastUpdateTime": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[GlobalSettings](#API_DescribeGlobalSettings_ResponseSyntax "#API_DescribeGlobalSettings_ResponseSyntax")**

The status of the flags `isCrossAccountBackupEnabled` and
`isMpaEnabled` ('Mpa' refers to multi-party approval).

Type: String to string map

**[LastUpdateTime](#API_DescribeGlobalSettings_ResponseSyntax "#API_DescribeGlobalSettings_ResponseSyntax")**

The date and time that the flag `isCrossAccountBackupEnabled` was last
updated. This update is in Unix format and Coordinated Universal Time (UTC). The value of
`LastUpdateTime` is accurate to milliseconds. For example, the value
1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidRequestException**

Indicates that something is wrong with the input to the request. For example, a
parameter is of the wrong type.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/cli2/backup-2018-11-15/DescribeGlobalSettings.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeGlobalSettings.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/SdkForCpp/backup-2018-11-15/DescribeGlobalSettings.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/SdkForGoV2/backup-2018-11-15/DescribeGlobalSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeGlobalSettings.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeGlobalSettings.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/SdkForKotlin/backup-2018-11-15/DescribeGlobalSettings.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeGlobalSettings.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/boto3/backup-2018-11-15/DescribeGlobalSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeGlobalSettings.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeGlobalSettings.md")
