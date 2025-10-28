# Promotion

Contains information on a promotion. A promotion defines additional business rules that apply to a configurable subset of recommended items.

## Contents

**filterArn**

The Amazon Resource Name (ARN) of the filter used by the promotion. This filter defines the criteria for promoted items. For more information, see
[Promotion filters](promoting-items.md#promotion-filters "promoting-items.md#promotion-filters").

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**filterValues**

The values to use when promoting items.
For each placeholder parameter in your promotion's filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.

For filter expressions that use an `INCLUDE` element to include items,
you must provide values for all parameters that are defined in the expression. For
filters with expressions that use an `EXCLUDE` element to exclude items, you
can omit the `filter-values`. In this case, Amazon Personalize doesn't use that portion of
the expression to filter recommendations.

For more information on creating filters, see
[Filtering recommendations and user segments](filter.md "filter.md").

Type: String to string map

Map Entries: Maximum number of 25 items.

Key Length Constraints: Maximum length of 50.

Key Pattern: `[A-Za-z0-9_]+`

Value Length Constraints: Maximum length of 1000.

Required: No

**name**

The name of the promotion.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**percentPromotedItems**

The percentage of recommended items to apply the promotion to.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-runtime-2018-05-22/Promotion.md "../../../goto/SdkForCpp/personalize-runtime-2018-05-22/Promotion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-runtime-2018-05-22/Promotion.md "../../../goto/SdkForJavaV2/personalize-runtime-2018-05-22/Promotion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-runtime-2018-05-22/Promotion.md "../../../goto/SdkForRubyV3/personalize-runtime-2018-05-22/Promotion.md")
