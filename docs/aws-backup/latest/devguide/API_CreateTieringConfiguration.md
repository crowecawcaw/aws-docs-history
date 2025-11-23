# CreateTieringConfiguration

Creates a tiering configuration.

A tiering configuration enables automatic movement of backup data to a lower-cost storage tier based on the age of backed-up objects in the backup vault.

Each vault can only have one vault-specific tiering configuration, in addition to any global configuration that applies to all vaults.

## Request Syntax

```
PUT /tiering-configurations HTTP/1.1
Content-type: application/json

{
   "CreatorRequestId": "`string`",
   "TieringConfiguration": {
      "BackupVaultName": "`string`",
      "ResourceSelection": [
         {
            "Resources": [ "`string`" ],
            "ResourceType": "`string`",
            "TieringDownSettingsInDays": `number`
         }
      ],
      "TieringConfigurationName": "`string`"
   },
   "TieringConfigurationTags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[CreatorRequestId](#API_CreateTieringConfiguration_RequestSyntax "#API_CreateTieringConfiguration_RequestSyntax")**

This is a unique string that identifies the request and
allows failed requests to be retried without the risk of running
the operation twice. This parameter is optional. If used, this
parameter must contain 1 to 50 alphanumeric or '-\_.' characters.

Type: String

Required: No

**[TieringConfiguration](#API_CreateTieringConfiguration_RequestSyntax "#API_CreateTieringConfiguration_RequestSyntax")**

A tiering configuration must contain a unique `TieringConfigurationName` string
you create and must contain a `BackupVaultName` and `ResourceSelection`.
You may optionally include a `CreatorRequestId` string.

The `TieringConfigurationName` is a unique string that is the name of the
tiering configuration. This cannot be changed after creation, and it must consist of only
alphanumeric characters and underscores.

Type: [TieringConfigurationInputForCreate](API_TieringConfigurationInputForCreate.md "API_TieringConfigurationInputForCreate.md") object

Required: Yes

**[TieringConfigurationTags](#API_CreateTieringConfiguration_RequestSyntax "#API_CreateTieringConfiguration_RequestSyntax")**

The tags to assign to the tiering configuration.

Type: String to string map

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": ***number***,
   "TieringConfigurationArn": "***string***",
   "TieringConfigurationName": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_CreateTieringConfiguration_ResponseSyntax "#API_CreateTieringConfiguration_ResponseSyntax")**

The date and time a tiering configuration was created, in Unix format
and Coordinated Universal Time (UTC). The value of `CreationTime`
is accurate to milliseconds. For example, the value 1516925490.087 represents
Friday, January 26, 2018 12:11:30.087AM.

Type: Timestamp

**[TieringConfigurationArn](#API_CreateTieringConfiguration_ResponseSyntax "#API_CreateTieringConfiguration_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies the created
tiering configuration.

Type: String

**[TieringConfigurationName](#API_CreateTieringConfiguration_ResponseSyntax "#API_CreateTieringConfiguration_ResponseSyntax")**

This unique string is the name of the tiering configuration.

The name cannot be changed after creation. The name consists of only
alphanumeric characters and underscores. Maximum length is 200.

Type: String

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

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/cli2/backup-2018-11-15/CreateTieringConfiguration.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/DotNetSDKV3/backup-2018-11-15/CreateTieringConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/SdkForCpp/backup-2018-11-15/CreateTieringConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/SdkForGoV2/backup-2018-11-15/CreateTieringConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CreateTieringConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateTieringConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/SdkForKotlin/backup-2018-11-15/CreateTieringConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CreateTieringConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/boto3/backup-2018-11-15/CreateTieringConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CreateTieringConfiguration.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CreateTieringConfiguration.md")
