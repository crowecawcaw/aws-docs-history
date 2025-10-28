# UpdateSettings

Updates the configurable settings for the specified directory.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "Settings": [
      {
         "Name": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_UpdateSettings_RequestSyntax "#API_UpdateSettings_RequestSyntax")**

The identifier of the directory for which to update settings.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[Settings](#API_UpdateSettings_RequestSyntax "#API_UpdateSettings_RequestSyntax")**

The list of [Setting](API_Setting.md "API_Setting.md") objects.

Type: Array of [Setting](API_Setting.md "API_Setting.md") objects

Required: Yes

## Response Syntax

```
{
   "DirectoryId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DirectoryId](#API_UpdateSettings_ResponseSyntax "#API_UpdateSettings_ResponseSyntax")**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

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

**DirectoryUnavailableException**

The specified directory is unavailable.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**IncompatibleSettingsException**

The specified directory setting is not compatible with other settings.

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

**UnsupportedSettingsException**

The specified directory setting is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/UpdateSettings.md "../../../goto/cli2/ds-2015-04-16/UpdateSettings.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateSettings.md "../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateSettings.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/UpdateSettings.md "../../../goto/SdkForCpp/ds-2015-04-16/UpdateSettings.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/UpdateSettings.md "../../../goto/SdkForGoV2/ds-2015-04-16/UpdateSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateSettings.md "../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateSettings.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateSettings.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateSettings.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/UpdateSettings.md "../../../goto/SdkForKotlin/ds-2015-04-16/UpdateSettings.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateSettings.md "../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateSettings.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/UpdateSettings.md "../../../goto/boto3/ds-2015-04-16/UpdateSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateSettings.md "../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateSettings.md")
