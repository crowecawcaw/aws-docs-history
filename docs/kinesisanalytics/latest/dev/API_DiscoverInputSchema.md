After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# DiscoverInputSchema

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Infers a schema by evaluating sample records on the specified streaming source (Amazon
Kinesis stream or Amazon Kinesis Firehose delivery stream) or S3 object. In the
response, the operation returns the inferred schema and also the sample records that the
operation used to infer the schema.

You can use the inferred schema when configuring a streaming source for your
application. For conceptual information, see [Configuring Application
Input](how-it-works-input.md "how-it-works-input.md"). Note that when you create an application using the Amazon Kinesis
Analytics console, the console uses this operation to infer a schema and show it in the
console user interface.

This operation requires permissions to perform the
`kinesisanalytics:DiscoverInputSchema` action.

## Request Syntax

```
{
   "InputProcessingConfiguration": {
      "InputLambdaProcessor": {
         "ResourceARN": "`string`",
         "RoleARN": "`string`"
      }
   },
   "InputStartingPositionConfiguration": {
      "InputStartingPosition": "`string`"
   },
   "ResourceARN": "`string`",
   "RoleARN": "`string`",
   "S3Configuration": {
      "BucketARN": "`string`",
      "FileKey": "`string`",
      "RoleARN": "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[InputProcessingConfiguration](#API_DiscoverInputSchema_RequestSyntax "#API_DiscoverInputSchema_RequestSyntax")**

The [InputProcessingConfiguration](API_InputProcessingConfiguration.md "API_InputProcessingConfiguration.md") to use to preprocess the records before
discovering the schema of the records.

Type: [InputProcessingConfiguration](API_InputProcessingConfiguration.md "API_InputProcessingConfiguration.md") object

Required: No

**[InputStartingPositionConfiguration](#API_DiscoverInputSchema_RequestSyntax "#API_DiscoverInputSchema_RequestSyntax")**

Point at which you want Amazon Kinesis Analytics to start reading records from the
specified streaming source discovery purposes.

Type: [InputStartingPositionConfiguration](API_InputStartingPositionConfiguration.md "API_InputStartingPositionConfiguration.md") object

Required: No

**[ResourceARN](#API_DiscoverInputSchema_RequestSyntax "#API_DiscoverInputSchema_RequestSyntax")**

Amazon Resource Name (ARN) of the streaming source.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: No

**[RoleARN](#API_DiscoverInputSchema_RequestSyntax "#API_DiscoverInputSchema_RequestSyntax")**

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on
your behalf.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: No

**[S3Configuration](#API_DiscoverInputSchema_RequestSyntax "#API_DiscoverInputSchema_RequestSyntax")**

Specify this parameter to discover a schema from data in an Amazon S3 object.

Type: [S3Configuration](API_S3Configuration.md "API_S3Configuration.md") object

Required: No

## Response Syntax

```
{
   "InputSchema": {
      "RecordColumns": [
         {
            "Mapping": "***string***",
            "Name": "***string***",
            "SqlType": "***string***"
         }
      ],
      "RecordEncoding": "***string***",
      "RecordFormat": {
         "MappingParameters": {
            "CSVMappingParameters": {
               "RecordColumnDelimiter": "***string***",
               "RecordRowDelimiter": "***string***"
            },
            "JSONMappingParameters": {
               "RecordRowPath": "***string***"
            }
         },
         "RecordFormatType": "***string***"
      }
   },
   "ParsedInputRecords": [
      [ "***string***" ]
   ],
   "ProcessedInputRecords": [ "***string***" ],
   "RawInputRecords": [ "***string***" ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[InputSchema](#API_DiscoverInputSchema_ResponseSyntax "#API_DiscoverInputSchema_ResponseSyntax")**

Schema inferred from the streaming source. It identifies the format of the data in the
streaming source and how each data element maps to corresponding columns in the
in-application stream that you can create.

Type: [SourceSchema](API_SourceSchema.md "API_SourceSchema.md") object

**[ParsedInputRecords](#API_DiscoverInputSchema_ResponseSyntax "#API_DiscoverInputSchema_ResponseSyntax")**

An array of elements, where each element corresponds to a row in a stream record (a
stream record can have more than one row).

Type: Array of arrays of strings

**[ProcessedInputRecords](#API_DiscoverInputSchema_ResponseSyntax "#API_DiscoverInputSchema_ResponseSyntax")**

Stream data that was modified by the processor specified in the
`InputProcessingConfiguration` parameter.

Type: Array of strings

**[RawInputRecords](#API_DiscoverInputSchema_ResponseSyntax "#API_DiscoverInputSchema_ResponseSyntax")**

Raw stream data that was sampled to infer the schema.

Type: Array of strings

## Errors

**InvalidArgumentException**

Specified input parameter value is invalid.

**message**

HTTP Status Code: 400

**ResourceProvisionedThroughputExceededException**

Discovery failed to get a record from the streaming source because of the Amazon
Kinesis Streams ProvisionedThroughputExceededException. For more information, see [GetRecords](../../../kinesis/latest/APIReference/API_GetRecords.md "../../../kinesis/latest/APIReference/API_GetRecords.md") in the Amazon Kinesis Streams API Reference.

HTTP Status Code: 400

**ServiceUnavailableException**

The service is unavailable. Back off and retry the operation.

HTTP Status Code: 500

**UnableToDetectSchemaException**

Data format is not valid. Amazon Kinesis Analytics is not able to detect schema for
the given streaming source.

HTTP Status Code: 400

**UnsupportedOperationException**

The request was rejected because a specified parameter is not supported or a specified
resource is not valid for this operation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/cli2/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/boto3/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/DiscoverInputSchema.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/DiscoverInputSchema.md")
