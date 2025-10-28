End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# LogSettingsResponse

The settings for conversation logs.

## Contents

**destination**

The destination where logs are delivered.

Type: String

Valid Values: `CLOUDWATCH_LOGS | S3`

Required: No

**kmsKeyArn**

The Amazon Resource Name (ARN) of the key used to encrypt audio logs
in an S3 bucket.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:[\w\-]+:kms:[\w\-]+:[\d]{12}:(?:key\/[\w\-]+|alias\/[a-zA-Z0-9:\/_\-]{1,256})$`

Required: No

**logType**

The type of logging that is enabled.

Type: String

Valid Values: `AUDIO | TEXT`

Required: No

**resourceArn**

The Amazon Resource Name (ARN) of the CloudWatch Logs log group or S3
bucket where the logs are delivered.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `^arn:[\w\-]+:(?:logs:[\w\-]+:[\d]{12}:log-group:[\.\-_/#A-Za-z0-9]{1,512}(?::\*)?|s3:::[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9])$`

Required: No

**resourcePrefix**

The resource prefix is the first part of the S3 object key within the
S3 bucket that you specified to contain audio logs. For CloudWatch Logs it
is the prefix of the log stream name within the log group that you
specified.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/LogSettingsResponse.md "../../../goto/SdkForCpp/lex-models-2017-04-19/LogSettingsResponse.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/LogSettingsResponse.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/LogSettingsResponse.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/LogSettingsResponse.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/LogSettingsResponse.md")
