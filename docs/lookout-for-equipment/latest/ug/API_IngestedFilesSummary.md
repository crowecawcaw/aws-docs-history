On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# IngestedFilesSummary

Gives statistics about how many files have been ingested, and which files have not been
ingested, for a particular ingestion job.

## Contents

**IngestedNumberOfFiles**

Indicates the number of files that were successfully ingested.

Type: Integer

Required: Yes

**TotalNumberOfFiles**

Indicates the total number of files that were submitted for ingestion.

Type: Integer

Required: Yes

**DiscardedFiles**

Indicates the number of files that were discarded. A file could be discarded because its
format is invalid (for example, a jpg or pdf) or not readable.

Type: Array of [S3Object](API_S3Object.md "API_S3Object.md") objects

Array Members: Minimum number of 0 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/IngestedFilesSummary.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/IngestedFilesSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/IngestedFilesSummary.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/IngestedFilesSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/IngestedFilesSummary.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/IngestedFilesSummary.md")
