# Filter

Contains information on a recommendation filter, including its ARN, status, and filter
expression.

## Contents

**creationDateTime**

The time at which the filter was created.

Type: Timestamp

Required: No

**datasetGroupArn**

The ARN of the dataset group to which the filter belongs.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**failureReason**

If the filter failed, the reason for its failure.

Type: String

Required: No

**filterArn**

The ARN of the filter.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**filterExpression**

Specifies the type of item interactions to filter out of recommendation results. The
filter expression must follow specific format rules. For information about filter expression structure and syntax, see
[Filter expressions](filter-expressions.md "filter-expressions.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2500.

Required: No

**lastUpdatedDateTime**

The time at which the filter was last updated.

Type: Timestamp

Required: No

**name**

The name of the filter.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**status**

The status of the filter.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/Filter.md "../../../goto/SdkForCpp/personalize-2018-05-22/Filter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/Filter.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/Filter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/Filter.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/Filter.md")
