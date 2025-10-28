# S3LogDestination

The Amazon S3 logging configuration settings for the pipe.

## Contents

**BucketName**

The name of the Amazon S3 bucket to which EventBridge delivers the log
records for the pipe.

Type: String

Required: No

**BucketOwner**

The AWS account that owns the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.

Type: String

Required: No

**OutputFormat**

The format EventBridge uses for the log records.

EventBridge currently only supports `json` formatting.

Type: String

Valid Values: `json | plain | w3c`

Required: No

**Prefix**

The prefix text with which to begin Amazon S3 log object names.

For more information, see [Organizing objects using
prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the _Amazon Simple Storage Service User Guide_.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/S3LogDestination.md "../../../goto/SdkForCpp/pipes-2015-10-07/S3LogDestination.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/S3LogDestination.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/S3LogDestination.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/S3LogDestination.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/S3LogDestination.md")
