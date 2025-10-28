# UpdateGlobalSettings

Updates whether the AWS account is opted in to cross-account backup.
Returns an error if the account is not an Organizations management account. Use the
`DescribeGlobalSettings` API to determine the current settings.

## Request Syntax

```
PUT /global-settings HTTP/1.1
Content-type: application/json

{
   "GlobalSettings": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[GlobalSettings](#API_UpdateGlobalSettings_RequestSyntax "#API_UpdateGlobalSettings_RequestSyntax")**

Inputs can include:

A value for `isCrossAccountBackupEnabled` and a Region. Example:
`update-global-settings --global-settings isCrossAccountBackupEnabled=false
 --region us-west-2`.

A value for Multi-party approval, styled as "Mpa": `isMpaEnabled`. Values can
be true or false. Example:
`update-global-settings --global-settings isMpaEnabled=false
 --region us-west-2`.

Type: String to string map

Required: No

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**InvalidRequestException**

Indicates that something is wrong with the input to the request. For example, a
parameter is of the wrong type.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/cli2/backup-2018-11-15/UpdateGlobalSettings.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateGlobalSettings.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/SdkForCpp/backup-2018-11-15/UpdateGlobalSettings.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/SdkForGoV2/backup-2018-11-15/UpdateGlobalSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateGlobalSettings.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateGlobalSettings.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/SdkForKotlin/backup-2018-11-15/UpdateGlobalSettings.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateGlobalSettings.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/boto3/backup-2018-11-15/UpdateGlobalSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateGlobalSettings.md "../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateGlobalSettings.md")
