End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# KendraConfiguration

Provides configuration information for the AMAZON.KendraSearchIntent
intent. When you use this intent, Amazon Lex searches the specified Amazon
Kendra index and returns documents from the index that match the user's
utterance. For more information, see [AMAZON.KendraSearchIntent](built-in-intent-kendra-search.md "built-in-intent-kendra-search.md").

## Contents

**kendraIndex**

The Amazon Resource Name (ARN) of the Amazon Kendra index that you
want the AMAZON.KendraSearchIntent intent to search. The index must be in
the same account and Region as the Amazon Lex bot. If the Amazon Kendra index
does not exist, you get an exception when you call the
`PutIntent` operation.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws:kendra:[a-z]+-[a-z]+-[0-9]:[0-9]{12}:index\/[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**role**

The Amazon Resource Name (ARN) of an IAM role that has permission to
search the Amazon Kendra index. The role must be in the same account and
Region as the Amazon Lex bot. If the role does not exist, you get an exception
when you call the `PutIntent` operation.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws:iam::[0-9]{12}:role/.*`

Required: Yes

**queryFilterString**

A query filter that Amazon Lex sends to Amazon Kendra to filter the
response from the query. The filter is in the format defined by Amazon
Kendra. For more information, see [Filtering
queries](../../../kendra/latest/dg/filtering.md "../../../kendra/latest/dg/filtering.md").

You can override this filter string with a new filter string at
runtime.

Type: String

Length Constraints: Minimum length of 0.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/KendraConfiguration.md "../../../goto/SdkForCpp/lex-models-2017-04-19/KendraConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/KendraConfiguration.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/KendraConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/KendraConfiguration.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/KendraConfiguration.md")
