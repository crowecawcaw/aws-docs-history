# PathOptions

Represents a set of options that define how DataBrew selects files for a given Amazon S3
path in a dataset.

## Contents

###### Note

In the following list, the required parameters are described first.

**FilesLimit**

If provided, this structure imposes a limit on a number of files that should be selected.

Type: [FilesLimit](API_FilesLimit.md "API_FilesLimit.md") object

Required: No

**LastModifiedDateCondition**

If provided, this structure defines a date range for matching Amazon S3 objects based on their
LastModifiedDate attribute in Amazon S3.

Type: [FilterExpression](API_FilterExpression.md "API_FilterExpression.md") object

Required: No

**Parameters**

A structure that maps names of parameters used in the Amazon S3 path of a dataset to their definitions.

Type: String to [DatasetParameter](API_DatasetParameter.md "API_DatasetParameter.md") object map

Map Entries: Maximum number of 10 items.

Key Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/PathOptions.md "../../../goto/SdkForCpp/databrew-2017-07-25/PathOptions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/PathOptions.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/PathOptions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/PathOptions.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/PathOptions.md")
