End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# StartMigration

Starts migrating a bot from Amazon Lex V1 to Amazon Lex V2. Migrate your bot when
you want to take advantage of the new features of Amazon Lex V2.

For more information, see [Migrating a bot](migrate.md "migrate.md") in the _Amazon Lex
developer guide_.

## Request Syntax

```
POST /migrations HTTP/1.1
Content-type: application/json

{
   "migrationStrategy": "`string`",
   "v1BotName": "`string`",
   "v1BotVersion": "`string`",
   "v2BotName": "`string`",
   "v2BotRole": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[migrationStrategy](#API_StartMigration_RequestSyntax "#API_StartMigration_RequestSyntax")**

The strategy used to conduct the migration.

- `CREATE_NEW` - Creates a new Amazon Lex V2 bot and migrates
  the Amazon Lex V1 bot to the new bot.
- `UPDATE_EXISTING` - Overwrites the existing Amazon Lex V2 bot
  metadata and the locale being migrated. It doesn't change any other
  locales in the Amazon Lex V2 bot. If the locale doesn't exist, a new locale
  is created in the Amazon Lex V2 bot.

Type: String

Valid Values: `CREATE_NEW | UPDATE_EXISTING`

Required: Yes

**[v1BotName](#API_StartMigration_RequestSyntax "#API_StartMigration_RequestSyntax")**

The name of the Amazon Lex V1 bot that you are migrating to Amazon Lex V2.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[v1BotVersion](#API_StartMigration_RequestSyntax "#API_StartMigration_RequestSyntax")**

The version of the bot to migrate to Amazon Lex V2. You can migrate the
`$LATEST` version as well as any numbered version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: Yes

**[v2BotName](#API_StartMigration_RequestSyntax "#API_StartMigration_RequestSyntax")**

The name of the Amazon Lex V2 bot that you are migrating the Amazon Lex V1 bot to.

- If the Amazon Lex V2 bot doesn't exist, you must use the
  `CREATE_NEW` migration strategy.
- If the Amazon Lex V2 bot exists, you must use the
  `UPDATE_EXISTING` migration strategy to change the
  contents of the Amazon Lex V2 bot.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([0-9a-zA-Z][_-]?)+$`

Required: Yes

**[v2BotRole](#API_StartMigration_RequestSyntax "#API_StartMigration_RequestSyntax")**

The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:[\w\-]+:iam::[\d]{12}:role/.+$`

Required: Yes

## Response Syntax

```
HTTP/1.1 202
Content-type: application/json

{
   "migrationId": "***string***",
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

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

**[migrationId](#API_StartMigration_ResponseSyntax "#API_StartMigration_ResponseSyntax")**

The unique identifier that Amazon Lex assigned to the migration.

Type: String

Length Constraints: Fixed length of 10.

Pattern: `^[0-9a-zA-Z]+$`

**[migrationStrategy](#API_StartMigration_ResponseSyntax "#API_StartMigration_ResponseSyntax")**

The strategy used to conduct the migration.

Type: String

Valid Values: `CREATE_NEW | UPDATE_EXISTING`

**[migrationTimestamp](#API_StartMigration_ResponseSyntax "#API_StartMigration_ResponseSyntax")**

The date and time that the migration started.

Type: Timestamp

**[v1BotLocale](#API_StartMigration_ResponseSyntax "#API_StartMigration_ResponseSyntax")**

The locale used for the Amazon Lex V1 bot.

Type: String

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

**[v1BotName](#API_StartMigration_ResponseSyntax "#API_StartMigration_ResponseSyntax")**

The name of the Amazon Lex V1 bot that you are migrating to Amazon Lex V2.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

**[v1BotVersion](#API_StartMigration_ResponseSyntax "#API_StartMigration_ResponseSyntax")**

The version of the bot to migrate to Amazon Lex V2.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

**[v2BotId](#API_StartMigration_ResponseSyntax "#API_StartMigration_ResponseSyntax")**

The unique identifier for the Amazon Lex V2 bot.

Type: String

Length Constraints: Fixed length of 10.

Pattern: `^[0-9a-zA-Z]+$`

**[v2BotRole](#API_StartMigration_ResponseSyntax "#API_StartMigration_ResponseSyntax")**

The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:[\w\-]+:iam::[\d]{12}:role/.+$`

## Errors

**AccessDeniedException**

Your IAM user or role does not have permission to call the Amazon Lex V2
APIs required to migrate your bot.

HTTP Status Code: 403

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/StartMigration.md "../../../goto/cli2/lex-models-2017-04-19/StartMigration.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/StartMigration.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/StartMigration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/StartMigration.md "../../../goto/SdkForCpp/lex-models-2017-04-19/StartMigration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/StartMigration.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/StartMigration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/StartMigration.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/StartMigration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/StartMigration.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/StartMigration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/StartMigration.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/StartMigration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/StartMigration.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/StartMigration.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/StartMigration.md "../../../goto/boto3/lex-models-2017-04-19/StartMigration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/StartMigration.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/StartMigration.md")
