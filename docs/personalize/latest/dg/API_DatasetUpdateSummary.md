# DatasetUpdateSummary

Describes an update to a dataset.

## Contents

**creationDateTime**

The creation date and time (in Unix time) of the dataset update.

Type: Timestamp

Required: No

**failureReason**

If updating a dataset fails, provides the reason why.

Type: String

Required: No

**lastUpdatedDateTime**

The last update date and time (in Unix time) of the dataset.

Type: Timestamp

Required: No

**schemaArn**

The Amazon Resource Name (ARN) of the schema that replaced the previous schema of the dataset.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**status**

The status of the dataset update.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DatasetUpdateSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/DatasetUpdateSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetUpdateSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetUpdateSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetUpdateSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetUpdateSummary.md")
