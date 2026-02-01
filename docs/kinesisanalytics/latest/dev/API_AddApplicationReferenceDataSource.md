After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# AddApplicationReferenceDataSource

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Adds a reference data source to an existing application.

Amazon Kinesis Analytics reads reference data (that is, an Amazon S3 object) and
creates an in-application table within your application. In the request, you provide the
source (S3 bucket name and object key name), name of the in-application table to create,
and the necessary mapping information that describes how data in Amazon S3 object maps
to columns in the resulting in-application table.

For conceptual information, see [Configuring Application
Input](how-it-works-input.md "how-it-works-input.md"). For the limits on data sources you can add to your application, see
[Limits](limits.md "limits.md").

This operation requires permissions to perform the
`kinesisanalytics:AddApplicationOutput` action.

## Request Syntax

```
{
   "ApplicationName": "`string`",
   "CurrentApplicationVersionId": `number`,
   "ReferenceDataSource": {
      "ReferenceSchema": {
         "RecordColumns": [
            {
               "Mapping": "`string`",
               "Name": "`string`",
               "SqlType": "`string`"
            }
         ],
         "RecordEncoding": "`string`",
         "RecordFormat": {
            "MappingParameters": {
               "CSVMappingParameters": {
                  "RecordColumnDelimiter": "`string`",
                  "RecordRowDelimiter": "`string`"
               },
               "JSONMappingParameters": {
                  "RecordRowPath": "`string`"
               }
            },
            "RecordFormatType": "`string`"
         }
      },
      "S3ReferenceDataSource": {
         "BucketARN": "`string`",
         "FileKey": "`string`",
         "ReferenceRoleARN": "`string`"
      },
      "TableName": "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationName](#API_AddApplicationReferenceDataSource_RequestSyntax "#API_AddApplicationReferenceDataSource_RequestSyntax")**

Name of an existing application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

**[CurrentApplicationVersionId](#API_AddApplicationReferenceDataSource_RequestSyntax "#API_AddApplicationReferenceDataSource_RequestSyntax")**

Version of the application for which you are adding the reference data source. You can
use the [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md") operation to get the current application version. If
the version specified is not the current version, the
`ConcurrentModificationException` is returned.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 999999999.

Required: Yes

**[ReferenceDataSource](#API_AddApplicationReferenceDataSource_RequestSyntax "#API_AddApplicationReferenceDataSource_RequestSyntax")**

The reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis
Analytics reads the object and copies the data into the in-application table that is
created. You provide an S3 bucket, object key name, and the resulting in-application
table that is created. You must also provide an IAM role with the necessary permissions
that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your
behalf.

Type: [ReferenceDataSource](API_ReferenceDataSource.md "API_ReferenceDataSource.md") object

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**ConcurrentModificationException**

Exception thrown as a result of concurrent modification to an application. For
example, two individuals attempting to edit the same application at the same
time.

**message**

HTTP Status Code: 400

**InvalidArgumentException**

Specified input parameter value is invalid.

**message**

HTTP Status Code: 400

**ResourceInUseException**

Application is not available for this operation.

**message**

HTTP Status Code: 400

**ResourceNotFoundException**

Specified application can't be found.

**message**

HTTP Status Code: 400

**UnsupportedOperationException**

The request was rejected because a specified parameter is not supported or a specified
resource is not valid for this operation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/cli2/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/boto3/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/AddApplicationReferenceDataSource.md")
