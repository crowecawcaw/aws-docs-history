After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# ApplicationDetail

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Provides a description of the application, including the application Amazon Resource
Name (ARN), status, latest version, and input and output configuration.

## Contents

**ApplicationARN**

ARN of the application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

**ApplicationName**

Name of the application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**ApplicationStatus**

Status of the application.

Type: String

Valid Values: `DELETING | STARTING | STOPPING | READY | RUNNING | UPDATING | AUTOSCALING`

Required: Yes

**ApplicationVersionId**

Provides the current application version.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 999999999.

Required: Yes

**ApplicationCode**

Returns the application code that you provided to perform data analysis on any of the
in-application streams in your application.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 102400.

Required: No

**ApplicationDescription**

Description of the application.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Required: No

**CloudWatchLoggingOptionDescriptions**

Describes the CloudWatch log streams that are configured to receive application
messages. For more information about using CloudWatch log streams with Amazon Kinesis
Analytics applications, see [Working with Amazon
CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md").

Type: Array of [CloudWatchLoggingOptionDescription](API_CloudWatchLoggingOptionDescription.md "API_CloudWatchLoggingOptionDescription.md") objects

Required: No

**CreateTimestamp**

Time stamp when the application version was created.

Type: Timestamp

Required: No

**InputDescriptions**

Describes the application input configuration. For more information, see [Configuring Application Input](how-it-works-input.md "how-it-works-input.md").

Type: Array of [InputDescription](API_InputDescription.md "API_InputDescription.md") objects

Required: No

**LastUpdateTimestamp**

Time stamp when the application was last updated.

Type: Timestamp

Required: No

**OutputDescriptions**

Describes the application output configuration. For more information, see [Configuring Application Output](how-it-works-output.md "how-it-works-output.md").

Type: Array of [OutputDescription](API_OutputDescription.md "API_OutputDescription.md") objects

Required: No

**ReferenceDataSourceDescriptions**

Describes reference data sources configured for the application. For more information,
see [Configuring Application
Input](how-it-works-input.md "how-it-works-input.md").

Type: Array of [ReferenceDataSourceDescription](API_ReferenceDataSourceDescription.md "API_ReferenceDataSourceDescription.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ApplicationDetail.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ApplicationDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ApplicationDetail.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ApplicationDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ApplicationDetail.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ApplicationDetail.md")
