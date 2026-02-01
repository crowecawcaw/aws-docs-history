# GetTieringConfiguration

Returns `TieringConfiguration` details for the specified
`TieringConfigurationName`. The details are the body of a tiering configuration
in JSON format, in addition to configuration metadata.

## Request Syntax

```
GET /tiering-configurations/`tieringConfigurationName` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[tieringConfigurationName](#API_GetTieringConfiguration_RequestSyntax "#API_GetTieringConfiguration_RequestSyntax")**

The unique name of a tiering configuration.

Pattern: `^[a-zA-Z0-9_]{1,200}$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "TieringConfiguration": {
      "BackupVaultName": "***string***",
      "CreationTime": ***number***,
      "CreatorRequestId": "***string***",
      "LastUpdatedTime": ***number***,
      "ResourceSelection": [
         {
            "Resources": [ "***string***" ],
            "ResourceType": "***string***",
            "TieringDownSettingsInDays": ***number***
         }
      ],
      "TieringConfigurationArn": "***string***",
      "TieringConfigurationName": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[TieringConfiguration](#API_GetTieringConfiguration_ResponseSyntax "#API_GetTieringConfiguration_ResponseSyntax")**

Specifies the body of a tiering configuration. Includes `TieringConfigurationName`.

Type: [TieringConfiguration](API_TieringConfiguration.md "API_TieringConfiguration.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/cli2/backup-2018-11-15/GetTieringConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/DotNetSDKV4/backup-2018-11-15/GetTieringConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/SdkForCpp/backup-2018-11-15/GetTieringConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetTieringConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetTieringConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetTieringConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetTieringConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetTieringConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/boto3/backup-2018-11-15/GetTieringConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetTieringConfiguration.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetTieringConfiguration.md")
