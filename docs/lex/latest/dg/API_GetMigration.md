End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetMigration

Provides details about an ongoing or complete migration from an
Amazon Lex V1 bot to an Amazon Lex V2 bot. Use this operation to view the migration
alerts and warnings related to the migration.

## Request Syntax

```
GET /migrations/`migrationId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[migrationId](#API_GetMigration_RequestSyntax "#API_GetMigration_RequestSyntax")**

The unique identifier of the migration to view. The
`migrationID` is returned by the [StartMigration](API_StartMigration.md "API_StartMigration.md") operation.

Length Constraints: Fixed length of 10.

Pattern: `^[0-9a-zA-Z]+$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "alerts": [
      {
         "details": [ "***string***" ],
         "message": "***string***",
         "referenceURLs": [ "***string***" ],
         "type": "***string***"
      }
   ],
   "migrationId": "***string***",
   "migrationStatus": "***string***",
   "migrationStrategy": "***string***",
   "migrationTimestamp": ***number***,
   "v1BotLocale": "***string***",
   "v1BotName": "***string***",
   "v1BotVersion": "***string***",
   "v2BotId": "***string***",
   "v2BotRole": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[alerts](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

A list of alerts and warnings that indicate issues with the migration
for the Amazon Lex V1 bot to Amazon Lex V2. You receive a warning when an Amazon Lex V1
feature has a different implementation in Amazon Lex V2.

For more information, see [Migrating a bot](../../../lexv2/latest/dg/migrate.md "../../../lexv2/latest/dg/migrate.md") in the _Amazon Lex V2
developer guide_.

Type: Array of [MigrationAlert](API_MigrationAlert.md "API_MigrationAlert.md") objects

**[migrationId](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

The unique identifier of the migration. This is the same as the
identifier used when calling the `GetMigration`
operation.

Type: String

Length Constraints: Fixed length of 10.

Pattern: `^[0-9a-zA-Z]+$`

**[migrationStatus](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

Indicates the status of the migration. When the status is
`COMPLETE` the migration is finished and the bot is available
in Amazon Lex V2. There may be alerts and warnings that need to be resolved to
complete the migration.

Type: String

Valid Values: `IN_PROGRESS | COMPLETED | FAILED`

**[migrationStrategy](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

The strategy used to conduct the migration.

- `CREATE_NEW` - Creates a new Amazon Lex V2 bot and migrates
  the Amazon Lex V1 bot to the new bot.
- `UPDATE_EXISTING` - Overwrites the existing Amazon Lex V2 bot
  metadata and the locale being migrated. It doesn't change any other
  locales in the Amazon Lex V2 bot. If the locale doesn't exist, a new locale
  is created in the Amazon Lex V2 bot.

Type: String

Valid Values: `CREATE_NEW | UPDATE_EXISTING`

**[migrationTimestamp](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

The date and time that the migration started.

Type: Timestamp

**[v1BotLocale](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

The locale of the Amazon Lex V1 bot migrated to Amazon Lex V2.

Type: String

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

**[v1BotName](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

The name of the Amazon Lex V1 bot migrated to Amazon Lex V2.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

**[v1BotVersion](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

The version of the Amazon Lex V1 bot migrated to Amazon Lex V2.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

**[v2BotId](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

The unique identifier of the Amazon Lex V2 bot that the Amazon Lex V1 is being
migrated to.

Type: String

Length Constraints: Fixed length of 10.

Pattern: `^[0-9a-zA-Z]+$`

**[v2BotRole](#API_GetMigration_ResponseSyntax "#API_GetMigration_ResponseSyntax")**

The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:[\w\-]+:iam::[\d]{12}:role/.+$`

## Errors

**BadRequestException**

The request is not well formed. For example, a value is invalid or
a required field is missing. Check the field values, and try
again.

HTTP Status Code: 400

**InternalFailureException**

An internal Amazon Lex error occurred. Try your request again.

HTTP Status Code: 500

**LimitExceededException**

The request exceeded a limit. Try your request again.

HTTP Status Code: 429

**NotFoundException**

The resource specified in the request was not found. Check the
resource and try again.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetMigration.md "../../../goto/cli2/lex-models-2017-04-19/GetMigration.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetMigration.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetMigration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetMigration.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetMigration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetMigration.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetMigration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetMigration.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetMigration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetMigration.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetMigration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetMigration.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetMigration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetMigration.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetMigration.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetMigration.md "../../../goto/boto3/lex-models-2017-04-19/GetMigration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetMigration.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetMigration.md")
