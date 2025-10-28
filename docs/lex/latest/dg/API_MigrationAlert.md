End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# MigrationAlert

Provides information about alerts and warnings that Amazon Lex sends during
a migration. The alerts include information about how to resolve the
issue.

## Contents

**details**

Additional details about the alert.

Type: Array of strings

Required: No

**message**

A message that describes why the alert was issued.

Type: String

Required: No

**referenceURLs**

A link to the Amazon Lex documentation that describes how to resolve the
alert.

Type: Array of strings

Required: No

**type**

The type of alert. There are two kinds of alerts:

- `ERROR` - There was an issue with the migration that
  can't be resolved. The migration stops.
- `WARN` - There was an issue with the migration that
  requires manual changes to the new Amazon Lex V2 bot. The migration
  continues.

Type: String

Valid Values: `ERROR | WARN`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/MigrationAlert.md "../../../goto/SdkForCpp/lex-models-2017-04-19/MigrationAlert.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/MigrationAlert.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/MigrationAlert.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/MigrationAlert.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/MigrationAlert.md")
