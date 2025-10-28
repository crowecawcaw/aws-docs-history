# AdapterVersionDatasetConfig

The dataset configuration options for a given version of an adapter.
Can include an Amazon S3 bucket if specified.

## Contents

**ManifestS3Object**

The S3 bucket name and file name that identifies the document.

The AWS Region for the S3 bucket that contains the document must match the Region that
you use for Amazon Textract operations.

For Amazon Textract to process a file in an S3 bucket, the user must have
permission to access the S3 bucket and file.

Type: [S3Object](API_S3Object.md "API_S3Object.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/AdapterVersionDatasetConfig.md "../../../goto/SdkForCpp/textract-2018-06-27/AdapterVersionDatasetConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/AdapterVersionDatasetConfig.md "../../../goto/SdkForJavaV2/textract-2018-06-27/AdapterVersionDatasetConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/AdapterVersionDatasetConfig.md "../../../goto/SdkForRubyV3/textract-2018-06-27/AdapterVersionDatasetConfig.md")
