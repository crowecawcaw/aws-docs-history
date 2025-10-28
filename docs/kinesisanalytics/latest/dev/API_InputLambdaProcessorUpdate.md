After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# InputLambdaProcessorUpdate

Represents an update to the [InputLambdaProcessor](API_InputLambdaProcessor.md "API_InputLambdaProcessor.md") that is used to preprocess the records in the
stream.

## Contents

**ResourceARNUpdate**

The Amazon Resource Name (ARN) of the new [AWS Lambda](../../../lambda.md "../../../lambda.md") function that is used to preprocess the records in
the stream.

###### Note

To specify an earlier version of the Lambda function than the latest, include the
Lambda function version in the Lambda function ARN. For more information about
Lambda ARNs, see [Example
ARNs: AWS Lambda](../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-lambda "../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-lambda")

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: No

**RoleARNUpdate**

The ARN of the new IAM role that is used to access the AWS Lambda
function.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputLambdaProcessorUpdate.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/InputLambdaProcessorUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputLambdaProcessorUpdate.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/InputLambdaProcessorUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputLambdaProcessorUpdate.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/InputLambdaProcessorUpdate.md")
