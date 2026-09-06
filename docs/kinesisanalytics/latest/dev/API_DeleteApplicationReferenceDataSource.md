

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# DeleteApplicationReferenceDataSource
<a name="API_DeleteApplicationReferenceDataSource"></a>

**Note**  
This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see [Amazon Kinesis Data Analytics API V2 Documentation](/kinesisanalytics/latest/apiv2/Welcome.html).

Deletes a reference data source configuration from the specified application configuration.

If the application is running, Amazon Kinesis Analytics immediately removes the in-application table that you created using the [AddApplicationReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html) operation. 

This operation requires permissions to perform the `kinesisanalytics.DeleteApplicationReferenceDataSource` action.

## Request Syntax
<a name="API_DeleteApplicationReferenceDataSource_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "ReferenceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteApplicationReferenceDataSource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DeleteApplicationReferenceDataSource_RequestSyntax) **   <a name="analytics-DeleteApplicationReferenceDataSource-request-ApplicationName"></a>
Name of an existing application.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9_.-]+`   
Required: Yes

 ** [CurrentApplicationVersionId](#API_DeleteApplicationReferenceDataSource_RequestSyntax) **   <a name="analytics-DeleteApplicationReferenceDataSource-request-CurrentApplicationVersionId"></a>
Version of the application. You can use the [DescribeApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html) operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned.  
Type: Long  
Valid Range: Minimum value of 1. Maximum value of 999999999.  
Required: Yes

 ** [ReferenceId](#API_DeleteApplicationReferenceDataSource_RequestSyntax) **   <a name="analytics-DeleteApplicationReferenceDataSource-request-ReferenceId"></a>
ID of the reference data source. When you add a reference data source to your application using the [AddApplicationReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html), Amazon Kinesis Analytics assigns an ID. You can use the [DescribeApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html) operation to get the reference ID.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[a-zA-Z0-9_.-]+`   
Required: Yes

## Response Elements
<a name="API_DeleteApplicationReferenceDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteApplicationReferenceDataSource_Errors"></a>

 ** ConcurrentModificationException **   
Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.    
 ** message **   

HTTP Status Code: 400

 ** InvalidArgumentException **   
Specified input parameter value is invalid.    
 ** message **   

HTTP Status Code: 400

 ** ResourceInUseException **   
Application is not available for this operation.    
 ** message **   

HTTP Status Code: 400

 ** ResourceNotFoundException **   
Specified application can't be found.    
 ** message **   

HTTP Status Code: 400

 ** UnsupportedOperationException **   
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.   
HTTP Status Code: 400

## See Also
<a name="API_DeleteApplicationReferenceDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/DeleteApplicationReferenceDataSource) 