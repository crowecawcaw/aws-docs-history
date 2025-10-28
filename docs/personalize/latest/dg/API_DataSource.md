# DataSource

Describes the data source that contains the data to upload to a dataset, or the list of
records to delete from Amazon Personalize.

## Contents

**dataLocation**

For dataset import jobs, the path to the Amazon S3 bucket where the data that you want to upload to
your dataset is stored. For data deletion jobs, the path to the Amazon S3 bucket that stores the list of records to delete.

For example:

`s3://bucket-name/folder-name/fileName.csv`

If your CSV files are in a folder in your Amazon S3 bucket and you want your import job or data deletion job
to consider multiple files, you can specify the path to the folder. With a data deletion job, Amazon Personalize uses all files in the folder and any sub folder. Use the following syntax with a `/` after the folder
name:

`s3://bucket-name/folder-name/`

Type: String

Length Constraints: Maximum length of 256.

Pattern: `(s3|http|https)://.+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DataSource.md "../../../goto/SdkForCpp/personalize-2018-05-22/DataSource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DataSource.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DataSource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DataSource.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DataSource.md")
