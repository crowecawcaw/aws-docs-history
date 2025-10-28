End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# MigrationSummary

Provides information about migrating a bot from Amazon Lex V1 to
Amazon Lex V2.

## Contents

**migrationId**

The unique identifier that Amazon Lex assigned to the migration.

Type: String

Length Constraints: Fixed length of 10.

Pattern: `^[0-9a-zA-Z]+$`

Required: No

**migrationStatus**

The status of the operation. When the status is `COMPLETE`
the bot is available in Amazon Lex V2. There may be alerts and warnings that
need to be resolved to complete the migration.

Type: String

Valid Values: `IN_PROGRESS | COMPLETED | FAILED`

Required: No

**migrationStrategy**

The strategy used to conduct the migration.

Type: String

Valid Values: `CREATE_NEW | UPDATE_EXISTING`

Required: No

**migrationTimestamp**

The date and time that the migration started.

Type: Timestamp

Required: No

**v1BotLocale**

The locale of the Amazon Lex V1 bot that is the source of the
migration.

Type: String

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

Required: No

**v1BotName**

The name of the Amazon Lex V1 bot that is the source of the
migration.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: No

**v1BotVersion**

The version of the Amazon Lex V1 bot that is the source of the
migration.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: No

**v2BotId**

The unique identifier of the Amazon Lex V2 that is the destination of the
migration.

Type: String

Length Constraints: Fixed length of 10.

Pattern: `^[0-9a-zA-Z]+$`

Required: No

**v2BotRole**

The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:[\w\-]+:iam::[\d]{12}:role/.+$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/MigrationSummary.md "../../../goto/SdkForCpp/lex-models-2017-04-19/MigrationSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/MigrationSummary.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/MigrationSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/MigrationSummary.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/MigrationSummary.md")
