# ValidationConfiguration

Configuration for data quality validation. Used to select the Rulesets and Validation Mode
to be used in the profile job. When ValidationConfiguration is null, the profile
job will run without data quality validation.

## Contents

###### Note

In the following list, the required parameters are described first.

**RulesetArn**

The Amazon Resource Name (ARN) for the ruleset to be validated in the profile job.
The TargetArn of the selected ruleset should be the same as the Amazon Resource Name (ARN) of
the dataset that is associated with the profile job.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: Yes

**ValidationMode**

Mode of data quality validation. Default mode is “CHECK_ALL” which verifies all rules
defined in the selected ruleset.

Type: String

Valid Values: `CHECK_ALL`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ValidationConfiguration.md "../../../goto/SdkForCpp/databrew-2017-07-25/ValidationConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ValidationConfiguration.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ValidationConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ValidationConfiguration.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ValidationConfiguration.md")
