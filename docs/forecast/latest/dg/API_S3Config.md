Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# S3Config

The path to the file(s) in an Amazon Simple Storage Service (Amazon S3) bucket, and an AWS Identity and Access Management (IAM) role that
Amazon Forecast can assume to access the file(s). Optionally, includes an AWS Key Management Service (KMS) key. This
object is part of the [DataSource](API_DataSource.md "API_DataSource.md") object that is submitted in the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") request, and part of the [DataDestination](API_DataDestination.md "API_DataDestination.md") object.

## Contents

**Path**

The path to an Amazon Simple Storage Service (Amazon S3) bucket or file(s) in an Amazon S3 bucket.

Type: String

Length Constraints: Minimum length of 7. Maximum length of 4096.

Pattern: `^s3://[a-z0-9].+$`

Required: Yes

**RoleArn**

The ARN of the AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3
bucket or files. If you provide a value for the `KMSKeyArn` key, the role must
allow access to the key.

Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your
account, you get an `InvalidInputException` error.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

**KMSKeyArn**

The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:aws:kms:.*:key/.*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/S3Config.md "../../../goto/SdkForCpp/forecast-2018-06-26/S3Config.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/S3Config.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/S3Config.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/S3Config.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/S3Config.md")
