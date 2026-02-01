After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# ListApplications

###### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
which only supports SQL applications. Version 2 of the API supports SQL and Java
applications. For more information about version 2, see [Amazon Kinesis Data Analytics
API V2 Documentation](../apiv2/Welcome.md "../apiv2/Welcome.md").

Returns a list of Amazon Kinesis Analytics applications in your account. For each
application, the response includes the application name, Amazon Resource Name (ARN), and
status. If the response returns the `HasMoreApplications` value as true, you
can send another request by adding the `ExclusiveStartApplicationName` in the
request body, and set the value of this to the last application name from the previous
response.

If you want detailed information about a specific application, use [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md").

This operation requires permissions to perform the
`kinesisanalytics:ListApplications` action.

## Request Syntax

```
{
   "ExclusiveStartApplicationName": "`string`",
   "Limit": `number`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ExclusiveStartApplicationName](#API_ListApplications_RequestSyntax "#API_ListApplications_RequestSyntax")**

Name of the application to start the list with. When using pagination to retrieve the
list, you don't need to specify this parameter in the first request. However, in
subsequent requests, you add the last application name from the previous response to get
the next page of applications.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

**[Limit](#API_ListApplications_RequestSyntax "#API_ListApplications_RequestSyntax")**

Maximum number of applications to list.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 50.

Required: No

## Response Syntax

```
{
   "ApplicationSummaries": [
      {
         "ApplicationARN": "***string***",
         "ApplicationName": "***string***",
         "ApplicationStatus": "***string***"
      }
   ],
   "HasMoreApplications": ***boolean***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ApplicationSummaries](#API_ListApplications_ResponseSyntax "#API_ListApplications_ResponseSyntax")**

List of `ApplicationSummary` objects.

Type: Array of [ApplicationSummary](API_ApplicationSummary.md "API_ApplicationSummary.md") objects

**[HasMoreApplications](#API_ListApplications_ResponseSyntax "#API_ListApplications_ResponseSyntax")**

Returns true if there are more applications to retrieve.

Type: Boolean

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/cli2/kinesisanalytics-2015-08-14/ListApplications.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/DotNetSDKV4/kinesisanalytics-2015-08-14/ListApplications.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/ListApplications.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/SdkForGoV2/kinesisanalytics-2015-08-14/ListApplications.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ListApplications.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/ListApplications.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/SdkForKotlin/kinesisanalytics-2015-08-14/ListApplications.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/SdkForPHPV3/kinesisanalytics-2015-08-14/ListApplications.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/boto3/kinesisanalytics-2015-08-14/ListApplications.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ListApplications.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ListApplications.md")
