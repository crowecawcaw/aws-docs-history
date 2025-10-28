# DatasetSummary

Provides a summary of the properties of a dataset. For a complete listing, call the
[DescribeDataset](API_DescribeDataset.md "API_DescribeDataset.md") API.

## Contents

**creationDateTime**

The date and time (in Unix time) that the dataset was created.

Type: Timestamp

Required: No

**datasetArn**

The Amazon Resource Name (ARN) of the dataset.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**datasetType**

The dataset type. One of the following values:

- Interactions
- Items
- Users
- Event-Interactions

Type: String

Length Constraints: Maximum length of 256.

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the dataset was last updated.

Type: Timestamp

Required: No

**name**

The name of the dataset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**status**

The status of the dataset.

A dataset can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DatasetSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/DatasetSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetSummary.md")
