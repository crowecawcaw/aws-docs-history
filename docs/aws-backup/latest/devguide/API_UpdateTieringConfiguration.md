# UpdateTieringConfiguration

This request will send changes to your specified tiering
configuration. `TieringConfigurationName`
cannot be updated after it is created.

`ResourceSelection` can contain:

- `Resources`
- `TieringDownSettingsInDays`
- `ResourceType`

## Request Syntax

```
PUT /tiering-configurations/`tieringConfigurationName` HTTP/1.1
Content-type: application/json

{
   "TieringConfiguration": {
      "BackupVaultName": "`string`",
      "ResourceSelection": [
         {
            "Resources": [ "`string`" ],
            "ResourceType": "`string`",
            "TieringDownSettingsInDays": `number`
         }
      ]
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[tieringConfigurationName](#API_UpdateTieringConfiguration_RequestSyntax "#API_UpdateTieringConfiguration_RequestSyntax")**

The name of a tiering configuration to update.

Pattern: `^[a-zA-Z0-9_]{1,200}$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[TieringConfiguration](#API_UpdateTieringConfiguration_RequestSyntax "#API_UpdateTieringConfiguration_RequestSyntax")**

Specifies the body of a tiering configuration.

Type: [TieringConfigurationInputForUpdate](API_TieringConfigurationInputForUpdate.md "API_TieringConfigurationInputForUpdate.md") object

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": ***number***,
   "LastUpdatedTime": ***number***,
   "TieringConfigurationArn": "***string***",
   "TieringConfigurationName": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_UpdateTieringConfiguration_ResponseSyntax "#API_UpdateTieringConfiguration_ResponseSyntax")**

The date and time a tiering configuration was created, in Unix format
and Coordinated Universal Time (UTC). The value of `CreationTime`
is accurate to milliseconds. For example, the value 1516925490.087 represents
Friday, January 26, 2018 12:11:30.087AM.

Type: Timestamp

**[LastUpdatedTime](#API_UpdateTieringConfiguration_ResponseSyntax "#API_UpdateTieringConfiguration_ResponseSyntax")**

The date and time a tiering configuration was updated, in Unix format
and Coordinated Universal Time (UTC). The value of `LastUpdatedTime`
is accurate to milliseconds. For example, the value 1516925490.087 represents
Friday, January 26, 2018 12:11:30.087AM.

Type: Timestamp

**[TieringConfigurationArn](#API_UpdateTieringConfiguration_ResponseSyntax "#API_UpdateTieringConfiguration_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies the updated
tiering configuration.

Type: String

**[TieringConfigurationName](#API_UpdateTieringConfiguration_ResponseSyntax "#API_UpdateTieringConfiguration_ResponseSyntax")**

This unique string is the name of the tiering configuration.

Type: String

Pattern: `^[a-zA-Z0-9_]{1,200}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AlreadyExistsException**

The required resource already exists.

**Arn**

**Context**

**CreatorRequestId**

**Type**

HTTP Status Code: 400

**ConflictException**

AWS Backup can't perform the action that you requested until it finishes
performing a previous action. Try again later.

**Context**

**Type**

HTTP Status Code: 400

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**LimitExceededException**

A limit in the request has been exceeded; for example, a maximum number of items allowed
in a request.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/cli2/backup-2018-11-15/UpdateTieringConfiguration.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateTieringConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/SdkForCpp/backup-2018-11-15/UpdateTieringConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/SdkForGoV2/backup-2018-11-15/UpdateTieringConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateTieringConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateTieringConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/SdkForKotlin/backup-2018-11-15/UpdateTieringConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateTieringConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/boto3/backup-2018-11-15/UpdateTieringConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateTieringConfiguration.md "../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateTieringConfiguration.md")
