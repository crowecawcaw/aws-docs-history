End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetMigrations

Gets a list of migrations between Amazon Lex V1 and Amazon Lex V2.

## Request Syntax

```
GET /migrations?maxResults=`maxResults`&migrationStatusEquals=`migrationStatusEquals`&nextToken=`nextToken`&sortByAttribute=`sortByAttribute`&sortByOrder=`sortByOrder`&v1BotNameContains=`v1BotNameContains` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[maxResults](#API_GetMigrations_RequestSyntax "#API_GetMigrations_RequestSyntax")**

The maximum number of migrations to return in the response. The
default is 10.

Valid Range: Minimum value of 1. Maximum value of 50.

**[migrationStatusEquals](#API_GetMigrations_RequestSyntax "#API_GetMigrations_RequestSyntax")**

Filters the list to contain only migrations in the specified
state.

Valid Values: `IN_PROGRESS | COMPLETED | FAILED`

**[nextToken](#API_GetMigrations_RequestSyntax "#API_GetMigrations_RequestSyntax")**

A pagination token that fetches the next page of migrations. If the
response to this operation is truncated, Amazon Lex returns a pagination token
in the response. To fetch the next page of migrations, specify the
pagination token in the request.

**[sortByAttribute](#API_GetMigrations_RequestSyntax "#API_GetMigrations_RequestSyntax")**

The field to sort the list of migrations by. You can sort by the
Amazon Lex V1 bot name or the date and time that the migration was
started.

Valid Values: `V1_BOT_NAME | MIGRATION_DATE_TIME`

**[sortByOrder](#API_GetMigrations_RequestSyntax "#API_GetMigrations_RequestSyntax")**

The order so sort the list.

Valid Values: `ASCENDING | DESCENDING`

**[v1BotNameContains](#API_GetMigrations_RequestSyntax "#API_GetMigrations_RequestSyntax")**

Filters the list to contain only bots whose name contains the
specified string. The string is matched anywhere in the bot name.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "migrationSummaries": [
      {
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
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[migrationSummaries](#API_GetMigrations_ResponseSyntax "#API_GetMigrations_ResponseSyntax")**

An array of summaries for migrations from Amazon Lex V1 to Amazon Lex V2. To see
details of the migration, use the `migrationId` from the
summary in a call to the [GetMigration](API_GetMigration.md "API_GetMigration.md")
operation.

Type: Array of [MigrationSummary](API_MigrationSummary.md "API_MigrationSummary.md") objects

**[nextToken](#API_GetMigrations_ResponseSyntax "#API_GetMigrations_ResponseSyntax")**

If the response is truncated, it includes a pagination token that you
can specify in your next request to fetch the next page of
migrations.

Type: String

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetMigrations.md "../../../goto/cli2/lex-models-2017-04-19/GetMigrations.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetMigrations.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetMigrations.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetMigrations.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetMigrations.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetMigrations.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetMigrations.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetMigrations.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetMigrations.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetMigrations.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetMigrations.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetMigrations.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetMigrations.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetMigrations.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetMigrations.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetMigrations.md "../../../goto/boto3/lex-models-2017-04-19/GetMigrations.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetMigrations.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetMigrations.md")
